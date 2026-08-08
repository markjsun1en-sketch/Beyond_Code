# Beyond Code: AI-Native Software Engineering
## 第三章补充文档：Agent Harness Engineering 与 AI-Native Software Engineering 的关系

> 本文档用于补充《第3章 什么是 AI 原生软件工程》。
>
> 目标不是新增独立章节，而是在第三章中增加一个专门小节，主动回答一个熟悉 Agent / Claude Code / Codex 的读者很可能提出的问题：
>
> > **AI-Native Software Engineering 和 Agent Harness Engineering 到底是什么关系？**
>
> 本补充建议作为第三章正式修订时的直接插入稿使用。

---

# 1. 修改结论

## 建议

**单独讲，但不单独成章。**

最佳位置：

```text
3.1 为什么需要一个新的工程定义
3.2 一个工作定义
3.3 AI 原生软件工程管理两个系统

3.4 Agent Harness Engineering 与 AI-Native Software Engineering
    3.4.1 Harness 解决什么问题
    3.4.2 Harness 为什么不是完整的软件工程体系
    3.4.3 从 Mechanism 到 Engineering Discipline
    3.4.4 Harness 在三层模型中的位置
    3.4.5 从 Harness 到 Domain Operating Model

3.5 AI 原生不等于 Agentic
3.6 AI 原生也不等于最大自动化
...
```

原第三章中：

> 3.4 AI 原生不等于 Agentic

及后续编号整体顺延一位。

---

# 2. 为什么必须单独增加这一节

如果不主动解释，熟悉 Agent Engineering 的读者很容易产生一个自然质疑：

> “你这里讲的不就是 Agent Harness Engineering 吗？”

这个质疑是合理的。

因为今天很多 Agent Harness 已经包含：

- Model；
- Context；
- Tool Use；
- Agent Loop；
- State；
- Sandbox；
- Skills；
- Memory；
- Thread；
- Worktree；
- Permission；
- Retry / Feedback。

如果不把边界说明清楚，AI-Native Software Engineering 很容易被误解成：

> 给已有 Harness Engineering 换了一个更大的名字。

因此，这一节的任务不是贬低 Harness，而是明确：

> **Harness 是 AI-Native Software Engineering 的重要基础层，但不是完整的软件工程体系。**

---

# 3. 建议插入第三章的完整正文

# 3.4 Agent Harness Engineering 与 AI-Native Software Engineering

如果已经熟悉 Claude Code、Codex、SWE-agent 或其他软件开发 Agent，一个很自然的问题是：

> 前面讨论的这些问题，难道不就是 Agent Harness Engineering 吗？

这个问题值得在这里单独回答。

答案是：

> **两者高度相关，但并不等价。**

更准确地说：

> **Agent Harness Engineering 是 AI-Native Software Engineering 的重要基础层之一。**

Harness 主要解决：

> 如何把一个模型变成能够在真实环境中持续行动的 Agent。

而 AI-Native Software Engineering 进一步解决：

> 如何把这些 Agent 纳入一个长期可靠、可验证、可治理、可维护的软件生产体系。

这一区别可以理解为：

```text
Agent Harness Engineering
        ↓
让 Agent 能够工作

AI-Native Software Engineering
        ↓
让 Agent 驱动的软件生产体系
能够长期工作
```

---

## 3.4.1 Harness 解决什么问题

一个语言模型本身并不是一个完整的软件工程 Agent。

模型可以：

- 理解文本；
- 生成代码；
- 推理；
- 回答问题。

但如果它不能：

- 读取项目文件；
- 修改代码；
- 执行命令；
- 观察运行结果；
- 调用测试；
- 保存任务状态；
- 根据失败调整；
- 与外部工具交互；

它仍然只是一个推理与生成组件。

Agent Harness 的作用，就是把这些能力组织起来。

可以抽象为：

```text
Model
+
Context
+
Tools
+
Agent Loop
+
State
+
Execution Environment
=
Agent Harness
```

其中：

### Model

负责：

- 理解；
- 推理；
- 生成；
- 选择行动。

### Context

负责告诉模型：

- 当前任务；
- 项目状态；
- 相关文件；
- 工具说明；
- 历史信息。

### Tools

允许 Agent：

- 读写文件；
- 搜索代码；
- 运行命令；
- 调用 Git；
- 运行测试；
- 使用浏览器；
- 操作外部系统。

