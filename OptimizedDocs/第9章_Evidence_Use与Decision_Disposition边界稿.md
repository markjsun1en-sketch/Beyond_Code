# 第9章 Verification and Evidence Engineering
## Evidence 如何进入有权裁决，而不是把 PASS 直接写成“完成”

> 工作稿状态：对象边界稿，等待作者裁决。
> 当前仓库没有独立的第9章正文；本稿依据大纲建立未来正文接口，不替代原稿。
> 已接受 Claim：`CLM-C09-001`（`accepted + narrowed`）。
> 待裁决 Claim：`CLM-C09-002`、`CLM-C09-003`（均为 `partial / unreviewed`）。
> Evidence：[ER-20260818-003](../Evidence/receipts/ER-20260818-003__CLM-C09-001.md)、[ER-20260818-004](../Evidence/receipts/ER-20260818-004__CLM-C09-002.md)、[ER-20260818-005](../Evidence/receipts/ER-20260818-005__CLM-C09-003.md)。
> 上游接口：[第四章边界稿](第4章_Intent与Agent_Input对象边界回接稿.md)、[第六章重构稿](第6章_Truth与State_Architecture_重构稿.md)。

这份边界稿只解决三个问题：

1. “声称完成、观察到结果、验证通过、接受结果”是否属于同一个完成等级；
2. Evidence 类型是否可以排列成对所有 Claim 都成立的通用强弱栈；
3. Test PASS 在什么条件下可以形成 Acceptance，又在什么条件下只能作为 Evidence。

它不替第9章预写完整方法手册，也不新增一个覆盖 Intent、Truth、Review 和 Release 的超级对象。

---

# 9.A 候选修订：Completion 不采用单轴等级

“任务完成”可能同时指：

- Agent 声称已经完成；
- 代码变化已经存在；
- 目标行为已经被观察；
- 某组检查在声明范围内通过；
- 有权角色接受候选成为某个基线；
- 结果已经被采用或允许发布。

这些状态可以连续发生，但不属于同一种语义。

| 维度 | 回答的问题 | 示例 |
|---|---|---|
| Completion Claim | 谁声称什么工作已经完成 | “command-response correction 已实现” |
| Observation Status | 实际观察了哪个目标 | target executed / target not observed |
| Validation Status | Evidence 覆盖哪个 Claim 和 Scope | `verified-for-scope` |
| Decision Disposition（有权角色对指定目标作出的处置） | 谁接受、拒绝或保留了什么 | accepted as E1 source baseline |

因此，大纲中的：

```text
Claimed Completion
→ Observed Completion
→ Verified Completion
→ Accepted Completion
```

可以保留为教学顺序，但不能被实现为一个同质、单调的 `completion_level`。前三项主要描述断言和认知状态；Accepted 描述规范性裁决。

一个结果完全可能处于：

```text
completion_claim = submitted
observation_status = observed
validation_status = verified-for-scope
decision_target = E1 source baseline
decision_disposition = rejected
```

这不是矛盾。它表示 Evidence 支持了被测试的行为 Claim，但有权角色没有接受候选的实现范围。

同样，`accepted` 不能脱离目标单独出现。至少要说明：

```text
accepted_for = evidence chain
accepted_for = source baseline
accepted_for = qualification result
accepted_for = release decision
```

这些短语不一定是项目的固定枚举。它们强调的是：记录 Accepted 时必须保留 `decision_target`。

完整证据和限制见 [ER-20260818-004](../Evidence/receipts/ER-20260818-004__CLM-C09-002.md)。该结构性修改尚未获得作者裁决。

---

# 9.B Evidence 的三个不同问题

Evidence Engineering 不只问“证据强不强”，而要分开三个问题。

## Evidence Coverage（证据对目标 Claim 的覆盖）

回答：

> 这份 Evidence 实际支持或反驳哪个 Claim、版本、环境和 Scope？

它可以记录：

```text
unsupported
partial
verified-for-scope
counterevidence
unresolved
```

Coverage 是 Claim-dependent（随目标主张而变化的），不是证据文件自身携带的永久分数。

## Evidence Use Context（证据准备服务的决策语境）

