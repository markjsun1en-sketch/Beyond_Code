# Beyond Code: AI-Native Software Engineering
## 变更说明：Human Smoothing、Tight Boundaries 与 Agent Cohesion

> 本文档用于记录 2026-08-07 讨论后，对现有《Beyond Code: AI-Native Software Engineering》相关文档建议进行的结构与内容修改。
>
> 本文档不是正文替代稿，而是一份 **Patch Specification / Change Proposal**：明确指出原文档哪些位置需要调整、调整原因、修改方式以及建议新增文本。

---

# 0. 本次变更摘要

本次讨论新增或强化了以下核心判断：

1. 传统非 AI 软件开发中，人类成员经常通过常识、项目经验、默契、社会沟通和临场判断，承担大量未被正式建模的“平滑”和问题修复作用。
2. 当部分执行工作转交给 AI Agent 后，这种隐性平滑能力不能被稳定假设存在，因此过去被人类自然吸收的模糊、冲突和流程缺口会被暴露出来。
3. 因此，AI-native 软件工程并不是要求把 Agent 的每一步执行都规定得更死，而是要求：
   - **边界更严格**
   - **职责更清晰**
   - **接口更显式**
   - **证据更明确**
   - **边界内部执行保持灵活**
4. 这一原则可以概括为：
   - **Tight Boundaries, Flexible Execution**
   - 中文建议：**明确边界，灵活执行** / **边界严格，执行自治**
5. 该原则与传统软件工程中的 **High Cohesion, Low Coupling** 高度同构，但作用对象从 Code Module 上移到了 Agent / Worker / Workflow / Production Organization。
6. 可进一步形成三个重要设计原则：
   - **Contract over Reasoning Process**
   - **Encapsulate Execution, Expose Evidence**
   - **Agent Cohesion / Task Cohesion**
7. 这些内容不需要推翻现有大纲，但应强化第二章、设计原则、Agent Organization、Evidence、术语表和产品附录之间的理论连接。

---

# 1. 影响文档清单

| 文档 | 是否需要更新 | 优先级 | 修改规模 |
|---|---|---:|---:|
| `beyond_code_ai_native_software_engineering_outline_zh.md` | 是 | P0 | 中 |
| 第二章《当传统软件工程的隐含假设开始失效》当前草稿 | 是 | P0 | 中 |
| `beyond_code_appendices_claude_codex_ai_native_software_engineering_zh.md` | 是 | P1 | 小-中 |
| 核心术语表 | 是 | P0 | 小 |
| 前言（个人实践叙事版） | 可选微调 | P2 | 极小 |
| 导读（行业大众版） | 可选微调 | P2 | 极小 |
| 第一章《软件工程的角色演进》 | 暂不需要 | — | 无 |
| 后续 Agent Execution / Organization / Evidence 章节 | 尚未成稿，写作时直接纳入 | P0 | 新增原则 |

---

# 2. 主大纲文档修改

## 目标文档

`beyond_code_ai_native_software_engineering_outline_zh.md`

---

## 2.1 在“全书核心命题”中增加一条基础判断

### 原位置

文档开头：

> # 一、全书核心命题

当前已有五条基本判断。

### 修改方式

**新增第 6 条。**

### 建议新增文本

> 6. 传统人类团队长期依赖大量未被正式写入流程的隐性纠错能力，例如常识、项目经验、团队默契、角色判断和临场协调。Agent 接管部分执行后，这些能力不能再被默认存在，因此 AI 原生软件工程需要把过去依赖人类隐性完成的边界判断、事实裁决、升级条件和验证要求逐步显式工程化。

### 修改目的

为后续 Human Smoothing Effect、Smoothing Gap 和 Tight Boundaries 建立全书级理论前提。

---

## 2.2 在“全书核心生命周期”之后增加一个设计原则层

### 原位置

当前为：

```text
Human Intent
→ ...
→ Controlled Evolution
```

之后直接进入贯穿能力：

```text
Governance
Traceability
Security
Economics
Observability
```

### 修改方式

在生命周期和贯穿能力之间新增：

# AI-Native Design Principles

### 建议新增内容

```text
Intent over Instruction
        ↓
Tight Boundaries, Flexible Execution
        ↓
Contract over Reasoning Process
        ↓
Encapsulate Execution, Expose Evidence
        ↓
Evidence over Confidence
```

