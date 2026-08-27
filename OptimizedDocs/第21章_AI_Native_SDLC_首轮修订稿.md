# 第21章 AI-Native Software Development Lifecycle
## 从固定阶段流水线到可裁剪的状态迁移网络

> 工作稿状态：首轮逻辑修订稿，不替代 [全书大纲](../OringinalDocs/beyond_code_ai_native_software_engineering_outline_zh.md)。
> 回接说明：[RR-034](../RevisedResult/RR-034_第21章AI_Native_SDLC首轮调整计划.md)。
> 适用边界：本章提出 Lifecycle Profile 与 Lifecycle Transition 的候选整合模型；它不替代所有传统 SDLC，不声称阶段数量或顺序普遍最优，也不把 Execution Epoch、Sprint、多 Agent 或完整 Gate Stack 设为每项工作的必经对象。AI Game Dev OS v4.94 只提供状态与处置语义案例，不证明该 Lifecycle 提高效率、质量或安全性。

传统 Software Development Lifecycle 通常被写成：

~~~text
Requirement
→ Design
→ Implementation
→ Test
→ Deployment
→ Maintenance
~~~

这个抽象仍然有用。

它描述软件从需求到运行和维护的主要活动。

Agent 没有取消 Requirement、Design、Test 或 Operations。

它改变的是：越来越多的解释、规划、执行、验证和提案可以被委托给能够调用 Tool、
修改状态、并行工作和长期运行的执行主体。

这使 Lifecycle 还需要回答：

- 当前 Work 的 Intent、Scope、Acceptance Target 与 Non-goal 是什么；
- Agent 依据哪个 State、Decision、Assumption 与 Context 工作；
- 谁授权哪个 Tool、Permission、Credential 和 External Effect；
- 一个 Attempt 何时开始、暂停、失效、重开或关闭；
- Evidence 可以支持哪个 Decision Target；
- Test PASS、Acceptance、Integration、Release 与 Operations 怎样分开；
- 失败、未知外部结果和 `non-result` 如何留在路径中；
- 什么时候进入 Human Review、Takeover、Recovery 或 Re-evaluation；
- 哪些经验只成为 Candidate，哪些可以进入 Memory、Skill、Policy 或 Workflow。

这是 Lifecycle 模型可能需要承载的问题空间，不是每项 Work 都要实例化的统一清单。
具名 Lifecycle Profile 应只选择当前影响面、持续时间、授权分布、下游用途和恢复要求实际触发的部分。

如果把这些关系继续排成一条更长的流水线，会得到一个看起来完整、实际上难以裁剪的
流程图。

本章使用以下中心句：

> **A lifecycle is not the list of stages every task must visit; it is the set of authorized transitions through which work may open, branch, pause, recover, close, and re-enter operation.**

Lifecycle 不是每项任务必须访问的阶段清单，而是 Work 可以在其中打开、分支、暂停、
恢复、关闭并重新进入运行的有授权状态转换集合。

---

# 21.1 先区分必要、有用与可选

## 必要的最低控制功能

只要 Agent 被委托修改持久工程状态或产生外部影响，Lifecycle 在语义上至少需要保留：

- 当前 Work 和 Attempt 的 Identity；
- Scope、允许动作与允许影响面；
- 对执行与关闭具有权限的具名 Human / System Authority；
- Result、Failure、Unknown 或 `non-result` 的可见性；
- Stop、Recovery 或能够安全丢弃本次 Attempt 的边界。

“必要”指最低控制功能，不要求每项 Work 分别持久化全书对象。Issue、VCS、Sandbox、CI 或 Human Workflow 可以共同承担这些功能。

## 条件性／有用

当持续时间、并发、影响、不确定性、Policy / 合同 / Rights、下游处置、恢复要求等具名风险或 Decision Use 触发时，下列能力通常有用：

- 版本化 Lifecycle Profile、Execution Contract、Baseline、Context、Assumption 与 Conflict Record；
- 正式 Evidence Plan、Coverage、Transition / Decision Target；
- Acceptance、Integration、Release Authorization 与 Operational Disposition 的分立记录；
- Exception Authority、Independent Review、Checkpoint、Handoff、Pause、Rebase 与 Re-evaluation Case；
- 第22章定义的 Capability Fit Review；
- 长期 Memory / Evolution Candidate 的独立 Promotion / Adoption；
- 在需要并行、专业隔离或 Review Independence 时引入的独立 Multi-Agent Role。

## 可选

以下实现不应成为 AI-native SDLC 的定义条件：

- Human Control Plane（包括完整 Dashboard）；
- Execution Epoch；
- Self-Evolution（包括 Pipeline）；
- 统一 Dashboard / Registry 与完整 Decision Graph；
- 每项工作都创建完整 Workflow Record；
- 完整 Gate Stack 或每个阶段由不同 Agent 执行；
- 固定 Controller / Worker 组织；
- 固定 G0–G4 风险等级；
- Sprint 作为唯一时间粒度；
- 全量 Trace、全量在线 Evaluation 或永久 Context Retention；
- 任务完成后自动写入 Memory 或修改 Workflow。

低风险、局部、易恢复的修改，可以把多个关系压缩进一份短 Work Brief 和一次有边界
验证，不需要把概念模型完整持久化。

后续章节将展开候选关系全集。具名 Lifecycle Profile 只选择当前用途触发的部分；未触发对象可以省略，不应为完成模型而实例化。

---

# 21.2 传统 SDLC 仍然存在

传统 SDLC 的阶段通常围绕 Product / Software Artifact 展开：

- 需要什么；
- 怎样设计；
- 如何实现；
- 怎样验证；
- 如何发布；
- 怎样维护。

AI-native 控制循环可以出现在每个阶段：

| 传统活动 | Agent 可能承担 | 新增控制问题 |
|---|---|---|
| Requirement | 整理需求、发现冲突、生成候选 | 谁拥有 Intent 与优先级 Authority |
| Design | 分析方案、原型、模拟、评审 | Context、Assumption、Trade-off 与 Acceptance Target |
| Implementation | 修改代码、数据、配置和资产 | Tool、Permission、Scope、Baseline 与 Recovery |
| Test | 生成、运行和解释测试 | Claim、Coverage、Verifier Integrity 与 `non-result` |
| Deployment | 准备、执行和观察发布 | Environment、Release Authority、Rollback 与 External Effect |
| Maintenance | 监控、修复、迁移和演化 | Drift、Re-evaluation、Memory 与 Evolution Boundary |

因此 AI-native SDLC 不是把传统六阶段替换为十几个 Agent 阶段。

它是在原有活动中加入受托执行的 Identity、Authority、Evidence、Decision 与 Recovery
关系。

---

# 21.3 Lifecycle 是关系模型，不是新平台

本章使用 **Lifecycle（生命周期：具名 Work 从 Trigger 和 Intent 形成，到执行、评价、
处置、集成、运行以及可能学习的允许状态转换与关闭关系）** 作为整合视图。

Lifecycle 不拥有：

- Intent 的内容；
- 项目 Truth；
- Context Source；
- Tool Permission；
- Evidence 的真实性；
- Human Authority；
- Memory 内容；
- AgentOps Telemetry。

这些对象继续由前面章节拥有。

第21章只组织：

1. 哪些对象在一次状态转换中被引用；
2. 谁可以作出转换处置；
3. 缺失、冲突、失败或 Drift 会把路径带到哪里；
4. 哪些阶段可以压缩、循环、跳过或独立关闭；
5. 怎样避免一个阶段的完成被误写成整个 Work 的完成。

如果现有 Issue、Workflow Engine、CI/CD、Release System 和 Incident System 已经能表达
这些关系，就没有必要再建一个 Lifecycle 平台。

---

# 21.4 主干是状态迁移网络

候选主干可以表示为：

~~~text
Need / Trigger
  ↕
Intent + Acceptance Target
  ↕
Grounding
  State / Decision / Assumption / Conflict
  Context Contract + Manifest
  Authority + Risk Boundary
  ↓
Plan / Execution Contract
  ↓
Bounded Execution Attempt
  ↕ observe / retrieve / pause / rebase / recover
Attempt Outcome + Target Result + Evaluation Result
  ↓
Observation + Evidence + Coverage
  ↓
