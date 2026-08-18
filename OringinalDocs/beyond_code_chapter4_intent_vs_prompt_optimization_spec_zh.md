# Beyond Code: AI-Native Software Engineering
## 第四章优化说明：Intent Engineering 与 Prompt Engineering 的边界重构

> 本文档用于修订《第4章 Intent Engineering：从模糊需求到可执行意图》。
>
> 修订目标：
>
> 1. 承认 Intent Engineering 与高质量 Prompt Engineering 在任务表达层存在显著重叠；
> 2. 避免把 Goal、Constraint、Acceptance、Non-goal 等常见 Prompt Engineering 元素重新命名成“新理论”；
> 3. 将第四章重心从“如何写一个更好的任务 Prompt”提升到“如何把 Intent 作为长期、可版本化、可追踪、可继承、可治理的软件工程资产”；
> 4. 建立 Intent → Prompt Projection → Agent Execution 的清晰层级关系；
> 5. 与 Tight Boundaries, Flexible Execution、Low Coupling、Agent Contract、Context Engineering 和 Evidence Engineering 保持一致。

---

# 0. 核心修正结论

当前第四章的主要问题不是方向错误，而是：

> **前半部分对 Goal、Motivation、Constraint、Non-goal、Acceptance、Evidence 等内容展开较多，读者很容易把 Intent Engineering 理解成“结构化、高质量 Prompt Engineering”。**

这个质疑是成立的。

因此，应主动承认：

> **一个执行准备充分的 Intent，在单次 Agent 调用中，往往会表现成一个高质量 Prompt。**

真正需要区分的不是：

> Intent 里写了什么 vs Prompt 里写了什么

而是：

> **Intent 是什么性质的工程对象，Prompt 又是什么性质的运行时对象。**

建议全章采用以下核心定义：

> **Prompt Engineering 优化一次模型或 Agent 交互；Intent Engineering 管理目标的生命周期。**

进一步定义：

> **Intent Engineering 与高质量 Prompt Engineering 在任务表达层高度重叠，但 Intent Engineering 将“意图”从一次模型调用中的文本提升为一个可版本化、可追踪、可继承、可治理，并可投影到多个 Agent / Role / Runtime 的长期软件工程资产。**

---

# 1. 第四章总体结构需要怎样调整

## 当前问题

现有章节顺序大致是：

```text
Requirement vs Intent
Intent structure
Intent over Instruction
Motivation
Goal
Non-goal
Constraint
Assumption
Acceptance
Evidence
Decision Point
Intent Object
Intent ≠ Prompt
...
```

前半部分占比较大，因此容易给人：

> Intent Engineering = 写更完整的任务描述

的印象。

## 建议新的章节重心比例

### 第一部分：与 Prompt Engineering 的关系 — 20%

主动承认重叠，并定义边界。

### 第二部分：Intent 作为长期工程资产 — 50%

重点展开：

- Identity
- Ownership
- Versioning
- Hierarchy
- Inheritance
- Registry
- Drift
- Decision History
- Lifecycle
- Evidence Mapping

### 第三部分：Intent Projection — 30%

讨论：

```text
Intent
+
Role
+
Context
+
Policy
+
Runtime
↓
Agent-specific Prompt
```

以及这一结构如何降低 Agent Coupling、提高 Runtime 可移植性。

---

# 2. 章节标题建议

现标题：

> # 第4章 Intent Engineering：从模糊需求到可执行意图

可以保留。

但建议副标题或开篇定义更明确地加入：

> **从一次 Prompt 到长期目标资产**

或者：

> **从任务描述到可版本化的目标系统**

不建议把标题直接改成 Prompt vs Intent，因为本章仍然要建立正向方法论，而不是只做术语辩论。

---

# 3. 4.1 “Requirement 不等于 Intent”需要修订

## 当前风险

当前写法容易形成：

```text
Requirement
≠
Intent
```

过度切割传统 Requirements Engineering。

