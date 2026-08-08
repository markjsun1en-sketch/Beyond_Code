# Beyond Code: AI-Native Software Engineering

## 从代码生产到智能软件组织

> 一套面向 AI 参与软件生产之后的新工程范式：如何管理意图、上下文、概率性执行、验证证据、人类认知带宽、自治边界、长期记忆与组织演化。

---

## 文档信息

- **文档类型**：书籍 / 长文章详细大纲
- **建议中文书名**：《超越代码：AI 原生软件工程》
- **英文主标题**：*Beyond Code: AI-Native Software Engineering*
- **建议副标题**：从代码生产到智能软件组织
- **目标读者**：软件架构师、技术负责人、AI Agent 工程师、产品与项目负责人、研发效能负责人、QA / DevOps 负责人，以及游戏、影视、工业软件等复杂数字生产领域的制作人
- **核心定位**：不是 AI 编程工具教程，而是讨论 AI 成为软件生产参与者之后，软件工程的流程、制度、组织与基础设施应如何重构

---

# 一、全书核心命题

传统软件工程主要解决：

> 如何让人类团队可靠地生产、验证、部署和维护软件。

AI 原生软件工程需要进一步解决：

> 如何让人类与概率性、上下文依赖、半自主的智能代理共同生产软件，同时保持结果可验证、过程可理解、权力可控制、经验可积累、系统可演化。

本书的基本判断是：

1. AI 带来的变化不只是编码效率提高，而是**软件生产者构成发生变化**。
2. 当 AI 从工具转变为执行者，传统软件工程中的若干隐含假设开始失效。
3. 软件开发的核心瓶颈会从“代码生产速度”逐步转移到“意图表达、上下文组织、结果验证、人类理解与治理能力”。
4. AI 原生软件工程不是替代传统软件工程，而是在传统软件工程之上增加新的工程层。
5. 人类不应通过逐行检查所有 AI 产出来维持控制，而应通过证据、认知压缩、风险分级、决策界面和自治治理保持主导权。

---

# 二、全书核心生命周期

```text
Human Intent
    ↓
Intent Formalization
    ↓
Context Assembly
    ↓
Truth / State Resolution
    ↓
Agent Planning
    ↓
Plan Review
    ↓
Governed Execution
    ↓
Continuous Observation
    ↓
Verification and Evidence
    ↓
Cognitive Compression
    ↓
Human Decision
    ↓
Integration / Deployment
    ↓
Memory Update
    ↓
Controlled Evolution
```

以下能力贯穿整个生命周期：

```text
Governance
Traceability
Security
Economics
Observability
```

---

# 三、AI 原生软件工程的问题空间

## 1. Intent Alignment

AI 是否理解人真正想实现的目标，而不是只完成字面任务？

## 2. Context Management

AI 是否获得了完成任务所需的正确、足够且不过期的项目知识？

## 3. Truth and State Management

当文档、代码、运行时、数据库和 Agent 推断发生冲突时，什么才是当前事实？

## 4. Agent Execution

Agent 如何规划、调用工具、执行任务、根据反馈调整，并在正确条件下停止？

## 5. Agent Reliability

如何处理非确定性、幻觉、工具失败、执行漂移、不可复现和失败恢复？

## 6. Verification and Evidence

AI 声称“完成”时，如何形成可验证的证据链？

## 7. Review Engineering

Review 是否应从纯事后检查扩展为执行前、执行中和执行后的全生命周期机制？

## 8. Cognitive Overload

当 AI 的生产速度超过人类的理解速度时，人类如何避免形式化 Review 和认知失控？

## 9. Governance and Autonomy

哪些任务可以自动执行，哪些需要审批，哪些必须由人类决定？

## 10. Observability and Intervention

人类如何持续看到 Agent 的目标、状态、风险、成本和阻塞，并在必要时接管？

## 11. Memory Engineering

项目事实、决策、经验、失败和技能如何被长期保存，又如何避免记忆污染？

## 12. Self-Evolution

Agent、Skill、Workflow 和组织结构如何基于经验改进，同时保持可审计、可验证和可回滚？

## 13. Multi-Agent Organization

多个 Agent 如何形成具有角色、权限、交接、冲突处理和升级机制的生产组织？

## 14. Traceability、Security 与 AgentOps

如何追踪每一次变化的来源、保护知识产权与数据边界，并管理模型、工具、成本和漂移？

---

# 第一部分：为什么传统软件工程需要扩展

---

# 第1章 软件工程的角色演进：从工具增强到智能协作

## 本章核心问题

软件工具的增强，与软件生产者本身的变化，有什么本质区别？

## 1.1 人类直接控制机器

早期软件开发中，人类显式表达全部执行逻辑：

```text
Human
  ↓
Code
  ↓
Machine
```

主要工程问题包括：

- 如何正确表达机器行为
- 如何控制程序复杂性
- 如何减少人为错误
- 如何建立可重复开发流程

## 1.2 工具增强人类开发

高级语言、IDE、版本控制、自动化测试、CI/CD、云计算和 DevOps 逐步提升人类效率：

```text
Human
  ↓
Development Tools
  ↓
Code
  ↓
Machine
```

这一阶段的共同特征是：

> 工具虽然越来越强，但意图、判断、理解和责任主要仍属于人类。

## 1.3 AI 成为软件生产参与者

AI 开始参与：

- 需求解释
- 任务拆分
- 技术方案设计
- 代码生成
- 重构
- 测试
- Review
- 文档
- 运维诊断
- 决策建议

新的生产关系变为：

```text
Human
  ↓
AI Agent
  ↓
Code / Configuration / Assets
  ↓
Runtime System
```

## 1.4 从 AI-assisted 到 AI-native

区分三个阶段：

### AI-assisted Development

AI 作为增强工具，人类仍控制主要步骤。

### Agentic Development

