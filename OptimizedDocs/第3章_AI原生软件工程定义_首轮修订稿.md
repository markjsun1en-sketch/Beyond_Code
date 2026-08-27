# 第3章 什么是 AI 原生软件工程
## 从“使用 Agent”到工程化受托执行

> 工作稿状态：首轮逻辑修订稿，不替代 [第3章原稿](../OringinalDocs/第3章.md)。
> 回接说明：[RR-020](../RevisedResult/RR-020_前六章首轮分别调整说明.md)。
> 适用边界：本章把“真实执行路径委托”作为问题起点，把“工程环境适配”作为按影响、可逆性与授权风险选择的候选响应；这是一项书内分析约定，不是行业分类裁决或全对象清单。Control and Evidence Plane 是横切平面，不是第三个同级生产系统。

第1章讨论了一个角色变化：软件 Agent 开始在真实项目中接受开放式任务，读取项目材料，选择部分执行路径，并通过工具改变工程状态。

第2章进一步提出：当这种委托扩大到更长任务、更高风险、更多并发参与者或更难恢复的状态面时，一些过去可以由人类持续补齐的操作条件会变得不可靠。

但这两个现象还不能自动推出一个新学科。

如果“AI 原生软件工程”只是“使用了 AI”，它无法区分代码补全、单次 Agent Task 和长期受治理的智能生产系统。如果它只是“使用更多 Agent”，又会把执行能力误当成工程成熟度。

因此，本章需要回答三个问题：

1. 本书所说的 AI 原生软件工程以什么条件为起点？
2. 它管理哪些系统，又不管理哪些对象？
3. 它与传统软件工程、Agentic Development 和 Harness Engineering 是什么关系？

---

# 3.1 一个可判别的工作定义

本书采用以下工作定义。它是一项分析约定，不是从行业样本中发现的自然分类：

> **当智能代理承担真实项目中的部分执行路径时，本书把“如何根据这种委托的影响、可逆性与授权风险设计、运行和演化相应工程响应”的问题域及方法体系，称为 AI 原生软件工程。**

这个定义包含一个问题起点和一组候选工程响应。前者说明本书何时开始关注 AI-native 问题；后者说明本书准备检验哪些工程方法。它们不能被用来循环推出“所有被称为 AI-native 的项目都必须实现本书全部对象”。

## 问题起点：Delegated Execution（受托执行）

Agent 不只是提供候选文字，而是在被授予的范围内完成部分真实执行路径，例如：

- 读取并选择项目材料；
- 制定或调整局部方案；
- 修改文件、配置或其他受控状态；
- 调用工具并根据反馈继续行动；
- 产生需要被验证、接受或拒绝的工程结果。

这里的关键词是“被委托”。Agent 不天然拥有目标、路径、权限或裁决权；这些能力来自明确或隐含的 Delegation、Policy 和工具边界。

## 候选响应：Engineering Adaptation（工程环境适配）

当受托执行扩大影响面、延长时间、增加状态分叉或提高恢复成本时，项目可以针对这些风险建立可裁剪的机制，例如：

- Intent 与任务范围；
- Context 的选择、来源和更新；
- State、Decision、Assumption 与 Evidence 的区分；
- 工具、数据和写入权限；
- 验证、审查和用途裁决；
- 失败后的恢复、接管和责任追踪。

如果没有真实执行路径的委托，本书通常把实践放在 AI-assisted Development 一侧。如果已经发生 Delegated Execution，却没有足以覆盖当前风险的工程响应，本书把它描述为 Agentic Execution 与相应的治理缺口；这不意味着低风险任务必须持久化后文全部对象。

采用 Engineering Adaptation 的理由不能来自这一定义本身，而要来自可独立检查的风险：Agent 是否能够改变真实状态，Authority 与工具可达性是否分离，观察者是否可能改变目标，以及失败是否难以恢复。后续章节提出的对象都是对这些风险的候选响应，不是由术语自动推出的必要清单。

---

