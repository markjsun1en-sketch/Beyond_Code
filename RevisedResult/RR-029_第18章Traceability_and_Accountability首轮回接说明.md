# RR-029：第18章 Traceability and Accountability 首轮回接说明

- 记录日期：2026-08-24
- 工作稿：[第18章 Traceability and Accountability](../OptimizedDocs/第18章_Traceability_and_Accountability_首轮修订稿.md)
- 原始结构：[全书大纲第18章](../OringinalDocs/beyond_code_ai_native_software_engineering_outline_zh.md)
- 新增材料：[Cognitive Control、Trust 与 Human Control Plane v0.1](../OringinalDocs/ai_native_cognitive_control_trust_human_control_plane_v0.1.md)
- 核心 Trace Claim：[CLM-C06-003](../Evidence/receipts/ER-20260810-003__CLM-C06-003.md)，`partial / unreviewed / narrow`
- 核心 Accountability Claim：[`CLM-C18-001`](../Evidence/claim-ledger.md)，`partial / unreviewed / narrow`
- 补充 Evidence：[CLM-C06-002](../Evidence/receipts/ER-20260810-002__CLM-C06-002.md)、[CLM-C09-001](../Evidence/receipts/ER-20260818-003__CLM-C09-001.md)
- 审阅依据：[RR-018](RR-018_第六章独立Agent逻辑与措辞审阅.md)、[RR-021](RR-021_Human_Control_Plane与认知控制架构审阅.md)、[RR-024](RR-024_第13章Governed_Autonomy首轮回接说明.md)、[RR-028](RR-028_第17章Multi_Agent_Organization_Design首轮回接说明.md)
- 记录性质：章节回接说明与 Evidence 适配审计，不是新的 Evidence Receipt
- 章节对象模型与措辞状态：`unreviewed`

## 回接结果

第18章已经形成独立工作稿。

Traceability 被定义为：

> 沿着具名、版本绑定且有来源的关系，定位 Intent、Work、Context、Subject、Authority、Action、Change、Evidence、Review、Decision 与 Outcome 的能力。

Accountability 被定义为：

> 组织要求具名 Human 或角色对目标、控制设计、授权、复核、处置、运行或恢复承担解释与后果责任的规范性关系。

本轮建立的中心边界是：

> Traceability 提供可检查材料，Accountability 决定谁必须对哪些决定和控制作出解释；前者不能自动生成后者。

中心链条是：

~~~text
named Trace Contract
→ source-linked external decision environment
→ typed Action / Change / Evidence / Review relations
→ Authority-bound Decision Record
→ visible Outcome, Gap and Correction
→ bounded Reconstruction and Accountability Review
~~~

工作稿不保存或声称恢复隐藏思维，不承诺所有任务可以确定性重放。

## 两个核心 Claim

### CLM-C06-003

现有 Receipt 的 Claim 是：

> 对长任务或多 Agent 工作，保存版本绑定的外部决策环境，是比复现隐藏推理更现实的审计、恢复和复查目标。

该 Claim 已扩展登记位置为第6/18章，但 Receipt 本身没有被重写。

Coverage 仍为 `partial`：

- SP122 支持外部计划、版本、运行身份、Evidence 与 Human Decision 可以被检查；
- 不支持保证恢复、行为复现、固定字段完备性或因果改进。

### CLM-C18-001

本轮新增：

> Trace 记录可以支持行动归因、有限重建和责任审查，但不能自行分配或解除 Accountability；项目应把责任绑定到具名 Decision Target、Authority 与 Human／组织角色，并将 Agent 视为可被行动归因的执行主体。

Coverage 登记为 `partial`：

- CLM-C06-003 支持 Trace 与有限重建；
- CLM-C06-002 支持 Agent Assertion、Evidence 与 Authority 分开；
- CLM-C09-001 支持 Review / Evidence、Adoption 与 Release Decision 分开；
- 没有 Receipt 直接验证 Accountability Surface 或不同组织中的责任效果。

因此处置为 `narrow`，不是 `verified`。

## 原大纲的五项前提修正

### 1. Git History 不是“只能回答改了什么”

Git 可以保存 Diff、Ancestry、Author / Committer Metadata、Message、Signature、Tag 和外部 Reference。

工作稿没有贬低 Git，而是区分：

- Git History 管理版本事实；
- Decision Trace 连接 Intent、Authority、Evidence 与 Decision。

Decision Graph 引用 Git，不复制 Git 成为第二个 Repository State。

### 2. 完整追踪链不是稳定线性 Pipeline

原大纲：

~~~text
Intent
→ Context
→ Plan
→ Agent
→ Tool Action
→ Change
→ Evidence
→ Review
→ Decision
~~~

被改为有类型关系图。

原因是：