回答：

> 当前收集这份 Evidence，是用于开发反馈、资格验证、Gate 输入，还是采用／发布决策？

例如：

```text
development feedback
bounded regression
qualification
acceptance decision
adoption decision
release decision
```

这些用途不是全书通用成熟度阶梯。项目可以定义自己的 Profile；同一份 Evidence 也可能只适合其中一部分用途。

## Decision Disposition

回答：

> 对哪个 `decision_target`，哪一个 Authority 作出了什么处置？

例如：

```text
accepted
rejected
deferred
blocked
not-decided
```

关系可以表达为：

```text
Evidence
→ evaluates a Claim for a Scope
→ is considered for an Intended Use
→ informs an Authorized Disposition
```

任何箭头都不自动赋予下一个对象 Authority。

---

# 9.C 候选修订：从 Evidence Stack 到 Evidence Portfolio

大纲当前把下列材料排成一个 Stack：

```text
Text Explanation
→ Diff
→ Static Analysis
→ Automated Test
→ Runtime Observation
→ User-facing Validation
→ Production Metrics
```

这个顺序可以表示系统暴露面逐渐扩大，但容易被误读为通用强弱等级。不同 Evidence 类型回答的是不同问题。

| Evidence 类型 | 适合支持的 Claim | 单独不能证明 |
|---|---|---|
| Text Explanation | 变更叙事、已声明的 Intent 与限制 | 目标行为真的发生 |
| Diff | 哪些 Repository 内容发生改变 | Runtime 行为正确 |
| Static Analysis | 声明规则下的静态属性 | 目标环境中的动态结果 |
| Automated Test | 被选场景在测试环境中的行为 | 实现范围必要、产品采用或发布授权 |
| Runtime Observation | 指定 Build/环境中的实际行为 | 未观察场景同样成立 |
| Human/User-facing Validation | 体验、审美或业务接受判断 | 大规模生产行为 |
| Production Metrics | 部署人群中的指标变化 | 因果来源、源代码正确性或未测风险 |

因此更稳妥的表达是 Evidence Portfolio（围绕目标 Claim 和用途组合的证据集合）：

```text
Claim + Scope + Risk + Intended Use
→ Required Evidence Portfolio
→ Coverage + Gaps + Counterevidence
```

Portfolio 不表示 Evidence 越多越好。它要求每一项材料回答一个具体问题，并暴露尚未覆盖的风险。

例如，D-048 的 exact-inventory Evidence 足以支持“验证器改变了自身 authority-bearing surface”，却不能产生目标 compile 的 PASS/FAIL。D-079 的 42 项 focused tests 支持所选行为检查，却不能单独裁决额外实现范围是否适合 E1。

完整证据和反例见 [ER-20260818-005](../Evidence/receipts/ER-20260818-005__CLM-C09-003.md)。“Portfolio 替代通用 Stack”当前仍是待作者裁决的结构建议。

---

# 9.D Acceptance-to-Evidence Mapping 必须声明裁决目标

第四章已经把 Acceptance Criterion 与 Required Evidence 关联起来。第9章不再创建另一套映射，而是补足“这份证据允许谁作出什么决定”。

最小字段可以是：

```yaml
acceptance_id: AC-01
decision_target: candidate-as-E1-source-baseline
claim_scope:
  - command-response contract
non_goal:
  - exhaustive schema mirroring

required_evidence:
  - focused contract tests
  - bounded diff review
evidence_intended_use: development-acceptance

decision_authority: human-lead
gate_delegation: none
downstream_non_claims:
  - qualification
  - adoption
  - release
```

这里的 Decision Target（裁决对象）不是新的 Truth 类型。它只是说明当前要决定的是 Evidence chain、source baseline、qualification result、supported adoption，还是 production release。

Mapping 至少要防止三种错配：

1. 用“测试套件名称”代替目标 Claim；
2. 用 Test PASS 代替实现范围裁决；
3. 把局部 Acceptance 扩张为 Adoption 或 Release。

它也必须保留 `non_goal`。否则验证器很容易把“还可以检查什么”扩张成“当前阶段必须证明什么”。

---

