# 第4章 Intent Engineering
## Intent Artifact 如何进入 Agent Execution

> 工作稿状态：对象边界回接稿，不替代 [第4章原稿](../OringinalDocs/第4章.md)，也不是完整章节重写。
> 回接说明：[RR-020](../RevisedResult/RR-020_前六章首轮分别调整说明.md)。
> 适用边界：本稿只定义 Intent Artifact 进入 Agent Execution 的接口，不让 Intent 吸收 Context、State、Policy、Authority 或执行控制。

这份回接稿只解决一个问题：

> 第四章定义的 Intent，怎样在不吸收 Context、State、Policy 和执行控制的前提下，转化为具体 Agent 可以执行的输入？

它不为第四章增加新的理论中心。相反，它删除 `Prompt Projection` 与 `Intent Projection` 的重复，并把原稿中混合的生命周期、授权和运行时对象拆开。

---

## 4.A Requirement、Intent、Task 与 Agent Input

这四个对象可能包含相似文字，但承担不同职责。

| 对象 | 回答的问题 | 生命周期 | 主要责任人 |
|---|---|---|---|
| Requirement | 利益相关者要求或约束了什么 | 随产品和组织决策演化 | 产品、组织或授权角色 |
| Intent Artifact | 这次变化希望达到什么结果，为什么，边界在哪里 | 跨多次执行持续存在 | Intent Owner |
| Task | 当前要完成哪一段可分配工作 | 通常短于 Intent | Controller 或执行团队 |
| Agent Input | 某个 Agent 在本次运行实际收到什么 | 绑定一次运行或调用 | Harness / Controller |

Requirement 可以成为 Intent 的来源，但并不自动成为可执行 Intent。它可能包含冲突、歧义、历史遗留或尚未裁决的偏好。

当 Task 由某个 Intent 派生时，它不应静默成为新的价值目标，并应保留 Parent Intent、范围和验收关系。

并非所有 Task 都起源于 Intent Graph。调查、Incident Response、例行维护或 Evidence Collection 也可能由 Policy、告警或外部事件触发。这类 Task 应记录 Trigger Source；只有当它需要建立或改变长期价值目标时，才创建、派生或升级 Intent。

Agent Input 是一次运行的完整输入装配结果。它可以包含 Prompt 或多轮 Message，但还可能包含：

- System Instructions；
- Context Manifest 指向的材料；
- Policy 与 Tool Schema；
- Execution Contract；
- Output Schema；
- 当前 Runtime Observation。

本章所说 Prompt，是 Agent Input 中的指令／消息表达层，而不是所有运行输入的同义词。实际序列化 Prompt 可能具有审计价值，但不应成为长期 Intent 的唯一载体。

因此：

```text
Intent != Prompt
Intent != Task
Agent Input != Intent alone
```

---

## 4.B Intent Artifact 的最小职责

Intent Artifact 描述 Desired Outcome，并保存这项期望的身份、来源和边界。

一个标准对象可以包含：

```yaml
intent_id: INT-042
parent_intent_id: INT-010
version: 3
owner: product-owner
status: active

motivation: 为什么需要这项变化
desired_outcome: 希望出现的结果
in_scope:
  - 本次允许改变的范围
out_of_scope:
  - 明确不应顺便处理的范围
constraints:
  - 必须满足的限制

acceptance_targets:
  - AC-01
required_evidence_refs:
  - EV-01
human_decision_points:
  - HDP-01

source_requirements:
  - REQ-017
assumption_refs:
  - ASM-009
decision_refs:
  - DEC-012
```

最后三组字段是引用，不是把其他对象复制进 Intent。

这里的 Evidence 字段是“需要什么类型或引用的材料”，不是已经产生的 Evidence Record。Intent Artifact 不负责保存：

- 当前代码或 Runtime State；
- “已经验证”的描述性事实；
- 本次装配、传输或开放访问的全部 Context Payload；
- 工具权限和允许写入的文件清单；
- 一次运行的状态、日志或结果。

这些分别属于 State Claim、Evidence、Context Manifest、Execution Contract，以及第7–8章定义的 Attempt、Attempt Outcome 与 Result 记录。

---

## 4.C Intent 的身份、版本与生命周期

Intent 的增量价值不在于拥有一组比 Prompt 更新的内容字段，而在于它是可引用、可版本化、可继承和可裁决的工程对象。

最小身份包括：

```text
Intent ID
Version
Owner
Parent / Source
Lifecycle Status
```

Intent Lifecycle 建议只表达 Intent 自身的状态：

```text
Draft
  ↓ approval
Approved
  ↓ activation
Active
  ├─→ Superseded
  └─→ Cancelled
```

`Executed`、`Verified`、`Accepted` 和 `Failed` 不属于这条生命周期。它们描述某次 Execution 或其结果。

