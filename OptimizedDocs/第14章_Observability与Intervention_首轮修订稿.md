# 第14章 Observability and Intervention
## 可观测性不是日志堆积，干预也不是告警的自动后果

> 工作稿状态：首轮逻辑修订稿，不替代 [全书大纲](../OringinalDocs/beyond_code_ai_native_software_engineering_outline_zh.md) 或 [Cognitive Control、Trust 与 Human Control Plane v0.1](../OringinalDocs/ai_native_cognitive_control_trust_human_control_plane_v0.1.md)。
> 回接说明：[RR-025](../RevisedResult/RR-025_第14章Observability与Intervention首轮回接说明.md)。
> 适用边界：本章把 Observation、Detector、Signal、Exception 与 Intervention 分开建模；相关案例提供边界示例，不证明 Observation Contract、Detector Health 或 Exception Lifecycle 是通用最优实现。

第13章把自治定义为已有 Authority 下的可撤回委托配置。

但一项委托要真正可治理，至少还需要知道：

- 具名动作是否开始；
- 实际作用于哪个对象；
- 哪些状态发生变化；
- 哪些结果被观察；
- 哪些表面没有被观察；
- Detector 是否真的完成检查；
- 异常信号是否到达有权处置者；
- Pause、Rollback 或 Takeover 是否实际生效。

缺少这些信息时，bounded autonomy 可能只是一句 Policy 声明。

本章使用的工作定义是：

> **Operational Observability（运行可观测性：通过有来源、有范围、有时效且可检查的外部记录，判断具名执行、状态变化、观察缺口和控制机制当前发生了什么的能力）**。

这不是对控制理论或传统分布式系统 Observability 的重新定义，而是本书针对受托执行系统使用的工程范围。

Observability 只提供可检查信息。

它不会自动形成正确诊断，不会授予 Intervention Authority，也不会证明未被观察的部分健康。

---

# 14.1 先区分必要、有效与可选

“Agent 需要 Observability”仍然过于宽泛。

需要分三层判断。

## 必要条件

只要系统允许 Agent 对持久状态、外部系统或后续决策产生影响，项目就需要某种方式确认：

- 动作目标；
- 动作边界；
- 动作是否发生；
- 已知结果或 `non-result`；
- Stop 与 Recovery 是否可验证。

这可以是很小的记录，不要求中央 Telemetry Platform。

## 有用能力

当任务长期运行、并发、多 Agent、异步或跨工具时，结构化 Event、Coverage、Detector 和 Exception Record 通常更有用，因为直接观察已经难以维持。

## 可选实现

统一 Dashboard、完整 Activity Timeline、集中式指标平台、异常预测和自动干预都是实现选择，不是 AI-native 工程的定义门槛。

对一次性、同步、低风险且 Human 全程直接检查的任务，简单命令输出和 Diff 可能已经足够。

判断标准不是“是否拥有 Dashboard”，而是：

> 对当前 Decision Target，系统是否能说明观察了什么、没有观察什么、记录是否仍新鲜，以及谁可以根据这些信息采取什么动作？

---

# 14.2 八个对象不能合并

本章区分八个经常被压成“日志”或“告警”的对象。

| 对象 | 回答的问题 | 不自动等于 |
|---|---|---|
| Telemetry Event | 哪个 Source 发出了什么原始或结构化事件 | 真实世界完整状态 |
| Observation Record | 在什么边界内实际记录了什么 | 对原因的解释 |
| State Claim | 当前对某个状态提出什么可检验主张 | 已经被接受的事实 |
| Evidence | 哪些 Observation 或 Artifact 被用于支持或反对哪个 Claim | Decision |
| Detector Evaluation | 哪个 Detector 用哪些输入检查了什么条件 | Detector 有效性 |
| Detection Signal | 某个具名条件匹配、未知或评估失败 | 已确认 Exception 或 Incident |
| Exception Record | 哪个偏离、风险或未知被路由进入处置流程 | 根因已知 |
| Intervention Record | 哪个有权主体要求、执行并验证了什么控制动作 | 目标效果已经实现 |

**Telemetry Event（遥测事件：由具名 Source 在具名时间发出的原始或结构化运行记录）** 可以来自 Tool、Agent Harness、Runtime、Gate、Repository、Queue 或 Human 操作。

**Observation Record（观察记录：在声明 Subject、Scope、采集方法和时间边界内得到的可检查记录）** 表示实际看到了什么。

**Detector Evaluation（检测器评估：具名 Detector 版本对绑定输入和条件完成的一次可追溯检查）** 需要记录输入、结果和自身运行状态。

**Detection Signal（检测信号：Detector 对具名条件给出的匹配、未知或评估失败结果）** 只是路由输入。

**Exception Record（异常记录：把某个偏离、风险、未知或控制失败纳入具名处置流程的记录）** 还需要 Triage、Owner、Authority 与 Disposition。

**Intervention Record（干预记录：有权主体为改变执行或风险状态而请求、实施并验证某项控制动作的记录）** 必须把“要求动作”与“动作生效”分开。

State Claim 与 Evidence 的正式所有权仍在第6章和第9章。本章只说明它们怎样由运行观察产生、怎样触发处置。

对象之间可能形成：

