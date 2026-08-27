# 第16章 Self-Evolution Engineering
## 变化先成为候选，只有在具名目标和边界内才可能被称为改进

> 工作稿状态：首轮逻辑修订稿，不替代 [全书大纲](../OringinalDocs/beyond_code_ai_native_software_engineering_outline_zh.md) 或 [Cognitive Control、Trust 与 Human Control Plane v0.1](../OringinalDocs/ai_native_cognitive_control_trust_human_control_plane_v0.1.md)。
> 回接说明：[RR-027](../RevisedResult/RR-027_第16章Self_Evolution_Engineering首轮回接说明.md)。
> 适用边界：AI Game Dev OS v4.94 只支持在该案例中分开 Candidate、Scoped Accepted Baseline、Evaluation Evidence 与 Adoption，并记录受限 Pilot 和 Forward Correction；现有材料不能证明其改善长期效率、质量、Human Attention 或缺陷率。

第15章把执行经验保留为有来源、有范围的 Memory Candidate。

下一步不是：

~~~text
experience
→ lesson
→ rule
→ system improved
~~~

因为每个箭头都可能引入新的判断：

- 一次结果是否代表稳定模式；
- 根因是否真的被识别；
- 经验能否迁移；
- 新 Rule 是否改变 Authority；
- Candidate 是否与 Baseline 可比；
- 指标改善是否来自漏报或目标投机；
- Rollback 是否真的可用；
- 采用后是否出现新的副作用。

本章保留 Self-Evolution Engineering 这一名称，但将它限定为：

> **Self-Evolution Engineering（自演化工程：工程系统基于具名经验提出自身配置、流程、Skill、Agent Contract 或组织结构的变更候选，并通过有边界评估、Authority 裁决、采用后观察和恢复机制管理这些候选的过程）**。

这里的 “evolution” 是治理工作流名称，不表示变化天然向更好方向发展，也不表示系统拥有独立意志。

本章的中心原则是：

> **Self-evolution is not self-authorization.**

中文语义是：

> **系统可以参与发现问题、提出候选和生成 Evidence，但不能因为变化由自己提出或测试通过，就自行获得采用、扩权或宣布改进的资格。**

---

# 16.1 先区分 Change、Calibration、Adoption 与 Improvement

这些术语不能互换。

## Change（变化）

配置、Artifact、Procedure、Workflow、Contract 或组织关系发生不同。

Change 是可观察状态，不包含价值判断。

## Calibration（校准：根据当前目标、环境、阶段和 Guardrail 调整系统配置，使其更适合具名用途的过程）

Calibration 承认不存在脱离场景的全局最优。

## Adoption（采用：有权主体决定将某个 Candidate 作为具名范围内的当前使用配置）

Adoption 是 Decision，不是事实发现。

## Improvement Claim（改进主张：声称某个 Candidate 在具名目标、Guardrail、Scope、环境和观察窗口内优于或更适合某个 Baseline 的可检验主张）

Improvement 需要比较边界。

因此：

~~~text
candidate created
≠ adopted

adopted
≠ activated everywhere

test passed
≠ improved

metric moved
≠ objective achieved
~~~

---

# 16.2 必要、有用与可选

## 必要

当系统变更会影响 Authority、Safety Boundary、共享 Workflow、重要 Skill、Agent Contract 或长期组织行为时，项目需要：

- 具名 Change Candidate；
- Source 与 Problem；
- Scope 与 Owner；
- Authority；
- Evaluation 或明确的紧急处置理由；
- Recovery；
- Adoption / Rejection 记录；
- Post-adoption Observation。

## 有用

对重要、可版本化、重复且可比较的 Workflow，Baseline、Hypothesis、Objective、Guardrail、Controlled Evaluation 和 Staged Rollout 通常有用。

## 可选

自动 Pattern Mining、A/B Testing、Shadow Execution、Multi-armed Bandit、Evolution Dashboard 和自动降级建议都是可选机制。

低风险参数编辑、一次性紧急修复和不可比组织变化，不需要伪装成严格实验。

---

# 16.3 九个对象不能压成“系统学会了”

本章区分：

| 对象 | 回答的问题 | 不自动等于 |
|---|---|---|
| Change Signal | 哪个 Observation、Failure、Review 或 Human Request 提示可能需要变化 | 根因已知 |
| Learning Candidate | 从经验中提出了什么 Pattern、Lesson 或改进方向 | 通用规律 |
| Change Candidate | 准备改变哪个具名系统表面 | 已经改进 |
| Baseline | 当前比较或恢复参照是什么 | 永久 Known-Good |
| Evaluation Contract | 用什么 Claim、Objective、Guardrail、样本和停止条件检查 Candidate | 评估必然有效 |
| Evaluation Evidence | 实际观察了什么 | Adoption Decision |
| Adoption Decision | 是否在具名范围采用 Candidate | 已全量激活或发布 |
| Activation / Rollout Record | Candidate 在哪里、何时、以何种比例或阶段运行 | 目标收益已实现 |
| Post-adoption Disposition | 采用后保留、收窄、撤回、前向修正还是扩大 | 永久 Improvement |