### Agent Loop

形成：

```text
Observe
→ Reason
→ Act
→ Observe
→ Revise
```

的执行闭环。

### State

保存：

- Thread；
- 当前任务；
- 工具返回；
- 工作区；
- 中间结果。

### Execution Environment

通过：

- Sandbox；
- Worktree；
- Container；
- Permission；

限制和承载 Agent 的真实行动。

因此，Harness Engineering 已经远远超过 Prompt Engineering。

Prompt Engineering 主要讨论：

> 怎样与模型交流。

Harness Engineering 开始讨论：

> 怎样为模型建立一个可以行动的工作环境。

---

## 3.4.2 Harness 为什么不是完整的软件工程体系

Harness 能够让 Agent 工作，并不自动回答：

> 这个 Agent 是否应该做这件事。

例如，一个 Harness 可能已经提供：

- 文件读写；
- Shell；
- Git；
- Test；
- Worktree；
- Memory；
- Skill。

但这些机制本身不会自动决定：

### Intent

这个任务真正应该达到什么目标？

### Truth

当前项目事实是什么？

### Boundary

Agent 被允许改到哪里？

### Authority

它能否：

- 修改公共 API；
- 改数据库；
- Merge；
- Deploy？

### Evidence

什么证据才足以证明完成？

### Human Decision

哪些地方必须由人类判断？

### Memory Governance

什么经验允许进入长期记忆？

### Accountability

当结果出错时，责任链如何重建？

Harness 提供：

> **Mechanism。**

AI-Native Software Engineering 则需要进一步提供：

> **Engineering Discipline。**

---

## 3.4.3 从 Mechanism 到 Engineering Discipline

这一差异可以通过几个例子看得更清楚。

### Context

Harness 问：

> 如何把 Context 提供给 Agent？

AI-native Software Engineering 还要问：

- Context 来自哪里？
- 是否过期？
- 是事实、意图还是推断？
- 多个来源冲突时相信什么？
- 哪些信息属于当前任务？
- 哪些内容不应进入 Context？

于是：

```text
Context Mechanism
→
Context Engineering
```

### Sandbox

Harness 问：

> 如何限制 Agent 的文件和命令访问？

AI-native Software Engineering 还要问：

- 为什么这个任务拥有这些权限？
- 风险等级是什么？
- 哪些操作需要升级？
- 权限什么时候撤回？
- 是否允许改变自身权限？

于是：

```text
Sandbox Mechanism
→
Governed Autonomy
```

### Memory

Harness 问：

> 如何让 Agent 记住过去？

AI-native Software Engineering 还要问：

- 什么值得记？
- 来源是什么？
- 谁批准？
- 何时过期？
- 是否只适用于当前项目？
- 错误记忆如何回滚？
- 如何避免 Memory Pollution？

于是：

```text
Memory Mechanism
→
Memory Engineering
```

### Test

Harness 问：

> Agent 能否运行测试？

AI-native Software Engineering 还要问：

- 哪个 Acceptance Criterion 由哪个 Test 验证？
- 测试覆盖了哪些风险？
- 哪些风险仍然没有证据？
- Test 是否来自当前 Commit？
- 测试通过是否足以支持“完成”？

于是：

```text
Test Execution
→
Evidence Engineering
```

### Multi-Agent

Harness 问：

> 能否同时运行多个 Agent？

AI-native Software Engineering 还要问：

- 谁拥有全局 Intent？
- 谁负责局部执行？
- 谁可以修改共享区域？
- 如何 Handoff？
- 如何解决冲突？
- 谁汇总结果？
- 谁决定停止？

于是：

```text
Parallel Agents
→
Multi-Agent Organization
```

因此：

> AI-Native Software Engineering 并不是简单增加更多 Harness 功能，而是把这些机制放入一个具有明确目标、责任、风险和生命周期的软件工程体系中。

---

## 3.4.4 Harness 在三层模型中的位置

前一节把 AI 原生软件工程分成：

```text
Product System
+
Production Intelligence System
```

进一步加上治理后，可以得到：

```text
Control & Evidence Plane
        ↓
Production Intelligence System
        ↓
Product System
```

Agent Harness 主要位于：

> **Production Intelligence System。**

其中包含：

