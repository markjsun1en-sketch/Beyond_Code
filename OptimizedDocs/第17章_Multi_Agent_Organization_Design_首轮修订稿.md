# 第17章 Multi-Agent Organization Design
## Agent 数量不是组织证据；可治理安排需要显式角色、Authority、接口与责任闭环

> 工作稿状态：首轮逻辑修订稿，不替代 [全书大纲](../OringinalDocs/beyond_code_ai_native_software_engineering_outline_zh.md) 或 [Cognitive Control、Trust 与 Human Control Plane v0.1](../OringinalDocs/ai_native_cognitive_control_trust_human_control_plane_v0.1.md)。
> 回接说明：[RR-028](../RevisedResult/RR-028_第17章Multi_Agent_Organization_Design首轮回接说明.md)。
> 适用边界：本章提出一个候选组织模型，用于区分 Work、Role、Assignment、Authority、Handoff、Conflict 与 Integration；它不声称多 Agent 必然提高质量、速度或成本表现。

多个 Agent 可以同时：

- 搜索；
- 规划；
- 实现；
- 审阅；
- 测试；
- 总结；
- 生成更多 Agent。

这不表示项目已经形成组织。

如果缺少边界，多 Agent 更可能扩大：

- 重复劳动；
- Context 分叉；
- 决策冲突；
- Authority 重叠；
- 共享状态竞争；
- Handoff 损失；
- Review 共因失败；
- 输出洪水；
- Coordination Cost；
- 无人负责的尾部问题。

本章使用的工作定义是：

> **Multi-Agent Organization Design（多 Agent 组织设计：把具名工作、角色契约、Subject、Authority、责任、依赖、交接、冲突和集成处置组织成可检查协作关系的工程活动）**。

组织不是 Agent 数量。

组织是：

> 谁在什么边界内承担什么义务，拥有什么 Decision Authority，向谁提供什么可检查输出，发生冲突或失败时由谁继续处置。

---

# 17.1 先区分必要、有用与可选

## 必要

只要多个 Human、Agent 或 Gate 共同影响同一结果，项目就需要最小的：

- Work Ownership；
- Authority Boundary；
- Dependency；
- Handoff；
- Conflict / Escalation；
- Final Disposition。

这些规则也适用于 Human-only 团队。

## 有用

当工作可分离、需要不同 Domain Expertise、需要风险相称的独立审阅，或单一 Context 已难以承载全部表面时，多个 Role / Subject 可能有用。

## 可选

Controller、Planner、Specialist、Reviewer、QA、Researcher、Knowledge Miner、Security Agent 与 Release Agent 都是可选 Role Profile，不是 AI-native 项目的必备岗位。

低风险、紧耦合或规模很小的任务，单 Agent 加清楚 Tool 和 Human Checkpoint 可能成本更低。

---

# 17.2 Agent、Subject、Role、Persona 与 Skill 需要分开

**Agent Instance（Agent 实例：在具名时间运行、具有可识别模型、Contract、Context、Tool 与状态边界的执行实例）** 是运行主体的一种。

**Delegated Subject（受托主体：被 Authority Grant 和 Assignment 识别、可承担具名动作或决定的 Human、Agent、Gate 或组合配置）** 是治理对象。

**Role（角色：围绕某类 Decision Lens、责任、输入、输出和升级路径定义的可复用工作契约）** 不是某个模型的人格。

**Persona（人格化表达：用于影响沟通风格、视角或探索方式的提示性设定）** 不自动拥有 Responsibility 或 Authority。

**Subject Configuration（主体配置：对承担 Work 的具名 Human、Agent 或 Gate 及其模型／版本、运行边界、Context 与 Tool 配置的引用集合）** 使同一个 Role 在不同执行条件下可被区分。

Skill 提供 Method、Procedure 或 Tool Binding，不定义完整 Role。

因此：

~~~text
Agent Instance / Human / Gate
+ Role Contract
+ Assignment
+ Authority Grant
+ Work Reference
→ Delegated Subject for this organizational relation
~~~

同一个 Agent Instance 可以先后承担多个 Role。

但同一实例换一个 Role 名称，不会自动形成 Review Independence。

---

# 17.3 九个候选对象展开组织关系

本章区分：

| 对象 | 回答的问题 |
|---|---|
| Work Reference | 当前协作关系服务哪个由第7章定义的 Work |
| Role Contract | 以什么责任、视角、接口和禁区工作 |
| Subject Configuration | 哪个 Human、Agent 或 Gate 以什么配置承担 Role |
| Assignment | 谁在什么时间和 Scope 被绑定到哪个 Work |
| Authority Reference | Subject 可以采取或裁决哪些动作 |
| Dependency / Coordination Relation | 与其他 Work 或 Subject 怎样关联 |
| Handoff Package / Receipt | 交出了什么，接收方接受了什么 |
| Conflict Record | 哪些 Claim、Decision、Authority 或资源关系发生冲突 |
| Integration Disposition | 哪些输出被保留、拒绝、组合、返工或升级 |

**Work Reference（工作引用）** 指向第7章拥有的 Work，并在本章说明组织关系服务哪个具名目标、Scope、依赖与关闭边界。本章不建立第二个 `Work Unit` 上位对象；开放式 Prompt 也不能替代 Work Reference。

**Role Contract（角色契约：声明 Role 的目标、责任、Decision Lens、输入、输出、Authority、禁区、Evidence 和升级路径的约束）** 是组织接口。

**Assignment（任务绑定：在具名时间把 Subject Configuration、Role Contract、Work Reference 和 Authority Reference 绑定起来的记录）** 使“谁负责”可检查。

