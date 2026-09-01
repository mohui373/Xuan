# Bole Xuan | Personal Academic Website

[中文说明](README.md) | **English README**

This repository contains the source code for Bole Xuan's academic website, built with [al-folio](https://github.com/alshedivat/al-folio).

- Chinese site: <https://mohui373.github.io/Xuan/>
- English site: <https://mohui373.github.io/Xuan/en/>
- Bilingual maintenance: [Chinese–English Mirror Guide](docs/BILINGUAL_SYNC.md)

Routine updates can be made directly on the `main` branch through GitHub's web editor. GitHub Actions deploys the site after each content commit; no local Ruby, Jekyll, or Docker installation is required.

## Direct Editing Links

| Content                                                             | Direct editor                                                                               | Website location                       |
| ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | -------------------------------------- |
| All English profile, research, publication, project, and CV content | [Edit English data](https://github.com/mohui373/Xuan/edit/main/_data/en.yml)                | English site                           |
| English page structure and section order                            | [Edit English page](https://github.com/mohui373/Xuan/edit/main/_pages/en.md)                | English site                           |
| Chinese homepage                                                    | [Edit Chinese homepage](https://github.com/mohui373/Xuan/edit/main/_pages/about.md)         | Chinese homepage                       |
| Chinese research data                                               | [Edit Chinese research data](https://github.com/mohui373/Xuan/edit/main/_data/research.yml) | Chinese homepage and research page     |
| Chinese publications                                                | [Edit bibliography](https://github.com/mohui373/Xuan/edit/main/_bibliography/papers.bib)    | Chinese homepage and publications page |
| Chinese CV                                                          | [Edit Chinese CV](https://github.com/mohui373/Xuan/edit/main/_data/cv.yml)                  | Chinese CV page                        |
| Shared public links                                                 | [Edit social links](https://github.com/mohui373/Xuan/edit/main/_data/socials.yml)           | Navigation and search                  |
| Shared visual style                                                 | [Edit site style](https://github.com/mohui373/Xuan/edit/main/_sass/_site.scss)              | Both languages                         |

## Mirror Workflow

Chinese and English are maintained as a paired mirror:

1. When Chinese content changes, update the corresponding section in `_data/en.yml` in the same commit.
2. When English content introduces a factual change, update the paired Chinese source in the same commit.
3. Keep names, dates, links, research status, project roles, manuscript status, and item counts aligned.
4. Use natural academic English rather than literal translation, and do not add facts that are absent from the Chinese source.
5. Run `python test/bilingual_sync.py` before committing when working locally.

See [the full mapping table](docs/BILINGUAL_SYNC.md) for the exact Chinese–English file pairs.

## After Editing

1. Select **Commit changes** and commit directly to `main`.
2. Open [GitHub Actions](https://github.com/mohui373/Xuan/actions).
3. Wait for **Deploy site** to complete successfully.
4. Review both the [Chinese site](https://mohui373.github.io/Xuan/) and the [English site](https://mohui373.github.io/Xuan/en/).

If only `_sass/_site.scss` is changed, manually run [Deploy site](https://github.com/mohui373/Xuan/actions/workflows/deploy.yml) from the Actions page.

## Attribution and Copyright

- The site is based on the [al-folio](https://github.com/alshedivat/al-folio) template and customized under its [MIT License](LICENSE).
- al-folio was created by Maruan Al-Shedivat. This repository is an independent personal customization and is not an official al-folio repository.
- Bole Xuan retains rights to the personal academic writing, research descriptions, CV information, portrait, and original content. See the [Personal Content License](CONTENT_LICENSE.md).