同一个长期 Intent 可能对应一个持续存在的 Work，并经历多次 Attempt：

```text
Intent v3
└── Work W-03
    ├── Attempt A-17 → Attempt Outcome: blocked before target
    │                  Target Result: `non-result`
    ├── Attempt A-18 → Target Result + Evaluation Result
    │                  Acceptance: rejected
    └── Attempt A-19 → Target Result + Evaluation Result
                       Acceptance: accepted
                       Adoption: no Decision Record yet
```

一次 Attempt 失败不等于 Intent 失效；一次 Target Result 被接受，也不一定意味着长期 Intent 已经完成或已经获得 Adoption。

---

## 4.D Owner、Authority 与 Agent Delegation

“AI 可以帮助生成 Intent，但不能拥有 Intent”需要收窄。

更准确的规则是：

> 最终价值目标及 Parent Intent 的变更权属于被授权的人类或组织角色；Agent 可以在明确委托范围内派生、维护或修改局部 Intent，但不能静默扩大目标和权限。

授权至少区分：

```text
propose      提出候选 Intent 或修改
derive       从 Parent Intent 派生 Child Intent
approve      批准 Intent 进入 Active
supersede    替换既有 Intent
cancel       取消 Intent
```

例如，一个 Controller 可以被授权把“完成 Save Migration”拆成测试、实现和审查三个 Child Intent，但不能自行把目标扩大为“重做整个存档系统”。

Agent 是否可以修改局部 Intent，不由模型能力决定，而由 Delegation 与 Policy 决定。

---

## 4.E Hierarchy 与 Inheritance

Child Intent 应继承 Parent Intent 中仍然适用的约束和验收关系，但继承不是全文复制。

```text
Parent Intent
├── invariant constraints
├── shared non-goals
├── acceptance mapping
└── decision boundaries
        ↓ explicit inheritance
Child Intent
├── local outcome
├── local scope
├── inherited refs
└── local exceptions
```

每一项 Exception 都应显式记录来源和授权。否则，局部优化可能通过“重新表述任务”静默抹掉 Parent Intent。

Parent Intent 更新后，不应假设所有 Child Intent 自动同步。系统需要标记：

```text
still compatible
needs review
superseded
```

这是一种 Drift 检查，不要求每个项目都建设完整 Intent Graph。

---

## 4.F Execution View：从长期对象到角色输入

本章只保留一个投影概念：`Execution View`。

Execution View 是从某个 Intent 为特定角色、任务和运行选择出的 Intent 子集。

```text
Intent Artifact
        ↓ role / task / authority projection
Execution View
```

不同角色可能看到不同侧面：

```text
Controller View
├── parent intent
├── decomposition authority
├── cross-lane constraints
└── escalation conditions

Worker View
├── local outcome
├── allowed scope
├── local non-goals
└── required evidence

Reviewer View
├── acceptance criteria
├── evidence requirements
├── known risks
└── independence constraints
```

Execution View 仍然不是完整 Agent Input。

```text
Execution View
+ Context selected under Context Contract
+ Decision / Policy references
+ Tool and Runtime capabilities
+ Execution Contract
+ Output Contract
        ↓ assembly / serialization
Agent Input
```

`Prompt` 是这组输入的一种文本序列化形式。它可以很重要，但没有必要成为第二个持久工程对象。

---

## 4.G Intent、Context、State 与 Contract 的边界

四个章节对象应保持稳定分工。

| 对象 | 核心语义 | 不应承担 |
|---|---|---|
| Intent Artifact | Desired Outcome | 当前 State、实际 Context、运行权限 |
| State Claim / Snapshot | 关于当前或历史状态的描述 | 价值目标、规范授权 |
| Context Contract / Manifest | 应提供什么 / 装配和记录了什么 | 证明材料本身为真，或证明模型实际采用了它 |
| Execution Contract | 本次执行被允许做什么、如何结束 | 长期价值目标、项目全部状态 |

跨章装配关系是：

```text
Intent Artifact                    desired outcome
Decision / Policy                  normative content under authority
State Claims + Assumptions         current basis and unknowns
Evidence / Provenance              support and counterevidence
        ↓ selection
Context Contract + Manifest        required and supplied information
        ↓ authorization
Execution Contract                 allowed action and completion gates
        ↓ runtime serialization
Agent Input
```

这不是一个要求所有项目都持久化全部对象的固定框架。低风险任务可以把多个对象压缩进一份短任务说明；高影响、高复用、跨执行、存在多方 Authority 或失败后难恢复的任务，更可能需要稳定 ID、版本和记录。任务时长与 Agent 数量只是风险信号，不是唯一条件。

---

## 4.H Acceptance 与 Evidence Trace

Acceptance Criteria 描述“什么结果可被接受”。Required Evidence 描述“用什么材料判断”。二者应该建立映射，而不是在执行结束后临时寻找证明。