# 3.2 AI-assisted、Agentic 与 AI-native 不是一条成熟度阶梯

三个词经常被放在同一条从低到高的路线中，但它们描述的并不是同一个维度。

## AI-assisted Development

描述一种协作模式：

```text
Human controls the task
→ AI proposes a candidate
→ Human selects, applies and verifies
```

AI 可以显著影响结果，但真实执行路径主要仍由人类掌握。

## Agentic Development

描述一种执行能力：

```text
Human or system delegates a bounded task
→ Agent selects and performs multiple steps
→ Result returns to an authorized decision path
```

它回答“Agent 能否在限定环境中持续行动”，不自动回答该环境是否具有充分的状态、证据、恢复和治理能力。

## AI-native Software Engineering

描述一种工程响应：

> 当受托执行成为项目的真实生产条件时，工程体系是否针对这种条件被重新设计。

因此更准确的分析方式是两个轴：

```text
Axis A: Execution Delegation
候选建议 ←────────────→ 多步真实执行

Axis B: Engineering Adaptation
临时使用 ←────────────→ 状态、证据、恢复与治理被系统化
```

一个项目可以有很强的 Agentic Capability，却只有临时性的治理；也可以只委托少量高风险动作，却为这些动作建立严格的 AI-native 边界。

多 Agent、长期 Memory、自我演化和高度自治都是可能增加复杂度的条件，不是 AI-native 的定义门槛，更不是所有项目应该追求的最高层级。

---

# 3.3 AI 原生软件工程管理两个被工程化的系统

本书区分两个系统。

## Product System（产品系统）

最终被交付、运行和维护的软件系统，包括：

```text
Code
Data
Assets
Runtime
Infrastructure
Configuration
```

传统软件工程的架构、测试、部署、安全和运维原则继续直接作用于这一系统。

## Production Intelligence System（生产智能系统）

参与生产 Product System 的智能执行环境，包括：

```text
Agents
Harnesses
Context assembly
Tools and permissions
Skills and procedures
Memory sources
Workflow and handoff
Evaluation mechanisms
```

它不是一个模型名称，也不是某个 Agent Framework。模型只是这个系统中的一个组件。

同一个模型在不同 Context、Tool、Policy、State 和 Evaluation 条件下，会形成不同的工程行为面。因此，项目需要评估和治理的是完整生产配置，而不只是模型能力。

---

# 3.4 Control and Evidence Plane 是横切平面，不是第三个生产系统

为了观察和约束前述两个系统，还需要一组横切能力：

```text
Intent and Decision references
State and Assumption records
Authority and permission
Execution boundary
Observation and Evidence
Review and disposition
Trace and recovery
Policy and evaluation
```

本书将这组能力称为 **Control and Evidence Plane（控制与证据平面）**。

它不与 Product System、Production Intelligence System 构成三个同级“产品”。它横切两个系统：

```text
                 Control and Evidence Plane
               ─────────────────────────────
               intent / state / authority
               observation / evidence / review
                         ↓        ↑
Production Intelligence System → Product System
          Agent execution           changed software
```

这里的 `Evidence` 不是天然的控制权。Evidence 支持或反驳 Claim；有权角色或被明确委托的 Gate 才能对具名用途作出处置。将二者放在同一个横切平面，只表示它们共同参与控制闭环，不表示它们属于同一类型。

---

# 3.5 与传统软件工程的关系：扩展作用面，不撤销基础

AI 原生软件工程不替代传统软件工程。

模块化、自动化测试、版本控制、最小权限、小步修改、可观测性和可恢复性仍然重要。变化在于，这些原则除了作用于 Product System，也开始作用于 Production Intelligence System。

例如：

| 传统作用面 | 在智能生产系统中的对应问题 |
|---|---|
| 模块职责 | Agent、Skill 或 Workflow 是否拥有清晰职责 |
| 接口 | Agent Contract、Tool Schema 与 Handoff 是否明确 |
| 版本 | Context、Policy、Skill 与 Model 是否可识别 |
| 最小权限 | Agent 能读、写、执行和发布什么 |
| 测试 | Harness、Tool、Workflow 与目标结果分别如何验证 |
| 可观测性 | 外部可见的输入、动作、产物、结果和失败是什么 |
| 回滚 | 状态变化、规则变化和能力升级怎样撤回或隔离 |

