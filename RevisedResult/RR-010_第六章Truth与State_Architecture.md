# RR-010：第六章 Truth and State Architecture 审阅

- 记录日期：2026-08-10
- 审阅对象：[第六章正文](../OringinalDocs/第6章.md)
- 记录性质：正式改稿前的结构、概念与外部参照审阅
- Human Disposition：`unreviewed`

## 核心结论

第六章识别的问题成立：文档、代码、运行时、数据、配置、决策和假设可能相互冲突，Agent 不能仅靠语言连贯性自行构造“当前现实”。Domain-scoped authority、State Snapshot、显式 Assumption、Claim/Evidence/Provenance 是本书目前最有工程价值的一组机制。

但当前正式对象模型混用了四类不同维度：信息类别、技术领域、证据状态和生命周期状态。章节一方面说 Decision、Truth、Assumption 必须分离，另一方面又定义 Decision Truth 和 Evidence Truth；一方面说 Evidence 不是 Truth，另一方面把 Evidence Truth 列为 Truth Domain。这是需要在改稿前解决的内部矛盾。

## 主张裁决

| 主张 | 裁决 | 原因 |
|---|---|---|
| Source of Truth 应绑定具体问题和 Domain | `survives` | 避免 Git、文档或 Runtime 被错误提升为全局权威 |
| Code as Implementation Truth | `narrow` | 应指“Repository State 对当前源实现问题具有权威”；生成物、脏改、构建和部署仍需独立状态 |
| Doc as Intent | `narrow` | 设计文档可能表达 Intent，但文档也可能是 Policy、Decision、Observation 或 Runbook |
| Decision Truth 是 Truth Domain | `contradicted` | Decision 是规范性 authority，不是描述性事实 domain |
| Evidence Truth 是 Truth Domain | `contradicted` | 章节后文已正确指出 Evidence 支持 Claim，而不等于 Truth |
| Observed、Verified、Derived、Assumed 是同一状态轴 | `contradicted` | Derived 可以同时被验证；Observed 是证据方式；Assumed 是授权/认识状态 |
| Current State 包含 Active Decisions 和 Open Assumptions | `split` | 它们属于 Execution Baseline，但不是描述性 State 本身 |
| Agent 创建 Claim，Evidence/Authority 将其提升为 Truth | `narrow` | 更准确是更新 claim status 或形成 accepted claim；不应把记录动作写成创造 Truth |
| Truth Registry | `narrow` | 高风险项目可用 Claim Registry/State Index；“Truth Registry”容易把可修订 Claim 实体化为真理 |
| 决策环境可复现比隐藏推理可复现更现实 | `survives` | 与可观察、可审计工程边界一致 |

## 建议采用正交 Claim Model

不要再使用一个 `Type + Domain + Status` 混合所有含义。建议至少拆成：

```text
claim_kind:
  descriptive | normative | intent | assumption

subject_domain:
  repository | runtime | data | configuration | environment | behavior

epistemic_basis:
  observed | measured | test-verified | inferred | reported

lifecycle_status:
  active | stale | superseded | expired

disposition:
  proposed | approved | rejected | conflicted

provenance:
  source | activity | responsible_agent | timestamp | version | scope

evidence_links:
  supporting | counterevidence | limitations
```

这些轴可以组合。例如，一条 Claim 可以同时是：

```text
descriptive
+ runtime
+ inferred
+ active
+ conflicted
```

W3C PROV 已经提供 Entity、Activity、Agent 以及 derivation、revision、primary source 和 responsibility 等来源关系。书中不需要复刻完整标准，但应说明 Claim/Provenance 模型建立在既有 provenance 思想上，而不是全新发明。[W3C PROV-O](https://www.w3.org/TR/prov-o/)

## State、Decision 与 Execution Baseline 要分开

建议改为：

```text
State Snapshot
├── repository state
├── runtime state
├── data/config/environment state
└── observed versions

Execution Baseline Manifest
├── State Snapshot reference
├── active Intent reference
├── active Decision / Policy references
├── open Assumptions
├── Context Manifest reference
└── Evidence baseline
```

这样既保留“任务需要组合当前现实和工作假设”，又不把 Assumption 或 Decision 当作 State。

## “Truth Write Permission”需要重命名

当前表格把 Git、Monitoring、Test、Human 等都称为 Authoritative Writer，容易误导。建议拆成三类权限：

1. `State mutation authority`：谁能改变代码、配置、数据或部署；
2. `Claim assertion authority`：谁能提交某类 Claim；
3. `Claim promotion/disposition authority`：谁能批准、拒绝或解决冲突。

Test 和 Monitoring 产生 observation/evidence；Git/Merge 改变 repository state；Human/Gate 赋予规范性 Decision authority。它们不是以相同方式“写 Truth”。

## 章节命名与术语边界

可以继续保留书面标题 `Truth and State Architecture`，但正文应明确：

> 系统存储和治理的是 Claim、Evidence、State、Decision 与 Assumption；“Truth”是经限定问题、范围、来源和裁决后可被当前任务依赖的状态，而不是一个由 Agent 或 Registry 创造的实体。

建议将：

- Truth Claim → Claim；
- Truth Registry → Claim Registry / State Index；
- Truth Write Permission → Claim and State Authority；
- Evidence Truth → Evidence Record / Observation；
- Decision Truth → Approved Decision / Normative Authority。

## 结构压缩建议

当前正文有 90 个编号小节、约 3,200 行，建议压缩约 50%，组织为：

1. 多来源冲突问题；
2. 代码、运行时、数据和配置的 Domain-scoped Authority；
3. Claim 的正交类型模型；
4. Provenance 与 Evidence；
5. Decision 与 Assumption；
6. State Snapshot；
7. Execution Baseline Manifest；
8. Conflict Resolution 与显式 Unknown；
9. Invalidation、Freshness 与 Dependency；
10. State Transition 与可复现执行环境；
11. 两个 AI Game Dev OS 案例；
12. 适应性治理边界与结论。

成熟度模型、Truth Debt、State Debt、Registry、多个 Pattern 和 Readiness Gate 不应全部成为主体。可把 Registry/Graph 作为高风险实现选项，把 Governance Profile 移到第 13 章。

## 需要补证据的主张

- SP122 是否真的出现过 stale/conflicted authority 影响运行表现；
- State Snapshot 是否减少了跨 Thread 恢复成本；
- Dirty Worktree 是否造成过可观察的错误归因；
- Save Migration 案例是否来自实际任务还是说明性假设；
- Claim/Evidence Graph 是否已经在 AI Game Dev OS 中运行，还是当前建议。

示例中的 commit、版本和截图必须标注为真实引用或 fictional example，不能保持介于两者之间的状态。

## 当前裁决建议

保留本章核心论证，但在任何正文润色前先重建正式对象模型。第六章不是增加更多 Truth 类型，而是防止不同性质的信息被语言一致性错误合并。完成类型拆分后，它可以成为 Intent、Context、Execution、Evidence 和 Governance 之间的关键枢纽。