~~~text
Telemetry Source
→ Telemetry Event
→ bounded Observation Record
→ supports or challenges a State Claim
→ may become Evidence for a named use

Observation Records
+ Detector Configuration
→ Detector Evaluation
→ matched / not_detected / unknown / error
→ optional Signal and Exception routing

Exception Disposition
+ Authority Grant
→ Intervention Request
→ execution observation
→ effect verification / recovery / unresolved
~~~

这不是自动状态机。

一个 Human 可以直接根据 Observation 建立 Exception；一个 Signal 也可能被判定为 Duplicate、Expected Change 或 False Positive。

---

# 14.3 Observation Contract 先声明观察问题

收集更多数据不是起点。

起点是：

> 为哪个 Decision Target，需要观察哪个 Subject 的哪些行为或状态？

一个 **Observation Contract（观察契约：声明观察问题、来源、覆盖、时效、完整性、隐私和失败语义的版本化约束）** 可以是：

~~~yaml
observation_contract_id: OBS-CONTRACT-014
version: 2
decision_targets:
  - delegated_task_health
  - intervention_readiness

subjects:
  - task_execution
  - bound_worktree
  - test_harness
  - authority_usage

questions:
  - did_the_named_action_start
  - which_subject_was_actually_observed
  - did_state_change_outside_scope
  - was_required_evidence_produced
  - can_execution_be_paused_and_recovered

sources:
  - task_event_stream
  - tool_call_receipts
  - repository_snapshot
  - test_result_receipts
  - control_action_receipts

coverage:
  included:
    - local_worktree_actions
    - bounded_test_process
  excluded:
    - model_internal_reasoning
    - uninstrumented_external_side_effects

time:
  event_time_required: true
  ingestion_time_required: true
  maximum_decision_age: 10m

integrity:
  observer_version_required: true
  source_identity_required: true
  target_mutation_policy: fail_closed

failure_semantics:
  missing_source: unknown
  detector_error: unknown
  target_not_reached: non_result

privacy:
  secret_payload_capture: prohibited
  retention: 30d
~~~

这是设计 Profile，不是通用 Schema。

一个低风险工具可能只需要几项字段；一个生产迁移需要更严格的身份、时间、数据和恢复记录。

---

# 14.4 观察声明、动作与结果，不声称读取隐藏认知

原大纲建议观察当前目标、计划、已完成步骤、阻塞、工具调用、风险、成本、Context、Permission 与 Checkpoint。

这些对象需要进一步区分。

| 观察面 | 可以记录 | 不能仅凭记录断言 |
|---|---|---|
| Goal / Intent | 具名 Intent Artifact、版本、Scope | Agent 真正“想要什么” |
| Plan | 已提交的 Plan、修订和当前 Step | 内部推理完整过程 |
| Tool Action | 请求、参数边界、权限、开始和结果 | 工具产生的所有外部副作用都已覆盖 |
| State Change | Diff、Commit、Snapshot、Queue 状态 | 变化一定正确或被接受 |
| Context Access | 可观察的读取、检索和引用记录 | 模型注意、理解或使用了全部 Context |
| Risk | 具名 Risk Claim、触发条件、Owner | 一个分数代表真实总体风险 |
| Cost | 可获得的 Token、Runtime、API、Review 数据 | 所有认知与机会成本都被计量 |
| Checkpoint | 创建、确认、恢复尝试和状态 | Checkpoint 一定可恢复 |
| Authority Use | Grant 引用、Action Class、Decision Target | 有 Permission 就有 Authority |
| Human / Gate Decision | 选项、Authority、Disposition、理由 | 决定是客观 Truth |

对于 Codex 或其他 Agent Task，本书只把可见消息、Tool Activity、Output、Artifact 和 File Change 当作过程证据。

Plan 与 Explanation 可以记录为 Agent 的显式表达，不能被称为隐藏 Chain-of-thought 的完整读取。

---

# 14.5 Activity Timeline 是投影，不是完整因果历史

**Activity Timeline（活动时间线：把有来源的执行事件与已记录关系组织成可下钻时间视图的投影）** 可以帮助 Human 理解任务进展。

原大纲的时间线：

~~~text
Goal Received
→ Context Loaded
→ Plan Approved
→ Files Modified
→ Test Failed
→ Plan Revised
→ Evidence Collected
→ Awaiting Human Decision
~~~

适合作为 Human-facing View，但需要三个限制。

## 时间顺序不等于因果关系

`Test Failed` 出现在 `Files Modified` 之后，不证明该修改导致失败。环境、Baseline、并发变化或测试缺陷都可能解释结果。

## 并发执行不是单线故事

多个 Agent、Tool、Queue 和 Human Decision 形成部分顺序。Timeline 需要保留：

- Event ID；
- Parent / Correlation ID；
- Subject；
- Candidate 与 Baseline；
- Event Time；
- Ingestion Time；
- Source；
- Scope；
- Uncertainty。

## View 不拥有原始记录

Timeline 可以压缩事件，但必须能下钻到 Source。否则它会成为一套容易过期的竞争状态。

因此更准确的表达是：

> Activity Timeline 是对有来源事件和已记录关系的可读投影，不是系统完整发生史，也不是因果证明。

---