```text
Agents
Agent Loop
Context I/O
Tools
Skills
State
Sandbox
Threads
Worktrees
```

也就是：

> Agent 实际运行所需要的执行基础设施。

AI-Native Software Engineering 则研究三层之间的完整关系。

## Control & Evidence Plane

负责：

- Intent；
- Truth；
- Boundary；
- Permission；
- Evidence；
- Review；
- Cognition；
- Trace；
- Evaluation。

## Production Intelligence System

负责：

- Agent；
- Tool；
- Context；
- Skill；
- Memory；
- Execution Loop。

## Product System

是最终被生产和修改的：

- Code；
- Data；
- Assets；
- Runtime；
- Infrastructure。

因此可以画成：

```text
Human Intent
      ↓
┌─────────────────────────┐
│ Control & Evidence Plane│
│                         │
│ Intent                  │
│ Truth                   │
│ Boundaries              │
│ Governance              │
│ Evidence                │
│ Review                  │
└────────────┬────────────┘
             ↓
┌─────────────────────────┐
│ Production Intelligence │
│                         │
│ Agent Harness           │
│ Agents                  │
│ Tools                   │
│ Skills                  │
│ State                   │
│ Memory                  │
└────────────┬────────────┘
             ↓
┌─────────────────────────┐
│ Product System          │
│                         │
│ Code                    │
│ Data                    │
│ Runtime                 │
│ Infrastructure          │
└─────────────────────────┘
```

这里可以得到一个重要结论：

> **Harness 解决 Production Intelligence 的运行问题；AI-Native Software Engineering 解决 Production Intelligence 如何与 Product System、人类和组织形成可靠生产闭环的问题。**

---

## 3.4.5 Harness Engineering 本身也正在向外扩张

Harness 与 AI-Native Software Engineering 之间并不是一条绝对边界。

现实产品正在不断扩展 Harness 的职责。

早期 Harness 主要关注：

```text
Tool Calling
Agent Loop
State
```

后来逐渐加入：

- Permission；
- Sandbox；
- Skills；
- Memory；
- Worktree；
- Subagents；
- Hooks；
- Review；
- Automation。

也就是说：

```text
Agent Harness
        ↓
Harness Engineering
```

本身正在变得越来越像一个小型生产系统。

这种演化很合理。

因为只要 Agent 开始参与真实工程，Harness 很快就会遇到：

- Context Drift；
- Permission Risk；
- Failure Recovery；
- Long-running State；
- Parallel Conflict；
- Evaluation。

因此，Harness Engineering 与 AI-Native Software Engineering 会存在大量交集。

区别不应通过：

> “这个功能到底属于谁”

来机械划分。

更好的区分方式是看它们回答的问题范围。

### Agent Harness Engineering

主要问题：

> **How do we make the agent work reliably as an execution system?**

关注：

```text
Model
Context I/O
Tools
Loop
State
Sandbox
Runtime
```

### AI-Native Software Engineering

主要问题：

> **How do we make agent-driven software production work reliably as an engineering system?**

进一步关注：

```text
Intent
Truth
Boundary
Evidence
Cognition
Governance
Memory Governance
Organization
Accountability
Economics
```

因此：

> Harness Engineering 可以继续向外扩张，但 AI-Native Software Engineering 的研究对象始终更大：它研究的是完整的软件生产体系，而不是单个 Agent Runtime。

---

## 3.4.6 从 Harness 到 Domain Operating Model

如果继续向上看，可以形成一个更完整的层级关系。

```text
Model
    ↓
Agent Harness / Runtime
    ↓
Agentic Workflow
    ↓
AI-Native Software Engineering
    ↓
Domain-specific Production Operating Model
```

需要注意：

这里不是纯技术调用栈。

AI-Native Software Engineering 更像横跨整个系统的工程方法论。

因此更严谨地画，可以写成：

```text
                     Engineering Methodology
             ┌─────────────────────────────────┐
             │ AI-Native Software Engineering  │
             └─────────────────────────────────┘
                         ↓ applies to

Model
  ↓
Agent Harness / Runtime
  ↓
Agentic Workflows
  ↓
Domain Production System
```

例如，在游戏开发领域：

```text
Model
    ↓
Claude Code / Codex
    ↓
Agent Runtime / Harness
    ↓
AI-Native Software Engineering Principles
    ↓
AI Game Dev OS
    ↓
Game Production
```

