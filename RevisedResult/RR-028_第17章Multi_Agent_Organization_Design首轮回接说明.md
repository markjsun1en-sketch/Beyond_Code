# RR-028：第17章 Multi-Agent Organization Design 首轮回接说明

- 记录日期：2026-08-24
- 工作稿：[第17章 Multi-Agent Organization Design](../OptimizedDocs/第17章_Multi_Agent_Organization_Design_首轮修订稿.md)
- 原始结构：[全书大纲第17章](../OringinalDocs/beyond_code_ai_native_software_engineering_outline_zh.md)
- 新增材料：[Cognitive Control、Trust 与 Human Control Plane v0.1](../OringinalDocs/ai_native_cognitive_control_trust_human_control_plane_v0.1.md)
- 核心 Claim：[`CLM-C17-001`](../Evidence/claim-ledger.md)，当前为 `unsupported / accepted / narrow`
- 关联案例 Evidence：[CLM-C12-001](../Evidence/receipts/ER-20260824-002__CLM-C12-001.md)、[CLM-C16-001](../Evidence/receipts/ER-20260824-003__CLM-C16-001.md)、[CLM-C09-001](../Evidence/receipts/ER-20260818-003__CLM-C09-001.md)
- 审阅依据：[RR-021](RR-021_Human_Control_Plane与认知控制架构审阅.md)、[RR-023](RR-023_第12章Cognitive_Compression首轮回接说明.md)、[RR-024](RR-024_第13章Governed_Autonomy首轮回接说明.md)、[RR-027](RR-027_第16章Self_Evolution_Engineering首轮回接说明.md)
- 记录性质：章节回接说明，不是新的 Evidence Receipt
- 章节核心假设状态：`LOGIC_HYPOTHESIS_CORE_ACCEPTED_DETAILS_OPEN`
- 章节措辞状态：`VOICE_NOT_REVIEWED`

## 回接结果

第17章已经形成独立工作稿。

Multi-Agent Organization Design 被限定为：

> 把具名工作、角色契约、Subject、Authority、责任、依赖、交接、冲突和集成处置组织成可检查协作关系的工程活动。

本轮首先拒绝一个前提：

> 多个 Agent 并行运行，不表示项目已经形成组织。

核心链条是：

~~~text
bounded Work Unit
+ Role Contract
+ Subject Configuration
+ accepted Assignment
+ Authority Reference
→ candidate output and visible execution state
→ Handoff Receipt / Review / Conflict
→ authorized Integration Disposition
→ explicit next responsibility
~~~

2026-08-24 初始核心句为：

> Agent count is not evidence of organization. A governable multi-agent arrangement must at least make work, authority, responsibility, interfaces, conflict and integration explicit.

当时中文语义被收窄为“数量不是组织证据，可治理安排至少需要说明这些关系”，没有声称这些对象足以形成高效组织，也没有声称多 Agent 优于单 Agent。W0 后的当前表述见本记录末尾 Addendum；旧句保留在这里用于说明 Claim 为什么需要再次收窄。

## 核心 Claim 的初始证据状态

本轮分配了 `CLM-C17-001`：

> Agent 数量本身不足以证明已经形成组织或获得组织效能；可治理的多 Agent 安排至少需要说明 Work、Role、Authority、Responsibility、Handoff、Conflict 与 Integration 的关系。

该 Claim 在 2026-08-24 初次登记为：

- Evidence Coverage：`unsupported`；
- Human Status：`unreviewed`；
- Current Disposition：`hold`。

原因不是现有案例反驳了它，而是尚未建立直接 Receipt：

- 没有单 Agent 与多 Agent 的受控比较；
- 没有验证九对象是否完整或最小；
- 没有测量不同 Topology 的质量、速度、成本或缺陷结果；
- 既有 Receipt 只支持 Review、Evidence、Adoption、Release 和任务投影的局部分离。

因此，本章中心模型属于带替代方案与失败模式的当前建议，不作为已验证事实。

## 原大纲内容保留情况