建议配套说明：

### Principle 1 — Intent over Instruction

优先明确：

- Goal
- Motivation
- Constraint
- Non-goal
- Acceptance

而不是把 Agent 退化成逐步执行脚本。

### Principle 2 — Tight Boundaries, Flexible Execution

明确规定：

- Scope
- Truth Baseline
- Permission
- Risk Boundary
- Evidence
- Escalation

边界内部允许 Agent 自主选择执行路径。

### Principle 3 — Contract over Reasoning Process

外部系统不应微操 Agent 的内部推理过程，而应约束：

- 它收到什么；
- 可以做什么；
- 必须返回什么；
- 什么时候必须停止或升级。

### Principle 4 — Encapsulate Execution, Expose Evidence

Agent 内部的搜索、尝试、Debug 和调整可以被封装；但：

- Result
- Evidence
- Risk
- Scope Change
- Trace

必须显式暴露。

### Principle 5 — Evidence over Confidence

任何完成声明都必须由独立证据支持，而不是依赖 Agent 的语言置信度。

---

## 2.3 修改“第2章 传统软件工程的隐含假设正在失效”大纲

### 原位置

> # 第2章 传统软件工程的隐含假设正在失效

当前有“假设一”到“假设七”的结构。

### 修改方式

保留七个假设，同时增加新的关键小节：

## 2.x 人类平滑效应：传统软件工程中的隐性纠错层

### 建议插入位置

建议放在：

> 2.8 本章结论

之前。

更具体建议：

- 原 2.7“假设七：软件的真实状态容易确定”
- **新增 2.8 Human Smoothing Effect**
- 原 2.8 本章结论顺延为 2.9

### 建议新增大纲内容

#### 2.8.1 Human Smoothing Effect

定义：

> 在传统软件生产中，人类成员利用常识、项目经验、社会沟通、隐性知识和临场判断，自发修补需求、流程和信息中的不完整性、冲突与例外。

典型表现：

- 发现需求模糊后主动询问；
- 根据项目历史修正旧文档；
- 识别“字面正确但实际不合理”的实现；
- 在专业之间补齐隐含上下文；
- 通过经验判断何时应暂停执行。

#### 2.8.2 Smoothing Gap

定义：

> 当部分执行工作转交给 Agent 后，原本由人类隐性承担的平滑能力无法稳定存在，由此暴露出的流程、上下文和治理缺口。

#### 2.8.3 AI 暴露而非创造所有问题

重要观点：

> AI 并不只是制造新的软件工程问题，它也会暴露过去长期被人类默契和临场判断吸收掉的问题。

#### 2.8.4 从隐性能力到显性工程机制

映射：

| 传统人类隐性能力 | AI-native 显性机制 |
|---|---|
| 人类理解需求真实意图 | Intent Engineering |
| 老员工知道什么是真的 | Truth Hierarchy |
| 团队知道哪些信息过期 | Context Provenance |
| Lead 知道哪些地方不能动 | Scope / Permission Boundary |
| 资深成员知道什么时候问人 | Escalation Rules |
| Reviewer 知道哪些风险高 | Risk Model |
| QA 知道什么才算完成 | Evidence-Driven DoD |

### 修改目的

解释一个关键问题：

> 为什么传统团队即使流程不够精确，也经常能够正常运行，而 AI 接管以后反而需要更精确的边界和接口？

---

## 2.4 在“第7章 Agent Execution Engineering”中新增设计原则

### 原位置

当前包含：

- Agent 与传统自动化区别
- 基础执行循环
- Controller / Worker
- Planner / Executor
- Tool Use
- Agent Contract
- Execution Scope

### 修改方式

新增两节：

## 7.x Tight Boundaries, Flexible Execution

建议内容：

Agent 不应被逐步微操，而应明确：

```text
Goal
Constraints
Allowed Scope
Truth Baseline
Permissions
Required Evidence
Escalation Rules
```

内部允许：

```text
Search
Plan
Experiment
Implement
Test
Debug
Retry
```

强调：

> 严格的是边界，不是每一步执行路径。

### 新增：

## 7.x Contract over Reasoning Process

建议核心句：

