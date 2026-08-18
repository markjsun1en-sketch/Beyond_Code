# 第6章 Truth and State Architecture
## 在 Claim、State、Decision 与 Assumption 之间建立可验证秩序

> 工作稿状态：等待作者裁决，不替代 `OringinalDocs/第6章.md`。  
> 结构审阅：[RR-010](../RevisedResult/RR-010_第六章Truth与State_Architecture.md)  
> 核心 Claim：`CLM-C06-001`、`CLM-C06-002`、`CLM-C06-003`、`CLM-C06-004`；关联边界：`CLM-C09-001`。
> Evidence：五条 Claim 的证据边界均已在 Receipt 中记录；`CLM-C06-004` 与 `CLM-C09-001` 已由作者接受并收窄，正文只采用收窄后的范围。
> 本轮证据回接：[RR-015](../RevisedResult/RR-015_第六章Evidence_Generation与Non-result回接.md)
> 术语标注：遵循已接受的 [RR-013](../RevisedResult/RR-013_双语术语标注规范.md)，核心英文术语仅在首次正式定义时补充中文语义。

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

本章所说“当前可依赖的事实”，应理解为：

> 在一个明确问题、版本、范围和时间窗口中，经过适当来源与证据支持，当前被授权用于工程决策的 State Claim。

它必须允许以后被：

```text
revalidated
superseded
expired
conflicted
rejected
```

如果一个系统只能写入 Truth，却不能表达“不知道”“存在冲突”或“曾经成立”，它更容易制造确定性幻觉。

---

# 6.2 五类记录必须分开

第六章首先需要建立的不是更多 Truth Domain，而是五类不同工程对象。

## Intent Artifact（意图资产：可版本化的期望结果记录）

表达：

> 希望未来达到什么状态，以及为什么。

例如：

> 旧版 Save 应能安全迁移到当前版本。

Intent 描述 Desired State（期望达到的状态），不证明系统已经做到。

## Decision / Policy Record（决策／策略记录：当前规范性授权）

表达：

> 当前被授权采用什么规则、方案或约束。

例如：

> 在 v1.0 前不得移除旧 Save 兼容层。

Decision 是 Normative Authority（规定当前应该如何行动的授权）。它规定应该怎样行动，不描述系统物理上已经怎样运行。

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

五者之间的基本关系是：

```text
Intent              desired outcome
Decision / Policy   normative authority
State Claim         description of state
Assumption          explicit unknown used for work
Evidence            support or counterevidence
```

它们不能因为出现在同一文档、同一 Context Pack 或同一句自然语言里就静默转换。

---

# 6.3 State Claim 需要正交元数据

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
- Stale 描述生命周期；
- Rejected 描述处置结果。

更稳妥的 State Claim 可以使用多个正交轴。

```text
Claim ID
Statement

Subject Domain
Scope
Version / State Reference

Epistemic Basis
Validation Status
Lifecycle Status
Disposition

Provenance
Evidence Links
Owner / Authority
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
test-verified
inferred
reported
```

一条 Derived Claim 仍然可以经过验证，因此 `derived` 与 `verified` 不应互斥。

## Validation Status（验证覆盖状态）

回答：

> 当前验证覆盖到什么程度？

例如：

```text
unverified
partial
verified-for-scope
counterevidence
unresolved
```

其中，`verified-for-scope` 只表示证据覆盖了已声明的 Claim 与范围。它不等于 `qualified-for-use`（已经满足某个具体用途的资格条件）。后者还取决于预期用途、风险等级、适用 Gate，以及谁拥有接受该用途的 Authority。

## Lifecycle Status（生命周期状态）

回答：

> 这条 Claim 现在还适用吗？

例如：

```text
active
stale
superseded
expired
```

## Disposition（有权角色作出的当前裁决）

回答：

> 有权角色或机制如何处理它？

例如：

```text
proposed
accepted-for-use
rejected
conflicted
```

