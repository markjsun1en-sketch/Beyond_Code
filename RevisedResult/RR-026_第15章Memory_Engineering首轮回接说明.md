# RR-026：第15章 Memory Engineering 首轮回接说明

- 记录日期：2026-08-24
- 工作稿：[第15章 Memory Engineering](../OptimizedDocs/第15章_Memory_Engineering_首轮修订稿.md)
- 原始结构：[全书大纲第15章](../OringinalDocs/beyond_code_ai_native_software_engineering_outline_zh.md)
- 新增材料：[Cognitive Control、Trust 与 Human Control Plane v0.1](../OringinalDocs/ai_native_cognitive_control_trust_human_control_plane_v0.1.md)
- 审阅依据：[RR-019](RR-019_前五章独立Agent逻辑与措辞审阅.md)、[RR-021](RR-021_Human_Control_Plane与认知控制架构审阅.md)
- 关联案例 Evidence：[CLM-C06-004](../Evidence/receipts/ER-20260818-002__CLM-C06-004.md)、[CLM-C09-001](../Evidence/receipts/ER-20260818-003__CLM-C09-001.md)、[CLM-OUTLINE-002](../Evidence/receipts/ER-20260818-001__CLM-OUTLINE-002.md)、[CLM-C16-001](../Evidence/receipts/ER-20260824-003__CLM-C16-001.md)
- 记录性质：章节回接说明，不是新的 Evidence Receipt
- 章节对象模型与措辞状态：`unreviewed`

## 回接结果

第15章已经形成独立工作稿。

Memory Engineering 被定义为：

> 对可长期检索记录的候选产生、审查准入、来源绑定、适用性维护、检索使用、冲突处置、失效与删除进行工程化管理。

本轮没有把 Memory 写成 Truth Store、完整 Archive、当前 Context、模型内部状态或组织智能本身。

中心链条是：

~~~text
Source Record
→ Memory Candidate
→ scoped Promotion Decision
→ Memory Record + Provenance
→ bounded Retrieval Candidate
→ current applicability and conflict checks
→ Context selection
→ observable use and outcome
→ reaffirm / narrow / supersede / quarantine / delete
~~~

Capture 不等于 Promotion，Retrieval Hit 不等于 Validation，进入 Context 不等于被模型理解或采用。

## 原大纲内容保留情况

| 原大纲主题 | 新工作稿落点 | 处理 |
|---|---|---|
| 单次智能与组织智能 | 15.1–15.2 | 保留；Memory 只提供连续性的一部分 |
| 七种 Memory 类型 | 15.5 | 改为可重叠 Record Role，不作为互斥分类 |
| Memory Provenance | 15.7–15.9 | 保留；增加 Derivation、Transformation、Omission 与循环来源检查 |
| Memory Pollution | 15.10–15.11 | 扩展为范围、时效、Authority、同源重复、跨项目传播和 Instruction 污染 |
| Capture→Validate→Store→Retrieve→Reconfirm→Deprecate→Delete | 15.12–15.15 | 拆为 Admission、Applicability、Supersession、Retention 四条独立轴 |
| 项目与跨项目知识分离 | 15.20–15.21 | 保留；跨项目使用必须生成目标侧 Candidate |
| Memory Review | 15.23 | 改为风险和事件触发，不要求定期全文重读 |

原大纲问题域均得到承接，但线性生命周期、Fact Memory 永久有效和项目经验自动通用化的含义没有保留。

## 七个工程对象

工作稿区分：

1. Source Record：Primary Artifact、Observation、Decision、Incident、Commit、Test 或 Human Note；
2. Memory Candidate：被提议用于未来用途、尚未完成准入的记录或总结；
3. Promotion Decision：有权主体决定是否以具名用途、Scope、状态和期限准入；
4. Memory Record：经过准入、保留来源和适用边界的长期记录；
5. Memory Index：用于发现记录的导航结构；
6. Retrieval Candidate：Search 命中但尚未完成当前适用性检查的记录；
7. Use Record：记录 Selected、Supplied、Accessed、Cited 或 Adopted 等可观察过程。