**Change Signal（变化信号：提示某个系统表面可能需要重新检查的具名 Observation、Failure、Conflict、Metric、Review 或 Human Request）** 只是入口。

**Learning Candidate（学习候选：从一个或多个有来源经验中提出、尚未验证其适用性和因果解释的 Pattern、Lesson 或 Rule Proposal）** 仍是推导。

**Change Candidate（变更候选：对具名 Configuration、Skill、Workflow、Agent Contract、Policy 或 Organization Surface 提出的版本化改变）** 是待评估对象。

**Evaluation Contract（评估契约：声明 Candidate 的比较问题、Baseline、Objective、Guardrail、Evidence、样本、完整性、停止与恢复条件的约束）** 决定评估语义。

**Activation / Rollout Record（激活与逐步启用记录：说明已采用 Candidate 实际在哪些环境、角色、流量或阶段生效的记录）** 将 Adoption Decision 与真实运行状态分开。

**Post-adoption Disposition（采用后处置：具名 Authority 根据激活后的新 Evidence，通过 Decision Record 对继续、收窄、撤回、扩大或前向修正这一具名 Decision Target 作出的处置）** 是第9章 Disposition 的 Target-specific subtype，防止 Adoption 变成永久结论。

关系可以表示为：

~~~text
Observation / Failure / Human Request
→ Change Signal
→ Learning Candidate
→ Change Candidate
→ Evaluation Contract
→ Evaluation Evidence
→ Adoption Decision
→ bounded Activation / Rollout
→ Post-adoption Observation
→ keep / narrow / revoke / expand / forward-correct
~~~

它不是自动流水线。

项目可以拒绝一个 Candidate，也可以因紧急风险跳过比较、直接执行有权修复，但必须记录无法建立的 Evidence 和后续复核。

---

# 16.4 Self-modification 是机制，Evolution 是待验证的结果关系

**Self-modification（自我修改：系统中的某个执行路径改变该系统自身的配置、规则、Procedure、Workflow、Contract 或组织记录的机制）** 只描述谁改了什么。

它可能产生：

- 修复；
- 退化；
- 兼容迁移；
- 临时绕过；
- 探索性分支；
- 安全事件；
- 无实质效果。

Human 手工修改 Workflow 也可能形成有效演化；Agent 自动修改参数也可能只是 Mutation。

所以：

> 变化由谁产生，与变化是否值得采用，是两个不同问题。

Self-Evolution Engineering 关注的是 Candidate 如何被约束、比较、裁决和观察，而不是为自动修改赋予更高地位。

---

# 16.5 Evolution Surface 不是成熟度层级

原大纲把变化分为四层。本章将它们改为可组合的 **Evolution Surface（演化表面：一次候选变更实际准备影响的系统对象范围）**。

| Surface | 示例 | 主要风险 |
|---|---|---|
| Configuration | 参数、路由、Threshold、Context Selection | 隐性行为漂移、指标投机 |
| Skill / Workflow | 步骤、Tool 组合、Evidence Requirement | 重复错误、兼容性、控制缺失 |
| Agent Contract | Role、Responsibility、Stop、Escalation | Authority 漂移、职责空洞 |
| Governance / Policy | Gate、Floor、Approval、Exception | 自我授权、治理活锁、漏控 |
| Organization | Controller / Worker、Review、Handoff、Decision Path | 冲突、复杂度、责任稀释 |

这些 Surface 不是从低到高的进化阶梯。

一个参数变化可以产生高影响；一个组织标签变更也可能几乎没有运行效果。

需要根据 Action Surface、Impact、Irreversibility、Authority、Observation 和 Recovery 决定治理强度。

---

# 16.6 从经验到候选必须保留 Epistemic Type

原大纲给出：

~~~text
Execution
→ Reflection
→ Pattern Extraction
→ Rule Candidate
→ Validation
→ Skill Update
~~~

本章将它改写为：

~~~text
Execution and Observation
→ bounded record
→ Reflection Candidate
→ Pattern / Causal Hypothesis
→ Change Candidate
→ claim-specific evaluation
→ Adoption Decision
→ Post-adoption Observation
~~~

**Reflection Candidate（反思候选：Human 或 Agent 对已记录经验提出的事后解释、未知和行动建议）** 不是 Observation。

**Pattern Candidate（模式候选：声称多个有来源事件在声明条件下具有可复用相似性或关系的推导）** 需要保留：