这些维度组合后，系统才能表达：

> 这是一条关于 Runtime 的推导性 Claim，证据覆盖部分成立，当前版本仍 Active，但与另一条观测存在未解决冲突。

而不是被迫把它压成：

> True。

---

# 6.4 Source of Truth（针对特定问题的优先权威来源）必须绑定问题

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

可以建立一个最小 Authority Matrix（问题—权威来源矩阵）：

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

因此：

```text
Authority
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

关于这一点，现有证据只能支持有限范围。SP122 的 authority audit 显示：实现 commit 对“实际实现了什么”有描述价值，但不能覆盖已经批准的设计方向；历史冲突也必须被保留。[ER-20260810-001](../Evidence/receipts/ER-20260810-001__CLM-C06-001.md)

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

成熟系统则使用 Typed Records 和 Domain-scoped Authority。

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

因此 State Snapshot（状态快照：某时点可观察项目状态的引用集合）只描述状态：

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

---

# 6.7 Evidence 先说明观察了什么，再支持 Claim

一张 1920×1080 runtime capture 不是 Claim；“Stage / Limit 在目标战斗场景中被 HP 层级压制”才是 Claim。即使二者关联，仍要记录截图绑定的 Build/Commit、场景与反例范围，区分机器测量和人工审美判断，并说明最终体验裁决权属于谁。

所以关系是：

```text
Evidence
    supports / contradicts
Claim
    accepted for a scope by
Authority / Validation Rule
```

但在判断 Evidence 支持什么之前，还要先回答两个问题：

- **Evidence Generation Integrity（证据生成过程自身的完整性）**：验证器、脚本或 Agent 是否保持了声明的观察边界；
- **Target Observation Result（对目标实际得到的观察结果）**：目标是否真的执行并被观察。

如果验证器在观察目标前失败，且阻断目标执行或改变 authority-bearing input/surface，就只能得到关于验证器的结果；缺席的目标结果必须记录为 `non-result`（没有形成目标判定结果），不能写成 PASS 或 FAIL。Integrity 不等于绝对没有副作用：已声明、被隔离且不改变观察对象的正常输出不自动构成失败。

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

这些字段分别回答：实际观察了谁、观察是否完成、生成过程是否完整、目标得到什么结果、Evidence 准备用于什么决策。它们是一组最小问题，不是统一 Schema。对于观察前被阻断的运行，应拆开记录：

```text
generator_integrity = compromised
observation_status = target-not-observed
target_result = non-result
```

部分观察必须保留实际 Scope，不能提升为完整目标结果。即使生成过程完整且测试 PASS，也只说明声明范围内的检查通过；`qualified-for-use` 仍须结合 `intended_use` 和相应 Acceptance Authority 判断。

Provenance 至少应记录 Source、Producing Activity、Responsible Agent/Tool/Human、Timestamp、Revision、Scope，以及它是 Derivation 还是 Primary Source。

这些思想并不是 AI 时代才出现。W3C PROV 已经区分 Entity、Activity、Agent、derivation、revision 和 primary source。本书的增量不是重新发明 provenance，而是把它接入 Agent 的 Context、Execution 和 Evidence 链路。

同理：

> Agent 可以提交 Claim，但 Agent 的语言确信度不能赋予 Claim 项目权威。

真正需要区分的是三种权限：

- **State Mutation Authority（状态修改权）**：谁能改变代码、配置、数据或部署状态；
- **Claim Assertion Authority（主张提交权）**：谁能提交某类 Claim 或 Observation；
- **Claim Disposition Authority（主张裁决权）**：谁能批准、拒绝、标记冲突，或使 Claim 成为当前任务可依赖的记录。

Test 和 Monitoring 产生 Evidence；Git/Merge 改变 Repository State；授权人作出 Normative Decision。它们不以同一种方式“写 Truth”。

SP122 的结果包展示了这种区分：machine checks 通过、qualifying evidence chain 被人类接受，并没有同时授权 supported adoption 或 production release。[ER-20260810-002](../Evidence/receipts/ER-20260810-002__CLM-C06-002.md)

v4.94 的 D-079 又给出一个更窄的边界：候选实现的 42 项 focused tests 通过，但 Human 仍拒绝其超出 E1 所需的实现与验证范围；后续前向修正删除了 262 行，只保留当前契约与 8 个回归用例。PASS 证明的是所选检查在该候选上通过，不证明额外范围必要，也不自动完成 Acceptance、Adoption 或 Release。[ER-20260818-003](../Evidence/receipts/ER-20260818-003__CLM-C09-001.md)

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

成熟系统不需要永远给 Agent 一个确定答案。

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

> Agent 这次实际看到了什么？

```text
Context Pack ID
Source references
Versions / hashes
Selection reason
Omitted categories
Freshness checks
```

## State Snapshot

回答：

> 项目在某个时间点处于什么可观察状态？

Agent 可能没有看到某个 Feature Flag；它仍然属于 State，但不属于该 Agent 的 Context。

## Execution Baseline Manifest

回答：

> 本次任务被授权依赖哪些 State、Intent、Decision、Policy 和 Assumption？

三者的关系可以表示为：

```text
State Snapshot             project state
Context Manifest           supplied information
Intent / Decision / Policy normative references
Assumptions                explicit unknowns
        ↓
