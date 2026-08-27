# RR-018：第六章独立 Agent 逻辑与措辞审阅

- 记录日期：2026-08-19
- 审阅对象：`OptimizedDocs/第6章_Truth与State_Architecture_重构稿.md`
- 仓库基线：`main@cd842c6fd82f`
- 文件状态：工作稿包含尚未提交的内容恢复；本记录行号绑定本次审阅版本
- 审阅方式：三个只读 `critical_reviewer` 独立检查逻辑、措辞和跨章覆盖，再由主笔归并
- 当前状态：审阅完成；所有修改建议等待作者裁决

## 结论

第六章不需要推翻重写，也不需要继续恢复原稿中的成熟度等级、Truth/State Debt 或以 Truth Registry 为中心的结构。

当前主要问题已经从“内容压缩过度”转为“对象模型尚未完全闭合”：正文虽然成功区分了 Intent、Decision、State Claim、Assumption 与 Evidence，却在局部再次混合了描述性可信度、规范性使用许可、验证覆盖、冲突关系和生命周期状态。

没有发现 P0 级结构失败。存在八组应在定稿前处理的 P1 问题，其中前五组会改变理论含义，不能只按文字润色处理。章节可以继续作为工作稿，但在这些问题解决前，不宜把当前 Schema 当作正式对象模型。

## 独立审阅边界

三个审阅 Agent 并行接收不同检查任务：

1. 概念与逻辑审阅：循环定义、类型混用、普遍化、事实与推导混合；
2. 措辞与术语审阅：绝对化、保证性措辞、双语术语和可观察过程边界；
3. 内容覆盖与章节边界审阅：对照原第六章以及第四、五、九章的职责分配。

它们没有修改正文、Evidence、原稿或外部工程。主笔只归并三者的重合发现，并保留彼此不一致的判断；Agent 的结论不自动成为改稿指令。

## 核心 Claim 复审

| Claim | 归并裁决 | 本轮含义 |
|---|---|---|
| `CLM-C06-001` | `narrow` | “单一来源不能回答所有问题”的方向成立，但有效边界应是多个状态面或决策面可能独立变化；不能外推为每个项目都需要 Authority Matrix。 |
| `CLM-C06-002` | `split` | 五种语义角色必须可辨认；这不等于必须形成五种物理文件，也不等于当前列出的 Status 枚举已经正交。 |
| `CLM-C06-003` | `narrow` | 保存版本绑定的外部执行依据有利于复查；当前证据没有证明能够完整恢复环境、重现结果或提高效率。 |
| `CLM-C06-004` | `accepted + local narrowing` | 已接受的“目标未被观察时不得虚构 PASS/FAIL”保持不变；正文仍需排除“输入改变但目标随后被观察”的反例。 |
| `CLM-C09-001` | `survives` | 已接受边界保持不变；第六章关系图仍需把 Validation Coverage 与 Acceptance Disposition 分开。 |

本轮不修改 Claim Ledger 的人工状态。`CLM-C06-001/002/003` 仍为 `unreviewed`；对 `CLM-C06-004` 的建议是修正局部推导，不是撤销作者已经作出的接受裁决。

## P1：必须先修复的逻辑问题

### 1. “事实成立”与“获准使用”再次合并

- 位置：约 64–68、258、594–600 行。
- 当前表述：把“当前可依赖的事实”定义为“当前被授权用于工程决策的 State Claim”。
- 问题：Evidence 可以改变一条描述性 Claim 获得的支持程度；Authority 可以允许某条 Claim 或 Assumption 用于特定决策，但授权本身不能把未知变成事实。
- 反例：负责人可以批准在显式不确定性下继续发布；这个 Decision 不会使对应 Assumption 成为已验证事实。
- 最小处理：分别定义 `evidence support / validation coverage` 和 `accepted-for-use for a decision target`；正文使用“当前获准依赖的 Claim”时，不再把它称为事实。

### 2. 所谓“正交元数据”仍混合多个轴

- 位置：约 224–292、1158–1160 行。
- 当前问题：
  - `test-verified` 同时表达形成方式和验证结果；
  - `counterevidence` 是 Evidence 与 Claim 的关系，不是覆盖程度；
  - `unresolved` 更接近冲突状态；
  - `conflicted` 被放入 Disposition，但冲突未必已经得到裁决。
- 反例：一条 `observed` Claim 可以同时具有部分覆盖、反向证据、未解决冲突和尚未裁决四种状态。
- 最小处理：至少分开 formation method、validation coverage、evidence relation/conflict、lifecycle 和 authority disposition；在枚举尚未修正前，不宣称它们已经正交。

### 3. Authority 公式描述的是适用边界，不是授权来源

- 位置：约 342–350、1138–1140 行。
- 当前表述：`Authority = Question + Domain + Scope + Version + Time`。
- 问题：这些字段只能限定一个既有 Authority 在哪里适用，不能说明谁通过 Owner、Policy、Role 或 Delegation 获得权威。否则任何来源都可能通过自我声明获得 Authority。
- 最小处理：改为“Authority grant 决定谁或什么拥有权威；Question、Domain、Scope、Version 与 Time 决定其 applicability”。