而实际上：

- Goal
- Constraint
- Acceptance
- Stakeholder Intent

本来就是成熟 Requirements Engineering 的内容。

## 建议改法

### 建议新标题

# 4.1 Requirement、Prompt 与 Intent：三个不同层级

### 建议正文核心

需要明确区分：

```text
Requirement
→ 描述系统需要满足什么

Intent
→ 描述某次变化为什么存在、要达到什么结果，并如何在生命周期中保持一致

Prompt
→ 在某个具体模型 / Agent / Role / Runtime 下，如何把 Intent 和其他运行信息传给执行系统
```

强调：

> Intent Engineering 不是替代 Requirements Engineering，而是在 Agent 能直接解释并执行任务的条件下，为 Requirement 与 Agent Execution 之间增加一个可治理的目标层。

推荐表达：

> 传统 Requirements Engineering 解决“系统需要什么”；Intent Engineering 进一步解决“这个目标在多 Agent、多阶段、长时间执行中如何保持身份、边界、版本与可追踪性”；Prompt Engineering 则解决“这一次如何把这些信息有效传递给模型或 Agent”。

---

# 4. 新增专门小节：Intent Engineering 与 Prompt Engineering 的重叠

## 建议插入位置

放在新的 4.1 之后。

标题建议：

# 4.2 为什么 Intent 看起来很像一个好 Prompt

### 必须主动承认

以下元素同时属于优质 Prompt Engineering 和 Intent Engineering：

- Goal
- Motivation
- Constraint
- Non-goal
- Assumption
- Acceptance Criteria
- Output Requirement
- Escalation Condition

这不是冲突，而是因为：

> **当 Intent 被投递给 Agent 时，它必然会成为 Prompt / Agent Input 的一部分。**

推荐核心句：

> 一个执行准备充分的 Intent，在单次调用中往往就是一个高质量 Prompt；两者的真正差异不在内容字段，而在生命周期、身份、复用方式和治理责任。

---

# 5. 新增关键定义：Intent ≠ Prompt 的真正原因

## 建议新小节

# 4.3 Prompt 是 Runtime Input，Intent 是 Engineering Artifact

这是本章最重要的边界之一。

## Prompt

Prompt 是：

> 某一次模型 / Agent 执行的运行时输入。

通常由：

```text
Role
+
Intent
+
Context
+
Policy
+
Instruction
+
Output Format
```

组成。

Prompt 的生命周期通常绑定：

- 一次调用；
- 一个 Thread；
- 一个 Agent；
- 一个 Runtime。

## Intent

Intent 是：

> 项目中某个目标或变化的长期工程对象。

至少可能包含：

```text
Intent ID
Owner
Version
Parent Intent
Goal
Motivation
Scope
Non-goal
Constraint
Assumption
Acceptance
Evidence Mapping
Decision History
Status
```

Intent 可以存在于：

- 多个 Agent；
- 多个 Prompt；
- 多个 Thread；
- 多个模型；
- 多个执行阶段

之外。

## 推荐核心公式

```text
1 Intent
→ N Prompts
```

例如同一个 Intent：

```text
优化 Player Status Stage 信息层级
```

可以分别投影为：

### Controller Prompt

```text
根据该 Intent 规划执行路径、风险和 Worker 分工。
```

### Worker Prompt

```text
只处理 Stage layout，并遵守 Scope / Evidence Boundary。
```

### Reviewer Prompt

```text
根据 Acceptance Criteria 验证结果，不负责实现。
```

因此：

> **Prompt 是通信载体；Intent 是目标资产。**

---

# 6. 新增核心概念：Prompt Projection / Intent Projection

## 建议新小节

# 4.4 Intent Projection：同一目标如何生成不同 Agent 输入

建议正式引入一个工作概念：

> **Intent Projection**

定义：

> 将稳定 Intent 与当前 Role、Context、Policy、Runtime 组合，生成适合某个 Agent 执行的 Prompt / Agent Input。

