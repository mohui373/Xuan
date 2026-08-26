# Xuan 学术网站编辑指南

本指南用于说明如何在 `mohui373/Xuan` 仓库中维护个人学术网站。

日常修改建议直接在 GitHub 网页完成，不需要在 Windows 本地安装 Ruby、Jekyll、MSYS2 或 Docker。

## 1. 首页

文件：`_pages/about.md`

主要用于修改：

- 姓名与身份介绍
- 研究简介
- 核心研究问题
- 首页展示的研究方向
- 首页项目介绍
- 方法与工具展示

如果只是调整文字，直接修改 Markdown / HTML 内容即可。

## 2. 研究方向

文件：`_data/research.yml`

主要用于维护三个研究方向及其状态。常见状态包括：

- `Under Review`
- `In Preparation`
- `Ongoing Research`

修改研究标题、研究问题、摘要或标签后，首页和研究页会读取这里的数据。

## 3. 论文与手稿

文件：`_bibliography/papers.bib`

用于维护：

- 已发表论文
- Under Review 手稿
- In Preparation 手稿

不要填写尚未确认的期刊、DOI、预印本链接或其他出版信息。

## 4. CV 内容

文件：`_data/cv.yml`

主要用于修改：

- 教育经历
- 研究经历
- 项目经历
- 方法技能
- 软件工具
- 奖项与学术活动

公开网页中不要写入手机号、出生日期、籍贯、家庭住址等私人信息。

## 5. 项目

项目列表页：`_pages/projects.md`

项目详情：`_projects/`

当前开放研究工具 `paper-to-paradigm` 的详情页位于 `_projects/` 中。

## 6. 公开链接

文件：`_data/socials.yml`

用于维护 GitHub、邮箱以及后续确认可公开的 ORCID、OSF、Google Scholar 等链接。

只添加已经确认属于本人且可以公开展示的链接。

## 7. 英文页面

文件：`_pages/en.md`

英文版本目前作为独立入口维护。后续内容完善时，应与中文版研究状态保持一致。

## 8. 头像

目标路径：`assets/img/profile-bole.jpg`

建议上传经过压缩的清晰头像，避免文件过大影响网页加载速度。

## 9. 网站配置

主要配置文件：

- `_config.yml`
- `_config_xuan.yml`

`_config_xuan.yml` 主要保存个人站点覆盖配置，包括：

- 姓名
- 中文站点简介
- GitHub Pages 地址
- `baseurl: /Xuan`
- 搜索、SEO 等个人设置

网站构建时会同时读取 `_config.yml` 与 `_config_xuan.yml`。

## 10. 在 GitHub 网页中修改

1. 打开 `mohui373/Xuan`。
2. 确认当前分支为 `main`。
3. 打开需要修改的文件。
4. 点击右上角铅笔图标 **Edit this file**。
5. 修改后点击 **Commit changes**。
6. 直接提交到 `main`。
7. 打开 **Actions** 页面查看 `Deploy site`。
8. 等待绿色勾出现后，再查看网页。

网站地址：`https://mohui373.github.io/Xuan/`

## 11. 发布分支说明

人工只维护 `main`。

`gh-pages` 是 GitHub Actions 自动生成的发布分支，不需要手动编辑。

## 12. 修改前的检查原则

每次更新研究或论文内容时，优先确认：

- 研究状态是否准确
- 作者顺序是否准确
- 论文题目是否为当前版本
- 是否误写未确认结果
- 是否包含不应公开的个人信息
- 中文版和英文版是否存在明显状态冲突

对于尚未确定的研究内容，宁可使用较宽泛的 `Ongoing Research` 描述，也不要提前写死理论、变量、样本或结果。
