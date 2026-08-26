# 宣博乐｜个人学术网站

这是宣博乐（Bole Xuan）的独立个人学术网站源码，基于 [al-folio](https://github.com/alshedivat/al-folio) 构建。

- 正式维护仓库：`mohui373/Xuan`
- 计划站点地址：`https://mohui373.github.io/Xuan/`
- 当前用途：博士申请、研究展示、论文与开放研究项目展示

> 本仓库作为后续唯一维护的个人学术主页仓库。旧仓库 `mohui373/mohui373.github.io` 仅保留用于迁移核对，待新版稳定后可归档。

## 最常修改的文件

| 想修改什么 | 文件 |
| --- | --- |
| 网站名称、简介与站点设置 | `_config_xuan.yml` / `_config.yml` |
| 首页文字与版块 | `_pages/about.md` |
| 三个研究方向与研究状态 | `_data/research.yml` |
| 论文、手稿与发表状态 | `_bibliography/papers.bib` |
| 教育、经历、技能、获奖 | `_data/cv.yml` |
| 开源项目 | `_pages/projects.md`、`_projects/` |
| 英文页 | `_pages/en.md` |
| 头像 | `assets/img/profile-bole.jpg` |

## 部署方式

网站由 GitHub Actions 自动构建。

1. 在 `main` 分支修改并提交内容；
2. `Deploy site` workflow 自动执行；
3. 构建使用 `_config.yml` + `_config_xuan.yml`；
4. 成功后发布到 GitHub Pages 项目地址 `/Xuan/`。

日常内容更新不要求在本地安装 Ruby、Jekyll 或 Docker。

## 内容状态约定

- `Manuscript under review`：稿件审稿中。
- `Manuscript in preparation`：稿件准备中。
- `Ongoing Research`：研究进行中。
- 不虚构期刊、DOI、预印本、样本、结果或未公开链接。
- 不上传未脱敏 CV；电话、出生日期、籍贯和住址不进入公开网站。

## 当前研究主线

1. 受挫、说服与目标追求
2. 社会规范与道德决策
3. AI、组织变革与员工行为

开放研究项目：[`paper-to-paradigm`](https://github.com/mohui373/paper-to-paradigm)

## 迁移说明

`reference/` 保存旧站个人化内容的参考快照。新版页面应以根目录下的正式内容文件为准，后续可以重新设计，而不必机械复刻旧站视觉。
