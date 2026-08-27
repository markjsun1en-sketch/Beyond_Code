# RR-024：第13章 Governed Autonomy 首轮回接说明

- 记录日期：2026-08-24
- 工作稿：[第13章 Governed Autonomy](../OptimizedDocs/第13章_Governed_Autonomy_首轮修订稿.md)
- 原始结构：[全书大纲第13章](../OringinalDocs/beyond_code_ai_native_software_engineering_outline_zh.md)
- 新增材料：[Cognitive Control、Trust 与 Human Control Plane v0.1](../OringinalDocs/ai_native_cognitive_control_trust_human_control_plane_v0.1.md)
- 审阅依据：[RR-021](RR-021_Human_Control_Plane与认知控制架构审阅.md)
- 关联 Evidence：[CLM-C09-001](../Evidence/receipts/ER-20260818-003__CLM-C09-001.md)、[CLM-C11-001](../Evidence/receipts/ER-20260824-001__CLM-C11-001.md)、[CLM-C12-001](../Evidence/receipts/ER-20260824-002__CLM-C12-001.md)、[CLM-OUTLINE-002](../Evidence/receipts/ER-20260818-001__CLM-OUTLINE-002.md)
- 记录性质：章节回接说明，不是新的 Evidence Receipt
- 章节对象模型与措辞状态：`unreviewed`

## 回接结果

第13章已经形成独立工作稿。

中心定义被固定为：

> Governed Autonomy 是在具名 Authority、Scope、Policy、Evidence、监督和恢复条件内，系统无需逐次人工批准即可执行的动作配置。

本轮没有把自治写成 Agent 的固有属性、历史成功后的奖励或 L0–L5 单轴成熟度。章节把它改为可版本化、可过期、可暂停、可收窄和可撤销的 Delegation Configuration。

核心关系被收窄为：

```text
Structural Assurance + Operational Evidence
→ supports scoped Reliance Disposition

Authority Grant
→ permits named actions and decisions

Autonomy Profile
→ operationalizes delegated Authority
```

因此，Reliance 可以改变是否依赖某个配置，却不会自动产生 Authority；Autonomy Profile 可以实施已有委托，却不能创建或扩大委托。

## 原大纲内容保留情况

| 原大纲主题 | 新工作稿落点 | 处理 |
|---|---|---|
| L0–L5 Autonomy Level | 13.1、13.11 | 保留为可选运行模式语汇，不作为成熟度阶梯 |
| Risk-based Autonomy | 13.7 | 改为多因素判断，不压成统一 Risk Score |
| Automation Default Off | 13.5 | 收窄为绑定 Action、Resource、Environment、Impact 与 Reversibility 的策略 |
| Permission Model | 13.2、13.6 | 与 Capability、Authority Grant 和 Responsibility 分开 |
| Stop-the-line | 13.14、13.16–13.17 | 拆成 Hard Stop、Process Warning、Pause、Revoke、Takeover 与 Recovery |
| Human-in-the-loop | 13.15 | 从逐次点击改为具名裁决、授权、接管和制度审查 |

原大纲的主要问题域得到保留，但会造成单轴升级、默认扩权或 Human 按钮化的表达没有继续沿用。

## 六个对象的边界

工作稿区分：

1. Capability：技术上可能完成什么；
2. Permission：执行环境实际开放什么；
3. Authority Grant：哪个有权来源允许谁对什么目标采取或裁决什么动作；
4. Reliance Disposition：对具名配置和用途，当前 Evidence 是否足以支持依赖；
5. Autonomy Profile：已有 Authority 在运行时使用何种监督、审批、升级、停止和恢复条件；
6. Responsibility / Accountability：谁负责目标、控制设计、执行结果和最终处置。

这六个对象共同约束 Eligible Action Surface，不是按成熟度依次生成。Execution 产生的 Evidence 可以更新 Reliance，但不能反向扩大 Permission、Authority 或 Profile。

## Autonomy Profile 的处理

工作稿将 Autonomy Profile 设计为多维、版本化配置，至少绑定：

- Subject Configuration；
- Capability 与 Action Class；
- Repository、Path、Environment 与 Data Scope；
- Authority Reference；
- Supervision Mode；
- Preconditions 与 Evidence Requirement；
- Escalation Trigger 与 Protected Stop Condition；
- Recovery、Expiry 与 Revocation。

正文中的 YAML 只是设计 Profile，不是已经验证的通用 Schema。

新 Capability 不静默继承旧 Profile。是否需要新 Grant，取决于它是否跨越新的 Resource、Environment、Decision Target、风险或不可逆动作，而不是取决于 Agent 对两项任务的语义相似度判断。