> 外部系统应该管理 Agent 的契约，而不是试图规定或依赖其内部推理过程。

Contract 至少包含：

```text
Input
Boundary
Authority
Expected Output
Evidence
Escalation
```

### 修改目的

避免 AI-native 被误解成：

- 更长 Prompt；
- 更细步骤；
- 更强微操。

---

## 2.5 在“第9章 Verification and Evidence Engineering”增加原则

### 原位置

第9章当前重点：

- Completion Levels
- Evidence-Driven DoD
- Evidence Stack
- Evidence Coverage
- Evidence Provenance
- Review Agent

### 修改方式

新增：

## 9.x Encapsulate Execution, Expose Evidence

### 建议内容

传统软件架构：

> Encapsulate Implementation.

AI-native 扩展：

> **Encapsulate Execution, Expose Evidence.**

含义：

不要求人类或上层 Controller 阅读 Agent 的全部搜索、尝试和中间步骤，但必须显式获得：

- 最终结果；
- 修改范围；
- Evidence；
- 未验证假设；
- 风险；
- Scope Change；
- 必要 Trace。

推荐结构：

```text
Intent
    ↓
┌─────────────────┐
│ Flexible Agent   │
│ Execution        │
└─────────────────┘
    ↓
Result
Evidence
Risk
Trace
```

### 修改目的

把 Evidence Engineering 与 Cognitive Engineering、Agent Encapsulation 连起来。

---

## 2.6 在“第12章 Cognitive Compression”补一个重要限定

### 原位置

第12章目前强调：

- Progressive Disclosure
- Change Narrative
- Architecture Impact
- Risk Map
- Decision Surface
- Compression Trust

### 修改方式

增加一个原则说明：

> Cognitive Compression 不是为了重新暴露 Agent 的所有内部执行细节，而是为了将被封装的执行结果转换为人类可判断的信息。

建议引用：

> **Encapsulate Execution, Expose Evidence.**

并明确：

```text
Transparency
≠
Show everything
```

而应是：

```text
Transparency
=
Expose the information required
for verification and decision
```

### 修改目的

防止“透明性”被误解为日志越多越好。

---

## 2.7 在“第17章 Multi-Agent Organization Design”增加 Agent Cohesion

### 原位置

当前包含：

- 多 Agent 不等于组织
- Agent Role
- Responsibility and Authority
- Structured Handoff
- Conflict Resolution
- Controller / Worker
- Human-Agent Organization

### 修改方式

新增：

## 17.x Agent Cohesion and Coupling

### 建议内容

传统：

> High Cohesion, Low Coupling

AI-native 映射：

| 传统软件架构 | Agent 系统 |
|---|---|
| Module | Agent / Worker |
| Responsibility | Goal |
| Interface | Agent Contract |
| Input Parameters | Intent + Context |
| Encapsulation | Execution Autonomy |
| Internal Implementation | Agent Reasoning / Tool Path |
| API Boundary | Scope / Permission Boundary |
| Return Value | Result + Evidence |
| Exception | Escalation |
| Unit Test | Eval / Evidence |

定义：

### Agent Cohesion

一个 Agent / Worker 应围绕一个清晰任务职责，拥有完成该职责所需的：

- Relevant Context；
- Tools；
- Skills；
- Local Decision Authority。

### Agent Coupling

不同 Agent 之间应依赖：

```text
Intent
State
Contract
Evidence
Handoff
```

而不是依赖：

- 无限共享 Context；
- 隐性假设；
- 彼此内部推理；
- 模糊责任。

### 核心结论

> Tight Boundaries, Flexible Execution 可以视为 High Cohesion / Low Coupling 在智能执行系统中的治理层表达。

---

## 2.8 更新“成熟度模型”的评估标准

### 原位置

> 第22章 AI 原生研发成熟度模型

### 修改方式

Level 3 以后增加以下判断指标：

### Level 3 增加

- 是否存在明确 Agent Contract；
- 是否定义 Scope / Authority / Escalation Boundary；
- Worker 是否能够在边界内独立完成任务。

### Level 4 增加

- Agent 交互是否主要通过结构化 Contract / Handoff；
- 人类是否通过 Evidence 和 Decision Surface 控制系统，而非逐步微操；
- 是否能测量或限制 Cognitive Load。

### Level 5 增加