Decision Record + Authorized Disposition
  ├── retrieve / replan / rework / narrow
  ├── reject / cancel / hold
  ├── accept-for-scope / authorize-integration / authorize-release
  └── authorize-rollback / suspend
  ↓ authorized action, when applicable
Integration Execution / Release Execution
  ↓
Integration Outcome / Release Outcome
  ↓ when applicable
Operations
  ↕ Drift / Re-evaluation
Learning Candidate
  ↓ separate promotion or adoption decision
Future Baseline
~~~

这个图不是严格执行顺序。

- Grounding 可以暴露 Intent Conflict；
- Execution 可以触发新 Retrieval；
- Observation 可以使 Baseline 失效；
- Evidence Gap 可以要求缩小 Claim 或 Scope；
- Human Decision 可以拒绝已通过 Test 的 Candidate；
- Integration Conflict 可以创建新 Attempt；
- Release 后的 Drift 可以重新打开 Design、Evaluation 或 Authority Decision；
- Learning Candidate 可以被拒绝、过期或限制在局部 Scope。

路径允许回退，不表示历史被覆盖。

每个 Attempt、Decision 和 Baseline 仍保留自己的 Identity。

---

# 21.5 Work、Attempt、Outcome、Change 与 Release 关系分开

Lifecycle 最常见的语义压缩，是把“一个任务”当成所有对象。

本节只建立 Lifecycle 的整合 Bridge，不取得这些基础对象的定义所有权。第7章拥有 Work、Execution Contract、Attempt、Checkpoint 与 Bounded Execution；第8章拥有 Attempt Outcome、Target Result、Evaluation Result、Failure、`non-result` 与 Recovery。本章按这些已冻结关系引用它们。

## Work Reference

Lifecycle 引用由第7章定义的 **Work**，以定位其具名目标、Scope、Owner、约束和关闭语义。一个 Work 可以跨多个 Attempt、Agent、Commit、Review 和 Release；一次 Attempt 结束不自动关闭 Work。

## Attempt Reference

Lifecycle 引用由第7章定义的 **Attempt**，以区分同一 Work 下具名 Execution Contract、Baseline、输入快照、Context、配置和时间边界不同的执行实例。Attempt 可能完成、部分执行、取消、超时、崩溃或没有到达 Target。

## Attempt Outcome、Target Result 与 Evaluation Result References

Lifecycle 引用第8章拥有的三类结果关系：**Attempt Outcome** 记录该 Attempt 实际发生了什么；**Target Result** 只在 Target 获得足够执行时记录其输出或行为；若前置 Verifier 已经阻断 Target，应显式记录 `non-result`，而不是填写 Target FAIL；**Evaluation Result** 记录 Test、Verifier、Review 或 Human Evaluation 对具名 Target 与运行形成的结果。

三者都不自动形成 Work Acceptance、Adoption 或 Release Authorization。

## Change Reference

Change 是对 Code、Data、Configuration、Artifact 或 External State 的具体变化。

一个 Attempt 可以产生多个 Change；一个 Change 也可能尚未被接受。

## Release Authorization、Release Execution 与 Release Outcome References

Lifecycle 引用第9章拥有的 **Release Authorization**，以及第18章拥有的 **Release Execution / Release Outcome**：前者是允许具名 Artifact 或 Change 进入指定发布面的规范性 Decision；Execution 是实际分发、部署或推进的一次或多次 Attempt；Outcome 是 Environment、User 或 Downstream Consumer 实际观察到的后果。

这些关系可以表示为：

~~~text
Work
├── Attempt A → Attempt Outcome: pre-target blocked → Target Result: non-result
├── Attempt B → Candidate Change → rejected-for-scope
└── Attempt C → Accepted Change
                    ↓
                 Integration
                    ↓
              Release Candidate
                    ↓
           Release Authorization
                    ↓
            Release Execution
                    ↓
       Succeeded / Failed / Rolled Back
                    ↓
             Release Outcome
~~~

如果只保留 Work 的最终 `done` 或一个裸 `released`，就会失去失败路径、Evidence 适用范围、授权未执行、执行失败和恢复历史。

---

# 21.6 Lifecycle Profile 选择路径，不定义成熟度

**Lifecycle Profile（生命周期配置：针对具名 Work、风险面和恢复条件，选择必要
Transition、Gate、Observation、Review 与 Recovery 的有范围配置）** 可以说明：

- Work Type 与 Intended Use；
- Data、Tool、Permission 与 External Effect；
- Reversibility 与 Recovery；
- State Uncertainty 与 Conflict；
- Duration、Concurrency 与 Handoff；
- Required Evaluation 与已知 Coverage；
- Human Cognitive Authority 与具名 Human Authority Grant；
- Protected Control Floor；
- Required / Optional Transition；
- Escalation、Fallback、Expiry 与 Owner。

示例：

~~~yaml
lifecycle_profile_id: LP-021-bounded-change
applies_to:
  work_type: repository_change
  environment: development
  external_effect: repository_only

required:
  - intent_and_acceptance_target
  - baseline_and_context_reference
  - bounded_execution_contract
  - change_observation
  - claim_matched_evaluation
  - integration_disposition

conditional:
  checkpoint:
    when:
      - work_crosses_session
      - baseline_drift_detected
      - write_scope_expands
  independent_review:
    when:
      - protected_surface_changed
      - recovery_uncertain

floor:
  - no_secret_in_prompt
  - no_write_outside_grant
  - target_non_result_preserved

closure:
  allowed:
    - accepted_for_integration
    - rejected
    - cancelled
    - partial
    - target_non_result
~~~

这不是通用 Schema，也不是 G0–G4 等级。

一个组织可以把 Profile 表达为 Policy、Workflow Template、Task Form、代码配置或操作惯例。

---

# 21.7 Profile 依据风险面组合

流程裁剪不应只问“任务是低、中还是高风险”。

需要识别实际风险面：

- External Effect 与 Blast Radius；
- Data、Secret、Privacy、IP 与 Provider Boundary；
- Tool、Credential、Permission 与 Authority；
- Reversibility、Rollback 与 Forward Recovery；
- State Uncertainty、Conflict 与 Dirty Worktree；
- Duration、Concurrency、Agent 数量与 Handoff；
- Evaluation Coverage 与未知失败面；
- Human Decision Capacity；
- Production、Customer、Player 或法定影响；
- Governance 与 Total Production Cost。

相同的“中风险”标签可能掩盖完全不同的控制需要。

例如：

- 数据受限但动作只读：重点是 Context、Provider、Retention 与 Rights；
- 数据公开但可写 Production：重点是 Authority、Action Sink、Transaction 与 Recovery；
- 低影响但跨数周：重点是 Baseline、Handoff、Drift 与 Rebase；
- 局部且易恢复：可以压缩 Plan、Review 和持久化对象；
- Creative Work：需要保留 Human Direction 与审美裁决，而不是增加自动 Score。

回答“是”的数量不是风险分数。

Profile 是具体控制选择，不是项目成熟度排名。

---

# 21.8 Lifecycle Transition 绑定转换条件与 Authority

**Lifecycle Transition（生命周期转换：把具名 Work、Attempt、Change 或 Release 从一个
有边界状态迁移到另一个状态的授权关系）** 至少需要回答：

- Transition Target 是什么；
- 当前 Scope、Baseline 与输入是什么；
- 需要哪些 Evidence 或已知 Coverage；
- 谁拥有 Decision Authority；
- 允许哪些 Disposition；
- 失败、未知、超时或撤权时怎样处理；
- 是否产生新的 Attempt、Baseline 或 Candidate。

示例：

~~~yaml
transition_id: LT-021-018
work_ref: W-021-UI-fix
from: evidence_ready
decision_target: accept_change_for_integration

scope:
  paths:
    - ui/settings/
  non_goals:
    - save_migration

required_inputs:
  - intent_ref
  - baseline_ref
  - diff_ref
  - focused_test_result
  - coverage_statement

authority:
  decider: ui_maintainer
  automated_gate: focused_test_gate_for_named_scope

dispositions:
  - accept_for_integration
  - request_change
  - narrow_scope
  - reject
  - hold

on_unknown:
  action: hold_and_request_evidence
~~~

不需要为每次 Transition 创建独立文件。

