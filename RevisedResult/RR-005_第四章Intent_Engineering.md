# RR-005：第四章 Intent Engineering 审阅

- 记录日期：2026-08-08
- 审阅对象：[第四章：Intent Engineering](../OringinalDocs/第4章.md)、[全书大纲中的第四章](../OringinalDocs/beyond_code_ai_native_software_engineering_outline_zh.md)
- 记录性质：既有对话审阅结论的结构化重建
- Human Disposition：`unreviewed`

## 核心结论

第四章的理论位置成立，但当前更像完整方法手册，而不是结构收敛后的正式章节。它真正的增量不是重新发明 Goal、Constraint、Assumption 或 Acceptance Criteria，而是把利益相关者目标运行化为可被 Agent 消费、分解、继承、验证和升级的工程接口。

推荐工作定义：

> Intent Engineering 是把利益相关者目标转化为版本化、可追踪、受风险边界约束并与证据相连的 Intent，使自主执行者能够执行和派生局部目标，同时不能静默改变 Parent Intent。

## 与既有需求工程的关系

Goal-Oriented Requirements Engineering 和 KAOS 已经研究 goals、constraints、assumptions、agents、goal operationalization、conflict resolution、assumption retraction 和 agent assignment。因此“Requirement 不等于 Intent”过于绝对。参考：[Goal-Driven Requirements Engineering: the KAOS Approach](https://webperso.info.ucl.ac.be/~avl/gore.php)。

更准确的表述是：

> 需求产物并不自动等于 Agent 可直接执行的 Intent。

本章应将 Intent Engineering 定位为面向自主执行者的需求运行化层，而不是对 Requirements Engineering 的替代。

## 本章真正有辨识度的增量

```text
Requirement / Goal
        ↓
Execution-ready Intent
        ↓
Context + Contract + Authority
        ↓
Agent Execution
        ↓
Evidence + Human Decision
```

具体包括：

- Intent 在 Controller、Worker、Reviewer 间的继承和稀释；
- Parent Intent 与局部派生目标的授权关系；
- Intent 与权限、Evidence、Escalation 的执行前绑定；
- Context compression、handoff 和局部优化导致的 Intent Drift；
- 同一 Intent 被不同模型或 Runtime 消费时的适配层。

## 必须修改的问题

### 1. AI 所有权表述过强

AI 可以在授权范围内生成和管理局部目标。应将“AI 不能拥有 Intent”改为：Agent 不能未经授权地重定义最终价值目标或 Parent Intent。

### 2. Worker 规则过于绝对

Worker 可以提出修改、细化局部目标或在 Contract 内作选择；禁止的是静默改写 Parent Intent。

### 3. 缺少多方目标冲突

需要增加产品、技术、安全、体验、成本等 Intent 冲突及其优先级、审批者、受影响方和升级规则。

### 4. 缺少来源与完整性安全

Intent Object 至少需要：

```text
source
authority
approved_by
status
valid_scope
supersedes
effective_version
```

否则过期文档或外部注入可能被误识别为正式 Intent。

### 5. Intent 与 Truth 分离不彻底

Intent Object 应引用带版本和采集时间的 Truth Snapshot，而不是把事实内容直接嵌入 Intent。

### 6. 主观 Acceptance 尚未运行化

“快速定位”“不显拥挤”等标准需要注明验证场景、目标分辨率、评审者、证据类型和分歧裁决方式。

### 7. 缺少有效性验证

“结构化 Intent 会降低误解、漂移或 Agent Coupling”目前主要是合理推导，需要真实任务的前后对比或反例。

## 结构压缩建议

原大纲有七个主体部分，当前正文扩展为 44 节、约 2,500 行。建议压缩 35%–45%，收敛为：

1. 与 Requirements Engineering 的关系；
2. Execution-ready Intent 的定义；
3. Intent Object；
4. 分解、继承与局部授权；
5. Drift、Version 和 Lifecycle；
6. Acceptance、Evidence 与 Human Decision；
7. 冲突、权限与风险分级；
8. AI Game Dev OS 完整案例。

Intent Registry 和多档 Profile 有用但不是所有任务的必要设施，可缩成一节或放入附录。Human Smoothing、Low Agent Coupling、章末原则、反模式和检查清单存在重复，应保留最能推进本章论证的版本。

章末提前使用一级标题 `Context Engineering` 会在 Markdown 结构上像是第五章已经开始，应改成普通过渡文本。

## 对 AI Game Dev OS 的反向建议

先用 SP122 一类真实任务验证三个问题：

- SP/MP 是否明确记录 Parent Intent；
- Worker Contract 是否区分 delegated authority 与 escalation boundary；
- Acceptance 是否在执行前绑定 Required Evidence。

暂不直接建设完整 Intent Registry。先比较原始请求、执行过程、返工和最终结果，确认结构化 Intent 是否降低了特定失败成本。

## 当前裁决建议

保留本章及 Intent Engineering 术语，但明确这是本书为 Agent-facing requirements operationalization 使用的工作概念；收窄学科宣称，补足冲突、授权、来源和安全模型，并完成结构压缩。

