# 第15章 Memory Engineering
## 长期连续性来自受治理的记录，不来自把历史自动写成真理

> 工作稿状态：首轮逻辑修订稿，不替代 [全书大纲](../OringinalDocs/beyond_code_ai_native_software_engineering_outline_zh.md) 或 [Cognitive Control、Trust 与 Human Control Plane v0.1](../OringinalDocs/ai_native_cognitive_control_trust_human_control_plane_v0.1.md)。
> 回接说明：[RR-026](../RevisedResult/RR-026_第15章Memory_Engineering首轮回接说明.md)。
> 适用边界：本章提出候选 Memory Governance（记忆治理）模型，用于管理 Candidate、Promotion、Provenance、Retrieval、Conflict 与 Expiry；它不声称现有案例工程已经完整实现该模型，也不承诺自动改善长期效率或质量。

第14章建立了 Observation、Detector、Exception 与 Intervention 的运行链。

但运行记录不会因为被保存，就自动成为长期知识。

一个系统可以拥有大量：

- Log；
- Task Transcript；
- Commit；
- Test Result；
- Review；
- Decision；
- Incident；
- Summary；
- Workflow；
- Preference Note。

仍然无法回答：

- 哪些记录对未来有用；
- 哪些结论仍然适用；
- 哪些只是一次性判断；
- 哪些已经被取代；
- 哪些相互冲突；
- 哪些可以跨项目复用；
- 哪些有权进入当前 Context；
- 哪些应该被隔离或删除。

本章使用的工作定义是：

> **Memory Engineering（记忆工程：对可长期检索记录的候选产生、审查准入、来源绑定、适用性维护、检索使用、冲突处置、失效与删除进行工程化管理）**。

Memory Engineering 的目标不是让系统“记住一切”。

它要让后来的人或 Agent 能够定位有用历史，同时知道：

> 这条记录从哪里来、当时说了什么、适用于哪里、现在是否仍可用，以及哪些信息与它冲突。

---

# 15.1 单次能力、项目连续性与组织智能不是同一件事

强模型可以在一次任务中生成高质量结果。

这不表示项目已经拥有：

- 可追踪的历史决定；
- 稳定的失败经验；
- 可复用的 Procedure；
- 跨 Thread 的状态连续性；
- 对旧结论的失效机制；
- 对项目偏好和约束的正确解释。

**Project Memory（项目记忆：为未来项目决策保留、可检索且有来源与适用边界的持久记录集合）** 只提供连续性的一部分。

组织智能还依赖：

- Authority；
- Evidence；
- Workflow；
- Human Judgment；
- Review；
- Recovery；
- 当前 Context；
- Model 与 Tool Capability。

所以不能写成：

~~~text
more memory
→ more intelligence
~~~

更准确的是：

~~~text
traceable records
+ bounded retrieval
+ current validation
+ human and delegated judgment
→ may improve continuity and reuse
~~~

是否真的改善质量、速度或风险，仍需要具名结果和对照。

---

# 15.2 先区分必要、有用与可选

## 必要

高影响、长期或跨角色任务至少需要保留足够的外部记录，使后来者能够定位：

- 原 Intent 与 Scope；
- 当时的 Source、Evidence 与 Unknown；
- Decision 与 Authority；
- 关键 State Transition；
- 未解决问题；
- Recovery 或 Supersession。

这不要求构建向量数据库。

## 有用

当项目跨 Thread、跨 Agent、跨版本，或重复发生相似决策时，结构化 Memory Record、Index、Expiry 与 Conflict Link 通常有用。

## 可选

Embedding Retrieval、Graph Memory、自动摘要、跨项目知识库、个性化 Preference Model 和自动 Pattern Extraction 都是可选实现。

一个小型项目使用版本化 Decision Log、Issue、Git History 和几份维护良好的文档，可能比复杂 Memory Platform 更可靠。

---

# 15.3 Memory 不等于 Truth、Archive、Context 或模型参数

这些对象需要分开：

| 对象 | 作用 | 与 Memory 的关系 |
|---|---|---|
| Primary Source / Artifact | 保存原始代码、运行、决定或证据 | Memory 可以引用，不应无理由复制 |
| Archive | 以保留为目标保存历史材料 | 被保存不表示适合检索或复用 |
| Project Memory | 为未来用途维护有边界记录 | 仍可能过期、冲突或错误 |
| Memory Index | 帮助发现记录 | 命中不表示适用 |
| Context | 当前任务可访问的信息表面 | 只选择部分 Memory |
| Agent Input | 本次真正传给模型或 Harness 的输入 | 不等于模型理解 |
| Model Weights / Provider Memory | 模型或平台内部持续状态 | 项目通常不能把它当作可审计权威记录 |
| Truth / State Claim | 对当前或历史状态提出的可检验主张 | Memory 可以保存 Claim，但不赋予其 Truth |

项目应尽量把重要连续性放在可导出、可引用和可审查的外部记录中，而不是依赖不可检查的“模型应该还记得”。

平台级个人 Memory 可以改善交互便利性，但不能自动承担项目 Authority、Evidence 或审计职责。

