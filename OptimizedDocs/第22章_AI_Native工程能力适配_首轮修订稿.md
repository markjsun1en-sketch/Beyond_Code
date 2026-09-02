# 第22章 AI-Native 工程能力适配
## 从六级成熟度阶梯到 Capability Fitness

> 工作稿状态：首轮逻辑修订稿，不替代 [全书大纲](../OringinalDocs/beyond_code_ai_native_software_engineering_outline_zh.md)。
> 回接说明：[RR-035](../RevisedResult/RR-035_第22章AI_Native工程能力适配模型首轮调整计划.md)。
> 适用边界：本章提出 Engineering Capability Profile 与 Capability Fit Review 的候选整合模型；它不声称能力面分类已经完备或最优，不建立组织总分或通用成熟度排名，也不把 Multi-Agent、Persistent Memory、Human Control Plane、Execution Epoch 或 Self-Evolution 设为所有项目的升级目标。AI Game Dev OS v4.94 只提供能力存在、治理活动、验证结果与有权处置需要分离的案例，不证明本模型提高效率、质量、安全或成本表现。

“我们现在处于哪个阶段？”

这个问题很自然。

它可以帮助团队整理现状、解释预算、规划下一项工程投入，也可以让不同组织比较自己
已经建立和仍然缺少的机制。

但只要回答变成：

~~~text
more autonomy
+ more agents
+ more registries
+ more evidence
+ more memory
+ more evolution
= higher maturity
~~~

它就把不同问题压成了同一方向。

AI-native 工程能力并不共享一个天然的“越多越好”单位。

更多 Tool Permission 可能扩大有效行动面，也可能扩大 Blast Radius；更多 Review 可能
增加独立检查，也可能制造等待和 Governance Livelock；更多 Memory 可能改善连续性，
也可能传播陈旧判断和污染；更多 Trace 可能支持重建，也可能增加 Privacy、Retention
和认知成本。

本章把 **Capability Fitness（能力适配性：当前工程能力配置对于具名 Workload、
Intended Use、风险面、恢复要求和成本约束是否足够且不过度）** 作为中心问题。

中心句是：

> **Do not rank mechanisms by accumulation; evaluate whether a bounded capability configuration is fit for a named workload, risk surface, and operating constraint.**

不要按机制累积数量排名，而要判断一个有边界的能力配置，是否适合具名 Workload、
风险面与运行约束。

这不是取消发展路径。

它把发展路径从“升级到更高 Level”改成：

~~~text
identify a bounded need
→ compare required and current capability
→ expose gap, excess and unknown
→ make an authorized disposition
→ observe adoption, outcome, cost and drift
→ re-evaluate
~~~

---

## 22.1 继承最低控制边界，只新增 Capability Fit 问题

第21章已经区分必要、条件性与可选控制。本章继承其中的最低语义：Work / Attempt Identity、Scope / Allowed Effect、具名 Authority、Result / Failure / Unknown / `non-result` 可见性，以及 Stop / Recovery / 可安全丢弃边界。现有 Issue、VCS、Sandbox、CI 与 Human Workflow 可以共同承担这些功能，不要求建立独立 Registry 或成熟度平台。

第22章新增的问题不是“机制是否更多”，而是当前 Capability 对具名 Workload 与 Intended Use 是否适配。必要输入只有当前配置与 Evidence、Gap / Excess / Unknown、风险与成本边界，以及能对具名 Decision Target 作出处置的 Authority。

Engineering Capability Profile、Capability Fit Review 和更完整的 Baseline、Context、Evidence、Handoff、Memory / Evolution、Multi-Agent 或 Re-evaluation 记录都由实际风险触发。Multi-Agent Topology、Persistent Memory、Self-Evolution、Human Control Plane、Execution Epoch、完整 Decision Graph、全量 Trace 与组织级 Score 仍是可选机制，不是成熟终点。

简单不等于不成熟，复杂也不自动等于适配。

---

## 22.2 成熟度阶梯先要说明“什么在被排序”

一个有序 Level 模型如果要承担路线图，至少需要说明：

1. 每一级是否评价同一个对象；
2. 等级之间依据什么共同判据排序；
3. 更高等级是否保留前一级真正必要的边界；
4. 某项能力增加时，为什么其他能力也应该随之增加；
5. 不同 Workload、Scope 和风险面是否仍然可比；
6. 谁依据什么 Evidence 作出 Level 判断；
7. 等级变化会支持什么实际 Decision；
8. 什么时候保持较低复杂度反而是正确选择。

如果这些问题没有答案，Level 更像功能清单或叙事顺序，不是测量模型。

这并不表示所有 Maturity Model 都无用。

对于同一流程、同一对象、同一目的，清楚的分阶段标准可以支持准入、培训或改进。

问题在于：原第22章并没有持续评价同一个对象。

---

## 22.3 原 Level 0–5 在相邻层之间更换评价轴

原大纲的六个 Level 可以拆解为：

| 原 Level | 主要内容 | 实际评价轴 | 隐含但未成立的跳跃 |
|---|---|---|---|
| Level 0：Ad Hoc Assistant | Chat、复制粘贴、无项目记忆 | 使用方式、连续性 | 有记忆自然高于无记忆 |
| Level 1：Supervised Copilot | AI 编码、逐项 Human Review | 协作方式、监督强度 | 逐项 Review 是通向自治的前级 |
| Level 2：Bounded Workflow Agent | Tool Permission、Evidence、Sandbox、Rollback | Authority、验证、恢复 | 有受限执行必然高于 Copilot |
| Level 3：Governed Multi-Agent System | Controller / Worker、Context Registry、Review Agent、Handoff | 组织 Topology、协调 | 多 Agent 自然高于单 Agent |
| Level 4：Cognitive and Evidence-driven Organization | Cognitive Compression、Decision Interface、Observability、Review Budget | Human Control、Evidence、Operations | 这些机制必须作为一个组织层级共同出现 |
| Level 5：Controlled Self-Evolving Organization | Memory、Skill Evolution、跨项目迁移、组织优化 | 学习、采用、演化 | Self-Evolution 是所有组织的终点 |

Level 0 到 Level 1 主要改变协作方式。

Level 1 到 Level 2 改变执行权限和恢复边界。

Level 2 到 Level 3 改变组织结构。

Level 3 到 Level 4 改变 Human Control、Evidence 与运行观察。

Level 4 到 Level 5 改变 Memory、Adoption 与 Evolution。

这些变化没有共同的自然单位，也不是同一个对象的单调增长。

---

## 22.4 六种描述可以在同一项目中同时成立

考虑一个项目的四类 Work：

| Work | 可能采用的配置 |
|---|---|
| 局部代码补全 | Human 使用 Copilot，逐项检查 Diff |
| 依赖更新 | Bounded Agent 在受限目录和 Sandbox 中执行并运行测试 |
| 生产发布 | 单一 Release Agent 配合独立 Human / Security Authority，不使用 Controller / Worker |
| 项目知识维护 | Human 明确 Promotion 到 Project Memory，不允许自动跨项目迁移 |

如果使用原 Level：

- 第一个 Work 像 Level 1；
- 第二个像 Level 2；
- 第三个可能具备 Level 4 的 Evidence 与 Observability，却没有 Level 3 的多 Agent；
- 第四个具备部分 Level 5 Memory 机制，却拒绝 Self-Evolution。

这不是例外。

Capability 是按 Workload、Action、Environment 和 Decision Target 被使用的。

把整个项目压成一个 Level，会丢失真正影响工程决定的差异。

---

## 22.5 原六级模型保留为拆解材料，不保留排名

原六种描述仍有诊断价值。

它们提醒读者注意：