### 4. Decision 与 Assumption 示例违反自身生命周期模型

- 位置：约 456–539 行。
- 当前问题：
  - Decision 的 `rationale` 把“可能仍有旧版 Save”这一未验证判断藏在理由中，没有引用后文的 Assumption；
  - `temporary` 与 `active/superseded/expired` 放在同一生命周期轴；
  - 同一 Scope 下“仍然 Active，却被 supersede”自相矛盾；
  - Assumption 的 `resolved/rejected/expired` 又混合处置与生命周期；
  - Plan、Decision 和执行动作被统一写成“重新验证”。
- 最小处理：Rationale 引用 Assumption；`temporary` 改为 validity mode；Supersession 显式声明覆盖 Scope；分别使用 Claim revalidate、Plan reassess、Decision reconsider/supersede、Action reauthorize。

### 5. Evidence、Validation Rule 与 Acceptance 再次合并

- 位置：约 545–604 行。
- 当前关系图：Claim 由 `Authority / Validation Rule` 接受。
- 问题：普通 Validation Rule 更新的是覆盖或检查结果；只有被明确委托相应裁决权的自动 Gate 或角色，才能对具名 Decision Target 作出 Acceptance Disposition。
- 反例：测试确认行为 PASS，而产品 Owner 仍可拒绝实现范围；两者并不矛盾。
- 最小处理：把图拆成两条关系：Evidence/Validation 更新 Claim Coverage；有权角色或被委托的 Gate 更新具名用途的 Disposition。

### 6. `non-result` 的推出条件仍然过宽

- 位置：约 559–586、1186–1188 行。
- 当前问题：正文把“验证器阻断目标”和“验证器改变 authority-bearing surface”并列后，统一推出目标 `non-result`。
- 反例：验证器改变输入后，目标仍可能实际运行；此时存在对“改变后对象”的观察，只是该结果不能支持原预期对象的 Claim。
- 最小处理：只有 `observation_status = target-not-observed` 才推出 `target_result = non-result`；若观察对象变化，记录实际 `observed_subject` 及结果对原目标的不适用性。

### 7. State Snapshot 和 Context Manifest 被写成了不可观察的完整状态

- 位置：约 424–433、667–704、763 行。
- 当前问题：
  - State Snapshot 被图示为 `project state`，但它只能是限定范围和采集时间下的 Claim、观察及引用集合；
  - Context Manifest 被写成“Agent 实际看到了什么”，工程记录通常只能证明信息被提供、开放或被工具访问，不能证明模型注意或使用了什么。
- 最小处理：State Snapshot 定义为带 Domain、Scope、Time 和 Freshness 限制的版本化观察／引用集合；Context Manifest 统一写为“本次提供、开放或可观察访问的信息”。

### 8. State Compression 示例重新把 Decision 塞回 State

- 位置：约 814–854 行。
- 当前问题：本节声称压缩 State Snapshot，却用 `Decision: Use A temporarily...` 作为 State Summary 示例；结尾又禁止把 Decision 放进 State Index。
- 最小处理：若保留 State Summary，示例必须换成带 Scope、Version、Condition 的 State Claim；Decision 压缩规则归入 Execution Baseline 或第五章 Context Compression。

## P2：应在同一轮处理的严谨性问题

### 9. `Decision Environment Reproducibility` 超过实际承诺

- 位置：约 867–905 行。
- 问题：本节实际支持的是 traceability、inspectability 和有限 reconstructability，却使用 `Reproducibility` 与“它承诺”这类保证性表述。外部服务、工具版本、secret 或缺失 Snapshot 都可能阻止环境重建。
- 最小处理：优先使用 `Decision Environment Traceability`，或明确写成 `Reconstructability Goal`；将“承诺”改为“提高后来复查的可能性”，并继续声明不保证结果复现。

### 10. Freshness 应绑定依赖关系

- 位置：约 911–968 行。
- 问题：代码、数据或环境发生任意变化，不会自动使所有历史 Claim stale；变化必须触及 Claim 的已声明依赖、Scope 或观察条件。历史 Claim 仍可能对原 Baseline 有效，只是不再适用于当前 Baseline。
- 最小处理：区分 `historical validity` 与 `applicability to current baseline`，只沿显式依赖传播 revalidation。

### 11. Readiness 被写成普遍 Gate，且章节职责有扩张

- 位置：约 787–812、1049–1098 行。
- 问题：高风险任务的前置条件因 Domain 而异；当前 Git/Dirty Worktree 问题清单是候选检查，不是已经由证据证明的通用 Gate。低／普通／高风险三档以及 Review、Rollback 组合又接近第四章和第十三章的治理职责。
- 最小处理：第六章只保留“识别与动作相关的 State 缺口”和“持久化强度按风险裁剪”；具体阻断、升级、Review 和治理 Profile 通过跨章引用处理。