| 原大纲主题 | 新工作稿落点 | 处理 |
|---|---|---|
| 多 Agent 不等于组织 | 17.1–17.3、17.28、17.35 | 保留并扩展为 Work、Role、Authority、Handoff、Conflict 与 Integration 关系 |
| Controller、Planner、Specialist、Reviewer、QA 等角色 | 17.4–17.5、17.10–17.15 | 改为可组合 Role Library，不作为固定组织图 |
| Responsibility and Authority | 17.3–17.7、17.23、17.25 | 分离 Responsibility、Authority、Permission 与 Accountability |
| Structured Handoff | 17.16–17.18 | 扩展为 Handoff Package、Receipt、职责接管时间和 Source-linked Context |
| Agent Conflict Resolution | 17.19–17.21 | 先分冲突类型，再匹配 Source、Decision Target 与 Authority |
| Controller / Worker | 17.10–17.13 | Controller 改为协调 Role；Worker 输出 Candidate，并拥有反向升级路径 |
| Human-Agent Organization | 17.25–17.26 | Human 绑定具名价值与风险责任，不作为每一步默认 Gate |

原大纲问题域都得到承接，但“角色名称即组织结构”“Controller 统一拥有全局 Authority”“人类角色线性迁移”没有保留。

## 九个组织对象

工作稿区分：

1. Work Unit；
2. Role Contract；
3. Subject Configuration；
4. Assignment；
5. Authority Reference；
6. Dependency / Coordination Relation；
7. Handoff Package / Receipt；
8. Conflict Record；
9. Integration Disposition。

Work Unit 不是开放式 Prompt；Role Contract 不是职位名称；Assignment 不是 `Agent A → Task B`；Integration Disposition 也不等于 Merge Command。

这九个对象是候选分解，不是经过完备性证明的通用 Schema。

## Agent、Role、Persona 与 Skill

工作稿分开：

- Agent Instance：具名运行实例；
- Delegated Subject：被 Assignment 与 Authority 识别的治理主体；
- Role：围绕责任、Decision Lens、输入、输出与升级路径形成的契约；
- Persona：影响表达或探索方式的提示性设定；
- Skill：提供方法、Procedure 或 Tool Binding。

同一 Agent 可以承担多个 Role，但换 Role 名称不会自动产生 Review Independence。

这一边界延续了前文“能力、Permission、Authority、Reliance 与 Autonomy 分离”的结论，没有把 Agent 人格化名称写成责任主体。

## Role Contract 与 Role Library

Role Contract 候选字段包括：

- Purpose；
- Decision Lens；
- Responsibilities；
- Allowed / Prohibited Decisions；
- Inputs 与 Required Source Access；
- Outputs；
- Evidence Obligations；
- Escalation；
- Handoff Target；
- Stop Condition；
- Expiry。

Controller、Planner、Builder、Specialist、Reviewer、Validator、Challenger、QA、Researcher、Knowledge Curator、Security Reviewer 和 Release Role 被保留为可选 Profile。

原大纲中的 Cognition Agent 没有保留为稳定 Role 名称；Attention Routing、Compression Validation、Exception Detection、Human Interface 与 Organization Review 被视为可分开的 Responsibility，避免再次形成超级对象。

本轮没有：

- 为每个 Role 建立固定 Agent；
- 把角色数量写成成熟度；
- 要求小项目采用完整角色集；
- 创建第三个“主笔 Agent”或自动组织调度层。

## Controller、Planner 与 Worker

Controller 被拆为可能的 Intent Custody、Work Coordination、Context Routing、Dependency Tracking、Integration、Attention Routing 与 Escalation 责任。

它不自动拥有：

- Truth；
- Human Intent 改写权；
- 自我授权权；
- Domain Review；
- 全部 Integration；
- Release；
- Policy Override。

Planner 输出 Plan Candidate。Plan Accepted、Assignment Created 和 Execution Authorized 分开。

Worker 输出 Candidate Artifact、实际修改、Evidence、Unknown、Blocker 与 `non-result`。完成交付、运行测试或 Merge 不自动完成 Scope Acceptance、Adoption 或 Release。

Controller / Worker 被写成双向协作关系：Controller 路由 Work，Worker 可以上报条件变化、Scope 冲突和 Authority 缺口。

## Review 与独立性

工作稿分开：

- Reviewer：根据 Review Contract 检查 Candidate 与目标、范围、风险或完整性关系；
- Validator：对具名 Claim 或 Contract 运行指定检查；
- Challenger：寻找反例、隐藏假设、替代解释和适用边界。

Review Independence 被拆成七个候选维度：

1. Producer；
2. Contract；
3. Context；
4. Source；
5. Method；
6. Decision；
7. Authority。

不同 Agent 名称、相同模型与相同 Summary 只构成额外采样，不自动构成完整独立性。

独立审阅也不自动正确；它只能降低部分共因失败，不能弥补错误 Contract、Source 缺失或能力不足。