## Trust 相关概念的收窄

新增材料中的 `Assured Trust` 与 `Earned Trust` 被拆为：

- Structural Assurance：边界、隔离、验证与恢复设计提供的先验控制条件；
- Operational Evidence：具名配置在具体环境和任务中的可检查运行观察；
- Reliance Disposition：有权角色对具名用途是否可依赖的当前处置。

本章不建立全局 Trust Score，也不写“成功历史产生 Authority”。运行历史需要同时保留 Failure、Rework、Rollback、Human Intervention 和 Incident，而不是只累计成功次数。

## 治理强度与停止语义

原材料中的 Governance Floor 被收窄为 Protected Control Floor：它绑定 Action Class 与 Environment，不是全项目 G0–G4 等级。

工作稿允许 Policy 预先授权治理强度变化，但执行主体不能静默改变自己的 Grant、Protected Floor 或 Revocation 条件。该边界替代了“治理只能单调升级”的绝对规则。

Stop-the-line 被拆成：

- Hard Stop：阻止当前可达的高影响危险、越权动作或 false promotion；
- Process Warning：提示治理对象增长、Proof Surface 膨胀或流程失衡；
- Pause、Restrict、Revoke、Expire、Takeover：不同的处置状态；
- Recovery：处理已经发生的状态变化和不可逆副作用。

Process Warning 可以触发收窄、重分阶段或 Human checkpoint，但不应自动制造下一份同类 Governance Transaction。

## Evidence 回接边界

正文只使用已登记 Evidence 支持以下项目内边界：

- D-048 支持 Validator Integrity 作为 Stop Condition，并区分目标 `non-result` 与目标 FAIL；
- D-073 至 D-075 支持把 Governance Artifact 增长视为 Process Warning，同时保留严格控制曾发现真实缺陷的反向证据；
- D-079 支持 Test PASS、Scope Acceptance、Adoption 与 Release 的 Authority 分离；
- SP122 和 v4.94 的记录支持 Decision Disposition 可以分层，但不证明任何统一 Autonomy Schema。

这些证据没有提供自治效率、治理成本、缺陷逃逸或接管时间的跨配置量化对照。

## 有意不进入本章的内容

- L0–L5 是所有项目必经的成熟路径；
- 模型能力越强就自然拥有更多 Authority；
- 成功次数或 Trust Score 自动升级 Autonomy；
- Capability、Permission、Authority 与 Responsibility 是同一对象；
- 新 Capability 自动继承旧 Grant；
- Agent 能创建 Subagent 就能转交全部 Authority；
- 所有动作一律 Default Off；
- 治理强度只能增加、不能由既有 Policy 收窄；
- 所有 Process Warning 都必须 Hard Stop；
- Human-in-the-loop 等于每一步点击确认；
- 任意 Human 都可以覆盖安全、合规或职责分离 Policy；
- Test PASS 自动形成 Acceptance、Adoption 或 Release；
- v4.94 已验证本章对象模型具有普遍最优性。

## 与相邻章节的接口

- 第12章拥有 Human-facing Projection、Progressive Disclosure 与 Decision Surface；
- 第13章拥有 Authority Grant、Delegation、Autonomy Profile、Supervision Mode、Revocation 与 Takeover Contract；
- 第14章拥有 Telemetry Source、Observation Coverage、Detector Health、Exception Lifecycle 与 Intervention；
- 第15章拥有 Memory Promotion、Retrieval、Conflict 与 Expiry；
- 第16章拥有 Workflow Candidate、Baseline、Calibration 与 Adoption。

第13章读取 Observation 与 Evidence 来改变运行配置，但不把 Telemetry、Memory 或 Workflow Registry 吸收到 Autonomy 对象中。

## 当前审阅点

本章对象模型和措辞尚未由作者单独裁决。下一轮应重点检查：

1. 六对象拆分是否过细，尤其 Reliance Disposition 是否应留在第9章并仅在本章引用；
2. Autonomy Profile YAML 是否适合正文，还是应移到附录；
3. Supervision Mode 表是否仍然会被误读为等级；
4. Protected Control Floor 与第7、14章是否重复；
5. Governance Cost 是否需要第20章的量化方法支持；
6. v4.94 三个案例的篇幅是否与现有 Evidence Coverage 相称；
7. 核心命题“Autonomy does not earn Authority”是否需要登记为独立 Claim 并进行正式反证。

## Human Disposition

- 章节逻辑与措辞：`unreviewed`
- Decision by：pending
- Decision at：pending
- Rationale：现有 accepted Claim 只支持章节中的部分边界；本章组合出的对象模型和设计建议仍等待作者接受、收窄、拆分或撤回。