AI 可以自主规划和执行限定任务。

### AI-native Software Engineering

软件流程、权限、验证、组织和知识体系从一开始就按“人类 + Agent”共同生产设计。

## 1.5 本章结论

AI 的核心影响不是“让人写代码更快”，而是：

> 软件生产者从单一人类团队转变为人类与智能代理共同组成的生产系统。

---

# 第2章 传统软件工程的隐含假设正在失效

## 本章核心问题

传统软件工程在哪些前提下成立，而这些前提为什么在 AI 环境下不再可靠？

## 2.1 假设一：人类是主要代码生产者

传统 Review 默认生产者具有：

- 稳定的项目理解
- 可追问的设计意图
- 相对连续的责任归属
- 对自己代码的基本解释能力

AI 不天然具备这些条件。

## 2.2 假设二：变化速度不超过团队理解速度

传统情况下，代码生产与 Review 能力大致处于同一数量级。

AI 可能在几分钟内产生：

- 数十个文件修改
- 数千行代码
- 多层架构调整
- 大量测试与文档
- 多个并行方案

由此产生：

> AI Production Throughput > Human Understanding Throughput

## 2.3 假设三：执行者行为相对稳定

传统工具通常具有确定性。

Agent 行为可能受到：

- 模型版本
- Sampling
- 上下文顺序
- 上下文压缩方式
- 工具返回
- 中间执行状态
- 历史对话
- 隐含推断

影响。

## 2.4 假设四：项目知识主要存在于代码和文档中

AI 环境下，项目状态还分散在：

- Prompt
- Agent Contract
- Skill
- Memory
- Context Pack
- Tool Configuration
- Model Policy
- Historical Interaction
- Execution Trace

## 2.5 假设五：团队规模受人力约束

未来可能出现：

```text
1 Human Lead
+
20–100 Specialized Agents
```

组织成本不会消失，而会转化为：

- Agent 分工
- 上下文同步
- 任务冲突
- 权限边界
- 责任划分
- 输出压缩

## 2.6 假设六：人能够直接检查主要产出

当 AI 产出超过人类吸收能力后，“人工 Review”可能退化为：

- 快速扫一眼
- 只看是否测试通过
- 依赖 Agent 自我总结
- 在理解不足的情况下批准

## 2.7 假设七：软件的真实状态容易确定

AI 可能同时接触：

- 旧文档
- 新代码
- 未提交修改
- 不同分支
- 过期截图
- 历史决策
- Agent 推断

因此，“当前事实是什么”本身成为工程问题。

## 2.8 本章结论

传统软件工程仍然有效，但不足以单独覆盖：

> 概率性执行者、超高速产出、上下文依赖、认知失配和自治治理。

---

# 第3章 什么是 AI 原生软件工程

## 3.1 工作定义

AI 原生软件工程是：

> 研究如何设计、构建、验证、治理和演化由人类与智能代理共同参与的软件生产系统的工程学科。

## 3.2 它不替代传统软件工程

仍然需要：

- 软件架构
- 模块化
- 测试
- 版本控制
- CI/CD
- DevOps
- 安全工程
- 项目管理
- 质量保证

新增的工程能力包括：

- Intent Engineering
- Context Engineering
- Truth Architecture
- Agent Reliability
- Evidence Engineering
- Cognitive Engineering
- Governed Autonomy
- Memory Governance
- Self-Evolution Governance
- Multi-Agent Organization

## 3.3 传统软件工程与 AI 原生软件工程对比

| 维度 | 传统软件工程 | AI 原生软件工程 |
|---|---|---|
| 主要生产者 | 人类开发者 | 人类与 Agent |
| 核心输入 | 需求与设计 | Intent、Context、Constraint |
| 执行特征 | 相对确定 | 概率性、路径可变 |
| 核心资产 | Code、Doc | Intent、Context、Code、Memory、Skill |
| Review 对象 | 代码和设计 | 代码、Agent 行为、证据与风险 |
| 测试对象 | 软件行为 | 软件行为 + Agent 行为 |
| 速度瓶颈 | 编码与协调 | 验证、理解与治理 |
| 组织方式 | 人类团队 | Human-Agent Organization |
| 长期学习 | 人员经验 | Memory、Skill、Evolution |
| 控制机制 | 权限和流程 | 风险分级、Gate、Autonomy Policy |
| 状态追踪 | Git、Issue、CI | Decision Graph、Trace、Evidence、Context Snapshot |

## 3.4 软件工程目标的变化

传统目标：

> Build Correct Software

AI 原生软件工程增加：

> Build, Verify, Understand, Govern and Evolve Software with Intelligent Agents

## 3.5 本章结论

AI 原生软件工程的重点不是最大化自动化，而是：

> 在扩大智能生产能力的同时，保持系统可靠、人类可理解、权责可追踪、演化可控制。

---

# 第二部分：AI 软件生产的基础表达层

---

# 第4章 Intent Engineering：从模糊需求到可执行意图

## 本章核心问题

AI 如何知道人真正想实现什么，而不是只执行表面文字？

## 4.1 自然语言需求不等于可执行意图

需要区分：

- 用户表达
- 业务目标
- 项目目标
- 当前任务
- 隐含假设
- 非目标
- 验收标准
- 风险容忍度

## 4.2 Intent Object

```text
Goal
Motivation
Scope
Non-goals
Constraints
Assumptions
Priority
Risk
Acceptance Criteria
Required Evidence
Human Decision Points
```

## 4.3 Goal Decomposition

将目标拆分为：

```text
Outcome
→ Milestone
→ Task
→ Action
```

避免 Agent 在错误抽象层级直接执行。

## 4.4 Intent Alignment

在执行前确认：

- Agent 如何理解目标
- 哪些约束最重要
- 哪些结果不接受
- 哪些地方必须询问或升级
- 如何判定完成

