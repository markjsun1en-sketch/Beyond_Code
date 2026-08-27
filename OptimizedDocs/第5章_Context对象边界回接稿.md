# 第5章 Context Engineering
## 从 Context 原则集合到可组合的信息系统

> 工作稿状态：对象边界回接稿，不替代 [第5章原稿](../OringinalDocs/第5章.md)，也不是完整章节重写。
> 回接说明：[RR-020](../RevisedResult/RR-020_前六章首轮分别调整说明.md)。
> 适用边界：本稿把 Context Contract、Context Pack 与 Context Manifest 作为可组合的信息接口，不在本章重新定义 Truth，也不把 Context Pattern 排成统一成熟度等级。

这份回接稿解决三个接口问题：

1. Context 是“应提供的信息”还是“实际提供的信息”？
2. Context 如何引用 State Claim，而不在第五章重复定义 Truth？
3. Context Pattern 是线性成熟度，还是可以组合的设计维度？

---

# 5.A Context 是受控的信息表面

Context 不是 Prompt 的附件，也不是项目知识的完整副本。

本章采用以下定义：

> **Context 是一次 Agent 推理或执行时可访问的、经过选择的信息表面。它影响 Agent 对项目世界的工作表示，但不等于项目现实，也不等于模型内部的完整世界模型。**

这个定义刻意区分：

```text
Project State                 项目实际处于什么状态
Available Information        系统能够检索到什么
Selected Context             本次决定提供什么
Agent Input                  Harness 向本次运行边界提交什么
Agent Interpretation         Agent 如何理解这些输入
```

Context Engineering 能直接控制的是中间两层，并通过 Harness 影响 Agent Input。它不能保证模型一定正确理解，也不能把未观察到的现实自动变成事实。

因此，“为 Agent 构建正确的工作世界”更适合作为教学比喻；正式表述应是：

> 为 Agent 构建与当前 Intent、风险和授权相匹配的 Controlled Information Surface。

---

# 5.B Context Contract 与 Context Manifest

原稿中的 Context Pack 同时承担了规范和记录职责，需要拆开。

## Context Contract

回答：

> 本次执行需要、允许或禁止提供哪些信息？

```yaml
required:
  - active_intent
  - target_module_instructions
  - repository_state
optional:
  - relevant_history
forbidden:
  - unrelated_private_data
freshness_rules:
  repository_state: current_worktree
  runtime_capture: within_24h
missing_context_action: escalate_or_retrieve
```

Context Contract 是规范性对象。它可以是独立文件，也可以成为[第7章](第7章_Agent_Execution_Engineering_首轮修订稿.md)所定义 Execution Contract 的一个字段。

## Context Manifest

回答：

> 本次运行装配、传输或开放访问了哪些来源和版本？

```yaml
manifest_id: CTX-2026-0810-07
attempt_ref: A-018
run_ref: RUN-018  # 仅在 Runtime 另有 Run Identity 时使用
sources:
  - path: AGENTS.md
    revision: commit-hash
    selection_reason: repository-policy
  - path: src/save/migration.gd
    revision: dirty-worktree
    selection_reason: target-implementation
omissions:
  - production_runtime_logs
freshness_checks:
  - repository_status_checked_at: timestamp
```

Context Manifest 是描述性记录。它不证明来源中的内容正确，也不证明模型注意或采用了它；它记录本次装配选择、传输或开放访问了什么。该记录本身是否可信，还取决于生成机制和 Provenance。

## Context Pack

`Context Pack` 可以保留为工程便利词，表示实际传输的文件、片段、索引和摘要集合。但它不是新的治理层：

```text
Context Contract   required / optional / forbidden rules
Context Pack       actual payload
Context Manifest   provenance record of the payload
```

---

# 5.C Context 引用 Truth，不定义 Truth

第五章不再建立自己的 Truth 类型或 Confidence 等级。

Context Item 只需要携带足够的引用信息：

```text
Source
Version / Hash
Scope
Authority for the current question
Validation Status
Freshness
Known Conflict
```

这些字段的含义由第六章的 State Claim、Evidence、Decision 与 Assumption 模型解释。

例如：

```text
Design document says migration must preserve v2 saves
```

进入 Context 后，它仍可能是：

