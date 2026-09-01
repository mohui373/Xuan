# 宣博乐｜个人学术网站

这是宣博乐（Bole Xuan）的个人学术网站源码，基于 [al-folio](https://github.com/alshedivat/al-folio) 构建。

网站地址：<https://mohui373.github.io/Xuan/>
完整说明：[网站编辑与结构指南](docs/LOCAL_EDITING_GUIDE.md)

日常维护只需在 GitHub 网页编辑 `main` 分支；提交后，GitHub Actions 会自动发布网站。无需在 Windows 安装 Ruby、Jekyll、Docker 或其他开发环境。

## 直接编辑入口

| 想改什么                              | 直接打开编辑页                                                                            | 网页中的位置 |
| ------------------------------------- | ----------------------------------------------------------------------------------------- | ------------ |
| 首页文案、简介、按钮及首页档案链接    | [编辑首页](https://github.com/mohui373/Xuan/edit/main/_pages/about.md)                    | 首页         |
| 研究页标题与总介绍                    | [编辑研究页](https://github.com/mohui373/Xuan/edit/main/_pages/research.md)               | 研究页       |
| 具体研究方向、问题、状态及研究 OSF    | [编辑研究数据](https://github.com/mohui373/Xuan/edit/main/_data/research.yml)             | 首页、研究页 |
| 论文题目、作者及投稿状态              | [编辑论文数据](https://github.com/mohui373/Xuan/edit/main/_bibliography/papers.bib)       | 首页、论文页 |
| 论文页说明、分组及说服研究 OSF        | [编辑论文页](https://github.com/mohui373/Xuan/edit/main/_pages/publications.md)           | 论文页       |
| 教育、实践、项目、手稿、技能及荣誉    | [编辑 CV 数据](https://github.com/mohui373/Xuan/edit/main/_data/cv.yml)                   | 简历页       |
| 开放项目总览                          | [编辑项目页](https://github.com/mohui373/Xuan/edit/main/_pages/projects.md)               | 项目页       |
| paper-to-paradigm 项目详情            | [编辑项目详情](https://github.com/mohui373/Xuan/edit/main/_projects/paper-to-paradigm.md) | 项目详情页   |
| 导航和搜索中的公开邮箱、GitHub、ORCID | [编辑社交链接](https://github.com/mohui373/Xuan/edit/main/_data/socials.yml)              | 导航、搜索   |
| 英文版入口                            | [编辑英文页](https://github.com/mohui373/Xuan/edit/main/_pages/en.md)                     | EN           |
| 头像                                  | [上传头像](https://github.com/mohui373/Xuan/upload/main/assets/img)                       | 首页         |
| 网站名称、网址、SEO 与全站功能        | [编辑站点配置](https://github.com/mohui373/Xuan/edit/main/_config_xuan.yml)               | 全站         |
| 视觉色彩与版式                        | [编辑站点样式](https://github.com/mohui373/Xuan/edit/main/_sass/_site.scss)               | 全站         |

> 如果只修改站点样式 `_sass/_site.scss`，提交后请打开 [Actions](https://github.com/mohui373/Xuan/actions/workflows/deploy.yml)，选择 **Run workflow** 手动运行一次 `Deploy site`；其他上表内容提交后会自动发布。

## 每次修改后的操作

1. 点击上表链接，修改内容。
2. 点击 **Commit changes**，直接提交到 `main`。
3. 打开 [Actions](https://github.com/mohui373/Xuan/actions)，等待 **Deploy site** 显示绿色勾。
4. 打开网站刷新查看。通常需要 1–3 分钟。

不要直接编辑 `gh-pages` 分支；它由 GitHub Actions 自动生成。

## 来源、版权与贡献者

- 本站代码以 [al-folio](https://github.com/alshedivat/al-folio) GitHub 模板为基础，并依照其 [MIT License](LICENSE) 进行个性化修改与发布。
- 该模板由 Maruan Al-Shedivat 创建；本仓库不是 al-folio 官方仓库，也不代表原项目立场。
- 本站的个人学术文字、研究资料、简历信息、头像与原创内容由宣博乐（Bole Xuan）保留权利；未经明确许可，请勿转载、再发布或用于训练、商业推广等用途。详情见 [个人内容版权说明](CONTENT_LICENSE.md)。
- GitHub 的“Contributors”仅按 Git 提交统计。当前仓库的代码提交者为 `mohui373`；模板来源通过本节和 MIT 许可证明确署名。
