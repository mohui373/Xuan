# 网站编辑与结构指南

这份指南对应 [mohui373/Xuan](https://github.com/mohui373/Xuan)。日常只需在 GitHub 网页编辑 `main` 分支，提交后 GitHub Actions 会自动更新网站。

## 网站由什么组成

```text
_config_xuan.yml                 全站名称、域名、SEO 与功能设置
_pages/
  about.md                       首页文案与模块顺序
  research.md                    研究页框架
  publications.md                论文页框架
  projects.md                    项目总览框架
  cv.md                          简历页框架
  en.md                          英文入口
_data/
  research.yml                   研究方向的可复用数据
  cv.yml                         教育、经历、学术交流、论文、技能、获奖
  en.yml                         英文版全部内容数据
  socials.yml                    公开邮箱与外部链接
_bibliography/papers.bib         论文与手稿
_projects/paper-to-paradigm.md   项目详情
assets/img/profile-bole.webp     首页头像
_sass/_site.scss                 自定义视觉风格
```

页面从数据文件读取内容：`_data/research.yml` 同时驱动首页与研究页；`_data/cv.yml` 驱动简历页；`papers.bib` 驱动论文页。因此同一项资料通常只需改一次。

## 逐项直接编辑

| 内容                       | 直接编辑                                                                                          | 修改提示                                                                                                |
| -------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| 首页姓名、简介、首页各模块 | [about.md](https://github.com/mohui373/Xuan/edit/main/_pages/about.md)                            | 修改文字即可；不要随意删掉 `{% for %}` 等 Liquid 标记。                                                 |
| 研究方向与状态             | [research.yml](https://github.com/mohui373/Xuan/edit/main/_data/research.yml)                     | 注意 YAML 缩进；每一层统一保留两个空格。                                                                |
| 论文与手稿                 | [papers.bib](https://github.com/mohui373/Xuan/edit/main/_bibliography/papers.bib)                 | 只填写已确认的作者、题目、状态和链接。                                                                  |
| CV、获奖与技能             | [cv.yml](https://github.com/mohui373/Xuan/edit/main/_data/cv.yml)                                 | 不放电话、地址、生日、身份证件等隐私。                                                                  |
| 项目总览                   | [projects.md](https://github.com/mohui373/Xuan/edit/main/_pages/projects.md)                      | 用于项目页引言与说明。                                                                                  |
| 项目详情                   | [paper-to-paradigm.md](https://github.com/mohui373/Xuan/edit/main/_projects/paper-to-paradigm.md) | 可增加背景、方法、链接与更新。                                                                          |
| 公开链接                   | [socials.yml](https://github.com/mohui373/Xuan/edit/main/_data/socials.yml)                       | 只加入已确认属于本人且可公开的链接。                                                                    |
| 英文版内容                 | [en.yml](https://github.com/mohui373/Xuan/edit/main/_data/en.yml)                                 | 与中文的研究状态、条目顺序、日期和公开链接同步。                                                        |
| 简历栏目与结构             | [cv.md](https://github.com/mohui373/Xuan/edit/main/_pages/cv.md)                                  | 改真实中文标题和栏目顺序；正文资料仍编辑 cv.yml。                                                       |
| 学术交流                   | [cv.yml](https://github.com/mohui373/Xuan/edit/main/_data/cv.yml)                                 | 编辑 Academic Presentations；英文同步 cv.presentations，不填未确认的报告题目。                          |
| 网站名称、域名、搜索与 SEO | [\_config_xuan.yml](https://github.com/mohui373/Xuan/edit/main/_config_xuan.yml)                  | 修改域名时需同时更新 GitHub Pages 设置。                                                                |
| 头像                       | [assets/img](https://github.com/mohui373/Xuan/tree/main/assets/img)                               | 点击 **Add file → Upload files**，使用实际页面引用的 profile-bole.webp；只上传 JPG 不会自动替换该头像。 |
| 配色与首页排版             | [\_site.scss](https://github.com/mohui373/Xuan/edit/main/_sass/_site.scss)                        | 这是高级设置；需要大幅改版时建议先告诉 Codex。                                                          |

## 提交与发布

1. 确认分支为 `main`。
2. 点击文件右上角铅笔图标，修改后点击 **Commit changes**。
3. 在 [Actions](https://github.com/mohui373/Xuan/actions) 中等待 **Deploy site** 变为绿色勾。
4. 刷新网站。部署通常在 1–3 分钟内完成。

`gh-pages` 是自动生成的发布分支，切勿手动编辑。

## 哪些材料仍待补充

- 已删除隐私信息的 CV PDF。
- 学术报告题目（可选；未确认前只展示已确认的会议名称、年份与口头报告形式）。

## 域名设置

当前网站地址为 <https://mohui373.github.io/Xuan/>。未来如需使用自定义域名，应同时修改 [\_config_xuan.yml](https://github.com/mohui373/Xuan/edit/main/_config_xuan.yml)、仓库根目录的 `CNAME` 文件，并在 GitHub Pages 设置中更新自定义域名；完成 DNS 设置后再启用 HTTPS。