- Approved Decision；
- 未批准 Proposal；
- 已 supersede 的历史记录；
- 仅描述作者当时判断的文档。

Selection 不产生 Authority。Retrieval 命中也不产生 Validation。

因此：

```text
retrieved != true
included != authoritative
summarized != verified
```

当 Context 来源互相冲突时，第五章负责：

- 暴露冲突；
- 保留来源和版本；
- 按 Contract 触发补充检索或升级。

第六章负责：

- 判断它们分别属于哪种对象；
- 为当前问题确定 Authority；
- 保存验证、处置和未解决状态。

---

# 5.D Minimum Initial Context + Progressive Retrieval

“Minimum Sufficient Context”适合作为优化目标，但不应被解释为执行前总能准确求出的固定最小集合。

更可执行的模型是：

```text
Minimum Initial Context
        ↓ task begins
Progressive Retrieval
        ↓ unresolved dependency
Missing-context Escalation
```

初始 Context 应足以让 Agent：

- 理解当前 Intent 与范围；
- 识别 Authority 与禁止事项；
- 定位第一批相关对象；
- 知道如何继续检索；
- 知道什么时候必须停止和升级。

渐进检索则根据执行中出现的依赖下钻：

```text
repository map
→ module instructions
→ target file
→ dependency
→ historical decision
→ runtime evidence
```

如果 Context Pack 被定义成不可越界的完整世界，缺失信息会被模型用推断补齐。真正的 Tight Boundary 应同时限制无关输入和允许有依据的下钻。

---

# 5.E Context Quality 使用不可压缩为单分数的检查项

不再使用统一的 High / Medium / Low Context Confidence。

一个来源是否值得使用，至少需要分别检查：

| 维度 | 问题 |
|---|---|
| Relevance | 它是否与当前 Intent 和任务有关？ |
| Provenance | 它来自哪里，能否定位原始来源？ |
| Authority | 它有权回答当前问题吗？ |
| Validation | 它经过了什么检查？ |
| Freshness | 它对当前版本和时间仍适用吗？ |
| Scope | 它能支持多大范围的判断？ |
| Security | 它能否携带指令，还是只能作为数据？ |
| Cost | 获取、加载和维护它的成本是多少？ |

模型自报 Confidence 可以作为弱信号，但不能替代其中任何一项。

一个来源可以：

- 高相关但低 Authority；
- 高 Authority 但已过期；
- 新鲜但未经验证；
- 已验证但只覆盖旧 Commit；
- 内容正确但不允许进入当前 Agent 的数据边界。

这些检查项会互相制约，并不声称数学上正交。例如 Authority 依赖 Scope，Freshness 会影响 Validation 对当前版本的适用性，Security Policy 也可能禁止使用高相关来源。把它们压缩成一个分数，会丢失工程决策所需的信息。

---

# 5.F 可组合的设计维度

Static、Layered、Retrieval、Lifecycle、Snapshot 和 Projection 不是一条 Level 0–5 的线性道路。它们属于不同设计维度。

## Source Organization

决定信息如何被组织和发现：

```text
static instructions
layered documentation
repository map
typed index
```

## Retrieval

决定何时、按什么依据取得更多信息：

```text
direct load
search
RAG
dependency traversal
progressive retrieval
```

## Storage / Access Tier 与 Validity Lifecycle

这两个维度不能放进同一状态序列。

Storage / Access Tier 决定信息如何被访问和存放：

```text
hot
warm
cold
archive
```

Validity Lifecycle 决定某个来源是否仍适用于当前问题：

```text
active
stale-for-current-scope
expired
invalidated
```

一个 invalidated Record 可能因为正在调查而保持 hot；一个 cold archive 也可能仍然是有效历史来源。Hot / Warm / Cold 只有在存在明确的更新、归档和恢复机制时，才是有用的运维比喻。

## Continuity

决定长任务和跨 Agent 工作如何恢复：

```text
checkpoint
handoff
context manifest
execution snapshot
progress record
```

## Projection and Governance

决定哪些角色可以访问、被授权依赖或执行哪些内容：

```text
role projection
policy filtering
data boundary
tool instruction authority
adaptive assembly
```

真实系统通常是组合：