- Decision 可能在 Action 前授权，也可能在 Review 后 Adoption；
- Evidence 可以 Narrow 旧 Claim；
- Later Decision 可以 Supersede 旧 Decision；
- 多个 Subject、Tool 与 Authority 可能并行参与；
- Handoff、Recovery 与 Exception 会回接前序关系。

时间顺序不自动等于因果。

### 3. “完整轨迹”必须相对 Trace Contract

工作稿要求 Trace Contract 声明：

- Decision Target；
- Required Record；
- Required Relation；
- Integrity；
- Access；
- Retention；
- Known Exclusion。

Coverage 可以是 `complete-for-release-decision-v2`，同时对事故因果仍然 `partial`。

没有 Scope 和 Exclusion 的“完整执行轨迹”不可验证。

### 4. 可重放不适用于所有高风险活动

工作稿分开：

- Decision Environment Reconstruction；
- Action Replay；
- Result Reproduction；
- State Restoration。

模型、外部 API、数据、时间、Credential、Tool 与 Human Judgment 可能阻止确定性复现。

新 Replay 产生新 Attempt 和新 Evidence，不能覆盖原记录。

### 5. 责任不能简单“最终交给人类”

工作稿拒绝一个无 Decision Target 的单一“最终责任人”。

Accountability 按 Intent、System Design、Policy、Delegation、Assignment、Evidence、Review、Adoption、Release、Recovery 与 Record Governance 分配。

Human 也可能受 Policy、法规、多方授权和组织制度约束。

本章不推导法律责任。

## 八个概念

工作稿分开：

1. Provenance；
2. Traceability；
3. Auditability；
4. Reconstructability；
5. Replayability；
6. Explainability；
7. Attribution；
8. Accountability。

关键差异包括：

- Provenance 不证明当前适用；
- Traceability 不证明记录完整；
- Auditability 不保证审计发现问题；
- Reconstruction 不重现内部行为；
- Replay 不保证相同结果；
- Explainability 不恢复 Hidden Reasoning；
- Attribution 不自动形成组织或法律归责；
- Accountability 不由日志自动生成。

## 十一种 Record Role

工作稿使用：

1. Trace Contract；
2. Intent / Work Reference；
3. Execution Baseline Reference；
4. Subject Configuration Reference；
5. Assignment / Authority Reference；
6. Action / Activity Record；
7. Change / Artifact Reference；
8. Evidence / Observation Reference；
9. Review / Handoff Reference；
10. Decision Record；
11. Outcome / Exception / Recovery Reference。

这些是语义角色，不要求生成十一个文件。

对象集尚未得到完备性或最小性验证。

## Decision Graph

Decision Graph 被定义为来自 Primary Record 的有类型投影。

候选关系包括：

- `derived_from`；
- `used`；
- `supplied_to`；
- `performed_by`；
- `authorized_by`；
- `generated`；
- `observed`；
- `supports_for_scope`；
- `reviewed_by`；
- `disposed_by`；
- `supersedes`；
- `invalidates`；
- `handed_to`；
- `released_as`；
- `recovered_by`。

`caused_by` 不能从时间相邻自动推导。

Graph 节点需要 Source Link、Version、Freshness 与 Missing State。

## Identity 与 Attribution

工作稿区分：

- Requester；
- Planner；
- Assigned Worker；
- Agent Instance；
- Model / Contract；
- Tool；
- Credential；
- Commit Author；
- Committer；
- Reviewer；
- Decision Authority；
- Deployer；
- Incident Responder。

一个 `actor` 字段不足以承载这些关系。

Commit Author 不自动等于唯一代码产生者、Reviewer、Adoption Authority 或 Release Authority。

Authentication、Attribution 与 Accountability 分开。

## Context、Plan 与 Action

Context Trace 只记录：

~~~text
eligible
→ selected
→ supplied / accessible
→ visibly accessed
→ cited
~~~

它不推断模型实际注意、理解或依赖了什么。

Plan Candidate、Plan Review、Assignment、Execution Start、Replanning、Cancellation 与 Handoff 分开记录。

Action Record 保存 Requested、Attempted、Completed、Interrupted 或 Revoked 的可见动作。

Action Success 不证明上层 Intent 完成，也不自动证明因果。

## Decision Record 与 Stated Rationale

Decision Record 候选字段包括：

- Decision Target；
- Authority Holder 与 Grant；
- Disposition；
- Candidate / Baseline；
- Intent、Work、Context 与 Plan；
- Evidence / Counterevidence；
- Stated Rationale；
- Alternatives；
- Assumption / Unknown；
- Effective Scope / Time；
- Expiry / Reopen；
- Supersession。

Stated Rationale 是有来源、可审查的外部理由。

它不是：

- 模型完整内部推理；
- 唯一心理原因；
- 无遗漏因果解释；
- Decision 正确性的独立 Evidence。

