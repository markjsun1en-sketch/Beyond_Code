# RR-027：第16章 Self-Evolution Engineering 首轮回接说明

- 记录日期：2026-08-24
- 工作稿：[第16章 Self-Evolution Engineering](../OptimizedDocs/第16章_Self_Evolution_Engineering_首轮修订稿.md)
- 原始结构：[全书大纲第16章](../OringinalDocs/beyond_code_ai_native_software_engineering_outline_zh.md)
- 新增材料：[Cognitive Control、Trust 与 Human Control Plane v0.1](../OringinalDocs/ai_native_cognitive_control_trust_human_control_plane_v0.1.md)
- 核心 Evidence：[CLM-C16-001](../Evidence/receipts/ER-20260824-003__CLM-C16-001.md)，accepted + narrowed，Coverage 为 partial
- 补充案例 Evidence：[CLM-C06-004](../Evidence/receipts/ER-20260818-002__CLM-C06-004.md)、[CLM-OUTLINE-002](../Evidence/receipts/ER-20260818-001__CLM-OUTLINE-002.md)
- 审阅依据：[RR-011](RR-011_Execution_Epoch与治理逻辑.md)、[RR-021](RR-021_Human_Control_Plane与认知控制架构审阅.md)
- 记录性质：章节回接说明，不是新的 Evidence Receipt
- 章节措辞状态：unreviewed

## 回接结果

第16章已经形成独立工作稿。

Self-Evolution Engineering 被限定为：

> 工程系统基于具名经验提出自身配置、流程、Skill、Agent Contract 或组织结构的变更候选，并通过有边界评估、Authority 裁决、采用后观察和恢复机制管理这些候选的过程。

“Evolution”只作为治理工作流名称，不表示变化天然进步，也不表示系统拥有独立意志。

中心链条是：

~~~text
Observed Problem
→ Learning Candidate
→ Change Candidate
→ scoped Baseline and Evaluation
→ Claim-specific Evidence
→ Authority-bound Adoption
→ bounded Activation
→ Post-adoption Observation
→ keep / narrow / expand / revoke / forward-correct
~~~

中心边界是：

> Self-evolution is not self-authorization.

系统可以参与问题发现、Candidate 产生、实现和 Evidence 生成，但不能自行扩大 Grant 或宣布 Improvement。

## 原大纲内容保留情况

| 原大纲主题 | 新工作稿落点 | 处理 |
|---|---|---|
| Execution→Reflection→Pattern→Rule→Validation→Skill Update | 16.3、16.6 | 拆开 Observation、Reflection、Pattern、Candidate、Evaluation、Adoption 与采用后观察 |
| Configuration、Skill / Workflow、Agent Contract、Organization 层级 | 16.5、16.23 | 改为可组合 Evolution Surface，不作为成熟度层级 |
| 自由自我修改风险 | 16.4、16.12、16.15–16.17、16.22 | 保留错误强化、目标投机、边界削弱、局部最优和复杂度风险，并增加 Authority 与 Common-mode Failure |
| Evolution Gate | 16.14 | 拆成 Candidate、Evaluation、Result、Adoption、Activation、Release、Expansion 与 Recovery Decision |
| Learning from Failure | 16.7 | 先区分结果，再把原因写成可重叠 Candidate |
| Self-Evolution 与 Self-Modification | 16.4 | Self-modification 只描述机制；是否值得采用需要独立评估 |

原大纲核心问题得到保留，但线性学习流水线、层级进化和一个 Gate 完成全部裁决的表达没有沿用。

## Change、Calibration、Adoption 与 Improvement

工作稿明确：

- Change 是状态变化，不含价值判断；
- Calibration 是对具名环境和阶段的适配过程；
- Adoption 是有权主体作出的使用决定；
- Improvement Claim 需要 Objective、Guardrail、Scope、环境和观察窗口支持。

Candidate Created、Merged、Test PASS、Adopted 与 Improvement Supported 是不同状态。

## 九个对象

工作稿分开：

1. Change Signal；
2. Learning Candidate；
3. Change Candidate；
4. Scoped Accepted Baseline；
5. Evaluation Contract；
6. Evaluation Evidence；
7. Adoption Decision；
8. Activation / Rollout Record；
9. Post-adoption Disposition。

紧急安全修复可以在具名 Authority 下跳过普通比较，但必须记录无法建立的 Evidence、不可逆边界和后续 Review。

## Reflection、Pattern 与 Failure

Reflection 被标记为 Retrospective Inference，不是 Observation。Pattern Candidate 需要 Source、Sampling Boundary、Counterexample、Alternative Explanation、Scope 和 Intended Use。

Failure 先区分 target fail、target pass but unaccepted、non-result、partial、intervention failure 与 escaped failure。Environment、Tool、Reasoning、Design、Workflow、Authority、Context、State、Observer、Dependency、Coordination 和 Human Decision 只作为可重叠 Cause Candidate。

D-048 的 Verifier Self-mutation 与 Target non-result 由 CLM-C06-004 支持，没有由 CLM-C16-001 越界覆盖。

## Baseline 与 Comparability

Known-Good 被改为 Scoped Accepted Baseline。Baseline 只有在仍安全、适用、可访问和值得维护时，才作为比较或恢复点。

Comparability 检查 Task、Input、Data、Model、Tool、Context、Authority、Reviewer、Environment、Order Effect、Sample、Coverage 与 Failure Semantics。

低频、高变异或创意任务可以使用 Expert Review、Replay、Bounded Pilot、Failure Injection 和显式不确定性，不用伪精确数字替代不可比性。

## Evaluation、Objective 与 Guardrail

