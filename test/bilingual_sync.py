"""Validate the structural alignment of the Chinese and English site mirrors."""

from pathlib import Path
import re

import yaml


ROOT = Path(__file__).resolve().parents[1]


def load_yaml(relative_path: str):
    return yaml.safe_load((ROOT / relative_path).read_text(encoding="utf-8"))


def require(condition: bool, message: str):
    if not condition:
        raise SystemExit(f"Bilingual sync check failed: {message}")


research_zh = load_yaml("_data/research.yml")["streams"]
research_en = load_yaml("_data/en.yml")["research"]["streams"]
cv_zh = load_yaml("_data/cv.yml")["cv"]["sections"]
english = load_yaml("_data/en.yml")
cv_en = english["cv"]

require(len(research_zh) == len(research_en), "research stream counts differ")
for zh, en in zip(research_zh, research_en, strict=True):
    require(zh["slug"] == en["slug"], f"research slug differs: {zh['slug']}")
    require(zh["status_key"] == en["status_key"], f"research status key differs: {zh['slug']}")
    require(zh["status"] == en["status"], f"research status differs: {zh['slug']}")
    require(zh.get("osf_url") == en.get("osf_url"), f"OSF link differs: {zh['slug']}")

section_pairs = {
    "Education": "education",
    "Experience": "experience",
    "Projects": "projects",
    "Publications": "publications",
    "Skills": "skills",
    "Open Source Projects": "open_source",
    "Awards": "honors",
    "Languages": "languages",
}

for chinese_key, english_key in section_pairs.items():
    require(
        len(cv_zh[chinese_key]) == len(cv_en[english_key]),
        f"CV item count differs for {chinese_key} / {english_key}",
    )

bibtex = (ROOT / "_bibliography/papers.bib").read_text(encoding="utf-8")
bib_count = len(re.findall(r"^@\w+\{", bibtex, flags=re.MULTILINE))
english_publication_count = sum(len(group["entries"]) for group in english["publications"])
require(bib_count == english_publication_count, "publication counts differ")

english_page = (ROOT / "_pages/en.md").read_text(encoding="utf-8")
for anchor in ("research", "publications", "projects", "cv"):
    require(f'id="{anchor}"' in english_page, f"English page is missing #{anchor}")

require("Coming Soon" not in english_page, "English page is still a placeholder")
print("Bilingual mirror structure is aligned.")