```yaml
acceptance_id: AC-01
statement: 旧版 Save 可以在目标 Build 中迁移并加载
decision_target: bounded-implementation-acceptance
scope:
  build: target-build-id
  save_versions: [v2]
non_goals:
  - supported-adoption
  - production-release
required_evidence:
  - migration_test_result
  - target_build_runtime_capture
decision_authority: release-owner
```

这份映射不意味着：

- 测试通过自动完成产品接受；
- Evidence 自动成为 State Claim；
- Agent 有权裁决主观体验或发布风险。

第六章将这一区分表达为：

```text
Evidence supports or challenges Claim in Scope
Authority records a Disposition for a named Claim use / Decision Target
```

Authority 决定一条 Claim 是否足以被用于具名下游裁决，不通过处置把 Claim 本身改写成事实。

Intent Trace 可以按风险追踪：

```text
Requirement
→ Intent Version
→ Child Intent / Task
→ Work
→ Execution Contract
→ Attempt
→ Change + Attempt Outcome / Target Result
→ Evidence Use
→ Authorized Decision Record / Disposition
```

第7章拥有 Work、Execution Contract、Attempt 与 Checkpoint；第8章拥有 Attempt Outcome、Target Result、Evaluation Result、Failure、`non-result` 与 Recovery；第9章才处理结果如何进入 Evidence Use，以及具名 Authority 如何对 Decision Target 作出处置。本章只保留从 Intent 到这条执行链的引用关系。

---

## 4.I Risk-based Clarification 与治理强度

Intent 精度不等于篇幅。是否需要确认、Registry 或完整 Trace，应由错误成本和授权风险决定。

### 低风险局部任务

通常只需要：

- 一句话 Outcome；
- Scope / Non-goal；
- 一项可运行验证。

### 普通多文件任务

通常需要：

- 可引用 Intent；
- 关键 Constraint 和 Assumption 引用；
- Acceptance-to-Evidence Mapping；
- 明确允许写入范围。

### 高影响、跨执行或多方 Authority 任务

可能需要：

- Versioned Intent Artifact；
- Owner 与 Delegation；
- Parent/Child Trace；
- Decision Points；
- Execution Baseline；
- 独立 Review 与 Human Disposition。

Clarification 同样按风险决定。可逆、局部并能验证的未知可以记录为 Assumption 后继续；涉及不可逆数据、外部发布、安全或价值取舍的未知必须进入已授权的处置路径，例如 Block、Isolate、Collect Evidence、Invoke Delegated Gate 或 Escalate，而不一定只能询问 Human。

---

## 4.J 多方 Intent 冲突

Parent/Child Drift 不是 Intent 冲突的唯一形式。产品、技术、安全、体验、成本和合规可能同时提出合法但不兼容的目标。

例如：

```text
Product Intent    保持旧 Save 用户可继续进入游戏
Security Policy   禁止继续使用存在已知缺陷的解析路径
Delivery Intent   本周完成版本冻结
```

Agent 无权把三者压成一个看似一致的新目标。一个可检查的冲突记录至少需要：

```text
conflicting intent / policy references
affected scope
priority or authority source
known trade-offs
decision target
authorized resolver
current disposition
```

如果 Authority 和证据不足，允许的结果可以是缩小 Scope、延期某个目标或保留未解决冲突。Intent Engineering 的职责是保存冲突及其裁决接口，不是保证所有目标都能同时满足。

---

## 第四章边界结论

第四章的中心应当是：

> **把希望达到的结果保存为可引用、可版本化、可授权和可追踪的 Intent Artifact。**

它不需要证明 Intent Engineering 是一门完全独立于 Requirements Engineering 或 Prompt Engineering 的新学科。

本章相对 Prompt Engineering 的有效增量是：

- Intent 跨运行存在；
- Intent 有稳定 Identity 和 Owner；
- Intent 可以被版本化、继承和 supersede；
- 同一 Intent 可生成多个角色的 Execution View；
- Agent Input 由 Intent、Context、Policy、Contract 与 Runtime 共同装配；
- 执行结果可以追溯回 Intent 与 Acceptance，而不是只追溯回一段 Prompt。
- 多个合法 Intent 与 Policy 的冲突不会被 Agent 静默调和。

应删除或降级的表述包括：

- Prompt 只是一次性、无状态文本；
- Agent 绝对不能拥有任何 Intent；
- Intent 在一次执行后自动进入 Completed；
- Prompt Projection 与 Intent Projection 都是核心对象；
- Intent Object 应吸收 Truth、Context、Policy 和整个 Control Plane。

这份边界确定后，第四章完整重写时可以按 RR-008 的十个主体模块压缩，而不是把原有 44 个小节和优化说明中的 23 个提案继续叠加。