**Integration Disposition（集成处置：具名 Authority 通过 Decision Record，对多个输出如何被接受、组合、拒绝、返工或升级这一具名 Decision Target 作出的处置）** 是第9章 Disposition 的 Target-specific subtype，不等于 Merge Command。

基本关系是：

~~~text
Work Reference
+ Role Contract
+ Subject Configuration
+ Assignment
+ Authority Reference
→ bounded execution
→ candidate output + Evidence + Unknown
→ Handoff / Review / Conflict
→ Integration Disposition
→ next state and responsibility
~~~

Responsibility 与 Accountability 横切整条链。

---

# 17.4 Role Contract 不是职位名称

本章的候选 Role Contract 关注：

- Purpose；
- Decision Lens；
- Responsibilities；
- Allowed Decisions；
- Prohibited Decisions；
- Inputs；
- Required Source Access；
- Outputs；
- Evidence Obligations；
- Escalation；
- Handoff Target；
- Stop Condition；
- Expiry。

候选示例：

~~~yaml
role_id: independent-scope-reviewer
version: 3

purpose:
  - assess_candidate_scope_fit

responsibilities:
  - inspect_candidate_and_declared_non_goals
  - identify_over_scope_and_missing_evidence
  - preserve_counterevidence

allowed_decisions:
  - review_disposition_for_scope

prohibited:
  - modify_candidate_source
  - approve_release
  - expand_own_review_scope

inputs:
  - intent_ref
  - candidate_ref
  - baseline_ref
  - evidence_refs

outputs:
  - review_record
  - blocker_or_non_blocker_findings
  - unresolved_unknowns

escalation:
  - authority_conflict
  - missing_primary_source
  - unsafe_action_reachable
~~~

这是设计 Profile，不是通用 Schema。

“你是 Reviewer”没有说明 Reviewer 能否 Reject、Block、Recommend 或 Adopt。

---

# 17.5 Role Library 是组合工具，不是固定组织图

常见 Role 可以包括：

| Role | 主要输出 | 常见边界 |
|---|---|---|
| Coordinator / Controller | Work 分配、依赖、状态投影、升级 | 不自动拥有全部 Decision Authority |
| Planner | Plan Candidate、Dependency、Unknown | Plan 不是 Execution Authority |
| Builder / Worker | Candidate Artifact、Diff、运行 Evidence | 输出不是 Adoption |
| Specialist | Domain Analysis 或实现 | 专业判断不覆盖项目 Authority |
| Reviewer | Finding、Counterexample、Disposition Recommendation | 是否能 Block 取决于 Grant |
| Validator | 对具名 Claim 的检查结果 | PASS 不扩张 Decision Target |
| Challenger | 反例、隐藏假设、替代解释 | 不负责自动重写 Candidate |
| QA / Tester | Scenario、Result、Coverage、Defect | 不自动决定产品采用 |
| Researcher | Source、Synthesis、Uncertainty | 搜索命中不是项目事实 |
| Knowledge Curator | Memory Candidate、Provenance、Conflict | 不产生 Truth |
| Security / Privacy Reviewer | Threat、Boundary、Required Control | Risk Finding 不自动扩大自己的 Authority |
| Release Role | Release Evidence 与处置输入 | Release Authority 需另行显式授予 |

Role 可以组合，也可以由 Human 承担。

原大纲中的 Cognition Agent 没有被保留为稳定 Role 名称。Attention Routing、Compression Validation、Exception Detection、Human Interface 与 Organization Review 属于不同 Responsibility，把它们合并成“认知角色”会再次制造超级对象。

Role 数量应由真实分工触发，不由“组织看起来完整”触发。

---

# 17.6 Responsibility、Authority、Permission 与 Accountability 分开

**Responsibility（职责：某个 Role 被要求执行、维护、响应、升级或恢复某项工作的义务）** 不表示它拥有所有相关决策权。

Authority 决定可以采取或裁决什么。

Permission 决定平台技术上允许什么。

第18章把 Accountability 定义为组织要求具名 Human 或角色对目标、控制设计、授权、复核、处置、运行或恢复承担解释、审查、纠正或后果责任的规范性关系；它不能简单推给模型。

本章只说明 Responsibility 怎样随 Assignment 与 Handoff 分配，并引用该 Accountability 关系。Trace 或执行日志可以支持 Attribution，却不会自动产生组织问责；法律责任也不能由这些对象直接推出。

例如：

~~~text
Worker
responsible for implementation and evidence
not authorized to release

Reviewer
responsible for independent finding
authorized to reject a named Decision Target for closing or continuing that Review Target
not authorized to rewrite policy

Human Product Owner
accountable for product adoption
not authorized to bypass security policy alone
~~~

“Owner”需要说明它是 Work Owner、Decision Owner、Recovery Owner、Artifact Maintainer 还是 Accountable Human。

---

# 17.7 Assignment 需要身份、容量和接受状态

一个 Assignment 不只是：

~~~text
Agent A → Task B
~~~

还需要：

- Assignment ID；
- Work Reference；
- Role Contract Version；
- Subject Configuration；
- Authority Reference；
- Start / Expiry；
- Input / Context Contract；
- Expected Output；
- Dependency；
- Capacity / Budget；
- Stop / Cancel；
- Reassignment；
- Acceptance Status。

Subject 可以：

- accept；
- reject_out_of_scope；
- request_missing_input；
- request_authority；
- defer_due_to_dependency；
- return_non_result。

