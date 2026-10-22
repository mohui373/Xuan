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
    require(zh["number"] == en["number"], f"research number differs: {zh['slug']}")
    require(zh["status_key"] == en["status_key"], f"research status key differs: {zh['slug']}")
    localized_status = {
        "review": {"Under Review", "审稿中"},
        "preparation": {"In Preparation", "准备中", "稿件完善中"},
        "ongoing": {"Ongoing Research", "研究进行中"},
    }
    allowed_status = localized_status[zh["status_key"]]
    require(zh["status"] in allowed_status and en["status"] in allowed_status, f"research status label differs: {zh['slug']}")
    require(zh.get("osf_url") == en.get("osf_url"), f"OSF link differs: {zh['slug']}")
    if en.get("paper_title"):
        require(zh.get("paper_title") == en["paper_title"], f"paper title differs: {zh['slug']}")
    for field in ("design", "diagram", "findings"):
        require(len(zh.get(field, [])) == len(en.get(field, [])), f"research {field} counts differ: {zh['slug']}")
    require(bool(zh.get("limitations")) == bool(en.get("limitations")), f"research limitations differ: {zh['slug']}")
    for field in ("study_title", "findings", "limitations"):
        require(bool(zh.get(field)) and bool(en.get(field)), f"research section missing {field}: {zh['slug']}")

section_pairs = {
    "Education": "education",
    "Experience": "experience",
    "Projects": "projects",
    "Academic Presentations": "presentations",
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

def normalized_date(value):
    return str(value).replace("至今", "Present").replace("PRESENT", "Present")


for chinese_key, english_key in (("Education", "education"), ("Experience", "experience"), ("Projects", "projects")):
    for zh, en in zip(cv_zh[chinese_key], cv_en[english_key], strict=True):
        for field in ("date", "start_date", "end_date"):
            if field in zh or field in en:
                require(normalized_date(zh.get(field)) == normalized_date(en.get(field)), f"CV {field} differs: {chinese_key}")
                value = normalized_date(zh.get(field))
                require(value == "Present" or re.fullmatch(r"\d{4}(?:\.(?:0[1-9]|1[0-2]))?", value), f"CV date format differs: {value}")

for zh, en in zip(cv_zh["Academic Presentations"], cv_en["presentations"], strict=True):
    require(zh["title"] == en["original_title"], "conference name differs")
    require(str(zh["date"]) == str(en["date"]), "conference year differs")
    presentation_formats = {"口头报告": "Oral presentation", "海报报告": "Poster presentation", "参会": "Conference attendance"}
    require(presentation_formats.get(zh["format"]) == en["format"], "conference format differs")

require("summary" not in load_yaml("_data/cv.yml")["cv"] and "summary" not in cv_en, "CV summary was restored")
for zh, en in zip(cv_zh["Publications"][:3], cv_en["publications"][:3], strict=True):
    require("summary" not in zh and "note" not in en and "authors" not in en, "compact manuscript format differs")

chinese_cv_page = (ROOT / "_pages/cv.md").read_text(encoding="utf-8")
for anchor in ("contact-information", "education", "experience", "projects", "presentations", "publications", "skills", "open-source-projects", "awards", "languages"):
    require(re.search(rf'<h3\b[^>]*\bid="{anchor}"', chinese_cv_page), f"Chinese CV heading is missing #{anchor}")
    require(chinese_cv_page.count(f'id="{anchor}"') == 1, f"Chinese CV duplicates #{anchor}")
require("Professional Summary" not in chinese_cv_page, "CV summary heading was restored")

site_config = load_yaml("_config_xuan.yml")
require(load_yaml("_config.yml").get("middle_name") == "" and site_config.get("middle_name") == "", "template middle name was restored")
require("©" not in site_config["footer_text"] and "Copyright" not in site_config["footer_text"], "footer duplicates the theme copyright")
require("https://github.com/alshedivat/al-folio" in site_config["footer_text"], "footer is missing the al-folio attribution")

bibtex = (ROOT / "_bibliography/papers.bib").read_text(encoding="utf-8")
bib_count = len(re.findall(r"^@\w+\{", bibtex, flags=re.MULTILINE))
english_publication_count = sum(len(group["entries"]) for group in english["publications"])
require(bib_count == english_publication_count, "publication counts differ")

english_page = (ROOT / "_pages/en.md").read_text(encoding="utf-8")
for anchor in ("research", "publications", "projects", "cv"):
    require(f'id="{anchor}"' in english_page, f"English page is missing #{anchor}")

require("Coming Soon" not in english_page, "English page is still a placeholder")
print("Bilingual mirror structure is aligned.")