- Source Set；
- Sampling Boundary；
- Similarity Basis；
- Counterexample；
- Alternative Explanation；
- Scope；
- Confidence Basis；
- Intended Decision Use。

一次失败可以产生调查问题，不能单独证明 Pattern。

Pattern Extraction 也不能用同一 Source 的多个 Summary 制造样本数量。

---

# 16.7 Learning from Failure 先分结果，再分原因候选

原大纲列出偶发、环境、工具、推理、设计、流程、权限和 Context Failure。

这些可以作为诊断视角，但不是互斥根因分类。

首先引用第7–10章的既有关系，不建立新的“学习结果”枚举：

| 上游关系 | 在本节中的含义 |
|---|---|
| Attempt Outcome | 本次执行实际触达哪里、产生什么外部后果 |
| Target Result / explicit `non-result` | 预期 Target 形成了什么结果，或已确认没有形成该 Target 的结果 |
| Evaluation Result | 具名 Test、Verifier 或 Human Evaluation 对哪个 Target、Criteria 与运行得出什么 |
| Acceptance / Adoption Disposition | 有权主体是否接受该结果用于具名 Scope，或是否采用 Candidate |
| Later Failure / Finding | 后来发现什么未检测问题、Coverage Gap 或新的不符合；不重写过去记录 |

历史材料中的 `target_fail`、`target_pass_but_unaccepted`、`partial`、`intervention_failure` 与 `escaped_failure` 只能作为上述关系的局部简写：`target_pass_but_unaccepted` 分开 Evaluation PASS 与 Acceptance Disposition；Intervention 的失败仍要落到其 Attempt / Target / Evaluation；Escaped Failure 是后来形成的 Failure / Finding，不是原运行的隐藏结果。

然后提出原因候选：

- Environment；
- Tool；
- Model / Reasoning；
- Design；
- Workflow；
- Authority；
- Context；
- State / Baseline；
- Observer / Validator；
- Dependency；
- Coordination；
- Human Decision；
- 多因素交互。

Failure Classification 需要 Evidence 和 Unknown。

例如 D-048 不能先写“推理失败”或“目标 Compile 失败”；可观察事实是 Verifier Self-mutation、Integrity Stop 与 Target `non-result`，见 [D-048 验证器自我修改案例记录](../Evidence/receipts/ER-20260818-002__CLM-C06-004.md)。

Learning from Failure 的输出应该先是：

~~~text
observed failure or non-result
+ current causal hypotheses
+ counterevidence
+ unresolved unknowns
+ candidate response
~~~

不是自动写入一条永久 Rule。

---

# 16.8 Change Candidate Contract

候选 **Change Candidate Contract（变更候选契约：把问题、假设、目标表面、范围、预期收益、Guardrail、Baseline、Authority、Evaluation 与 Recovery 绑定起来的版本化记录）** 可以是：

~~~yaml
candidate_id: WF-CAND-016
candidate_type: workflow
version: 1

observed_problem:
  claim: duplicate_governance_successors_delay_delivery_evidence
  evidence_refs:
    - GOV-INC-001

hypothesis:
  statement: >
    Separating development evidence from qualification evidence
    may reduce meta-only successor work for this v4.94 scope.
  epistemic_type: inference

target_surface:
  workflow: gate_b_development
  scope: v4.94_function_first_pilot

baseline_ref: WF-BASELINE-015
baseline_applicability: historical_comparison_only

objectives:
  - produce_bounded_development_evidence

guardrails:
  - no_production_claim
  - no_qualification_claim
  - no_authority_expansion
  - preserve_predecessor_history

evaluation_ref: EVAL-CONTRACT-016
adoption_authority_ref: AUTH-WF-ADOPT-03

recovery:
  rollback_available: false
  forward_correction: required

expires_at: 2026-09-30
~~~

这是设计 Profile，不是 v4.94 实际 Schema，也不是所有变更的强制模板。

---

# 16.9 Baseline 是有范围的参照，不是永久 Known-Good

**Scoped Accepted Baseline（有范围的已接受基线：在声明 Scope、Environment、Time 与 Intended Use 下，由有权主体接受为当前比较、运行或恢复参照的具名版本）** 可以承担：

- Comparison；
- Recovery；
- Production Continuity；
- Historical Trace；
- Candidate Parent。

但 Baseline 可能：

- 过期；
- 已不安全；
- 与 Candidate 不可比；
- 无法在新环境运行；
- 包含旧缺陷；
- 因外部迁移不能恢复；
- 只适用于 Historical Comparison。

因此不采用“永远保留 Known-Good”作为普遍规律。

更准确是：

> 仅在 Baseline 仍安全、适用且值得维护时保留比较或恢复能力；否则记录不可回退原因并建立 Forward Recovery。

---