---

# 15.4 七个工程对象构成最小 Memory 链

本章区分：

## Source Record（来源记录：作为 Memory Candidate 依据的原始或更接近原始的外部记录）

原始或更接近原始的 Artifact、Observation、Decision、Incident、Commit、Test、Review 或 Human Note。

## Memory Candidate（记忆候选：被提议为未来用途保留、但尚未完成准入裁决的记录或派生总结）

Candidate 可以由 Human、Agent、Workflow 或 Rule 提出。

## Promotion Decision（记忆准入裁决：有权主体决定某个 Candidate 是否以何种用途、Scope、状态和期限进入 Project Memory）

Promotion Authority 只决定能否进入 Memory Surface，不因此拥有底层事实的 Truth Authority。

## Memory Record（记忆记录：经过具名准入处置、保留 Source、Scope、状态、失效与冲突信息的可长期检索记录）

Record 可以是对 Primary Source 的引用，也可以包含有边界的 Derived Summary。

## Memory Index（记忆索引：用于发现 Memory Record 的导航、检索与过滤结构）

Index 不是另一份 Truth Store。

## Retrieval Candidate（检索候选：根据当前 Query 命中、但尚未完成适用性与 Context 选择检查的 Memory Record）

命中只表示相似或满足过滤条件。

## Use Record（使用记录：说明某条 Memory 是否被选择进入 Context、是否可观察地被访问，以及它用于哪个 Decision 的过程记录）

Use Record 不能证明模型理解或采纳了该 Memory。

基本关系是：

~~~text
Source Record
→ Memory Candidate
→ Promotion Decision
→ Memory Record + Index
→ Retrieval Candidate
→ applicability / authority / freshness / conflict checks
→ selected Context Item + Context Manifest
→ observable use and outcome
→ reaffirm / narrow / dispute / supersede / deprecate
~~~

每个箭头都可能停止。

自动 Capture 不等于 Promotion，Retrieval Hit 不等于 Validation，进入 Context 不等于被模型采用。

---

# 15.5 记忆类型应视为 Record Role，不是互斥分类

原大纲列出 Fact、Decision、Experience、Skill、Preference、Failure 和 Constraint Memory。

这些视角有用，但混合了内容、来源、用途和 Authority。

更稳妥的做法是把它们写成可重叠的 **Record Role（记录角色：说明一条 Memory 准备用于什么未来问题的用途标签）**。

| Record Role | 应保留的边界 | 不能自动成为 |
|---|---|---|
| State / Fact Claim Reference | Subject、Scope、Time、Source、Evidence、Applicability | 永久事实 |
| Decision Memory | Decision Target、选项、Authority、理由、Tradeoff、Supersession | 当前 Policy |
| Experience / Lesson Candidate | 观察、推导、替代解释、适用条件 | 通用规律 |
| Procedure / Skill Reference | Version、Environment、验证状态、Permission、Recovery | 可执行 Authority |
| Preference / Identity Record | Owner、表达方式、Scope、稳定性、Override | 所有人共同偏好 |
| Failure / Incident Memory | 影响、时间线、根因状态、Correction、未解决项 | 所有相似问题的原因 |
| Constraint / Policy Reference | Authority、Scope、Effective Time、Exception、Supersession | 自然事实 |

一条记录可以同时是 Decision Memory 和 Failure Memory。

这种重叠应显式标记，不需要强行放入唯一目录。

`Fact Memory` 这个名称尤其需要谨慎。被记住的通常是一个有来源、有时间和适用范围的 Claim，而不是脱离条件的永恒事实。

---

# 15.6 Promotion Contract 决定什么能进入长期工作面

一个 **Memory Promotion Contract（记忆准入契约：规定 Candidate 的未来用途、来源要求、适用边界、审查方式和失效条件的记录）** 可以是：

~~~yaml
memory_candidate_id: MEM-CAND-240
candidate_kind: retrospective_lesson
intended_uses:
  - future_validator_design_review

source_refs:
  - incident:D-048
  - review:d048_verifier_integrity_review

candidate_statement:
  text: >
    When a verifier changes an authority-bearing observation surface
    before the target is reached, observer integrity and target result
    must be recorded separately.
  epistemic_type: recommendation

scope:
  domains:
    - validator_design
  conditions:
    - target_not_reached
    - authority_bearing_surface_changed
  excluded:
    - declared_isolated_normal_outputs

promotion:
  authority_ref: AUTH-MEMORY-REVIEW-02
  required_review:
    - source_binding
    - counterevidence
    - cross_project_scope

lifecycle:
  review_on:
    - verifier_architecture_change
    - contradictory_incident
  expires_at: null
~~~

这是设计 Profile，不是统一 Schema。

Promotion 至少要检查：

- Future Decision Use；
- Source 与 Derivation；
- Epistemic Type；
- Scope 与 Exclusion；
- Counterevidence；
- Current Compatibility；
- Retention 与 Privacy；
- Promotion Authority；
- Invalidation Trigger；
- Review Cost。

