# RR-041：reader-facing-polish v0.1 隔离前向测试

- 记录日期：2026-08-28
- 被测 Skill：[reader-facing-polish v0.1](../.agents/skills/reader-facing-polish/SKILL.md)
- 实施计划：[RR-039](RR-039_PolishedDocs人类化成书实施计划.md)
- 案例候选：[RR-040](RR-040_公开案例组合与章节映射.md)
- 记录性质：编辑工作流隔离测试，不是章节候选、Evidence Receipt 或出版验收
- 当前状态：`accepted as bounded workflow test / W0 opened Chapter 12 and 17 logic gates / P0 not started`

## 1. 测试目标

v0.1 需要分别回答两个问题：

1. 当逻辑基线、案例或授权不足时，它是否会停止，而不是为了完成任务生成伪候选稿；
2. 当逻辑基线明确且测试被限定在仓库外时，它是否能实际生成 Reader-facing 文字，同时保持事实、对象、假设与案例边界。

两个测试均由独立只读／隔离 Worker 执行。Worker 不拥有 Beyond Code 正文或两个外部仓库的写权限；所有允许的测试写入只位于 `/tmp`。

## 2. Test A：第17章 Scope Gate

### 输入边界

- 请求：使用 Skill 将第17章派生为 Reader-facing 候选；
- 允许写入：`/tmp/reader-facing-polish-forward-test/`；
- 不允许：仓库写入、外部联网研究、Claim／Evidence／逻辑修改、两个外部仓库变更；
- 允许读取：当前第17章逻辑稿、RR-028、Claim Ledger 与 RR-040。

### Observable Result

- Skill 没有生成 `/tmp/reader-facing-polish-forward-test/第17章.md`；
- 没有修改 Beyond Code 或两个外部仓库；
- Scope Gate 识别出 `CLM-C17-001` 仍为 `unsupported / unreviewed / hold`，RR-028 仍把章节逻辑与措辞记为 `unreviewed`；
- RR-040 的 Anthropic Multi-agent Research 仍是 `unreviewed` 候选映射，没有被当成已接受正文材料。

### Disposition

`pass for blocking behavior`。

这不是“缺少 Receipt 所以不能写”，而是核心 Claim、对象粒度与章节逻辑尚未形成明确接受基线。Skill 正确把问题路由到主任务／Human，没有用语言优化替代逻辑裁决。

## 3. Test B：第23章隔离表达片段

### 输入边界

- 请求：生成约 1200–1800 个中文字符的非候选测试片段，覆盖开篇和一个 Case Episode；
- 允许写入：`/tmp/reader-facing-polish-prose-test/第23章_隔离测试片段.md`；
- 不允许：`PolishedDocs/` 写入、外部联网研究、新案例集成、Claim／Evidence／逻辑修改；
- 逻辑基线：RR-036 及第23章核心案例 Claim 已接受。

### Observable Result

- 生成文件共 1794 个字符，其中 1252 个汉字；
- SHA-256：`a4419270f955b4c896c71649252cca84bc8e18d1d319f820bd8c718aa5a642a0`；
- 文件只存在于 `/tmp`，未复制到仓库；
- 片段从“当时选定的 `18/18 PASS` 与 Human Aesthetic Signoff 仍打开”的冲突进入；
- 没有加入外部案例、虚构经历、效果数字、Claim ID、Receipt、Git 元数据或审计状态。

该 `/tmp` 文件是临时测试 Artifact，不在本仓库归档，也不是第23章候选稿。

## 4. 六类 Fidelity 结果

| 检查 | 结果 | 观察 |
|---|---|---|
| Source Fidelity | pass | `18/18 PASS` 被限定为当时选定检查；Visual Capture、Human Gate、四项 Follow-up、独立 qualifying run 与 Adoption／Production 边界均来自已接受材料 |
| Epistemic Fidelity | pass | “当时记录”“后来的决定”承载事实与同期处置，“回头看”承载事后推导；没有效果或单因果主张 |
| Model Fidelity | pass | Machine Check、Human Acceptance、Closure、Evidence Use、Supported Adoption 与 Production Release 未合并 |
| Hypothesis Fidelity | not applicable / pass | 片段未提出 Design Hypothesis，也未把候选方案写成已实现效果 |
| Case Role / Provenance Fidelity | pass | 两仓库被明确写为共享作者、方法与反馈链的 `longitudinal case`，没有伪装成独立复制验证 |
| Reader Fidelity | bounded pass | 先展示冲突，再承担术语；没有表格和定义清单；最终作者声音仍需 Human 判断 |

## 5. 测试推动的 Skill 修订

独立审阅与两个测试共同推动了以下修订：

