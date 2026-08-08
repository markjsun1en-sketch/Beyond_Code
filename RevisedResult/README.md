# RevisedResult：审阅结论档案

本目录保存对《Beyond Code: AI-Native Software Engineering》写作计划、理论补充、章节草稿和写作基础设施的审阅结论，作为后续修改 `OptimizedDocs/` 时的依据。

## 记录边界

- `OringinalDocs/` 保存作者原始材料，本目录不替代、覆盖或反向修改原稿。
- `RevisedResult/` 保存“如何判断、为什么修改、哪些地方仍待验证”。
- `Evidence/` 保存 Claim Ledger、Evidence Receipt、反向证据和人工裁决。
- `OptimizedDocs/` 保存根据审阅结论和证据形成的工作稿。
- 本目录中的首批文件是对既有对话审阅结论的结构化重建，不是对话逐字稿。
- 未经作者裁决的建议默认状态为 `unreviewed`，不能视为已经接受的改稿指令。

## 首批审阅记录

| ID | 主题 | 结论状态 | 文件 |
|---|---|---|---|
| RR-001 | 全书定位与写作意义 | 保留，范围已收窄 | [RR-001](RR-001_全书定位与写作意义.md) |
| RR-002 | AI Game Dev OS 作为案例与证据 | 可用，但不能单独证明普遍理论 | [RR-002](RR-002_AI_Game_Dev_OS案例适用性.md) |
| RR-003 | Human Smoothing / Tight Boundaries 变更说明 | 有意义，不宜整篇直接并入正文 | [RR-003](RR-003_Human_Smoothing与Tight_Boundaries.md) |
| RR-004 | 第三章 Harness 补充 | 应吸收核心边界，不宜原样插入 | [RR-004](RR-004_第三章Harness补充.md) |
| RR-005 | 第四章 Intent Engineering | 理论位置成立，需要收窄宣称和压缩结构 | [RR-005](RR-005_第四章Intent_Engineering.md) |
| RR-006 | 写作 Agent / Skill 基础设施 | 有用但非必要，维持最小体系 | [RR-006](RR-006_写作Agent与Skill体系.md) |
| RR-007 | 第二章核心主张的证据审阅 | 部分支持，普遍性表述需要收窄 | [RR-007](RR-007_第二章核心主张证据审阅.md) |

## 后续使用方式

1. 修改章节前，先读取对应审阅记录及其引用的原稿。
2. 将拟修改的核心判断区分为事实、同期判断、事后推导和当前建议。
3. 若判断依赖外部工程事实，先在 `Evidence/` 建立或更新 Claim 与 Receipt。
4. 仅将通过主笔裁决的结论写入 `OptimizedDocs/`。
5. 作者审阅后，在记录末尾填写 Human Disposition：`accepted / narrowed / rejected / deferred`。
6. 新事实推翻旧结论时，新增一条“结论变化记录”，说明改变结论的具体事实或定义，不静默覆盖历史判断。

## 命名建议

```text
RR-NNN_主题.md
```

审阅记录编号只表示登记顺序，不表示优先级或证据强度。

## 相关产物

- 形式化证据保存在 [Evidence](../Evidence/)；本目录只记录审阅结论及其修改含义。
- 已形成的正文候选保存在 [OptimizedDocs](../OptimizedDocs/)；不在本目录复制正文，以免产生两个待维护版本。