不是所有 Task Summary 都值得进入长期 Memory。

---

# 15.7 Memory Provenance 必须记录转换链

**Memory Provenance（记忆来源链：从 Primary Source、Producing Activity 和 Responsible Subject 到当前 Memory Record 的生成、派生、修订与准入关系）** 至少应回答：

- Source 在哪里；
- Source Revision 或 Identity 是什么；
- 谁或哪个 Tool 产生；
- 何时观察、记录、总结和准入；
- 哪些内容是原始记录；
- 哪些是 Human Judgment；
- 哪些是 Agent Summary；
- 哪些是 Retrospective Inference；
- 哪些转换删除或压缩了信息；
- 哪个 Authority 接受其进入 Memory；
- 哪些 Source 已经不可访问；
- 是否存在循环引用。

候选字段可以是：

~~~text
memory_id
source_ref / source_revision
derived_from
producing_activity
responsible_subject
captured_at / promoted_at
transformation_method
epistemic_type
scope / intended_use
applicable_versions / environments
conflict_refs
invalidation_triggers
review_status
retention_policy
~~~

“这条内容在 Memory 中出现了很多次”不是多个独立 Provenance。

多个 Summary 如果都派生自同一 Source，只能算同一来源链的重复传播。

---

# 15.8 事实、决定、推导与建议进入 Memory 后仍需分开

进入长期记录不会改变 Epistemic Type。

例如：

~~~text
Observable fact:
D-079 candidate 471dd87 passed 42 selected tests.

Contemporaneous judgment:
Human rejected it as over-scoped for E1.

Retrospective inference:
Test fit and implementation-scope fit are separate questions.

Current recommendation:
Bind automated acceptance only to a named Decision Target and Authority.
~~~

如果 Memory Summary 压成：

~~~text
The candidate was wrong despite passing tests.
~~~

它删除了：

- 哪部分行为通过；
- 谁拒绝了什么；
- 拒绝依据；
- 适用阶段；
- 后来的推导与原始事实区别。

这类压缩会制造权威感，却降低复用价值。

---

# 15.9 Derived Summary 是新记录，不是 Source 的透明副本

**Derived Memory Summary（派生记忆摘要：从一个或多个 Source 经过选择、压缩和解释形成的二级记录）** 本身需要：

- Summary Producer；
- Source List；
- Transformation Method；
- Omitted Surface；
- Intended Audience；
- Scope；
- Generated At；
- Review Record / Finding / authorized Disposition Reference；
- Drill-down；
- Conflict 与 Unknown。

摘要可以提高检索效率。

但它也可能：

- 删除条件；
- 合并不同 Authority；
- 把失败与 `non-result` 混合；
- 把一次 Decision 变成通用规则；
- 把已过期状态写成现在时；
- 将 Counterevidence 隐藏在下层；
- 让派生内容反过来“证明”自己的 Source。

因此，摘要被频繁检索不应提高其 Truth Status。

---

# 15.10 Memory Pollution 不只是“记住了错误事实”

**Memory Pollution（记忆污染：错误、失去范围、失去时效、失去来源或获得错误 Authority 的记录进入长期复用链，并影响后续判断）** 可以来自：

- Source 本身错误；
- Summary 删除 Scope；
- Decision 被写成 Fact；
- Preference 被写成 Policy；
- 临时 Workaround 被写成标准 Procedure；
- 一次 Failure 被泛化成普遍 Cause；
- Historical Claim 被写成 Current State；
- Retrieval Match 被当作 Compatibility；
- 同源 Summary 被当作多源佐证；
- Agent 生成内容引用另一条派生 Memory，形成循环支持；
- 受污染外部内容携带 Prompt Injection；
- 过期 Skill 被赋予当前 Tool Authority；
- 项目特例被推广到所有项目；
- 已撤销 Constraint 继续进入 Context。

典型传播链是：

~~~text
weak or mis-scoped conclusion
→ promoted without boundary
→ retrieved repeatedly
→ used in generated explanations
→ re-summarized as corroboration
→ appears institutionally established
~~~

重复使用增加的是影响范围，不是证据独立性。

---

# 15.11 Memory Amplification 需要看传播条件

**Memory Amplification（记忆放大：一条记录因长期保留、频繁检索、广泛注入或高指令权而持续扩大影响的现象）** 不必是坏事。

经过验证的安全约束被稳定复用，可以减少重复错误。

风险来自放大与边界不匹配。

需要分别观察：

~~~text
retrieval frequency
context injection frequency
number of affected roles
decision impact
instruction or authority weight
lifetime
cross-project reach
source visibility
conflict visibility
recovery cost
~~~

这些因素不需要压成统一 Memory Risk Score。

低频但拥有高 Tool Authority 的过期 Procedure，可能比高频的普通说明更危险。

发现污染后的响应也不只有 Delete：

- Quarantine；
- Narrow Scope；
- Remove Instruction Authority；
- Attach Conflict；
- Rebuild Summary；
- Re-run Validation；
- Stop Cross-project Propagation；
- Supersede；
- Delete or Redact。

---

