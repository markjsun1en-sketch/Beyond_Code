# 第6章 Truth and State Architecture
## 在 Claim、State、Decision 与 Assumption 之间建立可验证秩序

> 工作稿状态：完整章节候选，不替代 [第6章原稿](../OringinalDocs/第6章.md)。
> 回接说明：[RR-020](../RevisedResult/RR-020_前六章首轮分别调整说明.md)。
> 适用边界：本章治理的是可修订的 Claim 及其依据，而不是“Truth 对象”；Intent、Decision／Policy、State Claim、Assumption 与 Evidence 被建模为语义上可区分的记录，授权使用不等于事实成立。

上一章讨论 Context Engineering（上下文工程，即持续选择、组织和更新 Agent 可访问信息表面的工程活动）。

Context Engineering 回答：

> Agent 为完成当前 Intent，应该接触哪些信息？

但信息进入 Context 后，还有另一个问题：

> 这些信息分别在描述什么？为什么可以相信？它们对当前任务仍然有效吗？

一份设计文档说系统应该采用方案 A。

当前代码实现的是方案 B。

运行时观测显示的是行为 C。

测试仍按旧规则验证。

一个历史决定已经被后续决定取代。

当前 Worktree 还有一组尚未提交的变化。

把这些材料全部交给 Agent，并不会自动产生真实世界。更强的模型甚至可能把互相冲突的材料解释成一个语言上连贯、工程上并不存在的状态。

因此，本章讨论的不是哲学意义上的真理，也不是建立一个保存“最终正确答案”的数据库。

它讨论的是：

> **软件项目如何管理关于当前状态的 Claim（可被证据支持、反驳和修订的陈述），使其来源、证据、适用范围、不确定性和冲突能够被 Agent 与人类共同检查。**

---

# 6.1 Truth Architecture（状态主张及其依据的治理结构）管理的不是“真理对象”

“Truth Architecture”是本书对问题域的名称。

但系统真正能够保存的只有：

- 关于状态的陈述；
- 产生陈述的来源；
- 支持或反对陈述的 Evidence；
- 赋予规范性约束的 Decision 与 Policy；
- 尚未验证、但暂时允许使用的 Assumption；
- 对这些对象作出的当前裁决。

换句话说：

```text
System stores Claims and Records
not metaphysical Truth
```

本章需要分别回答两个问题：

```text
Descriptive support
这条 State Claim 获得了多少适用证据支持？

Authorized use
谁允许它或某条显式 Assumption 被用于哪一个决策目标？
```

因此，本章不把“当前被授权使用”定义成“事实成立”。更准确的表达是：

> 在明确问题、版本、范围和时间窗口中，一条 State Claim 可以获得不同程度的证据支持；有权角色或授权机制再决定它是否足以作为某个具体决策的依赖依据。

Authority 可以允许团队在不确定条件下行动，但这种允许不会把 Assumption 变成已验证事实。

State Claim 及其使用关系还要允许以后被：

```text
revalidated
superseded
expired
conflicted
rejected
```

如果一个系统只能写入 Truth，却不能表达“不知道”“存在冲突”或“曾经成立”，它更容易制造确定性幻觉。

---

# 6.2 五种语义角色必须可区分

第六章首先需要建立的不是更多 Truth Domain，而是五种不同的工程语义角色。

## Intent Artifact（意图资产：可版本化的期望结果记录）

表达：

> 希望未来达到什么状态，以及为什么。

例如：

> 旧版 Save 应能安全迁移到当前版本。

Intent 描述 Desired State（期望达到的状态），不证明系统已经做到。

## Decision / Policy Record（决策／策略记录：在有效授权下形成的规范性内容）

表达：

> 当前被授权采用什么规则、方案或约束。

例如：

> 在 v1.0 前不得移除旧 Save 兼容层。

Decision / Policy Record 规定当前应该怎样行动，不描述系统物理上已经怎样运行。它的规范效力来自有效的 Authority Grant、Scope 与适用条件；记录本身不是授权来源，也不能反向扩大作出它的主体所拥有的 Authority。

## State Claim（状态主张：关于具体状态的可判断陈述）

表达：

> 关于当前或过去状态的一条可判断陈述。

例如：

> Commit `abc123` 中包含 v2 → v3 Migration。

State Claim 必须绑定 Domain（状态领域）、Scope（适用范围）、Version（版本）、Time（时间）和 Provenance（来源及流转记录）。

## Assumption（假设：尚未验证但暂时采用的未知）

表达：

> 尚未验证，但当前执行暂时需要采用的工作假设。

例如：

> 仍然存在使用 v2 Save 的活跃用户。

Assumption 不是低质量 Truth。它是一个拥有风险、验证路线和失效条件的独立对象。

## Evidence Record（证据记录：支持或反驳主张的可检查材料）

表达：

> 观察、测量、测试、截图、日志或人工评审等可检查材料。

例如：

> 三个 v2 Save 样本经过 Migration 后均能在目标 Build 加载。

Evidence 支持或反对 Claim，但 Evidence 不等于 Claim。

五种角色之间的基本关系是：

```text
Intent              desired outcome
Decision / Policy   normative content under authority
State Claim         description of state
Assumption          explicit unknown used for work
Evidence            support or counterevidence
```

它们不能因为出现在同一文档、同一 Context Pack 或同一句自然语言里就静默转换。

“角色可区分”不等于“必须形成五个文件”。同一个不可变测试报告可以既是 Evidence Artifact，也可以成为关于该次运行的 Primary Source；一份任务说明也可以引用 Intent、Decision 和 Assumption。真正需要避免的是：读者或 Agent 无法判断某段内容此刻被用作期望、授权、状态陈述、显式未知，还是支持材料。

是否拆成独立 Record，应由复用范围、冲突风险、生命周期差异和追踪成本决定。

## Claim 是上位类型，不同子类型不共享同一验证标准