### 12. D-048 的事故事实与本书推导需要分句

- 位置：约 1006–1043 行。
- 当前问题：直接工程缺陷是 verifier self-mutation；结果分类必须区分 verifier failure、target failure 和 non-result，是在此基础上的本书推导。当前结尾容易把事故原因改写为报告语义问题。
- 最小处理：先陈述 incident defect，再陈述结果语义边界；保留“修正方案没有被本次取证证明运行成功”的限制。

### 13. “成熟系统”和“本书的增量”都是未取证的地位声明

- 位置：约 393–400、590、648、1092–1098 行。
- 问题：“成熟系统使用 Typed Records”形成隐含成熟度阶梯；“本书的增量”容易被理解为未经检索或比较的原创性声明。
- 最小处理：改为条件句，例如“多状态面、高冲突或高恢复成本的系统可能受益”；把“本书的增量”改为“本书在此关注的连接方式”。

### 14. Execution Baseline 与比较基线尚未区分

- 位置：新稿约 690–721 行；原稿约 851 行附近。
- 问题：新稿主要讨论“从什么状态开始执行”，原稿还包含“用什么基线证明变化”，例如修改前 benchmark、旧 runtime capture 或 migration 样本。二者不是同一概念。
- 最小处理：增加 `Execution State Baseline` 与 `Evaluation Comparator` 的一句边界；比较基线的选择和充分性归第九章处理。

## 跨章去重裁决

三名审阅者对“保留还是迁移”存在局部差异。主笔归并如下：

| 内容 | 主笔裁决 | 理由 |
|---|---|---|
| Evidence 与 Claim 的基本关系 | 第六章保留接口级定义 | 它是 State Claim 对象边界的一部分。 |
| `qualified-for-use`、Acceptance/Adoption/Release、D-079 展开 | 收窄后迁往／引用第九章 | 这些内容的中心问题是 Evidence Use 与 Decision Disposition。 |
| D-048 | 第六章保留短案例；完整 generator 字段与 incident 分析归第九章 | 本章需要一个 non-result 接口例，但不应让 Evidence Generator 成为 State Architecture 的中心。 |
| State Compression | 第六章只保留 State Index 的类型约束；通用压缩方法归第五章 | 第五章决定如何选择与压缩 Context，第六章只防止类型丢失。 |
| Execution Baseline Manifest | 保留，但明确为 typed references 的装配清单 | 它不能复制 Context、Authority、Evidence 与环境内容成为超级 Manifest。 |
| State Boundary | 作为 Execution Baseline 的字段组或视图保留 | 不再把它塑造成与 Baseline 并列的新正式对象。 |
| 风险档位、Review、Rollback 组合 | 第六章只留原则，机制归第四／十三章 | 防止恢复内容重新演化成简化治理成熟度。 |

## 措辞统一表

| 当前写法 | 建议边界 |
|---|---|
| Fact / State Claim / accepted-for-use | Fact 不由授权产生；分别记录描述性支持与用途裁决。 |
| Orthogonal | 只有真正可独立组合的维度才称正交；否则写“分别记录”。 |
| Authority | 区分授权来源 `Authority Grant` 与适用边界 `Authority Applicability`。 |
| State Snapshot | 始终指声明范围和时间绑定的观察／引用集合，不等同完整项目状态。 |
| Context Manifest | 记录提供、开放或可观察访问的信息，不声称模型实际注意了什么。 |
| Evidence Generation Integrity | 收窄为证据生成过程是否维持声明的观察边界。 |
| Target Observation Result | 拆成 `observation_status` 与 `target_result`。 |
| Human / Human Lead / 授权人 | 统一为“有权人类角色或授权机制”，具体角色由项目定义。 |
| active / superseded | 同一 Scope 下互斥；跨 Scope 并存必须显式说明。 |

## 建议修改顺序

1. 先修复 State Claim 元数据、Authority、Decision/Assumption Lifecycle 三组对象模型；
2. 再拆开 Evidence Coverage、Acceptance Disposition 与 `non-result` 条件；
3. 修正 State Snapshot、Context Manifest、State Compression 和 Freshness 的语义；
4. 压缩或迁移第九章、第五章和第十三章内容；
5. 最后处理 `must`、`mature`、`increment`、`reproducibility` 等措辞，并复核双语术语。

这个顺序是必要依赖，不是优先级装饰：如果先润色句子，再改对象模型，会产生二次返工。

## Human Disposition

- 本轮审阅结论：`unreviewed`
- 第六章正文：本轮未修改
- Claim Ledger：本轮未修改
- 建议下一步：作者先裁决“核心 Claim 复审”和“跨章去重裁决”，再执行正文修改

## 验证记录

- 三个独立 Agent 均报告只读完成；
- `OringinalDocs/` 未修改；
- `OptimizedDocs/` 未因本次审阅新增改动；
- `Evidence/` 未修改；
- 外部工程未访问或修改；
- 本记录仅保存归并后的审阅依据，不替代 Evidence Receipt。