## 4.5 Intent Drift

常见来源：

- 任务拆分失真
- Agent 自行补全
- 局部优化替代整体目标
- 历史决策丢失
- 需求变化未同步
- Worker 擅自扩展范围

## 4.6 Intent Registry

记录：

- 原始意图
- 当前版本
- 修改原因
- 决策者
- 适用范围
- 对应任务
- 失效条件

## 4.7 与传统需求工程的关系

传统需求工程主要服务人类团队。

Intent Engineering 还要服务：

> 不具备完整隐含背景、可能自行推断、并能直接执行操作的 Agent。

---

# 第5章 Context Engineering：为 AI 构建正确的工作世界

## 5.1 为什么 Prompt Engineering 不够

Prompt 通常解决一次交互。

长期软件工程需要：

- 当前代码状态
- 项目架构
- 历史决策
- 领域规则
- 禁止事项
- 工具能力
- 失败记录
- 当前分支和运行环境

## 5.2 Context 的组成

```text
Task Context
Project Context
Domain Context
Runtime Context
Historical Context
Policy Context
Tool Context
```

## 5.3 Context Selection

核心问题不是“越多越好”，而是：

- 哪些内容与当前任务相关
- 哪些内容必须完整保留
- 哪些内容可以摘要
- 哪些内容可能误导
- 哪些内容存在冲突

## 5.4 Context Budget

可以建立不同档位：

- Lean
- Standard
- Expanded
- Full

不同档位适配：

- 小修复
- 功能开发
- 架构重构
- 跨系统任务

## 5.5 Context Drift

常见问题：

- 过期文档继续进入上下文
- 已否决方案被重新采纳
- 当前分支与历史状态混淆
- 不相关脏改被误判为任务状态
- 摘要丢失关键例外
- Agent 自行将推断写成事实

## 5.6 Context Provenance

每段上下文应记录：

- 来源
- 更新时间
- 可信等级
- 是否为事实
- 是否为意图
- 是否为推断
- 是否经过验证

## 5.7 Context Compression

压缩的价值：

- 降低 Token 成本
- 提高相关性
- 减少上下文噪音

压缩的风险：

- 丢失关键例外
- 隐藏冲突
- 过度简化
- 将推断固化为事实

## 5.8 Context Governance

建立：

- 上下文版本
- 过期策略
- 可信度
- 权限
- 注入规则
- 更新责任

---

# 第6章 Truth、State 与 Decision Architecture

## 6.1 Doc as Intent, Code as Truth

文档表达：

> 想成为怎样。

代码表达：

> 当前实现是什么。

该原则用于防止：

- 旧文档覆盖当前实现
- Agent 根据目标描述虚构当前状态
- 把未来设计当作现有功能

## 6.2 Code 也不是全部事实

真实系统状态还包括：

- Build
- Runtime
- Database
- Deployment
- Asset
- Configuration
- External Service
- Feature Flag

## 6.3 Truth Hierarchy

可按项目建立事实优先级：

```text
Runtime Evidence
    >
Executable Tests
    >
Current Code
    >
Generated Artifacts
    >
Approved Decisions
    >
Documentation
    >
Agent Assumptions
```

## 6.4 Assumption Layer

Assumption 不能替代事实，应：

- 显式标注
- 记录来源
- 设定验证方式
- 设定过期时间
- 禁止静默升级为事实

## 6.5 Architecture Decision Record

记录：

- 为什么选择该方案
- 否决过哪些方案
- 有哪些代价
- 适用前提
- 何时需要重审

## 6.6 State Snapshot

为每次长任务记录：

- Commit
- Branch
- Worktree
- Dependency Version
- Context Version
- Agent Version
- Tool Version
- Runtime Environment

## 6.7 本章结论

AI 环境中的事实管理，不只是文档管理，而是：

> 对多来源状态、不同可信度和不同时间版本进行工程化裁决。

---

# 第三部分：执行、可靠性与验证

---

# 第7章 Agent Execution Engineering

## 7.1 Agent 与传统自动化的区别

传统自动化：

```text
Fixed Input
→ Fixed Procedure
→ Output
```

Agent：

```text
Goal
→ Plan
→ Act
→ Observe
→ Evaluate
→ Revise
```

## 7.2 基础执行循环

Agent 需要具备：

- 目标理解
- 计划生成
- 工具选择
- 环境观察
- 结果判断
- 路径调整
- 停止判断

## 7.3 Controller / Worker 模式

### Controller

负责：

- 保持目标
- 管理边界
- 分配任务
- 处理冲突
- 维护全局状态
- 汇总结果
- 触发人类决策

### Worker

负责：

- 在限定范围内执行
- 返回证据
- 报告阻塞
- 不擅自扩张任务
- 不修改治理规则

## 7.4 Planner / Executor 分离

同一 Agent 自规划自执行的风险：

- 计划为自己的执行辩护
- 目标漂移难以发现
- 难以独立检查方案
- 错误假设会贯穿全程

## 7.5 Tool Use

Agent 可能调用：

- 文件系统
- Git
- 编译器
- 测试
- 数据库
- 浏览器
- 游戏引擎
- 部署环境
- 外部服务

## 7.6 Agent Contract

明确：

- 能做什么
- 不能做什么
- 需要哪些输入
- 输出格式
- 停止条件
- 升级条件
- 证据要求
- 权限边界

## 7.7 Execution Scope

每次执行应定义：

- 任务范围
- 文件范围
- 模块范围
- 分支范围
- 环境范围
- 时间或成本预算

---

# 第8章 Agent Reliability Engineering

## 8.1 AI 错误分类

- Intent Error
- Context Error
- Planning Error
- Tool Error
- Execution Error
- State Error
- Verification Error
- Reporting Error

## 8.2 非确定性与可复现性

记录：