# 16.10 Comparability 必须在评估前声明

**Comparability（可比性：Baseline 与 Candidate 在足以回答当前 Improvement Claim 的任务、输入、环境、版本、角色和观察条件上是否可进行有意义比较）** 不是“都有运行结果”。

需要检查：

- Task Mix；
- Input / Data；
- Model 与 Tool Version；
- Context；
- Authority；
- Human Reviewer；
- Environment；
- Time Window；
- Learning / Order Effect；
- Sample Size；
- Observation Coverage；
- Failure Semantics；
- Candidate Scope。

低频、高变异或创意任务可能无法形成统计对照。

此时可以使用：

- Structured Expert Review；
- Scenario Replay；
- Counterfactual Analysis；
- Bounded Pilot；
- Failure Injection；
- Qualitative Comparison；
- Explicit Uncertainty。

不能用伪精确数字替代不可比性。

---

# 16.11 Evaluation Contract 先定义 Claim，再选择指标

Evaluation 不是“跑更多测试”。

一个 Evaluation Contract 至少回答：

- Candidate 改变什么；
- 当前 Improvement Claim 是什么；
- Baseline 是否适用；
- 哪些 Objective 是 Primary；
- 哪些 Guardrail 不得退化；
- 哪些 Evidence 能回答这些 Claim；
- 哪些结果是 PASS、FAIL、Partial、Unknown 或 `non-result`；
- 谁产生 Evidence；
- 谁拥有 Evaluation Integrity Review；
- 谁拥有 Adoption Authority；
- 何时停止；
- Candidate 失败后怎样恢复。

候选结构是：

~~~yaml
evaluation_id: EVAL-CONTRACT-016
candidate_ref: WF-CAND-016
baseline_ref: WF-BASELINE-015

claims:
  primary:
    - bounded_development_evidence_is_produced
  guardrails:
    - qualification_boundary_preserved
    - production_boundary_preserved
    - authority_not_expanded

methods:
  - artifact_path_inspection
  - bounded_test_receipt
  - independent_scope_review

comparability:
  status: partial
  limitations:
    - no_controlled_time_comparison
    - accumulated_project_knowledge_differs

stopping:
  hard:
    - authority_boundary_contact
    - false_qualification_promotion
  warning:
    - repeated_meta_only_successor

decision_targets:
  - pilot_result_disposition
  - workflow_adoption
~~~

示例中的 `partial` Comparability 不妨碍产生有边界 Evidence，但禁止将结果升级为全局效率结论。

---

# 16.12 Objective 与 Guardrail 必须分别声明

单一目标容易产生 Goodhart 式替代。

例如：

~~~text
Objective:
reduce human interruptions
~~~

可能通过以下方式“达成”：

- 不报告异常；
- 延迟路由；
- 降低 Detector Sensitivity；
- 把 Decision 推迟到更晚阶段；
- 删除 Human Checkpoint；
- 将失败重新分类。

所以 Candidate 至少需要：

~~~text
Primary Objective
+ Quality Guardrail
+ Safety / Authority Guardrail
+ Recovery Guardrail
+ Human / Creative Guardrail
+ Cost Boundary
~~~

Guardrail 不是越多越好。

每条 Guardrail 应指向：

- 被保护风险；
- Observation Method；
- Failure Semantics；
- Decision Owner；
- 当前阶段；
- 维护成本。

无法指出保护对象的 Guardrail 可能重新制造 Governance Overload。

---

# 16.13 创意与体验目标不能由机器指标替代

游戏与创意软件的 Candidate 可能影响：

- Fun；
- Surprise；
- Taste；
- Pacing；
- Aesthetic Coherence；
- Player Comprehension；
- Creative Diversity。

这些目标可以使用行为数据、Playtest、Telemetry 和结构化 Review。

但机器指标不能自动替代有经验的 Human Creative Judgment。

**Human Creative Calibration（人类创意校准：由具名创意责任人依据当前产品方向、目标受众和实际体验，对 Candidate 的创意适用性作出可追踪判断）** 应保留：

- Decision Target；
- Reviewer Role；
- Product Surface；
- Build / Scenario；
- Observed Experience；
- Preference / Identity Reference；
- Alternative；
- Tradeoff；
- Disposition。

它不要求 Human 审阅每个底层动作，也不表示创意判断不可被质疑。

---

# 16.14 Evolution Gate 应拆成多个 Decision Target

原大纲要求“有来源、有对比基线、有评估、有审批、可回滚、有范围、有重新验证”。

这个方向成立，但一个统一 Evolution Gate 会把多种 Authority 合并。

更适合拆成：