# 14.6 Observation Coverage 是范围声明，不是装饰性百分比

**Observation Coverage（观察覆盖：当前采集和检查机制声明能够观察哪些 Subject、Action、State、Failure Mode、Environment 与时间窗口，以及明确不能观察什么）** 必须绑定问题。

例如：

| 观察问题 | Covered | Partial | Unobserved |
|---|---|---|---|
| 本地 Worktree 文件变化 | Git Snapshot 与 Diff | 未跟踪的临时文件 | 外部挂载目录 |
| Tool 调用是否返回 | Tool Receipt | 子进程后续动作 | 未接入的外部服务 |
| 测试目标是否运行 | Harness Receipt | 部分 Shard | 未启动的目标场景 |
| Authority 使用 | Grant Ref 与 Action Log | 语义 Scope 需复核 | 绕过平台的外部动作 |
| Human Attention Route | Queue 与 Acknowledge | 读取不等于理解 | 线下沟通 |

异质 Coverage 不宜轻率压成 `87% observed`。

百分比可能掩盖一个低频但高影响的未观察表面。

Coverage Record 至少应说明：

- Observation Question；
- Subject 与 Environment；
- Included / Excluded Surface；
- Collection Method；
- Failure Mode；
- Time Window；
- Last Successful Observation；
- Known Blind Spot；
- Owner 与 Review Date。

Coverage 不是“观察了很多”，而是“对这个问题，哪些部分有记录、哪些部分没有”。

---

# 14.7 Unknown 需要按来源拆开

`unknown` 不是一个统一故障。

至少可以区分：

| Unknown 类型 | 含义 | 候选响应 |
|---|---|---|
| uninstrumented | 当前没有采集机制 | 限制 Claim、补采集或收窄 Scope |
| source_unavailable | Source 当前不可达 | 重试、切换 Source、Pause |
| stale | 有记录，但超过当前 Decision 的时效边界 | 重新观察 |
| delayed | 事件可能仍在传输或排队 | 等待 Watermark 或标记 provisional |
| schema_incompatible | Source 与 Consumer 版本不兼容 | 隔离、迁移或更新 Detector |
| detector_error | Detector 没有完成有效评估 | 记录 unknown，不能写 not_detected |
| sampled_out | 采样策略没有保留该事件 | 不对未采样表面作全量 Claim |
| access_denied | 当前主体无权读取 | 请求有权路径或保留未知 |
| conflicting | 多个 Source 给出不一致观察 | 暂停合并结论并请求裁决 |
| not_applicable | 该问题对当前 Scope 不适用 | 明确记录理由，不计作成功 |

不同 Unknown 对应不同恢复方式。

把所有缺失都显示为灰色 N/A，会删除最重要的诊断信息。

---

# 14.8 Freshness 需要多个时间

**Freshness（时效适用性：某条 Observation 对当前 Decision Target 是否仍足够新鲜）** 不是文件最后修改时间的同义词。

至少要区分：

~~~text
event_time       目标事件何时发生
observed_at      Source 何时完成观察
ingested_at      记录何时进入当前系统
evaluated_at     Detector 何时处理
projected_at     Dashboard / Brief 何时生成
decision_at      有权处置何时发生
~~~

一条昨晚的测试结果，对今天未变化的纯函数 Candidate 可能仍适用；对持续变化的生产状态可能已经失效。

Freshness 需要绑定：

- Decision Target；
- Subject / Build / Environment Identity；
- 可能使 Observation 失效的 Dependency；
- 最大可接受 Age；
- Event-time Watermark 或完整性条件。

“刚刚生成的 Dashboard”不表示其中 Source 都是新的。

---

# 14.9 Observer Integrity 与 Target Result 必须分开

**Observer Integrity（观察器完整性：采集或验证机制是否在声明边界内运行，并保持被观察对象、输入和解释边界可识别）** 是 Observation 的前提之一。

它不等于 Observer 没有任何副作用。

已声明、隔离且不改变目标身份或 Authority Surface 的正常输出，可以是有效采集的一部分。

需要警惕的是：

- Observer 在观察前改变 Target；
- 采集代码改变具有 Authority 意义的 Inventory；
- Instrumentation 改变时序或资源条件；
- Observer 失败后仍沿用旧结果；
- 采集失败被显示为目标 FAIL；
- Partial Observation 被提升为完整 Coverage。

D-048 提供了一个直接边界案例，证据见 [Target `non-result` 案例记录](../Evidence/receipts/ER-20260818-002__CLM-C06-004.md)。

当 Launcher 在目标 Compile 前改变自身 exact inventory，第二次检查 fail closed 时，应分开记录：

~~~text
observer_integrity = failed
target_observation = not_reached
target_result = non-result
~~~

不能写成：

~~~text
target_compile = failed
~~~

因为目标根本没有被观察。

这项案例不证明所有 Observer 必须完全无副作用，也不证明所有静默故障都可检测。

---

# 14.10 Detector Health 不是一个绿色圆点

**Detector Health（检测器健康：现有 Evidence 对具名数据路径、Detector 配置、评估执行和信号路由是否按声明工作所支持的当前判断）** 至少包含多个维度：