本书把 Claim（主张：对具名对象、范围、时间或版本提出的可被支持、挑战、限定或撤回的命题）作为上位语义类型。

一条可检查的 Claim 至少需要能够关联：

- Statement 与 Target；
- Scope 与 Reference Time / Revision；
- Producer 与 Provenance；
- Evidence 与 Counterevidence；
- Intended Use；
- 当前仍未成立的结论。

State Claim、Behavior Claim、Completion Claim、Risk Claim、Reliance Claim 与 Improvement Claim 可以共享这些关系，但它们的 Target、评价方法、Authority 与允许用途不同。一个 Behavior Claim 的 Test PASS 不能自动验证 Improvement Claim；一个 Completion Claim 也不能自动形成 Acceptance、Adoption 或 Release。

---

# 6.3 State Claim 需要分别记录多个维度

一个混合 `Type + Status` 字段很容易把不同问题塞在一起。

例如：

```text
Observed
Verified
Derived
Approved
Stale
Rejected
```

这些词并不属于同一个维度：

- Observed 描述证据如何产生；
- Derived 描述推导方式；
- Verified 描述验证状态；
- Approved 描述授权裁决；
- Stale 描述对当前 Baseline 的适用性；
- Rejected 只有在说明是 Evidence 反驳还是有权角色拒绝某种用途时才有明确语义。

更稳妥的 State Claim 可以分别记录多个维度。只有在值可以独立组合且同一维度内部语义一致时，才把它称为正交轴。

```text
Claim ID
Statement

Subject Domain
Scope
Version / State Reference

Epistemic Basis
Validation Coverage
Evidence Relation
Conflict Status
Applicability Status

Provenance
Evidence Links
Producer / Owner
Decision / Disposition Links
```

## Subject Domain（主张所描述的状态领域）

回答：

> 这条 Claim 在描述哪一种状态？

常见 Domain 包括：

```text
Repository
Build
Runtime Behavior
Data
Configuration
Environment
Deployment
```

Domain 不是越多越好。项目只需要区分那些具有不同 Authority、更新机制或风险的状态。

## Epistemic Basis（主张形成的认知依据）

回答：

> 这条 Claim 是怎样形成的？

例如：

```text
observed
measured
inferred
reported
declared
```

这些值只描述 Claim 怎样形成。Test 是否通过以及覆盖了什么，应记录在 Evidence 与 Validation Coverage 中。一条 Derived Claim 仍然可以经过验证，因此 `inferred` 与 `verified-for-scope` 可以同时成立。

## Validation Coverage（验证覆盖程度）

回答：

> 当前验证覆盖到什么程度？

例如：

```text
unverified
partial
verified-for-scope
```

其中，`verified-for-scope` 只表示证据覆盖了已声明的 Claim 与范围。它不等于 `qualified-for-use`（已经满足某个具体用途的资格条件）。后者还取决于预期用途、风险等级、适用 Gate，以及谁拥有接受该用途的 Authority。

## Evidence Relation（证据与主张的关系）

回答：

> 当前材料是在支持、反驳，还是形成混合结果？

例如：

```text
none-linked
supporting
counterevidence
mixed
```

这不是 Evidence 自身的固定强弱等级，而是它与某条具体 Claim 的关系。

## Conflict Status（冲突状态）

回答：

> 是否存在尚未解决的竞争 Claim 或不兼容来源？

例如：

```text
none-detected
detected
unresolved
resolved-with-record
```

## Applicability Status（对当前范围的适用状态）

回答：

> 这条 Claim 现在还适用吗？

例如：

```text
active
stale-for-current-baseline
superseded
expired
```

## Claim Use Disposition（针对具名用途的有权处置）

回答：

> 对哪个 Decision Target，有权角色或机制允许怎样使用这条 Claim？

例如：

```text
accepted-for-use:<decision-target>
rejected-for-use:<decision-target>
deferred-for-use:<decision-target>
```

Claim Use Disposition 是外部 Decision Record 针对 Claim Use 的结果关系，不是 State Claim 自身的真值或描述性状态。Authority 可以允许、拒绝或延后某种依赖用途，不能通过处置使 Claim 本身成为事实。

这些描述性维度与外部使用关系明确分开后，系统才能表达：

> 这是一条关于 Runtime 的推导性 Claim，证据覆盖部分成立，当前版本仍 Active，但与另一条观测存在未解决冲突。

而不是被迫把它压成：

> True。

---

# 6.4 Source of Truth（针对特定问题的优先权威来源）需要授权来源和适用边界

软件团队经常说：

> Git 是 Source of Truth。

这句话只有在问题明确时才成立。

Git 可以回答：

> 当前 Repository State 中有哪些源文件？

但不能独立回答：

- 哪个 Commit 已部署到 Production；
- 当前数据库是什么 Schema；
- 某个 Feature Flag 是否启用；
- 用户实际看到什么行为；
- 产品是否批准继续兼容旧接口。

因此更严谨的规则是：

> **Source of Truth is scoped to a question.**

对存在多状态面或高冲突成本的项目，可以建立一个最小 Authority Matrix（问题—权威来源矩阵）：

| 问题 | 优先来源 | 常见补充证据 |
|---|---|---|
| 当前源实现是什么 | Repository/Commit/Worktree | Static analysis、diff |
| 当前 Build 包含什么 | Build artifact + build metadata | Source revision、CI record |
| 当前实际发生什么 | Runtime observation | Logs、trace、capture |
| 当前数据状态是什么 | Database/Save metadata | Migration history、snapshot |
| 当前配置是什么 | Effective runtime config | Config source、deployment manifest |
| 当前应该遵守什么 | Approved Decision/Policy | Intent、rationale |
| 本次任务以什么为起点 | State Snapshot | Git status、runtime/data references |

这张表不应成为全项目固定真理层级。

Runtime Observation 可以推翻“界面没有重叠”这类行为 Claim，却不能决定“是否允许重做整个 HUD”。后一个问题属于产品 Decision Authority。