# 15.12 Lifecycle 不是一条单轴状态机

原大纲给出：

~~~text
Capture
→ Validate
→ Store
→ Retrieve
→ Reconfirm
→ Deprecate
→ Delete
~~~

这条链适合说明存在生命周期，但会造成三个误解：

1. Store 仿佛只发生在 Validate 之后；
2. Retrieve 仿佛会自动 Reconfirm；
3. Deprecate 仿佛表示内容 False，之后必然 Delete。

更准确的模型至少有四个独立轴。

## Admission Status

~~~text
captured
candidate
promoted
rejected
quarantined
~~~

## Epistemic / Applicability Status

~~~text
unreviewed
supported_for_scope
partial
disputed
stale
not_established_for_current_baseline
~~~

## Supersession Status

~~~text
current
superseded
deprecated
historical_only
~~~

## Storage / Retention Status

~~~text
hot
archived
redacted
scheduled_for_deletion
deleted_with_tombstone
retained_under_hold
~~~

一条 Memory 可以同时是：

~~~text
promoted
+ historical_only
+ supported_for_original_scope
+ archived
~~~

它不是当前建议，但仍是有效历史记录。

---

# 15.13 Expiry 与 Invalidation 不等于内容变成 False

**Memory Invalidation（记忆失效：某条 Memory 对具名当前用途的适用关系因依赖、版本、环境、Authority 或新 Evidence 变化而不再成立）** 应与历史有效性分开。

常见 Trigger 包括：

- Source Revision 改变；
- 适用的 Code、Schema、Data 或 Environment 改变；
- Decision 被 Supersede；
- Policy 或 Authority 被撤销；
- Preference Owner 修改表达；
- Procedure 所需 Tool 不再兼容；
- 新 Incident 提供 Counterevidence；
- Memory 依赖的 Assumption 到期；
- 项目进入不同生命周期阶段；
- Cross-project Transfer 改变了原 Scope。

**Expiry（到期：记录达到预定时间、版本或复核条件，需要重新建立当前适用性）** 只表示需要 Re-evaluation。

例如一个旧 Migration Procedure 到期，不表示每一步都错误；它表示不能直接对当前环境执行。

候选处置是：

~~~text
revalidate
narrow
mark historical
supersede
quarantine
deprecate
delete
~~~

---

# 15.14 Conflict Detection 不能只靠语义相似度

Memory Conflict 至少有多种类型：

| Conflict 类型 | 示例 | 需要的处置 |
|---|---|---|
| Direct Claim Conflict | 同一 Build 被记录为 deployed 与 not deployed | 检查 Source、Time 与 Domain |
| Temporal Supersession | 旧 Policy 与新 Policy 不同 | 保留历史并标记 Effective Time |
| Scope Conflict | 项目 A 的规则被用于项目 B | 收窄或建立 Transfer Candidate |
| Authority Conflict | Agent Summary 与 Human Decision 不一致 | 保留来源并按 Decision Target 升级 |
| Applicability Conflict | Procedure 对旧 Tool 有效，对新 Tool 未验证 | 标记不适用于当前配置 |
| Preference Conflict | 不同 Owner 或阶段的审美偏好不同 | 绑定 Owner、产品面与时间 |
| Evidence Conflict | 新 Observation 反对旧经验 | 保留 Counterevidence，重新审查 |
| Instruction Conflict | 两个 Skill 给出互斥动作 | 按 Authority、Scope 与 Compatibility 裁决 |

Embedding Similarity 可以发现候选相关项，不能判断哪条拥有 Authority，也不能区分更新、反例和不同 Scope。

Conflict 处置不应让模型静默合成一条“折中真相”。

至少需要：

- 保留原记录；
- 建立 Conflict Link；
- 标记当前 Applicability；
- 指定 Owner；
- 指定 Decision Target；
- 说明暂时选择哪条及依据；
- 设置后续 Review 或 Expiry。

---

# 15.15 Supersede、Deprecate、Quarantine 与 Delete 是不同动作

## Supersede（取代）

新记录成为当前使用入口，旧记录保留历史与 Provenance。

## Deprecate（弃用）

不再建议用于新任务，但可能仍对历史重建或旧环境适用。

## Quarantine（隔离）

记录因污染、来源不明、恶意内容、冲突或高风险而暂时不能进入普通 Retrieval / Context。

## Delete（删除）

根据 Retention、Privacy、Security 或治理要求移除内容。

## Tombstone（删除标记：在不保留被删除敏感内容的前提下，记录某个 Identity 已被删除、禁止重新导入或需要特殊处置的最小标记）

删除与审计、隐私和历史连续性可能冲突。

项目需要决定：

- 是否保留 Hash、ID、Reason 与 Deleted At；
- 是否允许从 Archive 重新导入；
- Derived Summary 是否级联删除；
- Index 与 Embedding 是否同步移除；
- Backup 与 Cache 怎样处理；
- Legal Hold 是否覆盖普通删除；
- 删除后哪些历史引用会失效。

---

# 15.16 Retrieval 是候选发现，不是知识调用成功