这种映射只是设计启发，不意味着 Agent 与软件 Module 在本体上相同。Agent 的行为还受到模型版本、上下文选择、运行反馈和授权环境影响。

---

# 3.6 与 Harness Engineering 的关系

Harness Engineering 通常关注智能执行环境怎样获得：

- Context；
- Tool；
- State；
- Sandbox；
- 执行循环；
- 反馈和恢复能力。

AI 原生软件工程还讨论：

- 为什么执行某项工作；
- 谁能改变目标和 Policy；
- Product System 的结果怎样被接受；
- 人类组织如何理解、接管和承担责任；
- 经验怎样进入 Memory、Skill 或后续制度；
- 这些机制的成本是否值得。

二者大量重叠，边界也会随着工程实践变化。本书不采用 `Harness Engineering ⊂ AI-native Software Engineering` 这样的行业公认集合关系，只作范围声明：

> 在本书中，Harness Engineering 主要分析智能执行环境本身；AI 原生软件工程采用更宽的生产系统、产品系统和组织责任视角。

---

# 3.7 从 Human Smoothing 到风险相称的显式工程

人类团队经常依赖默契、经验和即时沟通补足不完整流程。本书把这种持续补齐称为 Human Smoothing Effect（人类平滑效应）。

Agent 也可能发现歧义并主动询问，但工程系统不能把“每次都能正确补齐”当成可靠前提。

这不意味着所有隐性知识都必须进入 Registry。显式化本身会产生维护、过期、错误 Authority 和认知负担。

更稳妥的规则是：

> 高影响、高复用、跨角色、易漂移或失败后难恢复的边界与知识，应优先进入可检查的外部记录；低风险、局部且易验证的工作可以使用轻量约定。

需要被显式化的通常不是 Agent 的全部过程，而是：

```text
Goal and non-goal
State and scope references
Authority and permission
Known assumptions and conflicts
Required observation and evidence
Escalation or recovery path
```

---

# 3.8 Tight Boundaries, Flexible Execution

本书将这一设计取向称为：

> **Tight Boundaries, Flexible Execution。**

中文语义是：

> 明确任务边界，在边界内保留与风险相称的执行裁量。

“明确”不等于把所有步骤写死，“灵活”也不等于让 Agent 自行决定目标与权限。

一组常用检查面包括：

| 边界 | 回答的问题 |
|---|---|
| Goal Boundary | 当前要解决什么，哪些结果不属于本次任务 |
| Scope Boundary | 可以改变哪些文件、模块、数据或服务 |
| State Boundary | 从哪个 Repository、Build、Runtime、Data 或 Config 状态开始 |
| Authority Boundary | Agent 可以提出、执行或裁决什么 |
| Risk Boundary | 哪些条件触发 Block、Isolation、Evidence Collection 或 Escalation |
| Evidence Boundary | 什么材料支持什么范围的完成 Claim |

这六项是本书的工作检查表，不是已经证明穷尽所有项目的固定分类。安全关键、数据密集或受监管项目还可能需要更具体的边界。

---

# 3.9 Contract over Hidden Reasoning

项目不应把不可读取的模型隐藏推理当作审计依赖。

更可治理的对象是外部可检查的 Contract：

```text
Input references
Goal and scope
Allowed actions
Forbidden actions
Expected outputs
Required evidence
Escalation conditions
Completion and handoff rules
```

这并不表示“内部过程完全不重要”。Tool calls、文件变化、测试输出、错误、Checkpoint 和可观察消息仍然是过程证据。边界在于：

> 管理可观察的输入、动作、状态变化和结果，不要求系统读取或保存隐藏思维过程。

---

# 3.10 Encapsulate Execution, Expose Evidence