这组字段用于检查一个 Gate、Review 或自动 Workflow 是否真的拥有清楚语义。

---

# 21.9 Phase、State Claim、Lifecycle Status 与 Transition 不是同一个概念

**Phase（阶段：为了组织活动而形成的工作分组）** 可以叫 Design、Implementation、
Evaluation 或 Operations。

**State Claim（状态主张）** 描述某个具名 Work、Attempt、Change、Artifact 或 Environment 在特定时间和 Scope 下的可观察情况。它保持描述性，不包含“允许采用”“应当发布”等规范性处置。

**Lifecycle Status（生命周期状态）** 是对已记录 Transition 与 Disposition 的 Target-specific 投影，例如 candidate、blocked、accepted-for-scope 或 released-to-environment。它不能替代关于 Implementation、Runtime 或 Environment 的 State Claim。

**Transition** 是具名 Lifecycle 对象从一个 Status 到另一个 Status 的有权、可追踪变化。它应引用相应 Decision Record、执行 Attempt 与前后 State Claim；Transition 的存在不会使底层描述性 Claim 自动为真。

因此：

- “进入 Test Phase”不表示 Test 已运行；
- “Evaluation Complete”不表示 Outcome 已接受；
- “Review Done”不表示 Change 可以 Merge；
- “Deployment Phase”不表示 Production 已改变；
- “Maintenance”不表示 Drift 已被控制。

Phase 用来组织工作，State Claim 描述发生了什么，Lifecycle Status 投影当前路径位置，Transition 记录哪一个有权决定和执行使路径发生变化。

---

# 21.10 Need 与 Trigger 只打开 Work Candidate

Need 或 Trigger 可能来自：

- Human Request；
- Product Opportunity；
- Bug / Incident；
- Test Failure；
- Security / Privacy Signal；
- Drift Finding；
- Dependency、Provider 或 Contract Change；
- Memory Retrieval；
- Evolution Candidate；
- External Deadline 或 Policy Requirement。

Trigger 被观察到，不表示：

- 问题已经理解；
- 当前描述是权威 Intent；
- Work 应该自动执行；
- 提议者具有优先级 Authority；
- Root Cause 已知；
- 建议方案已被接受。

Lifecycle 的第一项转换通常是：

~~~text
Need / Trigger
→ Work Candidate
→ Intent Formation or Triage
~~~

低价值、重复、无 Authority 或超出 Scope 的 Candidate 可以在这里关闭，而不必进入
完整 Planning 和 Execution。

---

# 21.11 Intent Formation 定义方向，不授予全部执行权

Intent Formation 使用：

- Need 与 Trigger；
- Stakeholder Input；
- Product / Technical / Security / Cost / Compliance Constraint；
- Existing Decision 与 Non-goal；
- Affected Subject 与 Environment。

候选输出包括：

- Intent Artifact；
- Scope 与 Non-goal；
- Acceptance Target；
- Priority / Trade-off Decision；
- Open Question；
- Intent Authority；
- 需要的 Grounding 和下一 Decision Target。

Intent 可以打开进一步分析，但不自动授予：

- Repository Write；
- Production Access；
- Data Transmission；
- Release；
- Memory Promotion；
- Policy Modification。

这些需要各自的 Authority 和 Transition。

Intent 发生冲突时，不应让执行 Agent根据语气、顺序或 Prompt 位置自行决定优先级。

---

# 21.12 Grounding 建立当前可依赖边界，不“解决 Truth”

**Grounding（执行落地准备：为当前 Decision Target 组合有来源的 State、Decision、
Assumption、Conflict、Context、Authority 与已知缺口，使下一动作具有可检查依据）**
替代原大纲中过强的 `Truth Resolution` 表达。

Grounding 可能引用：

- 当前 State Claim 与 Snapshot；
- Active Decision / Policy；
- Intent 与 Acceptance Target；
- Assumption 与 Unknown；
- Conflict 与 Dirty Work；
- Source Version、Commit、Environment 与 Runtime；
- Context Contract / Manifest；
- Data / Rights / Security Boundary；
- Capability、Permission 与 Authority；
- Required Evidence 与 Recovery 条件。

输出不是一个无范围的 Truth 对象。

它更接近：

~~~text
Execution Baseline reference
+ Context Contract / Manifest
+ explicit assumptions and conflicts
+ authority and risk boundary
+ known coverage gaps
~~~

Grounding 不足时，允许：

- Progressive Retrieval；
- Human Clarification；
- Scope Narrowing；
- Assumption-based Exploration；
- Hold；
- Cancel。

系统不需要为了让流程图继续而生成一个伪确定答案。

Grounding 是 Lifecycle 中的活动投影，不是新的独立 Record 或 Truth Store。

## Lifecycle 面的输入、输出与非主张

| Lifecycle 面 | 主要输入 | 候选输出 | 不自动产生 |
|---|---|---|---|
| Need / Trigger | Human Need、Incident、Observation、Opportunity | Work Candidate | 已接受 Intent |
| Intent Formation | Need、Stakeholder、Constraint | Intent Artifact、Acceptance Target、Non-goal | 实施授权 |
| Grounding | State Source、Decision、Assumption、Conflict | Baseline Reference、Context Manifest、Known Gap | 完整 Truth |
| Planning | Intent、Baseline、Context、Authority | Plan、Execution Contract、Evidence Plan、Recovery Boundary | Plan Acceptance |
| Execution | Contract、Tool、Permission、Attempt State | Action、Artifact、Observed Effect、Checkpoint | 正确结果 |
| Evaluation | Outcome、Claim、Test、Observation | Evidence、Coverage、Counterevidence、`non-result` | Acceptance |
| Disposition | Evidence、Scope、Authority Grant、Decision Target | Accept、Reject、Narrow、Rework、Hold、Cancel、Authorize | Integration / Release Execution |
| Integration | Authorized Change、Target Baseline、Conflict Check | Integration Execution Record、Integrated State Observation | Release Authorization |
| Release Authorization | Release Candidate、Environment、Evidence、Authority Grant | authorized / blocked / deferred / conditional | Release Execution |
| Release Execution | Authorized Release Target、Execution Contract、Attempt | distributed / deployed / partially-executed / failed / rolled-back | Release Outcome 健康或更高资格 |
| Release Outcome | Environment / User / Downstream Observation | healthy / degraded / failed / unknown-for-scope | 长期适用性或 Production Qualification |
| Operations | Operational Baseline、Window、Telemetry | Drift Finding、Incident、Re-evaluation Case | Root Cause |
| Learning | Accepted Experience、Failure、Review | Memory / Evolution Candidate | Promotion / Adoption |

`可验证 Context Pack` 在本章收窄为可检查的 Context Contract / Manifest 与已知缺口；
它记录选择和来源，不证明内容为真或 Model 实际采用。

`Verified New State` 也不作为统一尾声。更准确的是保存 Post-action State Observation、
Verification Scope 与 Authorized Disposition。

---

# 21.13 Planning 形成候选路径，Execution Contract 形成受权边界

Plan 可以描述：

- 目标和 Step；
- Dependency；
- Work Decomposition；
- Agent / Human Assignment；
- Tool 和 Environment；
- Checkpoint；
- Evidence Plan；
- Recovery 与 Stop Condition；
- 预计成本和时间。

Plan 是 Proposal。

它只有在与 Authority、Permission、Baseline 和 Evidence Requirement 对齐后，才可能
进入执行。

按照已冻结的所有权，第7章正式定义 **Execution Contract**。本章只引用它进入 Lifecycle 所需的关系：它把具名 Intent、Scope、Baseline、Context、Tool、Permission、Authority、Evidence、Stop 与 Recovery 绑定到一次或一组 Attempt，不要求 Plan 的每个细节都被提前预测。

它规定不能静默改变的边界，以及发生变化时怎样重新决策。

下列是 Lifecycle 所需的引用面，不是第21章另建的 Contract Schema：

~~~text
Execution Contract
├── Work / Intent / Acceptance references
├── Baseline and Context references
├── Scope and prohibited effects
├── Subject / Agent / Tool assignments
├── Permission, Credential and Authority
├── Governance floor and conditional controls
├── Evidence and checkpoint requirements
├── Stop, recovery and handoff
└── expiry and owner
~~~

