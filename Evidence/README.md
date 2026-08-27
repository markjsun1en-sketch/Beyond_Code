# Evidence

本目录保存《Beyond Code》的 Claim Ledger、Evidence Receipt、反向证据与人工裁决。

## 工作面

- `claim-ledger.md`：全书重要主张及其当前证据状态。
- `receipts/`：一条 Claim 对应一份或多份可追溯 Evidence Receipt。
- `.agents/skills/evidence-receipt/`：收据生成流程、证据判断规则和模板。

Evidence Receipt 是重要 Claim 的审计工具，不是理论进入正文的许可证。

## 何时使用正式 Receipt

至少满足一项时使用：

- 依赖精确 Git 历史、Runtime、Artifact 或同期 Decision；
- 从单项目案例推广到跨项目、组织或行业；
- 陈述具体 Security、Privacy、Legal、IP 或其他高风险事实；
- 结论将直接改变 AI Game Dev OS；
- 声称提高质量、速度、成本、可靠性或安全性；
- 来源发生实质冲突，或作者明确要求正式取证。

## 何时不使用

下列内容默认不建立 Receipt：

- 术语定义与候选对象模型；
- 章节结构和解释性类比；
- 普通叙事修改；
- 作者经验、审美与方向判断；
- 已明确写成 Proposal 的建议。

这些内容通过定义一致性、解释力、最强反例、替代模型、适用边界和
Human Review 审查。没有效果实验会限制效果 Claim，但不会自动使候选
理论失去讨论资格。

## 命名

- Claim：`CLM-CNN-NNN`，例如第二章第一条主张为 `CLM-C02-001`。
- 全书结构主张：`CLM-OUTLINE-NNN`。
- Receipt：`ER-YYYYMMDD-NNN`。
- 文件：`<receipt_id>__<claim_id>.md`。

## 引用规则

1. 区分可观察事实、当时判断、事后推导和当前建议。
2. 仓库来源必须记录 path、branch、commit 和当前 worktree 状态。
3. Manifest 内声明的 immutable revision 与保存 Manifest 的 commit 分开记录。
4. Codex task 只引用可见消息、工具活动、输出和文件变化，不推断隐藏思维过程。
5. 大型证据保留在原工程，通过绝对路径和 revision 引用，不在本仓库复制。
6. 单项目案例默认不能证明全行业命题，除非主张本身已明确限定范围。

## 人工裁决

AI 只能给出 `verified / partial / counterevidence / unsupported` 的证据覆盖判断。
最终的 `accepted / rejected` 由作者决定，并同时回写 Receipt 与 Claim Ledger。

`partial` 不等于观点不可写；它只表示 Evidence 没有覆盖精确 Claim 的全部范围。
Human Acceptance 也不会把 `partial` 自动升级为 `verified`。

Claim ID、Receipt ID、Coverage、Human Status 和历史处置保留在本目录、
`RevisedResult/` 或编辑索引中。Reader-facing Chapter 使用自然语言说明来源、
推导、Proposal、Scope 与限制，不重复显示内部工作流状态。