| Gate / Decision | 回答的问题 |
|---|---|
| Candidate Admission | 这个问题是否值得形成正式 Candidate |
| Evaluation Authorization | 是否允许在声明环境和风险边界内评估 |
| Evaluation Integrity | Evidence 是否按 Contract 产生 |
| Result Disposition | 当前 Evidence 支持什么，不支持什么 |
| Adoption | 是否把 Candidate 设为具名范围的当前配置 |
| Activation / Rollout | 是否允许在目标环境逐步启用 |
| Release | 是否允许进入生产或外部使用 |
| Expansion | 是否扩大 Scope、角色或环境 |
| Revocation / Recovery | 是否撤回、回退或前向修正 |

这些 Decision 可以由不同 Human 或 Delegated Gate 拥有。

Test PASS 可能满足 Evaluation Integrity 的一部分，不自动完成 Adoption、Activation 或 Release。

---

# 16.15 AI Review 不能成为唯一自证路径

同一个 Agent 可以：

- 提出 Candidate；
- 生成实现；
- 运行测试；
- 解释结果。

这可以提高效率，但会产生 Common-mode Failure。

独立性需要与风险匹配。

候选方式包括：

- Deterministic Check；
- Independent Reviewer；
- Separate Agent Contract；
- Human Review；
- Shadow Comparison；
- External Test Harness；
- Red-team / Counterexample Search；
- Production Guardrail。

低风险参数变化不必强制多 Agent Review。

高影响、可扩权或改变验证机制本身的 Candidate，不应只依赖 Candidate Producer 的 Summary 和自选测试。

Independent Review 也不自动正确；它需要 Source Access、Scope、Authority 和 Conflict Route。

---

# 16.16 Self-Evolution 不能扩大自己的 Authority

Candidate 可能触及：

- Tool Permission；
- Authority Grant；
- Policy Floor；
- Review Independence；
- Evidence Requirement；
- Stop Condition；
- Memory Promotion；
- Skill Instruction Priority；
- Delegation Depth。

这些变化不能因为系统认为“效率更高”而自动生效。

必须区分：

~~~text
propose authority change
evaluate authority change
grant authority change
activate authority change
audit authority use
~~~

执行主体可以在既有 Grant 内提出 Proposal，不能自行批准扩大自身 Grant。

一个自动 Policy Gate 可以拥有窄 Adoption Authority，但不得修改自己的 Decision Target、Threshold、Evidence Source 或 Grant，除非另有明确上级 Authority。

---

# 16.17 Candidate 应与当前运行路径隔离

候选评估可以使用：

## Offline Replay

对保存的 Input、Event 或 Artifact 重放。优点是可重复；局限是不能覆盖新的交互和环境变化。

## Shadow Mode

Candidate 观察真实输入但不拥有真实 Mutation Authority。局限是无法完全模拟闭环行为。

## Sandbox / Isolated Worktree

允许真实变更但限制 Resource、Credential 和外部副作用。

## Canary / Staged Rollout

在小 Scope、特定角色或有限流量中激活。需要清楚的 Exposure、Stop 与恢复条件。

## Parallel Path

Baseline 和 Candidate 同时运行。成本较高，也可能引入 Coordination 与数据一致性问题。

隔离强度与风险相称。

不是每个 Markdown Template 变化都需要 Canary；也不能因为 Shadow PASS 就宣称 Production Safety。

---

# 16.18 Adoption、Activation、Release 与 Improvement 分开

可以出现：

~~~text
Evaluation Evidence accepted
Adoption approved for pilot
Activation limited to one environment
Release blocked
Improvement claim still partial
~~~

也可以出现：

~~~text
Candidate rejected for current scope
some tests retained as useful evidence
forward correction becomes new candidate
~~~

因此状态至少应区分：

| 状态 | 含义 |
|---|---|
| candidate_exists | Candidate Artifact 存在 |
| evaluation_completed | 声明的评估已形成结果 |
| evidence_accepted_for_use | Evidence 可用于具名 Decision |
| adopted_for_scope | Candidate 被接受为某范围当前配置 |
| activated | 已在具名环境实际启用 |
| released | 已获外部或生产使用处置 |
| improvement_supported | 在声明目标和窗口内有 Evidence 支持改进主张 |
| expansion_approved | 可以扩大到新 Scope |

这些状态不是成熟度等级，也不必全部使用。

---

# 16.19 Recovery 不应默认等于 Rollback

Candidate 变化可能：

- 可直接回滚；
- 只能回滚部分 Artifact；
- 需要迁移数据；
- 已产生外部副作用；
- 改变了组织与 Human 习惯；
- 使旧 Baseline 不再安全；
- 只能前向修正。

**Forward Correction（前向修正：不恢复到旧状态，而是在保留已发生历史和约束的基础上形成更小、兼容或风险更低的新 Candidate）** 是独立恢复路径。

Recovery Contract 应说明：