| 维度 | 要检查的问题 |
|---|---|
| Source Health | Source 是否可达，Identity 是否正确 |
| Collection Health | 采集是否运行，是否发生丢弃或权限失败 |
| Transport Health | Event 是否积压、乱序或丢失 |
| Schema Health | Source 与 Detector 是否版本兼容 |
| Configuration Identity | 实际运行的是哪个 Rule、Model、Threshold 与 Suppression Policy |
| Evaluation Health | Evaluation 是否开始、完成或报错 |
| Coverage Currency | Coverage 声明是否仍适用于当前 Subject 与 Environment |
| Route Health | Signal 是否到达预定 Queue、Gate 或 Human |
| Effectiveness Evidence | Detector 是否通过注入、回放、事故或抽样验证发现目标条件 |

Heartbeat 只能支持进程仍在响应，不能证明：

- 输入完整；
- Rule 正确；
- Schema 未漂移；
- Alert Route 可达；
- Detector 能识别目标 Failure Mode。

同样，Detector 自己报告 healthy 不能构成充分自证。

高影响 Detector 可以使用：

- 独立 Watchdog；
- Synthetic Event；
- Recorded Replay；
- Cross-source Reconciliation；
- Human Random Audit；
- Failure Injection；
- Route Acknowledgement。

不同机制发现不同故障，不需要全部部署。

---

# 14.11 Silence 只能表示有边界的 Non-detection

本章所说的 **Non-detection（未检测到：具名 Detector 在绑定输入和有效评估边界内没有匹配目标条件）** 不是“系统没有问题”的同义词。

没有告警可能意味着：

~~~text
named condition did not occur
condition occurred outside coverage
source became stale
event was delayed or sampled out
detector evaluation failed
suppression policy hid the signal
routing failed
queue was not acknowledged
~~~

所以 `SYSTEM STABLE` 不是一个可以从空队列直接推出的全局结论。

可辩护的表达是：

> 在已声明且仍适用的 Observation Coverage 内，Source 满足 Freshness，具名 Detector Evaluation 已成功完成，Route Health 正常，并且没有检测到需要当前角色介入的具名条件。

如果界面需要更短的文本，可以显示：

~~~text
No routed exception for this decision scope.
Coverage: declared
Freshness: within policy
Detector evaluation: completed
Known blind spots: 2
~~~

短文本后仍需保留下钻。

`No Signal`、`Not Detected`、`Unknown` 和 `Not Applicable` 不能显示成同一个绿色状态。

---

# 14.12 Detector 输出不是根因，也不是 Decision

一个 Detector 可能发现：

- 超时；
- 越权 Action 请求或可观察动作；
- Evidence 缺失；
- Scope 增长；
- Error Rate 变化；
- 未确认的 Human Queue；
- Observer Integrity Failure。

这些都是具名条件的检测结果。

它们不自动证明：

- 根因是什么；
- 影响有多大；
- 当前 Candidate 应被拒绝；
- Workflow 必须改变；
- Human 存在过错；
- 应该执行哪一种 Recovery。

因此 Detector Evaluation 应保留：

~~~yaml
evaluation_id: DET-EVAL-901
detector_id: DET-AUTH-SCOPE
detector_version: 4
configuration_digest: sha256:example
coverage_ref: COVERAGE-014
input_watermark: EVT-2048
started_at: 2026-08-24T10:01:00+08:00
completed_at: 2026-08-24T10:01:02+08:00
result: matched
matched_condition: write_outside_granted_scope
observation_refs:
  - OBS-4401
health_basis:
  - source_current
  - schema_compatible
  - route_acknowledged
limitations:
  - external_mount_not_observed
~~~

这是审计 Profile，不是所有 Detector 的强制字段。

---

# 14.13 Signal、Exception 与 Incident 是不同处置层

可以采用以下语义。

## Signal

Detector 或 Human 提交的候选异常输入。

## Exception

Signal 经 Policy 或 Triage 进入具名处置流程，或 Human 直接建立需要处置的偏离记录。

## Incident（事故事件：已经造成或可能造成具名损害、需要独立调查与恢复处置的事件记录）

它可以处于已确认或仍在调查状态，需要独立的影响、时间线、处置与恢复记录。

三者不构成必然阶梯。

例如：

- 一个 Signal 可以是 Expected Change；
- 一个 Exception 可以在没有损害时通过 Forward Correction 关闭；
- 一个 Incident 可以由 Human 发现，而没有任何自动 Signal；
- 多个 Signal 可以对应同一 Incident；
- 一个 Detector Error 本身也可能成为 Control Exception。

`severity: critical` 不会自动把 Signal 变成事实。

---

# 14.14 Exception Lifecycle 必须保留未知与责任

候选 Lifecycle 可以是：

~~~text
raised
→ triaged
→ acknowledged
→ dispositioned
→ intervention_requested
→ intervention_applied / non-result
→ effect_verified / unresolved / forward_recovery
→ closed / superseded
~~~

这不是通用状态机。

每个项目需要根据风险和工具能力删减。

Exception Record 至少要回答：