**Memory Retrieval（记忆检索：根据当前 Query、Filter 和索引机制发现候选 Memory Record 的过程）** 至少包含：

~~~text
current decision question
→ query and filters
→ retrieval candidates
→ scope / version / environment checks
→ freshness / invalidation checks
→ authority / instruction checks
→ conflict and counterevidence expansion
→ context selection
→ Context Manifest
~~~

检索质量不能只看相似度。

还需要检查：

- 当前 Decision Target；
- Record Role；
- Intended Use；
- Source；
- Project Namespace；
- Version 与 Environment；
- Current Applicability；
- Conflict；
- Authority；
- Security Label；
- Token / Attention Cost。

高相似度的旧 Workaround 可能正是最不该复用的内容。

低相似度但 Authority 明确的当前 Policy 可能更重要。

---

# 15.17 Retrieved、Selected、Supplied、Accessed 与 Adopted 分开

第5章已经建立：

~~~text
Project Memory / historical records
→ retrieval candidate
→ Context selection + authority / freshness checks
→ Context Pack + Manifest
~~~

第15章继续区分：

| 状态 | 可观察含义 |
|---|---|
| retrieved | Index 或 Search 返回了该 Record |
| selected | Context Assembly 决定提供该 Record |
| supplied | Payload、Reference 或 Access Path 被实际开放 |
| accessed | 工具可观察到 Source 被读取或展开 |
| cited | 输出显式引用该 Record |
| adopted | 有权 Decision 明确采用其中建议或规则 |

即使 Access Log 存在，也不能证明模型理解、相信或依赖了该条内容。

反过来，模型可能基于先验生成相似结论，而没有访问 Memory。

Use Record 只能记录可观察过程，不能声称隐藏认知状态。

---

# 15.18 Skill 不是普通 Memory Record

原大纲的 Skill Memory 容易混合：

~~~text
historical lesson
procedure
instruction
tool invocation
mutation authority
~~~

一个 Skill 至少可能包含：

- Information Content；
- Procedure；
- Instruction；
- Tool Binding；
- Permission Requirement；
- Authority Boundary；
- Verification；
- Recovery。

Memory 可以保存 Skill Version、使用历史、失败经验和 Candidate Proposal。

但把 Skill Record 检索出来，不会自动：

- 安装 Skill；
- 激活 Instruction Priority；
- 授予 Tool Permission；
- 扩大 Authority；
- 证明当前 Environment 兼容；
- 接受 Skill Update。

重要 Skill 变化属于第16章的 Candidate、Validation 与 Adoption 问题。

---

# 15.19 Preference 与 Project Identity 需要 Human Authority

**Preference Memory（偏好记忆：记录具名 Human、团队或项目在声明产品面、时间和适用条件下表达或接受的选择倾向）** 不能只写：

~~~text
The user prefers minimal UI.
~~~

至少需要：

- Preference Owner；
- Source；
- Explicit / Inferred；
- Product Surface；
- Strength 或 Override 条件；
- Effective Time；
- Current Intent 是否覆盖；
- Conflicting Preference；
- Human Review Record / Finding / authorized Disposition Reference；
- Last Reviewed At。

一次选择可能来自：

- 临时限制；
- 当前实验；
- 时间不足；
- 特定受众；
- 实际偏好；
- 对多个坏选项的妥协。

Agent 从行为中推断的 Preference 只能成为 Candidate，不能静默升级为 Project Identity 或 Producer Soul。

当前明确 Intent 通常可以覆盖历史偏好；安全、合规和组织 Policy 则不能被普通偏好覆盖。

---

# 15.20 项目记忆与跨项目知识必须分层

一个可用 Namespace 可以区分：

~~~text
task-local
repository / module
project
organization
domain
cross-project candidate
personal preference
external reference
~~~

Scope 变宽不是简单复制。

项目特例可能依赖：

- 当前 Architecture；
- 团队角色；
- Toolchain；
- Authority Model；
- Product Phase；
- Historical Constraint；
- Data；
- Risk Appetite；
- Creative Direction。

因此：

> **Project success does not create cross-project validity.**

中文语义是：

> **一条经验在某个项目中有效，不会自动获得跨项目适用性；扩大适用范围需要新的 Candidate、翻译、验证和裁决。**

跨项目搜索可以返回项目内 Memory，但默认应显示原 Namespace，而不是把来源抹成“通用最佳实践”。

---

# 15.21 Cross-project Transfer 应生成新 Candidate

**Memory Transfer（记忆迁移：把一个 Namespace 中的记录提议用于另一个项目、环境或组织边界的过程）** 至少需要：

1. 保留原 Source 与 Namespace；
2. 声明目标项目和 Decision Use；
3. 提取依赖与隐含条件；
4. 识别 Authority、Tool、Data 和 Policy 差异；
5. 保留 Counterexample；
6. 形成目标侧 Candidate；
7. 在目标环境验证或由有权角色接受；
8. 设置目标侧 Expiry 与 Owner。

迁移结果应是：

~~~text
source project memory
+ transfer rationale
+ target compatibility evidence
→ target-side memory candidate
~~~