强制把不完整 Assignment 视为已接受，会把输入缺口隐藏成执行失败。

---

# 17.8 Work Decomposition 先按接口和风险，而不是按 Agent 数量

适合并行的 Work 通常具有：

- 可独立描述的输出；
- 清楚输入；
- 有限共享写面；
- 可识别依赖；
- 可单独验证的 Claim；
- 明确 Integration Owner；
- 失败不会让其他单元不可解释。

不适合过度拆分的工作可能：

- 高度共享隐含 Context；
- 需要连续创意判断；
- 每一步都会改变下一步问题；
- 共享同一小段代码或状态；
- 集成成本高于执行成本；
- 责任无法单独定位。

多 Agent 并行不是默认目标。

更准确的目标是：

> 在不丢失决策连续性和责任的前提下，选择合适的并行、串行或协作边界。

---

# 17.9 Coordination Topology 没有通用最优

**Coordination Topology（协作拓扑：Role / Subject 之间分配工作、交换状态、提交决定和升级冲突的关系结构）** 可以包括：

| Topology | 优点 | 主要失败模式 |
|---|---|---|
| Central Coordinator | 全局路由清楚，便于限流 | Bottleneck、单点错误、Context 压缩损失 |
| Pipeline | 接口明确，适合阶段性产物 | Handoff Loss、局部优化、反馈延迟 |
| Peer Collaboration | 适合探索和多视角 | Authority 冲突、重复工作、共识成本 |
| Builder–Reviewer | 生产与挑战分开 | Review Capture、往返循环 |
| Specialist Hub | Domain 复用 | 中央整合负担、知识孤岛 |
| Human-led Cell | 价值和风险判断明确 | Human Bottleneck、等待 |

一个项目可以同时使用多种 Topology。

Topology 是 Profile，不是成熟度等级。

---

# 17.10 Controller 首先是协调 Role，不是超级 Authority

原大纲为 Controller 分配：

- 维持全局 Intent；
- 控制 Context；
- 限制 Worker Scope；
- 汇总结果；
- 管理认知负载；
- 触发 Human Decision。

这些功能有用，但不应全部收进一个超级对象。

可以拆成：

~~~text
Intent Custody
Work Coordination
Context Routing
Dependency Tracking
Integration
Attention Routing
Escalation
~~~

Controller 可以持有其中部分 Responsibility。

它不自动：

- 拥有 Truth；
- 改写 Human Intent；
- 授予自己 Authority；
- 取代 Domain Reviewer；
- 接受所有输出；
- 代表 Human 作价值判断；
- 覆盖 Policy Gate。

中央 Controller 的 Summary 也是派生投影，需要 Source Link、Unknown 和 Conflict。

---

# 17.11 Worker 交付的是 Candidate，不是自动成立的结果

Worker 的主要职责可以是：

- 在 Work 内生成 Candidate Artifact；
- 保留实际修改、运行结果与 Evidence；
- 标记 Assumption、Unknown、Blocker 和 `non-result`；
- 说明超出 Scope 的问题；
- 在条件失效时停止、拒绝或请求升级。

Worker 不因为完成了交付就自动获得：

- Claim Acceptance；
- Scope Acceptance；
- Adoption；
- Integration；
- Release；
- Authority Expansion。

即使 Worker 同时运行了测试，测试结果也只支持其声明的行为 Claim，除非项目已把具名决定明确授权给该 Gate。

Worker 返回 `non-result` 不是逃避责任。当必要输入、Authority、Tool、环境或 Observation 不成立时，一条可解释的 `non-result` 比虚构完成更有组织价值。

---

# 17.12 Controller / Worker 不是普适的上下级关系

Controller 可以分配 Work，但不表示它对 Worker 所在 Domain 拥有更高的判断能力或 Decision Authority。

Worker 也不是被动的 Tool。它可以对下列情况发起反向信号：

- Assignment 与 Source State 冲突；
- 原定 Scope 无法产生所需 Evidence；
- 前置依赖已过期；
- 实际风险超过 Grant；
- 需要另一个 Role 作决定；
- 当前任务已不再值得继续。

可以用下列关系理解：

~~~text
Controller --coordinates--> Work and dependencies
Worker --produces-------> Candidate and execution evidence
Worker --escalates------> changed conditions and missing authority
Reviewer --challenges---> named claim or candidate
Authority Holder --creates-------> Decision Record for named target
Decision Record --records-------> target-specific disposition
~~~

Human、Policy Gate 或 Domain Owner 可以在 Controller / Worker 关系之外持有一些 Decision Authority。

因此，一条 Controller 调度链不应被画成项目全部的 Authority Hierarchy。

---

# 17.13 Planner 产生 Plan Candidate，不产生默认执行权

Planner 可以负责：

- 拆分 Work；
- 识别 Dependency 与 Critical Path；
- 声明 Assumption 和 Unknown；
- 提议顺序、并行度与 Stop Condition；
- 标记需要的 Authority 和 Evidence。

这些输出是 **Plan Candidate（计划候选：对工作拆分、顺序、依赖、资源和关闭条件的可审查提案）**。

Plan Accepted、Assignment Created 与 Execution Authorized 是不同状态。

执行中可能出现新 Evidence、Source Drift 或 Dependency Failure。此时应保留原计划与修订理由，而不是让 Worker 暗中完成无记录的 Replanning。

但计划也不需要在开工前穷尽所有可能。当探索价值高于预先建模价值时，一个有 Scope、Budget 和 Stop Condition 的试探 Work 可能更合理。

---

# 17.14 Reviewer、Validator 与 Challenger 不是同一种决定