- AI 使用是否仍然是零散对话；
- 人类是否承担逐项 Review；
- Agent 是否获得 Tool 和状态修改能力；
- Work 是否跨 Agent、Role 与 Handoff；
- Human 是否面对认知和 Review Bandwidth 问题；
- Memory、Skill、Policy 与 Workflow 是否可能被改变。

本章保留这些问题，但不再称它们为从低到高的阶段。

也不把六个 Level 改名为六种新的固定 Archetype。

固定 Archetype 仍可能让读者寻找“我是哪一种”，并忽略一个项目内部的混合配置。

更合适的做法是从具名 Workload 出发，投影所需能力。

---

## 22.6 “成熟”如果保留，只能描述有范围的校准能力

本章不再问：

> 这个组织是 Level 几？

如果继续使用“工程成熟性”，本书把它收窄为：

> 在具名 Scope 和观察窗口内，团队能否可重复地识别能力需要，建立不低于保护底线的配置，观察其实际表现，并在失配、成本或 Drift 出现时调整或退出。

这里的关键动作是：

~~~text
identify
configure
bound
observe
decide
revise
retire
~~~

它允许增加能力，也允许：

- 限制过宽 Authority；
- 删除没有 Decision Use 的 Gate；
- 合并重复 Registry；
- 停止无效 Automation；
- 保持已经足够的简单流程；
- 把未知保留为未知；
- 在新用途或环境变化后重新评估。

因此，“成熟”不是 Capability 数量，而是持续进行有边界校准的能力。

这仍然是本书提出的候选定义，不是行业统一定义。

---

## 22.7 适配判断必须先固定 Scope、Workload 与 Intended Use

“系统有没有 Evidence？”

“Agent 能不能自治？”

“Memory 是否完善？”

这些问题都缺少 Scope。

Capability Fitness 至少需要绑定：

- Organization / Project / Repository / Service；
- Work Type 与 Workload Population；
- User、Affected Party 与 Intended Use；
- Action、Data、Tool、Environment 与 External Effect；
- Impact、Reversibility 与 Recovery Time；
- Duration、Concurrency 与 Handoff；
- Decision Target 与 Decision Authority；
- Evaluation Window 与已知 Coverage；
- Policy、Contract、Rights 与 Protected Control Floor；
- 当前时间、版本和触发 Re-evaluation 的条件。

同一机制对不同用途可能得到不同 Finding。

例如，一个 Read-only Retrieval Agent 对内部代码搜索可能适配；如果它被允许把源代码
发送到未经批准的外部处理面，Security、Privacy、Confidentiality 与 Contract Boundary
就改变了。

Capability 名称相同，不表示用途相同。

---

## 22.8 第22章只新增两个候选整合概念

本章新增：

1. Engineering Capability Profile；
2. Capability Fit Review。

它不重新拥有：

- 第4章的 Intent、Scope 与 Acceptance Target；
- 第5–6章的 Context、State、Decision、Assumption 与 Conflict；
- 第7章的 Work、Execution Contract、Attempt、Checkpoint 与 Bounded Execution；
- 第8章的 Attempt Outcome、Target Result、Evaluation Result、Failure、`non-result` 与 Recovery；
- 第9章的 Evidence Use、Decision Target、Acceptance、Adoption 与 Release Authorization；
- 第10章的 Review、Review Target、Finding、Review Budget、Review Independence 与 Review Disposition；
- 第11–12章的 Cognitive Load、Review Bandwidth、Cognitive Compression、Human Decision Interface 与 HCP Projection；
- 第13–14章的 Authority、Autonomy、Observation 与 Intervention；
- 第15–16章的 Memory / Evolution Candidate、Promotion 与 Adoption；
- 第17章的 Role、Assignment、Handoff 与 Integration；
- 第18–19章的 Trace、Security、Privacy、Supply Chain 与 IP Boundary；
- 第20章的 Operational Evaluation、Operational Outcome observation、Operational Baseline、Cost 与 Drift；
- 第21章的 Lifecycle Profile 与 Transition。

Engineering Capability Profile 只投影这些对象的当前配置。

Capability Fit Review 只比较当前配置与具名用途需要，并连接有权处置。

二者都不是新的全局 Truth Store。

---

## 22.9 Engineering Capability Profile 描述当前可观察配置

**Engineering Capability Profile（工程能力配置：对具名 Scope 和时间点，描述当前
实际可用的工程机制、边界、Evidence 与已知缺口的投影）** 回答：

- 当前准备支持什么 Workload 与 Intended Use；
- 哪些能力实际存在；
- 哪些能力进入了真实工作路径；
- Scope、Authority、Failure 与 Recovery 边界是什么；
- 当前 Evidence 和 Observation Coverage 是什么；
- 哪些关系未知、过期、冲突或发生 Drift；
- 运行、等待、Review、维护和认知成本是什么。

一个候选表达：

~~~yaml
profile_ref: local-refactor-profile
profile_at: 2026-08-27

scope:
  repository: example-project
  workload: local_reversible_refactor
  environment: developer_worktree
  intended_use: prepare_change_for_human_review

current_configuration:
  intent_and_scope: short_work_brief
  context_and_state: pinned_head_plus_dirty_state_check
  execution_and_authority: path_limited_write
  evaluation_and_decision: focused_tests_plus_diff_review
  human_control: final_scope_disposition
  recovery: preserve_diff_and_revert_named_change

known_gaps:
  - no_cross_session_handoff

not_needed_for_current_scope:
  - multi_agent_controller
  - persistent_memory
  - self_evolution

re_evaluate_on:
  - production_write_added
  - repository_scope_expanded
  - recovery_path_changes
~~~

这不是通用 Schema。

Profile 可以是一段文字、一张表、一份配置、一次查询投影或已有系统中的组合视图。

---

## 22.10 Profile 记录实际状态，不记录愿望清单

以下句子不能直接进入 Current Profile：

- “计划建立独立 Review”；
- “未来支持 Rollback”；
- “系统应当具有完整 Trace”；
- “Agent 可以自主优化 Workflow”；
- “团队遵循风险治理”。

它们可能表达 Proposal、Desired Outcome 或 Policy Intent，但不是对当前能力的描述。

Current Profile 需要区分：

| 类型 | 示例 |
|---|---|
| Observable Presence | 仓库中存在某配置、Tool 或 Workflow |
| Operational Use | 真实路径在当前 Scope 调用了该机制 |
| Declared Boundary | Policy / Contract 声明允许与禁止什么 |
| Observed Behavior | 运行中实际发生了什么 |
| Evidence Coverage | 当前验证观察了什么、未观察什么 |
| Desired Capability | 计划、目标或候选变化 |
| Unknown | 当前无法确认 Presence、Use、Boundary 或 Outcome |

文件存在不表示机制被使用。

机制被使用不表示边界正确。

文档声明不表示运行遵循。

运行成功一次也不表示长期适配。

---

## 22.11 Profile 必须有时间和版本边界

Capability Profile 不是永久标签。

下列变化可能使它失效：

- Model、Tool、Skill、Prompt 或 Policy 变化；
- Context、Data、Repository 或 Workload 变化；
- Permission、Credential、Authority 或 Action Sink 变化；
- Evaluation、Verifier 或 Observer 变化；
- Human Role、Review Capacity 或组织所有权变化；
- Provider Contract、价格、Retention 或 Rights 变化；
- 新 Incident、Counterevidence 或未知外部结果；
- 原 Recovery、Rollback 或 Sandbox 不再可用。

因此 Profile 应说明：

~~~text
profile scope
+ observed-at / effective period
+ source or baseline references
+ known gaps
+ invalidation / re-evaluation triggers
~~~

Profile 过期不表示过去记录错误。

它表示不能不经检查地把过去配置当成当前状态。

---

## 22.12 Required Capability Boundary 是审查输入，不是最高配置

Capability Fit Review 需要一个比较对象。

本章称之为 Required Capability Boundary：