不是：

~~~text
source project memory
→ global rule
~~~

来自 External Capability Layer 的知识也要经过相同检查，尤其要处理 License、Confidentiality、Prompt Injection 和来源更新。

---

# 15.22 自动 Capture 与自动 Promotion 必须分开

运行系统可以自动 Capture：

- Task Event；
- Tool Receipt；
- Commit；
- Test Result；
- Exception；
- Intervention；
- Decision Form；
- Review Outcome；
- Handoff；
- Runtime Metric。

自动 Capture 适合形成 Archive 或 Candidate Source。

自动 Promotion 风险更高，因为它决定未来默认能检索到什么。

可以预先委托窄 Promotion Rule，例如：

> 将每个已签署 Release Decision 的只读引用和 Authority Metadata 加入 Decision Index。

但以下内容不宜仅因一次任务成功就自动 Promotion：

- 通用经验；
- Root Cause；
- Project Preference；
- 新 Procedure；
- Skill Update；
- Policy；
- 跨项目规律；
- 对 Human Intent 的总结。

自动规则需要记录：

- Promotion Rule Version；
- Source Requirement；
- Maximum Scope；
- Forbidden Record Type；
- Conflict Check；
- Expiry；
- Rollback / Quarantine；
- Authority Reference。

---

# 15.23 Memory Review 不应退化为定期全文重读

**Memory Review（记忆审查：根据风险、变化和使用情况重新检查 Memory 的来源、适用性、冲突、权限与保留状态）** 是第10章 Review 的 Target-specific 应用，可以由事件触发。它默认产生 Finding、Unknown 与 Disposition Recommendation，不因名称获得保留、删除或授权变更权。

候选 Trigger 包括：

- Memory 被用于高影响 Decision；
- Source、Dependency 或 Environment 改变；
- 新 Counterevidence；
- Repeated Rework；
- Incident 或 Escaped Defect；
- Preference Owner 改变；
- Policy / Authority 更新；
- Skill / Tool Version 更新；
- Cross-project Transfer；
- Expiry 到达；
- 异常高 Retrieval 或 Injection Frequency；
- 长期未使用且维护成本高；
- Security / Privacy Request。

Memory Review 可以建议：

~~~text
keep
reaffirm for scope
narrow
attach conflict
rebuild summary
remove instruction authority
quarantine
supersede
deprecate
delete
~~~

这些建议只有在具名 Authority 通过 Decision Record 对 Memory Retention、Instruction Authority 或 Retrieval Eligibility 等 Decision Target 作出处置后，才产生规范性效力。Reviewer 报告的 PASS 只是 Finding / Recommendation；只有 Review Contract 已明确委托相应 Grant 时，它才可以同时形成窄 Review Disposition。无论哪种情况，都不证明未来永久正确。

---

# 15.24 Security、Privacy 与 Memory Poisoning

**Memory Poisoning（记忆投毒：恶意、不可信或被错误赋权的内容进入长期检索与 Context 链，从而持续影响后续判断或动作）** 会扩大一次输入攻击的持续时间和传播范围。

具体风险包括：

- Prompt Injection 被持久化；
- Secret、Credential、Personal Data 或 Proprietary Code 泄露；
- 恶意 Summary 隐藏原 Source；
- 外部知识更新后旧内容继续使用；
- 跨项目检索泄露边界；
- 删除只清理正文，Embedding 与 Cache 仍存在；
- 低权限记录携带高优先级 Instruction；
- 攻击者通过重复出现制造“共识”；
- Agent 自己生成并引用自己的 Memory，形成循环权威。

防护可以包括：

- Source Trust 与 Security Label；
- Data Minimization；
- Redaction；
- Namespace Isolation；
- Instruction / Data Separation；
- Quarantine；
- Retrieval-time Policy Filter；
- Access Audit；
- Derived Copy Tracking；
- Cascade Delete；
- External Content Revalidation；
- High-impact Use Review。

Security Label 也不等于内容真实。它只描述处理与访问边界。

---

# 15.25 Memory 可观测性关注使用链，不关注“读心”

可以观察：

- Candidate 数量和来源；
- Promotion / Rejection；
- Retrieval Candidate；
- Selected / Supplied / Accessed / Cited；
- Conflict Hit；
- Stale Record Hit；
- Quarantine；
- Supersession；
- Cross-project Transfer；
- Memory-linked Rework 或 Incident；
- Review Delay；
- Storage 与 Retrieval Cost。

不能直接观察：

- 模型是否真正记住；
- 某条 Memory 在隐藏推理中占多大权重；
- 没有 Citation 就一定没有影响；
- 有 Citation 就一定造成了结果。

候选指标可以是：

~~~text
stale retrieval incident
scope mismatch incident
conflict surfaced before action
memory-linked rework
source drill-down success
quarantine response time
cross-project transfer rejection
retrieval and review cost
~~~

这些指标需要与任务结果、漏报、维护成本和 Human Judgment 联合解释。

`retrieval rate ↑` 或 `memory usage ↑` 不是 North-star Metric。