- 由哪个 Signal、Observation 或 Human 提交；
- 影响哪个 Subject、Scope 与 Decision Target；
- 当前可观察事实；
- 当前推导与替代解释；
- Coverage、Freshness 与 Detector Health；
- Severity 与 Urgency 由谁判断；
- 当前 Owner；
- 当前 Authority；
- 可用动作与 Non-effect；
- Deadline / Expiry；
- 关闭条件；
- Counterevidence 与未解决 Unknown。

关闭 Exception 不等于修复根因。

它可能表示：

- 误报；
- 风险被接受；
- 当前 Scope 不适用；
- 已建立新的 Owner；
- 临时限制已生效；
- 问题转为 Incident 或 Workflow Candidate；
- Evidence 仍不足但任务已终止。

Disposition 必须说明是哪一种。

---

# 14.15 Severity、Urgency 与 Authority 不应压成单一分数

异常路由至少涉及：

~~~text
impact
reachability
irreversibility
time sensitivity
observation confidence
affected authority boundary
recovery availability
current exposure
~~~

高影响但不可达的问题，可能适合计划修复。

中等影响但正在持续写入错误状态的问题，可能需要立即 Pause。

低 Evidence Confidence 不代表低风险；它可能要求缩小 Claim、收窄 Scope 或请求独立 Observation。

一个统一 `risk = 83` 无法表达这些差异。

更重要的是，Severity 不产生 Authority。

Detector 可以把 Exception 路由给有权主体；除非已有明确 Grant 与 Policy Mapping，否则它不能因为分数很高就自行扩大 Intervention。

---

# 14.16 State Dashboard 是 Decision View，不是全量状态仓库

原大纲希望人类快速知道：

- 哪些任务正在运行；
- 哪些等待批准；
- 哪些出现异常；
- 哪些产生高风险变化；
- 哪些 Agent 长时间无进展；
- 哪些任务超出预算。

这些需求可以保留，但 Dashboard 必须显示其语义边界。

一个 Decision View 至少需要：

- Decision Target；
- Subject、Candidate 与 Baseline；
- Current State Claim；
- Source Link；
- Coverage 与 Blind Spot；
- Freshness；
- Detector Health；
- Exception 与 Unknown；
- Available Action；
- Authority Reference；
- Last Intervention 与 Effect Status。

`running`、`blocked`、`awaiting approval` 和 `over budget` 不能只靠颜色表达。每个状态需要来源、时间和判定规则。

Dashboard 生成失败或陈旧时，应显示 Projection Failure，而不是继续展示上次的绿色状态。

第12章的 Human Control Plane 可以投影这些信息，但不拥有它们。

---

# 14.17 Exception Routing 的目标不是 Alert 数量最少

**Exception Routing（异常路由：把第12章 Attention Routing 应用于运行时 Exception，根据 Decision Target、风险、时效、Authority 和当前认知负担，将异常送达适合处置者的过程）** 不是新的 Attention 上位对象，也不是简单去重。

需要同时考虑：

- 谁拥有所需 Authority；
- 谁理解相关 Domain；
- 当前是否存在职责冲突；
- Exception 的 Deadline；
- 是否可批处理；
- 是否有自动 Gate；
- 是否存在未确认的高风险项目；
- 同一根因是否制造多个重复 Signal；
- 路由失败怎样升级。

减少 Human Interruption 可能来自：

- 更好的自动验证；
- 更准确的聚合；
- 更少的无效工作；
- 更高的漏报；
- 更长的延迟；
- 不健康的 Detector；
- 被压抑的反馈。

所以 `interruptions ↓` 不能单独证明系统改善。

Attention Queue 至少应区分：

~~~text
new
acknowledged
owned
waiting_for_evidence
waiting_for_authority
intervention_in_progress
expired
unresolved
~~~

Queue 状态不是 Exception 本身的 Truth，只是路由状态。

---

# 14.18 Intervention Point 是有权动作路径

**Intervention Point（干预点：在具名执行或状态边界上，允许有权主体暂停、收窄、改变、接管或恢复的可执行控制路径）** 需要与第13章的 Authority Grant 对齐。

原大纲列出的动作可以重新解释为：

| 动作 | 需要明确的边界 |
|---|---|
| 暂停 | 是否停止新动作，在途动作怎样处理 |
| 修改目标 | 形成新的 Intent Revision，而不是静默改变原目标 |
| 缩小范围 | 更新 Task Scope、Grant 或 Autonomy Profile |
| 更换 Agent | 新 Subject 是否重新绑定 Context、Authority 与 Recovery |
| 回滚 | Baseline 是否仍适用，外部副作用是否可逆 |
| 转人工 | 是否完成真正 Takeover，而不是只改 Owner 字段 |
| 降低权限 | Permission 是否关闭，Authority 是否同时撤销或只暂时限制 |
| 要求重新规划 | 新 Plan 是否仍满足原 Intent、Scope 与 Authority |

Intervention Point 存在，不等于动作已经可用。

项目还需要验证 Credential、Queue、Subagent、Tool Session、Lock、External Side Effect 和 Evidence Preservation。

---

# 14.19 Intervention Contract 把请求、执行与效果拆开

候选 **Intervention Contract（干预契约：声明触发依据、有权主体、目标动作、预期效果、风险、验证与恢复条件的记录）** 可以是：

~~~yaml
intervention_id: INT-204
exception_ref: EXC-088
requested_by: delegated-control-gate
authority_ref: AUTH-STOP-014