因此需要分开：

```text
Authority Source / Grantor
= recognized Owner / Role / institutional mandate

Authority Grant
= Source / Grantor
+ Subject
+ Action / Decision Type
+ Scope / Condition / Time
+ Policy / Delegation references

Authority Applicability
=
Question
+ Domain
+ Scope
+ Version
+ Time
```

而不是：

```text
One source rules everything
```

授权机制决定谁或什么拥有 Authority；Question、Domain、Scope、Version 和 Time 只限定该 Authority 在哪里适用，不能凭空产生授权。

关于这一点，现有证据只能支持有限范围。SP122 的 authority audit 显示：实现 commit 对“实际实现了什么”有描述价值，但不能覆盖已经批准的设计方向；历史冲突也必须被保留。[SP122 authority-audit 案例记录](../Evidence/receipts/ER-20260810-001__CLM-C06-001.md)

---

# 6.5 “Code as Truth”应收窄，而不是废弃

`Doc as Intent, Code as Truth` 仍然是一个有用的早期启发式。

它防止 Agent 把未来设计或过期文档误认为当前实现。

但更准确的表达是：

> **Repository State is the authority for questions about current source implementation.**

Repository State 不只是一条 Commit ID，还可能包括：

```text
Commit
Branch
Worktree
Dirty Changes
Submodules
Generated Sources
```

而“文档”也不天然等于 Intent。不同文档可能是：

- Intent；
- Decision；
- Policy；
- Runbook；
- Historical Record；
- Observation；
- Proposal。

因此简单规则可以保留为教学入口：

```text
Design Doc as intended state
Repository State as source implementation baseline
```

当项目存在多个独立变化的状态面、高冲突或高恢复成本时，Typed Records 和 Domain-scoped Authority 可能比这条启发式更合适。

---

# 6.6 Decision、State 与 Assumption 不能混成 Current State

一个任务开始时，人们常把所有必要信息统称为“当前状态”。

但下面三项性质不同：

```text
Runtime uses schema v3             State Claim
Do not remove v2 compatibility     Decision
Some active users still have v2    Assumption
```

如果把它们都放进 State Model，Agent 容易把：

> 当前决定继续兼容 v2

误读为：

> 已经证明当前仍有大量 v2 用户。

因此 State Snapshot（状态快照：在声明范围、时点和采集边界内形成的状态观察与引用集合）只描述有界状态记录：

```text
State Snapshot
├── repository / worktree
├── build / deployment
├── runtime behavior
├── data / configuration
└── environment / dependency versions
```

任务执行确实还需要 Intent、Decision 和 Assumption，但这些应通过另一个对象组合。

本书将其称为：

> **Execution Baseline Manifest（执行基线清单：记录本次执行获准依赖的状态、意图、决策与显式假设）。**

```text
Execution Baseline Manifest
├── State Snapshot reference
├── Intent Artifact reference
├── Active Decision / Policy references
├── Open Assumptions
├── Known Conflicts
├── Known Dirty Changes
└── Evidence Baseline
```

Manifest 的作用不是宣布这些内容都是真实状态，而是声明：

> 本次执行被授权从哪些状态、规则和显式未知出发。

## Decision Record 需要同时保存理由与生命周期

Decision 不只是一个约束句子。长期项目还需要知道：谁在什么范围内作出决定、为什么这样决定、它何时生效，以及什么条件会使它失效。

一个最小 Decision Record 可以包含：

```yaml
decision_id: DEC-014
statement: release R 之前保留 v2 compatibility
owner: release-owner
authority_grant_ref: AUTH-REL-001
decision_target:
  type: policy-application
  target_ref: save-migration-release-R
  intended_use: release-R planning
scope: save-migration
effective_version: v3

considered_evidence_refs:
  - EVD-SAVE-DISTRIBUTION-004
disposition: approved

rationale: 在用户分布未知时保留有界兼容路径
assumption_refs:
  - ASM-009
options_considered:
  - remove-v2-loader-now
chosen_option: keep-bounded-compatibility
tradeoffs:
  - temporary maintenance cost

supersedes: DEC-006
review_condition: v2 usage confirmed below threshold
expiry: release-R
validity_mode: temporary
```

这里至少要保持四个不同维度：

```text
Record Status        draft / recorded / withdrawn
Decision Disposition approved / rejected / deferred / conditional
Applicability Status active / superseded / expired / cancelled
Validity Mode        temporary / open-ended / condition-bound
```

`proposed` 属于尚未形成正式 Decision 的 Record Status，不是已经作出的 Decision Disposition。一个 Decision 可以历史上已经批准，但当前因版本变化而过期；也可以只在未被后续 Decision 覆盖的 Scope 中继续 Active。同一 Scope、Version 和时间窗口内，`active` 与 `superseded` 不应同时成立。若把这些维度塞进同一个 `status`，Agent 很容易把“历史上批准过”误读成“当前仍应执行”。

Rejected Options（已被否决但可能再次出现的方案）值得保存时，应记录否决原因和重新考虑条件：

```text
option
reason_rejected
reconsider_when
```

不需要保存每一次头脑风暴。优先记录成本较高、容易被 Agent 重新提出，或只有在特定条件下才不适用的方案。

## Assumption Record 需要风险、验证路线和失效条件

Assumption 允许任务在信息不完整时继续，但它不能只是一句藏在计划里的“暂时认为”。一个可检查的 Assumption Record 可以包含：

```yaml
assumption_id: ASM-009
statement: active users 中仍存在 v2 saves
source: incomplete telemetry
reason_for_use: migration scope cannot otherwise be bounded

impact: high
validation_method: inspect save-version distribution
owner: data-owner
expiry: before production migration
dependent_actions:
  - enable-v2-write-path
```

`impact` 不是模型信心分数。它描述假设错误后可能造成的工程后果。项目可以采用自己的策略；一个简单的默认边界是：