可以表示为：

```text
Intent
+
Role
+
Context
+
Policy
+
Runtime
↓
Prompt Projection
↓
Agent Input
```

## 为什么重要

如果 Intent 本身写死：

- 模型名称；
- Tool 顺序；
- 文件路径；
- 内部推理步骤；

Intent 就与 Runtime 强耦合。

更好的结构是：

```text
Stable Intent
↓
Runtime-specific Projection
↓
Claude Code / Codex / Other Runtime
```

这样：

- 模型可以替换；
- Agent Role 可以替换；
- Tool 可以替换；
- Runtime 可以替换；
- Intent 保持稳定。

## 与传统软件工程的类比

可以使用：

```text
High-level Specification
↓
Compiler / Adapter
↓
Runtime-specific Representation
```

但要注意不要把 Intent 和 Source Code 完全等价。

更准确的类比是：

> Intent 是相对稳定的高层目标描述；Prompt 是某次运行时对这一目标的序列化 / 投影。

推荐核心句：

> **Prompt is a runtime projection of intent.**

中文：

> **Prompt 是 Intent 在特定 Agent、Role、Context 和 Runtime 下的一次运行时投影。**

---

# 7. “Intent over Instruction”需要降权和重新定位

## 当前问题

现在该原则出场太早、展开较长，容易继续强化：

> Intent Engineering = Prompt 写法原则

## 建议修改

保留该原则，但将其定位为：

> Intent Projection 与 Agent Contract 的设计原则之一。

而不是 Intent Engineering 的全部核心。

建议表述：

> Intent over Instruction 并不是要求 Prompt 里永远少写步骤，而是要求长期 Intent 不与某一条固定执行路径绑定。确定性、安全性或合规流程仍然可以包含明确 Instruction。

---

# 8. Motivation / Goal / Non-goal / Constraint 等小节需要压缩

## 当前问题

这些部分内容本身合理，但展开过多。

建议把：

- Motivation
- Goal
- Non-goal
- Constraint
- Assumption
- Acceptance

压缩为一个更集中小节：

# Execution-ready Intent 的基础字段

建议保留简短解释：

### Motivation

为什么存在。

### Goal

成功后的 Outcome。

### Scope / Non-goal

做什么，不做什么。

### Constraint

必须遵守什么现实边界。

### Assumption

哪些判断尚未验证。

### Acceptance

什么结果才算成功。

### Required Evidence

如何证明成功。

### Human Decision Point

哪些判断不能由 Agent 自己越过。

这样减少“Prompt 教程感”。

---

# 9. Intent Object 应提前成为全章中心

## 当前 Intent Object 出现较晚

建议提前。

在解释 Intent 与 Prompt 区别后，立刻给出：

```text
Intent Object

ID
Owner
Version
Status

Motivation
Goal

Scope
Non-goals
Constraints
Assumptions

Parent Intent
Child Intents

Acceptance Criteria
Evidence Mapping

Decision Rights
Decision History
```

然后后续章节都围绕：

> 这个对象如何产生、拆解、继承、变化和被消费

展开。

这会明显提高“软件工程”感。

---

# 10. 增强 Intent Identity

Prompt 通常不需要稳定 ID。

Intent 需要。

因为需要支持：

```text
INT-SP122-001
```

在：

- Thread A；
- Worker B；
- Review C；
- Commit D；
- Evidence E

之间保持同一目标身份。

因此建议新增：

# Intent Identity

说明：

> 如果目标在跨 Thread、跨 Agent、跨 Commit 后无法保持稳定身份，就无法可靠进行版本、追踪和 Drift Detection。

---

# 11. 增强 Intent Ownership

当前已有 Intent Owner，但建议上移并加强。

核心：

> Agent 可以协助生成、质疑、细化 Intent，但 Agent 不应成为最终 Intent Owner。

Owner 负责：