# 9.E 自动 Gate 可以裁决，但 Authority 必须先被委托

本章不采用“只有 Human 才能 Acceptance”的绝对规则。

项目可以明确授权机器 Gate 对一个窄目标自动作出处置。例如：

```yaml
gate_id: regression-gate-01
delegated_decision: accept-regression-result
claim_scope: parser-contract-v3
required_evidence:
  - test-suite: parser-v3-regression
allowed_disposition:
  pass: accepted-for-regression
  fail: rejected-for-regression
downstream_non_authorities:
  - supported-adoption
  - production-release
```

只有在以下条件明确时，PASS 才能直接映射到对应 Acceptance：

- `decision_target` 已声明；
- Claim、版本、环境和 Scope 已限定；
- Gate 被相应 Authority 明确授权；
- PASS、FAIL、`non-result` 和异常语义已定义；
- 授权没有被撤销、过期或越过下游边界。

没有这种委托时，Test 输出 Evidence；它不自行取得 Acceptance Authority。

这就是 `CLM-C09-001` 的收窄边界：不是否认自动 Gate，而是阻止未授权的语义升级。

---

# 9.F Acceptance、Adoption 与 Release 是不同裁决面

本书在第9章中采用以下工作定义：

| 裁决面 | 当前问题 | 可能的 Authority |
|---|---|---|
| Evidence Disposition | 证据是否适合支持指定 Claim/Scope | Validator、Reviewer、Human |
| Acceptance | 指定结果是否满足命名的 Criterion/Target | 被授权 Gate 或 Owner |
| Adoption（采用裁决：是否将结果纳入受支持基线或实践） | 项目是否开始依赖、维护或推广该结果 | Project/Product Authority |
| Release（发布裁决：是否允许分发、部署或进入生产） | 是否允许结果进入目标发布面 | Release/Operations Authority |

这些裁决可能由同一个人一次完成，也可能分散在不同角色和时间。重点不是强制流程更长，而是避免一个状态词吞掉多个决策。

```text
evidence accepted for bounded claim
!= candidate accepted as source baseline
!= result adopted as supported baseline
!= result authorized for release
```

如果某个低风险项目确实把后续决策合并，应通过明确 Delegation 表达，而不是让工具从 PASS 自行推断。

---

# 9.G 三个已取证的分离案例

| 案例 | Evidence 结果 | 实际裁决 | 明确保留的非 Claim |
|---|---|---|---|
| v4.94 D-079 | 42 项 focused tests PASS | over-scoped E1 candidate 未被接受；较小的前向修正成为后续祖先 | 不证明较小实现长期成本更低 |
| v4.94 F4a | 48/48 bounded tests PASS | Evidence 被接受为 `NON_QUALIFYING` development closure 的一部分 | qualification、Gate、production |
| lessismore SP122 | qualifying evidence chain 被 Human 接受 | supported adoption 仍 blocked | production approval |

这些案例共同支持：Evidence 成功与后续裁决可以分离。

它们不支持：

- Test 不重要；
- 测试越少越好；
- Human 应覆盖所有自动 Gate；
- 所有项目都必须采用同一组 Acceptance/Adoption/Release 状态；
- v4.94 的 E0–E3 应成为全书通用等级。

来源、版本、反证和限制见 [ER-20260818-003](../Evidence/receipts/ER-20260818-003__CLM-C09-001.md)。

---

# 9.H Evidence-Driven DoD 应输出边界，而不是一个 Done

Definition of Done 可以继续要求实现、测试、运行、视觉、性能、回归与风险 Evidence，但最终输出不应只剩：

```text
done = true
```

更可检查的最小结果是：

```yaml
completion_claim: submitted
claim_scope: parser-contract-v3
observation_status: observed
validation_status: verified-for-scope
evidence_use: bounded-regression

decision_target: regression-result
decision_disposition: accepted
decision_authority: regression-gate-01

downstream_status:
  adoption: not-decided
  release: not-authorized
```

小型任务不需要持久化整份 YAML。一句话也可以表达同样边界：

> 当前 Commit 的 parser-v3 regression 已由授权 Gate 接受；未作 Adoption 或 Release 判断。

