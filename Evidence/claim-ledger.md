# Beyond Code Claim Ledger

本表只登记会影响章节论证、全书结构或 AI Game Dev OS 反馈的重要主张。
普通叙事与措辞不要求逐句登记。

| Claim ID | 主张摘要 | 位置 | 类型 | Evidence | 覆盖状态 | 人工状态 | 当前处置 |
|---|---|---|---|---|---|---|---|
| `CLM-C02-001` | Agent 承担执行路径后，部分隐性组织知识需要被显式化为边界、权威和证据机制 | 第2章 2.2 | inference | `ER-20260807-001` | partial | unreviewed | narrow |
| `CLM-OUTLINE-001` | 新增 Human Smoothing 等概念后不需要重构现有 23 章结构 | 变更说明结论 | recommendation | `ER-20260807-002` | unsupported | unreviewed | hold |
| `CLM-C06-001` | Source of Truth 必须绑定具体问题、Domain、版本和状态，冲突不能被单一全局权威静默覆盖 | 第6章 | inference | `ER-20260810-001` | partial | unreviewed | narrow |
| `CLM-C06-002` | Intent、Decision/Policy、描述性 State Claim、Assumption 与 Evidence 应保持正交区分，Agent 断言本身不产生项目权威 | 第6章 | recommendation | `ER-20260810-002` | partial | unreviewed | keep |
| `CLM-C06-003` | 长任务或多 Agent 工作应优先保存版本绑定的外部决策环境，而不是试图复现隐藏推理 | 第6/18章 | inference | `ER-20260810-003` | partial | unreviewed | narrow |
| `CLM-OUTLINE-002` | v4.94 记录了 meta-only 治理活锁及随后分阶段、仍为 NON_QUALIFYING 的 function-first 开发闭环 | 跨章治理；第7/13/20/23章 | fact | `ER-20260818-001` | verified | accepted | keep |
| `CLM-C06-004` | 观察目标前、阻断执行或改变 authority-bearing surface 的验证器失败应与目标结果分开，并记录 target non-result | 第6/9章 | recommendation | `ER-20260818-002` | partial | accepted | narrow |
| `CLM-C09-001` | 未获 Acceptance Authority 委托或范围仍待裁决时，Test PASS 不证明范围必要，也不自动完成 Acceptance、Adoption 或 Release | 第4/6/9章 | recommendation | `ER-20260818-003` | partial | accepted | narrow |
| `CLM-C09-002` | Claimed、Observed、Verified 与 Accepted Completion 不应建模为同质单轴等级；Accepted 是绑定目标与 Authority 的处置 | 第9章 9.2、9.5 | recommendation | `ER-20260818-004`；补充 `ER-20261030-003` | partial | unreviewed | narrow |
| `CLM-C09-003` | Evidence Stack 不应被解释为跨 Claim 类型的通用强弱排序；Evidence 类型应匹配 Claim、Scope 与用途 | 第9章 9.3 | recommendation | `ER-20260818-005` | partial | unreviewed | narrow |
| `CLM-C11-001` | 当需人工判断的保留 AI 变更持续超过合格审阅容量时，逐项人工审阅不能单独维持控制；响应方式仍需在限流、扩容和风险委托之间裁决 | 第11章 | inference | `ER-20260824-001` | partial | accepted | split |
| `CLM-C12-001` | Human Control Plane 只应作为现有 Control and Evidence Plane 面向人的有边界投影，并暴露观测覆盖、Detector Health、下钻和接管路径 | 第12–14章 | recommendation | `ER-20260824-002` | partial | accepted | narrow |
| `CLM-C16-001` | 重要且可版本化、可恢复的 Workflow 变更应作为有范围的候选假设评估；产生、合并或 Test PASS 本身不等于 Improvement | 第16章 | recommendation | `ER-20260824-003` | partial | accepted | narrow |
| `CLM-C17-001` | Agent 数量本身不足以证明已经形成组织或获得组织效能；本书把 Work、Role、Assignment、Authority、Responsibility、Handoff、Conflict 与 Integration 作为候选检查面，不声称它们完备、最小、跨项目必要或产生组织效能 | 第17章 | recommendation | 无直接 Receipt；`CLM-C09-001`、`CLM-C12-001`、`CLM-C16-001` 仅提供相邻案例边界 | unsupported | accepted | narrow |
| `CLM-C18-001` | Trace 记录可以支持行动归因、有限重建和责任审查，但不能自行分配或解除 Accountability；项目应把责任绑定到具名 Decision Target、Authority 与 Human／组织角色，并将 Agent 视为可被行动归因的执行主体 | 第18章 | recommendation | `ER-20260810-003`、`ER-20260810-002`、`ER-20260818-003` 仅组合覆盖部分边界 | partial | unreviewed | narrow |
| `CLM-C19-001` | 读取不可信内容且能产生副作用的 Agent 不能只依赖 Prompt 或模型自律；Data / Instruction、Context、Function、Permission、Credential 与 Action Sink 需要模型外边界，部署位置本身不证明安全 | 第19章 | recommendation | `ER-20260824-004` | partial | unreviewed | narrow |
| `CLM-C19-002` | AI-native 供应链应覆盖所有能改变 Context、Decision、Tool、Build、Runtime 或 Output 的行为组件；Provenance 说明来源与产生过程，不自动证明行为安全或适用 | 第19章 | recommendation | `ER-20260824-005` | partial | unreviewed | narrow |
| `CLM-C19-003` | `AI-generated` 不能单独决定 IP 处置；输入权限、服务条款、第三方 License、Human Contribution、Output Provenance、下游用途与适用法域需要分开记录 | 第19章 | recommendation | `ER-20260824-006` | partial | unreviewed | narrow |
| `CLM-C23-001` | SP122 的 Human 决定分别接受当前 D2 Battle 视觉／可读性基线与 post-repair v4.93 qualifying evidence chain，同时保留 follow-up、Supported Adoption 与 Production 边界 | 第23章 | fact | `ER-20260827-001` | verified | accepted | keep |
| `CLM-C14-001` | lessismore CardInformation 的保存记录表明旧覆盖检查影响说明展示；具名修复分开展示资格与 QA 适用性，有限验证保留 stale／pending 下的说明生成及真实坏输入的拒绝路径 | 第14章 14.9、14.20–21 | fact | `ER-20261030-001` | verified | unreviewed | keep |
| `CLM-C15-001` | DevOS OBS16–18 的有限保存试验显示 AND 问句漏检、标识符候选的局部召回与条件丢失；原文回读支持核对但不自动补召回或判断适用性 | 第15章 15.16–17、15.25 | fact | `ER-20261030-002` | verified | unreviewed | keep |
| `CLM-C21-001` | lessismore与DevOS具名规则调整了原入口、交接、按影响验证及复用／停止条件，并保留硬边界；同次矩阵残缺与无收益证据限制继续可见 | 第21章 21.28–30；第23章23.44.7 | fact | `ER-20261030-004` | verified | unreviewed | keep |
| `CLM-C16-002` | 具名奖励页对照记录单题改善，另三题未观察到预定质量优势；不构成纯AI IDE对照或整体收益证明 | 第16章 16.10–15、16.24 | fact | `ER-20261122-001` | verified | unreviewed | keep |
| `CLM-C18-002` | 具名材料分别记录部分回收、归档导航恢复及旧S5缺口后的新执行，保留父hold与各自恢复范围，后继盘点仍待审阅 | 第18章 18.21–24 | fact | `ER-20261122-002` | verified | unreviewed | keep |
| `CLM-C20-001` | RandomHeroes取样少于预设且弃用失真计时探针；lessismore短流程累计与最大值分向变化，均不直接证明Agent工作流收益 | 第20章 20.6–11、20.25 | fact | `ER-20261122-003` | verified | unreviewed | keep |
| `CLM-C12-002` | GDD复核记录报告并处置遗漏，Buff静态分支可核对；白板隔离故障以独立回读核实状态，各自保留历史、运行与根因限制 | 第12章 12.13–14；第5章5.7、第14章14.16 | fact | `ER-20261122-004` | verified | unreviewed | keep |
| `CLM-C22-001` | 本地有限Beta分发切片、RandomHeroes本机APPLIED接入与完整正式资格具有不同范围，未证明通用迁移或灾备成功 | 第22章 22.15–16、22.37 | fact | `ER-20261122-005` | verified | unreviewed | keep |
| `CLM-C23-002` | 两个独立专业生产任务分别保留方案校准、隔离交付与采用边界；FU05人工两路线接受记录与同字节槽位限制并存 | 第23章 23.44.2–3；第4章4.3回接 | fact | `ER-20261122-006` | verified | unreviewed | keep |
| `CLM-C23-003` | SP139保存方向比较、样段、正式绑定和指定检查过程，有限人工选择不扩为全图审美或Sprint完成 | 第23章 23.44.4 | fact | `ER-20261122-007` | verified | unreviewed | keep |

## 状态约定

- 覆盖状态：`verified / partial / counterevidence / unsupported`。
- 人工状态：`unreviewed / accepted / rejected`。
- 当前处置：`keep / narrow / split / withdraw / hold`。

永久 ID 由主笔分配。删除主张时保留原行，并将处置改为 `withdraw`，不得复用 ID。