> 为支持具名 Workload 和 Intended Use，在当前风险、恢复、Policy、成本与 Human
> Decision 条件下，至少需要哪些工程功能和保护边界。

它不是：

- 当前所有最佳实践的并集；
- 全书对象的完整实例；
- 最高自治或最高治理配置；
- 行业通用 Checklist；
- 自动产生 Authority 的规范。

Required Boundary 可以包含：

- 当前用途不可缺少的控制功能；
- Protected Control Floor；
- 可接受的 Unknown 与 Residual Risk；
- 需要的 Evidence 和 Coverage；
- Human Decision、Intervention 与 Takeover；
- Recovery 与 Exit；
- 不需要或明确禁止的机制。

“不需要 Multi-Agent”也可以是 Boundary 的有效结果。

---

## 22.13 Capability Fit Review 比较需要与当前配置

**Capability Fit Review（能力适配审查：针对具名 Workload、Intended Use、风险与成本，
比较所需边界和当前 Profile，并为有权处置提供 Finding 的有范围审查）** 使用以下关系：

~~~text
Workload / Intent / Intended Use
          +
Risk / Impact / Reversibility / Constraints
          ↓
Required Capability Boundary
          ↕ compare
Current Engineering Capability Profile
          +
Observable Evidence / Coverage / Unknown
          ↓
Fitness Finding
          +
Named Capability Use / Configuration Change / Adoption Target
          ↓ authorized Decision Record
Fitness Disposition
          ↓
Maintain / Restrict / Experiment / Strengthen / Replace / Retire / Defer
          ↓
Adoption / Operation / Outcome / Cost / Drift
          ↺
Re-evaluation
~~~

Review Target 与下游 Decision Target 必须分别明确；二者可以引用同一个 Capability Candidate，但回答的问题不同。

例如：

- 是否允许该 Agent 从 Read-only 扩展到 Repository Write；
- 当前 Context 机制是否足以支持跨会话迁移；
- 是否需要引入独立 Reviewer；
- 当前 Trace 是否足以重建 Release Decision；
- 某项 Memory 是否应继续自动检索；
- 某个 Gate 是否应维持、收窄、合并或退出。

Review 不回答“整个组织有多先进”。

---

## 22.14 Finding 与 Disposition 必须分开

**Fitness Finding（适配发现：基于当前 Scope、Profile、Evidence 与已知未知形成的审查
判断）** 是第10章 Finding 的 Target-specific subtype，可能指出：

- 当前配置足够；
- 只在更窄 Scope 内足够；
- 某个必要能力缺失；
- 某项机制相对当前用途过度；
- Evidence 或状态不足，无法判断；
- 不同来源发生冲突。

**Fitness Disposition（适配处置：由具名 Authority 对 Capability Use、Configuration Change
或 Adoption Target 作出的维持、限制、试验、增强、替换、退出或延期决定）** 是第9章 Disposition 的 Target-specific subtype。Decision Record 必须命名该 Decision Target；Fitness Finding 是决定输入，不自动成为被处置对象。

二者不能合并，因为同一个 Finding 可能产生不同处置。

例如，发现缺少可验证 Rollback：

- 可以先补 Rollback；
- 可以把 Scope 收窄为 Read-only；
- 可以改为 Human Execution；
- 可以限制到 Sandbox；
- 可以暂停用途；
- 在低影响、易人工恢复的 Scope 中，也可能记录 Residual Risk 后继续。

Finding 本身不授予动作。

---

## 22.15 Presence、Use、Boundary、Evidence 与 Sustained Fitness 是五种判断

| 判断 | 核心问题 | 不能自动推出 |
|---|---|---|
| Presence | 某机制是否存在 | 它进入真实路径 |
| Operational Use | 机制是否被实际调用 | Scope 与 Authority 正确 |
| Boundary Adequacy | Scope、Authority、Failure 与 Recovery 是否满足当前需要 | 目标结果已经产生 |
| Evidence Adequacy | 当前 Evidence 是否足以支持具名 Decision Target | 长期仍然适配 |
| Sustained Fitness | 在观察窗口中，结果、成本、控制和恢复是否持续适合当前用途 | 跨项目普遍最优 |

常见误推包括：

~~~text
review_agent_present
⇒ review_independent

tests_passed
⇒ acceptance_target_covered

rollback_command_exists
⇒ recovery_verified

memory_active
⇒ memory_current_and_applicable

trace_complete_for_one_system
⇒ decision_reconstructable_end_to_end

self_evolution_pipeline_runs
⇒ adopted_change_improved_the_system
~~~

每个箭头都需要额外 Evidence、Scope 与 Decision。

---

## 22.16 Adoption State 与 Fitness 是两条轴

Experiment、Pilot、Active、Sustained、Restricted 和 Deprecated 可以描述某项机制的
采用状态。

采用状态回答“它处于怎样的组织生命周期”。

Fitness 回答“它是否适合当前具名用途”。

两者可能形成不同组合：

| Adoption State | 可能的 Fitness Finding |
|---|---|
| Experiment | 有希望，但 Evidence 与 Coverage 仍不足 |
| Pilot | 对窄 Scope 适配，对扩大用途未知 |
| Active | 已进入真实路径，但可能存在 Gap 或 Excess |
| Sustained | 过去稳定使用，但可能因 Drift 失配 |
| Restricted | 在限制条件内适配 |
| Deprecated | 当前不再采用，但过去用途不因此被改写为错误 |

未采用某项能力，也可能只是当前 Scope 不需要。

Active 不等于 Fit，Sustained 不等于永远有效，Deprecated 也不等于从未有价值。

---

## 22.17 Capability Fitness 不压成统一总分

将多维能力改成矩阵后，再计算一个总分，看起来比 Level 更精细。

但总分仍然面临：

- Authority、Security、Recovery、Cost 与 Human Judgment 没有共同单位；
- 权重随 Workload、Intended Use 和风险面变化；
- 高 Context 或 Automation 分数不能抵消 Production Write 缺少 Authority；
- 强 Trace 不能抵消 Recovery 不可用；
- 低 Token Cost 不能抵消 Privacy 或 Rights Boundary；
- 平均分会隐藏一个局部但决定性的 Protected Floor 缺口；
- Unknown 容易被错误地填成零或中间值。

本章允许在单一 Decision Target 内使用局部指标。

例如，可以比较：

- 同一 Workload 的 Accepted Outcome Rate；
- 同一 Evaluation Window 的 Human Waiting；
- 同一 Scope 的 Recovery Success；
- 同一 Review Contract 的 Coverage；
- 同一配置变更前后的 Total Production Cost。

这些指标不能自动汇总成组织成熟度。

---

## 22.18 Finding 与 Disposition 使用候选语汇，不建立全书 Enum

Capability Fit Review 可以使用下列候选 Finding：

- `fit_for_scope`：当前 Evidence 足以支持具名 Scope 的适配判断；
- `constrained_fit`：只在更窄 Scope、期限或限制下适配；
- `gap`：所需边界缺失或当前机制不足；
- `excess`：机制相对当前用途产生不相称的成本、等待或复杂度；
- `not_needed_for_scope`：当前具名用途不需要该能力；
- `unknown`：Evidence、Coverage、状态或冲突不足以形成判断。

有权角色可以作出：

- `maintain`；
- `restrict`；
- `experiment`；
- `strengthen`；
- `replace`；
- `retire`；
- `defer`。

Finding 与 Disposition 是两个字段，不是一个状态词。

~~~yaml
decision_target: allow_repository_write_for_local_refactor

fitness_findings:
  execution_scope: fit_for_scope
  recovery: constrained_fit
  cross_session_handoff: not_needed_for_scope
  production_effect: prohibited_by_scope

disposition:
  action: maintain
  constraints:
    - developer_worktree_only
    - no_production_credentials
    - human_diff_disposition_required
  re_evaluate_on:
    - scope_expansion
    - recovery_change