Agent 可以在限定范围内搜索、规划、试验、实现和调试，而不需要人类批准每个微步骤。

但执行封装不能成为不可观察的黑盒。至少需要暴露与当前风险相称的：

- 实际修改了什么；
- 使用了哪些版本与状态引用；
- 哪些验证实际运行；
- 验证观察了什么；
- 哪些失败发生在目标观察之前；
- 哪些 Claim 只覆盖有限 Scope；
- 哪些未知、冲突和用途裁决仍未关闭。

这形成一条关系：

```text
Encapsulated execution
        ↓ produces
Observable changes + Evidence
        ↓ supports / challenges
Claim in Scope + declared Coverage
        ↓ informs
Authority-bound Decision Record
        ├── targets ──> named Decision Target
        └── records ─> Target-specific Disposition
```

---

# 3.11 Evidence over Unsupported Confidence

“Evidence over Confidence”不表示所有 Evidence 可以排成统一强弱阶梯。

Diff、Static Analysis、Test、Runtime Capture、人工体验评审和生产指标回答的是不同问题。哪一种更适用，取决于：

```text
Claim
Scope
Risk
Intended Use
Observation Boundary
```

例如：

- Diff 可以直接回答“本次修改是否触及公共 API”；
- Runtime Capture 可以回答“特定 Build 与场景中界面是否重叠”；
- 人工评审可能对审美或价值取舍拥有最终裁决权；
- Test PASS 只支持被执行检查的结果，不自动批准实现范围、采用或发布。

因此需要分开两条路径：

```text
Evidence / Validation Rule
→ Validation Coverage

Authorized Role or Delegated Gate
→ Acceptance / Adoption / Release Authorization Disposition
```

只有 Gate 获得明确的限定委托时，机器结果才能同时触发相应处置。

---

# 3.12 Human Cognitive Authority

本书保留 Human Cognitive Authority（人类对需要 Human Judgment 之事项保留的最终认知裁决权）这一原则，但不把它理解为人类必须阅读全部过程或亲自执行所有决定。

它要求组织在重要决策上保持：

- 定位原始 Evidence 的能力；
- 理解 Claim、Scope 与不确定性的能力；
- 识别自动化越权或证据缺口的能力；
- 否决、暂停、接管和恢复的能力；
- 对价值取舍与最终责任进行归属的能力。

低风险、可逆且被 Policy 明确委托的裁决可以自动化。Human Authority 的核心不是“每一步人工点击”，而是自动化边界、委托来源和接管路径仍然可被组织理解和改变。

---

# 3.13 Risk-based Autonomy

Agent 的模型能力、工具能力和自治授权不是同一件事。

治理强度不应只随“模型更强”单调增加。它更接近以下因素的组合：

```text
Granted Action Surface
× Impact
× Irreversibility
× State Uncertainty
× Verification Difficulty
× Recovery Cost
```

同一个高能力模型在只读、隔离环境中可能只需要轻量治理；一个能力较弱但拥有生产数据写权限的自动化系统反而需要更严格边界。

可选处置不只有“询问人类”：

```text
continue within scope
narrow
collect evidence
isolate
block
invoke delegated gate
escalate
```

具体 Policy 由项目风险和组织责任决定。

---

# 3.14 AI 原生软件工程的问题空间

后续章节把问题空间分成若干职责面。它们不是互斥学科，也不是成熟度等级。

## Desired Outcome

- Intent Engineering：目标、动机、范围和验收目标怎样跨执行保持身份。

## Supplied Information and Typed Records

- Context Engineering：哪些信息被选择、装配、传输和记录。
- Truth and State Architecture：State Claim、Decision、Assumption 与 Evidence 怎样保持类型和适用边界。

## Execution and Trust

- Agent Execution：执行权限、Contract、状态变化和恢复。
- Reliability：允许行为、失败模式和可重复评估。
- Verification and Evidence：观察、覆盖、反向证据与用途适配。
- Review Engineering：人类和自动审查怎样分工。

