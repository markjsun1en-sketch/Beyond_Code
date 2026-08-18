# RR-009：第五章 Context Engineering 及 Patterns 审阅

- 记录日期：2026-08-10
- 审阅对象：[第五章正文](../OringinalDocs/第5章.md)、[第五章 Patterns 优化说明](../OringinalDocs/beyond_code_chapter5_context_patterns_change_spec_zh.md)
- 记录性质：正式改稿前的结构、概念与外部参照审阅
- Human Disposition：`unreviewed`

## 核心结论

第五章讨论的是一个真实且已被当前 Agent 实践确认的问题：Context Engineering 不只处理 Prompt 措辞，而是持续选择、组织、压缩和更新进入模型/Agent 工作集的信息。Anthropic 将其描述为对整个动态 context state 的持续策展；OpenAI 的实践也强调以短入口、结构化知识库和 progressive disclosure 替代巨型说明文件。[Anthropic](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)、[OpenAI](https://openai.com/index/harness-engineering/)

因此本章的研究对象成立。但当前正文有 73 个编号小节、约 2,870 行；优化说明又新增七个 Pattern、案例、成熟度和路线图。如果按“保留全部旧内容再增加 Pattern”执行，章节会更长。正确策略应是用 Pattern 和生命周期模型替换重复原则，而不是叠加。

## 主张裁决

| 主张 | 裁决 | 原因 |
|---|---|---|
| Context Engineering 管理动态信息工作集 | `survives` | 与当前一手实践定义一致 |
| More Context 不必然更好 | `survives` | 长上下文研究和实际 Agent 系统均观察到相关性、位置与污染问题 |
| Context 是 Agent 的局部世界模型 | `narrow` | Context 是可控制的信息输入面；模型先验、工具结果和未观察环境仍会影响行为 |
| Minimum Sufficient Context | `narrow` | 是目标，不是执行前总能准确求出的固定集合；必须配套渐进检索和缺失恢复 |
| Context Pack 是 Execution Contract 的一部分 | `split` | Contract 规定所需/禁止 Context；实际 Pack/Manifest 记录本次提供了什么，二者不能混为一物 |
| 七种 Context Pattern 构成成熟度进阶 | `contradicted` | Static、Layered、Retrieval、Lifecycle、Snapshot、Projection 是可组合的不同维度，不是互斥阶段 |
| Level 5 Adaptive 必然更成熟 | `unsupported` | 动态装配也可能增加不可解释选择、错误路由和注入风险 |
| AI Game Dev OS 当前为 Level 2.5–3 | `unsupported` | 缺少量表、评分规则和跨工程证据收据 |
| Context Ablation 能验证 Context 价值 | `narrow` | 方法有用，但需重复试验、固定模型/版本、匹配任务和不确定性报告 |

“更多 Context 可能降低使用效果”有研究依据，但不能写成适用于所有模型和任务的常数规律。`Lost in the Middle` 说明相关信息的位置和冗余输入会显著影响部分长上下文任务，结论应限定到所测任务与模型。[Liu et al.](https://arxiv.org/abs/2307.03172)

## Pattern 分类应重构

优化说明中的七个 Pattern 实际属于五个正交设计维度：

| 维度 | 可选机制 |
|---|---|
| Source organization | Static instructions、Layered context |
| Retrieval | Index、search、RAG、progressive retrieval |
| Lifecycle | Hot/Warm/Cold、archive、expiry、invalidation |
| Continuity | Snapshot、handoff、checkpoint |
| Projection & governance | Role projection、policy filtering、adaptive assembly |

一个真实系统通常同时采用多项。例如：`Layered + Retrieval + Hot/Warm/Cold + Snapshot + Role Projection`。因此建议将“七级 Pattern 进阶”改成“Context System 设计维度与常见组合”。

## 必须修正的概念

### Context 不是完整世界模型

建议定义为：

> Context 是一次 Agent 推理或执行时可访问的、经过选择的信息表面；它影响 Agent 对项目世界的工作表示，但不等于项目现实，也不等于模型内部完整世界模型。

### Context Contract 与 Context Manifest

```text
Context Contract
→ required / optional / forbidden / freshness rules

Context Manifest
→ actual sources / versions / hashes / omissions supplied this run
```

Contract 是规范性对象，Manifest 是描述性记录。

### Confidence、Authority 与 Validation

删除笼统的 High/Medium/Low Context Confidence。改为分别记录：

- provenance；
- authority；
- validation status；
- freshness；
- scope。

模型自报 confidence 只可作为弱信号。

### Minimum Sufficient Context

建议改成：

```text
Minimum Initial Context
+ Progressive Retrieval
+ Missing-context Escalation
```

因为执行中才可能暴露新依赖，固定 Pack 不应成为阻止下钻的边界。

## Maturity Model 应改成 Capability Profile

线性 Level 0–5 容易暗示“越动态、越自动越成熟”，与跨章治理文档提出的 Architecture Fitness 和 Governance Economics 冲突。建议改成能力矩阵：

```text
Selection
Provenance
Freshness
Retrieval
Lifecycle
Continuity
Projection
Security
Evaluation
```

项目成熟度是这些能力与风险、规模和成本的适配度，不是总分或最高 Level。

## AI Game Dev OS 案例边界

Hotspace → Archive → Index → Snapshot → Memory Summary → Deep Retrieval 是有价值的候选案例结构，但目前应标记为：

- `observable implementation`：需绑定 AI_DEV_OS_Evolve 的具体版本和文件；
- `retrospective inference`：它可被解释为 lifecycle-oriented context model；
- `unsupported`：Level 2.5–3、降低错误率或优于其他结构；
- `current recommendation`：Typed Context、Freshness、Invalidation、Role Projection。

没有 Evidence Receipt 前，不应把路线图写成已经由案例证明的必然演进顺序。

## 结构压缩建议

最终正文建议控制为 12–16 个主体小节，压缩约 45%–55%：

1. Context 的定义与边界；
2. Controlled Information Surface；
3. 类型与质量轴；
4. Initial Selection + Progressive Retrieval；
5. Provenance、Freshness、Conflict；
6. Context Contract 与 Manifest；
7. Lifecycle 与 Invalidation；
8. Compression、Snapshot 与 Continuity；
9. Role Projection 与 Handoff；
10. Security 与外部内容 authority；
11. 设计维度和典型组合；
12. AI Game Dev OS 案例；
13. Evaluation 与成本；
14. 结论。

原则、反模式和检查清单只保留正文没有重复表达的信息。下一章预告不要使用一级章节标题。

## 当前裁决建议

保留第五章，接受从“原则清单”转向“设计维度 + 组合模式 + 案例”的修订目标；拒绝线性 Pattern/Maturity 进阶和未经取证的 Level 2.5–3 判断。Pattern 必须替换旧重复内容，而不是继续增加篇幅。