~~~

这些词不是通用标准。

项目可以使用自己的语汇，只要不会把观察、Finding、Decision 和 Action 混为一体。

---

## 22.19 八个 Capability Surface 是审查投影

**Capability Surface（能力面：为了审查方便，把相关工程关系投影到同一问题域的候选
分组）** 不是新的对象层级，也不声称穷尽所有项目。

首轮使用八个能力面：

| Capability Surface | 核心问题 | 主要接口 |
|---|---|---|
| Work and Intent | Need、Intent、Scope、Acceptance Target 与 Non-goal 是否清楚 | 第4、17、21章 |
| Context and State | Baseline、State Claim、Context、Conflict、Gap 与 Freshness 是否可见 | 第5–6章 |
| Execution and Authority | Agent 可执行什么、不能执行什么，怎样暂停、恢复与撤权 | 第7–8、13–14章 |
| Evaluation and Decision | Observation、Evidence、Coverage、Review 与 Decision 是否分离 | 第9–10章 |
| Human Control and Cognition | Human 是否能理解当前 Decision Target，并保留方向、介入与接管权 | 第11–12、14章 |
| Organization and Handoff | Work、Role、Assignment、Handoff、Conflict 与 Integration 怎样连接 | 第17章 |
| Memory, Learning and Evolution | Candidate 怎样形成、Promotion、Adoption、Expiry、Recovery 与退出 | 第15–16章 |
| Operations, Trace, Security and Economics | 运行 Baseline、Drift、Trace、保护边界和总成本怎样观察 | 第18–20章 |

这些 Surface 可以被拆分、合并或只选择其中一部分。

受监管生产系统可能把 Security、Privacy、IP 与 Trace 各自展开；局部只读工具可能只需
检查 Work、Context、Evaluation 和 Human Decision。

回答“已覆盖”的 Surface 数量不产生分数。

---

## 22.20 Work and Intent Surface 先检查问题是否值得被执行

这个 Surface 关注：

- Need 与 Trigger 来自哪里；
- Intent Owner 和 Affected Party 是谁；
- Scope、Non-goal、Constraint 与 Priority 是否清楚；
- Acceptance Target 是否能被评价；
- Open Question 与多方 Intent Conflict 是否可见；
- Work 是否被正确拆分；
- 谁可以改变目标、取消工作或接受结果。

候选 Fit 问题：

- 当前 Agent Input 是否表达了真实 Intent，而不只是最后一句 Prompt；
- Work 是否在目标仍冲突时被过早打开；
- 局部 Acceptance 是否被误写成 Product Success；
- Scope 是否能够与 Tool、Permission 和 Evaluation 对齐；
- Human 是否仍保留价值、体验、审美与 Trade-off 裁决。

常见 Gap：

- 目标只存在于对话中；
- Non-goal 缺失；
- Acceptance Target 无法判断；
- 多方 Intent 被压成单一 Priority；
- Work 完成标准与 Release 标准混在一起。

常见 Excess：

- 为一个局部可逆修改建立完整需求治理委员会；
- 每次轻量探索都要求提前冻结全部 Acceptance；
- 为创意方向使用自动 Score 代替 Human Judgment；
- 将 Intent 反复改写成多个同步 Registry，却没有具名 Decision Use。

---

## 22.21 Context and State Surface 检查当前依据，不承诺完整世界

这个 Surface 关注：

- 当前 State Source、Revision、Environment 与 Dirty State；
- Decision、Assumption、Conflict、Unknown 与 Freshness；
- Context Contract、Pack、Manifest 与 Access；
- Initial Selection 与 Progressive Retrieval；
- Provenance、Compression、Loss 与 Drill-down；
- Saved Baseline 和 Current Observation 的差异；
- 缺失或冲突时怎样 Retrieve、Narrow、Rebase 或 Hold。

候选 Fit 问题：

- 当前 Work 是否能定位自己依据的 Baseline；
- Context 是否包含必要来源，也允许执行中发现新依赖；
- 过期、冲突和未知是否被显式保存；
- Agent 是否只能访问当前授权的信息表面；
- Context Manifest 是否只描述“提供了什么”，而没有伪装成 Truth 或 Safety 证明。

常见 Gap：

- 只保存对话摘要，不保存版本引用；
- 把 Working Tree 当成 Clean Baseline；
- Context 缺失时继续猜测；
- Compression 后无法下钻；
- State Conflict 被最后写入覆盖。

常见 Excess：

- 把整个仓库、全部历史和所有文档一次性注入；
- 为每次局部任务创建全量 Snapshot；
- 用更多 Context 掩盖 Intent 或 State 不清；
- 把 Retrieval、Memory 与 Truth 复制成多个平行系统。

---

## 22.22 Execution and Authority Surface 检查可行动边界

这个 Surface 关注：

- Capability、Permission、Authority Grant 与 Responsibility；
- Tool、Credential、Data、Action Sink 与 Environment；
- Execution Contract、Attempt、Checkpoint 与 Handoff；
- Supervision、Pause、Restrict、Revoke 与 Takeover；
- External Effect、Blast Radius 与 Reversibility；
- Failure、Timeout、Unknown External Result 与 `non-result`；
- Sandbox、Fallback、Rollback、Recovery 与安全退出。

候选 Fit 问题：

- Agent 是否只在已授予的 Scope 内执行；
- 新 Tool 或 Action 是否错误继承旧 Authority；
- 执行者是否可以自行扩大 Grant 或降低 Protected Floor；
- 失败后是否知道停止什么、保存什么、恢复什么；
- Authority 撤销后，在途 Tool、下游 Agent 和 Credential 如何处理。

常见 Gap：

- Tool 可用被当成 Permission 已授予；
- Permission 被当成 Acceptance Authority；
- 只有成功路径，没有 Unknown 与 Recovery；
- Sandbox 名称存在，但 Side Effect 仍可离开边界；
- Rollback 命令没有目标 Baseline 和验证。

常见 Excess：

- 对 Read-only 分析要求生产级 Release Gate；
- 每个局部 Attempt 都要求多方批准；
- 为可逆开发动作使用资格期身份完备性作为入口；
- 把所有 Human Review 都变成逐 Tool Call 点击。

---

## 22.23 Evaluation and Decision Surface 检查证据用途

这个 Surface 关注：

- Observation、Evidence Generation 与 Verifier Integrity；
- Claim、Scope、Baseline 与 Intended Use；
- Validation、Evaluation、Review 与 Counterevidence；
- Coverage、Known Gap 与 `non-result`；
- Finding、Acknowledgment、Approval 与 Decision；
- Acceptance、Adoption、Integration、Release 与 Qualification；
- Decision Authority、Disposition、Expiry 与 Re-evaluation。

候选 Fit 问题：

- Evidence 是否观察了当前 Claim 的 Subject；
- Test PASS 具体覆盖什么；
- Verifier Failure、Target Failure 与 Target `non-result` 是否分开；
- Review 是否具有所需独立性；
- Automated Gate 是否只作出 Grant 内的窄处置；
- Evidence 是否足以支持当前 Decision，而非另一个更窄判断。

常见 Gap：

- Completion 声明代替 Evidence；
- Test Count 代替 Coverage；
- Review Comment 被当成 Decision；
- Human Acknowledgment 被当成 Acceptance；
- 开发验证被当成 Production Qualification。

常见 Excess：

- 为不相关 Claim 反复增加测试；
- Reviewer 只扩大 Proof Surface，却不能指出当前 Decision Use；
- 所有 Evidence 被统一排成 Weak / Medium / Strong；
- 对低影响 Work 要求全量独立 Review，却没有增加可用信息。

---

## 22.24 Human Control and Cognition Surface 检查可判断性

这个 Surface 关注：