- Reversible Surface；
- Irreversible Surface；
- Baseline Applicability；
- Data / External Side Effect；
- Credential / Permission；
- In-flight Task；
- Memory / Skill / Policy Copy；
- Owner；
- Effect Verification；
- Maximum Recovery Time；
- Evidence Preservation。

Rollback Command 成功不表示所有状态已经恢复。

---

# 16.20 Adoption 之后仍需要 Post-adoption Observation

采用只表示一个有权 Decision 在当时成立。

之后还需要观察：

- Objective 是否持续；
- Guardrail 是否退化；
- 新 Failure Mode；
- Human Rework；
- Detector Health；
- Scope Creep；
- Authority Use；
- Creative Diversity；
- Governance Cost；
- Recovery Readiness；
- Baseline 是否仍可比较。

**Workflow Drift（工作流漂移：实际执行的步骤、配置、角色、Evidence Requirement 或 Authority Boundary 相对已采用 Workflow 发生未评估变化）** 需要绑定实际 Identity。

Drift 可以来自：

- Tool / Model Update；
- Context Selection；
- Hidden Default；
- Manual Workaround；
- Partial Rollout；
- Skill Update；
- Policy Change；
- Environment；
- Human Practice。

发现 Drift 不自动表示回滚。可能需要 Rebaseline、Narrow、Revalidate、Forward-correct 或接受新 Candidate。

---

# 16.21 Production 与 Exploration 应分开，但比例不固定

历史 Evidence 容易奖励：

- 稳定；
- 可预测；
- 高接受率；
- 低失败率；
- 低 Human Intervention。

如果系统只优化这些信号，可能压缩探索、惊喜和新解空间。

因此项目可以分开：

~~~text
Production / Reliability Path
+ Controlled Exploration Path
~~~

二者需要不同：

- Objective；
- Risk Budget；
- Evidence；
- Discard Tolerance；
- Authority；
- Data / User Exposure；
- Review；
- Adoption Gate。

固定 `80% exploitation / 20% exploration` 不进入本章。

**Exploration Budget（探索预算：项目明确允许用于产生、评估和丢弃非当前最优候选的资源、风险与时间边界）** 需要由 Human 或有权 Policy 保护，不能靠 Candidate 自己争取。

探索结果也不能绕过 Production Adoption。

---

# 16.22 治理成本必须进入 Candidate 评价

一个 Workflow 可能减少 Execution Time，却增加：

- Template；
- Gate；
- Manifest；
- Reviewer；
- Waiting；
- State Transition；
- Dashboard；
- Recovery；
- Human Attention；
- Training；
- Maintenance；
- Proof Surface。

候选评价应考虑：

~~~text
execution cost
context cost
governance cost
review and waiting cost
cognitive cost
expected rework
failure and recovery cost
maintenance cost
opportunity cost
~~~

这不是要求计算一个精确总分。

安全、隐私、不可逆损失和明确保留给 Human 的 Decision Type 不能被低平均成本抵消。

如果 Candidate 为证明自身增加的治理对象超过它准备消除的负担，应触发 Process Warning，而不是自动创建下一层证明对象。

---

# 16.23 不同 Evolution Surface 需要不同评估

## Configuration Candidate

关注参数范围、默认值、阶段、回退、Sensitivity 和 Silent Drift。

## Context / Routing Candidate

关注 Retrieval Miss、Stale Context、Authority Injection、Privacy、Token / Attention Cost 和任务结果。

## Skill / Workflow Candidate

关注 Procedure、Tool Compatibility、Evidence、Stop、Recovery、Human Handoff 和重复使用。

## Agent Contract Candidate

关注 Role、Responsibility、Decision Target、Prohibited Action、Escalation、Authority 和与其他 Agent 的冲突。

## Governance / Policy Candidate

关注被保护风险、False Positive、False Negative、Livelock、Bypass、Override Authority 和治理成本。

## Organization Candidate

关注 Coordination、Decision Latency、Handoff Loss、Responsibility Gap、Output Flood 与 Human Cognitive Load。

组织结构的正式设计由第17章展开。本章只规定它也应先成为 Candidate，不能因增加角色数量就宣称系统进化。

---

# 16.24 案例只保留 Candidate、Evaluation 与 Adoption 边界

[v4.94 演化候选案例记录](../Evidence/receipts/ER-20260824-003__CLM-C16-001.md)与[治理活锁和 Function-first 历史记录](../Evidence/receipts/ER-20260818-001__CLM-OUTLINE-002.md)保存来源与限制；完整失败序列见[第23章](第23章_AI_Game_Dev_OS纵向案例_首轮修订稿.md)。