**Reviewer（审阅角色：根据第10章定义的具名 Review Contract，检查 Candidate 与目标、范围、风险或完整性关系的角色）** 通常输出 Finding 和 Disposition Recommendation。

**Validator（验证角色：对具名 Claim、Contract 或行为条件运行指定检查的角色）** 回答被验证对象是否在声明覆盖内成立。

**Challenger（反证角色：主动寻找反例、隐藏假设、替代解释和适用边界的角色）** 不以快速达成一致为目标。

低风险工作中，这些 Role 可以合并。但记录仍需声明：

- 当前检查的 Review Target 与 Intended Decision Use；
- 对哪个 Claim 发言；
- 覆盖了什么；
- 没有覆盖什么；
- 结论是建议、阻断还是有权裁决。

`PASS` 不应成为一个无范围的组织动词。

---

# 17.15 组织拓扑如何实现 Review Independence

第10章拥有 Review Independence 的正式定义。本章只说明 Role、Subject Configuration 与协作拓扑如何实现或削弱它；不同 Role 名称本身不构成独立性。

组织设计直接沿用[第10章的七维定义](第10章_Review_Engineering_首轮修订稿.md)，这里只检查拓扑新增的问题：Producer 与 Reviewer 是否属于可区分的 Subject Configuration，是否共享同一 Context、Source、Model、Method 与失败假设，Reviewer 的 Finding 是否能在不被 Producer 改写的情况下到达具名 Decision Authority。

两个具有不同名称、但使用同一模型、同一 Prompt、同一 Summary 和同一失败假设的 Agent，可以提供额外采样，但不应被写成完整独立审阅。

反过来，独立 Reviewer 也不自动正确。提高这些维度的分离，是为了减少对同一 Source、Summary、Method 与失败假设的依赖；现有材料不证明它已经降低实际共因失败，也不能消除能力不足、Source 缺失或错误 Contract。

独立性要求应与风险、不可逆性、影响面和 Self-referential Change 相称。

---

# 17.16 Structured Handoff 交付最小的可继续性

**Handoff Package（交接包：交出方为下一个 Role 组织的有来源状态、产物、决定、Evidence、Unknown 与风险集合）** 的目标不是转存全部 Context，而是使接收方能识别：

- 自己正在接受什么；
- 哪些结论已经裁决；
- 哪些仍是 Candidate；
- 哪些条件尚未成立；
- 下一个动作需要什么 Authority。

候选 Contract：

~~~yaml
handoff_id: HO-017
work_unit_ref: WU-042

from:
  subject_ref: agent-builder-2
  role_ref: bounded-builder-v3
to:
  requested_role_ref: scope-reviewer-v2

goal_and_intent_ref:
  - INT-008

candidate_and_baseline:
  candidate_ref: commit-or-artifact-ref
  baseline_ref: scoped-baseline-ref

current_state:
  completed:
    - bounded_implementation
  actual_changes:
    - source_diff_ref
  in_flight:
    - none

decisions:
  - decision_ref: DEC-021
    status: accepted_for_evaluation

assumptions:
  - external_contract_unchanged
evidence_refs:
  - EV-101
counterevidence_refs:
  - EV-104
unknowns:
  - production_latency
non_results:
  - scenario_x_not_observed
blockers:
  - none
open_risks:
  - shared_state_race

requested_next_action:
  - review_scope_fit
requested_authority:
  - review_disposition_only

source_links:
  - task_ref
  - diff_ref
expires_at: named-condition-or-time
~~~

这是设计 Profile，不是每次必填的通用表单。

小任务可用更小的 Handoff，但不应删掉会改变接收方决定的 Unknown、Counterevidence 和 Authority Boundary。

---

# 17.17 Handoff Submitted 不等于 Handoff Accepted

**Handoff Receipt（交接回执：接收方对交接包的可读性、范围、缺失与接管状态作出的记录）** 可以是：

- `accepted_for_named_work`；
- `partially_accepted`；
- `rejected_out_of_scope`；
- `missing_required_input`；
- `authority_not_available`；
- `dependency_not_ready`；
- `superseded`。

Receipt 应说明：

- 接受哪些 Work 和 Artifact Custody；
- 从哪个时点起承担哪些继续职责；
- 哪些输入仍未验证；
- 哪些决定权没有随交接转移；
- 不接受时返回给谁。

接收 Handoff 只表示接管具名工作或保管具名产物。

它不自动表示：

- 交出方的 Claim 为真；
- Candidate 被采用；
- 所有风险已被接管；
- Authority 已完整转移；
- 原责任主体不再需要解释其已完成的决定。

---

# 17.18 共享状态应少而有来源，Context 应按 Role 投影

多 Agent 组织需要某些 **Shared Organizational State（共享组织状态：为协作公开的 Work、Assignment、Dependency、Decision、Authority 和 Handoff 索引）**。

但这不意味着建立一个无边界的全员 Prompt。

更稳妥的结构是：

~~~text
authoritative source records
        ↓
small shared coordination index
        ↓
role-specific Context Projection
        ↓
Source-linked decisions and outputs
~~~

Shared State 保留 Identity、Version、Freshness、Source Link 和 Conflict。

Role-specific Context 只传递完成当前 Contract 所需的信息，并允许下钻原始记录。

两条边界同时成立：

> 无来源的全局 Summary 可能成为第二个状态库。

> 拥有源文件的访问权，也不表示 Subject 已经理解其适用性。

---

# 17.19 Conflict 不只是两个 Agent 给出不同答案

