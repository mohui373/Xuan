# 宣博乐｜个人学术网站

这是宣博乐（Bole Xuan）的个人学术网站源码，基于 [al-folio](https://github.com/alshedivat/al-folio) 构建。

网站由 GitHub Actions 自动生成：在 `main` 分支修改并提交内容后，GitHub 会自动更新网页。日常编辑不需要在 Windows 安装 Ruby、Jekyll、MSYS2 或 Docker。

网站地址：`https://mohui373.github.io/Xuan/`

## 最常修改的文件

| 想修改什么               | 在 GitHub 中打开                   |
| ------------------------ | ---------------------------------- |
| 网站名称、简介、公开邮箱 | `_config.yml`、`_config_xuan.yml`  |
| 首页文字与版块           | `_pages/about.md`                  |
| 三个研究方向与研究状态   | `_data/research.yml`               |
| 论文、手稿与发表状态     | `_bibliography/papers.bib`         |
| 教育、经历、技能、获奖   | `_data/cv.yml`                     |
| 开源项目                 | `_pages/projects.md`、`_projects/` |
| GitHub、ORCID 等公开链接 | `_data/socials.yml`                |
| 英文页                   | `_pages/en.md`                     |
| 头像                     | `assets/img/profile-bole.jpg`      |

更完整的逐项说明见 [`docs/LOCAL_EDITING_GUIDE.md`](docs/LOCAL_EDITING_GUIDE.md)。

## 直接在 GitHub 网页修改

1. 打开要修改的文件。
2. 点击右上角铅笔图标 **Edit this file**。
3. 修改后点击 **Commit changes**。
4. 打开仓库的 **Actions** 页面，等待 `Deploy site` 显示绿色勾。
5. 网页通常会在几分钟内更新。

## 内容状态约定

- `Manuscript under review`：稿件审稿中。
- `Manuscript in preparation`：稿件准备中。
- `Ongoing Research`：研究进行中。
- 未正式公开的论文不填写虚构的期刊、DOI、预印本或 PDF 链接。
- 未脱敏 CV 不上传；电话、出生日期、籍贯和住址不写入公开仓库。

## 后续待补材料

- 准确的 ORCID iD 或 ORCID 主页链接。
- 可以公开的 OSF 个人主页或项目链接。
- 删除隐私信息后的 CV PDF。
- 完整英文版内容。
