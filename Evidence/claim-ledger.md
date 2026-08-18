# Beyond Code Claim Ledger

本表只登记会影响章节论证、全书结构或 AI Game Dev OS 反馈的重要主张。
普通叙事与措辞不要求逐句登记。

| Claim ID | 主张摘要 | 位置 | 类型 | Evidence | 覆盖状态 | 人工状态 | 当前处置 |
|---|---|---|---|---|---|---|---|
| `CLM-C02-001` | Agent 承担执行路径后，部分隐性组织知识需要被显式化为边界、权威和证据机制 | 第2章 2.2 | inference | `ER-20260807-001` | partial | unreviewed | narrow |
| `CLM-OUTLINE-001` | 新增 Human Smoothing 等概念后不需要重构现有 23 章结构 | 变更说明结论 | recommendation | `ER-20260807-002` | unsupported | unreviewed | hold |
| `CLM-C06-001` | Source of Truth 必须绑定具体问题、Domain、版本和状态，冲突不能被单一全局权威静默覆盖 | 第6章 | inference | `ER-20260810-001` | partial | unreviewed | narrow |
| `CLM-C06-002` | Intent、Decision/Policy、描述性 State Claim、Assumption 与 Evidence 应保持正交区分，Agent 断言本身不产生项目权威 | 第6章 | recommendation | `ER-20260810-002` | partial | unreviewed | keep |
| `CLM-C06-003` | 长任务或多 Agent 工作应优先保存版本绑定的外部决策环境，而不是试图复现隐藏推理 | 第6章 | inference | `ER-20260810-003` | partial | unreviewed | narrow |
| `CLM-OUTLINE-002` | v4.94 记录了 meta-only 治理活锁及随后分阶段、仍为 NON_QUALIFYING 的 function-first 开发闭环 | 跨章治理；第7/13/20/23章 | fact | `ER-20260818-001` | verified | accepted | keep |
| `CLM-C06-004` | 观察目标前、阻断执行或改变 authority-bearing surface 的验证器失败应与目标结果分开，并记录 target non-result | 第6/9章 | recommendation | `ER-20260818-002` | partial | accepted | narrow |
| `CLM-C09-001` | 未获 Acceptance Authority 委托或范围仍待裁决时，Test PASS 不证明范围必要，也不自动完成 Acceptance、Adoption 或 Release | 第4/6/9章 | recommendation | `ER-20260818-003` | partial | accepted | narrow |
| `CLM-C09-002` | Claimed、Observed、Verified 与 Accepted Completion 不应建模为同质单轴等级；Accepted 是绑定目标与 Authority 的处置 | 第9章 9.1 | recommendation | `ER-20260818-004` | partial | unreviewed | narrow |
| `CLM-C09-003` | Evidence Stack 不应被解释为跨 Claim 类型的通用强弱排序；Evidence 类型应匹配 Claim、Scope 与用途 | 第9章 9.3 | recommendation | `ER-20260818-005` | partial | unreviewed | narrow |

## 状态约定

- 覆盖状态：`verified / partial / counterevidence / unsupported`。
- 人工状态：`unreviewed / accepted / rejected`。
- 当前处置：`keep / narrow / split / withdraw / hold`。

永久 ID 由主笔分配。删除主张时保留原行，并将处置改为 `withdraw`，不得复用 ID。