**Conflict Record（冲突记录：保留不相容 Claim、Decision、Authority、Policy、Dependency、资源或创意方向及其未决状态的对象）** 首先需要给冲突分型：

| 冲突类型 | 核心问题 | 不充分的处理 |
|---|---|---|
| Observable State Conflict | 对同一状态有不同观察 | 按 Agent 声望投票 |
| Evidence Interpretation Conflict | 承认同一 Evidence，但对支持范围理解不同 | 只比文件数量 |
| Design / Strategy Conflict | 两种方案保护不同目标或 Trade-off | 伪装成单一事实问题 |
| Authority Conflict | 两个 Grant 覆盖或互相否定 | 让执行更快的 Subject 获胜 |
| Policy / Instruction Conflict | 上层约束与局部任务不相容 | 由局部 Prompt 覆盖 Policy |
| Dependency / Resource Conflict | 顺序、容量或共享写面不兼容 | 归因于某个 Agent 不够智能 |
| Creative / Value Conflict | 审美、方向或体验判断不同 | 用虚构精确分数消除判断 |
| Responsibility Conflict | 没有主体愿意或能够接管后续 | 把任务标成 Done |

分型不是为了一次解决，而是为了找到合适的 Source、Decision Target 和 Authority。

---

# 17.20 Conflict Resolution 先解析冲突，再选择处置方式

原大纲中的“事实优先级、角色权限、证据强度、风险升级、人类裁决”保留为问题清单，不保留为一条机械排序。

处理步骤可以是：

1. 命名冲突对象与当前 Decision Target；
2. 分开 Observable Fact、Contemporaneous Judgment、Retrospective Inference 与 Recommendation；
3. 标识 Source Identity、Version、Freshness 与 Applicability；
4. 检查 Evidence 是否适配 Claim Type；
5. 查找重叠、缺失或已失效的 Authority；
6. 声明每个方案保护的 Objective、Guardrail 与代价；
7. 根据风险选择 Clarify、Test、Narrow、Split、Defer、Escalate 或 Reject；
8. 由拥有该 Decision Target 的主体记录 Disposition；
9. 保留 Minority Position、Unknown 和 Reopen Condition。

“证据更强”只在 Evidence 可比且回答同一 Claim 时才有意义。Runtime Claim 与价值判断不能进入同一条强弱排行。

Human 裁决也不是默认最后一格。只有当 Human 对该价值、风险接受或组织设计真正持有 Authority 时，这个路径才成立。

---

# 17.21 Deadlock 与 Livelock 是组织失败，不只是调度失败

**Deadlock（死锁：多个 Work、Subject 或 Authority 互相等待，无一方能在现有条件下继续）** 可能来自：

- 循环 Dependency；
- 交叉 Approval；
- 无人拥有的 Decision Target；
- 交接两端都在等对方先接管；
- 回收 Grant 后没有 Recovery Owner。

**Livelock（活锁：系统持续生成响应、审查或后续任务，却不使原目标更接近可裁决状态）** 可能表现为：

- Reviewer 和 Worker 无限返工；
- Controller 不断创建元任务；
- 每个新 Governance Record 又触发一个新 Record；
- 越来越多 Agent 参与同一个未定义 Decision；
- 没有终止语义的 Automatic Successor。

应对方式包括：

- 在创建工作前检查依赖图；
- 为 Review Loop 设置返回类型、Budget 和升级条件；
- 使用可观察 Deadline，但不把超时自动解释为失败原因；
- 阻止无 Authority 的自动后续；
- 在无法进展时产生 Blocked Receipt，而不是继续制造活动。

---

# 17.22 Parallel Execution 需要 Isolation 和 Integration Disposition

并行放大的不只是吞吐，还包括：

- 共享写面竞争；
- Baseline Drift；
- 重复修改；
- 测试和环境相互污染；
- 不兼容的 Assumption；
- Merge 成功却语义冲突。

风险越高，越需要明确：

- Artifact Ownership；
- Write Surface；
- Worktree / Sandbox / Environment Isolation；
- Shared Resource Lock 或 Reservation；
- Baseline Identity；
- Rebase / Refresh Condition；
- Integration Order；
- Conflict Owner；
- Recovery Point。

Integration 的结果可以是：

- `accepted_as_is`；
- `accepted_with_narrowing`；
- `combined_with_other_candidate`；
- `returned_for_rework`；
- `rejected`；
- `deferred`；
- `superseded`；
- `non_integrable_for_current_baseline`。

Integration Owner 负责形成该处置，但只在 Grant 允许时才能执行 Merge、Adoption 或 Release。

---

# 17.23 下游委托不会自动携带上游 Authority

当 Controller 或 Worker 创建下游 Agent 时，需要区分：

- 有权创建 Assignment；
- 有权转授某些 Decision Authority；
- 有权扩大 Work Scope；
- 有权分配 Credential 或 Tool Permission；
- 有权接受下游输出。

这些不是同一件事。

委托链应声明：

- Maximum Delegation Depth；
- Transferrable / Non-transferrable Authority；
- Delegated Scope；
- Required Evidence；
- Expiry；
- Revocation；
- In-flight Disposition；
- Credential 与 Memory 的回收方式。

上游 Grant 被撤销时，需要检查下游委托是否一起失效。

但级联撤销也不应被简化为 Kill Signal：已产生的外部副作用、进行中交接、Credential、Memory Candidate 和待裁决产物都需要处置。

---

# 17.24 输出洪水需要流量控制，不是只需要更强 Summary

多 Agent 可能同时生成：

