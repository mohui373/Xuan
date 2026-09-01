# 中英文镜像维护指南 | Chinese–English Mirror Guide

本站以中文版为当前事实来源，并将英文版作为内容镜像。中英文文案不要求逐字翻译，但姓名、时间、研究状态、链接、项目角色、论文状态和条目数量必须一致。

The Chinese site is the current source of record, and the English site is its content mirror. The prose should read naturally in each language, while names, dates, research status, links, project roles, manuscript status, and item counts must remain aligned.

## 文件映射 | File Mapping

| 中文内容                                                | 英文镜像                                               | 同步范围                                       |
| ------------------------------------------------------- | ------------------------------------------------------ | ---------------------------------------------- |
| `_pages/about.md`                                       | `_data/en.yml` → `profile`, `core_question`, `methods` | 首页简介、关键词、核心问题、方法               |
| `_pages/research.md` + `_data/research.yml`             | `_data/en.yml` → `research`                            | 研究总述、三项研究、状态、设计、OSF            |
| `_pages/publications.md` + `_bibliography/papers.bib`   | `_data/en.yml` → `publications`                        | 论文分组、题目、作者、状态、OSF                |
| `_pages/projects.md` + `_projects/paper-to-paradigm.md` | `_data/en.yml` → `project`                             | 项目简介、Skills 与 GitHub 链接                |
| `_data/cv.yml`                                          | `_data/en.yml` → `cv`                                  | 教育、实践、科研项目、论文、技能、荣誉、语言   |
| `_data/socials.yml` + `_config_xuan.yml`                | `_pages/en.md`                                         | 邮箱、GitHub、ORCID 与站点身份                 |
| `_sass/_site.scss`                                      | 中英文共用                                             | 视觉样式无需翻译，但必须同时检查两种语言的排版 |

英文页面结构统一保存在 `_pages/en.md`，英文文案统一保存在 `_data/en.yml`。除页面结构调整外，日常英文内容更新应优先修改 `_data/en.yml`。

## 双向同步规则 | Bidirectional Sync Rules

1. 修改中文内容时，在同一次提交中检查并更新对应英文内容。
2. 修改英文内容时，反向检查对应中文来源；若英文修改包含新的事实、时间或状态，必须同步中文。
3. 研究状态、日期、OSF、ORCID、GitHub、论文题目和项目角色不得只更新一侧。
4. 英文采用自然的学术表达，不做生硬逐字翻译，也不补充中文版没有的新事实。
5. 提交前运行：

   ```bash
   python test/bilingual_sync.py
   npx prettier --check _pages/en.md _data/en.yml README.md docs/BILINGUAL_SYNC.md
   ```

6. 部署后同时检查：
   - 中文版：<https://mohui373.github.io/Xuan/>
   - English: <https://mohui373.github.io/Xuan/en/>

## 直接编辑 | Direct Editing

- [编辑英文内容数据](https://github.com/mohui373/Xuan/edit/main/_data/en.yml)
- [编辑英文页面结构](https://github.com/mohui373/Xuan/edit/main/_pages/en.md)
- [编辑中文首页](https://github.com/mohui373/Xuan/edit/main/_pages/about.md)
- [编辑中文研究数据](https://github.com/mohui373/Xuan/edit/main/_data/research.yml)
- [编辑中文 CV](https://github.com/mohui373/Xuan/edit/main/_data/cv.yml)