局部可逆 Work 可以把这些内容压缩进一份 Brief；高影响 Work 则可能需要独立版本。

---

# 21.14 Plan Review 不应成为所有任务的独立等待点

Plan Review 有价值的场景包括：

- Scope 容易扩张；
- 多方 Intent 或 Authority 冲突；
- Tool / Data / Production Effect 较高；
- Recovery 不清楚；
- 长任务或多 Agent 依赖复杂；
- Evidence Plan 可能无法覆盖 Acceptance Target；
- Human 需要在成本投入前作 Trade-off。

但一个清楚、局部、易验证的修正，可能由已有 Policy 直接允许：

~~~text
short work brief
→ bounded edit
→ automated validation
→ diff / outcome disposition
~~~

判断是否需要独立 Plan Review，应看它会改变什么 Decision，而不是流程图上是否存在
一个 `Plan Gate` 方框。

Review 也不产生执行 Permission。

Reviewer 可以认为 Plan 合理，但 Tool、Credential 或目标 Environment 仍需独立授权。

---

# 21.15 Execution Attempt 必须有边界

本章不新增 `Bounded Execution Attempt` 对象。按照已冻结的章节所有权，第7章正式定义 Attempt；本节只列 Lifecycle Transition 需要从 Attempt Record 读取的关系，不构成第21章的 Attempt Schema：

- Attempt ID；
- Work 与 Contract Reference；
- Start Baseline；
- Subject、Agent、Tool 与 Environment；
- Current Scope 与 Authority；
- Started / Paused / Closed Time；
- Observable Action、Change 与 External Effect；
- Checkpoint / Handoff；
- Attempt Outcome / Target Result / Evaluation Result Reference；
- Output / State Observation Reference。

Attempt 不是内部 Chain-of-thought 容器。

Attempt 只关联执行时可观察的动作、边界与上游引用；完整外部决策环境、记录完整性和重建覆盖由第18章 Trace 负责。

同一 Work 的新 Attempt 需要新 Identity，尤其当以下对象变化时：

- Baseline；
- Intent / Scope；
- Agent / Tool；
- Permission / Authority；
- Model / Policy；
- Evaluation Requirement；
- Recovery Path。

重新尝试不能用同一状态覆盖失败或无结果的 Attempt。

---

# 21.16 Execution 中允许 Retrieve、Pause、Rebase 与 Recover

执行不是从 Plan 到 Output 的封闭直线。

允许的中途转换包括：

## Retrieve

发现 Context 缺口，按 Contract 获取额外信息。Retrieval 不自动扩大 Instruction Authority。

## Pause

临时停止新 Side Effect，保存当前 Attempt、在途动作、未知和恢复条件。

## Rebase

外部 State、Intent、Decision 或 Baseline 改变后，由具名 Authority 决定是否形成新
Baseline、调整 Contract 或创建新 Attempt。

Rebase 不重写过去的执行依据。

## Restrict

收窄 Tool、Permission、Data、Path、Workload 或 Output Use。

## Escalate

把超出当前 Authority、Risk 或 Evidence Boundary 的 Decision 交给更合适主体。

## Recover

使用 Rollback、Forward Correction、Fallback、Compensation 或人工接管恢复可接受状态。

这些动作需要成为显式 Transition，而不是只存在于 Agent 自述中。

---

# 21.17 Checkpoint Reference 保存决策边界，不是固定进度百分比

第7章拥有 **Checkpoint** 的正式定义。第21章只引用它在 Work 或 Attempt 中保存的 Baseline、State Observation、Open Risk、Evidence、Authority 与下一允许动作，用于判断 Lifecycle 从哪里继续；Checkpoint Reference 不等于 `50% complete`。

适合 Checkpoint 的触发包括：

- 即将跨越新的写入面；
- Baseline 或 Intent 变化；
- 进入不可逆动作；
- 多 Agent Handoff；
- 运行时间或成本超出当前预算；
- Evidence Gap 扩大；
- Human Decision Required；
- 需要暂停并在另一 Thread / Session 恢复。

Checkpoint 可以形成：

~~~text
continue
pause
retrieve
rebase
restrict
handoff
request_authority
stop
~~~

Checkpoint 本身是否可恢复，需要由实际 State、Artifact、Credential 和外部系统确认。

保存一个摘要并不等于保存了可恢复状态。

---

# 21.18 Observation 与 Evidence 在 Lifecycle 中承担不同作用

Observation 记录：

- Tool Action；
- Change；
- State；
- Test / Runtime Result；
- External Response；
- Permission Use；
- Detector / Gate Result；
- Human / Agent Message；
- Cost、Latency 与 Queue；
- Coverage Gap。

Evidence 则是为一个 Claim 与 Decision Use 选择、解释并保留的支持关系。

因此：

~~~text
event observed
≠ claim supported
≠ evidence coverage sufficient
≠ outcome accepted
≠ change integrated
≠ artifact released
~~~

Lifecycle 需要保存 Evidence Intended Use：

- 调试；
- Validation；
- Acceptance；
- Adoption；
- Release；
- Incident；
- Accountability；
- Memory Promotion；
- Evolution Evaluation。

同一个 Test Result 可以在多个 Decision 中被引用，但它的 Scope 不会因此自动扩大。

---

# 21.19 Evaluation Result 以 Coverage 与 `non-result` 进入 Lifecycle

第8章拥有 Evaluation Result、Target Result 与 `non-result` 的正式定义。本章只说明这些结果怎样进入 Evidence Use 与下一 Decision Target。Evaluation 可能产生：

- PASS；
- FAIL；
- Partial；
- Unknown；
- Not Applicable；
- Verifier Failure；
- Target `non-result`；
- Coverage Gap；
- Counterevidence；
- Re-run / Human Review Required。

原大纲中的 `Evidence Collection` 不应被画成一个自动完成的节点。

更准确的 Lifecycle 输出是：

~~~text
Evidence Set
+ Claim and Scope
+ Coverage Statement
+ Counterevidence / Limitation
+ Evaluation Identity
+ Decision Use
~~~

如果 Verifier 在目标前失败，Target 没有执行，就不能为了保持流程连续而填入 Target FAIL。

如果 Test PASS 但没有覆盖 Scope Fit、Authority 或 Release Condition，也不能跳过相应 Decision。

---

# 21.20 Authorized Disposition 选择下一条 Lifecycle 路径

第9章拥有 Decision Target、Decision Record 与 Disposition 的上位定义。本节只说明有权处置如何选择 Lifecycle Transition，不建立新的 `Authorized Disposition` 类型或通用枚举。

具名 Decision Target 的处置可能是 accept、reject、narrow、defer、block、cancel、authorize、adopt、retire 或其他由该 Contract 定义的结果。它随后可以允许 proceed、retrieve、replan、rework、integrate、rollback、suspend 等下一 Transition；这些动作路径本身不是通用 Disposition。

`unknown` 是当前 State Claim、Evaluation Result 或 Finding 的不足状态，不是已经作出的处置。如果材料或 Authority 不足，有权主体可以 defer、hold、block 或 request-evidence，并显式保留 Unknown。

Lifecycle 投影至少读取：

- Decision Target；
- Subject / Artifact / Change；
- Scope 与 Environment；
- Evidence 与 Coverage；
- Authority；
- Effective Time 与 Expiry；
- Open Risk、Condition 与 Follow-up；
- 下一允许 Transition。

Human 仍拥有方向、体验、审美和最终观点，不表示每项低风险 Transition 都必须人工点击。

Policy 或 Automated Gate 可以在明确 Grant 内作出处置。

---

# 21.21 Completion 是多种关系，不是一列 `done`

需要区分：

~~~text
Agent Claimed Completion
Attempt Closed
Attempt Outcome Recorded
Target Result Formed or explicitly `non-result`
Evaluation Completed
Evidence Ready
Outcome Accepted for Scope
Change Integrated
Artifact Released
Operational Baseline Active
Learning Candidate Promoted or Adopted
~~~

它们不是一条通用成熟度阶梯，也不会自动连续发生。

**Closure（关闭）** 是停止某个具名对象当前活动关系的统称，不是一组可以跨 Target 共用的状态枚举。下表只是上游 Target-specific 关系在 Lifecycle 中的投影，不重新定义 Work、Attempt Outcome、Result 或 Decision。关闭时仍要保留 Outcome、Open Item、Evidence、Authority 与后续路径：