- 当前需要 Human 判断的 Decision Target；
- Information Volume、Decision Complexity 与 Review Bandwidth；
- Progressive Disclosure、Brief、Drill-down 与 Conflict Visibility；
- Direction、Experience、Aesthetics、Ethics 与 Rights Judgment；
- Override、Intervention、Takeover 与 Stop Authority；
- Attention Allocation、Waiting、Alert 与 Escalation；
- Human 决定如何被保存、重开和质疑。

候选 Fit 问题：

- Human 看到的是当前决定所需的信息，还是 Agent 活动流水；
- 摘要是否保留 Scope、Evidence、Conflict、Unknown 与不可逆影响；
- Human 是否能够下钻到来源；
- Review Queue 是否超过有资格人员的处理能力；
- Agent 是否把 Recommendation 呈现成已经决定；
- Human 保留的不是“点击动作”，而是真实方向与责任。

常见 Gap：

- Dashboard 只有数量和状态颜色，没有 Decision Target；
- 摘要删除 Material Conflict；
- Human 只能 Approve / Reject，不能 Narrow、Hold、Request Evidence 或 Takeover；
- Alert 没有 Owner 与 Response Path；
- 创意与体验判断被自动指标替代。

常见 Excess：

- 把所有 Tool Event 推给 Human；
- 每个低风险动作都要求同步关注；
- 为了“人在环中”增加无信息审批；
- 同一 Finding 在多个界面重复等待。

---

## 22.25 Organization and Handoff Surface 检查协作关系，不数 Agent

这个 Surface 关注：

- Work、Role Contract、Assignment 与 Authority；
- Decomposition、Dependency、Concurrency 与 Integration；
- Handoff Package、Open Item、Baseline 与 Receipt；
- Controller、Worker、Reviewer 与 Human Role；
- Conflict、Escalation、Reassignment 与 Cancellation；
- 独立性、共享 Context 与信息泄漏；
- Coordination、Waiting、Rework 与 Integration Cost。

候选 Fit 问题：

- Work 是否真的可分解；
- 多 Agent 是否带来并行性、专业边界或 Review Independence；
- 每个 Assignment 是否有 Scope、Input、Output 与 Authority；
- Handoff 是否保存未完成项和未知；
- Controller 是协调 Role，还是无边界超级 Authority；
- Integration Owner 是否能够处理冲突和组合结果。

常见 Gap：

- 只有角色名称，没有 Role Contract；
- 多个 Agent 同时写同一 Surface；
- Reviewer 依赖被审对象的同一不完整 Context；
- Handoff 只说 `done`；
- Conflict 没有 Resolution Authority。

常见 Excess：

- 把一个不可分解任务机械拆成多个 Agent；
- 为简单顺序工作建立 Controller / Worker 层；
- 增加 Reviewer 数量但没有独立 Decision Target；
- Agent 之间反复同步，超过实际执行成本。

---

## 22.26 Memory, Learning and Evolution Surface 检查行为变化边界

这个 Surface 关注：

- Experience、Observation、Failure 与 Candidate；
- Provenance、Scope、Applicability、Conflict 与 Expiry；
- Promotion、Storage、Retrieval、Use 与 Behavior Effect；
- Change Candidate、Evaluation Contract 与 Comparison Baseline；
- Adoption、Activation、Release 与 Post-adoption Observation；
- Rollback、Forward Recovery、Revocation 与 Retirement；
- 跨会话、跨项目和跨组织传播。

候选 Fit 问题：

- 工作完成后是否只产生 Candidate；
- 谁可以把 Candidate 提升到哪一层 Memory；
- Retrieval 是否说明当前适用性；
- “被检索”是否与“影响行为”分开；
- 自我修改是否经过独立 Adoption；
- 采用后是否观察 Outcome、Guardrail、Cost 与 Drift。

常见 Gap：

- CLOSED 自动写入 Memory；
- Failure Retrospective 被当成已知 Root Cause；
- 旧项目经验跨项目传播却没有 Scope；
- Candidate 直接修改当前 Skill 或 Policy；
- Adoption 后没有恢复和退出路径。

常见 Excess：

- 所有会话都永久保存；
- 每次反馈都生成新 Skill；
- 为很少重复的 Work 建立复杂 Evolution Pipeline；
- 自动 Memory 注入扩大 Context 和 Prompt Injection Surface；
- 把变化频率当成学习速度。

---

## 22.27 Operations, Trace, Security and Economics Surface 检查持续适用性

这个 Surface 关注：

- Operational Baseline、Workload、Evaluation Window 与 Outcome；
- Metric Contract、Cost Attribution 与 Human Attention；
- Identity、Action、Context、Decision 与 Evidence Trace；
- Security、Privacy、Confidentiality、Supply Chain 与 IP Boundary；
- Model、Tool、Permission、Evaluation、Economic 与 Contract Drift；
- Incident、Re-evaluation、Fallback、Rollback、Suspend 与 Retire；
- Retention、Access、Deletion 与 Reconstruction。

候选 Fit 问题：

- 当前运行配置是否可识别；
- Outcome 是否与 Tool Call、Artifact 和 Agent 声明分开；
- Trace 是否服务于具体 Decision、Reconstruction 或 Accountability；
- Data、Model Processing、Tool、Dependency 与 Rights Boundary 是否明确；
- Token、Human、Coordination、Failure、Governance 与 Maintenance Cost 是否进入比较；
- Drift 是否相对于具名 Baseline，并触发有范围 Re-evaluation。

常见 Gap：

- 只有调用量，没有 Accepted Outcome；
- 只有平均数，没有 Workload、分母和 Coverage；
- Trace 无法连接 Authority 与 Decision；
- Secret、Personal Data 或受保护材料进入普通 Prompt / Log；
- Provider、Model 或 Permission 变化后仍沿用旧判断。

常见 Excess：

- 永久保存全部 Prompt 与 Tool Payload；
- 为没有下游 Decision Use 的指标建 Dashboard；
- 把所有风险货币化成一个伪精确分数；
- 所有 Drift 都触发完整回归；
- 为降低成本删除法定、合同要求或明确保留给 Human 的 Decision Type。

---

## 22.28 Capability Surface 不是正交分区

八个 Surface 会相互影响。

例如：

~~~text
Intent changes
→ Scope and Acceptance Target change
→ Context and State requirements change
→ Authority and Evaluation need re-binding
→ Lifecycle path and Operational Baseline may change
~~~

Memory Promotion 同时涉及：

- Context and State 的来源与适用性；
- Evaluation and Decision 的 Promotion Evidence；
- Human Control 的裁决权；
- Security and Privacy 的 Retention；
- Operations 的 Drift 与 Expiry。

多 Agent Handoff 同时涉及：

- Work Decomposition；
- Context Projection；
- Authority；
- Trace；
- Integration；
- Human Review Capacity。

因此 Surface 是阅读和审查视图，不是强制系统边界。

本章不创建八个 Registry，也不要求每项机制只属于一个 Surface。

---

## 22.29 每个能力面使用同一组检查问题

无论审查哪个 Surface，都可以先问：

1. Purpose：为什么当前 Workload 需要它；
2. Scope：适用于什么 Action、Data、Environment 与 Population；
3. Mechanism：当前由哪个可观察机制承担；
4. Authority：谁可以使用、配置、Override、暂停或撤销；
5. Evidence：什么支持“机制存在”和“机制适合当前用途”；
6. Coverage：Evidence 实际观察了什么、未观察什么；
7. Failure：失败、未知、冲突、超时和误报怎样呈现；
8. Recovery：怎样隔离、回滚、接管、重新授权或退出；
9. Ownership：谁负责维护和最终处置；
10. Economics：运行、等待、Review、维护、认知和机会成本是什么；
11. Drift：什么变化会使当前配置失效；
12. Re-evaluation：何时、由谁、基于什么重新审查。