```text
Layered Sources
+ Progressive Retrieval
+ Hot/Warm/Cold Lifecycle
+ Checkpoint projection when needed
+ Role Projection
```

组合是否合适，取决于风险、规模、任务持续时间和维护成本，不取决于 Pattern 数量。

---

# 5.G Snapshot、Manifest 与 Handoff

原稿中的 `State Snapshot`、`Context Snapshot` 和 Handoff Summary 需要区分。

| 对象 | 回答的问题 |
|---|---|
| State Snapshot | 在声明 Domain、Scope、时点与采集边界内记录了哪些 State Claim／状态引用？ |
| Context Manifest | 本次装配、传输或开放访问了哪些信息来源？ |
| Access Log | 工具层能够观察到哪些实际读取行为？ |
| Checkpoint projection（可选） | 第7章的 Checkpoint 被序列化后，当前 Attempt 进行到哪里，下一步是什么？ |
| Handoff | 哪些状态、责任和未决问题移交给下一执行者？ |

这些记录都不能单独证明模型注意、理解或采纳了什么。Interpretation 只有在外显输出、选择或动作中才能被有限推断，并应保留替代解释。

第7章拥有 Checkpoint 的正式定义。本章只允许把它序列化为面向 Context 恢复的可选投影，不建立平行的 Execution Snapshot 上位对象。一个可恢复的 Checkpoint 投影可以包含：

```text
Attempt Reference
Intent Version
Input State reference
Context Manifest reference
Completed actions
Produced changes
Open assumptions
Known conflicts
Pending validations
Next safe action
```

它不需要保存完整聊天记录，也不声称保存模型隐藏推理。

普通 Summary 容易抹掉来源、冲突和未验证假设；因此用于恢复或裁决的摘要应保留可下钻引用和不确定性，而不是只保留叙事结论。

---

# 5.H Context Projection 与 Intent Execution View

第四章的 Execution View 选择“这个角色需要理解 Intent 的哪一部分”。

第五章的 Context Projection 选择“这个角色需要访问哪些信息来源”。

两者共同参与 Agent Input 装配，但不能混为同一个对象。

```text
Intent Artifact
        ↓
role-specific Execution View

Available Information
        ↓ Context Contract + selection
role-specific Context Pack + Manifest

Execution View
+ Context Pack
+ Policy / Tools / Output Contract
        ↓
Agent Input
```

Worker 不一定需要 Controller 的全部协调记录；Reviewer 也不应只看到 Worker 对自己工作的摘要。Role Projection 应降低无关耦合，同时保留独立审查所需的原始 Evidence。

---

# 5.I Security 与指令权

进入 Context 的内容默认是信息，不自动拥有指令权。

尤其是：

- 搜索结果；
- 外部网页；
- 用户生成内容；
- Issue 和日志文本；
- 检索到的历史 Prompt；
- 第三方 Skill 或模板。

系统需要分别判断：

```text
may_read
may_quote
may_treat_as_project_authority
may_issue_instructions
may_trigger_tools
```

Least Context 不是简单减少 Token，而是减少不必要的信息暴露、错误 Authority 和攻击面。

当外部内容与项目 Policy 冲突时，Context Assembly 不应让模型自行调和成“看起来合理”的新指令；应保留冲突并按 Authority 升级。

---

# 5.J Memory 与 Skill 进入 Context 的边界

“Memory 是长期存储，Context 是当前工作集”只能作为对 Project Memory 的简化说明，不是对所有 Memory 类型的完整定义。

更准确的关系是：

```text
Project Memory / historical records
        ↓ retrieval candidate
Context selection + authority / freshness checks
        ↓
Context Pack for this run
```

Memory Record 被检索不表示它仍然正确，也不表示它已经进入当前 Agent Input。项目需要保留 Source、Scope、Freshness、Conflict 与 Invalidation。

Skill 也不能只按普通文档处理。它可能同时包含：

```text
Information content
Procedure
Instructions
Tool or mutation authority
```

因此需要分别检查：

- 内容是否仍与当前项目版本兼容；
- Procedure 是否经过当前环境验证；
- Instruction 是否有权覆盖普通 Context；
- Tool 调用和状态修改是否获得相应 Permission；
- 失败后是否存在隔离和恢复路径。

