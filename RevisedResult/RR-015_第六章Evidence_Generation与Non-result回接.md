# RR-015：第六章 Evidence Generation 与 Non-result 回接

- 记录日期：2026-08-18
- 修改对象：`OptimizedDocs/第6章_Truth与State_Architecture_重构稿.md`
- 修订前基线：`d9fcd35`
- 触发 Claim：`CLM-C06-004`、`CLM-C09-001`
- Evidence：[ER-20260818-002](../Evidence/receipts/ER-20260818-002__CLM-C06-004.md)、[ER-20260818-003](../Evidence/receipts/ER-20260818-003__CLM-C09-001.md)
- 当前状态：已回接工作稿；新增措辞等待作者审阅

## 修订结论

第 6 章需要补充“Evidence 实际观察了什么”的边界，但不需要新增 Truth 类型或独立理论中心。

本轮只处理两个已经由作者接受并收窄的判断：

1. 验证器在目标观察前失败，且阻断目标执行或改变 authority-bearing input/surface 时，验证器结果与目标结果必须分开；
2. 未获 Acceptance Authority 委托或实现范围仍待裁决时，Test PASS 不证明额外范围必要，也不自动完成 Acceptance、Adoption 或 Release。

## 已实施修改

### 1. 区分范围验证与用途资格

在 6.3 中明确：

```text
verified-for-scope != qualified-for-use
```

前者描述证据覆盖；后者还依赖预期用途、风险、Gate 和 Acceptance Authority。

### 2. 增加 Evidence 观察边界

6.7 新增两个维度：

- `Evidence Generation Integrity`：证据生成过程是否保持声明的观察边界；
- `Target Observation Result`：目标是否实际执行并被观察。

同时提供最小记录字段：`observed_subject`、`observation_status`、`generator_integrity`、`target_result` 与 `intended_use`。这些字段是需要回答的问题，不是强制全书或所有项目采用统一 Schema。

### 3. 用已取证案例替换说明性案例

6.12 删除 hypothetical Save Migration，改用 D-048 Verifier Self-mutation（验证器自我修改）：

- Python import 在目标执行前生成 bytecode 文件；
- exact-inventory check 正确 fail closed；
- 目标 compile 没有执行，因此结果是 `non-result`，不是目标 FAIL；
- corrective request 是修正方案记录，不被写成已经验证成功的 target result。

### 4. 回接 D-079 的范围裁决

第 6 章仅用 D-079 说明 Evidence 与 Disposition 的分离：42 项 focused tests PASS，但 Human 拒绝额外实现范围；前向修正删除 262 行并保留 8 个回归用例。

本轮没有把 D-079 展开成完整案例。Evidence Use 与 Decision Disposition 的主要论证仍留给第 9 章。

## 明确保留的限制

- 不主张所有验证器必须完全无副作用；
- 已声明且隔离的正常输出不自动构成 Integrity failure；
- 不把 D-048 推广为所有语言、工具链或测试系统的共同缺陷；
- 不把一次 Test PASS 降格为无意义，只限制它能支持的 Claim；
- 不从 v4.94 推导普遍效率提升、function-first 唯一性或 production qualification。

## 对章节结构的影响

- 不新增章节；
- 不改变第 6 章的 Claim / State / Decision / Assumption 主模型；
- 只扩展 Evidence Record 的观察边界与用途边界；
- 第 9 章仍需后续处理 Acceptance、Adoption 与 Release 的正式关系；
- 第 13 章的 Governance Livelock 尚未进入正文修改。

## Human Disposition

- Claim disposition：`accepted + narrowed`（已由作者于 2026-08-18 裁决）
- 本轮章节措辞：`unreviewed`

## 验证记录

- `git diff --check`：通过；
- `OringinalDocs/`：相对修订前基线无变化；
- `Evidence/`：相对修订前基线无变化；
- AI_DEV_OS_Evolve：只读检查后仍为 clean `main`。