这是一组语义检查。

它不要求每个 Surface 创建十二个字段、十二个 Gate 或十二份文件。

一个短 Profile 可以把多个答案压缩在同一段中，只要 Material Boundary 没有消失。

---

## 22.30 Protected Control Floor 不能被平均分抵消

不同 Workload 可以选择不同 Capability Profile。

但某些边界在具名 Scope 内不能由普通执行者自行取消。

候选 Protected Control Floor 可能包括：

- Secret 不进入普通 Prompt、Context 或 Log；
- Production Write 绑定 Identity、Scope 与 Authority；
- 不伪造 Target Result，`non-result` 保持可见；
- 不把开发验证写成 Qualification；
- 不让执行 Agent扩大自己的 Permission 或 Grant；
- Personal Data、Confidential Material 与 IP Rights 按适用边界处理；
- Human 对指定方向、例外、接管和必须由 Human Judgment 完成的 Decision Type 保留裁决权；
- 不可逆或高影响动作具有明确停止与恢复路径。

一个 Profile 在七个 Surface 上表现充分，也不能抵消第八个 Surface 的 Floor 缺口。

同样，Protected Floor 不是全书统一清单。

它来自具名 Policy、合同、法定要求、风险处置和有权 Human Decision。

---

## 22.31 Capability Gap 与 Capability Excess 需要对称检查

传统成熟度模型通常只问“还缺少什么”。

AI-native 工程还需要问“什么已经过度”。

### Capability Gap

可能包括：

- State / Baseline 不可定位；
- Authority 与 Permission 不清；
- Evaluation 不覆盖 Decision Target；
- Human 无法介入或接管；
- Recovery 不可用；
- Memory 没有来源、范围或过期；
- Trace 无法重建 Material Decision；
- Drift 后没有 Re-evaluation。

### Capability Excess

可能包括：

- Context 多到淹没相关信息；
- Gate 多到形成等待和 Governance Livelock；
- Test 增加但 Acceptance Coverage 没有增加；
- Reviewer 增加但没有独立性或 Decision Use；
- Multi-Agent Handoff 成本高于并行收益；
- Trace 精度超过 Reconstruction 需要，却增加 Privacy 与 Retention Cost；
- Memory 自动注入扩大陈旧信息和攻击面；
- Dashboard 展示更多 Activity，却没有减少 Decision Uncertainty；
- Evolution Pipeline 频繁产生 Candidate，却缺少稳定 Adoption 和退出。

Gap 不自动要求增加 Automation。

可能的处置还包括收窄 Scope、降低 Delegation、改回人工路径或停止当前用途。

Excess 也不自动要求删除控制。

必须先确认它是否承担 Protected Floor、法定、合同或不可替代的 Recovery 功能。

---

## 22.32 Governance Economics 比较增量价值和总生产成本

Capability Fit 不能只比较功能。

需要观察：

- Direct Model / Tool Cost；
- Context Assembly 与 Retrieval Cost；
- Validation、Review 与 Decision Cost；
- Human Waiting 与 Attention Cost；
- Coordination、Handoff 与 Integration Cost；
- Failure、Rework、Rollback 与 Incident Cost；
- Governance、Trace、Retention 与 Compliance Cost；
- Maintenance、Drift、Migration 与 Exit Cost；
- 未被保护的风险与不可货币化 Guardrail。

候选比较可以表示为：

~~~text
incremental control or production value
versus
incremental total production cost
+ new failure surface
+ residual uncertainty
+ protected floor constraints
~~~

这不是要求把所有价值和风险换成货币。

有些边界应保持为 Guardrail；有些成本只能给出区间或定性判断。

“治理更少”不是目标。

“治理更多”也不是目标。

目标是在不降低 Protected Floor 的前提下，使控制与当前 Decision Use 相称。

---

## 22.33 固定迁移顺序把依赖关系误写成组织阶段

原大纲建议：

~~~text
Truth
→ Context
→ Evidence
→ Governance
→ Cognition
→ Memory
→ Evolution
~~~

这条序列可以提醒团队不要在基础边界缺失时直接追求 Self-Evolution。

但它不能成为统一 Roadmap。

原因包括：

- Context Selection 与 State Grounding 会反复迭代；
- Evidence 既可能在执行前形成，也可能来自执行与运行；
- Governance 不是 Evidence 之后才出现，它先约束 Action 和 Evidence Generation；
- Human Cognition 不是后期能力，Intent 与风险判断从开始就存在；
- Memory 对某些跨会话 Work 很早就重要，对另一些项目始终可选；
- Evolution 不是终点，而是需要独立 Evaluation、Adoption 与 Recovery 的 Change Surface；
- 一个组织可以先解决某个局部 Security Gap，而不建设完整 Context Platform。

因此本章保留条件依赖，撤销固定先后。

---

## 22.34 Need-driven Dependency 说明“没有什么就不能安全做什么”

条件依赖比 Level 更接近工程决定：

### Delegated Side Effect

Delegated Side Effect 的最低依赖不等于完整对象栈：

~~~text
Work / Attempt Identity
+ Scope and Allowed Effects
+ Named Human / System Authority
+ Observable Result / Failure / Unknown / non-result
+ Stop / Recovery / Boundary for safely discarding this Attempt
~~~

Baseline 深度、正式 Context / Assumption / Conflict Record、Evidence Plan / Decision Target、Exception Authority、
独立 Intervention 与 Re-evaluation Case，由持续时间、并发、影响、不确定性、Policy / 合同 / Rights、下游处置和恢复要求等因素条件触发。

### Persistent Memory

只要信息可能跨会话影响未来行为，就依赖：

~~~text
Provenance
+ Scope and Applicability
+ Promotion Authority
+ Conflict and Expiry
+ Retrieval / Use Visibility
+ Revocation or Retirement
~~~

### Self-Evolution

只要系统可能修改 Skill、Policy、Workflow 或组织结构，就依赖：

~~~text
Bounded Change Candidate
+ Comparison Baseline
+ Evaluation and Counterevidence
+ Independent Adoption Authority
+ Activation Boundary
+ Post-adoption Observation
+ Recovery and Exit
~~~

### Multi-Agent

多 Agent 只有在至少一个条件成立时才有明确理由：

- Work 可分解并能独立推进；
- 并行收益大于协调与集成成本；
- 专业 Boundary 需要分离；
- Review Independence 需要不同角色或信息面；
- Tool、Data 或 Authority 必须隔离。

### Human Decision Interface

它由 Decision Complexity、Information Volume、Review Bandwidth、Risk、Intervention 与
Takeover 需要触发，而不是由“进入 Level 4”触发。

这些依赖说明最低前提，不说明所有组织必须采用相同实现。

---

## 22.35 能力变化沿 Candidate、Evaluation、Disposition 与运行观察循环

发现 Gap 或 Excess 后，不应直接修改生产配置。

候选变化沿用第16、20和21章的边界：

~~~text
Observed Need / Failure / Cost / Drift
                ↓
Capability Gap or Excess Hypothesis
                ↓
Bounded Change Candidate
                ↓
Evaluation + Counterevidence + Coverage
                ↓
Authorized Disposition
                ↓
Adopt / Restrict / Replace / Retire / Defer
                ↓
Operation + Outcome + Cost + Drift
                ↺
Re-evaluation
~~~

候选变化可能是：

- 新增 Context Manifest；
- 收窄 Tool Permission；
- 引入独立 Reviewer；
- 合并两个重复 Gate；
- 暂停自动 Memory Retrieval；
- 改为单 Agent；
- 增加 Recovery Check；
- 退出某个 Model / Provider；
- 取消 Self-Evolution，回到显式 Human Adoption。

Capability Calibration 不是只向“更多”移动。

---

## 22.36 局部、可逆、易观察的代码修改

假设 Work 是开发 Worktree 中的局部 Refactor：