| 影响与可逆性 | 当前任务可以怎样使用 |
|---|---|
| 低影响、可逆且可快速验证 | 继续执行，同时验证 |
| 中等影响或会扩大修改范围 | 显式记录，在 Checkpoint 前验证 |
| 高影响、不可逆或涉及数据／发布 | 阻断依赖动作，或请求有权角色裁决 |

这不是固定的 Low/Medium/High 成熟度模型。风险阈值应由项目 Policy、影响和当前 Authority 决定。

## Assumption Resolution（假设处置）不应改写历史

原稿使用了“Assumption Promotion”这一表达，容易让人理解成把一条假设原地升级为 Truth。更稳妥的记录方式是：

```text
Assumption ASM-009 remains as historical input
Evidence EV-021 evaluates it
A scoped State Claim is created or updated
ASM-009 resolution becomes supported / refuted / still-unresolved
ASM-009 lifecycle becomes closed or expired when applicable
```

如果 Evidence 只覆盖部分样本，新的 Claim 也只能 `verified-for-scope`。如果假设被反驳，应按对象类型处理依赖：State Claim 重新验证，Plan 重新评估，Decision 重新审议或 supersede，尚未执行的动作重新授权。历史记录本身不应被删除。

小型任务可以把这些字段压缩成一句带 Owner 和验证条件的工作说明。只有假设具有高影响、跨任务复用、长期有效或多个依赖者时，才值得持久化完整记录。

---

# 6.7 Evidence 先说明观察了什么，再支持 Claim

一张 1920×1080 runtime capture 不是 Claim；“Stage / Limit 在目标战斗场景中被 HP 层级压制”才是 Claim。即使二者关联，仍要记录截图绑定的 Build/Commit、场景与反例范围，区分机器测量和人工审美判断，并说明最终体验裁决权属于谁。

所以关系是：

```text
Evidence
    supports / contradicts
Claim

Validation Rule
    updates declared coverage

Authorized Role or Delegated Gate
    creates a Decision Record
Decision Record
    targets a named Decision Target
    records a Target-specific Disposition
```

但在判断 Evidence 支持什么之前，还要先回答三个问题：

- **Evidence Generation Integrity（证据生成过程是否维持声明的观察边界）**：验证器、脚本或 Agent 是否以已声明、受隔离的方式工作，且没有静默改变本次要观察的对象；
- **Target Observation Status（目标观察状态）**：目标是否真的执行并形成了可识别的观察；
- **Target Result（前向引用）**：第8章正式定义在具名 Attempt、观察对象与 Scope 下形成的目标结果；本章只读取它来判断 Evidence 实际支持什么。

按第8章拥有的 Outcome / Result 语义，如果验证器在观察目标前失败并阻断目标执行，就只能得到关于验证器的结果；缺席的 Target Result 必须记录为 `non-result`（没有形成目标判定结果），不能写成 PASS 或 FAIL。

如果验证器改变了 authority-bearing input/surface（会影响目标身份、授权或解释边界的输入／表面），但目标随后仍被执行和观察，则不能机械记录为 `non-result`。系统应记录实际 `observed_subject`，并说明该结果为何不能支持原预期对象的 Claim。Integrity 也不等于绝对没有副作用：已声明、被隔离且不改变观察对象的正常输出不自动构成失败。

一个最小 Evidence Record 可以显式保存：

```text
observed_subject
observation_status
generator_integrity
target_result
intended_use
scope / revision / timestamp
provenance / evidence links
```

这些字段分别回答：实际观察了谁、观察是否完成、生成过程是否保持观察边界、目标得到什么结果、Evidence 准备用于什么决策。它们是一组候选问题，不是统一 Schema。对于观察前被阻断的运行，应拆开记录：

```text
generator_integrity = compromised
observation_status = target-not-observed
target_result = non-result
```

部分观察必须保留实际 Scope，不能提升为完整目标结果。即使生成过程完整且测试 PASS，也只说明声明范围内的检查通过；`qualified-for-use` 仍须结合 `intended_use` 和相应 Acceptance Authority 判断。普通 Validation Rule 只更新覆盖状态；只有获得明确委托的自动 Gate，才可以对限定的 Decision Target 同时作出处置。

Provenance 至少应记录 Source、Producing Activity、Responsible Agent/Tool/Human、Timestamp、Revision、Scope，以及它是 Derivation 还是 Primary Source。

这些思想并不是 AI 时代才出现。W3C PROV 已经区分 Entity、Activity、Agent、derivation、revision 和 primary source。本书在此关注的是：怎样把这些已有概念接入 Agent 的 Context、Execution 和 Evidence 链路。

同理：

> Agent 可以提交 Claim，但 Agent 的语言确信度不能赋予 Claim 项目权威。

真正需要区分的是三种权限：

- **State Mutation Authority（状态修改权）**：谁能改变代码、配置、数据或部署状态；
- **Claim Assertion Authority（主张提交权）**：谁能提交某类 Claim 或 Observation；
- **Claim Use Disposition Authority（主张用途裁决权）**：谁能针对具名 Decision Target，允许、拒绝或延后将 Claim 作为当前任务的依赖依据。

Test 和 Monitoring 产生 Evidence；Git/Merge 改变 Repository State；授权人作出 Normative Decision。它们不以同一种方式“写 Truth”。

SP122 的结果包展示了这种区分：machine checks 通过、qualifying evidence chain 被人类接受，并没有同时授权 supported adoption 或 production release。[SP122 结果包案例记录](../Evidence/receipts/ER-20260810-002__CLM-C06-002.md)

v4.94 的 D-079 又给出一个更窄的接口例：候选实现的 42 项 focused tests 通过，但 Human 仍拒绝其超出 E1 所需的实现与验证范围；后续前向修正删除了 262 行，只保留当前契约与 8 个回归用例。PASS 证明的是所选检查在该候选上通过，不证明额外范围必要，也不自动完成 Acceptance、Adoption 或 Release。完整的 Evidence Use 与 Decision Disposition 边界由第9章展开。[D-079 测试与范围裁决记录](../Evidence/receipts/ER-20260818-003__CLM-C09-001.md)