action: pause_new_writes
target:
  task_id: TASK-441
  worktree: WT-22

reason:
  detector_evaluation_ref: DET-EVAL-901
  matched_condition: write_outside_granted_scope

expected_effects:
  - reject_new_write_actions
  - preserve_current_evidence

in_flight_policy: isolate_and_report
external_side_effect_policy: reconcile_separately

verification:
  - permission_state_snapshot
  - queue_state_snapshot
  - worktree_diff_after_pause

fallback:
  - revoke_bound_credential
  - human_takeover

expires_at: 2026-08-24T10:20:00+08:00
~~~

这是设计示例。

干预状态至少要区分：

~~~text
requested
authorized
dispatched
applied
effect_observed
effect_not_observed
partial
non-result
recovered
unresolved
~~~

按下 Pause 不等于所有执行停止。

收到 Rollback 命令不等于外部状态恢复。

---

# 14.20 自动干预需要显式 Mapping

自动 Detector 可以触发自动控制，但需要预先绑定：

~~~text
named detector result
+ coverage and health conditions
+ policy version
+ authority grant
+ target action
+ maximum scope
+ verification
+ recovery
→ authorized automatic intervention
~~~

例如：

> 当 exact-inventory Detector 在目标执行前发现 authority-bearing surface 改变，且 Detector 自身 Evaluation 完成时，当前 Harness 可以阻止该目标执行并记录 target `non-result`。

这不授权 Detector：

- 修改自己的 Rule；
- 扩大检查 Scope；
- 删除 Evidence；
- 判定目标代码失败；
- 创建无限 successor；
- 代表 Human 接受新的 Workflow。

自动 Mapping 还需要定义：

- Detector Error 时 fail open、fail closed 还是降级；
- False Positive 的恢复路径；
- 重复 Signal 的去重与幂等性；
- 最大 Intervention Duration；
- 谁可以 Override；
- Override 是否需要独立 Authority；
- 如何避免两个 Controller 相互反复触发。

更多自动停止不自动意味着更安全。错误 Detector、Common-mode Failure 和 Recovery 缺失会把安全机制本身变成风险源。

---

# 14.21 干预后必须重新观察目标效果

Intervention 成功至少有三种不同含义：

1. 控制命令被接受；
2. 目标执行状态发生预期变化；
3. 原风险被限制、恢复或转交。

它们不能合并成 `success: true`。

例如 Pause 后应检查：

- 新动作是否被拒绝；
- 在途动作是否结束或隔离；
- Credential 是否仍可使用；
- Queue 是否继续投递；
- Subagent 是否继续工作；
- 外部状态是否仍变化；
- Evidence 是否保留；
- 谁拥有 Recovery。

Rollback 后应检查：

- 恢复的是哪个 Baseline；
- Source、Runtime、Data 和 External State 是否一致；
- 是否存在不可逆副作用；
- 旧 Baseline 是否仍安全适用；
- 是否只能 Forward Recovery。

Intervention Effect Observation 也可能失败。

此时应记录 `effect_unknown` 或 `non-result`，不能因为控制命令返回 200 就宣称风险已经解除。

---

# 14.22 Telemetry 应尽量自动产生，但人工判断不能被伪造

运行系统可以自动记录：

~~~text
workflow_id and version
subject configuration
started / completed / failed
tool action
state transition
rework / rollback
human intervention
acceptance result
exception and route
~~~

这比要求 Human 每次手工填表更可能长期维持。

但“自动记录”有边界。

以下内容通常不能可靠地从运行 Event 直接推断：

- 为什么 Human 接受风险；
- 某个创意结果是否符合体验目标；
- Reviewer 是否真正理解变更；
- 一次等待是认知困难还是外部中断；
- Rework 是缺陷、偏好变化还是 Scope 变化；
- 未上报的问题是否不存在。

这些需要选择性 Human Annotation、Decision Rationale 或后续 Review。

目标不是消灭人工输入，而是只在机器无法观察的语义处请求人工判断。

---

# 14.23 观察也有成本、权限和风险

Telemetry 可能引入：

- Runtime 与 Storage Cost；
- 高基数和重复 Event；
- Secret、Credential 或 Personal Data 泄露；
- Source Code 与 Prompt Retention 风险；
- Observer Effect；
- Schema Migration；
- Dashboard Maintenance；
- False Positive 与 Alert Fatigue；
- 对可量化指标的错误优化；
- 新的 Authority Surface。

因此不能使用 `log everything` 作为默认答案。

Observation Contract 应明确：

- Data Minimization；
- Redaction；
- Access Control；
- Retention；
- Deletion 与 Legal Hold；
- Source / Event Identity；
- Sampling；
- Aggregation；
- Audit；
- 对调试和事故调查的最低保留。

隐藏 Secret 后，仍要保留足够的结构信息来判断动作边界；保留完整 Payload 时，则需要与风险相称的权限和期限。

Observability 是控制机制，也可能成为新的攻击面和认知负担。

---

# 14.24 AI Game Dev OS v4.94 提供了哪些边界案例

本章使用三组已有项目记录，并区分其中的可观察事实、后续推导与适用限制。

## D-048：Observer Failure 与 Target `non-result`