- 批准目标；
- 批准重大变化；
- 解决冲突；
- 接受 Outcome。

强调：

```text
Agent can propose intent changes.
Human / Organization owns intent.
```

---

# 12. 强化 Intent Lifecycle

建议新增一个完整生命周期：

```text
Draft
↓
Clarified
↓
Approved
↓
Active
↓
Decomposed
↓
Executed
↓
Verified
↓
Accepted
↓
Completed / Superseded / Cancelled
```

并支持：

```text
Reopen
Revise
Deprecate
```

这部分是 Prompt Engineering 通常不会系统处理的。

---

# 13. 强化 Intent Versioning

每次重大变化记录：

```text
Intent ID
Version
Changed Field
Reason
Decision Owner
Effective From
Affected Tasks
```

重点区分：

> Intent Evolution vs Intent Drift

### Intent Evolution

显式批准的目标变化。

### Intent Drift

没有明确决策，目标在执行和 Handoff 中逐渐改变。

---

# 14. 强化 Intent Hierarchy

建议改成明确结构：

```text
Product Intent
↓
Feature Intent
↓
Milestone Intent
↓
Task Intent
```

并解释：

> Task 不只是 Activity，它应能追溯到上层 Intent。

增加：

```text
Intent Graph
```

概念。

---

# 15. 强化 Intent Inheritance

这是超出普通 Prompt Engineering 的关键点。

Worker Task 应同时获得：

```text
Local Goal
+
Relevant Parent Intent
```

而不是只获得局部动作。

例如：

```text
Parent Intent:
提升战斗信息读取效率

Local Intent:
优化 Stage layout
```

这样避免：

> 局部成功，整体失败。

---

# 16. 强化 Intent Registry

建议作为第四章核心基础设施。

Intent Registry 回答：

> 当前项目为什么在做这些任务？

与 Task Tracker 区分：

### Task Tracker

记录：

- 做什么；
- 谁做；
- 状态。

### Intent Registry

记录：

- 为什么做；
- 目标是什么；
- 来源是什么；
- 版本是什么；
- 谁拥有；
- 对应什么 Evidence。

---

# 17. 新增 Prompt / Task / Intent 三者关系

建议加入一张表：

| 对象 | 核心问题 | 生命周期 | 是否长期 |
|---|---|---:|---:|
| Requirement | 系统需要什么 | 项目 / 产品 | 是 |
| Intent | 为什么发生这次变化、期望什么结果 | 跨任务 / 跨 Agent | 是 |
| Task | 需要完成什么工作单元 | 执行阶段 | 中 |
| Prompt | 这一次如何告诉模型 / Agent | 单次运行 | 否 |
| Agent Contract | 这个角色被允许如何参与 | 角色 / Workflow | 是 |

这样可以避免术语混淆。

---

# 18. 强化 Intent 与 Agent Contract 的关系

核心结构：

```text
One Intent
↓
Multiple Agent Contracts
```

例如：

```text
Intent
├── Controller Contract
├── Worker Contract
├── Reviewer Contract
└── Cognition Contract
```

这也是：

> High Agent Cohesion / Low Agent Coupling

的基础。

---

# 19. 强化 Intent 与 Context 的分离

必须保留：

```text
Intent
= What / Why

Context
= What the agent needs to know
```

建议强调：

> Intent 不应该成为巨大 Context Pack。

否则会出现：

- 目标与知识混合；
- Intent 难版本化；
- 重复信息；
- Runtime 强耦合。

---

# 20. 强化 Intent 与 Truth 的分离

必须保留：

```text
Intent
= Desired State

Truth
= Verified Current State
```

建议加一句：

> Intent 不能因为表达得更清楚就升级成 Truth。

---

# 21. Acceptance 与 Evidence Mapping 应保留，但压缩 Prompt 写法细节

建议从“如何写 Acceptance Criteria”转向：

# Intent-to-Evidence Mapping

结构：