---

# 15.26 案例只保留 Memory 转换风险

完整事件见[第23章](第23章_AI_Game_Dev_OS纵向案例_首轮修订稿.md)。本章只保存三条“不得写入长期记忆的结论”：

| Episode | 必须保留的记录 | 不得压成 |
|---|---|---|
| D-048 | Observer Failure、Target 未被观察、`non-result`、Human Disposition 与 Corrective Path | “Source 导致 Target Compile 失败” |
| D-079 | 42 个 Selected Tests PASS、Human 拒绝 Over-scoped Scope、较小 Forward Correction 成为后续 Baseline | “测试证明较小方案最好” |
| D-073 至 D-075 | Governance Artifact 增长、Delivery Evidence 停滞与后续路线变化；Strict Fail-closed 曾捕获真实缺陷，后续结果仍是 `NON_QUALIFYING` | “严格治理总是有害”或“Function-first 单独造成恢复” |

这些内容分别见[Target `non-result` 案例记录](../Evidence/receipts/ER-20260818-002__CLM-C06-004.md)、[测试与范围裁决记录](../Evidence/receipts/ER-20260818-003__CLM-C09-001.md)、[演化候选案例记录](../Evidence/receipts/ER-20260824-003__CLM-C16-001.md)和[治理活锁历史记录](../Evidence/receipts/ER-20260818-001__CLM-OUTLINE-002.md)。现有材料没有长期维护成本或受控效率对照；只能形成有范围 Lesson Candidate。

---

# 15.27 最小实现从一个高价值记忆问题开始

不要先构建全项目 Vector Store。

选择一个重复且重建成本高的问题，例如：

- 为什么某项 Architecture Decision 存在；
- 哪个 Incident Lesson 对当前 Validator 适用；
- 哪个 Policy 已经取代旧 Policy；
- 哪个 Procedure 与当前 Tool Version 兼容；
- 哪些 Human Preference 仍适用于当前产品面。

建立最小闭环：

1. 定义未来 Decision Use；
2. 选择 Primary Source；
3. 创建 Memory Candidate；
4. 标记 Fact、Judgment、Inference 或 Recommendation；
5. 绑定 Source、Scope、Version、Environment 与 Authority；
6. 声明 Counterevidence、Conflict 与 Unknown；
7. 由具名角色作 Promotion Decision；
8. 建立一个可过滤 Index；
9. 模拟 Retrieval；
10. 执行 Applicability、Freshness 与 Authority Check；
11. 写入 Context Manifest；
12. 记录可观察 Use；
13. 模拟 Source Change、Conflict 与 Expiry；
14. 演练 Quarantine、Supersede 与 Delete；
15. 评估是否减少了重建成本或错误。

如果系统只能写入和搜索，却不能处理失效、冲突和删除，它还不是可治理的 Project Memory。

---

# 15.28 与相邻章节的所有权边界

| 对象 | 所属章节 | 第15章如何使用 |
|---|---|---|
| Context Contract、Pack、Manifest、Progressive Retrieval | 第5章 | 决定检索到的 Memory 是否进入当前信息面 |
| State Claim、Source、Provenance、Applicability、Conflict | 第6章 | 约束 Memory 中 Claim 的语义 |
| Evidence Use 与 Decision Disposition | 第9章 | 约束 Memory 何时能支持当前 Decision |
| HCP Projection 与 Drill-down | 第12章 | 显示 Memory Source、Conflict 与 Expiry |
| Authority Grant 与 Delegation | 第13章 | 约束 Promotion、Adoption、Delete 与 Cross-project Transfer |
| Observation、Exception 与 Intervention | 第14章 | 提供候选 Source 和 Memory 使用反馈 |
| Candidate、Promotion、Record、Index、Retrieval、Conflict、Expiry | 第15章 | 本章核心对象 |
| Workflow / Skill Candidate、Evaluation Contract、Activation / Rollout Record | 第16章 | 评估经验是否应改变系统行为；基础 Adoption 引用第9章 |

第15章可以保存 Skill 或 Workflow 的历史与 Lesson Candidate，但不能自行安装 Skill、改变 Workflow 或扩大 Authority。

---

# 15.29 本章原则

1. **Memory 提供连续性，不产生 Truth。** 保存与重复不等于验证。
2. **Capture 不等于 Promotion。** 自动归档不能静默进入默认长期工作面。
3. **Promotion Authority 不等于 Truth Authority。** 准入只决定检索资格和用途边界。
4. **Record Role 可以重叠。** Fact、Decision、Experience、Failure 与 Constraint 不是互斥目录。
5. **Provenance 包含转换链。** Summary 必须显示 Source、Omission 与 Derivation。
6. **Epistemic Type 不随存储改变。** Fact、Judgment、Inference 与 Recommendation 继续分开。
7. **Retrieval Hit 不等于 Applicability。** 相似度不能替代 Scope、Version、Authority 与 Conflict。
8. **进入 Context 不等于被采用。** 只记录可观察访问，不声称隐藏认知。
9. **Expiry 不等于 False。** 它表示当前适用性需要重新建立。
10. **Conflict 不应静默融合。** 保留来源、差异和有权处置。
11. **Cross-project Scope 必须重新获得。** 项目成功不会自动生成通用规律。
12. **Skill 与 Preference 需要额外 Authority。** Memory 不能自行激活 Instruction、Tool 或 Project Identity。
13. **Delete 需要处理 Derived Copy。** Index、Embedding、Cache 与 Backup 都属于删除面。
14. **Memory 机制也需要证据。** 更多记录和更高 Retrieval Rate 不自动代表更好的工程结果。

