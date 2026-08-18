# RR-008：第四章 Prompt 边界优化说明审阅

- 记录日期：2026-08-10
- 审阅对象：[第四章优化说明](../OringinalDocs/beyond_code_chapter4_intent_vs_prompt_optimization_spec_zh.md)、[第四章正文](../OringinalDocs/第4章.md)
- 前序审阅：[RR-005](RR-005_第四章Intent_Engineering.md)
- 记录性质：正式改稿前的结构与概念审阅
- Human Disposition：`unreviewed`

## 核心结论

新优化说明回应了 RR-005 的主要问题：它主动承认 Intent 与高质量 Prompt 在内容字段上重叠，把新意转向 Identity、Lifecycle、Traceability、Inheritance 和 Runtime Binding。这个方向应当保留。

但该说明仍不宜原样执行。它在压缩旧内容的同时又引入 Intent Projection、Prompt Projection、Intent Graph、Intent Lifecycle 等一组新术语，且部分生命周期、所有权和 Runtime 表述仍过于绝对。此前“收窄学科宣称、补足授权模型、压缩章节”的结论保持不变。

## 主张裁决

| 主张 | 裁决 | 原因 |
|---|---|---|
| Intent 与优质 Prompt 的内容字段高度重叠 | `survives` | Goal、Constraint、Acceptance 等并非 Intent 独有 |
| Prompt 是 Runtime Input，Intent 是 Engineering Artifact | `narrow` | 是有用主区分，但 system prompt、持久指令和多轮会话也可能具有长期生命周期 |
| 一个 Intent 可以产生多个角色输入 | `survives` | 能解释 Controller、Worker、Reviewer 的不同执行视图 |
| Prompt 是 Intent 的运行时投影 | `narrow` | Agent Input 还包含 Context、Policy、Tool Schema 和系统指令；Prompt 不是纯 Intent 投影 |
| Intent 应独立于模型和 Runtime | `narrow` | 语义目标可保持稳定，但可行性、授权和验证要求可能依赖 Runtime 能力 |
| Agent 不能拥有 Intent | `split` | 最终价值目标属于人类/组织；Agent 可在委托边界内拥有局部目标制定权 |
| Intent Registry 是第四章核心基础设施 | `narrow` | 对长期、多 Agent 项目有用；小型任务不需要独立 Registry |
| 优化说明不改变全书结构 | `unsupported` | 只能证明无需立即改章节数量，不能证明后续跨章审计不会要求重组 |

## 必须修正的对象边界

### Intent Projection 与 Prompt Projection

建议只保留一个术语：`Execution View` 或 `Intent Projection`。运行时链路写成：

```text
Intent Artifact
        ↓ role-specific view
Intent Projection
        +
Context + Policy + Tools + Output Contract
        ↓ assembly / serialization
Agent Input
```

“Prompt Projection”只是最后的序列化步骤，没有必要与 Intent Projection 同时升级为核心概念。

### Intent Lifecycle 与 Execution Lifecycle

提案中的：

```text
Draft → Approved → Active → Executed → Verified → Accepted → Completed
```

混合了目标状态、执行状态和结果裁决。建议拆为：

```text
Intent lifecycle:
Draft → Approved → Active → Superseded / Cancelled

Execution lifecycle:
Planned → Running → Verified / Failed → Accepted / Rejected
```

同一个长期 Intent 可以对应多个 Execution，不应在第一次执行后自动“完成”。

### Intent Authority

建议替换绝对句：

> 最终价值目标及 Parent Intent 的变更权属于被授权的人类或组织角色；Agent 可在明确委托范围内派生、维护和修改局部 Intent，但不能静默扩大自身授权。

## 结构建议

当前优化说明建议 23 个正式小节，仍然偏多。建议第四章最终只保留十个主体模块：

1. Requirement、Intent、Task 与 Agent Input；
2. 与 Prompt/Requirements Engineering 的重叠和增量；
3. Intent Artifact 的最小字段；
4. Identity、Owner、Authority；
5. Hierarchy、Inheritance 与局部派生；
6. Version、Drift 与 Lifecycle；
7. Intent、Context、Truth、Contract 的边界；
8. Intent-to-Evidence Trace；
9. Risk-based Clarification 与可选治理 Profile；
10. AI Game Dev OS 案例与结论。

Intent Registry、Graph 和 Projection 可作为这些模块中的机制，不应各自扩成理论中心。

## 必要、实用与可选

- 必要：Intent 作为长期目标资产；父子目标；授权边界；版本；Evidence Trace。
- 实用：角色投影、Registry、Lifecycle 状态机。
- 可选：独立 Prompt Projection 术语、完整 Intent Graph 基础设施、所有任务统一 Profile。

## 当前裁决建议

接受优化方向，不按说明原样扩写。先用上述十个模块重构第四章，并继续执行 RR-005 对 Requirements Engineering、多方冲突、来源安全和主观 Acceptance 的修正要求。