## Structured Handoff

Handoff Package 候选字段包括：

- Goal / Intent Reference；
- Work Unit、From / To Role；
- Candidate 与 Baseline；
- Current State、Completed、Actual Change 与 In-flight；
- 已有 Decision 及其 Authority；
- Assumption；
- Evidence 与 Counterevidence；
- Unknown、`non-result`、Blocker 与 Risk；
- Requested Next Action 与 Requested Authority；
- Source Link 与 Expiry。

工作稿新增 Handoff Receipt，区分：

- Submitted；
- Accepted for Named Work；
- Partially Accepted；
- Rejected Out of Scope；
- Missing Input；
- Authority Not Available；
- Dependency Not Ready；
- Superseded。

接收 Handoff 只表示接管具名工作或 Artifact Custody，不自动接受 Claim，不自动 Adoption，也不自动转移全部 Authority 与 Accountability。

## Shared State 与 Context

工作稿没有建议把全部 Context 复制给所有 Agent。

候选结构是：

~~~text
authoritative source records
→ small shared coordination index
→ role-specific Context Projection
→ Source-linked decisions and outputs
~~~

Shared State 保存 Work、Assignment、Dependency、Decision、Authority 与 Handoff 的小型有来源索引。

Role-specific Context 只包含完成当前 Contract 所需的内容，并保留下钻 Primary Source 的能力。

无来源 Global Summary 被视为潜在的第二状态库；Source Access 也不等于正确理解 Applicability。

## Conflict 与组织失效

工作稿将 Conflict 分成：

- Observable State；
- Evidence Interpretation；
- Design / Strategy；
- Authority；
- Policy / Instruction；
- Dependency / Resource；
- Creative / Value；
- Responsibility。

原大纲中的“事实优先级、角色权限、证据强度、风险升级、人类裁决”被改为检查维度，不作为通用强弱排序。

Runtime Claim、历史 Decision、设计 Trade-off 与价值判断不能机械进入同一 Evidence Ranking。

Deadlock 与 Livelock 被纳入组织失败：

- 循环 Dependency；
- 交叉 Approval；
- 无 Decision Owner；
- 无限 Review / Rework；
- 自动生成后继 Governance Work；
- 活动持续增加但目标不接近可裁决状态。

应对方式包括 Dependency Check、Review Budget、Stop / Escalation、Blocked Receipt 和阻止无 Authority 的自动后续。

## Parallel Execution、Integration 与委托

并行 Work 需要：

- Artifact Ownership；
- Write Surface；
- Worktree / Sandbox / Environment Isolation；
- Shared Resource Coordination；
- Baseline Identity；
- Integration Order；
- Conflict Owner；
- Recovery Point。

Integration Disposition 与 Merge、Adoption、Release 分开。

下游 Agent 不自动继承上游全部 Authority。创建 Assignment、转授 Authority、扩大 Scope、分配 Credential 和接受输出是不同决定。

Revocation 不能只发送 Kill Signal，还需处理 In-flight Work、External Side Effect、Credential、Memory Candidate 与待裁决产物。

## Human-Agent Organization

Human 可以承担 Intent Owner、Creative Owner、Policy Author、Risk Acceptance Authority、Domain Reviewer、Organization Designer、Exception Handler 或 Recovery Owner。

本轮没有把“Human in the Loop”视为充分设计，也没有把 Human 写成：

- 每个低风险动作的默认 Approval Gate；
- 所有决定的最终按钮；
- 可以单方越过安全 Policy、法规或多方授权的主体；
- 必然逐步退出实现工作的线性角色。

工作稿采用 Capability-relative Role Allocation：Human 与 Agent 的角色按当前能力、风险、项目阶段、事故状态和可用性分配。

## Organization Observability 与成本

Organization Observability 只观察可见的：

- Work、Assignment 与 Dependency；
- Authority 与 Decision；
- Handoff 与 Receipt；
- Candidate、Evidence 与 Non-result；
- Running、Waiting、Blocked、Cancelled 与 Unknown；
- Conflict 与待裁决结果。

不声称访问 Agent 的隐藏思维过程。

多 Agent 成本包括 Work Decomposition、Context 构造、等待、Handoff、重复探索、Review、Conflict、Integration、共享状态、Governance Artifact、Human Attention 与 Recovery。

Agent 数量、并发数、总 Token 或总输出不作为组织效能的单独指标。