---

# 6.8 冲突解析的目标不是制造唯一答案

多个来源冲突时，系统可以依次检查：

1. 当前问题属于哪个 Domain？
2. 各来源的 Scope、Version 和时间是否相同？
3. 哪个来源对该问题具有声明 Authority？
4. 是否存在直接 Observation 或适用的验证规则？
5. 新来源是否明确 supersede 旧来源？
6. 冲突能否在当前风险等级下自动解决？

常见策略包括：

## Authority-based（按权威解析）

适用于规范性 Decision 或具有明确所有者的状态来源。

## Version/Freshness-based（按版本与时效解析）

适用于同一来源、同一 Scope 的连续版本，但“更新”不能自动覆盖明确保留的旧兼容状态。

## Evidence-based（按证据解析）

适用于可观察行为。例如实际 Runtime Capture 可以反驳“当前没有重叠”。

## Human or Authorized Arbitration（人工或授权仲裁）

适用于产品方向、体验、风险接受和 Policy 冲突。

## Preserve Conflict（保留未解决冲突）

当证据不足或来源分属不同 Scope 时，最可靠的输出可能是：

```text
Conflict unresolved
Dependent action blocked or narrowed
```

存在高冲突或高错误成本的系统，不需要永远给 Agent 一个确定答案。

它需要让 Agent 知道：

```text
verified for scope
partially supported
assumed
unknown
conflicted
superseded
```

---

# 6.9 Context Manifest、State Snapshot 与 Execution Baseline

这三个对象容易混淆。

## Context Manifest（上下文清单：本次实际提供的信息记录）

回答：

> 本次向 Agent 装配、传输或开放访问了哪些信息？

```text
Context Pack ID
Source references
Versions / hashes
Selection reason
Omitted categories
Freshness checks
Observable access records, if available
```

Manifest 不证明模型注意、理解或使用了其中每一项。若工具能够记录实际读取行为，应把 Access Log 作为另一类可观察过程证据，而不是把它等同于模型认知状态。

## State Snapshot

回答：

> 在声明的 Domain、Scope、采集时间和能力边界内，记录了哪些状态观察、Claim 与引用？

某个 Feature Flag 可能没有进入 Snapshot，也可能没有提供给 Agent；这都不表示它不存在。Snapshot 是有界记录，不是项目本体。

## Execution Baseline Manifest

回答：

> 本次任务被授权依赖哪些 State、Intent、Decision、Policy 和 Assumption？

三者的关系可以表示为：

```text
State Snapshot reference       bounded state observations
Context Manifest reference     supplied information record
Intent / Decision references   desired and normative basis
Assumption references          explicit unknowns
Evidence Baseline references   pre-existing evidence, if relevant
            ↓ typed-reference assembly
Execution Baseline Manifest    authorized dependency index
            ↓ referenced by
Execution Contract
```

Execution Baseline Manifest 只装配 typed references，不复制全部 Context、Evidence、环境字节或运行记录。这里的 `Evidence Baseline` 只指执行前已经存在、并被本次任务引用的 Evidence；它不是对未来验证结果的预先裁决。

Execution Contract 在下一章正式定义；本章只前向引用它如何服从现有 Authority Grant，并描述本次执行的允许动作、边界和结束条件：

- Agent 可以做什么；
- 不能做什么；
- 何时必须升级；
- 需要产生什么 Evidence；
- 什么条件允许结束执行。

## State Boundary（Execution Baseline 中的状态边界字段）与 Dirty Worktree

State Boundary 不是与 Execution Baseline 并列的新对象。它是 Baseline 中回答以下问题的一组字段或视图：

> 当前任务被允许从哪个 Repository、Build、Runtime、Data 和 Configuration 状态开始？

对代码任务，最低限度通常包括：

```text
baseline commit / branch
worktree identity
dirty changes
task ownership or provenance
protected or unrelated changes
```

Dirty Worktree（含有尚未提交变化的工作树）不能只被压成 `dirty = true`。Agent 至少要区分：

```text
current-task changes
known user / other-agent changes
temporary experiment
unknown ownership
```

可选处置包括：

- **Block**：变化与当前任务重叠，且继续执行可能覆盖或错误归因；
- **Isolate**：为任务使用独立 Worktree、Branch 或临时环境；
- **Snapshot**：记录当前差异、来源和 Baseline，再继续限定范围的工作；
- **Declare unrelated**：明确无关变化并保护其文件范围，不把它们纳入当前完成声明。

系统不应因为 Agent 想获得“干净状态”，就自动清理、覆盖或把未知变化归入自己。Dirty State 首先是 Provenance 与 Authority 问题，其次才是 Git 操作问题。

Worktree 可以建立 Repository State Boundary，但它不会自动提供：

- 正确 Intent；
- Runtime/Data/Configuration 状态；
- Decision Authority；
- Evidence Coverage；
- Review 独立性。

因此，Worktree 是一种隔离机制，不是完整的 State Architecture。

## Drift（基线与当前状态的偏移）必须按 Domain 解释

同一份代码在不同 Build、配置、环境或数据上可能产生不同结果。State Snapshot 应保存可识别这些差异的引用，而不是假设 Repo 代表全部现实。

| State Surface | 需要绑定的信号 | 忽略时的典型错误 |
|---|---|---|
| Repository | Commit、Branch、Dirty Changes | 在错误源基线上修改或归因 |
| Build / Deployment | Artifact identity、source revision | 把尚未部署的代码当成用户行为 |
| Configuration | Effective config、Feature Flags | 代码能力与实际启用状态混淆 |
| Environment | OS、Engine/Dependency、Tool versions | 在不同执行条件间错误外推 |
| Data | Schema/Data version、migration history | 用代码声明替代真实数据状态 |