| Episode | 本章使用的关系 | 保留的限制 |
|---|---|---|
| D-073 至 D-075 | Governance / Proof Surface 扩大但 Delivery Evidence 未推进，只能形成 Change Signal 与候选问题 | “Governance Livelock”包含事后判断，不是受控因果证明 |
| D-076 | 窄 Objective、禁止事项、Hard Stop 与 Dual Review 形成可撤回 Pilot；Review 只使 Candidate 可提交 Human 继续裁决 | 没有自动 Adoption，也没有 Throughput、Human Attention 或 Defect Outcome 测量 |
| D-077 | 架构拆分后的两个受限 Attempt 仍以 `SIGABRT/-6` 结束 | Recovery Plan 与 Safety Envelope 不等于有效执行；该失败阻断顺滑成功叙事 |
| D-079 | 42 个 Selected Tests PASS，Human 未接受 Over-scoped Candidate，Forward Correction 保留历史 | Test PASS 不等于 Scope Fit；较小实现的长期成本未知 |
| F1–F4a | Source、Read-only Replay、Package Identity 与 `48/48 PASS` 形成分阶段 Evidence | 结果仍是 `NON_QUALIFYING`，PC-0、Gate 与 Production 未成立 |

这条压缩路径不能证明 Function-first 是恢复的唯一原因，也不能证明该 Workflow 已完成长期 Improvement Evaluation。

---

# 16.25 最小实现从一个重复 Workflow 开始

选择一个：

- 重要但范围清楚；
- 重复发生；
- 可以版本化；
- 有可观察问题；
- 有适用 Baseline 或至少有历史参照；
- 可回滚或有可信 Forward Recovery；
- 评估收益高于双路径维护成本。

建立最小闭环：

1. 记录 Change Signal；
2. 分开 Observable Fact、Judgment、Inference 与 Recommendation；
3. 提出 Learning Candidate；
4. 形成 Change Candidate；
5. 声明 Evolution Surface 与最大 Scope；
6. 检查 Baseline 是否安全、适用且可比；
7. 写 Primary Objective 与少量关键 Guardrail；
8. 声明 Evaluation Contract 和完整性边界；
9. 绑定 Evaluation、Adoption、Activation 和 Recovery Authority；
10. 在隔离、Replay、Shadow 或小 Scope 中评估；
11. 记录 PASS、FAIL、Partial、Unknown 与 `non-result`；
12. 作出 Result Disposition；
13. 决定 Reject、Adopt for Scope 或 Forward-correct；
14. 观察采用后效果；
15. 在预定 Review Point 决定 Keep、Narrow、Expand 或 Revoke。

如果项目不能说明 Candidate 与当前配置的 Identity，也不能在失败时停止传播，就不应先自动化 Self-Evolution。

---

# 16.26 与相邻章节的所有权边界

| 对象 | 所属章节 | 第16章如何使用 |
|---|---|---|
| Work、Execution Contract、Attempt、Checkpoint、Bounded Execution | 第7章 | 为 Self-Evolution Candidate 的试验与激活提供具名执行边界 |
| Attempt Outcome、Target Result、Evaluation Result、Failure、`non-result`、Recovery | 第8章 | 保留评估、干预与恢复结果，不建立平行结果枚举 |
| Review、Review Target、Finding、Review Budget、Review Independence、Review Disposition | 第10章 | 约束 Candidate Review 与 Post-adoption Review，不赋予默认处置权 |
| Memory Candidate、Provenance、Conflict、Expiry | 第15章 | 提供有来源经验与 Lesson Candidate |
| Observation、Detector、Exception、Intervention | 第14章 | 提供 Change Signal 与 Post-adoption Observation |
| Authority Grant、Autonomy Profile、Revocation | 第13章 | 约束 Evaluation、Adoption、Activation 与 Recovery |
| Evidence Use、Acceptance、Adoption、Release Authorization | 第9章 | 决定 Evaluation Result 能支持什么发布授权处置 |
| Change Signal、Learning Candidate、Change Candidate、Evaluation Contract、Activation / Rollout Record、Post-adoption Disposition 特化 | 第16章 | 本章核心对象；基础 Adoption 与 Disposition 仍引用第9章 |
| Agent Role、Handoff、Conflict、Controller / Worker | 第17章 | 定义 Organization Candidate 的实际结构 |
| Release Execution、Release Outcome、Trace | 第18章 | 记录已授权激活或发布是否执行及其后果 |
| Metrics 与 Governance Economics | 第20章 | 提供长期评价方法，不产生单一 Improvement Score |
| Case Narrative | 第23章 | 展开 v4.94 与 SP122 时间序列 |

第16章可以提出 Organization Candidate，但不提前定义所有 Agent 角色。

---

# 16.27 本章原则