- Skill / Agent / Workflow 演化是否保持原有边界；
- 演化是否会自动扩大权限或耦合；
- 是否存在 Agent Cohesion / Coupling 评估。

---

# 3. 第二章当前草稿修改说明

## 目标文本

当前第二章：

> 《第2章 当传统软件工程的隐含假设开始失效》

---

## 3.1 保留现有 2.9，但扩大为新的核心段落

### 当前小节

> 2.9 一个更深的变化：过去许多“隐性组织能力”需要变成“显性系统能力”

### 建议

这是本次修改的最佳承载位置。

建议改名为：

# 2.9 从 Human Smoothing 到显性工程机制

然后将当前内容重构为四段。

---

### 2.9.1 Human Smoothing Effect

建议新增正文：

> 传统软件流程从来没有把所有现实情况完整形式化。需求可能模糊，文档可能过期，角色之间可能存在理解差异，流程也可能存在尚未覆盖的例外。但项目仍然能够运行，一个重要原因是人类成员一直在承担大量没有正式写入流程的纠错工作。
>
> 一个资深开发者看到模糊需求时，可能主动询问真正目的；看到旧文档时，会根据近期决策判断它已经失效；发现一个字面上符合要求、但明显破坏长期架构的方案时，也可能主动停止执行。这些行为来自常识、项目历史、职业经验和社会沟通。
>
> 本书暂时将这种现象称为 **Human Smoothing Effect（人类平滑效应）**：人类组织利用隐性知识和临场判断，自发吸收生产流程中的不完整性、冲突与例外。

---

### 2.9.2 Smoothing Gap

建议新增正文：

> Agent 并不是完全不具备类似判断能力。强模型可以发现冲突、提出疑问，甚至比普通开发者更快识别某些问题。真正的工程困难在于，我们无法把这种能力当作一个稳定、始终存在的组织基础设施。
>
> 当执行工作从长期参与项目的人类成员转移给上下文依赖、状态可变的 Agent 后，原本由人类自然补齐的流程缺口会显性暴露。本书将这种差异暂称为 **Smoothing Gap（平滑缺口）**。

---

### 2.9.3 AI 暴露了过去被吸收的问题

建议新增：

> 因此，AI-native 软件工程中的一些“新问题”并不完全是 AI 创造的。需求模糊、文档漂移、隐性约束、角色冲突和验证不足过去就存在，只是人类团队长期通过默契、经验和即时沟通把其中相当一部分吸收掉了。
>
> AI 的加入使这些隐性修补不能再被默认依赖，于是迫使组织将原本存在于人脑和团队关系中的能力逐步外部化。

---

### 2.9.4 Tight Boundaries, Flexible Execution

建议作为 2.9 的结论：

> 这种外部化并不意味着把 Agent 的每一步都规定得更死。
>
> 更合理的原则是：
>
> **Tight Boundaries, Flexible Execution。**
>
> 即：
>
> **明确边界，灵活执行。**
>
> 应该严格定义的是：
>
> - Goal；
> - Scope；
> - Truth Baseline；
> - Permission；
> - Risk Boundary；
> - Required Evidence；
> - Escalation Condition。
>
> 至于在这些边界内部如何搜索、尝试、实现、测试和修正，应尽可能让 Agent 保持执行自治。
>
> 因此，AI 原生软件工程的严格性不是流程微操，而是边界精确性。

---

## 3.2 在 2.10 “控制面正在扩大”中增加边界治理

### 当前内容

控制对象从：

```text
Software Change
```

扩展为：

```text
Software Change
+
Change-producing Intelligence
```

### 建议追加

```text
Control Plane
    ↓
Goal Boundary
Scope Boundary
State Boundary
Authority Boundary
Risk Boundary
Evidence Boundary
```

并增加一句：

> 对智能执行者的控制，不应主要依靠规定内部实现，而应依靠明确其可以进入的状态空间、可以采取的权限以及必须对外暴露的结果。

---

## 3.3 在 2.13 “哪些旧原则反而更重要”中增加高内聚低耦合映射

### 当前已有

- 小步修改
- 自动化测试
- 清晰架构
- 版本控制
- 最小权限
- 可观测性

### 建议新增

## 高内聚、低耦合

正文建议：