Data 任务往往具有更高不可逆性。涉及 Save、Database、Migration 或用户数据时，Snapshot 还可能需要：

```text
schema / data version
representative samples
backup identity
migration history
rollback capability
```

这些字段不是所有任务的固定清单。它们只在对应 Domain 会改变结论或错误成本时进入 Baseline。

Saved Baseline 与 Current Observation 不一致也不自动等于失败。差异可能来自预期变更、并发任务、过期 Snapshot 或错误环境。系统应先确定 Scope 和 Provenance，再选择 revalidate、rebase、narrow、block 或请求裁决。

## Risk-based State Readiness（按风险检查执行起点）

当任务涉及相应 State Surface、不可逆动作或较高错误成本时，需要判断当前 Baseline 是否足以支撑即将执行的动作。这里不再创建独立的 `Truth Readiness Gate` 和 `State Readiness Gate`；下面只是一组按 Domain 与风险选择的候选问题，不是通用 Gate：

```text
Baseline identified?
Dirty changes understood?
Target build / runtime known?
Relevant data and config known?
Active decisions still effective?
High-impact assumptions unresolved?
Rollback or recovery available?
Required observation path available?
```

检查失败后的动作取决于当前危险和已授权 Policy，而不是机械升级治理：

- 基线未知且动作不可逆：Block；
- 只缺少某个行为 Claim：缩小任务或先收集 Observation；
- Assumption 可逆且低影响：记录后执行并验证；
- Decision Authority 不清：进入已授权的 Block、Evidence Collection 或 Escalation 路径；
- Snapshot 过期但差异可解释：重建 Baseline 或 revalidate。

以 Save Migration 为说明性场景：如果代码中存在 v2→v3 migration，但生产 Save 分布、代表性样本和 rollback capability 未知，那么“migration path exists”可以是 Repository Claim，却不足以授权生产数据迁移。系统应保留未知、收集数据 Evidence，或阻断不可逆动作，而不是把代码存在改写为数据已经安全。

这个例子用于解释对象关系，不声称对应一个已经完成的仓库任务。

## State Compression 与 State Index 的类型边界

State Snapshot 经常需要被压缩，但摘要可能删除决定结论是否仍然成立的条件。

例如：

```text
State Claim:
Migration compatibility path A is active for build v3
until migration B reaches the declared completion condition.
```

不能被压缩成：

```text
Compatibility path A is active.
```

State Summary 至少要保留对当前判断有影响的：

```text
Scope
Version / Time
Condition / Expiry
Source / applicable authority
Known Conflict
Reference to primary record
```

长期项目可以维护一个很小的 State Index（当前关键状态及其来源的导航索引）：

```text
active state snapshot
repository / build / runtime / data / config identities
high-impact state claims
known conflicts and stale claims
links to evidence and primary records
```

State Index 不是全文 Archive，也不是复制全部 Evidence 的 Truth Registry。它只帮助人或 Agent 定位当前高影响 Claim，再按需下钻。

Active Decision 和 Open Assumption 仍由 Execution Baseline 引用，不能因为它们对执行重要，就被静默改写成 State Index 中的描述性状态。

第五章负责决定哪些索引项进入当前 Context，以及如何压缩、检索和展开；第六章只规定压缩不能把 Decision、Assumption 或 Evidence 静默改写成 State Claim，并解释条目的 Authority、Freshness 和冲突。换句话说：

```text
State Index       where current state records can be found
Context Manifest  which references were supplied in this run
```

低风险短任务通常不需要持久化 State Index。只有跨 Thread、长生命周期、多 Agent 或高状态重建成本的工作，才值得承担维护成本。

---

# 6.10 目标是外部决策环境的可追踪与有限重建

Agent 执行具有概率性。

即使保存相同 Prompt，也不保证重现相同路径。

而隐藏推理既不是项目可以可靠读取的工程对象，也不应该成为审计依赖。

更现实的目标是保存足够引用，使后来者能够追踪并在条件允许时有限重建：

```text
Intent Version
Execution Baseline Manifest
Context Contract + Manifest
Agent Contract / Policy
Model / Tool / Runtime Versions
Input State
Evidence Requirements
```

本书将这个目标称为：

> **Decision Environment Traceability（外部决策环境的可追踪性）与 Reconstructability Goal（有限重建目标）。**

它不承诺：

> 再跑一次一定产生同一输出。

它希望提高的是：

> 后来的人或 Agent 能定位当时的目标、状态、信息和授权，识别缺失条件，并在可用材料范围内重新检查原结果是否仍然适用。

现有实践支持这个较窄结论。SP122 保存了预执行 plan commit、修复 revision、lane authority、runtime identities、machine checks、Human review 和 artifact hashes；Anthropic 与 OpenAI 的长任务实践也强调显式 progress/state artifacts 与版本化 execution plans。但这些来源没有证明固定 Schema 能保证恢复成功。[SP122 可追踪决策环境案例记录](../Evidence/receipts/ER-20260810-003__CLM-C06-003.md)

因此本章采用：

> Preserve a traceable external decision environment, not hidden reasoning.

即：保存可检查的外部决策依据，尽可能支持有限重建，而不是试图保存或复现隐藏推理，也不保证恢复一定成功。

---

# 6.11 Freshness（时效性）、Invalidation（失效）与 State Transition（状态迁移）

一条 State Claim 在产生时可能正确，后来却不再适用。

例如：

```text
Claim:
All migration tests pass.

Scope:
commit abc123 + test environment E1
```

当代码、数据或环境的变化触及这条 Claim 已声明的依赖、Scope 或观察条件时，它不必变成 False，但对当前 Baseline 的适用关系应变成：

```text
not established for current baseline
```

这不抹除 Claim 对历史 Baseline 的有效性。需要区分 `historical validity` 与 `applicability to current baseline`。

常见 Invalidation Trigger（失效触发条件）包括：