| Closure Target | 可使用的 Target-specific Status 示例 |
|---|---|
| Work | closed / cancelled / transferred-with-open-items / abandoned |
| Attempt | completed / failed / cancelled / pre-target-blocked |
| Decision Case | decided / deferred / superseded / expired |
| Release Execution | completed / failed / partially-executed / rolled-back / unknown-external-result |

Target `non-result` 是 Target Result 缺席的显式分类，不是 Attempt、Work 或 Decision Case 的 Closure Status。

Work Acceptance 不自动关闭 Work；是否关闭仍取决于具名 Work 的关闭条件与 Authority。Failure 可以关联某个 Attempt Outcome，并触发 Attempt Closure，但它仍是第8章相对于具名 Contract、Target 或 Criterion 的有范围偏离分类，不应被缩成一个没有结果关系的状态字符串。关闭不是把未知清零，也不是把所有下游 Lifecycle 一起关闭。

---

# 21.22 Integration 是目标 Baseline 的处置

Integration 需要回答：

- 哪个 Change 被接受进入哪个 Target Baseline；
- Source 与 Target Revision 是什么；
- 是否存在 Conflict、Dirty State 或并行 Change；
- Test / Review Evidence 适用于哪个组合；
- 谁拥有 Integration Authority；
- Integration 后怎样重新观察状态；
- 失败时怎样恢复或 Forward-correct。

Merge Command 成功不等于 Integration Outcome 已接受。

例如：

- Git Merge 可以完成，但生成行为不符合产品 Intent；
- Artifact 可以被复制，但目标 Environment 状态未知；
- 多 Agent Output 可以组合，但责任和冲突仍未处置；
- Rebase 可以解决文本冲突，却改变 Evaluation Baseline。

Integration 后需要针对组合状态重新观察必要 Claim，而不是把所有分支 Test 机械相加。

---

# 21.23 Release Authorization、Execution 与 Outcome 分开

Release 相关 Target 可以包括：

- Package / Binary 发布；
- Production Deployment；
- Feature Flag 开启；
- Data Migration；
- Content / Asset 发布；
- API / Model / Tool Policy 激活；
- 面向客户、玩家或组织的 Workflow 启用。

首先需要分开三个关系：

1. `Release Authorization`：具名 Authority 是否允许 Target 进入指定发布面；
2. `Release Execution`：实际分发、部署或推进的一次或多次 Attempt；
3. `Release Outcome`：目标环境、用户或下游实际观察到什么后果。

Release Execution 与相应 Lifecycle Transition 需要绑定：

- Release Candidate Identity；
- Target Environment / Population；
- Release Authorization / Authority Grant Reference；
- Executing Subject、Execution Contract 与 Attempt Identity；
- Data、Security、Privacy、IP 与 Operational Boundary；
- Validation、Canary 与 Stop Condition；
- Rollback / Forward Recovery；
- External Effect Observation；
- Unknown Result 与 Incident Path。

`deployment command exited 0` 不能单独证明 Release Outcome 健康，也不能证明更高 Scope 的 Production Qualification 已成立。

项目需要保留“已授权但未执行”“执行失败”“部分执行”“执行后撤回”以及“执行成功但更高资格仍未成立”等可表达状态，并观察目标环境实际 State Claim 与用户可见 Outcome。

---

# 21.24 Operations 会重新打开 Lifecycle

Deployment 不是 Lifecycle 终点。

第20章的 Operational Baseline、Evaluation Window、Drift Finding 与 Re-evaluation Case
进入这一位置。

运行中可能观察到：

- Outcome 或 Reliability 变化；
- Model、Tool、Permission、Control 或 Evaluation Drift；
- Cost、Latency、Capacity 或 Human Load 变化；
- Provider Terms、Region、Retention、License 或 Rights Boundary 变化；
- Incident、Unknown External Result 或 Recovery Failure；
- 新用户、Workload、Environment 或用途。

这些 Trigger 可以重新打开：

- Intent；
- Grounding；
- Design / Plan；
- Evaluation；
- Security / IP Disposition；
- Release / Rollback；
- Memory / Evolution Candidate；
- Retirement Decision。

Lifecycle 因此是持续适用性管理，不是 Release 前的一次审批链。

---

# 21.25 Learning 只产生 Candidate，不自动修改未来行为

成功、失败、Incident、Override 和 Human Correction 都可能产生 Learning Candidate。

但它们需要另外检查：

- Source 与 Provenance；
- Observable Fact、Judgment、Inference 与 Recommendation；
- Scope 与适用条件；
- Counterexample 与 Conflict；
- Privacy、Security、Rights 与跨项目边界；
- Evaluation、Promotion / Adoption Authority；
- Expiry、Rollback 与 Revocation。

候选关系是：

~~~text
Work / Operations Outcome
→ Learning Candidate
→ separate evaluation and disposition
→ optional Memory Promotion or Evolution Adoption
→ future Baseline
~~~

不使用：

~~~text
task completed
→ memory updated
→ workflow improved
~~~

Change 不自动等于 Improvement，保留记录也不自动等于未来应检索或执行。

---

# 21.26 Gate、Validation、Review、Decision 与 Acceptance 分开

Lifecycle 中的控制词很容易被混用。

| 上游对象 | 在 Lifecycle 中的作用 | 不自动产生 |
|---|---|---|
| Validation | 检查具名可判定条件 | Scope Fit、Authority 或 Acceptance |
| Review | 依第10章的 Review Contract 检查具名 Review Target | 执行 Permission 或最终 Decision |
| Finding | 记录 Review 在具名 Criteria、Evidence 与 Coverage 内形成的有范围判断 | Authority 或动作许可 |
| Review Disposition | 具名 Authority 对“如何关闭、限制或继续使用某个 Review Target”这一 Decision Target 作出的处置 | Adoption 或 Release Authorization |
| Gate | 控制某类 Transition 是否可以发生 | Human Approval、Truth 或 Root Cause |
| Decision Record | 持有有效 Authority Grant 的 Subject 对具名 Decision Target 记录 Disposition | 描述性事实一定为真 |
| Approval | 允许具名 Target Action 的一种 Decision | Outcome Acceptance |
| Acceptance | 针对 Outcome、Claim、Scope 与用途的处置 | Integration、Release 或长期适用性 |

**Decision Gate（决策门：针对具名 Lifecycle Transition，依据预先规定的输入、
Evidence、Policy 与 Authority，允许、阻断、限制或升级下一动作的控制点）** 可以：

- 自动允许已授权的低风险 Transition；
- Fail Closed；
- 返回 `unknown`；
- 请求 Human Decision；
- Narrow Scope；
- 创建新 Attempt；
- 触发 Pause、Fallback 或 Recovery。

Gate 不能仅因存在就证明输入正确、Reviewer 理解充分或 Target Outcome 已达成。

---

# 21.27 原来的十个 Gate 是候选 Decision Target

原大纲列出的 Gate 可以按以下方式保留：

| 原 Gate | 候选 Decision Target | 何时可能值得独立 |
|---|---|---|
| Intent Gate | Intent 是否足以打开当前 Work | 多方冲突、高错误成本、开放式委托 |
| Context Gate | 当前信息是否足以支持下一动作，且允许进入该处理面 | 数据受限、来源冲突、高状态不确定性 |
| Plan Gate | Plan / Contract 是否在 Authority、Scope 与 Recovery 内 | 长任务、跨系统、难恢复动作 |
| Risk Gate | 是否满足 Protected Floor 与当前风险处置 | 高影响、不可逆、受监管动作 |
| Checkpoint Gate | 是否 Continue、Rebase、Restrict、Handoff 或 Stop | 长任务、并发写入、状态易漂移 |
| Evidence Gate | Evidence 是否足以支持具名 Decision Target | Acceptance、Adoption、Release 等重要处置 |
| Merge Gate | Change 是否适合进入目标 Baseline | Conflict、Scope、Review、组合风险 |
| Deployment Gate | Candidate 是否可进入具名 Environment / Population | 外部影响、恢复要求高 |
| Memory Gate | Candidate 是否可 Promote 到具名 Memory Scope | 长期、跨会话、跨项目传播 |
| Evolution Gate | Candidate 是否可 Adopt / Activate | Skill、Workflow、Policy、Organization 变化 |