> High Cohesion / Low Coupling 不会因为 Agent 出现而失效。它可能从代码模块设计进一步上移到 Agent 组织设计。
>
> 一个高内聚 Worker 应围绕单一明确目标拥有足够 Context、Tool 和局部决策权；多个 Agent 之间则应通过稳定 Contract、Structured Handoff 和 Evidence 交互，而不是共享无限上下文或依赖彼此的隐性推理。
>
> 在这一意义上，**Tight Boundaries, Flexible Execution** 可以被看作高内聚、低耦合原则在 AI 执行层和治理层的一种新呈现形式。

---

## 3.4 更新第二章“本章原则”

### 当前五条原则

建议增加：

## 原则六：边界比步骤更值得严格定义

> AI-native 的严格性主要体现在 Intent、Truth、Scope、Authority、Evidence 和 Escalation 上，而不是要求 Agent 机械遵循固定执行脚本。

## 原则七：显式 Contract 替代隐性默契

> 人类团队可以依靠共同历史和临场沟通补齐缺口；Agent 系统则应尽量通过显式 Contract 和 Structured Handoff 传递责任与状态。

---

## 3.5 更新第二章“常见反模式”

新增：

### 反模式六：为了可靠而把 Agent 完全脚本化

如果上层系统规定 Agent 的全部微观操作路径：

- 灵活推理能力被浪费；
- Workflow 与 Repo 结构强耦合；
- 模型升级无法带来能力提升；
- Agent 退化为昂贵脚本。

### 反模式七：为了自治而不给边界

如果只提供目标，不限制：

- Scope；
- Permission；
- Truth Baseline；
- Evidence；
- Escalation；

则自治容易变成范围漂移和不可控修改。

---

# 4. 产品附录文档修改

## 目标文档

`beyond_code_appendices_claude_codex_ai_native_software_engineering_zh.md`

---

## 4.1 在 Appendix A 统一评估方法中新增“Boundary / Cohesion”子维度

### 建议放置位置

可放在：

> 4. Agent Execution

与：

> 5. Reliability and Recovery

之间，或作为两者的联合检查项。

### 新增评估问题

- Agent 是否拥有清晰 Goal Boundary？
- 是否限制 Scope Boundary？
- 是否存在 State Boundary？
- 是否存在 Authority Boundary？
- 是否定义 Risk / Escalation Boundary？
- Agent 是否能在边界内自主完成任务？
- 是否需要上层频繁微操？
- 多 Agent 是否通过 Contract / Handoff 交互？
- Agent 职责是否足够内聚？

---

## 4.2 Claude Code Appendix 增加原则映射

### B.5 Agent Execution

增加：

> Claude Code 的 Agent / Subagent 模式可以被视为 Flexible Execution 的基础能力，但是否形成 Tight Boundaries 取决于 Permission、Tool Scope、Project Instructions、Plan 和外部 Workflow 如何组合。

### B.6 Reliability

Hooks 可以进一步解释为：

> 将部分概率性 Agent 行为约束在确定性的 Boundary / Gate 中。

### B.14 Multi-Agent Organization

增加：

> Subagent 的独立 Context 和工具权限有助于形成 Agent Cohesion；但若角色边界、输入输出和 Handoff 不清晰，多 Agent 仍然可能形成高耦合的组织结构。

---

## 4.3 Codex Appendix 增加原则映射

### C.3 / C.4 Context 与 State

增加：

> Worktree 是 State Boundary 的一种具体实现：它隔离 Worker 的文件状态，但并不自动解决 Goal、Authority 或 Risk Boundary。

### C.5 Agent Execution

增加：

> Thread / Worker 最理想的使用方式不是由 Controller 逐步指定所有操作，而是通过明确任务 Contract，在受限 Worktree 和权限范围中自主执行。

### C.14 Multi-Agent Organization

增加：

> Codex 的 Parallel Agents + Worktrees 为低耦合执行提供了基础设施，但真正的低耦合仍取决于 Structured Handoff、统一 Evidence Schema 和明确合并责任。

---

## 4.4 Appendix D 总表增加新的理论映射

新增两行：