Promotion Authority 只决定记录是否进入长期检索面，不会因此获得底层事实的 Truth Authority。

## Record Role 的收窄

Fact、Decision、Experience、Skill、Preference、Failure 和 Constraint 被改为可重叠 Record Role。

主要边界是：

- State / Fact Claim 继续绑定 Subject、Scope、Time、Source 和 Evidence；
- Decision Memory 保留 Decision Target、Authority、理由和 Supersession；
- Experience 只形成 Lesson Candidate，不自动成为通用规律；
- Skill Memory 被改为 Procedure / Skill Reference，不自动激活 Tool 或 Authority；
- Preference 绑定 Owner、产品面、时间和 Override；
- Failure Memory 分开事实、根因状态、Correction 与未解决项；
- Constraint / Policy Reference 保留 Authority 与 Effective Time。

`Fact Memory` 不被视为永恒事实；它通常只是保存了一个有边界的 Claim。

## Promotion、Provenance 与 Summary

工作稿新增候选 Memory Promotion Contract，要求声明：

- Future Decision Use；
- Primary Source 与 Derivation；
- Epistemic Type；
- Scope 与 Exclusion；
- Counterevidence；
- Compatibility；
- Retention 与 Privacy；
- Promotion Authority；
- Invalidation Trigger；
- Review Cost。

Derived Memory Summary 被视为新的二级记录，不是 Source 的透明副本。它需要 Source List、Transformation、Omitted Surface、Intended Audience、Generated At、Review Status 和 Drill-down。

同一 Source 派生出的多个 Summary 不能被当作多个独立证据来源。

## Memory Pollution 与 Amplification

污染被扩展为：

- 错误 Source；
- Summary 丢失 Scope；
- Decision 被改写成 Fact；
- Preference 被改写成 Policy；
- Workaround 被改写成标准 Procedure；
- Historical Claim 被写成 Current State；
- Retrieval Match 被当作 Compatibility；
- 同源 Summary 制造伪佐证；
- 派生 Memory 循环引用；
- Prompt Injection 持久化；
- 过期 Skill 获得当前 Authority；
- 项目特例被推广为跨项目规则。

Memory Amplification 关注 Retrieval Frequency、Injection Frequency、Decision Impact、Instruction Weight、Lifetime、Cross-project Reach、Source Visibility 和 Recovery Cost，不压成单一分数。

污染后的响应包括 Narrow、Attach Conflict、Rebuild Summary、Remove Instruction Authority、Quarantine、Supersede、Delete 等，不只有删除。

## Lifecycle 与 Conflict

原线性 Lifecycle 被拆成：

- Admission Status；
- Epistemic / Applicability Status；
- Supersession Status；
- Storage / Retention Status。

Expiry 与 Invalidation 只表示当前用途的适用性需要重新建立，不自动把历史内容变成 False。

Conflict 被拆为 Direct Claim、Temporal Supersession、Scope、Authority、Applicability、Preference、Evidence 和 Instruction Conflict。

Embedding Similarity 只能发现候选相关项，不能决定 Authority 或自动融合冲突。

Supersede、Deprecate、Quarantine、Delete 与 Tombstone 被分别定义，避免删除敏感内容、保留历史和防止重新导入之间的语义混乱。

## Retrieval 与 Context

第5章拥有 Context Assembly，第15章只提供 Retrieval Candidate 和适用性检查。

工作稿进一步区分：

- retrieved；
- selected；
- supplied；
- accessed；
- cited；
- adopted。

Access Log 不能证明模型理解、相信或依赖了某条 Memory；没有 Citation 也不能证明完全没有影响。

## Skill、Preference 与跨项目传播

Skill 被拆成 Information、Procedure、Instruction、Tool Binding、Permission、Authority、Verification 与 Recovery。Memory 可以保存 Skill History 和 Candidate，但不能安装、激活或授予 Authority。

Preference 可以是 Explicit 或 Inferred。Agent 推断只能成为 Candidate，不能静默升级为 Project Identity。