- 不接触 Production；
- 影响路径明确；
- 可以保存 Diff；
- 有 Focused Test；
- Human 可以检查范围并接受或拒绝。

一个可能适配的 Profile：

~~~text
short Intent / Scope / Acceptance Target
+ pinned repository and dirty-state observation
+ path-limited write
+ one bounded Attempt
+ focused validation and diff review
+ Human scope disposition
+ preserve / revert named change
~~~

它可能不需要：

- Multi-Agent；
- Persistent Memory；
- Execution Epoch；
- 独立 HCP Dashboard；
- 全量 Trace；
- 自动 Self-Evolution；
- 十个 Gate。

这不是“停留在 Level 1”。

它是对当前 Workload 保持较低复杂度的候选 Fit。

如果 Scope 扩大到跨仓库或 Production，Profile 需要重新审查。

---

## 22.37 跨会话、跨仓库的迁移

假设 Work 跨多个仓库、持续数周，并由不同角色接续。

可能需要：

- 版本化 Intent、Dependency Boundary 与 Non-goal；
- 每个仓库的 Baseline、Dirty State 与目标版本；
- Context Manifest 与 Known Gap；
- Execution Contract、Attempt / Handoff Identity；
- Checkpoint、Rebase、Conflict 与 Integration Disposition；
- Evaluation Plan、Coverage 与 `non-result`；
- Recovery、Partial Adoption 与 Roll-forward；
- Owner、Expiry 与 Re-evaluation。

是否使用 Multi-Agent，取决于：

- 仓库之间能否独立工作；
- 共享 Schema 与接口如何协调；
- 并行写入是否增加冲突；
- Reviewer 是否需要独立 Context；
- Integration Owner 是否有足够带宽。

Execution Epoch 也只是可选 Correlation Boundary。

长任务并不自动要求多 Agent，跨会话也不自动要求 Self-Evolution。

---

## 22.38 高影响、难恢复或受保护数据相关的变更

假设 Work 会改变生产数据、处理受保护信息，或产生难以撤回的外部影响。

可能需要：

~~~text
affected-party and Intended Use boundary
+ named Data / Tool / Environment / Rights scope
+ independent Security / Privacy / Release Decision Target
+ Protected Control Floor
+ stronger State Observation and Verifier Integrity
+ staged Execution and limited population
+ independent Review where required
+ external-effect observation
+ Incident, Recovery and Re-evaluation path
~~~

机制较多是风险与责任条件的结果，不是项目等级更高。

高影响也不自动要求多个 Agent。

一个边界清楚、Authority 分离的单执行主体，可能比复杂 Agent Organization 更容易观察和
恢复。

本章不能判断具体法律义务；适用法域、合同与专业意见必须单独确认。

---

## 22.39 案例只保留反单轴约束

完整 Case Spine 见[第23章](第23章_AI_Game_Dev_OS纵向案例_首轮修订稿.md)；本章只保留 Capability Fit 的三条反例。

| Episode | 反单轴关系 | 不能说明 |
|---|---|---|
| D-073 至 D-075 | Governance Mechanism Presence / Activity 不等于 Delivery Outcome 或 Capability Fitness | 严格治理普遍无效，或 Function-first 是唯一恢复路径 |
| D-079 | Selected Tests PASS 不等于 Scope Acceptance、Adoption 或 Sustained Fitness | 较小实现长期质量或成本更优 |
| F1–F4a | Source、Replay、Package Identity 与 `48/48 PASS` 可以支持有范围 Development Closure；结果仍是 `NON_QUALIFYING` | Intended-use Qualification、Gate、Production 或更高项目等级已经成立 |

来源与限制见[治理活锁与 Function-first 历史记录](../Evidence/receipts/ER-20260818-001__CLM-OUTLINE-002.md)和[D-079 范围裁决记录](../Evidence/receipts/ER-20260818-003__CLM-C09-001.md)。这些共享案例只约束状态、Evidence Use 与有权判断的分离，不证明本章候选模型的效果。

---

## 22.40 不给 AI Game Dev OS 打分

第23章可以使用 Engineering Capability Profile，但应绑定具名历史切片或未来
Decision Target。

例如可以问：

| Capability Surface | v4.94 历史切片可问的问题 |
|---|---|
| Work and Intent | Function-first Scope 与 Qualification Scope 是否分开 |
| Context and State | Source Baseline、Package Identity 与当前差异怎样保存 |
| Execution and Authority | Confined Execution、Verifier 与 Target Authority 怎样分开 |
| Evaluation and Decision | PASS、`non-result`、Acceptance 与 `NON_QUALIFYING` 怎样处置 |
| Human Control | Human 为什么拒绝 Over-scoped Candidate |
| Organization and Handoff | Governance、Review 与 Development Work 怎样连接 |
| Memory and Evolution | CLOSED 经验是否经过显式 Promotion |
| Operations and Economics | Governance Activity、Waiting、Rework 与 Delivery Outcome 怎样分开 |

这些问题可以形成局部 Case Profile。

它们不能产生：

- “AI Game Dev OS 当前为 Level 3.5”；
- “系统应优先建设 Level 4 或 Level 5”；
- “下一项功能必须是 HCP、Memory、Multi-Agent 或 Evolution”；
- “已有机制已经提高生产率、质量或安全”。

是否改变 AI Game Dev OS，应从一个具名问题、当前版本和正式 Decision Target 重新开始，
而不是从书中的等级表反推功能 Roadmap。

---

## 22.41 最小实现从一个真实决定开始

不要先建立组织级 Capability Platform。

选择一个同时满足以下条件的问题：

- 当前需要作出真实决定；
- Scope 与 Workload 可以限定；
- 当前机制和 Evidence 可以观察；
- Gap、Excess 或 Unknown 已经造成实际困惑；
- 有具名 Owner 与 Decision Authority；
- 决定可以在一段时间后重新评价。

最小步骤：

1. 写明 Decision Target；
2. 绑定 Workload、Intended Use、Scope、Baseline 与时间；
3. 声明 Required Capability Boundary；
4. 只投影与当前决定有关的 Profile；
5. 分开 Presence、Use、Boundary、Evidence 与 Unknown；
6. 形成 Fitness Finding；
7. 由有权角色作出 Disposition；
8. 保存 Constraint、Expiry、Recovery 与 Re-evaluation Trigger；
9. 在采用后观察 Outcome、Cost、Control 与 Drift；
10. 保留退出、替换和维持简单方案的可能。

一页候选模板：

~~~yaml
decision_target:
scope:
workload:
intended_use:
profile_at:

required_boundary:
current_mechanisms:
operational_use:
evidence_and_coverage:
known_failure_and_recovery:
protected_floor:
cost_boundary:
unknown_and_conflict:

fitness_findings:
authorized_disposition:
constraints:
owner:
expires_or_re_evaluate_on:
~~~

模板服务于决定。

没有真实 Decision Use 时，不要为了完整性填表。

---

## 22.42 与相邻章节的接口

第22.8节已经列出完整对象所有权；这里仅保留递进关系。第3–21章提供 AI-native 触发条件，以及 Intent、Context / State、Execution / Result、Evidence / Review、Authority / Observation、Memory / Evolution、Organization / Trace、Security / IP、Operations 与 Lifecycle 的现有配置。

第22章只把这些输入投影成 Engineering Capability Profile，并通过第10章的 Finding 与第9章的 Decision Target / Disposition 形成 Capability Fit Review。它不创建新的 Truth、统一总分、可靠性证明、法律结论或默认 Authority。

第23章只用具名时间序列暴露 Profile 的适用范围、限制与 Transfer Question，不给 AI Game Dev OS 排名，也不把案例重复出现当成独立验证。

---

## 22.43 本章原则