| 理论维度 | Claude Code | Codex | 外部系统仍需解决 |
|---|---|---|---|
| Tight Boundaries | Permission、Hooks、Agent Scope | Sandbox、Worktree、Approval | Goal / Risk / Evidence Boundary |
| Agent Cohesion / Coupling | Subagent、独立 Context | Thread、Worker、Worktree | Contract、Handoff、职责设计 |

---

# 5. 核心术语表修改

## 需要新增的术语

### Human Smoothing Effect

**中文建议：人类平滑效应**

工作定义：

> 在传统软件生产中，人类成员利用常识、项目经验、隐性知识、社会沟通和临场判断，自发修补需求、流程和信息中的不完整性、冲突与例外。

**状态：本书工作术语，暂不作为成熟学术术语引用。**

---

### Smoothing Gap

**中文建议：平滑缺口**

工作定义：

> 当执行工作转交给 Agent 后，原本由人类隐性承担的平滑和纠错能力无法被稳定假设存在，由此显现出的流程、Context、Boundary 和 Governance 缺口。

**状态：本书工作术语。**

---

### Tight Boundaries, Flexible Execution

**中文建议：明确边界，灵活执行**

定义：

> 对 Agent 的目标、状态、范围、权限、风险、证据和升级条件进行明确约束，同时允许其在边界内部自主选择执行路径。

---

### Contract over Reasoning Process

中文建议暂不强行翻译，可解释为：

> 优先管理 Agent 的输入、边界、责任、输出和升级契约，而不是控制或依赖其内部推理过程。

---

### Encapsulate Execution, Expose Evidence

**中文建议：封装执行过程，暴露验证证据**

定义：

> Agent 内部的搜索、实验和调整可以被封装，但外部必须能够获得支持判断的结果、Evidence、Risk 和必要 Trace。

---

### Agent Cohesion

**中文建议：Agent 职责内聚**

定义：

> 一个 Agent / Worker 围绕单一明确职责，拥有完成任务所需的相关 Context、Tool、Skill 和局部决策权限。

---

### Agent Coupling

**中文建议：Agent 耦合**

定义：

> Agent 之间对彼此内部状态、隐性上下文、推理过程和执行细节的依赖程度。理想情况下应通过 Contract、State、Evidence 和 Structured Handoff 降低不必要耦合。

---

### Task Cohesion

**中文建议：任务内聚**

定义：

> 一个任务是否具有足够明确的目标、上下文与完成边界，可以由单个 Worker 在最少外部协调下完成闭环。

---

# 6. 前言和导读的可选微调

## 结论

**不建议大改。**

两者当前已经平衡，不应把新概念再次扩大为前言主轴。

---

## 6.1 前言可选增加一句

### 建议位置

在：

> “此时需要管理的，不只是输入给模型的一段文字，而是一个完整的软件生产环境。”

之后。

### 可增加

> 传统团队中，许多模糊和例外原本可以由资深成员凭经验和即时沟通自然吸收；当执行逐渐转交给 Agent 后，这些隐性纠错能力不能再被默认存在，也就需要被更明确地写入边界、上下文、证据和升级机制。

仅一段即可。

---

## 6.2 导读可选增加一句

在介绍 Agent Reliability 或 Governance 时加入：

> AI-native 的严格并不意味着把 Agent 变成脚本。更合理的方向是“明确边界，灵活执行”：对目标、范围、权限和证据进行严格定义，在边界内部保留 Agent 的推理和执行空间。

同样不需要单独展开。

---

# 7. 第一章修改决定

## 结论

**第一章暂不修改。**

### 原因

第一章承担：

> 从 Tool Enhancement 到 Producer Change 的历史与角色演进。

Human Smoothing、Boundary、Cohesion 属于：

> 生产者变化之后为什么工程环境需要重新设计。

更适合第二章开始展开。

第一章最多可在未来统一润色时加入一个轻微伏笔，但当前没有必要。

---

# 8. 后续尚未成稿章节的写作约束

以下内容不需要“修改”，而应在正式写作时直接纳入。

## Agent Execution 章节

必须出现：

- Tight Boundaries, Flexible Execution
- Contract over Reasoning Process
- Agent Contract
- Task Cohesion
- Local Decision Authority

## Evidence 章节

必须出现：

- Encapsulate Execution, Expose Evidence
- Evidence over Confidence
- Evidence 与 Agent Encapsulation 的关系

## Cognitive Engineering 章节