不是每项 Work 都需要十个 Gate。

多个 Decision Target 可以在一份 Brief、Review 或 Policy 中组合，只要 Scope、Authority、
Evidence 和 Disposition 仍然可区分。

---

# 21.28 Gate 的存在需要下游 Decision Use

每个 Gate 至少要回答：

- 它保护哪个 Transition；
- 防止或暴露什么具体问题；
- 输入来自哪里，Coverage 如何；
- PASS、FAIL、Unknown 与 Error 分别意味着什么；
- 谁可以配置、Override 或关闭它；
- Override 的 Scope、Expiry 和 Evidence 是什么；
- Gate Failure 与 Target Result 怎样分开；
- 它的运行、等待、误报、漏报和维护成本是什么；
- 没有这个 Gate 时由哪个机制承担边界。

如果一个 Gate 不能指出 Decision Use，只因为“成熟流程应该有”而存在，它可能只是
增加 Governance Surface。

删除 Gate 也不是默认改进。

需要确认其保护的风险已经消失、被其他控制覆盖，或由具名 Authority 接受剩余风险。

---

# 21.29 Human Approval 只放在需要 Human Judgment 的转换上

Human 适合处理：

- Intent、Priority 与 Trade-off；
- Product、Creative、Experience 与 Ethical Judgment；
- 多方 Authority 冲突；
- Scope、Rights 或例外无法由 Policy 判定；
- 不可逆、高影响或责任重大的动作；
- Evaluation Coverage 不足但必须作出的有范围决定；
- Adoption、Release、Takeover 与 Incident 处置。

Human 不需要逐项点击：

- 重复、低风险、已预授权的 Read-only Action；
- 有确定 Contract 和 Validation 的局部转换；
- Policy 已授予 Automated Gate 的窄处置；
- 只用于收集 Evidence、不产生外部副作用的步骤。

有效 Human Decision Interface 应显示：

- Decision Target；
- Scope 与 Non-goal；
- Baseline 与 Change；
- Evidence、Coverage、Counterevidence；
- Effect、Risk 与 Recovery；
- 可选 Disposition；
- 需要 Human 提供的判断。

把全部原始记录倾倒给 Human，不等于保留 Human Control。

---

# 21.30 Adaptive Governance 不是自动增加流程

**Adaptive Governance（适应性治理：依据当前 Work 的实际行动面、不确定性、影响、
恢复能力和 Evidence，在 Protected Floor 之上调整控制强度与路径的有权机制）** 允许：

- 新风险出现时增加 Check、Review、Restriction 或 Human Decision；
- Scope 缩小时移除不再服务于 Decision Target 的非关键步骤；
- 从 Manual Review 迁移到有授权的 Automated Gate；
- Detector Coverage 下降时暂停或切换 Fallback；
- 从一次全量 Review 改成 Sampling 与 Exception Routing；
- 在 Incident 后临时提高控制并设置 Expiry；
- 在 Evidence 成熟后扩大已验证 Scope。

它不允许执行 Agent：

- 自行扩大 Authority；
- 降低 Protected Control Floor；
- 忽略已触发的 Hard Stop；
- 把未知风险重新标成低风险；
- 通过改写 Baseline 消除 Conflict；
- 为降低 Cost 删除法定、合同要求或明确保留给 Human 的 Decision Type。

自适应的对象是 Profile 和路径，不是把 Governance 本身交给执行者自由解释。

---

# 21.31 Protected Control Floor 跨路径保持

不同 Lifecycle Profile 可以具有不同步骤，但某些控制在特定 Scope 内不能被普通执行者取消。

候选 Floor 可能包括：

- Secret 不进入 Prompt / 普通 Log；
- Production Write 需要具名 Identity、Scope 与 Authority；
- Target `non-result` 不被伪造为 PASS / FAIL；
- Evidence、Incident 与历史 Baseline 不被静默重写；
- 不可逆动作具有 Stop、Confirmation 与 Recovery；
- 跨 Project / Tenant 默认隔离；
- Memory / Evolution 不自动获得跨 Scope 传播权；
- Human 对指定方向和必须由 Human Judgment 完成的 Decision Type 保留裁决权，并映射到具名 Human Authority Grant 或制度边界。

Floor 由 Policy、法定 / 合同要求和有权角色定义。

它不是全书统一清单。

Profile 可以增加控制，也可以在 Authority 和 Evidence 支持下调整 Floor 之上的步骤。

---

# 21.32 Execution Epoch 是可选受控运行区间

**Execution Epoch（执行区间：从某个 Execution Contract 被打开，到关闭、重启或显式
Rebase 之间，由固定引用的 Intent、Baseline、Authority、Tool 与 Governance 配置约束的
受控运行区间）** 适合：

- 跨会话或持续较长时间；
- 外部状态可能变化；
- 多 Agent / Tool 需要共享 Correlation Boundary；
- 中途变化不能静默替换 Baseline；
- 需要 Pause、Rebase、Escalate 或 Recover；
- Close 时需要明确 Attempt / Output State。

它不一定适合：

- 单文件低风险修正；
- 一次只读查询；
- 已由现有 Transaction、Job、Run 或 Request 明确覆盖的工作；
- 引入新名词的维护成本高于边界收益的项目。

Epoch 是 Contract 的生命周期区间，不复制 Intent、Context、State、Policy 和 Evidence
成为大型容器。

本章不要求每个 Lifecycle Profile 都打开 Epoch。

---

# 21.33 Sprint、Task、Run、Attempt、Transaction 与 Epoch 不是同义词

| 概念 | 主要边界 |
|---|---|
| Sprint | 团队规划、协调和交付节奏 |
| Task / Work Reference | 目标、Scope、责任和完成边界 |
| Run | 一次程序、Workflow 或服务运行实例 |
| Attempt | 针对同一 Work 的一次有身份执行尝试 |
| Transaction | 具有 Commit / Rollback 或补偿语义的状态变化边界 |
| Execution Epoch | 可选的固定引用与治理区间 |

一个 Sprint 可以包含多个 Work、Run 与 Epoch；一个长期 Work 也可以跨越多个 Sprint。

一个 Attempt 可以包含多个 Transaction；一个 Transaction 也可能由非 Agent 系统执行。

AI Game Dev OS 可以使用 Sprint 组织开发，但不能由此推出 Sprint-based Epoch 是
AI-native SDLC 的唯一实现。

---

# 21.34 Failure、Unknown 与 Recovery 是正式分支

第8章拥有 Failure、`non-result`、Unknown 与 Recovery 的结果分类；本节只说明它们如何触发 Lifecycle Transition，不重新定义失败或恢复对象。

| 事件 | Lifecycle 可能转换到 |
|---|---|
| Intent Conflict | Stakeholder / Intent Formation |
| Missing Context | Retrieval / Human Request / Narrow Scope |
| State Conflict | Conflict Decision / Hold / Alternate Baseline |
| Baseline Drift | Pause / Rebase / New Attempt |
| Permission Denied | Replan / Authority Request / Cancel |
| Verifier Failure before Target | Preserve Evidence / Target `non-result` / Repair Verifier |
| Target Validation Failure | Rework / Narrow / Reject |
| Scope Not Accepted | Narrow / Replan / Reject |
| Integration Conflict | Rebase / Conflict Decision / New Evaluation |
| Release Failure | Rollback / Forward Recovery / Incident |
| Unknown External Result | Stop New Action / Observe / Incident / Human Decision |
| Operational Drift | Restrict / Reroute / Re-evaluate / Retire |
| Authority Revoked | Stop / Revoke Credential / Preserve State / Reauthorize |

Recovery 也可能失败。

Lifecycle 需要允许：

- recovery pending；
- partial restoration；
- data repair required；
- manual takeover；
- forward correction；
- permanent limitation；
- residual risk accepted / rejected。

如果流程图只有 Happy Path，最重要的工程状态会被藏在方框之外。

---

# 21.35 Multi-Agent 只改变 Assignment 与 Handoff，不改变完成语义

多 Agent Lifecycle 需要额外处理：