D-048 的可观察记录与限制见 [Target `non-result` 案例记录](../Evidence/receipts/ER-20260818-002__CLM-C06-004.md) 与 [控制接口案例记录](../Evidence/receipts/ER-20260824-002__CLM-C12-001.md)。

可观察事实：

- Launcher 在 Target Compile 前改变自身 exact inventory；
- 第二次检查 fail closed；
- Target 没有执行，没有形成正常结果；
- 后续需要 Human 对 Retry 与 Round Accounting 作出处置。

它支持：

- Observer Integrity 与 Target Result 分离；
- `non-result` 是必要语义；
- 缺少正常结果不等于健康；
- Stop 后仍需要 Authority 与 Recovery。

它不证明所有静默故障都能被 Detector 发现。

## v4.94 Task Projection：有用但不完整

相关实现与缺口见 [控制接口案例记录](../Evidence/receipts/ER-20260824-002__CLM-C12-001.md)。

可观察事实：

- Task Adapter 存在绑定 Task、Commit 与 Review 的紧凑只读投影；
- 实现暴露 Blocker、Handoff、Cancel、Claim Withdrawal 和 Review Rejection 路径；
- 没有发现统一的 Observation Coverage Health、Detector Health、全局 Takeover 或 Delegation Revocation 界面。

它支持：

- Timeline / Dashboard 可以是 Non-authoritative Projection；
- Control Path 可以引用底层状态，而不是复制 Truth；
- “存在部分控制原语”不等于完整 Observability and Intervention Plane 已经实现。

## D-073 至 D-075：过程信号不等于根因证明

D-073 至 D-075 的提交序列与事后判断见 [治理活锁历史记录](../Evidence/receipts/ER-20260818-001__CLM-OUTLINE-002.md)。

可观察事实：

- 连续提交只改变 Governance、Proposal、Review 与 Transaction 路径；
- 没有 Package Source、Runtime、Test、Qualification 或 Gate Evidence 进展；
- 后续路线改变后产生了分阶段且明确 `NON_QUALIFYING` 的交付 Evidence。

它支持把 `meta-only successor`、Proof Surface 增长和交付 Evidence 停滞作为 Process Warning。

它不单独证明严格治理是根因，也不证明任意 Source/Test 文件增长就是有效进展。

---

# 14.25 最小实现从一个 Decision Path 开始

不要先建设完整 Telemetry Platform。

选择一个满足以下条件的 Decision Path：

- 重复出现；
- 具有明确风险；
- 当前直接观察成本较高；
- 存在可执行 Stop 或 Recovery；
- 能获得基本 Source Identity。

建立最小闭环：

1. 声明 Decision Target；
2. 定义 Subject、Action 与 Failure Mode；
3. 写 Observation Question；
4. 选择最小 Telemetry Source；
5. 记录 Included、Excluded 与 Unknown Coverage；
6. 定义 Freshness 和 `non-result`；
7. 建立一个可版本化 Detector；
8. 测试 Detector Error 与 Route Failure；
9. 绑定 Exception Owner 和 Authority；
10. 实现一个 Pause、Restrict 或 Recovery Action；
11. 验证 Intervention Effect；
12. 记录 False Positive、已知 False Negative / Escaped Incident、Delay、Rework 与 Human Intervention；
13. 决定是否值得扩展。

至少演练：

- Source Stale；
- Schema Drift；
- Detector Error；
- Signal Route Failure；
- Intervention Partial；
- Recovery Unavailable。

如果系统只在正常路径上演示绿色 Dashboard，它尚未验证控制能力。

---

# 14.26 与相邻章节的所有权边界

| 对象 | 所属章节 | 第14章如何使用 |
|---|---|---|
| State Claim、Source、Applicability、Evidence Generation Integrity | 第6章 | 生成和检查运行 Observation |
| Evidence Portfolio、Coverage、Acceptance / Adoption / Release Authorization | 第9章 | 将 Observation 用于具名 Claim 与发布授权决策 |
| Human-facing Projection、Progressive Disclosure、Decision Surface | 第12章 | 显示 Coverage、Health、Exception 与 Action |
| Authority Grant、Autonomy Profile、Pause、Revoke、Takeover | 第13章 | 约束谁能执行 Intervention |
| Telemetry Source、Observation Contract、Detector Evaluation、Exception Lifecycle、Intervention Effect | 第14章 | 本章核心对象 |
| Memory Promotion、Conflict、Expiry | 第15章 | 决定哪些历史观察可进入长期记忆 |
| Self-Evolution Candidate、Evaluation Contract、Activation / Rollout Record | 第16章 | 使用长期 Observation 评估 Workflow 变化；基础 Adoption 引用第9章 |
| Release Execution、Release Outcome、Trace | 第18章 | 观察已授权发布的执行与外部后果 |

第14章不从 Telemetry 自动生成长期 Memory，也不根据指标自动宣称 Workflow Improved。

---

# 14.27 本章原则

