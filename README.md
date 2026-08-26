# 宣博乐｜个人学术网站

这是宣博乐（Bole Xuan）的个人学术网站源码，基于 [al-folio](https://github.com/alshedivat/al-folio) 构建。

网站地址：<https://xuan.land>（域名 DNS 生效后启用）
完整说明：[网站编辑与结构指南](docs/LOCAL_EDITING_GUIDE.md)

日常维护只需在 GitHub 网页编辑 `main` 分支；提交后，GitHub Actions 会自动发布网站。无需在 Windows 安装 Ruby、Jekyll、Docker 或其他开发环境。

## 直接编辑入口

| 想改什么                     | 直接打开编辑页                                                                            | 网页中的位置 |
| ---------------------------- | ----------------------------------------------------------------------------------------- | ------------ |
| 首页文案、研究简介、按钮文字 | [编辑首页](https://github.com/mohui373/Xuan/edit/main/_pages/about.md)                    | 首页         |
| 研究方向、研究问题、状态     | [编辑研究数据](https://github.com/mohui373/Xuan/edit/main/_data/research.yml)             | 首页、研究页 |
| 论文、在审手稿、研究计划     | [编辑论文列表](https://github.com/mohui373/Xuan/edit/main/_bibliography/papers.bib)       | 论文页       |
| 教育经历、技能、获奖、经历   | [编辑 CV 数据](https://github.com/mohui373/Xuan/edit/main/_data/cv.yml)                   | 简历页       |
| 开放项目总览                 | [编辑项目页](https://github.com/mohui373/Xuan/edit/main/_pages/projects.md)               | 项目页       |
| paper-to-paradigm 项目详情   | [编辑项目详情](https://github.com/mohui373/Xuan/edit/main/_projects/paper-to-paradigm.md) | 项目详情页   |
| GitHub、公开邮箱、ORCID、OSF | [编辑公开链接](https://github.com/mohui373/Xuan/edit/main/_data/socials.yml)              | 导航、搜索   |
| 英文版入口                   | [编辑英文页](https://github.com/mohui373/Xuan/edit/main/_pages/en.md)                     | EN           |
| 头像                         | [上传头像](https://github.com/mohui373/Xuan/upload/main/assets/img)                       | 首页         |
| 网站名称、域名、SEO          | [编辑站点配置](https://github.com/mohui373/Xuan/edit/main/_config_xuan.yml)               | 全站         |
| 视觉色彩与版式               | [编辑站点样式](https://github.com/mohui373/Xuan/edit/main/_sass/_site.scss)               | 全站         |

## 每次修改后的操作

1. 点击上表链接，修改内容。
2. 点击 **Commit changes**，直接提交到 `main`。
3. 打开 [Actions](https://github.com/mohui373/Xuan/actions)，等待 **Deploy site** 显示绿色勾。
4. 打开网站刷新查看。通常需要 1–3 分钟。

不要直接编辑 `gh-pages` 分支；它由 GitHub Actions 自动生成。

## 内容原则

- 只放可公开的邮箱、链接、经历和材料；不要上传未脱敏的 CV。
- 审稿中、准备中的论文不要填写未确认的期刊、DOI 或研究结果。
- ORCID、OSF、Google Scholar 等链接确认后再加入。
- 需要新增页面、修改结构或更换域名时，直接告诉 Codex。
