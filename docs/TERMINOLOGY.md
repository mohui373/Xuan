# 网站中英文术语表

维护范围：中英文研究介绍、研究页、论文列表和简历。修改术语时同步检查 `_data/research.yml`、`_data/en.yml`、`_data/cv.yml` 和 `_bibliography/papers.bib`。

## 受挫与自我说服

| 中文         | 网站统一用法                     | 使用边界                                                                        |
| ------------ | -------------------------------- | ------------------------------------------------------------------------------- |
| 受挫、挫折   | frustration                      | 标题按标题规则写 Frustration，正文使用 frustration，不再用 setback 指代这一构念 |
| 调剂相关挫折 | reassignment-related frustration | 根据作者 2026-10-29 的指定统一；不同版本原稿中的旧用词不自动修改                |
| 自我说服     | self-persuasion                  | 与他人说服条件区分                                                              |
| 他人说服     | other-persuasion                 | 不随意改为一般性的外部干预                                                      |
| 目标承诺     | goal commitment                  | 不与努力指标、留任意愿混称                                                      |
| 感知论点质量 | perceived argument quality       | 表示对理由的主观评价，不表示客观论证质量已经提高                                |
| 信心         | confidence                       | 研究中指任务相关信心，不直接改称自我效能感                                      |
| 希望         | hope                             | 与信心分开保留                                                                  |
| 工作热情     | work passion                     | 不改为工作投入或员工敬业度                                                      |
| 留任意愿     | retention intention              | 与实际长期留任行为区分                                                          |

## AI 裁员与员工反应

| 中文                 | 网站统一用法                             | 使用边界                                                                      |
| -------------------- | ---------------------------------------- | ----------------------------------------------------------------------------- |
| AI 知识蒸馏式裁员    | AI knowledge distillation-driven layoffs | “蒸馏”是经验编码与岗位替代的情境比喻，不指特定模型训练技术                    |
| 幸存者员工、留任员工 | layoff survivors                         | 指裁员后留下的员工                                                            |
| 政策道德评价         | moral evaluation of the layoff policy    | 明确评价对象，不等同于一般道德判断能力                                        |
| 组织信任             | organizational trust                     | 结合研究中对管理层的信任测量解释                                              |
| 工作不安全感         | job insecurity                           | 不改为已发生的失业                                                            |
| 工作知识心理所有权   | work-knowledge psychological ownership   | 保留知识对象，不简化为一般心理所有权                                          |
| 知识隐藏意向         | knowledge-hiding intentions              | 不能写成已经观察到的知识隐藏行为；正式论文标题保留作者给出的 Knowledge Hiding |

## 道德线索与作弊

| 中文         | 网站统一用法           | 使用边界                                               |
| ------------ | ---------------------- | ------------------------------------------------------ |
| 重复道德线索 | repeated moral cues    | 保留正式论文标题中的用词                               |
| 掩蔽道德提醒 | masked moral reminders | 方法介绍与预注册保持一致，不仅凭掩蔽程序宣称无意识加工 |
| 诚实谦卑     | Honesty-Humility       | 作为人格构念使用，统一大小写及连字符                   |
| 道德脱离     | moral disengagement    | 不与内疚或主观冲突混用                                 |
| 内疚         | guilt                  | 保留情绪构念名称                                       |
| 主观冲突     | subjective conflict    | 不自动改称认知失调                                     |

## 核对与维护

- 自我说服用词核对了 2026-05-07 稿与 2026-10-20 稿，其他术语参考 AI 裁员的 2026-10-28 稿和新作弊研究英文预注册。
- 正式题名属于书目信息。本次受挫用词按作者要求同步调整，后续应与最终投稿题名再次核对。
- 原有 `reassignment-setback` 页面锚点和文献键保留兼容，不是向读者展示的术语。
- 术语核对不自动更新样本量、研究状态、作者顺序或结论；这些事实需单独确认。
- 运行 `python test/bilingual_sync.py` 检查术语、论文题名与中英文状态是否一致。