- Candidate；
- Finding；
- Question；
- Evidence；
- Conflict；
- Handoff；
- Exception；
- 新的 Work Proposal。

不加区分地全部推给 Human，会把运算并行变成判断串行。

可用的组织控制包括：

- WIP Limit；
- 按 Decision Target 分组；
- 合并重复 Finding，但保留来源；
- 区分 Blocker、Risk、Unknown 和 Informational Update；
- 只在需要新 Authority 时升级；
- 为低风险、已授权决定建立自动处置；
- 保留 Drill-down 和 Source Link；
- 对 Summary 做 Sampling 或 Omission Check。

Controller 压缩了信息，不表示判断负担已经下降。

如果 Human 还需要重新阅读所有 Source 才能信任它，或 Summary 系统性丢失 Counterevidence，组织只是改变了成本的位置。

---

# 17.25 Human-Agent Organization 不应把 Human 写成每一步的默认 Gate

Human 可能承担：

- Intent Owner；
- Product / Creative Owner；
- Policy Author；
- Risk Acceptance Authority；
- Domain Reviewer；
- Organization Designer；
- Exception Handler；
- Recovery Owner；
- Accountable Executive 或其他具名责任。

但“Human in the Loop”没有说明：

- 哪个 Human；
- 决定什么；
- 根据什么决定；
- 是 Approval、Override、Appeal 还是 Takeover；
- 是否有能力和时间处置；
- 哪些 Policy 连 Human 也不能单方越过。

人类不必然是所有低风险工作的最终按钮。一个获得清楚 Grant 的 Gate 可以在限定范围内自动处置。

人类也不必然拥有任意 Override。Security Policy、法规、多方授权或审批分离可以约束个人决定。

本书中 Human 的核心不是人工点击，而是把价值、风险承担、方向和组织设计绑定到真实的责任主体。

---

# 17.26 Human Role Migration 不是线性成熟度阶梯

原大纲提出 Human 从实现者转向意图定义者、规则制定者、风险承担者、最终决策者、组织设计者和价值判断者。

这个方向可以作为角色重新分配的假设，但不应写成通用迁移轨迹。

在同一项目中，同一个 Human 可能同时：

- 亲自编辑高语义密度代码；
- 审阅 Agent Candidate；
- 定义产品意图；
- 处理 Exception；
- 批准高风险处置；
- 调整 Role 和 Authority。

更准确的模型是 **Capability-relative Role Allocation（按能力、风险和当前条件分配角色）**，而不是“人类逐步退出实现”。

该分配会随模型能力、Tool Reliability、业务知识、项目阶段、事故状态和 Human Availability 变化。

---

# 17.27 Organization Observability 观察可见行为，不推测隐藏思维

**Organization Observability（组织可观测性：从可见记录中检查 Work、Assignment、Dependency、Authority、Handoff、Decision 和失败状态的能力）** 可以优先支持查询：

- 当前有哪些 Work；
- 由谁以哪个 Role 接受；
- 使用哪个 Contract 和 Authority；
- 依赖哪个 Baseline、Source 或其他 Work；
- 正在运行、等待、Blocked、Cancelled 还是 Unknown；
- 产生了什么 Candidate、Evidence 和 `non-result`；
- 交给了谁，是否接收；
- 当前冲突和待裁决 Decision 是什么。

`running` 不表示正在取得有效进展。

`idle` 不能自动区分已完成、等待输入、无能力、已中断或检测器失效。

可观测对象只包括可见消息、Tool Activity、Artifact、State Transition 和 Decision Record。不宣称读取 Agent 的隐藏思维过程。

---

# 17.28 组织成本应进入是否拆成多 Agent 的决定

多 Agent 方案的总成本不只是 Token 或运行时间，还包括：

- Work Decomposition Cost；
- Context Construction 与复制；
- Assignment 与调度；
- 等待和容量错配；
- Handoff Loss 和接收检查；
- 重复探索；
- Review 和 Conflict Resolution；
- Merge / Integration；
- 共享状态维护；
- Governance Artifact；
- Human Attention；
- Failure Recovery。

只有当下列一项或多项收益超过这些成本时，多 Agent 才是值得的候选：

- 真实的并行性；
- 不同 Domain Capability；
- 有意义的 Review Independence；
- Context Isolation；
- 更小的 Failure Blast Radius；
- 可恢复的专职输出；
- 更清楚的 Responsibility。

Agent 数量、总输出量或并发任务数不能单独作为组织效能指标。

当工作紧耦合、输出很小、责任难以分开或整合成本很高时，一个具有清楚 Contract 的单 Agent 可能是更合适的组织形态。

---

# 17.29 案例只保留组织关系投影

现有材料没有单 Agent / 多 Agent 匹配对照，也没有控制任务难度、Model、Context 与 Human Attention；完整 Case Spine 见[第23章](第23章_AI_Game_Dev_OS纵向案例_首轮修订稿.md)。

| Episode | 本章使用的关系 | 不能说明 |
|---|---|---|
| v4.94 Task Projection | Handoff、Cancel、Withdraw 与 Rework 可以通过绑定 Source 的非权威投影外显 | 完整 Multi-Agent Organization、全局 Authority / Detector Health / Revocation 已实现，或 Human Judgment Load 已降低 |
| D-076 Dual Review | 多个 Review Finding / Recommendation 可以进入后续 Human Decision，而不自动产生 Adoption | 两个 Reviewer 已充分独立、PASS 必然正确或 Dual Review 普遍值得 |
| SP122 | Evidence Disposition、Adoption 与 Production Release 可以属于不同 Decision Target | 一项组织设计效果测试 |