其中：

### Claude Code / Codex

主要提供：

- Agent Runtime；
- Tools；
- Worktree；
- Skills；
- Threads；
- Permission；
- Execution Interface。

### AI-Native Software Engineering

定义：

- Intent 如何表达；
- Context 如何治理；
- Truth 如何裁决；
- Boundary 如何设置；
- Evidence 如何形成；
- Review 如何进行；
- Memory 如何管理；
- 人类如何保持控制。

### AI Game Dev OS

把这些原则具体映射到：

- Game Design；
- Art；
- Programming；
- QA；
- Production；
- Runtime Validation；
- Asset Pipeline。

因此：

> **Agent Harness 是执行基础设施，AI-Native Software Engineering 是通用工程方法，而 Domain Operating Model 是领域实现。**

---

## 3.4.7 Harness 与 AI-native 的核心区别表

| 层面 | Agent Harness Engineering | AI-Native Software Engineering |
|---|---|---|
| 核心问题 | 如何让 Agent 能工作 | 如何让 Agent 驱动的软件生产体系长期可靠工作 |
| 主要对象 | Agent Runtime | 完整软件生产体系 |
| Model | 核心组件 | 基础能力之一 |
| Context | 加载与管理机制 | 来源、可信度、版本、冲突、适用范围 |
| Tools | Tool Calling | Tool 权限、风险、使用边界 |
| Sandbox | 执行隔离 | State / Authority / Risk Boundary |
| Memory | 存储与召回 | Provenance、污染、过期、审批、回滚 |
| Tests | Agent 可运行测试 | Evidence-Driven DoD |
| Multi-Agent | 并行与协调能力 | 组织、权责、Handoff、冲突、责任 |
| Review | 结果检查能力 | Pre / In-process / Post Review |
| Cognition | 通常非核心 | Human Cognitive Authority |
| Governance | Runtime 控制 | Risk-based Autonomy |
| Accountability | 通常较弱 | 完整责任链 |
| Evolution | Harness / Skill 改进 | Controlled Self-Evolution |

---

## 3.4.8 一句话区分

可以用两句话概括：

> **Harness makes the agent operational.**

> **AI-Native Software Engineering makes agent-driven software production governable.**

中文：

> **Harness 让 Agent 能够工作。**

> **AI 原生软件工程让 Agent 驱动的软件生产能够被长期管理。**

如果希望更强调长期工程：

> **Harness 解决 Agent 如何运行；AI-Native Software Engineering 解决使用 Agent 的软件组织如何长期运行。**

---

## 3.4.9 为什么这个区别重要

这个区别不仅是术语问题。

它直接影响系统设计。

如果把所有问题都视为 Harness 问题，很容易不断向 Runtime 中加入：

- 更多 Prompt；
- 更多 Tool；
- 更多 Memory；
- 更多 Hook；
- 更多 Agent。

最后得到一个越来越复杂的执行器。

但很多问题真正需要的是：

- 更明确 Intent；
- 更小 Scope；
- 更好的 Evidence；
- 更合理的组织角色；
- 更清晰的人类 Decision Point。

也就是说：

> 并不是所有 Agent 问题都应该通过增强 Agent 本身解决。

很多问题应该通过：

> **重新设计它所处的工程系统。**

这正是 AI-Native Software Engineering 独立出来的意义。

---

# 4. 对第三章现有内容的衔接修改

## 4.1 修改 3.3 结尾

原 3.3：

> AI 原生软件工程管理两个系统

建议在结尾增加：

> 在这两个系统之间，Agent Harness 承担了一个非常重要的中间角色：它把模型、Context、Tool、State 和执行循环组合成可以实际改变 Product System 的智能执行环境。但能够执行，并不等于已经形成完整的软件工程体系。下一节将专门解释 Harness Engineering 与 AI-Native Software Engineering 的关系。

---

## 4.2 原 3.4 顺延为 3.5

原：

> 3.4 AI 原生不等于 Agentic

改为：

> 3.5 AI 原生不等于 Agentic

开头可增加一句承接：

> Harness 解决了 Agent 的执行基础，而 Agentic 描述的是这种执行能力是否能够自主完成多步任务。但即使具备成熟 Harness 和较高 Agentic 能力，也不意味着项目已经形成 AI-native 软件工程体系。

---

