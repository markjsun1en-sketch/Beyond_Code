# RR-004：第三章 Agent Harness 补充审阅

- 记录日期：2026-08-08
- 审阅对象：[第三章补充：Agent Harness Engineering 与 AI-Native Software Engineering](../OringinalDocs/beyond_code_chapter3_supplement_agent_harness_vs_ai_native_se_zh.md)、[第三章正文](../OringinalDocs/第3章.md)
- 记录性质：既有对话审阅结论的结构化重建
- Human Disposition：`unreviewed`

## 核心结论

第三章需要回答“这是否只是 Harness Engineering”的质疑，但补充文档不宜原样插入正文。应吸收它对研究对象和责任范围的区分，同时避免把仍在扩张的行业术语写成严格、稳定的集合关系。

最可保留的区分是：

```text
Harness Engineering
关注 Agent 如何获得上下文、工具、状态、执行循环和反馈能力。

AI-Native Software Engineering
关注使用这些智能执行能力的软件生产体系如何长期可靠、可验证、可理解、可治理地运行。
```

## 已知事实

- 当前 Harness 实践已经覆盖 Context、Tool、State、Sandbox、Review、Memory 和多 Agent 等能力。
- Harness 的边界正在向工程流程、知识组织、验证和自治扩张，不只等于一个狭义 Runtime。
- AI-Native Software Engineering 在本书中还讨论产品系统、人类组织、责任、认知负担、演化和领域生产模型。

OpenAI 的 agent-first 工程实践也把仓库知识、应用可读性、验证工具、隔离环境和反馈循环纳入 Harness 工作范围，说明该边界具有动态性，而不是固定层级：[Harness engineering: leveraging Codex in an agent-first world](https://openai.com/index/harness-engineering/)。

## 需要收窄的判断

1. 不应把 `Harness Engineering ⊂ AI-Native Software Engineering` 写成行业公认的严格集合关系。
2. “Harness 只负责运行、AI-Native 负责工程”过于整齐，现实 Harness 已经承担部分工程治理。
3. “AI-Native 的研究对象始终更大”只能作为本书定义下的范围声明，而不是普遍事实。
4. AI Game Dev OS 是 Domain Operating Model 的一个实现案例，不能据此证明三层模型是唯一分层方式。

## 推荐定义

> 在本书中，Harness Engineering 指围绕智能执行环境的可用性与可靠性形成的工程实践；AI-Native Software Engineering 指包含 Product System、Production Intelligence System、人类组织及其全生命周期治理的更宽分析框架。二者大量重叠，区别主要来自分析对象，而不是工具清单。

这个定义保留本书边界，同时承认行业术语仍在演化。

## 结构问题

- 第三章正文已经很长，补充文档本身也超过一千行。
- Harness 的定义、三层位置、区别表、一句话区分和最终结论多次重复。
- “从 Harness 到 Domain Operating Model”适合在案例或后续组织章节展开，不需要全部堆入第三章。

## 修改策略

正文只保留四部分：

1. 为什么必须回应 Harness 质疑；
2. Harness 当前实际覆盖什么；
3. 本书为何仍需要更宽的生产系统与组织视角；
4. 三者关系：Runtime/Harness、通用工程方法、Domain Operating Model。

其余产品能力、工具表和扩张趋势移入附录，避免正文随产品演化快速过期。

## 所需证据

- 当前 Harness 工程的权威定义或一手实践；
- 一个 Harness 能运行但项目治理仍失败的案例；
- 一个 Harness 自身已经覆盖治理问题的反向案例；
- AI Game Dev OS 中 Runtime 能力与领域制度明确分离的工程产物。

## 当前裁决建议

保留补充文档作为素材库；第三章只吸收压缩后的边界论证。核心措辞使用“本书采用的分析范围”和“大量重叠”，不声称严格的学科从属关系。

