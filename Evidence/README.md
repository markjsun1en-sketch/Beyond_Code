# Evidence

本目录保存《Beyond Code》的 Claim Ledger、Evidence Receipt、反向证据与人工裁决。

## 工作面

- `claim-ledger.md`：全书重要主张及其当前证据状态。
- `receipts/`：一条 Claim 对应一份或多份可追溯 Evidence Receipt。
- `.agents/skills/evidence-receipt/`：收据生成流程、证据判断规则和模板。

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