- 模型
- 模型版本
- Context Snapshot
- 工具返回
- 环境状态
- 执行路径
- 关键中间决策

## 8.3 Retry 的局限

重复执行可能：

- 解决偶发失败
- 产生不同失败
- 放大副作用
- 增加成本
- 掩盖根本问题

Retry 需要：

- 失败分类
- 次数限额
- 状态回滚
- 失败升级
- 新策略而非机械重试

## 8.4 Sandbox 与 Blast Radius

根据任务风险限制：

- 文件写入
- 分支权限
- 网络访问
- 数据库操作
- 部署权限
- 外部系统调用

## 8.5 Fallback 和 Recovery

包括：

- Agent 降级
- 模型切换
- 工具降级
- 人工接管
- 回滚
- Checkpoint 恢复
- 切换为只读模式

## 8.6 Reliability Metrics

- Task Success Rate
- First-pass Success
- Rework Rate
- Regression Rate
- Rollback Rate
- Human Intervention Rate
- Scope Violation Rate
- Evidence Failure Rate

## 8.7 本章结论

Agent Reliability 不是要求 AI 永不犯错，而是：

> 让错误可分类、可检测、可限制、可恢复。

---

# 第9章 Verification and Evidence Engineering

## 9.1 完成声明的四个层次

- Claimed Completion
- Observed Completion
- Verified Completion
- Accepted Completion

## 9.2 Evidence-Driven DoD

AI 任务的完成条件应包含：

- 实现证据
- 测试证据
- 运行证据
- 视觉证据
- 性能证据
- 回归证据
- 风险说明

## 9.3 Evidence Stack

```text
Text Explanation
→ Diff
→ Static Analysis
→ Automated Test
→ Runtime Observation
→ User-facing Validation
→ Production Metrics
```

## 9.4 Evidence Coverage

不仅问“有没有证据”，还要问：

- 哪个验收标准由什么证据支持
- 哪些风险没有覆盖
- 证据是否来自当前版本
- 证据是否能独立复现
- 证据是否只是 Agent 自述

## 9.5 Evidence Provenance

记录：

- 证据生成环境
- 对应 Commit
- 对应任务
- 生成工具
- 时间
- 是否自动
- 是否人工确认

## 9.6 Review Agent 的职责

Review Agent 主要回答：

- 是否正确
- 是否符合约束
- 是否引入回归
- 是否存在安全风险
- 是否满足 DoD

它不等同于帮助人类理解变化的 Cognition Agent。

---

# 第10章 Review Engineering：从事后检查到全生命周期 Review

## 10.1 事后 Review 的局限

当执行已经完成时：

- 改动范围可能过大
- 方向性错误已经扩散
- 返工成本更高
- 人类难以重建过程
- Review 容易只剩结果检查

## 10.2 Pre-execution Review

执行前检查：

- 目标理解
- 非目标
- 任务拆分
- 修改范围
- 风险假设
- 计划合理性
- 证据计划
- 回滚方式

## 10.3 In-process Review

在 Checkpoint 检查：

- 是否继续符合 Intent
- 是否出现范围扩张
- 是否出现新依赖
- 是否需要人类决策
- 是否触发停止条件
- 当前证据是否足够

## 10.4 Post-execution Review

执行后检查：

- 功能正确性
- 回归
- 架构影响
- 质量
- 安全
- 完成证据

## 10.5 Review Budget

Review 强度根据：

- 风险
- 影响范围
- 可逆性
- 新颖度
- 自动化证据覆盖
- 历史成功率

动态分配。

## 10.6 Review Agent 与 Cognition Agent 分离

Review Agent 回答：

> 做得对不对？

Cognition Agent 回答：

> 人应该如何理解这次变化，以及需要决定什么？

---

# 第四部分：人类认知、控制与干预

---

# 第11章 Cognitive Overload：AI 生产速度超过人类理解速度

## 11.1 认知带宽失配

```text
AI Production Throughput
    >
Human Review Throughput
```

## 11.2 Review 不等于阅读

真正理解一项修改，需要：

- 知道为什么改
- 知道结构如何变化
- 知道潜在副作用
- 能预测维护成本
- 能指出错误假设
- 能在未来接手 Debug

## 11.3 Review Fatigue

高频、大量输出导致：

- 机械批准
- 自动化偏见
- 注意力衰减
- 风险敏感度下降
- 对 Agent 总结的过度依赖

## 11.4 Cognitive Debt

定义：

> 系统中已经发生、但团队尚未真正吸收和理解的变化总量。

它不同于技术债：

- 技术债：实现质量和架构折衷
- 认知债：团队逐渐失去系统心智模型

## 11.5 Ownership Erosion

长期认知不足会导致人类失去：

- 设计主导权
- Debug 能力
- 架构判断
- 责任判断
- 对系统的真实所有权

## 11.6 认知过载的反直觉结果

AI 生产率上升，不一定带来真实研发效率上升。

瓶颈可能转移到：

- Review
- 理解
- 决策
- 协调
- 风险管理
- 返工

## 11.7 Cognitive Load Budget

可以为任务设定：

- 最大改动范围
- 最大同时决策数
- 最大未理解变更量
- 最大并行 Agent 数
- 人类 Review 时间预算

---

# 第12章 Cognitive Compression 与 Human Decision Interface

## 12.1 压缩的目标

不是隐藏信息，而是形成信息层级：

```text
Decision Summary
→ Risk and Impact
→ Evidence
→ Detailed Changes
→ Raw Diff and Logs
```

## 12.2 Progressive Disclosure

第一层只展示：

- 做了什么
- 为什么
- 风险在哪里
- 哪些需要人决定
- 是否建议合并

需要时下钻到：

- 模块
- 文件
- 函数
- Diff
- 原始执行记录

## 12.3 Change Narrative

将大量修改转化为因果链：

```text
原始问题
→ 设计选择
→ 主要变化
→ 系统影响
→ 风险
→ 证据
```