来源与限制见[v4.94 任务投影记录](../Evidence/receipts/ER-20260824-002__CLM-C12-001.md)、[D-076 双重审阅记录](../Evidence/receipts/ER-20260824-003__CLM-C16-001.md)和[SP122 分离处置记录](../Evidence/receipts/ER-20260818-003__CLM-C09-001.md)。这些共享来源只支持 Role / Authority 与 Decision Target 的分离，没有验证本章九个对象的完备性或任何 Topology 的净收益。

---

# 17.30 最小实现从一个真实协作边界开始

不需要一次建立十个 Role。

选择一个：

- 经常出现 Handoff Loss；
- 需要异质 Domain Review；
- 存在不能由 Producer 自审的风险；
- 可以安全并行；
- 当前责任或 Authority 经常混淆的工作。

建立最小关系：

1. 一个有边界的 Work Reference；
2. 一个 Role Contract；
3. 一个 Subject Configuration；
4. 一个明确接受的 Assignment；
5. 一个 Authority Reference；
6. 一个 Handoff Package 与 Receipt；
7. 一个 Integration Disposition；
8. 一条 Cancel / Revoke / Escalate 路径。

如果风险需要，再增加一个与 Producer 有实质分离的 Reviewer。

候选试点可以优先演练：

- 一个缺少关键 Unknown 的 Handoff；
- 一个 Reviewer 与 Worker 结论冲突；
- 一个 Assignment 在 In-flight 状态被 Cancel 或 Grant 被 Revoked；
- 一个 Candidate 无法集成；
- 一个 Blocked 结果无法由原 Role 解决。

测量的不只是完成时间，还包括：

- 重复 Work；
- Handoff Clarification；
- Conflict Resolution Time；
- Escaped Defect / Risk；
- Review Finding 的有效性；
- Integration Rework；
- Human Decision Load；
- 被及时终止的无效工作。

如果一个单 Agent 已能以更低成本稳定完成，多 Agent 不是必须的下一步。

---

# 17.31 与相邻章节的所有权边界

| 对象 | 所属章节 | 第17章如何使用 |
|---|---|---|
| Intent Artifact、Conflict、Acceptance Target | 第4章 | 作为 Work 与 Role Contract 的方向输入 |
| Context Contract、Pack、Manifest、Access | 第5章 | 为不同 Role 建立有来源投影 |
| State Claim、Authority Grant、Applicability | 第6章 | 约束 Shared State 与冲突判断 |
| Work、Execution Contract、Attempt、Checkpoint、Bounded Execution | 第7章 | 将 Role 与 Assignment 绑定到既有执行边界，不重新定义 Work |
| Attempt Outcome、Target Result、Evaluation Result、Failure、`non-result`、Recovery | 第8章 | 组织 Handoff、Conflict 与 Integration 时保留结果分类 |
| Evidence Coverage、Acceptance、Adoption、Release Authorization | 第9章 | 避免 Review PASS 扩张决定或发布授权范围 |
| Review、Review Target、Finding、Review Budget、Review Independence、Review Disposition | 第10章 | 说明组织拓扑如何承载审阅，不重新定义 Review 对象 |
| HCP Projection、Brief、Compression Validation | 第12章 | 向 Human 投影组织状态，不产生新 Authority |
| Authority、Delegation、Revocation、Intervention | 第13章 | 约束 Assignment、Decision 与下游委托 |
| Observation、Detector、Exception | 第14章 | 提供组织运行的可见信号 |
| Organization Change Candidate | 第16章 | 将 Role、Topology 或 Handoff 改动作受治理候选 |
| Role、Assignment、Handoff、Conflict、Integration | 第17章 | 本章核心对象 |
| Release Execution、Release Outcome、Durable Decision Trace、Attribution、Audit 与 Accountability Evidence | 第18章 | 记录已授权发布的执行与结果，并保留组织行为的长期责任链 |

第17章分配当前运行责任，但不提前展开长期审计、署名、责任证据与 Decision Graph。

---

# 17.32 本章原则

1. **Agent 数量不是组织成熟度。** 组织需要 Work、Role、Authority、Responsibility、Handoff、Conflict 和 Integration。
2. **Role 不是 Persona。** Role Contract 声明决定视角、义务、输入、输出和禁区。
3. **Skill 不是 Role。** Method 可以被多个 Role 使用。
4. **Assignment 需要接受。** 不完整输入不应被隐藏成执行失败。
5. **Controller 是协调 Role，不是超级 Authority。** 它的 Summary 也需要来源和完整性边界。
6. **Worker 输出是 Candidate。** 完成 Work 不自动完成 Adoption 或 Release。
7. **Review Independence 是多维的。** 换名或多采样不等于完整独立。
8. **Handoff 需要 Receipt。** Submitted 不等于 Accepted，接管不等于 Truth 或 Authority 转移。
9. **Context 按 Role 投影。** Shared State 少而有来源，不建立无边界全员 Prompt。
10. **Conflict 先分型。** 事实、证据解释、设计、Authority 和价值冲突使用不同处置。
11. **并行需要隔离与集成。** Merge 可执行不表示语义可接受。
12. **委托不自动转授 Authority。** 下游 Agent 只能继承明示可转授的范围。
13. **Human 不是每步的默认 Gate。** 应将人类放在具名价值、风险和责任位置。
14. **组织成本进入方案比较。** 多 Agent 只在净收益成立时值得。

---

# 17.33 常见反模式