Evaluation Contract 先定义 Claim，再选择指标。工作稿分别声明 Primary Objective、Quality Guardrail、Safety / Authority Guardrail、Recovery Guardrail、Human / Creative Guardrail 与 Cost Boundary。

Guardrail 必须指向具体风险、Observation、Owner 和阶段；无法说明保护对象的控制可能重新制造 Governance Overload。

Human Creative Calibration 被保留为具名创意责任人的可追踪判断，不由单一机器指标替代。

## Gate、Authority 与独立性

统一 Evolution Gate 被拆成多个 Decision Target，避免 Test PASS 同时完成 Adoption、Activation、Release 和 Expansion。

高影响、自我扩权或改变验证机制的 Candidate 不应只依赖 Producer 的 Summary 与自选 Evidence。独立性与风险相称，可以来自 Deterministic Check、Independent Reviewer、Human、Shadow Comparison、External Harness 或 Counterexample Search。

执行主体可以提出 Authority Change Proposal，不能自行批准扩大自身 Grant。

## Activation、Recovery 与 Post-adoption

Offline Replay、Shadow Mode、Sandbox、Canary 和 Parallel Path 被列为可选评估方式。

Adoption、Activation、Release、Expansion 和 Improvement Supported 分开记录。

Recovery 不默认等于 Rollback。不可逆或旧 Baseline 已失效的变化需要 Forward Correction。

采用后继续观察 Objective、Guardrail、Failure、Rework、Detector Health、Scope、Authority、Creative Diversity、Governance Cost 与 Recovery Readiness。

## Production 与 Exploration

Production / Reliability Path 与 Controlled Exploration Path 可以使用不同 Objective、Risk Budget、Evidence、Discard Tolerance、Authority 和 Adoption Gate。

固定 80/20 比例没有进入正文。Exploration Budget 需要由 Human 或有权 Policy 保护，探索结果仍不能绕过 Production Adoption。

## Evidence 回接边界

CLM-C16-001 支持：

- D-073 至 D-075 形成具名 Observed Problem；
- D-076 是 scoped、retractable Pilot，Dual Review PASS 只产生 Human Disposition Eligibility；
- D-079 的 42 Tests PASS 不产生 Scope Acceptance；
- Forward Correction 可以保留历史并形成后续 Baseline；
- Candidate、Evidence、Adoption 和 Release 必须分开；
- 没有受控数据证明新 Workflow 全局更优。

CLM-OUTLINE-002 补充支持 Function-first Closure 和 F4a 48/48 PASS NON_QUALIFYING，没有把该事实错误归入 CLM-C16-001。

这些 Evidence 不证明 Workflow Calibration 提高长期效率、质量或 Human Attention，也不证明 Function-first 是恢复的唯一原因、本章对象完整或所有 Candidate 都可回滚。

## 有意不进入本章的内容

- Self-modification 自动构成 Evolution；
- Candidate 产生即表示系统已经学习；
- Merge、Test PASS、Review PASS 或 Adoption 自动构成 Improvement；
- Reflection 或 Root Cause Candidate 被写成 Observable Fact；
- 一次 Failure 自动生成永久 Rule；
- 配置、Workflow、Contract 与 Organization 是成熟度层级；
- Baseline 永远 Known-Good；
- 不可比任务仍计算精确改进百分比；
- Human Interruption 下降自动表示 Workflow 变好；
- Guardrail 越多越安全；
- 一个 Evolution Gate 拥有所有 Authority；
- Candidate 可以修改自己的 Authority、Detector 与 Policy Floor；
- Shadow PASS 证明 Production Safety；
- Rollback Command 证明状态恢复；
- 固定 Exploration 比例；
- 增加 Agent 或 Gate 数量即组织进化；
- v4.94 已证明 Function-first 普遍最优；
- 48/48 PASS NON_QUALIFYING 被写成完整 Qualification。

## 与相邻章节的接口

- 第15章拥有 Memory Candidate、Provenance、Conflict 与 Expiry；
- 第14章拥有 Change Signal 所需 Observation、Exception 与采用后 Telemetry；
- 第13章拥有 Evaluation、Adoption、Activation 与 Recovery Authority；
- 第9章拥有 Evidence Use、Acceptance、Adoption 与 Release；
- 第16章拥有 Learning Candidate、Change Candidate、Evaluation、Adoption 和 Post-adoption Disposition；
- 第17章拥有 Agent Role、Handoff、Conflict 与 Organization Design；
- 第20章拥有长期指标与 Governance Economics；
- 第23章拥有完整案例时间线。

## 当前审阅点

核心 Claim 已接受，但章节措辞和扩展对象仍未由作者单独裁决。下一轮应重点检查：

1. “Self-Evolution” 是否仍然概念过重，标题是否应改为 Governed System Change；
2. 九对象是否过细，Learning Candidate 与 Change Candidate 是否需要合并；
3. Evolution Surface 是否需要保留 Governance / Policy 类别；
4. 两段 YAML 是否应移入附录；
5. Failure Cause Candidate 是否把 Human Decision 写得过于工程化；
6. Gate 拆分是否与第9章重复；
7. Creative Calibration 是否应移入创意工程章节；
8. Production / Exploration 是否属于本章；
9. v4.94 案例篇幅是否与 partial Coverage 相称。

## Human Disposition

- 核心 Claim：accepted + narrowed
- 章节逻辑与措辞：unreviewed
- Decision by：pending
- Decision at：pending
- Rationale：已接受范围只覆盖重要、可版本化、可逆或可前向恢复的重复 Workflow；向 Configuration、Skill、Agent Contract、Policy 和 Organization 的扩展仍等待作者裁决。