多 Agent 只有在并行、异质能力、独立审阅、Context Isolation、Failure Containment 或责任清晰度带来的收益超过协调成本时，才是值得测试的候选。

## Evidence 回接边界

### CLM-C12-001

v4.94 的紧凑任务投影和 Blocker、Handoff、Cancel、Claim Withdrawal、Review Rejection 路径支持组织状态可以有非权威投影和显式控制语义。

它不证明完整 Multi-Agent Organization，也不证明投影已降低 Human Judgment Load。

### CLM-C16-001

D-076 的 Dual Review PASS 只使候选进入 Human Disposition Eligibility，支持 Review Result 与 Adoption Decision 分开。

它不证明两个 Reviewer 在七个独立性维度上充分分离，也不证明 Dual Review 普遍有效。

### CLM-C09-001

SP122 接受 Qualifying Evidence，同时保持 Adoption Blocked 与 Production Unapproved，支持不同 Decision Target 可以分离。

它是人工决定记录，不是组织设计效果测试。

### 总边界

现有 Evidence 可以支持：

> Candidate Production、Review、Evidence Disposition、Adoption 和 Release 可以由不同 Role / Authority 处理，并通过有来源记录保留边界。

现有 Evidence 不能支持：

- 多 Agent 比单 Agent 更快、更便宜或质量更高；
- 九对象构成完备或最小组织模型；
- Central Controller、Pipeline、Peer、Builder–Reviewer 等任一 Topology 普遍更优；
- 双 Review 等于独立 Review；
- Human Control Plane 已实现完整组织控制；
- v4.94 是完整 Multi-Agent Organization。

## 有意不进入本章的内容

- Agent 数量即组织成熟度；
- Persona 或 Agent Name 即 Role Contract；
- Controller 是全局 Truth / Authority Owner；
- Planner 产生 Plan 即获得 Execution Authority；
- Worker 交付、Test PASS 或 Merge 即完成 Adoption；
- 两个 Agent 名称不同即独立审阅；
- Reviewer PASS 自动完成 Release；
- Handoff Submitted 即对方已接管；
- Handoff 接受等于 Truth、Authority 或全部 Accountability 转移；
- 把全部 Context 提供给全部 Agent；
- Global Summary 成为新的权威状态库；
- 所有冲突按一个 Evidence Strength 排序；
- 创意和价值冲突由机器分数消除；
- Merge Success 等于 Semantic Integration；
- 下游 Agent 自动继承全部 Authority；
- Human 是每一步 Gate 或拥有任意 Override；
- Human 角色沿单一成熟度阶梯离开实现；
- 总 Token、总输出或并发任务数证明组织效能；
- v4.94 或 SP122 证明多 Agent 普遍更好。

## 与相邻章节的接口

- 第4章拥有 Intent Artifact、Conflict 与 Acceptance Target；
- 第5章拥有 Context Contract、Pack、Manifest 与 Access；
- 第6章拥有 State Claim、Evidence 与 Applicability；
- 第9章拥有 Evidence Coverage、Acceptance、Adoption 与 Release；
- 第12章拥有 HCP Projection、Brief 与 Compression Validation；
- 第13章拥有 Capability、Permission、Authority Grant、Delegation、Revocation 与 Autonomy Profile；
- 第14章拥有 Observation、Detector、Exception 与 Intervention；
- 第16章拥有 Organization Change Candidate 的评估与采用；
- 第17章拥有 Role、Assignment、Handoff、Conflict 与 Integration；
- 第18章拥有 Durable Decision Trace、Attribution、Audit 与 Accountability Evidence。

第17章处理当前组织关系，第18章处理这些关系怎样形成长期可追溯责任链。

## 2026-08-24 初始审阅点

在初次回接时，核心 Claim、对象模型和章节措辞尚未由作者裁决，当时列出以下检查点。W0 已处置高层 Claim 与所有权标签，但详细九对象、篇幅和声音问题仍开放；当前状态以本记录末尾 Addendum 为准。