一个 Skill 过期，不必然表示其中每句话错误；它表示当前适用性尚未建立。把过期 Skill 直接注入 Context 并赋予高指令权，才会形成高风险组合。

---

# 5.K Context Capability Profile，不使用单一成熟度等级

**Context Capability Profile（上下文能力配置：描述 Context System 在选择、来源、时效、检索、连续性、投影、安全与评价等维度的当前配置）** 可以记录为：

```yaml
selection: structured
provenance: partial
freshness: manual
retrieval: progressive-search
storage_tier: hot-warm-cold
validity: explicit-invalidation
continuity: snapshot
projection: role-based
security: policy-filtered
evaluation: ad-hoc
```

Context Capability Profile 用于说明“系统具有什么能力”，而不是宣称“它处于 Level 3”。

一个小项目采用静态 Instructions，可能比复杂的 Adaptive Assembly 更可靠、更经济。动态装配只有在它能减少错误或成本，并且选择过程可检查时，才是改进。

AI Game Dev OS 当前可以作为候选案例，用于观察 Hotspace、Archive、Index、Snapshot 和 Memory Summary 如何组合；在绑定具体版本、文件和运行结果前，不应写成已经证明的成熟度等级，也不应声称它必然降低错误率。

---

# 5.L Evaluation 与成本

Context Evaluation 应把任务结果和装配过程同时纳入观察。

候选指标包括：

```text
Task Success Rate
Context Miss Rate
Noise / Irrelevant Load
Stale Context Incident
Conflict Detection Rate
Retrieval Cost
Human Clarification Rate
Recovery Success Rate
```

Context Ablation 可以比较删除或替换某类信息后的结果，但结论必须绑定：

- 任务集合；
- 模型和工具版本；
- Context 顺序和预算；
- 重复次数；
- 成功判据；
- 不确定性。

单次任务成功不能证明一套 Context Architecture 更优。复杂的索引、Registry、自动摘要和 Adaptive Routing 也会产生维护成本与新故障面。

---

# 5.M 跨章接口

第四、第五和第六章应形成一组稳定接口，但实际执行不是严格单向流水线：

```text
Chapter 4
Intent Artifact
→ role-specific Execution View

Chapter 5
Minimum Initial Context
↔ selection / retrieval / projection

Chapter 6
Typed Records + State Claims
↔ authority / freshness / conflict resolution

Chapter 5
Progressive Retrieval as needed
→ Context Pack + Manifest

Chapter 6
Execution Baseline

Chapter 7
Work + Execution Contract
→ Agent Input
→ Attempt + Checkpoint
```

Execution Epoch 不进入这条基础链。需要长时固定引用区间时，它作为第21章定义的可选 Lifecycle 组织对象引用上述 Contract、Attempt 与 Checkpoint。

章节顺序上第五章位于第六章之前，但概念上需要前向引用并承认反馈关系：

> Context Item 的真实性、Authority 与冲突由下一章的 Claim 模型处理；本章只处理它是否以及如何进入当前信息表面。

这样第五章就不需要重复建立 Truth Registry、Decision Truth、Evidence Truth 或统一 Confidence。

---

# 第五章边界结论

第五章的中心应当是：

> **根据 Intent、风险和授权，持续选择、组织、检索、压缩、更新并记录 Agent 可访问的信息表面。**

完整重写时，建议将当前 73 个小节收敛为 RR-009 提出的 12–16 个主体模块，并用可组合设计维度替换七个线性 Pattern 和 Level 0–5 成熟度。

必须保留：

- Context 不等于 Prompt；
- More Context 不必然是 Better Context；
- Initial Selection + Progressive Retrieval；
- Provenance、Freshness、Conflict；
- Compression 后可下钻；
- Role Projection 与 Handoff；
- Security 与外部内容的 Authority 边界；
- Evaluation 与维护成本。

必须修正：

- Context 是完整世界模型；
- Context Pack 本身就是 Execution Contract；
- Context Confidence 可以概括来源质量；
- 七个 Pattern 是固定进阶；
- Adaptive 必然比 Static 成熟；
- AI Game Dev OS 已经被证明处于某个 Level。

这份边界稿确定了第五章与第四、第六章的接口，但尚未完成 AI Game Dev OS Context Architecture 的正式取证，也不把候选案例写成已验证结论。