## Human Control

- Cognitive Engineering：人类如何理解高吞吐变化而不被摘要误导。
- Governed Autonomy：委托、Policy、Gate、介入和接管。
- Observability and Intervention：如何知道发生了什么并及时停止。

## Learning and Organization

- Memory Engineering：哪些记录值得保留、失效和检索。
- Self-Evolution Engineering：Skill、Policy 与 Workflow 怎样受控变化。
- Multi-Agent Organization：角色、写入面、Handoff 和共享状态怎样协调。

## Cross-cutting Concerns

- Traceability and Accountability；
- Security、Privacy 与 IP；
- AgentOps、Evaluation 与成本。

章节边界用于减少概念重复，不表示这些问题在实际任务中按章节顺序发生。

---

# 3.15 一个迭代的 AI-Native Software Development Lifecycle

传统 SDLC 仍然存在。当受托执行触发状态、授权、观察或恢复风险时，项目可能需要在其周围增加相应的控制循环。

一个更准确的工作模型是：

```text
Intent and trigger
        ↓
Minimum Initial Context
        ↕
Typed Record / Claim Resolution
        ↕
Progressive Retrieval
        ↓ sufficient for current boundary
Planning and Plan Review
        ↓
Governed Execution
        ↕
Continuous Observation
        ↓
Evidence and Claim Coverage
        ↓
Authorized Disposition
        ↓
Integration / Deployment / Rejection
        ↓
Memory and Controlled Evolution, when justified
```

这个模型不是要求每个任务走完所有节点，也不是严格单向流水线。

- Context 缺口可能把 Planning 拉回 Retrieval；
- 新 Observation 可能使 State Claim 失效；
- Evidence 缺口可能要求缩小 Claim，而不是继续执行；
- Human Disposition 可能接受 Evidence、拒绝范围或延后 Adoption；
- 只有经过选择的经验才进入 Memory、Skill 或 Policy。

---

# 3.16 AI-native 不是更重的流程

完整对象模型用于帮助思考，不要求所有项目持久化全部对象。

低风险、局部、易验证的任务可以把 Intent、Scope、State Reference 和 Evidence Requirement 压缩进一份短任务说明。

当任务具有以下特征时，才更可能需要稳定 ID、Manifest、独立 Review 或恢复记录：

- 跨会话或跨角色；
- 影响面大；
- 状态面可能分叉；
- 数据或发布不可逆；
- Authority 容易冲突；
- 失败后重建成本高。

工程目标不是最大化 Artifact 数量，而是用足够低的治理成本降低当前风险。

---

# 3.17 如何判断一个项目是否需要更强的 AI-native 机制

与其给项目打统一成熟度分数，不如检查触发条件：

1. Agent 是否直接改变真实项目状态？
2. 它被委托了多少开放式路径选择？
3. 当前 State、Intent 与 Decision Authority 是否可能分离？
4. 任务是否跨会话、跨 Agent 或跨仓库？
5. 失败是否容易恢复？
6. 验证结果能否覆盖实际 Claim？
7. 自动化是否获得明确的写入与裁决授权？
8. 人类是否能在不阅读全部原始产出的情况下定位关键 Evidence？
9. Memory、Skill 与 Policy 是否可能过期或扩大权限？
10. 最终责任和接管路径是否清楚？

回答“是”的数量不是成熟度分数。每个问题只用于判断某种工程机制是否值得引入。

---

# 3.18 AI 原生软件工程最终优化什么

Generation Throughput（生成吞吐）不等于 Engineering Productivity（工程生产率）。

一个完整评价至少需要分别观察：

- Outcome Quality：结果是否解决原问题；
- Reliability：相似条件下是否可持续获得可接受结果；
- Evidence Coverage：完成 Claim 获得了什么范围的支持；
- Human Cognitive Cost：人类理解与裁决需要多少成本；
- Recovery Cost：失败、漂移或中断后恢复有多难；
- Governance Cost：边界、审查和记录本身消耗多少；
- Learning Efficiency：有效经验是否能被筛选、复用和撤销。