- Work Decomposition 与 Assignment；
- Shared / Local Baseline；
- Read / Write Ownership；
- Handoff Contract；
- Conflict 与 Integration Authority；
- Parallel Attempt Identity；
- Output Triage；
- Reviewer Independence；
- Controller / Worker Failure；
- Cancellation 与 Revocation Propagation。

但 Agent 数量不会改变以下关系：

- Test PASS 不自动产生 Acceptance；
- Permission 不自动产生 Authority；
- Handoff 不自动转移 Accountability；
- 子任务 `done` 不自动完成 Parent Work；
- 多个 Output 不自动形成可集成 Change；
- Summary 不自动覆盖 Source Evidence。

一个单 Agent 加清楚 Contract、Tool 和 Human Checkpoint，可能比多 Agent 组织更适合
紧耦合、低风险或输出很小的 Work。

---

# 21.36 三类候选 Profile 只用于说明裁剪

以下不是成熟度等级，也不要求项目沿序列升级。

## 局部、可逆、易观察

~~~text
Need / brief
→ Intent + Scope + Acceptance Target
→ current file / state reference
→ one bounded edit Attempt
→ automated validation
→ diff / outcome disposition
→ integrate or reject
~~~

通常不需要独立 Epoch、多 Agent 或十个 Gate。

## 跨会话、跨角色或存在集成风险

~~~text
versioned Work + Baseline + Context Manifest
→ Execution Contract
→ Attempt / Handoff Identity
→ Checkpoint and Evidence Plan
→ Integration Disposition
→ close with open items / next baseline
~~~

必要时使用 Execution Epoch，但不是默认。

## 高影响、难恢复或多方 Authority

~~~text
Intent and affected-party decision
→ Grounding + Security / Rights boundary
→ Protected Control Floor
→ staged Execution Contract
→ independent evaluation / review as required
→ canary / release decision
→ operational observation and re-evaluation
→ recovery / retirement path
~~~

高影响不自动要求多 Agent；独立 Authority、Recovery 和 Evidence Boundary 比角色数量更重要。

---

# 21.37 AI Game Dev OS v4.94 提供状态与处置语义案例

AI Game Dev OS v4.94 的既有记录已经在[第16章](第16章_Self_Evolution_Engineering_首轮修订稿.md)、
[第19章](第19章_Security_Privacy与IP_Boundary_首轮修订稿.md)和
[第20章](第20章_AgentOps_成本与模型漂移_首轮修订稿.md)中限定了 Evidence 用途。

本章只使用以下 Lifecycle 关系。

## D-073 至 D-075

Governance / Proof Surface 发生变化，但 Source、Runtime、Test、Qualification 与 Gate
Evidence 没有同步前进。

这说明：

- Governance Activity 不是 Delivery Transition；
- Artifact 数量不能代替 Outcome State；
- Process Warning 需要指出当前受保护 Claim 或缺失进展；
- Lifecycle 需要允许“活动发生但目标未推进”。

它不证明严格治理必然造成 Livelock。

## D-048

Verifier 在 Target 前改变 Authority-bearing Surface，后续 Check Fail Closed，Target
没有执行。

Lifecycle 需要保存：

~~~text
verifier transition: failed
attempt outcome: pre-target-blocked
target result: non-result
baseline integrity: changed
next path: preserve → repair verifier / new attempt
~~~

它不证明所有 Tool 必须绝对无副作用，也不证明 Exact Inventory 是唯一控制。

## D-079

Over-scoped Candidate 的 Selected Tests 通过，但 Human 没有接受 Scope；较小 Forward
Correction 成为后续 Baseline。

这说明：

~~~text
evaluation completed
≠ scope accepted
≠ candidate adopted
≠ long-term improvement proved
~~~

## F1–F4a

后续形成 Source、Read-only Replay、Package Identity 与 Bounded Test Evidence，但结果仍
明确为 `NON_QUALIFYING`。

Evidence Use 可以分阶段，`NON_QUALIFYING` 不能从 Lifecycle 图中消失。

这些案例没有提供新旧 Lifecycle 的时间、返工、缺陷、等待或成本对照。

完整时间序列仍由第23章承担。

---

# 21.38 最小实现从一类重复 Work 开始

选择一类：

- 重复发生；
- Intent 与 Acceptance Target 可以说明；
- Baseline 和 Attempt 可以识别；
- 失败、Handoff、Review 或 Recovery 已出现真实问题；
- 有具名 Owner 和 Decision Authority；
- 可以限制 Scope。

建立最小 Lifecycle：

1. 引用或标识第7章定义的 Work，并声明 Scope、Non-goal 与 Acceptance Target；
2. 记录最小 Baseline、Context 和 Known Gap；
3. 绑定 Tool、Permission、Authority 与 Prohibited Effect；
4. 引用或标识第7章定义的 Attempt，并声明关闭条件；
5. 选择一个 Claim-matched Evaluation；
6. 保留 PASS、FAIL、Unknown、Verifier Failure 与 `non-result`；
7. 绑定一个 Acceptance / Integration Decision Target；
8. 为 Baseline Drift 或 Permission Denial 定义一条返回路径；
9. 明确是否产生 Memory / Evolution Candidate；
10. 删除不支持任何 Transition 或 Decision 的 Gate 与字段；
11. 在一次真实 Work 后检查 Profile 是否过重或遗漏；
12. 再决定是否需要自动化或扩展。

最小实现的目标不是把所有章节对象放进一份 Schema。

它是让一个真实 Work 的打开、执行、评价、处置和关闭不再依赖隐含关系。

---

# 21.39 与相邻章节的接口

## 第4–6章：Intent、Context、Truth 与 State

第4章拥有 Intent 和 Acceptance Target；第5章拥有 Context Contract / Manifest；第6章
拥有 State Claim、Decision、Assumption、Conflict 与 Baseline。

第21章只说明它们何时进入 Transition，不创建统一 Truth Container。

## 第7–10章：Execution、Reliability、Evidence Use 与 Review

第7章拥有 Work、Execution Contract、Attempt、Checkpoint 与 Bounded Execution；第8章拥有 Attempt Outcome、Target Result、Evaluation Result、Failure、`non-result` 与 Recovery；第9章拥有 Evidence Use、Decision Target、Acceptance、Adoption 与 Release Authorization；第10章拥有 Review、Review Target、Finding、Review Budget、Review Independence 与 Review Disposition。

第21章只组织这些对象进入 Lifecycle Transition 的路径，不重新定义它们。

## 第11–14章：Human、Authority、Observation 与 Intervention

Human Decision Interface、Protected Floor、Detector、Pause、Takeover 与 Recovery 约束
Lifecycle Transition；第21章不复制其内部对象。

## 第15–17章：Memory、Evolution 与 Organization

Lifecycle 只产生 Learning Candidate；Promotion、Adoption、Role、Handoff 和 Integration
继续由对应章节拥有。

## 第18–20章：Trace、Boundary 与 Operations

Trace 提供外部决策环境；Security / IP 约束 Data、Tool 和 Release；AgentOps 处理采用后
Baseline、Drift、Cost 与 Re-evaluation。

Lifecycle 引用这些关系，但不成为全书新的 Truth Store。

## 第22–23章：能力适配与案例

第22章应讨论项目怎样选择足够的 AI-native 能力，而不是按更多 Agent、Gate 和 Registry
形成成熟度阶梯。

第23章负责展开 AI Game Dev OS 的时间序列，不让第21章案例段代替完整叙事。

---

# 21.40 本章原则

