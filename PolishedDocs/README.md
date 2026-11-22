# PolishedDocs

本目录保存《Beyond Code: AI-Native Software Engineering》的 Reader-facing 成书候选稿。

它与其他目录的边界如下：

- `OringinalDocs/` 保存不可静默改写的作者原始材料与早期声音；
- `OptimizedDocs/` 保存对象模型、逻辑、Claim 范围和 Evidence 边界已经校准的工作稿；
- `PolishedDocs/` 只负责面向读者的叙事、节奏、章节结构和表达；
- `RevisedResult/` 与 `Evidence/` 继续保存计划、审阅、裁决和正式证据，不进入 Reader-facing 正文。

`PolishedDocs/` 不是比 `OptimizedDocs/` 更高的事实源。若成书改写暴露出定义冲突、新事实、新 Claim 或案例边界变化，应先回到相应工作稿与审阅流程处理，再同步到这里。

当前目录以第1、6章作为最初的双声音基线。第1章已在 2026-09-02 因新的价值表达判断重新打开，并按 W0 同步两处逻辑接口，当前仍等待 Human 复核：

| 章节 | 候选稿 | 当前状态 |
|---|---|---|
| 第1章 | [软件工程角色演进](第1章_软件工程角色演进_成书候选稿.md) | 已分开局部用途与项目净收益，并按条件描述瓶颈迁移、分开 Responsibility／Accountability；`VOICE_REOPENED` |
| 第6章 | [Truth and State Architecture](第6章_Truth与State_Architecture_成书候选稿.md) | 文笔暂时接受；真实项目问题驱动的高密度技术章基线 |
| 第23章 | [纵向实践：AI Game Dev OS 与 lessismore](第23章_AI_Game_Dev_OS纵向案例_成书候选稿.md) | Human 判断当前无大问题；`VOICE_DEFERRED_FOR_CROSS_BOOK_REVIEW`，不是出版冻结 |

这些章节采用不同结构，不构成全书模板，也不因后续方向调整而补入对称案例。后续章节可以分别由作者纵向经历、技术模型、显式设计假设、外部比较或纵向案例承担主叙事；新增事实、跨项目推论或案例边界变化仍须先经过 `OptimizedDocs/`、`Evidence/` 或 `RevisedResult/` 路由。调整后的实施计划与保真记录见 [RR-039：PolishedDocs 人类化成书实施计划](../RevisedResult/RR-039_PolishedDocs人类化成书实施计划.md)。

Human 已接受 Phase 2 创建的 [`reader-facing-polish` v0.1](../.agents/skills/reader-facing-polish/SKILL.md)、[RR-040：公开案例组合与章节映射](../RevisedResult/RR-040_公开案例组合与章节映射.md) 和隔离测试结论。案例映射只作为编辑候选地图，不能直接成为 `PolishedDocs/` 的事实来源，也不表示其中案例已逐项获准进入正文。

第23章已按单独授权完成 Phase 3 派生与独立 Fidelity 复核，实施记录见 [RR-042](../RevisedResult/RR-042_第23章reader-facing-polish_Phase3_Pilot实施记录.md)。W0 后续接受第12、17章的窄逻辑入口，但没有启动两章的 Reader-facing Pilot；第1章只同步已经先进入逻辑母版的接口修正，没有加入外部案例或效果数字。第1、23章都没有因此升级为出版定稿。完整状态矩阵见 [RR-043](../RevisedResult/RR-043_全书成书修订W0决策与基线.md)。

后续章节建议使用：

```text
第N章_主题_成书候选稿.md
```

## W0 与图文分支合并后的使用边界

2026-11-22 合并保留本目录三份候选及其原有 Human Voice 状态。对应 `OptimizedDocs/` 后来新增了机制图、案例和术语修正，本目录仍保留具名历史派生结果，不能据此认定与当前母版完全一致。下次派生前须重新比对来源；当前 Showcase 继续发布完整23章工作稿，未自动采用这些候选。见 [RR-044](../RevisedResult/RR-044_W0与图文Showcase分支合并记录.md)。