1. **Fit for named use, not rank for the whole organization.** 为具名用途判断适配，不给整个组织排名。
2. **Profile describes; it does not authorize.** Profile 描述当前配置，不产生 Authority。
3. **Presence is not operational use.** 机制存在不表示进入真实路径。
4. **Use is not boundary adequacy.** 机制被调用不表示 Scope、Authority、Failure 与 Recovery 足够。
5. **Evidence is decision-specific.** Evidence 只支持与 Claim、Scope 和 Intended Use 对齐的决定。
6. **Finding is not disposition.** 审查判断不自动产生动作。
7. **Adoption is not fitness.** 已采用不表示适配，未采用不表示落后。
8. **Gap and excess are symmetric review targets.** 不足与过度都可能造成工程失配。
9. **Protected floors are not averaged away.** 保护底线不能被其他能力的高分抵消。
10. **Dependencies replace universal stages.** 说明某种动作依赖什么，不要求所有组织逐级迁移。
11. **Calibration can add, restrict, simplify or retire.** 校准可以增加、限制、简化或退出机制。
12. **Re-evaluate under drift.** 新用途、版本、环境、风险和成本变化会重开适配判断。

---

## 22.44 常见 Anti-pattern

### Feature-count Maturity

按 Agent、Registry、Gate、Memory、Trace 和 Automation 数量排名。

### Whole-project Level

忽略不同 Workload、Action 和 Environment，把整个项目压成一个等级。

### Score Washing

把 Authority、Security、Cost、Human Judgment 与 Recovery 加权成没有自然依据的总分。

### Adoption Equals Fit

把 Active、Sustained 或广泛使用当成有效性证明。

### Tool Presence Equals Capability

因为安装了 Tool、模型或插件，就声明工程能力已经形成。

### Documentation Equals Operation

因为存在 Policy、Workflow 或 Runbook，就声明真实路径遵循。

### Higher Autonomy Bias

把更少 Human 介入当成默认进步。

### Multi-Agent Prestige

为了看起来先进，把不可分解 Work 拆成多个 Agent。

### Memory Accumulation

把保存更多历史当成学习，把自动注入当成适用。

### Evolution as Destination

把能够修改 Skill、Policy 或 Workflow 当成组织最高阶段。

### Governance Monotonicity

认为治理只能增加，删除 Gate 或收窄 Trace 一定是退步。

### Efficiency-only Simplification

为了降低等待或成本，删除 Protected Floor、Rights Boundary 或明确保留给 Human 的 Decision Type。

### Case-to-Rank Generalization

用一个项目的一段历史给整个组织或行业打等级。

---

## 22.45 检查清单

### Decision 与 Scope

- [ ] 当前 Review 是否服务于具名 Decision Target？
- [ ] Workload、Intended Use、Action、Data、Environment 与 Population 是否明确？
- [ ] Profile 是否绑定时间、版本、Baseline 和已知失效条件？
- [ ] 是否避免给整个项目或组织打一个总 Level？

### Required Boundary

- [ ] 当前用途真正需要哪些控制功能？
- [ ] 哪些机制不需要或应被禁止？
- [ ] Protected Control Floor 来自谁、适用于什么 Scope？
- [ ] Residual Risk、Unknown 与 Human 保留裁决权是否保留，并映射到具名 Authority Grant 或制度边界？

### Current Profile

- [ ] Observable Presence、Operational Use 与 Desired Capability 是否分开？
- [ ] Policy 声明与 Observed Behavior 是否分开？
- [ ] Source、Revision、Environment 与 Dirty State 是否可定位？
- [ ] Profile 是否只是投影，而非新的 Truth、Authority 或 Acceptance Source？

### Fit Review

- [ ] Presence、Use、Boundary、Evidence 与 Sustained Fitness 是否分别判断？
- [ ] Finding 是否绑定 Evidence、Coverage、Counterevidence 与 Unknown？
- [ ] Finding 与 Authorized Disposition 是否分开？
- [ ] Disposition 是否包含 Constraint、Owner、Expiry、Recovery 与 Re-evaluation？

### Capability Surface

- [ ] Work / Intent 是否可被评价？
- [ ] Context / State 是否保存 Conflict、Gap 与 Freshness？
- [ ] Execution / Authority 是否包含 Stop、Revoke、Takeover 与 Recovery？
- [ ] Evaluation / Decision 是否分开 PASS、Acceptance、Adoption、Release 与 Qualification？
- [ ] Human Control 是否展示 Decision Target，而非 Activity Flood？
- [ ] Organization / Handoff 是否由可分解性和独立性需要触发？
- [ ] Memory / Evolution 是否只从 Candidate 进入独立 Promotion / Adoption？
- [ ] Operations / Trace / Security / Economics 是否包含 Drift、Rights 与总生产成本？

### Gap、Excess 与成本

- [ ] 是否同时检查缺失能力和过度机制？
- [ ] 新机制增加了什么 Failure、Coordination 与 Maintenance Surface？
- [ ] 删除机制是否影响 Protected Floor 或 Recovery？
- [ ] Token、Human、Review、Waiting、Governance、Failure 与 Exit Cost 是否进入比较？
- [ ] 不可货币化 Guardrail 是否没有被强行换算成分数？

### 路线与案例

- [ ] 路线是否按条件依赖，而非固定 Level 顺序？
- [ ] Multi-Agent、Memory、HCP、Epoch 与 Self-Evolution 是否保持可选？
- [ ] 案例是否绑定具名历史切片、版本、Scope 与 Evidence？
- [ ] AI Game Dev OS 是否没有被评成 Level N？
- [ ] v4.94 是否只支持 Presence、Activity、Validation、Acceptance 与 Qualification 分离？
- [ ] 是否避免把本章候选模型写成已经改善效果？

---

## 22.46 结论

AI-native 工程能力不能由功能数量、Agent 数量、自治强度或组织复杂度排序。

更可靠的判断关系是：

~~~text
named workload and Intended Use
+ risk, recovery and operating constraints
→ required capability boundary

current bounded profile
+ evidence, coverage, unknown and cost
↕ compare

fitness finding
→ authorized disposition
→ adoption / operation / outcome / drift
→ re-evaluation
~~~

Engineering Capability Profile 描述当前可观察配置。

Capability Fit Review 比较当前配置和具名用途需要。

Finding 保存适配判断，Disposition 决定维持、限制、试验、增强、替换、退出或延期。

它们共同保留六个关键分离：

- Presence 不等于 Operational Use；
- Use 不等于 Boundary Adequacy；
- Evidence 不等于 Acceptance；
- Adoption 不等于 Sustained Fitness；
- Capability Gap 不等于必须增加 Automation；
- Capability Excess 不等于可以删除 Protected Floor。

原 Level 0–5 提醒我们关注从 Chat、Copilot、Bounded Agent、Multi-Agent、Human Control
到 Memory 与 Evolution 的不同问题域。

但这些问题域不是一条组织升级路线。

一个适配的项目可能保持单 Agent、局部 Context、Human Promotion 和短 Lifecycle。

另一个高影响系统可能需要更强 Authority、Independent Review、Trace、Security、
Recovery 与 Re-evaluation，却仍然不需要 Self-Evolution。

如果“成熟”这个词仍然保留，它描述的应当是：项目能否持续识别实际需要，在不降低
保护底线的情况下建立相称能力，并在 Evidence、成本、风险或 Drift 改变时修正自己的
配置。

下一章将用 AI Game Dev OS 的具名开发历史，暴露这些边界在一个共享 Provenance 案例中的
适用范围与限制，并提出需要在其他情境重新回答的 Transfer Questions。

案例的任务不是证明该系统达到某个 Level，而是保留：哪些能力真实存在，在哪个 Scope
进入执行，什么 Evidence 被产生，哪些结果没有发生，Human 怎样裁决，以及哪些结论
仍然不能从现有历史中推出。
