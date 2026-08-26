# 宣博乐｜个人学术网站

这是宣博乐（Bole Xuan）的独立个人学术网站仓库，基于 [al-folio](https://github.com/alshedivat/al-folio) 构建。

## 网站定位

本仓库用于长期维护个人学术主页，主要服务于：

- 博士申请
- 研究方向展示
- 论文与在研项目展示
- 学术简历
- 开放研究与研究工具展示

正式维护仓库：`mohui373/Xuan`

计划站点地址：`https://mohui373.github.io/Xuan/`

今后只以 `main` 作为长期维护分支。旧仓库 `mohui373/mohui373.github.io` 仅作为历史参考，待新站稳定后可归档。

## 网站结构

第一版主要页面：

- 首页
- 研究
- 论文
- 项目
- 简历
- 英文版入口

当前先完成中文版，并为英文版保留独立结构。

## 当前研究主线

1. **受挫、说服与目标追求**  
   关注调剂相关挫折、自我说服、论点质量、信心、希望与目标承诺。

2. **社会规范与道德决策**  
   关注道德提醒、成就动机、作弊行为与规则遵从。

3. **AI、组织变革与员工行为**  
   当前进行中的研究方向，关注 AI 驱动裁员与传统裁员对幸存员工的不同影响，包括知识隐藏与工作态度等结果。

开放研究项目：[`paper-to-paradigm`](https://github.com/mohui373/paper-to-paradigm)

## 最常修改的文件

| 内容                     | 文件                               |
| ------------------------ | ---------------------------------- |
| 网站名称、简介与部署设置 | `_config.yml`、`_config_xuan.yml`  |
| 首页                     | `_pages/about.md`                  |
| 研究页面                 | `_pages/research.md`               |
| 三个研究方向的数据       | `_data/research.yml`               |
| 论文页面                 | `_pages/publications.md`           |
| 论文与手稿 BibTeX        | `_bibliography/papers.bib`         |
| 项目页面                 | `_pages/projects.md`、`_projects/` |
| CV 页面                  | `_pages/cv.md`                     |
| 教育、经历、技能与荣誉   | `_data/cv.yml`                     |
| 英文入口                 | `_pages/en.md`                     |
| 头像                     | `assets/img/profile-bole.jpg`      |

`reference/` 保存旧版学术主页的内容快照，仅用于核对和重新设计时参考。正式网页内容以根目录下的 `_pages/`、`_data/`、`_bibliography/` 和 `_projects/` 为准。

## 部署

网站通过 GitHub Actions 自动构建和发布。

日常维护流程：

1. 修改 `main` 分支中的内容；
2. commit 到 `main`；
3. GitHub Actions 自动运行 `Deploy site`；
4. 构建成功后更新 GitHub Pages。

构建时读取：

- `_config.yml`
- `_config_xuan.yml`

因此不要求日常在 Windows 本地安装 Ruby、Jekyll 或 Docker。

## 学术内容状态

统一使用以下状态：

- `Published`
- `Under Review`
- `In Preparation`
- `Ongoing Research`

不得为了完善页面而虚构：

- 投稿期刊
- DOI
- 预印本
- 样本量
- 实验结果
- 引用次数
- 未确认的奖项信息
- 未公开的研究设计

## 隐私原则

公开网页不展示：

- 手机号
- 出生日期
- 籍贯
- 家庭住址
- 未脱敏的完整个人材料

后续新增 Google Scholar、ORCID、OSF、CV PDF 等链接时，只使用已确认可公开的信息。

## 维护原则

这是个人长期学术主页，不是 al-folio 模板展示仓库，也不是科技产品官网。

后续修改优先保证：

- 学术事实准确
- 研究主线清晰
- 页面简洁易读
- 移动端可用
- 内容结构可持续维护