## 4.3 修改“三层模型”小节

如果原第三章后部仍保留：

> Product System / Production Intelligence System / Control and Evidence Plane

建议在 Production Intelligence System 内明确标注：

```text
Production Intelligence System

├── Agent Harness
│   ├── Agent Loop
│   ├── Tools
│   ├── State
│   ├── Sandbox
│   └── Thread / Worktree
│
├── Skills
├── Memory
└── Context Runtime
```

这样 Harness 在整个理论中的位置一眼可见。

---

# 5. 对全书理论的影响

本补充**不改变全书核心结构**。

它主要解决：

> AI-Native Software Engineering 与现有 Agent Engineering / Harness Engineering 如何衔接。

因此理论链可以更新为：

```text
Prompt Engineering
        ↓
Context Engineering
        ↓
Agent Engineering
        ↓
Harness Engineering
        ↓
Agentic Workflow / Orchestration
        ↓
AI-Native Software Engineering
        ↓
Domain-specific Production Operating Model
```

但需要注明：

> 这不是严格的历史阶段，也不是互相替代的技术层。它更接近“问题范围逐步扩大”的概念关系。

---

# 6. 与《Beyond Code》核心原则的关系

Harness Engineering 与本书新增原则之间，可以进一步建立映射。

## Tight Boundaries, Flexible Execution

Harness 提供：

- Sandbox；
- Tool Permission；
- Worktree。

AI-native 进一步定义：

- Goal Boundary；
- Scope Boundary；
- State Boundary；
- Authority Boundary；
- Risk Boundary；
- Evidence Boundary。

## Contract over Reasoning Process

Harness 提供 Agent Loop。

AI-native 要求：

> 上层系统通过稳定 Contract 使用 Agent，而不是与其内部执行步骤强耦合。

## Encapsulate Execution, Expose Evidence

Harness 内部负责复杂执行。

AI-native 要求：

> 对外输出结构化 Result、Evidence、Risk 与必要 Trace。

## High Agent Cohesion, Low Agent Coupling

Harness 提供：

- Subagent；
- Thread；
- Worktree；
- Skill。

AI-native 定义：

- 一个 Worker 应承担什么职责；
- Context 应如何隔离；
- Handoff 应如何结构化；
- Agent 之间应依赖什么接口。

---

# 7. 与产品附录的关系

这一节也为 Claude Code / Codex 附录提供更清晰的分析框架。

不再简单问：

> Claude Code / Codex 是否已经实现 AI-Native Software Engineering？

而应分别问：

### Runtime / Harness 层

它们已经提供什么？

### AI-native Engineering 层

哪些能力仍需要：

- Repo Rules；
- Project Workflow；
- Organization Policy；
- AI Game Dev OS；

补充？

这样产品分析不会变成：

> 工具有 / 没有某功能

而是：

> 当前工具位于理论体系的哪一层。

---

# 8. 建议在第三章术语中新增

## Agent Harness

定义：

> 将模型、Context、Tool、State、Agent Loop 和执行环境组合起来，使模型能够持续观察、行动并完成真实任务的运行系统。

## Harness Engineering

定义：

> 围绕 Agent Harness 的可靠执行、工具使用、状态管理、隔离、恢复和扩展所形成的工程实践。

## Production Intelligence System

定义：

> 由 Agent、Harness、Context、Skill、Tool、Memory 和 Workflow 共同构成，用于生产或修改 Product System 的智能执行系统。

## Control and Evidence Plane

定义：

> 管理 Production Intelligence System 的 Intent、Truth、Boundary、Permission、Evidence、Review、Cognition、Trace 和 Evaluation 的治理层。

---

# 9. 最终推荐结论

第三章正式版本应主动建立以下关系：

```text
Model
    ↓
Agent Harness
    ↓
Agentic Execution
    ↓
──────────────────────────
AI-Native Software Engineering
作为工程方法论覆盖整个生产体系
──────────────────────────
    ↓
Domain Operating Model
    ↓
Product Development
```

其中最需要读者记住的是：

> **Agent Harness Engineering 让智能执行成为可能。**

> **AI-Native Software Engineering 则让这种智能执行能够进入长期、可靠、可治理的软件生产。**

这既承认 Harness Engineering 是重要基础，也明确了《Beyond Code》讨论的工程边界为什么比 Harness 更大。
