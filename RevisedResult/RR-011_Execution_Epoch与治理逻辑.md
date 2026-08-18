# RR-011：Execution Epoch 与跨章节治理逻辑审阅

- 记录日期：2026-08-10
- 审阅对象：[跨章节治理逻辑修订说明](../OringinalDocs/beyond_code_cross_chapter_governance_epoch_change_spec_zh.md)
- 记录性质：跨章理论修订审阅
- Human Disposition：`unreviewed`

## 核心结论

这份文档解决了此前理论的一项真实缺口：治理机制本身消耗 Token、时间、等待、Review 和人类注意力，因此不能把“更多 Gate、更多 Registry、更多 Review”写成更高成熟度。风险分级、治理下限、运行中升级和执行基线应进入全书。

但风险相称和持续治理并不是新原则。NIST AI RMF 已明确要求依据组织风险容忍度选择风险管理活动，并在生命周期中持续、迭代地 Map、Measure、Manage，而不是执行统一清单。[NIST AI RMF Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/)

本书真正可能新增的部分，是把这些原则落实到 Agent 执行：谁能降低 Guardrail、运行过程中如何 Pin Baseline、发现新风险时如何 Pause/Rebase/Escalate，以及如何记录这一状态迁移。

## 主张裁决

| 主张 | 裁决 | 原因 |
|---|---|---|
| Governance 本身是生产成本 | `survives` | 修正“治理越多越成熟”的隐含方向 |
| 治理强度应与预期损失相称 | `survives` | 与既有风险管理原则一致，应作为基础而非新学科宣称 |
| Execution Epoch 固定关键执行引用 | `narrow` | 有用，但应定义为 Execution Contract 的运行区间，避免新增一个重复容器 |
| Working Truth Baseline 是被授权依赖的事实集合 | `split` | 当前定义混入 Decision、Constraint 和 Assumption；应改成 Typed Execution Baseline Manifest |
| 同一 Epoch 内治理只能单调上升 | `narrow` | 执行 Agent 不能自降权限或治理下限；授权角色可以在同一 Epoch 内依据新证据调整非关键检查 |
| G0–G4 可以通用映射任务类型 | `narrow` | 等级可作示例，具体下限必须由项目 Policy、资产和影响定义 |
| 最小化 Expected Total Production Cost | `narrow` | 是决策目标，不是可直接精确求解的单一公式；概率、尾部风险和不可量化损失需保留 |
| 新概念应 P0 扩散至多个未写章节 | `unsupported` | 尚无真实 Execution Epoch 对照案例，跨章扩散过早 |
| Sprint 是 Execution Epoch 的一种实现 | `survives` | 作为工作定义合理，但不是唯一粒度 |

## Execution Epoch 的推荐定义

建议把它定义成区间，而不是另一份大型对象：

> Execution Epoch 是从某个 Execution Contract 被打开，到其被关闭、重启或显式 Rebase 之间的受控执行区间。区间内由固定引用的 Intent、Execution Baseline、Policy Floor 和 Context Manifest 约束工作；外部变化不会静默替换这些引用。

建议结构：

```text
Execution Contract
├── Intent reference
├── Execution Baseline Manifest
├── Context Contract + Manifest
├── Governance Floor
├── Initial / Current Profile
├── Authority and permissions
└── Evidence requirements

Execution Epoch
├── opened_at
├── contract_version
├── observed risk signals
├── escalation / rebase decisions
└── closed_at + output state
```

这样 Epoch 是 Contract 的生命周期实例，而不是再次复制所有内容。

## Working Truth Baseline 应重命名

建议改成 `Execution Baseline Manifest`：

```text
State claims / snapshot
Active decisions and policy
Pinned intent
Open assumptions
Known conflicts
Known dirty changes
Source versions
```

其中只有第一项是描述性状态；Decision、Policy、Intent 和 Assumption 保持各自类型。这与 RR-010 的对象模型一致。

## Monotonic 的对象应是 Guardrail，不是全部治理活动

推荐原则：

> 执行 Agent 可以主动增加检查、暂停、升级或请求更高权限，但不能自行降低 Policy Floor、扩大自身 Authority、忽略已触发的强制 Gate，或把未解决风险重新分类为低风险。

不必规定所有 Review 和 Context 只能增加。独立 Policy Engine、授权人或外部 Reviewer 可以在同一 Epoch 中根据新证据减少非必要检查。真正单调的是：

- 执行 Agent 的自我授权不能扩大；
- Policy Floor 不能被执行 Agent 降低；
- 已记录的风险和冲突不能被静默删除。

## Governance Economics 的边界

建议使用多目标决策而不是伪精确公式：

```text
minimize:
  execution + context + review + waiting + cognitive + expected rework cost

subject to:
  policy floor
  legal/security constraints
  unacceptable-loss limits
  human decision rights
```

对于安全、隐私和不可逆数据损失，不能只用期望值抵消低概率高影响风险。

## 采用顺序

不建议立即按 P0 修改九个章节。先做一个最小闭环：

1. 在第六章引入 `Execution Baseline Manifest`；
2. 在第七章把 Epoch 作为 Execution Contract 的生命周期；
3. 在第十三章定义 Governance Floor、Authority 与 Risk Trigger；
4. 用三个任务试验：低风险 typo、可逆 UI 修改、Save Migration；
5. 比较治理成本、误升级、漏升级、返工和人类等待；
6. 通过证据后，再反馈第 20–23 章。

## 当前裁决建议

接受 Governance Economics、Policy Floor、运行中风险触发和“执行者不能自我降级 Guardrail”的核心方向。Execution Epoch 有条件保留为运行区间；Working Truth Baseline 重命名并类型化；Monotonic 只约束 Authority/Guardrail，不约束所有治理活动；跨章 P0 扩散暂缓到真实案例验证之后。