这些指标可能相互冲突。例如，更完整的 Trace 可以降低恢复成本，却增加治理和认知成本。AI-native 工程不是把它们压成一个总分，而是在具体任务中作出可解释权衡。

---

# 3.19 本章结论

AI Agent 的重要变化不只是生成更快，而是可以在真实项目中接受受托执行。

AI 原生软件工程也不是 Agentic Capability 的同义词。它是对受托执行条件的工程响应：

```text
Delegated execution
+ Engineering adaptation
= AI-native software engineering in this book
```

它同时管理：

```text
Product System
+ Production Intelligence System
```

并通过横切的 Control and Evidence Plane 建立 Intent、State、Authority、Observation、Evidence、Review 与 Recovery 的闭环。

最终目标不是最大自治，也不是最大治理，而是：

> 在扩大软件生产能力的同时，让目标仍可追踪、状态仍可检查、行动仍受授权、结果仍可验证、失败仍可恢复、责任仍可归属。

---

# 本章原则

1. **AI-native 由执行委托与工程适配共同定义。** 单纯使用 AI 或运行 Agent 不足以完成定义。
2. **Agentic 是能力维度，AI-native 是工程响应。** 二者不构成单轴成熟度。
3. **管理两个系统。** Product System 与 Production Intelligence System 都需要工程化。
4. **Control and Evidence Plane 是横切能力。** 它不是第三个同级产品系统。
5. **Tight Boundaries, Flexible Execution。** 严格的是目标、范围、状态、权限与证据边界，不是所有内部步骤。
6. **Contract over hidden reasoning。** 管理可观察输入、行动、状态变化和结果。
7. **Evidence fit over evidence ladder。** Evidence 强度取决于 Claim、Scope、Risk 和 Intended Use。
8. **Validation Coverage 不等于 Acceptance Disposition。** 自动裁决需要明确委托。
9. **Human Authority 不等于人工微操。** 组织应保留理解、否决、接管和改变自动化边界的能力。
10. **Governance should fit risk and cost。** Artifact、Registry、Gate 和 Agent 数量都不是成熟度本身。

---

# 常见反模式

- 有 Agent 就宣称已经 AI-native；
- 把多 Agent、长 Context 或更大模型当作成熟度；
- 把 Control Plane 当成第三套需要复制全部对象的超级系统；
- 为了可靠而微操 Agent 的每个步骤；
- 为了自治而让 Agent 静默改变 Goal、Authority 或 Policy；
- 把不同 Evidence 排成脱离 Claim 的统一强度阶梯；
- 把 Test PASS 写成实现范围、采用或发布已经批准；
- 把隐藏推理当作项目必须保存的审计资产；
- 为所有小任务建立同等重量的 Registry、Graph 和 Gate；
- 只计算生成速度，不计算验证、恢复、认知和治理成本。

---

# 本章检查清单

- Agent 是提供候选，还是已经被委托真实执行路径？
- 项目是否针对这种委托调整了 State、Authority、Evidence 和 Recovery？
- AI-assisted、Agentic 与 AI-native 是否被误写成单一成熟度阶梯？
- Product System 与 Production Intelligence System 的边界是否清楚？
- Control and Evidence Plane 是否被误建成复制所有对象的第三系统？
- 当前 Agent 的 Goal、Scope、State、Authority、Risk 和 Evidence Boundary 是否明确？
- Contract 管理的是外部可观察对象，还是依赖隐藏推理？
- Evidence 是否绑定具体 Claim、Scope 与 Intended Use？
- Validation Coverage 与 Acceptance/Adoption/Release 是否分开？
- 自动 Gate 是否真的获得相应 Decision Target 的委托？
- 自治强度是否依据实际行动面、影响、可逆性和恢复成本？
- Context 与 State Resolution 是否允许迭代，而不是固定单向流程？
- 人类是否保留理解关键变化、否决、接管和追责的能力？
- 新机制带来的治理成本是否被计算？