- v0.1 明确为 Pilot，Phase 3 关闭前只用于第12、17、23章或单独授权的隔离评估；
- 必须能够定位显式接受的逻辑基线与主审记录，不能由执行者自行判断 `stable enough`；
- Scope Gate 阻断后停止无必要的深读，不创建 Canonical Candidate；
- 隔离评估明确优先写到仓库外，不能自动复制进 `PolishedDocs/`；
- 外部研究与正式 Evidence 永远离开 Polish Skill，由主任务独立完成并先更新逻辑／Evidence 层；
- Source Map 默认只在执行上下文维护，不自动落盘，也不构成 Evidence；
- Narrative Center 是开放候选，不强制所有章节复现同一判断运动；
- Design Hypothesis、External Case 与 Textbook Facility 改为条件字段；
- Canonical Schema 可以因模型精度和引用价值保留，不能只按正文是否重复删除；
- 第一方工程记录只直接支持“团队报告或记录了什么”，不自动证明底层行为、因果效果或普遍性；
- Voice Acceptance 只关闭声音审阅，不自动决定逻辑、Evidence 或出版状态。

## 6. 尚未验证

- 本隔离测试自身没有测试完整第23章的宏观重组与大规模压缩；该项随后进入单独的 Phase 3 Pilot；
- 没有测试第12章 Design Hypothesis，因为其章节基线仍需明确 Human 裁决；
- 没有测试外部案例正式集成；RR-040 后续只被接受为编辑候选地图，具名案例仍须逐章路由，第23章不新增平行外部案例；
- 没有测试第17章的实际写作，因为其核心 Claim 与章节逻辑仍在 hold；
- 没有证明 Skill 能稳定复制作者声音、改善可读性或适用于全书；这些仍依赖逐章 Human Review。

## 7. Phase 3 Readiness

| 章节 | 当前条件 | Readiness |
|---|---|---|
| 第12章 | 核心 Claim 已 narrow／accepted；RR-023 仍记章节逻辑与措辞 `unreviewed` | `needs Human baseline decision` |
| 第17章 | 核心 Claim `unsupported / unreviewed / hold`；章节逻辑未接受 | `blocked` |
| 第23章 | RR-036 与核心案例 Claim 已接受；隔离表达测试通过；Human 已授权并完成正式 Pilot | `full candidate drafted / independent fidelity passed / Human voice review pending` |

## 8. 当前建议

### 必要

1. Human 审阅第23章完整候选的声音与压缩损失；
2. 在启动第12章前，明确其当前逻辑稿能否作为接受基线；
3. 在启动第17章前，裁决其核心 Claim 与章节对象模型。

### 有用

1. 以第23章完整 Pilot 回看 Skill 是否在长案例章中产生压缩损失；
2. 第17章外部案例应保持 Transfer Test，重点比较任务独立性、共享状态与协调成本，不复述厂商效果数字。

### 可选

- 如需保留 `/tmp` 测试片段，另行授权将其作为测试 Fixture 或审阅附件归档；默认让临时 Artifact 随环境清理。

## 9. 2026-09-02 W0 State Reconciliation

第2节与第7节记录的是 2026-08-28 隔离测试当时的输入状态。Test A 因未获接受的第17章逻辑基线而停止，仍是有效的 Scope Gate 测试结果；W0 没有反向改写这段历史。

W0 提供了新的 Human 决策：第12章 Pilot 主轴已经接受；第17章 Claim 已收窄为 `unsupported / accepted / narrow`，高层检查关系作为 Design Hypothesis 接受，九个详细对象保持开放；第23章状态为 `VOICE_DEFERRED_FOR_CROSS_BOOK_REVIEW`。因此后续 Readiness 改为：

| 章节 | W0 后条件 | Readiness |
|---|---|---|
| 第12章 | Pilot 主轴、Source Baseline 与 Evidence 边界已接受；详细模块开放，尚无 Reader-facing 授权 | `ready for separately authorized P0 scope review` |
| 第17章 | 高层 Design Hypothesis 与窄 Claim 已接受；九对象展开开放，尚无 Reader-facing 授权 | `ready for separately authorized P0 falsification` |
| 第23章 | 完整候选与 Agent Fidelity 已完成；Human 当前无大问题 | `staged for cross-book review` |

这项变化来自 Human 对逻辑范围的裁决，不来自新的经验 Evidence。W0 没有启动 P0，也没有证明 Skill 已可扩散到全书。

## Human Disposition

- Status: `accepted as bounded workflow test`
- Test authorized by: Human author
- Test authorization at: 2026-08-28
- Human decision at: 2026-08-28
- Accepted scope: 接受 Skill v0.1、RR-040 编辑候选地图与本隔离测试结果，并授权第23章进入正式 Phase 3 Pilot
- W0 reconciliation at: 2026-09-02
- W0 effect: 第12／17章逻辑入口已关闭，但 P0 未启动
- Not decided: 第12／17章 Reader-facing 声音、第23章最终声音、Skill 全书扩散或出版状态