## 12.4 Architecture Impact View

展示：

- 受影响模块
- 新增依赖
- 数据流变化
- 接口变化
- 运行时变化
- 未受影响区域

## 12.5 Risk Map

按以下维度展示：

- 影响范围
- 可逆性
- 数据风险
- 运行时风险
- 用户体验风险
- 架构风险
- 安全风险

## 12.6 Decision Surface

人类重点关注：

- 不可逆决策
- 架构变化
- 数据迁移
- 范围扩张
- 新外部依赖
- 核心体验变化
- 安全边界变化
- Memory / Skill 更新

## 12.7 Compression 的可信问题

AI 生成摘要也可能错误，因此必须：

- 引用实际证据
- 链接到 Diff
- 标记推断
- 支持下钻
- 允许独立 Reviewer 交叉检查
- 不允许“无证据的高置信总结”

## 12.8 Human Cognitive Authority

人类应保有：

- 知情权
- 解释权
- 决策权
- 否决权
- 接管权
- 要求下钻的权利

---

# 第13章 Governed Autonomy：受治理的自治

## 13.1 自动化不是二元选择

可定义自治等级：

- L0：仅建议
- L1：生成方案，人执行
- L2：AI 执行，人逐次批准
- L3：低风险自动，高风险审批
- L4：目标级自治，持续监控
- L5：高度自治，仅异常升级

## 13.2 Risk-based Autonomy

自治等级由以下因素决定：

- 影响范围
- 可逆性
- 证据覆盖
- 历史成功率
- 环境敏感度
- 数据风险
- 安全风险
- 业务风险

## 13.3 Automation Default Off

在系统未证明可靠之前：

> 能力存在，不代表权限默认开放。

## 13.4 Permission Model

Agent 权限细化为：

- Read
- Write
- Execute
- Commit
- Merge
- Deploy
- External Access
- Memory Update
- Skill Update
- Permission Change

## 13.5 Stop-the-line

出现以下情况应停止：

- Intent 冲突
- 状态不一致
- 风险升级
- 证据缺失
- 范围异常扩大
- 不可逆操作
- 权限超界
- 工具行为异常

## 13.6 Human-in-the-loop 的真正目的

不是让人审批每一步，而是：

> 将人类注意力集中到高影响、高风险和不可逆决策上。

---

# 第14章 Observability and Intervention

## 14.1 Agent 为什么需要可观测性

需要观察：

- 当前目标
- 执行计划
- 已完成步骤
- 当前阻塞
- 工具调用
- 风险变化
- 成本
- Context 变化
- 权限使用
- Checkpoint 状态

## 14.2 Activity Timeline

将 Agent 执行转为可读时间线：

```text
Goal Received
→ Context Loaded
→ Plan Approved
→ Files Modified
→ Test Failed
→ Plan Revised
→ Evidence Collected
→ Awaiting Human Decision
```

## 14.3 State Dashboard

人类应快速知道：

- 哪些任务正在运行
- 哪些等待批准
- 哪些出现异常
- 哪些产生高风险变化
- 哪些 Agent 长时间无进展
- 哪些任务超出预算

## 14.4 Intervention Point

人类可以：

- 暂停
- 修改目标
- 缩小范围
- 更换 Agent
- 回滚
- 转人工
- 降低权限
- 要求重新规划

## 14.5 Observability 不是日志堆积

日志是原始数据。

可观测性必须形成：

- 状态
- 趋势
- 异常
- 风险
- 决策信息

---

# 第五部分：长期记忆、演化与智能组织

---

# 第15章 Memory Engineering

## 15.1 单次智能与组织智能

模型能力强，不代表项目具备长期记忆。

## 15.2 记忆类型

- Fact Memory
- Decision Memory
- Experience Memory
- Skill Memory
- Preference Memory
- Failure Memory
- Constraint Memory

## 15.3 Memory Provenance

每条记忆需要：

- 来源
- 时间
- 项目
- 适用范围
- 可信度
- 验证状态
- 失效条件

## 15.4 Memory Pollution

```text
错误结论
→ 写入记忆
→ 重复使用
→ 多次强化
→ 形成系统性偏差
```

## 15.5 记忆生命周期

```text
Capture
→ Validate
→ Store
→ Retrieve
→ Reconfirm
→ Deprecate
→ Delete
```

## 15.6 项目记忆与跨项目知识分离

避免把：

- 某项目特殊规则
- 一次性 workaround
- 临时偏好
- 特殊环境限制

错误泛化到所有项目。

## 15.7 Memory Review

记忆也需要：

- 定期审查
- 冲突检测
- 过期清理
- 适用范围校验
- 来源追踪

---

# 第16章 Self-Evolution Engineering

## 16.1 从执行经验到系统能力

```text
Execution
→ Reflection
→ Pattern Extraction
→ Rule Candidate
→ Validation
→ Skill Update
```

## 16.2 Self-Evolution 的层级

### 配置层

参数、路由、阈值、Context 选择。

### Skill / Workflow 层

执行步骤、工具组合、证据要求。

### Agent Contract 层

角色职责、权限、停止条件。

### Organization 层

Controller / Worker 分工、Review 结构、升级路径。

## 16.3 为什么不能自由自我修改

风险：

- 错误强化
- 目标漂移
- 安全边界削弱
- 评估指标投机
- 局部最优
- 组织复杂度失控

## 16.4 Evolution Gate

任何演化必须满足：

- 有来源
- 有对比基线
- 有评估
- 有审批
- 可回滚
- 有适用范围
- 有重新验证机制

## 16.5 Learning from Failure

失败应先分类：

- 偶发失败
- 环境失败
- 工具失败
- 推理失败
- 设计缺陷
- 流程缺陷
- 权限缺陷
- Context 缺陷

再决定是否转化为规则。