Execution Baseline Manifest
        ↓
Execution Contract
```

Execution Contract（执行契约：规定本次执行权限、边界和结束条件）在下一章处理：

- Agent 可以做什么；
- 不能做什么；
- 何时必须升级；
- 需要产生什么 Evidence；
- 什么条件允许结束执行。

---

# 6.10 可复现的目标是外部决策环境

Agent 执行具有概率性。

即使保存相同 Prompt，也不保证重现相同路径。

而隐藏推理既不是项目可以可靠读取的工程对象，也不应该成为审计依赖。

更现实的目标是重建：

```text
Intent Version
Execution Baseline Manifest
Context Contract + Manifest
Agent Contract / Policy
Model / Tool / Runtime Versions
Input State
Evidence Requirements
```

这可以称为：

> **Decision Environment Reproducibility（外部决策环境的可重建性）。**

它不承诺：

> 再跑一次一定产生同一输出。

它承诺的是：

> 后来的人或 Agent 能知道当时在什么目标、状态、信息和授权下执行，并能重新检查原结果是否仍然成立。

现有实践支持这个较窄结论。SP122 保存了预执行 plan commit、修复 revision、lane authority、runtime identities、machine checks、Human review 和 artifact hashes；Anthropic 与 OpenAI 的长任务实践也强调显式 progress/state artifacts 与版本化 execution plans。但这些来源没有证明固定 Schema 能保证恢复成功。[ER-20260810-003](../Evidence/receipts/ER-20260810-003__CLM-C06-003.md)

因此本章采用：

> Reconstruct the external decision environment, not hidden reasoning.

即：重建可检查的外部决策环境，而不是试图保存或复现隐藏推理。

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

代码、数据或环境一旦变化，这条 Claim 不必变成 False，但应变成：

```text
stale for current state
```

常见 Invalidation Trigger（失效触发条件）包括：

- 依赖 Source 发生变化；
- Scope 或 Version 不再匹配；
- Decision 被 supersede；
- Assumption 到期；
- 新 Evidence 与旧 Claim 冲突；
- Runtime/Data/Configuration 发生状态迁移。

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
+ Verification Disposition
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

B 失效后，A 进入 `needs revalidation`。

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

完整来源与反证见 [ER-20260810-001](../Evidence/receipts/ER-20260810-001__CLM-C06-001.md) 和 [ER-20260810-002](../Evidence/receipts/ER-20260810-002__CLM-C06-002.md)。

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

exact-inventory check 本身并未失效；它检测到了真实变化。错误发生在把验证器失败、目标失败和目标未观察混成同一种结果时。

### 限制

- 这是一个 Python bytecode 副作用造成的单一案例；
- 它不证明验证器必须完全无副作用；
- 已声明并隔离的正常输出不自动构成 Integrity failure；
- 当前取证没有重跑历史 harness，修正方案的运行效果不能从该 incident 单独推出。

完整来源、反证与人工收窄边界见 [ER-20260818-002](../Evidence/receipts/ER-20260818-002__CLM-C06-004.md)。

---

# 6.13 适应性采用：不是每个项目都需要 Registry

Truth and State Architecture 的目标不是最大化元数据。

治理本身是成本。

## 低风险、局部任务

通常只需要：

```text
Current file / repo state
Clear scope
Simple verification
```

## 普通多文件任务

可能需要：

```text
Intent reference
Commit / branch / dirty state
Active decisions
Open assumptions
Tests / evidence
```

## 高风险、长任务或多 Agent 任务

才需要考虑：

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

成熟度不是：

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
Decision / Policy       normative authority
State Claim             described current state
Assumption              explicit unknown
Evidence / Provenance   observed basis and generation boundary
Context Manifest        information actually supplied
Execution Baseline      authorized starting bundle
```