成熟度不在于字段数量，而在于读者能否知道：什么被验证、准备用于什么、谁作出什么决定、哪些结论尚未形成。

---

# 9.I Evidence Gap（证据缺口）是决策输入，不自动等于更多治理

Evidence Coverage 不足时，可以：

- 收集更匹配的 Evidence；
- 收窄 Claim；
- 将结果标记为 `partial` 或 `non-result`；
- 推迟或阻断当前 Decision Target；
- 在高影响、不可逆或 Authority 不清时升级人工裁决。

因此，原变更说明中的：

> Low evidence coverage increases required governance.

不应直接写成普遍因果规则。更窄的表达是：

> **低 Evidence Coverage 会限制可作出的 Claim 与 Decision；是否增加治理，取决于影响、可逆性、现有授权和当前动作。**

这项收窄尚未建立独立 Claim 或完成作者裁决，本稿只记录为未来第9章与第13章的接口约束。

---

# 9.J Review Agent 的权限边界

Review Agent 可以：

- 检查 Evidence 是否绑定正确 Claim、Commit、环境与 Scope；
- 发现缺失、过期、冲突或 `non-result`；
- 检查 Acceptance-to-Evidence Mapping；
- 在被授权时执行自动 Gate；
- 向有权角色建议 accept、reject、narrow 或 defer。

Review Agent 不会因为名称中包含 Review 就自动拥有：

- 产品 Acceptance；
- supported Adoption；
- production Release；
- 扩大自身 Gate Scope 的权限。

如果项目希望 Review Agent 自动裁决，必须显式记录 Delegation、Scope、有效期和允许的 Disposition。

第10章可以继续讨论 Review 的时点、独立性和强度；第9章只定义 Evidence 怎样进入裁决。

---

# 第九章跨章接口

```text
Chapter 4
Acceptance Criterion + Required Evidence + Decision Target
        ↓
Chapter 6
Claim + Observation Boundary + Provenance + Authority
        ↓
Chapter 9
Evidence Coverage + Intended Use + Authorized Disposition
        ↓
Chapter 10
Review timing, independence and challenge
        ↓
Chapter 13
Risk-appropriate governance and decision rights
```

第9章不应重新定义 Intent、Truth、Execution Contract 或 Governance Profile。它的中心是：

> **让每份 Evidence 都能回答“支持哪个 Claim、覆盖什么 Scope、准备用于什么 Decision、谁有权作出该 Decision”。**

---

# 第九章边界结论

未来正文应保留的既有主题：

- Completion Claim、Observation、Verification 与 Acceptance 的区分；
- Evidence-Driven DoD；
- Evidence Coverage、Provenance 和 Counterevidence；
- Acceptance-to-Evidence Mapping；
- Review Agent 检查证据链的职责；
- Evidence 必须绑定 Commit、环境、版本和 Scope。

已经由 `CLM-C09-001` 接受并应回接的边界：

- Test PASS 不自动证明实现范围必要；
- 局部 Evidence Acceptance 不自动形成 Adoption 或 Release；
- 未获委托的 Agent 或 Gate 不能自行扩大裁决权限；
- 自动 Gate 的有效映射必须绑定 Decision Target、Scope 与 Authority。

等待作者裁决的结构修订：

- 不把 Claimed、Observed、Verified、Accepted 当成同质单轴等级；
- 不把 Evidence Stack 当成跨 Claim 类型的通用强弱阶梯；
- 不用一个 `done = true` 隐藏未形成的下游 Decision。

本轮不升级为既定结论：

- E0–E3 作为全书通用 Evidence 等级；
- “证据越多越成熟”；
- “所有 Acceptance 都必须由 Human 完成”；
- “低 Evidence Coverage 必然要求更高治理等级”；
- “Encapsulate Execution, Expose Evidence” 已被现有案例普遍验证；其原则性位置沿用 RR-003，证据强度另行审阅。

当前人工状态：

- `CLM-C09-001`：`accepted + narrowed`；
- `CLM-C09-002`：`unreviewed`；
- `CLM-C09-003`：`unreviewed`。

作者裁决后，这份边界稿才能作为未来第9章完整正文的结构依据。