```text
Intent
↓
Acceptance Criteria
↓
Evidence Requirement
↓
Verification
↓
Acceptance
```

强调：

> Evidence Mapping 是 Intent 进入工程闭环的重要原因，也是 Intent 超出普通 Prompt 的关键之一。

---

# 22. 增加 Intent Traceability

建议新增：

# Intent Trace

完整链：

```text
Parent Intent
↓
Task Intent
↓
Agent Execution
↓
Change
↓
Evidence
↓
Decision
```

用于回答：

> 这段代码为什么存在？

传统 Git 可能只能回答：

> 谁改了什么。

Intent Trace 进一步回答：

> 为什么需要这次变化。

---

# 23. 修改 Intent Profiles

可以保留 Lean / Standard / Expanded / Full，但不要写成 Prompt Template Length，而应写成：

> Intent Governance Profile。

### Lean

```text
Goal
Scope
Done
```

### Standard

```text
Motivation
Goal
Scope
Non-goal
Acceptance
Evidence
```

### Expanded

```text
Parent Intent
Truth Baseline
Assumption
Risk
Decision Right
```

### Full

```text
Version
Owner
Decision History
Dependencies
Evidence Mapping
Lifecycle
```

重点是：

> Profile 决定治理信息量，而不是 Prompt 长短。

---

# 24. 修改“AI 可以帮助生成 Intent，但不能拥有 Intent”

该节保留，且应该成为核心。

AI 可以：

- Extract
- Clarify
- Challenge
- Detect Ambiguity
- Suggest Acceptance
- Suggest Non-goal

但：

```text
Intent Authority
≠
Agent Authority
```

重大 Intent Change 必须由：

- Human；
- Product Owner；
- Producer；
- Authorized Organization Role

确认。

---

# 25. Intent Confirmation / Clarification 重新定位

建议放入：

# Risk-based Intent Clarification

区分：

```text
Low-impact ambiguity
→ explicit assumption

Medium-impact ambiguity
→ limited clarification

High-impact / irreversible ambiguity
→ mandatory human decision
```

这样与 Governed Autonomy 一致。

---

# 26. Intent 与 Tight Boundaries 的关系需要更精确

不要把全部 Boundary 都放进 Intent Object。

建议分层：

### Intent 自身主要定义

- Goal Boundary
- Outcome Boundary
- Non-goal
- Acceptance

### Agent Contract / Governance 定义

- Authority Boundary
- Tool Boundary
- Permission
- Escalation

### Truth / State 定义

- State Boundary
- Baseline

### Evidence 定义

- Evidence Boundary

它们在运行时组合：

```text
Intent
+
Truth
+
Agent Contract
+
Policy
+
Context
↓
Execution Boundary
```

这样避免 Intent 变成“万能容器”。

---

# 27. 一个重要修正：Intent Object 不要吸收整个 Control Plane

当前第四章有一个倾向：

> Scope、Permission、Truth Baseline、Risk、Evidence 全部进入 Intent。

长期看会让 Intent 过重。

应区分：

## Intent Object

主要负责：

```text
Why
Goal
Scope
Non-goal
Acceptance
Owner
Version
Hierarchy
```

## Execution Contract

运行时组合：

```text
Intent
+
Truth Baseline
+
Context
+
Agent Contract
+
Permission Policy
+
Evidence Requirement
```

这更符合：

> Low Coupling。

---

# 28. 新增核心结构：Intent → Execution Contract → Prompt

建议作为第四章最终模型。

```text
Intent Object
        ↓
Truth / Context / Policy / Role
        ↓
Execution Contract
        ↓
Prompt Projection
        ↓
Agent Execution
```

其中：

### Intent Object

稳定目标。

### Execution Contract

本次执行允许怎样工作。

### Prompt Projection

将 Contract 序列化为具体 Runtime 输入。

这个三层结构比：

```text
Intent = Very Good Prompt
```

清晰得多。

---