- 依赖 Source 发生变化；
- Scope 或 Version 不再匹配；
- Claim 所依赖的 Decision 被 supersede；
- Claim 所依赖的 Assumption 到期或被反驳；
- 新 Evidence 与旧 Claim 冲突；
- 与 Claim 适用范围相关的 Runtime/Data/Configuration 发生状态迁移。

因此一个经过验证的 Agent Task 不只是：

> Done。

更准确是：

```text
Input State Snapshot
+ Authorized Change
+ Evidence
+ Conflict / Assumption Update
        ↓
Output State Claims
+ Evaluation Result
+ Evidence Use Disposition
```

Git Commit 是 Repository Domain 中很强的 State Transition，但它不自动记录：

- Deployment；
- Runtime；
- Data；
- Human Acceptance；
- Evidence Scope。

高风险任务才可能需要 Claim Dependency Graph：

```text
Claim A depends on Claim B + Evidence C
```

B 的当前适用性失效后，只有在依赖关系明确时，A 才进入 `needs revalidation`。

小型任务不需要先建图。直接检查当前文件、执行验证并记录结果通常足够。

---

# 6.12 两个已取证案例

## 案例一：SP122 Authority Conflict

以下内容来自版本化工程产物，不是对隐藏推理的重建。

### 可观察事实

- authority audit 同时保留了 active、superseded 和 conflicted sources；
- 一个实现 commit 被保留为 Implementation Evidence，但被拒绝为当前 Design Authority；
- audit 保存了历史上 stale/conflicted rule 影响 runtime presentation 和 machine-PASS surface 的事件；
- 后续 Human review 只接受 qualifying evidence chain，没有批准 supported adoption 或 production release。

### 同期判断

- Reviewer 判定当前 authority 已解决；
- Human Lead 接受 R2 evidence chain，并明确限制接受范围。

### 本书推导

- 同一来源对不同问题可能具有不同 Authority；
- Implementation、Evidence Validation 与 Adoption Decision 必须分开；
- 历史冲突不能因当前修复完成而被重写。

### 限制

- 这是一个项目、一个 UI 生命周期规则案例；
- 它不能证明所有项目需要 Truth Registry；
- 它没有提供“使用对象模型前后”的成本对照。

完整来源与反证见 [SP122 authority-audit 案例记录](../Evidence/receipts/ER-20260810-001__CLM-C06-001.md) 和 [SP122 结果包案例记录](../Evidence/receipts/ER-20260810-002__CLM-C06-002.md)。

## 案例二：D-048 Verifier Self-mutation（验证器自我修改）

以下内容来自 AI Game Dev OS v4.94 的已提交 incident 与 corrective review，不是对目标代码结果的事后猜测。

### 可观察事实

- D-048 launcher 在目标 compile harness 执行前进行了普通 Python import；
- import 在 authority-bearing manifest surface 中生成了 `__pycache__` 与两个 `.pyc` 文件；
- 第二次 exact-inventory check 检测到变化并 fail closed；
- 目标 runtime directory 与 compile result 都没有产生。

### 同期判断与修正边界

- Review 将其判定为 manifest self-mutation defect，并保留失败现场；
- corrective request 提议使用 `python -I -B -S -c`、显式禁止 bytecode，并在执行前后检查 exact inventory；
- 该 request 没有授权或完成目标重试，因此它是修正方案记录，不是成功的 target result。

### 本书推导

这次运行产生了一条关于验证器的有效 Claim：Evidence generator 改变了自己的 authority-bearing surface。它没有产生关于目标 compile 是否通过的 Claim。

因此应记录为：

```text
observed_subject = verifier
generator_integrity = compromised
observation_status = target-not-observed
target_result = non-result
```

exact-inventory check 本身并未失效；它检测到了真实变化。直接工程缺陷是 verifier self-mutation；在结果记录层面，还存在把验证器失败、目标失败和目标未观察混成同一种结果的风险。

后一条是本书从事故中提取的对象边界，不是对直接故障原因的替代描述。

### 限制

- 这是一个 Python bytecode 副作用造成的单一案例；
- 它不证明验证器必须完全无副作用；
- 已声明并隔离的正常输出不自动构成 Integrity failure；
- 当前取证没有重跑历史 harness，修正方案的运行效果不能从该 incident 单独推出。

完整来源、反证与人工收窄边界见 [D-048 验证器自我修改案例记录](../Evidence/receipts/ER-20260818-002__CLM-C06-004.md)。

---

# 6.13 按风险裁剪持久化强度

Truth and State Architecture 的目标不是最大化元数据。

治理本身是成本。

以下三组只用于说明可能的裁剪方式，不是新的治理等级，也不由任务时长或 Agent 数量单独决定。

## 低风险、局部且易恢复的任务

通常只需要：

```text
Current file / repo state
Clear scope
Simple verification
```

## 存在跨文件依赖或状态分歧的任务

可能需要：

```text
Intent reference
Commit / branch / dirty state
Active decisions
Open assumptions
Tests / evidence
```

## 高影响、难恢复或存在多方 Authority 的任务

更可能需要考虑：

```text
State Snapshot
Execution Baseline Manifest
Typed Claims
Authority Matrix
Context Manifest
Invalidation
Independent Review
Rollback
```

工程适配度不是：

> Registry 越多、Graph 越大、Gate 越重。

而是：

> 能按问题风险，以足够低的成本确定当前状态、暴露未知和冲突，并阻止未经授权的 Claim 变成执行依据。

---

# 6.14 本章结论

Intent Engineering 解决：

> 我们希望未来达到什么状态？

Context Engineering 解决：

> Agent 当前应该接触哪些信息？

Truth and State Architecture 解决：

> 这些信息分别是什么类型，它们在什么问题、范围、版本和时间中可以被依赖？

本章的核心不是建立唯一 Source of Truth，而是建立可检查的关系：