1. **先声明观察问题。** Telemetry Volume 不是 Observability。
2. **Event、Observation、Claim、Evidence、Signal、Exception 和 Intervention 分开。** 它们不会自动互相升级。
3. **Coverage 必须显示盲区。** 未观察表面不能被绿色状态吞掉。
4. **Freshness 绑定 Decision。** 新生成的 View 可能包含过期 Source。
5. **Observer Integrity 与 Target Result 分开。** Observer 失败不能伪造目标 FAIL。
6. **Detector Health 是多维判断。** Heartbeat 和自报健康都不是充分证据。
7. **Silence 是有边界的 Non-detection。** 不是全局健康证明。
8. **Timeline 不证明因果。** 并发系统需要 Identity、Correlation 与 Uncertainty。
9. **Severity 不产生 Authority。** 自动干预需要显式 Policy Mapping 和 Grant。
10. **干预请求与目标效果分开。** Pause Button、Rollback Command 和 HTTP 200 都不是恢复证明。
11. **自动 Telemetry 不能伪造人类判断。** 体验、理由和责任仍需要有权角色表达。
12. **观察机制也受治理。** 成本、隐私、Retention、Attack Surface 和 Cognitive Load 都进入设计。

---

# 14.28 常见反模式

- 收集所有日志，再寻找用途；
- 用 Event 数量表示 Coverage；
- 把 Coverage 压成没有 Failure Mode 权重的单一百分比；
- 把 Dashboard 当作新的 Truth Store；
- 用时间顺序证明因果；
- 声称记录了模型隐藏推理；
- 把 Context Manifest 当作模型实际理解记录；
- `No Alert = Healthy`；
- Detector 自报 healthy 即结束检查；
- Detector Error 被显示为 not_detected；
- 旧 Observation 被新 Dashboard 包装成最新状态；
- Signal 自动升级为 Incident；
- Severity Score 自动扩大 Authority；
- 所有 Warning 都触发 Hard Stop；
- Alert 越少就认为 Workflow 越好；
- Queue Acknowledged 被当作问题解决；
- Pause Command 返回成功就认为执行已停止；
- Rollback 完成但未验证外部副作用；
- 人工 Rationale 被自动指标替代；
- 为了 Observability 长期保存 Secret 与完整 Payload；
- 用 D-048 证明所有静默故障都可检测；
- 用 v4.94 的部分 Task Projection 声称完整 HCP 已实现。

---

# 14.29 本章检查清单

## Observation Question

- 当前要支持哪个 Decision Target？
- Subject、Action、Environment 与 Failure Mode 是否具名？
- 当前需要的是 Event、State Claim、Evidence 还是 Decision？
- 是否声称观察了无法访问的内部认知？

## Source 与 Coverage

- Source Identity、Version 与 Collection Method 是否记录？
- Included、Excluded、Partial 与 Unknown Surface 是否显示？
- Source Stale、Unavailable、Delayed 与 Sampled Out 是否分开？
- Observation 是否可能改变 Target 或 Authority Surface？

## Time 与 Integrity

- Event、Ingestion、Evaluation、Projection 与 Decision Time 是否区分？
- Freshness 是否绑定当前 Decision，而不是统一 TTL？
- Observer Integrity Failure 是否与 Target Result 分开？
- Partial Observation 是否被错误提升为完整结果？

## Detector

- Detector、Configuration、Input 与 Coverage 是否版本化？
- Evaluation 是否明确记录 completed、unknown 或 error？
- Source、Transport、Schema、Route 与 Effectiveness Health 是否分开？
- 是否有 Synthetic Event、Replay、Independent Watchdog 或 Human Audit 中至少一种合适检查？

## Exception 与 Routing

- Signal、Exception 与 Incident 是否分开？
- Observable Fact、Inference、Alternative Explanation 与 Recommendation 是否分栏？
- Owner 是否拥有所需 Domain Knowledge 与 Authority？
- Route Failure、Queue Age、Duplicate 与 Expiry 是否处理？

## Intervention

- 动作是否绑定 Authority Grant 和最大 Scope？
- Request、Dispatch、Apply 与 Effect Observation 是否分开？
- In-flight、Credential、Queue、Subagent 与 External Side Effect 是否处理？
- Recovery 是 Rollback、Forward Recovery 还是暂时未知？
- 干预失败或 Partial 时，谁负责下一步？

## Cost 与 Human

- Telemetry 是否收集了不必要的 Secret、Payload 或 Personal Data？
- Retention、Redaction、Access 与 Deletion 是否明确？
- Alert 数量变化是否同时检查漏报、延迟和 Detector Health？
- Human Rationale、体验与责任是否被自动指标错误替代？

---

# 14.30 本章结论

Observability 不是把所有内部数据展示给人。

它是为具名 Decision 建立一条可检查链：

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

链条中的每一步都可能是 `partial`、`unknown`、`error` 或 `non-result`。

没有任何一步因为界面显示绿色就自动补全。

本章最重要的边界是：

> **Absence of a signal is not evidence of global health. An intervention request is not evidence of control effect.**

中文语义是：

> **没有信号，只能在覆盖、时效和 Detector Health 已知时支持具名条件未被检测到；发出干预请求，也只有在目标效果被重新观察后，才能支持控制已经生效。**

下一章将讨论这些 Observation、Decision 与 Exception 中，哪些可以进入长期 Memory，如何保留 Provenance、Scope 与 Expiry，以及怎样防止错误经验被反复放大。