# 29. 与 Agent Harness 的关系

第三章已经明确：

> Harness 解决 Agent 如何运行。

第四章可进一步说明：

Harness 接收的是：

```text
Prompt / Agent Input
Tools
Runtime State
```

而 Prompt 的上游应该是：

```text
Intent
+
Context
+
Policy
+
Role
```

因此：

```text
Intent Engineering
→ prepares stable goal assets

Context Engineering
→ prepares world knowledge

Governance
→ prepares boundaries

Harness
→ executes
```

这能与第三章形成连续逻辑。

---

# 30. 修改后的推荐章节结构

建议第四章正式修订为：

```text
4.1 Requirement、Intent、Task 与 Prompt
4.2 为什么 Intent 看起来像一个好 Prompt
4.3 Prompt 是 Runtime Input，Intent 是 Engineering Artifact
4.4 Intent Projection：从稳定目标到 Agent Input
4.5 Intent Object：目标如何成为工程资产
4.6 Execution-ready Intent 的基础字段
4.7 Intent Identity 与 Ownership
4.8 Intent Lifecycle
4.9 Intent Versioning：Evolution vs Drift
4.10 Intent Hierarchy 与 Intent Graph
4.11 Intent Inheritance
4.12 Intent Registry
4.13 Intent Traceability
4.14 Intent 与 Agent Contract
4.15 Intent 与 Context / Truth 的边界
4.16 Intent-to-Evidence Mapping
4.17 Intent Review
4.18 Risk-based Clarification
4.19 Intent Governance Profiles
4.20 AI 如何协助 Intent Engineering
4.21 Intent → Execution Contract → Prompt
4.22 完整案例
4.23 本章结论
```

---

# 31. 原第四章哪些内容可以保留

以下核心内容继续保留，但位置和篇幅调整：

- Intent over Instruction
- Motivation
- Goal
- Non-goal
- Constraint
- Assumption
- Acceptance Criteria
- Required Evidence
- Human Decision Points
- Intent Object
- Intent Decomposition
- Intent Inheritance
- Intent Drift
- Intent Versioning
- Intent Registry
- Intent Owner
- Controller as Intent Custodian
- Worker 不得自行改写 Intent
- Intent vs Truth
- Intent vs Context
- Intent vs Contract
- Intent Review
- Intent Profiles
- AI 可辅助但不能拥有 Intent

---

# 32. 哪些内容应该明显压缩

以下内容建议压缩约 30%–50%：

- Goal 怎么写
- Motivation 为什么重要
- Non-goal 示例
- Constraint 类型
- Acceptance Criteria 示例
- “更长不等于更精确”
- Prompt 风格示例

原因：

> 这些内容虽正确，但成熟 Prompt Engineering / Requirements Engineering 已经有大量类似实践，不应占据第四章理论中心。

---

# 33. 需要新增的核心术语

## Intent Artifact

中文：意图工程资产

定义：

> 具有稳定身份、Owner、Version、Hierarchy、Lifecycle 和 Traceability 的目标对象。

## Intent Projection

中文：意图投影

定义：

> 将稳定 Intent 与特定 Role、Context、Policy 和 Runtime 组合，生成某一次 Agent 执行所需输入的过程。

## Prompt Projection

建议：

- Intent Projection：强调从 Intent 到角色执行视图
- Prompt Projection：强调最终序列化成模型 / Agent 输入

## Intent Identity

定义：

> 一个 Intent 在跨 Agent、Thread、Task 和版本过程中保持可追踪的稳定身份。

## Intent Lifecycle

定义：

> Intent 从 Draft、Approved、Active、Executed、Verified 到 Completed / Superseded / Cancelled 的完整状态变化。

## Intent Graph

定义：

> Product、Feature、Milestone、Task 等不同层级 Intent 之间的父子与依赖关系。

## Intent Traceability

定义：

> 从目标到任务、执行、变更、Evidence 和最终 Decision 的可追踪链路。