- 通过增加 Agent 数量宣称组织成熟；
- 把 Agent Name 或 Persona 当作 Role Contract；
- 同一 Agent 换一个头衔后“独立审阅”自己；
- Controller 自动拥有 Intent、Truth、Integration 和 Release Authority；
- Planner 产生 Plan 后无需 Assignment 就开始执行；
- Worker 把交付、测试或 Merge 写成 Adoption；
- Reviewer `PASS` 覆盖未审阅的 Scope；
- 只给 Reviewer 提供 Producer Summary，却声称 Source Independent；
- 将全部 Context 复制给所有 Agent；
- 用一个无来源 Global Summary 取代原始状态；
- Handoff 发出即视为对方已接管；
- 交接时删除 `non-result`、Counterevidence 和 Unknown；
- 所有冲突都按“证据更强”排名；
- 为创意冲突伪造客观分数；
- 没有 Decision Owner 时不断增加 Reviewer；
- 自动 Successor 不断创建 Governance Work；
- 并行 Agent 共享同一写面而无 Ownership；
- Merge 成功被解释为语义集成成功；
- 上游 Agent 把全部 Authority 默认传给它创建的 Agent；
- 撤销 Assignment 后不处置 Credential、In-flight Work 和外部副作用；
- 全部输出都升级给 Human；
- 把 Human 写成拥有任意 Policy Override 的最终按钮；
- 用总 Token、总输出或并发数证明组织效能；
- 用 v4.94 Dual Review 证明多 Agent 必然更好。

---

# 17.34 本章检查清单

## Work 与 Role

- Work Reference 是否指向具有 Goal、Scope、Input、Output、Dependency 和 Close Condition 的 Work？
- Role Contract 是否声明 Responsibility、Decision Lens、Allowed / Prohibited Decision？
- Persona、Skill、Role、Subject Configuration 是否被分开？
- Assignment 是否被显式接受？
- Subject 是否可以返回 Out-of-scope、Missing Input 或 `non-result`？

## Authority 与 Responsibility

- Responsibility、Authority、Permission 和 Accountability 是否分开？
- Controller 实际拥有哪些 Authority？
- Planner、Worker、Reviewer 的 Decision Target 是什么？
- 下游委托可以转授哪些 Grant？
- Revocation 如何处置 In-flight Work、Credential、Memory 和 Side Effect？

## Review

- Reviewer 检查的具名 Claim 和 Scope 是什么？
- Reviewer 输出的是 Finding / Recommendation，还是在明确 Grant 下形成的 Review Disposition？
- Producer、Contract、Context、Source、Method、Decision 与 Authority 独立性分别如何？
- Reviewer 是否可见 Primary Source 与 Counterevidence？
- PASS 是否被错误扩张到 Adoption 或 Release？

## Handoff 与 Context

- Handoff 是否保留 Goal、State、Actual Change、Decision、Evidence、Unknown、Risk 和 Next Action？
- 是否有 Handoff Receipt？
- 哪些职责从什么时点转移？
- 交接是否被误写成 Truth、Adoption 或 Authority 转移？
- Shared State 是否有 Identity、Version、Freshness 和 Source Link？
- Role-specific Context 是否允许下钻原始记录？

## Conflict 与 Integration

- Conflict 属于事实、Evidence、Design、Authority、Policy、Resource、Value 还是 Responsibility？
- Decision Target 和 Decision Owner 是否存在？
- Minority Position、Unknown 和 Reopen Condition 是否保留？
- 并行 Work 是否有隔离写面、Baseline 和 Integration Order？
- Integration Disposition 是否与 Merge、Adoption 和 Release 分开？

## Flow 与 Cost

- 是否存在循环 Dependency、无限 Review Loop 或 Automatic Successor？
- WIP、Capacity、Timeout、Stop 和 Escalation 是否可观察？
- Summary 是否保留 Counterevidence、Unknown 和 Source Link？
- Human 是否只收到真正需要其 Authority 的决定？
- 并行、Domain Capability、Independence 或 Isolation 收益是否超过协调成本？
- 是否存在更简单的单 Agent 方案？

---

# 17.35 本章结论

Multi-Agent Organization Design 不把并发 Agent 列表包装成组织。

它建立的是：

~~~text
bounded Work Reference
+ Role Contract
+ Subject Configuration
+ accepted Assignment
+ Authority Reference
→ candidate output and visible execution state
→ Handoff Receipt / Review / Conflict
→ authorized Integration Disposition
→ explicit next responsibility
~~~

其中：

- Controller 协调工作，不自动成为超级 Authority；
- Worker 交付 Candidate 和 Evidence，不自动完成 Adoption；
- Reviewer 在具名范围内挑战结果，不把 PASS 扩张到未授权决定；
- Handoff 转移工作与记录，不自动转移 Truth、Authority 或全部 Accountability；
- Conflict 按对象与 Decision Target 处理，不靠一条虚构强弱表消除。

> **Agent count is not evidence of organization. In this book, a governable multi-agent arrangement makes work, authority, responsibility, interfaces, conflict and integration explicit.**

中文语义是：

> **Agent 数量本身不是组织已经形成的证据；本书把工作、Authority、Responsibility、协作接口、冲突和集成处置的显式关系，作为可治理多 Agent 安排的工作定义。**

当这条链不存在时，多 Agent 只是多个并行运行实例。

下一章将讨论：如何把 Assignment、Handoff、Review、Authority、Decision 和 Integration 保留为可追溯的责任链，使系统不只知道“改了什么”，还能回答“为什么、根据什么、由谁决定、哪些假设仍未验证”。