必须说明：

> Transparency ≠ expose all execution details

而是：

> expose enough structured information for human verification and decision.

## Multi-Agent Organization 章节

必须正式讨论：

- Agent Cohesion
- Agent Coupling
- High Cohesion / Low Coupling 的理论迁移
- Structured Handoff
- Controller / Worker contract

## Governance 章节

Tight Boundaries 至少拆成：

```text
Goal Boundary
Scope Boundary
State Boundary
Authority Boundary
Risk Boundary
Evidence Boundary
```

---

# 9. 建议形成的新理论链

修改后，全书应更明确地形成以下推导：

```text
Traditional Human Team
        ↓
Tacit Knowledge
Common Sense
Social Communication
Professional Judgment
        ↓
Human Smoothing Effect
        ↓
Ambiguous processes can still work
        ↓
Agent takes over execution
        ↓
Smoothing cannot be assumed
        ↓
Smoothing Gap
        ↓
Tacit organizational capability
must become explicit engineering infrastructure
        ↓
Intent
Context
Truth
Boundary
Contract
Evidence
Escalation
        ↓
Tight Boundaries
Flexible Execution
        ↓
High Agent Cohesion
Low Agent Coupling
        ↓
Encapsulated Execution
Explicit Evidence
        ↓
Human Governance
+
Agent Autonomy
```

这条链应成为第二章通向后续方法论章节的重要桥梁。

---

# 10. 修改后的核心设计原则集合

建议全书最终至少固定以下原则：

## 1. Intent over Instruction

定义目标和约束，而不是机械规定所有操作步骤。

## 2. Code as Truth, Doc as Intent

区分当前现实与未来目标。

## 3. Tight Boundaries, Flexible Execution

边界明确，内部执行自治。

## 4. Contract over Reasoning Process

治理输入、责任、边界和输出，而不是微操 Agent 内部推理。

## 5. High Agent Cohesion, Low Agent Coupling

让 Worker 围绕明确职责完成闭环，并通过稳定 Contract 与其他 Agent 交互。

## 6. Encapsulate Execution, Expose Evidence

封装内部执行，显式暴露验证信息。

## 7. Evidence over Confidence

不接受无证据的完成声明。

## 8. Automation Default Off

能力不自动等于权限。

## 9. Risk-based Autonomy

自治程度由影响范围、可逆性、证据和历史可靠性决定。

## 10. Human Cognitive Authority

人类保留知情、判断、否决、接管和最终责任能力。

---

# 11. 修改优先级与执行顺序

## P0 — 下一轮应立即修改

1. 第二章正文
2. 主大纲中的第二章
3. 主大纲增加 AI-Native Design Principles
4. 核心术语表
5. 后续 Agent / Evidence / Organization 章节写作约束

## P1 — 主体稳定后修改

6. Claude Code / Codex 产品附录
7. 成熟度模型评估项
8. Appendix 对照表

## P2 — 最终统一润色时修改

9. 前言增加一段伏笔
10. 导读增加一句原则说明
11. 第一章视全书整体节奏决定是否增加伏笔

---

# 12. 本次变更是否影响全书结构

## 结论

**不需要重构当前 23 章结构。**

本次变化属于：

> 理论连接增强，而不是章节体系推翻。

它主要补足了三个此前尚未完全连接起来的问题：

### 1. 为什么 AI-native 需要更精确的工程边界？

因为传统团队存在 Human Smoothing，而 Agent 环境存在 Smoothing Gap。

### 2. 为什么更严格的工程标准不等于把 Agent 脚本化？

因为正确原则是：

> Tight Boundaries, Flexible Execution.

### 3. 传统软件工程原则如何迁移到 AI-native？

High Cohesion / Low Coupling 从 Code Module 层向 Agent / Workflow / Organization 层扩展：

```text
High Cohesion
→ Agent Cohesion

Low Coupling
→ Contract-based Agent Interaction

Encapsulation
→ Flexible Execution

Interface
→ Agent Contract

Test
→ Evidence / Eval
```

因此，本次修改将使《Beyond Code》的核心论证更完整：

> AI-native 软件工程不是抛弃传统软件工程，而是在智能执行者加入生产系统以后，将传统成熟原则重新映射并扩展到“生产软件的智能系统”本身。