最终原则是：

> **Agent 不需要一个看起来没有矛盾的世界；它需要一个知道哪些是状态、哪些是决定、哪些是假设、验证器实际观察了什么、哪些证据只支持有限范围、哪些冲突仍未解决的工程环境。**

有了这层区分，下一章才能进一步讨论 Agent 如何在明确 Intent、Context、State 与 Authority 下打开 Execution Contract、执行、观察风险并形成经过验证的 State Transition。

---

# 本章原则

1. **Store Claims, not “Truth objects”。** 系统管理可修订 Claim 及其依据。
2. **Source of Truth 必须绑定问题。** Authority 由 Domain、Scope、Version 和 Time 决定。
3. **Intent、Decision、State Claim、Assumption、Evidence 必须分开。**
4. **先确认 Evidence 实际观察了什么。** 验证器结果与目标结果必须分开。
5. **Evidence supports Claims。** 范围内验证与用途资格、采用、发布不是同一状态。
6. **Provenance before confidence。** 来源和验证边界优先于语言确信感。
7. **State Snapshot 不包含全部工作语义。** Decision 与 Assumption 通过 Execution Baseline 引用。
8. **Preserve Unknown and Conflict。** 不确定性不是必须被模型补全的空白。
9. **Reconstruct the external decision environment。** 不依赖隐藏推理完成审计。
10. **Agent may assert; authority disposes。** 断言权、状态修改权和裁决权需要分开。
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

如果失败发生在目标观察之前，应分别记录 Evidence generator 的失败和目标的 `non-result`，不能虚构目标 FAIL。

---

# 本章检查清单

- 当前问题是什么，而不是“整个项目什么是真的”？
- 它属于哪个 State Domain？
- Primary Authority 对这个问题是否适用？
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
- Runtime、Data、Configuration 是否可能与 Repo 不同？
- Decision 是否已经 Superseded 或过期？
- Assumption 是否拥有风险、Owner、验证路线和 Expiry？
- 冲突能否自动解决，还是必须保留或升级？
- Agent 有权修改 State、提交 Claim，还是裁决 Claim？
- Context Manifest 是否记录 Agent 实际获得的信息？
- State Snapshot 是否独立于 Agent 当时看到的 Context？
- Execution Baseline 是否分别引用 State、Intent、Decision 和 Assumption？
- 任务结束后，哪些旧 Claim 应失效或重新验证？
- 是否能从 Input State、Change、Evidence 重建 Output State？
- 当前任务真的需要 Registry/Graph，还是简单验证已经足够？
