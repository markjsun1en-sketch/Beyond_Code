# RR-025：第14章 Observability and Intervention 首轮回接说明

- 记录日期：2026-08-24
- 工作稿：[第14章 Observability and Intervention](../OptimizedDocs/第14章_Observability与Intervention_首轮修订稿.md)
- 原始结构：[全书大纲第14章](../OringinalDocs/beyond_code_ai_native_software_engineering_outline_zh.md)
- 新增材料：[Cognitive Control、Trust 与 Human Control Plane v0.1](../OringinalDocs/ai_native_cognitive_control_trust_human_control_plane_v0.1.md)
- 审阅依据：[RR-021](RR-021_Human_Control_Plane与认知控制架构审阅.md)
- 关联 Evidence：[CLM-C06-004](../Evidence/receipts/ER-20260818-002__CLM-C06-004.md)、[CLM-C12-001](../Evidence/receipts/ER-20260824-002__CLM-C12-001.md)、[CLM-OUTLINE-002](../Evidence/receipts/ER-20260818-001__CLM-OUTLINE-002.md)
- 记录性质：章节回接说明，不是新的 Evidence Receipt
- 章节对象模型与措辞状态：`unreviewed`

## 回接结果

第14章已经形成独立工作稿。

本章把 Operational Observability 收窄为：

> 通过有来源、有范围、有时效且可检查的外部记录，判断具名执行、状态变化、观察缺口和控制机制当前发生了什么的能力。

它只提供可检查信息，不自动形成正确诊断，不产生 Intervention Authority，也不证明未被观察的部分健康。

中心控制链被写成：

~~~text
Observation Question
→ Source and Coverage
→ Observation Record
→ Freshness and Integrity
→ Detector Evaluation
→ bounded Signal / Exception
→ Authority-bound Intervention
→ Effect Observation and Recovery
~~~

每一阶段都可以是 `partial`、`unknown`、`error` 或 `non-result`，不能由绿色 Dashboard 自动补全。

## 原大纲内容保留情况

| 原大纲主题 | 新工作稿落点 | 处理 |
|---|---|---|
| 观察 Goal、Plan、Step、Blocker、Tool、Risk、Cost、Context、Permission、Checkpoint | 14.3–14.4 | 保留；区分声明、可观察动作、结果与不可观察的内部认知 |
| Activity Timeline | 14.5 | 保留为 non-authoritative projection；增加并发、时间和因果边界 |
| State Dashboard | 14.16 | 保留为 Decision View；必须显示 Source、Coverage、Freshness、Detector Health 与 Unknown |
| Intervention Point | 14.18–14.21 | 保留；绑定 Authority，并拆开 Request、Apply、Effect 与 Recovery |
| Observability 不是日志堆积 | 14.1–14.3、14.6 | 扩展为 Observation Question、Contract 与 Coverage |

原大纲主体得到保留，但“显示更多日志就形成可观测性”“有按钮就可以干预”和“时间线反映完整因果历史”的潜在含义被撤回。

## 对象模型

工作稿分开：

1. Telemetry Event：Source 发出的原始或结构化事件；
2. Observation Record：在声明边界内实际得到的记录；
3. State Claim：对具名状态提出的可检验主张；
4. Evidence：用于支持或反对具名 Claim 的 Observation 或 Artifact；
5. Detector Evaluation：Detector 对绑定输入和条件完成的检查；
6. Detection Signal：匹配、未知或评估失败结果；
7. Exception Record：进入具名处置流程的偏离、风险或未知；
8. Intervention Record：有权主体请求、实施并验证的控制动作。

这些对象不会自动升级。Signal 不自动成为 Incident，Exception 不自动证明根因，Intervention Request 不自动证明控制效果。

## Observation Contract 与 Coverage

工作稿新增候选 Observation Contract，要求先声明：

- Decision Target 与 Observation Question；
- Subject、Action、Environment 与 Failure Mode；
- Source Identity；
- Included、Excluded、Partial 与 Unknown Surface；
- Event、Ingestion、Evaluation、Projection 与 Decision Time；
- Observer Integrity；
- Failure Semantics；
- Privacy、Retention 与 Redaction。

示例 YAML 是设计 Profile，不是通用 Schema。

Observation Coverage 被定义为问题相关的范围声明，而不是 Event 数量或统一百分比。低频、高影响 Blind Spot 不能被大量低风险 Event 稀释。

Unknown 被拆成 uninstrumented、source unavailable、stale、delayed、schema incompatible、detector error、sampled out、access denied、conflicting 与 not applicable，以便对应不同处置。

## Detector Health 与 Silence

Detector Health 被拆成：

- Source；
- Collection；
- Transport；
- Schema；
- Configuration Identity；
- Evaluation；
- Coverage Currency；
- Route；
- Effectiveness Evidence。

Heartbeat 和 Detector 自报 `healthy` 都不是充分证据。高影响 Detector 可以按风险选择 Synthetic Event、Replay、Independent Watchdog、Cross-source Reconciliation、Human Audit 或 Failure Injection。

`Silence should mean healthy` 没有进入工作稿。

替代表述是：