## 16.6 Self-Evolution 与 Self-Modification 的区别

- Self-Modification：系统自行改变
- Self-Evolution Engineering：系统在治理、评估和回滚机制下改进

---

# 第17章 Multi-Agent Organization Design

## 17.1 多 Agent 不等于组织

多个 Agent 并行可能导致：

- 重复劳动
- 决策冲突
- Context 不一致
- 权限重叠
- 责任不清
- 输出洪水

## 17.2 Agent 角色结构

可能包括：

- Controller
- Planner
- Specialist
- Reviewer
- QA
- Researcher
- Knowledge Miner
- Cognition Agent
- Security Agent
- Release Agent

## 17.3 Responsibility and Authority

每个角色明确：

- 对什么负责
- 可以决定什么
- 不能决定什么
- 向谁升级
- 输出给谁
- 需要什么证据

## 17.4 Structured Handoff

```text
Goal
Current State
Completed Work
Decisions
Assumptions
Evidence
Open Risks
Next Action
```

## 17.5 Agent Conflict Resolution

冲突处理：

- 事实优先级
- 角色权限
- 证据强度
- 风险升级
- 人类裁决

## 17.6 Controller / Worker 的组织意义

Controller 不只是任务调度器，还负责：

- 维持全局 Intent
- 控制上下文
- 限制 Worker 范围
- 汇总结果
- 管理认知负载
- 触发人类决策

## 17.7 Human-Agent Organization

人类角色逐步转为：

- 意图定义者
- 规则制定者
- 风险承担者
- 最终决策者
- 组织设计者
- 价值判断者

---

# 第六部分：责任、边界与运行基础设施

---

# 第18章 Traceability and Accountability

## 18.1 从 Git History 到 Decision Graph

Git 能回答：

> 改了什么？

但不一定能回答：

- 为什么改
- 谁批准
- 使用了什么上下文
- Agent 为什么选择该方案
- 有什么证据
- 哪些假设尚未验证

## 18.2 完整追踪链

```text
Intent
→ Context
→ Plan
→ Agent
→ Tool Action
→ Change
→ Evidence
→ Review
→ Decision
```

## 18.3 Accountability

责任不能简单推给模型。

需要区分：

- 系统设计责任
- 权限授予责任
- Agent 执行责任
- Review 责任
- 最终批准责任
- 部署责任

## 18.4 Audit Trail

高风险系统需要：

- 可查询
- 可重放
- 可解释
- 可检测篡改
- 有保留期限
- 有访问控制

## 18.5 Decision Reconstruction

当问题发生时，应能重建：

- 当时知道什么
- 当时假设什么
- 为什么做出该决策
- 谁批准
- 哪个证据后来被证明不可靠

---

# 第19章 Security、Privacy 与 IP Boundary

## 19.1 数据边界

区分：

- 公开信息
- 内部信息
- 商业机密
- 个人数据
- 受监管数据

## 19.2 Model Boundary

决定哪些任务：

- 可用云模型
- 需要私有部署
- 必须本地执行
- 禁止进入模型上下文

## 19.3 Tool and Agent Permissions

防范：

- Secret 泄露
- Prompt Injection
- 越权写入
- 恶意依赖
- 外部系统误操作
- 数据破坏

## 19.4 知识产权问题

包括：

- 输入数据权利
- 生成代码来源
- 第三方 License
- 训练数据争议
- Agent 生成资产归属
- 过程数据是否构成企业资产
- Skill 和 Memory 的所有权

## 19.5 Supply Chain Security

Agent 可能自动引入：

- Package
- Script
- Plugin
- MCP Server
- 外部 API
- 模型服务

因此供应链审查更加重要。

## 19.6 Local、Private 与 Cloud Boundary

需要按：

- 数据敏感度
- 成本
- 延迟
- 能力
- 合规
- 可维护性

建立混合运行架构。

---

# 第20章 AgentOps、成本与模型漂移

## 20.1 AgentOps 与 DevOps / LLMOps 的关系

AgentOps 关注：

- Agent 运行状态
- 工具调用
- 成功率
- 延迟
- 成本
- 失败类型
- 人工介入
- 权限使用
- Context 使用

## 20.2 成本模型

成本不仅是 Token：

- 模型调用
- 工具执行
- 构建资源
- 测试环境
- 人类 Review
- 返工
- 失败恢复
- 认知切换
- 组织复杂度

## 20.3 Model Routing

根据任务选择：

- 快速低成本模型
- 强推理模型
- 专用模型
- 本地模型
- 多模型交叉验证

## 20.4 Model and Tool Drift

模型或工具更新可能导致：

- 行为改变
- Prompt 失效
- Skill 退化
- 输出格式变化
- 评估结果漂移
- 成本变化
- 安全边界变化

## 20.5 Re-evaluation

模型升级不能只看公开 Benchmark。

需要重新运行：

- 项目基准任务
- 安全测试
- 可靠性测试
- 成本测试
- 行为回归测试
- Cognition 输出质量测试

## 20.6 Agent Economics

最终关注：

> AI 是否真正降低了总交付成本，而不是只降低了代码生成成本。

---

# 第七部分：形成完整的方法论

---

# 第21章 AI-Native Software Development Lifecycle

## 21.1 传统 SDLC

```text
Requirement
→ Design
→ Implementation
→ Test
→ Deployment
→ Maintenance
```

## 21.2 AI 原生 SDLC

```text
Intent Definition
→ Intent Review
→ Context Assembly
→ Truth Resolution
→ Plan Review
→ Governed Execution
→ Checkpoint Review
→ Evidence Collection
→ Cognitive Compression
→ Human Decision
→ Integration
→ Memory Update
→ Evolution Candidate
```

## 21.3 各阶段输入输出