1. 当前列出的关系是否足以描述“可治理”，是否还需要激励、资源、制度环境或其他对象；
2. 九对象是否过细，Dependency 是否应只是 Work Unit 字段；
3. Subject Configuration 是否需要作为正文对象；
4. Accountability 是否应全部移到第18章；
5. Controller 是否仍承担过多 Context / Attention 责任；
6. Review Independence 七维是否过细，哪些应进入附录；
7. Handoff YAML 是否应移入附录；
8. Handoff Receipt 是否会制造过重流程；
9. Conflict 八分类是否与第4、6、9章重复；
10. Human Role Migration 的反驳是否需要案例支撑；
11. Organization Observability 是否与第14章重复；
12. 最小试点指标是否需要建立新的 Evidence Receipt 后才进入正文；
13. 章节篇幅是否应在作者裁决对象后压缩；
14. 标题是否应缩为 Governed Multi-Agent Collaboration，避免“Organization”概念过重。

## 2026-08-25 Narrative Cleanup Addendum

本次调整没有出现新的运行 Evidence，也没有改变 `CLM-C17-001` 的
Coverage、Human Status 或 Ledger 历史。

改变的是 Evidence Routing 的定义：正式 Receipt 用于历史事实、效果、
跨项目推广和高风险 Claim，不作为候选理论模型进入正文的许可证。

因此需要修正此前容易产生的误读：

- `unsupported` 继续约束“多 Agent 比单 Agent 更快、更便宜、质量更高”及
  “九对象是完备或最小组织模型”等效果或一般化 Claim；
- 它不表示 Work、Role、Assignment、Authority、Responsibility、Handoff、Conflict 与
  Integration 的候选概念分解不能进入正文；
- 本章对象集继续作为 `proposed conceptual model`，由定义一致性、解释力、
  反例、替代模型、Scope 和 Human Review 审查；
- 现有案例仍只支持 Review、Evidence Disposition、Adoption、Release 与
  Handoff 的局部分离，不证明多 Agent 组织效能。

Reader-facing Chapter 已据此：

1. 移除 Header 中的 Receipt 列表和内部状态；
2. 直接声明模型是候选组织模型；
3. 明确不声称多 Agent 必然改善质量、速度或成本；
4. 将若干通用 `必须 / 至少` 改为本书工作定义或候选检查项；
5. 保留案例事实、反例、组织成本和单 Agent 替代方案。

结论变化来自 Evidence Workflow 适用范围的重新定义，不来自对历史案例的
重新解释。

## 2026-09-02 W0 Decision Reconciliation Addendum

Human 以“授权W0”接受第17章的高层检查关系作为显式 Design Hypothesis（设计假设）。接受范围是：Agent 数量本身不足以证明已经形成组织或获得组织效能；本书可以用 Work、Role、Assignment、Authority、Responsibility、Handoff、Conflict 与 Integration 检查一个多 Agent 安排暴露了哪些协作关系。

正文 17.3 展开的九个候选对象是这个高层假设的工作性 elaboration，不在 W0 中逐项冻结。Subject Configuration、Dependency / Coordination 以及 Responsibility 如何映射到详细对象，留给 P0 的反例与压缩测试；若要改变逻辑对象，仍须先修改 `OptimizedDocs/`，不能在 Polish 阶段静默决定。

这项裁决改变了 `CLM-C17-001` 的措辞和 Human disposition，没有出现新的项目事实或外部 Evidence：

- 旧措辞中的“至少需要”容易被读成跨项目必要条件；
- 新措辞把这些关系限定为本书的候选检查面；
- Coverage 继续为 `unsupported`，因为没有证明对象集完备、最小、跨项目必要，也没有证明多 Agent 改善质量、速度、成本或 Human Load；
- Human 接受的是一个可供反例和迁移测试挑战的概念模型，不是经验定律。

W0 同时修正了本章所有权表中的两个陈旧标签：Authority Grant 归第13章，Intervention 归第14章。这是与 RR-037 已接受对象所有权的对齐，不是重新打开对象模型。

## Human Disposition

- Core Claim：`unsupported / accepted / narrow`
- Logic：`LOGIC_HYPOTHESIS_CORE_ACCEPTED_DETAILS_OPEN`
- Evidence Route：`EVIDENCE_BOUNDARY_ACCEPTED`；效果、完备性与跨项目必要性仍需新 Evidence
- Polish：`POLISH_NOT_AUTHORIZED`；W0 没有启动第17章 Pilot
- Six Fidelity：`NOT_RUN_FOR_POLISHED_CHAPTER`
- Human Voice：`VOICE_NOT_REVIEWED`
- Decision by：Human author
- Decision at：2026-09-02
- Authorization：`授权W0`
- Not accepted：九个详细对象逐项冻结、固定 Topology、完备或最小对象集、跨项目必要性、多 Agent 效能，以及 Human Control Plane 已降低认知负担