Conversation Transcript 可以作为过程记录，但不能取代 Decision Record。

## Evidence、Review 与 Decision

工作稿保留：

~~~text
Evidence
→ supports named Claim for declared Scope
→ accepted or rejected for named Use
→ informs an Authority-bound Decision
~~~

Review Submitted、Review Disposition、Acknowledgment、Approval、Acceptance、Adoption、Release Authorization 与 Deployment 被分开。

`approved` 没有 Decision Target 与 Authority 时没有稳定语义。

一个授权 Gate 可以合并 Validation 与 Acceptance，但不能扩张到未授权的 Adoption 或 Release。

## Accountability Surface

工作稿没有把 Tool / Agent 的执行和组织问责放在同一列。

它分别记录：

- 可被行动归因的 Human / Agent / Tool / Gate；
- 承担组织问责的 Human 或具名角色。

责任面包括：

- Intent / Product；
- System Design；
- Policy；
- Delegation；
- Assignment / Execution；
- Evidence；
- Review；
- Adoption；
- Release / Operations；
- Recovery；
- Record Governance。

Agent 可以承担 Operational Responsibility 并被 Attribution，但不能通过一句“AI 自动完成”成为最终责任承担者。

同样，这不表示所有错误都归给一个 Human。事故还需要检查控制设计、组织条件、共同 Context、共因失败与资源约束。

## Audit Trail 与完整性

Audit Trail 候选属性包括：

- Queryability；
- Stable Identity；
- Source / Revision；
- Time / Ordering；
- Cross-system Correlation；
- Tamper Evidence；
- Append-preserving Correction；
- Coverage / Gap；
- Access；
- Data Minimization；
- Retention / Deletion；
- Export；
- Collector Health；
- Drill-down。

`tamper-evident` 被用于替代 `tamper-proof`。

Hash 只能检测内容变化，不证明内容真实；Signature 绑定 Credential，不证明签名者理解；Append-only 不记录从未进入系统的事件。

Correction 使用追加、理由、Authority 与 Supersession，不静默改历史。

## 时间与跨系统关系

工作稿分开：

- Event Time；
- Ingestion Time；
- Commit Time；
- Effective Time；
- Observation Time；
- Recorded Time。

Correlation 可以使用 Work ID、Attempt ID、Execution Epoch、Request ID、Artifact Hash 与单源序列。

Execution Epoch 只作为可选 Correlation Profile，不升级为全书超级生命周期。

Ordering Unknown 必须保留。

## Decision Reconstruction

事故重建分开：

- Contemporaneous View：只使用当时合理可获得的信息；
- Retrospective View：加入后来 Evidence、Outcome 与推导。

重建过程记录 Baseline、Context、Authority、Action、Evidence、Decision、Gap、Observer Failure、Causal Hypothesis 与 Recovery。

Later Evidence 通过 Narrow、Invalidate、Reopen 或 Supersede 连接旧记录。

过去状态和当前状态不塞进一个 `valid` 字段。

## Trace Gap 与 Break-glass

Trace Gap 包括 Collector 缺失、Identity 丢失、Manifest 不存在、Side Effect 未观察、Decision Target 不清、Clock 冲突、Retention 删除或 Integrity Failure。

缺口改变 Coverage，不自动证明 Action 没发生、Subject 有恶意、Target FAIL 或系统健康。

高风险动作可以 Block、Reduce Scope、切换 Supervised、增加 Observation 或使用 Break-glass。

Break-glass 需要保存 Authority、跳过控制、Side Effect、补录与后续 Review。

## Random Audit

HCP 提案中的低风险任务固定 2–5% 抽查比例没有进入正文。

Sampling Contract 需要声明：

- Population；
- Risk / Severity；
- Model / Workflow Version；
- Novelty；
- Reversibility；
- Detection Power；
- Historical Failure；
- Common-mode Risk；
- Human Capacity。

Random、Risk-weighted、New Capability、Adversarial、Incident-triggered 和 Reviewer Rotation 可以组合。

Audit History 可以成为 Autonomy / Reliance Evidence，但不自动形成永久 Trust 或 Authority。

## Retention、Privacy 与成本

Trace 可能包含 Prompt、Source、Secret、Personal Data、Security Finding 与 Incident Detail。

工作稿拒绝“全部永久保留”。

Trace Contract 需要 Purpose、Required Fields、Redaction、Access、Retention、Deletion、Export 与外部服务边界。

具体 Security、Privacy、IP 与 Supply Chain 由第19章拥有。

Traceability 成本包括 Storage、Index、Migration、Collector Reliability、Privacy、Review、Cognitive Load 与 Retention Complexity。

低风险任务可以只保留 Task、Baseline、Commit、Evidence 与 Decision Note。