## Execution Contract

定义：

> 将 Intent、Truth Baseline、Context、Agent Contract、Policy、Permission 和 Evidence Requirement 组合成某次 Agent Execution 的正式约束对象。

---

# 34. 修改后的关键理论链

第四章应该最终形成：

```text
Human Need
    ↓
Requirement
    ↓
Intent Object
    ↓
Intent Registry / Graph / Version
    ↓
Execution Contract
    ↓
Intent / Prompt Projection
    ↓
Agent Execution
    ↓
Evidence
    ↓
Intent Acceptance
```

这会明显区别于：

```text
Write a better prompt
↓
Get a better answer
```

---

# 35. 与 High Cohesion / Low Coupling 的关系

修改后的 Intent Engineering 应明确支持：

## Low Coupling

稳定 Intent 不与：

- Model
- Prompt wording
- Tool path
- Agent implementation

强绑定。

## High Cohesion

一个 Intent 聚焦：

> 一个清晰 Outcome 和其完成条件。

不同 Agent 通过：

```text
Intent
+
Contract
```

共享目标，而不是共享全部执行历史。

因此可形成：

> **Stable Intent, Adaptable Execution.**

与：

> **Tight Boundaries, Flexible Execution**

一致。

---

# 36. 修改后的核心句集合

建议第四章保留以下核心句：

### 1

> **Prompt Engineering 优化一次交互；Intent Engineering 管理目标的生命周期。**

### 2

> **Prompt 是 Intent 在特定 Agent、Role、Context 与 Runtime 下的一次运行时投影。**

### 3

> **一个高质量 Intent 在单次执行时往往表现为一个高质量 Prompt，但一个高质量 Prompt 并不自动构成可治理的 Intent。**

### 4

> **Intent 应保持稳定，执行方式可以适配。**

### 5

> **Intent 是 Human Intent 与 Agent Execution 之间的长期工程接口。**

### 6

> **AI 可以协助形成 Intent，但最终 Intent Authority 属于人类或被授权的组织角色。**

---

# 37. 本次修订是否影响主大纲

## 结论

**需要小幅更新第四章大纲，但不改变全书章节结构。**

主大纲第四章应由：

> “如何把模糊需求写成执行良好的 Intent”

升级为：

> “如何把 Intent 从一次 Prompt 中抽离出来，形成长期、可版本化、可追踪、可投影的软件工程资产。”

---

# 38. 是否需要修改第三章

## 只需要极小修改

第三章已经定义：

- AI-native SE
- Harness
- Control Plane
- Production Intelligence

可以在第三章结尾增加一句伏笔：

> 下一章所讨论的 Intent，不应被理解为另一个 Prompt 模板。Prompt 是 Runtime 输入，而 Intent 将被定义为跨 Agent、跨 Runtime 保持稳定的工程目标资产。

无需大改。

---

# 39. 是否需要修改前言 / 导读

## 不需要

前言和导读不应继续增加术语密度。

当前只需要在正文第四章解决这个专业边界问题。

---

# 40. 本次修订的最终价值

本次修改解决的是第四章一个潜在的理论风险：

> **如果 Intent Engineering 只是在重新描述 Goal、Constraint、Acceptance 等优质 Prompt 写法，那么它不足以作为 AI-Native Software Engineering 的独立工程领域。**

修订后，Intent Engineering 的真正研究对象变成：

```text
Identity
Ownership
Lifecycle
Version
Hierarchy
Inheritance
Registry
Drift
Traceability
Evidence Mapping
Projection
```

这使它从：

> Prompt Content Design

上升为：

> **Goal Lifecycle Engineering**

最终可以用一句话概括：

> **Intent Engineering 的新意不在于告诉人们 Prompt 里应该写 Goal 和 Constraint，而在于把“目标”从一次对话中的文字，提升为整个 AI 软件生产体系中可以持续存在、流转、继承、验证和治理的正式工程资产。**