```text
Intent                  desired state
Decision / Policy       normative content under authority
State Claim             described current state
Assumption              explicit unknown
Evidence / Provenance   observed basis and generation boundary
Context Manifest        information actually supplied
Execution Baseline      authorized starting bundle
```

最终原则是：

> **Agent 不需要一个看起来没有矛盾的世界；它需要一个知道哪些是状态、哪些是决定、哪些是假设、验证器实际观察了什么、哪些证据只支持有限范围、哪些冲突仍未解决的工程环境。**

有了这层区分，第7章才能讨论 Agent 如何在明确 Intent、Context、State 与 Authority 下打开 Execution Contract，形成有身份的 Attempt 与可观察动作／状态；第8章再分类 Attempt Outcome、Target Result 与 Evaluation Result，第9章判断这些记录怎样成为 Evidence 并进入有权处置。State Transition 不能由执行动作或 Test PASS 直接推出。

---

# 本章原则

1. **Store Claims, not “Truth objects”。** 系统管理可修订 Claim 及其依据。
2. **Source of Truth 需要授权来源与适用边界。** Authority Grant 由被组织承认的 Owner / Role / Grantor 在制度或 Delegation 基础上签发，并可引用 Policy；Policy 是规范性约束，不自动等于 Grant。Question、Domain、Scope、Version 和 Time 限定其 Applicability。
3. **Intent、Decision、State Claim、Assumption、Evidence 的语义必须可区分。** 是否物理拆分由风险、生命周期和复用需要决定。
4. **先确认 Evidence 实际观察了什么。** 观察边界、目标观察状态与目标结果必须分开。
5. **Evidence supports Claims。** 范围内验证与用途资格、采用、发布不是同一状态。
6. **Provenance before confidence。** 来源和验证边界优先于语言确信感。
7. **State Snapshot 不包含全部工作语义。** Decision 与 Assumption 通过 Execution Baseline 引用；Dirty State 与 Drift 必须显式记录。
8. **Preserve Unknown and Conflict。** 不确定性不是必须被模型补全的空白。
9. **Preserve a traceable external decision environment。** 保存可检查依据并支持有限重建，不依赖隐藏推理完成审计。
10. **Agent may assert; authorized decisions dispose named uses。** 断言权、状态修改权和对具名 Decision Target 的用途裁决权需要分开。
11. **Governance should fit risk。** Registry、Graph 和 Gate 都是可选机制。

---

# 常见反模式

## 反模式一：One Source of Truth for Everything

同一个来源无法同时回答实现、运行、数据和产品授权问题。

## 反模式二：把所有状态塞进一个 Status 字段

验证、生命周期、授权和冲突必须是不同维度。

## 反模式三：Decision Truth / Evidence Truth

Decision 是规范性记录；Evidence 是支持材料。二者不应伪装成描述性 State Domain。

## 反模式四：Agent 说得确定，所以写入 Truth Registry

语言流畅度和模型 confidence 不产生项目 Authority。

## 反模式五：Snapshot 等于完整聊天记录

Snapshot 保存状态与引用；聊天记录只是一种过程证据。

## 反模式六：为了可靠，把所有 Claim 都注册

只有高影响、高复用、高冲突或高时效性的 Claim 值得长期治理。

## 反模式七：当前修复完成，就删除历史冲突

历史缺陷仍然是解释系统演化和防止复发的重要 Evidence。

## 反模式八：测试通过等于产品批准

机器验证、范围必要性、体验裁决、采用和发布属于不同决策面。D-079 的 42 项测试通过，并没有使被 Human 拒绝的额外实现范围自动成为必要范围。

## 反模式九：验证器失败等于目标失败

如果失败发生在目标观察之前并且目标没有形成观察，应分别记录 Evidence generator 的失败和目标的 `non-result`，不能虚构目标 FAIL。若目标在改变后的输入上被观察，则记录实际观察对象和适用范围。

---

# 本章检查清单

- 当前问题是什么，而不是“整个项目什么是真的”？
- 它属于哪个 State Domain？
- Authority Grant 由哪个 Owner、Role 或 Grantor 在什么制度、Policy 或 Delegation 基础上签发？它对当前问题是否适用？
- Claim 绑定哪个 Scope、Version、Time 和环境？
- 这是 Intent、Decision、State Claim、Assumption 还是 Evidence？
- Evidence 如何产生，生成过程是否改变了观察边界或 authority-bearing surface？
- 实际被观察的是目标、验证器，还是二者？
- 未观察目标时，是否明确记录为 `non-result`，而不是 PASS 或 FAIL？
- Evidence 能支持多大范围，预期用于哪一种决策？
- `verified-for-scope` 是否被误写成 `qualified-for-use`？
- 是否存在 Counterevidence 或替代解释？
- Observed、Derived、Verified、Approved、Stale 是否被错误塞进同一状态轴？
- 当前 Repository State 是否包含 Dirty Worktree？
- Dirty Changes 的来源、所有者、重叠范围和处置是否明确？
- Runtime、Data、Configuration 是否可能与 Repo 不同？
- 高风险或不可逆动作是否具备可识别 Baseline、恢复路径和实际 Observation 路径？
- Decision 是否已经 Superseded 或过期？
- Assumption 是否拥有风险、Owner、验证路线和 Expiry？
- 冲突能否自动解决，还是必须保留或升级？
- Agent 有权修改 State、提交 Claim，还是裁决 Claim？
- Context Manifest 是否记录本次装配、传输或开放访问的信息，而没有声称模型必然注意了它？
- State Snapshot 是否明确声明 Domain、Scope、Time 和采集边界，并与 Context Manifest 分开？
- Execution Baseline 是否分别引用 State、Intent、Decision 和 Assumption？
- State Summary / Index 是否保留 Scope、Version、Condition、Expiry、Source 和已知冲突？
- 任务结束后，哪些旧 Claim 应失效或重新验证？
- 是否能从 Input State、Change、Evidence 重建 Output State？
- 当前任务真的需要 Registry/Graph，还是简单验证已经足够？
