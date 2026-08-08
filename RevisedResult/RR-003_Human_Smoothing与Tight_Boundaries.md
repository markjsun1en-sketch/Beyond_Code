# RR-003：Human Smoothing 与 Tight Boundaries 变更说明审阅

- 记录日期：2026-08-08
- 审阅对象：[Human Smoothing、Tight Boundaries 与 Agent Cohesion 变更说明](../OringinalDocs/beyond_code_change_spec_human_smoothing_tight_boundaries_zh.md)
- 记录性质：既有对话审阅结论的结构化重建
- Human Disposition：`unreviewed`

## 核心结论

该文档有意义，因为它识别出一个能够连接全书多个主题的候选机制：传统团队会通过人的隐性知识、临场判断和沟通吸收流程中的缺口；Agent 进入生产后，这部分隐性纠错不再可靠，需要被转化为边界、Contract、Evidence 和升级机制。

但它目前更适合作为“全书变更假设与修改地图”，不适合作为已经验证的理论直接分发到多个章节。

## 有效部分

- Human Smoothing Effect 为第二章“旧假设失效”提供了更具体的中介机制。
- Tight Boundaries, Flexible Execution 能解释为什么可靠性不等于把 Agent 完全脚本化。
- Contract over Reasoning Process 和 Encapsulate Execution, Expose Evidence 与不可观察的内部推理边界相容。
- Agent Cohesion / Coupling 为多 Agent 章节提供了与传统软件设计原则连接的入口。
- 文档已经区分 P0、P1、P2 修改优先级，可作为后续修订 backlog。

## 尚未获得支持的部分

1. **Human Smoothing Effect 的范围。** 目前是解释性概念，需要通过同期记录、失败任务和反例说明它何时存在、由谁承担、成本是什么。
2. **Smoothing Gap 的因果强度。** Agent 暴露问题是合理推导，但不能默认所有失败都来自缺少人类隐性纠错。
3. **Tight Boundaries 与高内聚低耦合的关系。** 可以说是治理层映射，不能直接视为等价概念。
4. **全书结构不需要调整。** 文档关于“不需要重构当前 23 章结构”的结论缺少章节重复度和篇幅分析支持。
5. **术语扩散。** 一次引入 Human Smoothing、Smoothing Gap、Agent Cohesion、Task Cohesion 等多个术语，存在概念膨胀风险。

## 必须补充的操作性定义

### Human Smoothing

需要能够观察到：

- 输入或制度存在明确缺口；
- 人类进行了未被流程显式要求的纠正、补全或协调；
- 该行为改变了结果；
- 纠正行为的时间和认知成本可以被描述。

### Tight Boundary

边界至少需要说明：

- 保护的对象；
- 允许的动作；
- 禁止或需升级的动作；
- 违反边界如何被检测；
- 边界错误时如何修订。

### Flexible Execution

需要说明 Agent 仍然保留哪些局部选择，以及这些选择是否可观察、可撤销、可验证。

## 修改策略

- 第二章只吸收 Human Smoothing / Smoothing Gap 的最小定义和一个真实案例。
- 执行章节吸收 Tight Boundaries, Flexible Execution，并给出授权边界。
- Evidence 章节吸收 Encapsulate Execution, Expose Evidence。
- 多 Agent 章节再讨论 Cohesion / Coupling，避免提前展开完整理论。
- 术语表只保留在正文中得到案例和机制支撑的术语。

## 所需证据

- 一个资深开发者通过追问或隐性上下文修正模糊任务的实例；
- 一个 Agent 因同类缺口发生错误或返工的实例；
- 一个增加显式 Contract 或边界后仍然失败的反例；
- 边界带来的成本，包括文档负担、确认延迟或局部创造力下降。

## 当前裁决建议

保留这条理论链，但把所有定义标记为本书提出的工作概念；先选择少量章节最小化吸收，不能仅凭变更说明就断言 23 章结构无需调整。