| 阶段 | 输入 | 输出 |
|---|---|---|
| Intent | 人类需求 | 结构化目标、约束与非目标 |
| Context | 项目状态 | 可验证 Context Pack |
| Truth Resolution | 多来源信息 | 当前事实和显式假设 |
| Planning | Intent + Context | 执行计划、风险和证据计划 |
| Execution | 已批准计划 | 改动、运行结果与执行轨迹 |
| Verification | 改动 | 证据、缺陷和未覆盖风险 |
| Cognition | 大量结果 | 人类决策视图 |
| Decision | 压缩信息与证据 | 批准、拒绝、修改或回滚 |
| Memory | 已接受结果 | 受治理的项目经验 |
| Evolution | 经验候选 | 经过验证的 Skill / Workflow 改进 |

## 21.4 生命周期中的 Gate

- Intent Gate
- Context Gate
- Plan Gate
- Risk Gate
- Checkpoint Gate
- Evidence Gate
- Merge Gate
- Deployment Gate
- Memory Gate
- Evolution Gate

## 21.5 不同任务的流程裁剪

小任务不应走完整重流程。

需要 Adaptive Governance：

- 低风险任务：轻量 Context + 自动测试 + 简单摘要
- 中风险任务：计划 Review + Checkpoint + Evidence
- 高风险任务：完整链路 + 多 Agent Review + 人工决策

---

# 第22章 AI 原生研发成熟度模型

## Level 0：Ad Hoc Assistant

- 零散使用 Chat
- 无项目记忆
- 无正式验证
- 人工复制粘贴

## Level 1：Supervised Copilot

- AI 辅助编码
- 人类逐项 Review
- 传统流程为主
- 无独立 Agent 权限

## Level 2：Bounded Workflow Agent

- Agent 可执行限定任务
- 有工具权限
- 有基本证据
- 有回滚和 Sandbox

## Level 3：Governed Multi-Agent System

- Controller / Worker
- Context Registry
- Review Agent
- Risk-based Gate
- 可追溯 Handoff

## Level 4：Cognitive and Evidence-driven Organization

- 认知压缩
- 决策界面
- 全链路证据
- 可观测性
- 人类管理多个 Agent
- Review Budget

## Level 5：Controlled Self-Evolving Organization

- 经验可沉淀
- Skill 可演化
- 有评估与回滚
- 跨项目知识受治理迁移
- Agent 组织结构可优化

## 22.1 推荐迁移顺序

```text
Truth
→ Context
→ Evidence
→ Governance
→ Cognition
→ Memory
→ Evolution
```

不建议：

> 在没有 Truth、Evidence 和 Governance 的情况下直接追求自治与自我演化。

---

# 第23章 垂直实践：AI Game Dev OS

## 23.1 为什么游戏开发是合适的验证场景

游戏开发同时包含：

- 代码
- 美术
- 设计
- QA
- 内容
- 运行时验证
- 主观体验判断
- 多专业协同

因此它比纯代码场景更能暴露 AI 软件工程问题。

## 23.2 理论概念与 AI Game Dev OS 的映射

| 理论概念 | AI Game Dev OS 对应设计 |
|---|---|
| Intent Engineering | Doc as Intent |
| Truth Architecture | Code as Truth |
| Context Engineering | Context Packs |
| Agent Organization | Controller / Lead / Worker |
| Verification | Review Agent + Evidence-Driven DoD |
| Governance | Gate + Automation Default Off |
| Traceability | Registry + Handoff |
| Memory | LTM |
| Evolution | Self-Evolution |
| Cognition | Change Summary、Risk Map、Decision Surface |
| Observability | Timeline、Dashboard、Checkpoint |
| Reliability | Branch、Worktree、Sandbox、Rollback |

## 23.3 Player Status UI 优化案例

可按以下流程展开：

1. 人类提出体验目标
2. Controller 提取 Intent
3. 检查当前 Commit、Branch 和 Worktree
4. 构造 SP122 Context Pack
5. 执行前 Review 计划和范围
6. Worker 执行
7. 中途 Checkpoint
8. Review Agent 验证
9. Cognition Layer 压缩改动
10. 人类确认视觉层级和体验
11. 合并
12. 记录决策和经验
13. 评估是否更新 Skill / Pack

## 23.4 从游戏领域扩展到一般软件工程

区分：

### 游戏领域专属

- 美术风格
- 玩法体验
- 数值平衡
- 场景和内容生产

### 软件工程通用

- Intent
- Context
- Truth
- Verification
- Cognition
- Governance
- Memory
- Traceability

### 企业治理通用

- 权限
- 审计
- 安全
- IP
- AgentOps
- 成本

---

# 结语：软件工程的下一瓶颈

过去的软件工程瓶颈主要是：

> 人类生产软件的速度，以及管理复杂系统的能力。

AI 提高生产速度后，新的瓶颈逐渐变为：

- 意图是否准确
- 上下文是否可信
- 当前事实是否明确
- Agent 是否可靠
- 结果是否可验证
- 人类是否仍然理解系统
- 自治是否处于合理边界
- 组织是否能够安全学习
- 责任是否可以追踪

最终观点：

> AI 原生软件工程的目标，不是让 AI 尽可能多地替代人，而是建立一种工程体系，使智能代理能够高效生产，同时让人类始终保有认知、决策、责任和演化方向的主导权。

---

# 四、每章统一写作模板

为了避免写成松散概念合集，每一章建议采用统一结构。

## 1. 传统软件工程如何处理这个问题

建立历史和现实参照。

## 2. AI 环境改变了什么前提

指出范式变化，而不是只介绍新术语。

## 3. 出现了哪些新的失败模式

用具体案例说明问题。

## 4. 需要增加什么工程机制

提出结构、流程、角色和基础设施。

## 5. 如何验证机制有效

定义指标、证据和评估方式。

## 6. AI Game Dev OS 或其他实践案例

用真实工程过程落地。