跨项目传播必须保留原 Namespace，并生成目标侧 Candidate，完成依赖翻译、Compatibility Check、验证和目标 Authority 裁决。

## Evidence 回接边界

现有案例仅用于说明错误 Memory Summary 会怎样破坏对象边界：

- D-048 不能被记成“Target Compile FAIL”；实际是 Observer Integrity Failure 与 Target `non-result`；
- D-079 不能被记成“通过 42 个测试的 Candidate 已被证明最好”；Human 拒绝其 E1 Scope；
- D-073 至 D-075 不能被记成“严格治理总是有害”；现有事实只支持项目内的 Governance Livelock 序列和受限推导；
- v4.94 后续 `NON_QUALIFYING` 边界必须随 Lesson 一起保留。

这些 Receipt 没有证明：

- AI Game Dev OS 已实现本章 Memory Lifecycle；
- Memory Promotion 改善长期效率或质量；
- 本章 Record Role 和 Conflict 类型具有普遍完备性；
- Vector Retrieval、Graph Memory 或自动摘要优于简单 Decision Log；
- 跨项目传播流程能够防止所有错误泛化。

## 有意不进入本章的内容

- 更多 Memory 自动产生更多智能；
- Archive、Log、Transcript 与 Memory 是同一对象；
- Memory Record 自带 Truth；
- Promotion 等于验证；
- 每次成功都自动形成最佳实践；
- 重复出现次数等于独立证据；
- Summary 无需保留 Primary Source；
- Retrieve 等于 Use；
- Accessed 等于 Understood；
- Skill Record 被检索后获得 Tool Permission 或 Authority；
- 一次 Human 选择成为永久 Project Preference；
- Memory Conflict 由模型静默融合；
- Expiry 等于 False；
- Deprecated 等于 Deleted；
- 删除正文即可完成删除；
- 项目成功自动产生跨项目有效性；
- HCP 拥有新的 Memory Store；
- AI Game Dev OS 已验证完整 Memory Engineering 架构。

## 与相邻章节的接口

- 第5章拥有 Context Contract、Pack、Manifest 与 Progressive Retrieval；
- 第6章拥有 State Claim、Source、Provenance、Applicability 与 Conflict；
- 第9章拥有 Evidence Use 与 Decision Disposition；
- 第12章拥有 HCP Projection 与 Drill-down；
- 第13章拥有 Promotion、Adoption、Delete 和 Transfer 所需 Authority；
- 第14章拥有候选 Observation、Exception 与使用反馈；
- 第15章拥有 Candidate、Promotion、Record、Index、Retrieval、Conflict 与 Expiry；
- 第16章拥有 Workflow / Skill Candidate、Calibration 与 Adoption。

第15章保存行为变化的历史和候选经验，但不直接修改 Skill、Workflow、Agent Contract 或组织结构。

## 当前审阅点

本章对象模型和措辞尚未由作者单独裁决。下一轮应重点检查：

1. 七对象拆分是否过细，Use Record 是否值得成为正文对象；
2. 七种 Record Role 是否与原大纲类型相比更清楚；
3. Promotion Contract YAML 是否应移入附录；
4. Admission、Applicability、Supersession、Retention 四轴是否过重；
5. Conflict 类型是否与第6章重复；
6. Skill 与 Preference 的篇幅是否应分别移到第16章和项目身份章节；
7. Security / Privacy 是否需要在第19章展开；
8. 三个 v4.94 案例是否足够说明污染，而不会被误读为 Memory 实现证据；
9. 核心命题“Memory preserves claims; it does not create Truth or cross-project validity”是否需要登记独立 Claim 并正式取证。

## Human Disposition

- 章节逻辑与措辞：`unreviewed`
- Decision by：pending
- Decision at：pending
- Rationale：现有 Receipt 只为案例边界提供 Evidence；本章 Memory 对象模型、Lifecycle 和跨项目传播建议仍等待作者接受、收窄、拆分或撤回。