## Evidence 回接边界

### SP122

CLM-C06-003 支持：

- Plan 在执行前已有不可变 Commit；
- Plan 记录 Lane Owner、Tool / Skill、I/O、Write Surface、Handoff Authority 与 Conflict；
- Manifest 绑定 Plan、Repair Revision、Runtime Identity、Checks、Human Review、Non-claims 与 Hash；
- 后来者无需隐藏推理即可检查执行边界。

不支持：

- 完整 Resume；
- 每个字段必要；
- Trace 提高质量或速度；
- Runtime Identity 等于完整解释；
- Accountability 已经成立。

### AI Game Dev OS Snapshot

Receipt 记录 v4.93 存在 Snapshot Generator，但当时 Registry Artifact 是空 Skeleton。

这支持 Schema Capability、Artifact Existence、Operational Population 与 Audit Use 必须分开。

### D-079

CLM-C09-001 允许后来者从 Commit、Test、Human Decision、Forward Correction 与 Ancestry 区分：

- Test Result；
- Scope Decision；
- Source Adoption；
- Forward Correction；
- Release Non-claim。

它不证明 Human Decision 普遍最优，也不证明较小实现长期成本更低。

## 有意不进入本章的内容

- Git 只能记录 Diff；
- Commit Author 等于全部责任主体；
- Decision Graph 取代 Git 或 Primary Record；
- 完整 Trace 是无 Scope 的绝对状态；
- 时间线自动构成因果；
- Full Transcript 等于 Hidden Reasoning；
- Explainability 需要模型 Chain-of-Thought；
- Context Supplied 等于模型理解；
- Tool Success 等于目标完成；
- Evidence 存在等于 Decision 正确；
- Review PASS 自动完成 Adoption / Release；
- `approved` 无需 Target 和 Authority；
- Agent 成为最终组织或法律责任主体；
- 最后操作者承担全部事故责任；
- Append-only、Hash 或 Signature 证明记录真实完整；
- 缺少日志证明 Action 没发生；
- Trace Gap 等于 Target FAIL；
- 所有高风险活动都能完全重放；
- Replay 覆盖原 Attempt；
- Later Evidence 静默改写历史；
- 固定 2–5% Audit；
- Audit PASS 产生永久 Trust；
- 全部 Prompt、Secret 与 Personal Data 永久保留；
- Registry 文件存在等于 Live Trace 已运行；
- Graph 节点越多越成熟；
- AI Game Dev OS 已验证完整 Traceability / Accountability。

## 与相邻章节的接口

- 第4章拥有 Intent；
- 第5章拥有 Context Contract / Manifest / Access；
- 第6章拥有 State Claim、Decision、Assumption、Provenance 与 Execution Baseline；
- 第7章拥有 Plan、Action 与 State Transition；
- 第9章拥有 Evidence Use、Acceptance、Adoption 与 Release；
- 第12章拥有 HCP Projection；
- 第13章拥有 Authority、Delegation 与 Revocation；
- 第14章拥有 Observation、Detector、Exception 与 Intervention；
- 第15章拥有长期 Memory Provenance、Retention 与 Supersession；
- 第17章拥有 Role、Assignment、Handoff、Conflict 与 Integration；
- 第18章拥有 Trace Contract、Decision Graph、Attribution、Audit、Reconstruction 与 Accountability Evidence；
- 第19章拥有 Data、Model、Secret、Privacy、IP 与 Supply Chain Boundary；
- 第20章拥有运行指标与 Governance Economics。

## 当前审阅点

核心 Claim、对象模型与措辞尚未由作者裁决。下一轮应重点检查：

1. 八概念是否过多，Explainability 是否应单独成节；
2. 十一种 Record Role 是否过细，哪些只需作为关系；
3. Trace Contract YAML 是否应移入附录；
4. Decision Graph Edge 是否应减少到最小核心集；
5. Accountability Surface 是否仍把组织角色写得过于固定；
6. “Agent 不能成为最终责任主体”是否需要更严格限定为本书的组织模型，而非法律结论；
7. Stated Rationale 与 Decision Record 是否重复；
8. Context Trace 是否与第5章重复；
9. Execution Epoch 是否应完全移回 RR-011，而不在正文出现；
10. Tamper-evident 与 Integrity 是否需要更具体 Threat Model；
11. Random Audit 是否属于第20章 AgentOps，而非第18章；
12. Retention / Privacy 是否与第19章重复；
13. SP122 案例是否过多重复第6章；
14. 第18章篇幅是否应在对象裁决后压缩。

## Human Disposition

- CLM-C06-003：unreviewed
- CLM-C18-001：unreviewed
- 章节逻辑与措辞：unreviewed
- Decision by：pending
- Decision at：pending
- Rationale：pending