1. **Traditional SDLC remains.** AI-native 增加受托执行控制关系，不删除软件活动。
2. **Lifecycle is a transition network, not a mandatory pipeline.** 路径允许循环、停止、恢复和重开。
3. **Work, Attempt, Outcome, Change and Release are different identities.** 一个 `done` 不覆盖全部对象。
4. **Phase is not state.** 进入阶段不表示对应结果已发生。
5. **Intent does not grant every action.** 方向、执行、集成、发布和学习分别需要 Authority。
6. **Grounding is scoped.** Context、State、Decision、Assumption 与 Conflict 不压成最终 Truth。
7. **Plan is a proposal; Contract bounds execution.** Plan Review 不自动产生 Permission。
8. **Every Attempt preserves its baseline.** 新尝试不覆盖旧失败或 `non-result`。
9. **Observation is not Evidence, and Evidence is not Acceptance.** 每个关系绑定 Claim 与 Decision Use。
10. **Disposition selects the next path.** Gate 或 Test 结果不能自行跳过 Authority。
11. **Closure preserves unknowns.** 关闭不把未知、Open Item 或外部不确定结果清零。
12. **Integration, Release and Operations are separate.** Merge 或 Deploy Command 不等于外部 Outcome 已接受。
13. **Learning begins with a candidate.** Memory 与 Evolution 不因任务完成自动更新。
14. **Adaptive governance changes profiles, not protected rights.** 执行者不能自行降低 Floor 或扩大 Authority。
15. **Execution Epoch is optional.** 它是受控区间，不是超级 Lifecycle。
16. **Sprint is a planning rhythm, not the only lifecycle unit.** Task、Run、Attempt、Transaction 与 Epoch 保持区分。
17. **Failure and recovery are first-class branches.** Happy Path 不是完整 Lifecycle。
18. **More gates do not imply more maturity.** 每个控制需要 Decision Use、Owner、成本和替代路径。

---

# 21.41 常见 Anti-pattern

- 用更长 Pipeline 替代传统 SDLC；
- 要求每项任务访问所有阶段；
- Truth Resolution 一次产生最终事实；
- 把 Context Pack 称为内容已验证；
- Plan Review 等于执行授权；
- 每项 Work 固定十个 Gate；
- Human Approval Everywhere；
- Gate PASS 等于 Outcome Accepted；
- Test PASS 等于 Merge、Release 或 Improvement；
- 用一个 `done` 覆盖 Attempt、Outcome、Integration 与 Release；
- 把 Verifier Failure 写成 Target FAIL；
- 把 `non-result` 从指标和 Timeline 中删除；
- Rebase 时重写旧 Baseline；
- Sprint 等于 Execution Epoch；
- 所有任务强制打开 Execution Epoch；
- 多 Agent 被当成高成熟度的必要条件；
- Agent 数量决定 Review 独立性；
- Task 完成后自动 Promote Memory；
- Reflection 自动修改 Skill / Policy；
- Deployment 被画成流程终点；
- Incident 只进入 Root Cause，不先 Contain / Recover；
- 把 Activity Count 当成 Lifecycle Progress；
- 为降低 Governance Cost 删除 Protected Floor；
- 使用固定低／中／高 Profile 掩盖实际风险面；
- 为所有 Transition 创建独立 Registry 和 Dashboard。

---

# 21.42 检查清单

本清单按当前 Lifecycle Profile 检查适用项；不适用项可以标为 `N/A`，不能为了勾选而新增对象。

## Work 与 Identity

- [ ] Need / Trigger 是否只打开 Candidate，而不是自动执行？
- [ ] Work、Attempt、Attempt Outcome、Target Result、Evaluation Result 与 Change 是否分别可识别？
- [ ] Intent、Scope、Non-goal 与 Acceptance Target 是否明确？
- [ ] Parent / Child Work 与 Handoff 是否保留责任和 Open Item？

## Grounding 与 Contract

- [ ] State Claim、Lifecycle Status、Decision、Assumption、Conflict 与 Context 是否保持类型边界？
- [ ] Baseline、Source、Revision、Environment 与 Dirty State 是否可定位？
- [ ] Execution Contract 是否绑定 Tool、Permission、Authority、Evidence、Stop 与 Recovery？
- [ ] Grounding 不足时是否允许 Retrieve、Narrow、Hold 或 Cancel？

## Profile 与 Governance

- [ ] Lifecycle Profile 是否依据实际风险面，而非固定等级？
- [ ] Protected Control Floor 与可调整步骤是否分开？
- [ ] 执行 Agent 是否被禁止自行扩大 Authority 或降低 Floor？
- [ ] Gate 是否有 Decision Target、Owner、Evidence、Disposition、Expiry 与成本边界？
- [ ] 没有 Decision Use 的 Gate 是否可以合并或删除？

## Execution 与 Checkpoint

- [ ] 每个 Attempt 是否绑定 Contract、Baseline 和配置 Identity？
- [ ] Retrieve、Pause、Rebase、Restrict、Escalate 与 Recover 是否为显式 Transition？
- [ ] Checkpoint 是否保存实际可恢复边界，而非只有摘要？
- [ ] Baseline 变化是否创建新引用或 Attempt，而非覆盖过去？

## Evidence 与 Decision

- [ ] Observation、Evidence、Coverage、Review、Decision 与 Acceptance 是否分开？
- [ ] PASS、FAIL、Partial、Unknown、Verifier Failure 与 Target `non-result` 是否可表达？
- [ ] Evidence Intended Use 是否绑定 Acceptance、Adoption、Release Authorization 等具体 Decision？
- [ ] Automated Gate 是否只在明确 Grant 内作出处置？

## Closure、Integration 与 Release

- [ ] Attempt Closure 与 Work Closure 是否分开？
- [ ] Accepted Target 是否不自动产生 Integration 或 Release Authorization？
- [ ] Integration 后是否观察组合状态和 Conflict？
- [ ] Release Authorization、Release Execution 与 Release Outcome 是否分别绑定 Target、Environment、Authority、Attempt、Rollback 与 External Effect Observation？
- [ ] Unknown External Result 是否有停止、观察与 Incident Path？

## Operations 与 Learning

- [ ] Operational Baseline、Drift 与 Re-evaluation 是否可以重新打开 Lifecycle？
- [ ] Memory / Evolution 是否只接收 Candidate？
- [ ] Promotion、Adoption、Activation、Rollback 与 Revocation Authority 是否具名？
- [ ] 第23章案例叙事是否没有被 Lifecycle 抽象取代？

## Cost 与裁剪

- [ ] 当前 Profile 的 Gate、Review、Trace 和 Handoff 成本是否进入比较？
- [ ] 局部可逆 Work 是否能压缩流程？
- [ ] 高影响 Work 是否依据实际 Data、Authority、Recovery 和 Rights 增加控制？
- [ ] Profile 是否可以在新 Evidence 和 Authority 下调整，而不静默改写历史？

---

# 21.43 结论

AI-Native Software Development Lifecycle 不是在传统 SDLC 后面再增加一串 Agent 方框。

它处理的是受托执行带来的转换关系：

~~~text
Need / Trigger
→ Intent and Acceptance Target
→ scoped Grounding
→ Execution Contract and Attempt
→ Observation, Evidence and Coverage
→ Authorized Disposition
→ Integration Authorization / Release Authorization / Rejection / Recovery
→ Integration Execution / Release Execution
→ Integration Outcome / Release Outcome
→ Operations and Re-evaluation
→ optional Learning Candidate
~~~

这条主干允许循环、分支、暂停、失败、未知和关闭。

它的质量不由阶段数量、Gate 数量、Agent 数量或 Automation 数量决定。

更重要的是：

- 每个 Work 和 Attempt 有身份；
- 每个受托动作有 Scope、允许影响面和具名 Authority；
- Result、Failure、Unknown 和 `non-result` 保持可见；
- Stop、Recovery 或能够安全丢弃本次 Attempt 的边界可被识别；
- 当 Profile 实际引入 Baseline、Evidence、Gate 或 Decision 时，它们分别绑定 Scope、用途、Transition、Decision Target 与后续路径；
- Integration、Release、Operations 和 Learning 不被压成同一个“完成”；
- 流程可以按风险和恢复条件裁剪，但 Protected Floor 不由执行者自行降低。

一个成熟的 Lifecycle 可能很短。

对于局部、可逆、易观察的 Work，它可以是一份清楚 Brief、一次受限 Attempt、一个匹配
Claim 的 Validation 和一次有权处置。

对于长生命周期、高影响或多方 Authority 的 Work，它才需要更强 Baseline、Contract、
Checkpoint、Recovery、独立 Review、Release 和 Operations 路径。

下一章将讨论项目怎样判断自己真正需要哪些 AI-native 能力。这个判断不应形成“更多
Registry、更多 Agent、更多 Gate、更多 Automation 就更成熟”的单轴阶梯，而应关注：
当前机制能否在可接受治理成本下维持具名 Workload 的最低 Work / Attempt Identity、Scope、Authority、结果可见性与
Stop / Recovery 边界，并只在条件触发时增加 Grounding、Evidence、Human Decision 和长期治理机制。
