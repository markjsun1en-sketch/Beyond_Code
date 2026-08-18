# RR-016：第九章 Evidence Use 与 Decision Disposition

- 记录日期：2026-08-18
- 修改对象：`OptimizedDocs/第9章_Evidence_Use与Decision_Disposition边界稿.md`
- 修订前基线：`e6b8b23`
- 原始材料：第9章大纲、Human Smoothing / Tight Boundaries 变更说明、Execution Epoch 跨章变更说明
- 核心 Evidence：[ER-20260818-003](../Evidence/receipts/ER-20260818-003__CLM-C09-001.md)、[ER-20260818-004](../Evidence/receipts/ER-20260818-004__CLM-C09-002.md)、[ER-20260818-005](../Evidence/receipts/ER-20260818-005__CLM-C09-003.md)
- 当前状态：已建立边界稿；两个新增结构 Claim 与全部章节措辞等待作者裁决

## 前提检查

仓库目前没有独立的第9章正文，只有大纲和跨章变更说明。因此本轮不能称为“修订第9章正文”，只能建立未来正文需要遵守的对象边界。

已接受的 `CLM-C09-001` 足以支持 Test PASS 与范围／下游裁决分离，但不足以自动接受以下两个新判断：

- `CLM-C09-002`：Completion 四层不是同质单轴状态；
- `CLM-C09-003`：Evidence Stack 不应被解释为通用强弱等级。

两者已经登记为 `partial / unreviewed`，没有因写入工作稿而变成人工接受结论。

## 对大纲的结构判断

### 1. “完成声明的四个层次”混合两类状态

`Claimed / Observed / Verified` 主要涉及断言与认知覆盖；`Accepted` 涉及有权角色或 Gate 对指定目标作出的规范性处置。

它们可以作为教学顺序，但不应压缩进单一 `completion_level`。

### 2. Evidence Stack 存在通用强弱阶梯的误读风险

Diff、Static Analysis、Automated Test、Runtime Observation、Human Validation 与 Production Metrics 各自适合回答不同 Claim。排序可以表达暴露面变化，不能自动表达跨 Claim 的强弱。

当前建议将其改写为 Evidence Portfolio，并明确 `Claim + Scope + Risk + Intended Use`。

### 3. Review Agent 的名称不产生裁决权

Review Agent 可以检查 Evidence、执行已授权 Gate 或提出处置建议。Acceptance、Adoption 与 Release Authority 必须通过显式 Delegation 获得。

## 已实施边界

1. 用 Completion Claim、Observation Status、Validation Status 与 Decision Disposition 替换单轴完成等级；
2. 区分 Evidence Coverage、Evidence Use Context 与 Decision Disposition；
3. 将 Evidence Stack 收窄为按 Claim 组合的 Portfolio 候选模型；
4. 扩展第四章 Acceptance-to-Evidence Mapping，增加 `decision_target`、`claim_scope`、`non_goal`、`evidence_intended_use`、`decision_authority` 与 Gate Delegation；
5. 明确授权机器 Gate 可以作出窄裁决，避免把“Human 必须裁决一切”写成绝对规则；
6. 用 D-079、F4a 和 SP122 展示 Evidence 结果与后续处置的分离；
7. 将 Evidence-Driven DoD 从 `done = true` 收窄为带 Claim、Evidence、Authority 与下游非 Claim 的完成记录；
8. 保留第10章负责 Review 时点与独立性、第13章负责风险治理，避免第9章吸收整个 Control Plane。

## 事实、推导与建议的分离

### 可观察事实

- 当前第9章大纲把四种 Completion 并列为层次，并把异质 Evidence 类型排成 Stack；
- D-079 的 42 项 focused tests PASS 与 Human 拒绝 over-scoped candidate 同时成立；
- F4a 的 48/48 PASS 被限定为 `NON_QUALIFYING` bounded evidence；
- SP122 Human 接受 qualifying evidence chain 时，supported adoption 和 production 仍未获批。

### 事后推导

- Verification success、source-scope fit 与 downstream disposition 是不同问题；
- Evidence 类型的价值依赖目标 Claim 和 Intended Use；
- `accepted` 必须绑定 Decision Target 才具有可审计语义。

### 当前建议

- 正交保存 Completion 与 Disposition；
- 用 Evidence Portfolio / Coverage Map 替代通用强弱栈的读法；
- 自动 Gate 必须显式记录授权范围和下游非权限；
- Evidence Gap 优先触发收窄 Claim、补证、阻断或风险判断，不直接推导“更多治理”。

## 明确保留的限制

- 不证明正交 Schema 比单字段模型具有更低缺陷率或更低成本；
- 不证明 Evidence Portfolio 在所有项目中优于 Stack 图示；
- 不把 D-079 推导成“测试越少越好”；
- 不把 Human 裁决推导成所有 Gate 都必须人工执行；
- 不把 E0–E3 升级为全书通用等级；
- 不改变 RR-003 对 “Encapsulate Execution, Expose Evidence” 原则位置的判断，只拒绝把它写成已经获得普遍案例验证。

## 与此前结论的一致性

本轮没有反转 RR-003、RR-011 或 RR-014：

- Human Smoothing 仍是有用候选原则；
- Execution Epoch 和 G0–G4 仍未获得跨书扩散证据；
- v4.94 仍只支持具体过程边界，不证明普遍效率；
- 新变化仅来自对第9章大纲类型混用的显式登记，以及作者已接受的 `CLM-C09-001`。

## Human Disposition

- `CLM-C09-001`：`accepted + narrowed`（既有裁决）
- `CLM-C09-002`：`unreviewed`
- `CLM-C09-003`：`unreviewed`
- 本轮边界稿措辞：`unreviewed`

## 验证记录

- `git diff --check`：通过；
- `OringinalDocs/`：相对基线无变化；
- 两份新 Receipt：字段完整，均保持 `partial / unreviewed`；
- AI_DEV_OS_Evolve：clean `main`；
- lessismore：tracked diff clean；既有未跟踪 Godot 生成文件保持在原处，本轮没有写入。