> 在仍适用的声明覆盖内，Source 满足 Freshness，具名 Detector Evaluation 已成功完成，Route Health 正常，并且没有检测到需要当前角色介入的具名条件。

`No Signal`、`Not Detected`、`Unknown` 与 `Not Applicable` 不得共用一个绿色状态。

## Exception 与 Intervention

Signal、Exception 和 Incident 被分开。Exception Lifecycle 只作为可删减的候选 Profile，不是通用状态机。

Severity、Urgency、Observation Confidence、Reachability、Irreversibility、Authority Boundary 和 Recovery Availability 不被压成单一 Risk Score。

Intervention Point 继承第13章 Authority：

- Pause 需要处理新动作与在途动作；
- 修改目标形成新的 Intent Revision；
- 缩小范围需要更新 Scope、Grant 或 Profile；
- 更换 Agent 形成新的 Subject Binding；
- Rollback 需要验证 Baseline 与外部副作用；
- 转人工需要真正 Takeover；
- 降低 Permission 不自动等同于 Authority Revocation；
- Replan 仍需满足原 Intent 与 Authority。

工作稿新增 Intervention Contract 示例，并区分 requested、authorized、dispatched、applied、effect observed、partial、non-result、recovered 与 unresolved。

## Evidence 回接边界

正文只使用已登记 Evidence 支持以下项目内边界：

- D-048 支持 Observer Integrity Failure 与 Target `non-result` 分开；
- D-048 同时反驳“缺少正常输出即可视为健康”；
- v4.94 Task Adapter 支持紧凑、只读、可下钻的 Task Projection 和部分控制路径；
- 现有实现没有证明完整 Observation Coverage、Detector Health、Takeover 或 Delegation Revocation 已经存在；
- D-073 至 D-075 支持把 meta-only successor、Proof Surface 增长和交付 Evidence 停滞作为 Process Warning。

这些 Evidence 不证明：

- 所有静默故障都可检测；
- 统一 Observability Platform 必要或有效；
- 本章 Detector Health 维度完整；
- Timeline 或 Dashboard 降低了 Human Judgment Load；
- 严格治理是 D-073 至 D-075 的唯一原因；
- 自动 Intervention 比直接 Human Review 更安全或高效。

## 有意不进入本章的内容

- Telemetry Volume 等于 Observability；
- Event 数量等于 Coverage；
- Activity Timeline 可以证明因果；
- 系统能够记录模型隐藏 Chain-of-thought；
- Context Access 表示模型已经理解 Context；
- Dashboard 成为新的 Truth Store；
- `No Alert = Healthy`；
- Detector 自报健康即可结束验证；
- Detector Error 被显示为 `not_detected`；
- Signal 自动升级为 Exception 或 Incident；
- Severity Score 自动扩大 Authority；
- 所有 Warning 都触发 Hard Stop；
- Alert 越少就证明 Workflow 越好；
- Pause Button 或 HTTP 200 证明执行已停止；
- Rollback Command 证明外部状态已恢复；
- 自动 Telemetry 可以替代 Human Rationale 与体验判断；
- 为了可观测性默认长期保存所有 Prompt、Payload 与 Secret；
- v4.94 已经实现完整 Observability and Intervention Plane。

## 与相邻章节的接口

- 第6章拥有 State Claim、Source、Applicability 与 Evidence Generation Integrity；
- 第9章拥有 Evidence Use、Coverage 与 Acceptance / Adoption / Release；
- 第12章拥有 Human-facing Projection 与 Decision Surface；
- 第13章拥有 Authority Grant、Autonomy Profile、Pause、Revoke 与 Takeover；
- 第14章拥有 Observation Contract、Coverage、Detector Evaluation、Exception Lifecycle 与 Intervention Effect；
- 第15章拥有 Memory Promotion、Conflict 与 Expiry；
- 第16章拥有 Workflow Candidate、Baseline、Calibration 与 Adoption。

第14章不把 Telemetry 自动提升为长期 Memory，也不根据指标自动宣称 Workflow Improved。

## 当前审阅点

本章对象模型和措辞尚未由作者单独裁决。下一轮应重点检查：

1. 八对象拆分是否过细，尤其 Signal 与 Exception 是否需要在正文中保持独立；
2. Observation Contract 与 Detector Evaluation YAML 是否适合正文，还是应移入附录；
3. Unknown 分类是否足够稳定，还是仅保留为诊断示例；
4. Detector Health 九个维度是否造成新的治理负担；
5. Exception Lifecycle 是否与现有 Incident Management 术语发生冲突；
6. Intervention Contract 与第13章 Revocation Contract 是否重复；
7. Privacy、Security 与 Cost 是否需要在第19、20章展开；
8. 核心命题“Absence of a signal is not evidence of global health”是否需要登记独立 Claim 并进行正式反证。

## Human Disposition

- 章节逻辑与措辞：`unreviewed`
- Decision by：pending
- Decision at：pending
- Rationale：关联 Claim 只支持本章中的部分边界；Observation、Detector、Exception 与 Intervention 的组合模型仍等待作者接受、收窄、拆分或撤回。