1. **Self-Evolution 不等于 Self-authorization。** 系统可以提案和取证，不能自行扩大 Grant。
2. **Change 不等于 Improvement。** Improvement Claim 绑定 Objective、Guardrail、Scope、Environment 与观察窗口。
3. **观察、推导与原因候选分开。** Reflection 不是事实，Failure Result 不是 Root Cause，`non-result` 不是 Target FAIL。
4. **Baseline 与比较有边界。** 先检查安全性、适用性与可比性；不可比时保留不确定性，不制造精确提升率。
5. **Evaluation、Adoption、Activation、Release 与 Expansion 分开。** 高影响 Candidate 的 Producer 不应成为唯一评估者，采用后仍需观察 Drift、Rework 与 Guardrail。
6. **Recovery 与治理成本进入评价。** 不可逆变化需要 Forward Recovery 与 Owner；更多 Gate、Review、Agent 或 Proof Surface 不自动代表改进。

---

# 16.28 常见反模式

- 把 Candidate 产生、Merge、Test / Review PASS 或 Adoption 写成 Improvement；
- 把一次 Failure 变成永久 Rule、把 `non-result` 写成 Target FAIL，或把多因素压成单一 Root Cause；
- 让 Candidate 修改自己的 Detector、Threshold、Authority 或 Protected Floor，或由同一主体完成高影响提案、选证与批准；
- 对失效或不可比 Baseline 计算精确提升率，把 Shadow / Rollback Command 当成生产安全或状态已恢复；
- 用 v4.94 推出 Function-first 普遍最优，把 `48/48 PASS NON_QUALIFYING` 写成完整资格化，或用无对照的前后历史制造效率结论。

---

# 16.29 本章检查清单

## Signal 与 Candidate

- Change Signal 来自什么 Observation、Failure、Review 或 Human Request？
- Observable Fact、Contemporaneous Judgment、Inference 与 Recommendation 是否分开？
- Learning Candidate 的 Source、Counterexample 和 Scope 是否明确？
- Change Candidate 影响哪个 Evolution Surface？

## Baseline 与 Comparability

- Baseline 是否仍安全、适用、可访问和可比较？
- Candidate 与 Baseline 的 Task、Input、Environment、Model、Tool、Context 与 Authority 是否一致？
- 不可比性是否显式保留？
- Recovery 是 Rollback 还是 Forward Correction？

## Objective、Guardrail 与 Evaluation

- Improvement Claim 是否绑定 Objective、Scope、Environment 和 Window？
- Guardrail 是否指出具体被保护风险和 Observation Method？
- Evaluation Result 是否区分 PASS、FAIL、Partial、Unknown 与 `non-result`？
- Candidate Producer 是否控制全部 Source、Test 和 Review？

## Authority 与 Gate

- Candidate Admission、Evaluation、Result、Adoption、Activation、Release 和 Expansion Authority 是否分开？
- Candidate 是否试图改变自己的 Permission、Authority、Detector 或 Policy Floor？
- 自动 Gate 的 Decision Target 和最大 Scope 是否固定？
- Override、Appeal 与 Revocation 路径是否存在？

## Activation 与 Recovery

- Candidate 在 Offline、Shadow、Sandbox、Canary 或 Parallel Path 中怎样隔离？
- 采用是否与实际激活分开记录？
- In-flight、Data、External Side Effect、Memory、Skill 与 Credential 是否进入 Recovery？
- 干预和恢复效果是否重新观察？

## Post-adoption

- Objective、Guardrail、Drift、Rework、Human Attention 与 Creative Diversity 是否继续观察？
- 何时 Keep、Narrow、Expand、Revoke 或 Forward-correct？
- Baseline 是否需要 Rebaseline？
- 是否有 Evidence 支持 Improvement，而不只是 Adoption？

## Cost 与 Scope

- 评估与双路径维护是否值得？
- Governance Artifact 是否超过被保护风险和候选收益？
- 紧急修复、不可逆迁移或低频任务是否被强迫伪装成实验？
- 单项目案例是否被错误推广为通用流程？

---

# 16.30 本章结论

Self-Evolution Engineering 不把系统变化包装成必然进步。

它建立一条更谨慎的链：

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

这条链允许系统主动发现问题、提出候选、生成实现和 Evidence。

它同时保留两个不可跨越的边界：

> **A candidate does not become an improvement by being generated, merged, tested, or adopted.**

> **It becomes supportable only for a named objective, guardrails, scope, environment, authority and observation window.**

中文语义是：

> **候选不会因为被生成、合并、测试或采用就自动成为改进；只有在具名目标、Guardrail、范围、环境、Authority 和观察窗口内，Evidence 才可能支持一个有限的 Improvement Claim。**

下一章将讨论：当多个 Agent 分担 Candidate 产生、评估、Review、Adoption 和运行责任时，怎样设计角色、Authority、Handoff 与冲突路径，而不把“多个 Agent”误写成“形成了组织”。