每章结尾增加：

- **本章原则**
- **常见反模式**
- **可执行检查清单**
- **待验证假设**
- **开放问题**

---

# 五、压缩成长文章时的结构

如果先写一篇长文章，可压缩为以下八部分。

## 1. AI 为什么改变的是软件工程，而不只是编码效率

说明软件生产者发生变化。

## 2. 传统软件工程的七个隐含假设

展示传统方法为何需要扩展。

## 3. AI 原生软件工程的十四个核心问题

建立完整问题空间。

## 4. Intent、Context 与 Truth Architecture

解释 AI 如何获得正确目标和世界状态。

## 5. Agent 执行、可靠性与 Evidence-Driven DoD

解释 AI 如何可靠行动，以及如何证明完成。

## 6. Cognitive Overload、Cognitive Debt 与人类认知主权

阐述人类 Review 能力成为新瓶颈。

## 7. Governed Autonomy、Memory 和 Self-Evolution

说明 AI 组织如何在受控条件下扩大自治和积累经验。

## 8. 新的 AI-Native SDLC 与 AI Game Dev OS 案例

用完整流程展示理论落地。

---

# 六、可优先写作的核心文章

## 文章一

### 《AI 改变的不是编码效率，而是软件工程的基本假设》

重点：

- 软件生产者变化
- 七个传统假设失效
- AI 原生软件工程定义

## 文章二

### 《当 AI 写得比人看得更快：软件工程中的认知过载》

重点：

- Cognitive Overload
- Review Fatigue
- Cognitive Debt
- Ownership Erosion
- Human Cognitive Authority

## 文章三

### 《从 Code as Truth 到 Evidence-Driven DoD》

重点：

- Truth Architecture
- Verification Gap
- Evidence Stack
- Review Agent

## 文章四

### 《Agent 不是员工：为什么多 Agent 系统需要新的组织工程》

重点：

- Controller / Worker
- Agent Contract
- Handoff
- 权限
- 冲突处理

## 文章五

### 《自动化默认关闭：AI 软件工程中的受治理自治》

重点：

- Autonomy Level
- Risk-based Governance
- Stop-the-line
- Human-in-the-loop

## 文章六

### 《AI 系统如何学习而不污染自己》

重点：

- Memory Pollution
- Skill Evolution
- Evolution Gate
- 回滚和验证

---

# 七、建议保留的核心术语

| 英文 | 中文建议 |
|---|---|
| AI-Native Software Engineering | AI 原生软件工程 |
| Intent Engineering | 意图工程 |
| Context Engineering | 上下文工程 |
| Truth Architecture | 事实架构 / 真实状态架构 |
| Evidence Engineering | 证据工程 |
| Evidence-Driven DoD | 证据驱动的完成定义 |
| Review Engineering | Review 工程 / 审查工程 |
| Cognitive Overload | 认知过载 |
| Cognitive Debt | 认知债 |
| Cognitive Compression | 认知压缩 |
| Human Cognitive Authority | 人类认知主权 |
| Governed Autonomy | 受治理的自治 |
| Memory Engineering | 记忆工程 |
| Memory Pollution | 记忆污染 |
| Self-Evolution Engineering | 自我演化工程 |
| Agent Organization Design | Agent 组织设计 |
| Decision Surface | 决策界面 / 决策表面 |
| Context Provenance | 上下文来源追踪 |
| Evidence Provenance | 证据来源追踪 |
| Adaptive Governance | 自适应治理 |
| AgentOps | Agent 运行与治理体系 |

---

# 八、书名建议

## 推荐主标题

# Beyond Code: AI-Native Software Engineering

这个标题的优势：

1. **Beyond Code** 直接表达本书不只讨论代码生成。
2. 它能自然容纳 Intent、Context、Governance、Cognition、Memory 和 Organization。
3. 比单独使用“AI-Native Software Engineering”更有辨识度。
4. 适合未来同时面向技术、管理和生产负责人。
5. 不把内容限定在某个模型、框架或 AI Coding 工具上。

## 推荐中文对应

### 《超越代码：AI 原生软件工程》

副标题：

> 从代码生产到智能软件组织

也可以使用更强调人机关系的副标题：

> 人类与智能代理共同生产软件的新工程范式

## 不建议只使用英文标题而没有中文解释

对于中文读者，单独的 *Beyond Code* 容易显得偏泛。

建议始终搭配：

- 中文主标题
- 明确副标题
- 一句话定义

---

# 九、当前阶段仍需继续验证的开放问题

1. Cognitive Overload 是否可以形成可量化指标？
2. Cognitive Debt 应如何衡量和偿还？
3. Review Agent 与 Cognition Agent 是否应永久分离？
4. 哪些任务适合执行前 Review，哪些只需要事后验证？
5. 如何评价 AI 生成摘要本身的可信度？
6. 如何定义 Agent 组织中的责任，而不拟人化 Agent？
7. Memory Update 应由谁批准？
8. Self-Evolution 的最小安全闭环是什么？
9. 何时多 Agent 优于单 Agent？
10. AI-Native SDLC 是否需要按项目类型形成不同 Profile？
11. 如何衡量“人类仍然理解系统”？
12. 如何避免治理成本抵消 AI 带来的效率收益？
13. 如何将游戏开发中的主观体验证据纳入 Evidence Stack？
14. 企业级 AI 软件工程与个人开发者模式应如何分层？

---

# 十、建议下一步

1. 先以本大纲写一篇 8,000–15,000 字的理论总论。
2. 使用 AI Game Dev OS 作为贯穿案例，但不要让全书变成产品说明书。
3. 优先完整写出第 2、3、11、12、13 章，它们最能体现理论差异。
4. 再补 Intent、Context、Evidence、Memory 和 Evolution。
5. 最后形成 AI-Native SDLC、成熟度模型和实践手册。