---

# 15.30 常见反模式

- 把所有 Log 和 Transcript 直接称为 Memory；
- 把 Archive 中的内容默认注入 Context；
- 把 Memory Record 当作 Truth；
- 把 Promotion 当作事实验证；
- 每次任务成功都自动总结为最佳实践；
- 用重复出现次数表示独立证据；
- Summary 不保留 Primary Source；
- 把 Decision、Inference 和 Recommendation 压成一句 Fact；
- 把 Historical Claim 写成 Current State；
- 检索相似度高就忽略 Version 与 Environment；
- Retrieved 被写成 Used；
- Accessed 被写成 Understood；
- Skill Record 被检索后自动获得 Tool Authority；
- 一次 Human 选择被写成永久 Project Preference；
- 项目特例被推广为跨项目规则；
- Conflict 由模型自动融合成折中答案；
- Expired 被机械删除，导致历史不可重建；
- Deprecated 内容继续作为默认 Instruction；
- 删除正文但保留 Embedding、Cache 和 Derived Summary；
- Prompt Injection 被 Promotion 到长期 Memory；
- Agent 用自己的派生 Summary 反向证明自己的结论；
- 用 D-048、D-079 或 Governance Livelock 推出全局规律；
- 声称 AI Game Dev OS 已验证完整 Memory Engineering 架构。

---

# 15.31 本章检查清单

## Candidate 与 Promotion

- 未来 Decision Use 是否明确？
- Candidate 来自 Primary Source、Human Judgment 还是 Agent Summary？
- Fact、Judgment、Inference 与 Recommendation 是否分开？
- Promotion Authority 是否明确且没有被误写成 Truth Authority？
- 是否真的值得承担长期维护成本？

## Provenance 与 Scope

- Source、Revision、Producer、Time 与 Transformation 是否可追踪？
- 是否声明 Project、Domain、Version、Environment 与 Intended Use？
- Summary 删除了哪些条件或 Counterevidence？
- 多条记录是否其实来自同一来源链？

## Applicability 与 Conflict

- Freshness、Expiry 与 Invalidation Trigger 是否存在？
- Historical Validity 与 Current Applicability 是否分开？
- Direct、Temporal、Scope、Authority、Preference 和 Instruction Conflict 是否处理？
- 冲突是否被静默融合？

## Retrieval 与 Context

- Query 是否绑定当前 Decision Target？
- Namespace、Version、Environment、Authority 与 Security Filter 是否使用？
- Retrieved、Selected、Supplied、Accessed、Cited 与 Adopted 是否分开？
- Context Manifest 是否记录实际提供内容？
- 是否声称知道模型隐藏使用状态？

## Skill、Preference 与 Transfer

- Skill 的 Information、Procedure、Instruction、Tool 与 Authority 是否分开？
- Preference 是 Explicit 还是 Inferred，Owner 与 Override 是什么？
- Cross-project 使用是否生成目标侧 Candidate？
- External Memory 是否处理 License、Confidentiality 与 Injection？

## Lifecycle、Security 与 Cost

- Supersede、Deprecate、Quarantine 与 Delete 是否分开？
- Derived Summary、Index、Embedding、Cache 与 Backup 是否跟随处置？
- 是否支持 Redaction、Retention、Legal Hold 与 Tombstone？
- Memory Pollution 发生后能否停止传播并重建 Context？
- Retrieval 与 Review 收益是否覆盖 Storage、治理和认知成本？

---

# 15.32 本章结论

Memory Engineering 不从“如何让 Agent 永远记住”开始。

它从一个更严格的问题开始：

> 哪条历史记录有资格在未来被重新发现、进入 Context 并影响决定？

最小链条是：

~~~text
Source Record
→ Memory Candidate
→ scoped Promotion Decision
→ Memory Record + Provenance
→ bounded Retrieval Candidate
→ current applicability and conflict checks
→ Context selection
→ observable use and outcome
→ reaffirm / narrow / supersede / quarantine / delete
~~~

这条链的核心边界是：

> **Memory preserves claims and decisions; it does not convert them into truth, authority, or universal knowledge.**

中文语义是：

> **记忆负责保存和重新提供有来源的主张与决定；保存、检索和重复使用都不会自动把它们变成真理、授权或跨项目通用知识。**

下一章将讨论：当 Memory、Observation 和运行经验提出一个新的 Workflow、Skill、Agent Contract 或组织结构候选时，系统怎样评估、采用、撤回或前向修正，而不把“产生变化”误写成“完成进化”。
