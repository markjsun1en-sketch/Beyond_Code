# 第6章 Truth and State Architecture
## 让 Agent 面对真实的不一致

在 AI Game Dev OS 的早期，我用过一句很简单的原则：

> Doc as Intent, Code as Truth.

它解决了一个当时很实际的问题。Agent 很容易相信一份写得完整、语气确定的设计文档，却不知道那份文档描述的是未来方案、已经放弃的方向，还是尚未实现的目标。先把文档当作意图，把代码当作当前实现，可以阻止它根据“应该是什么”去想象“现在已经是什么”。

这句原则至今仍然有用。但项目继续发展以后，它开始显得不够。

代码里可能已经有一个功能，生产环境却没有启用；Repository 已经更新，当前 Build 仍来自上一个 Commit；设计文档要求方案 A，代码实现方案 B，运行时表现又更接近 C；测试验证的是旧行为，项目里还留着一个后来已被推翻的决定；与此同时，Agent 所在的 Worktree 还有一组不属于当前任务的修改。

这些材料可以同时存在，也可以分别正确。问题不再是“缺少信息”，而是每份信息回答的问题不同，版本不同，权威边界也不同。

更强的模型不一定会自动解决这种冲突。它反而可能把彼此不兼容的材料解释成一个语言上非常连贯、工程上从未存在过的世界。

Truth and State Architecture 要处理的，就是这个问题。

它不试图保存哲学意义上的“真理”，也不建立一个由系统写入最终答案的数据库。它管理的是关于项目状态的主张、形成主张的依据、仍然存在的未知，以及这些内容在什么范围内可以被当前工作依赖。

---

## 6.1 “Code as Truth”必须带着问题使用

先看一个最容易混淆的例子。

如果我们问“当前源代码实现了什么”，Repository State 通常是最直接的来源。这里的 Repository State 不只包括 Commit，还可能包括 Branch、Worktree、尚未提交的修改、生成源和 Submodule。

但同一个 Repository 无法独自回答：

- 哪个 Build 已经部署；
- 当前 Feature Flag 是否启用；
- 数据库正在使用什么 Schema；
- 用户实际看见了什么行为；
- 产品是否批准继续兼容旧接口。

所以，更准确的原则不是寻找一个统治全项目的来源，而是：

> Source of Truth is scoped to a question.

也就是说，所谓“事实来源”必须先说明它在回答哪个问题。

| 当前问题 | 通常首先检查的来源 |
|---|---|
| 源实现是什么 | Repository、Commit 与 Worktree |
| 某个 Build 包含什么 | Build Artifact 与构建元数据 |
| 运行时实际发生什么 | Runtime Observation、Log、Trace 或 Capture |
| 数据与配置当前是什么 | 数据／配置系统及其版本记录 |
| 当前应该遵守什么 | 有效的 Decision、Policy 与对应授权 |

这张表不是固定优先级。一次 Runtime Capture 可以直接反驳“当前界面没有重叠”这样的行为主张，却不能决定“是否允许重做整个 HUD”。后一个问题不是运行时事实，而是产品决策。

这里还要再拆开两个经常被写在一起的概念。

借用第13章会正式展开的 Authority Grant（授权记录），我们可以说明某个主体为什么能够在具名范围、条件和时间内执行某类动作或作出某类决定。Question、Domain、Scope、Version 和 Time 只说明这份 Authority 在哪里适用；它们不能凭空产生授权。

因此，更新更快的来源不必然更有权，拥有实现细节的来源也不必然拥有产品裁决权。要先确定问题，再看来源、版本、证据和授权是否对得上。

`Doc as Intent, Code as Truth` 可以继续作为简单入口，但它最好被理解为：

```text
Design document → intended state, when that is the document's role
Repository state → source implementation baseline
```

“文档”并不是单一类型。它还可能保存 Decision、Policy、Runbook、Observation、Proposal 或历史记录。把所有文档都当 Intent，只会用另一种简单化替换原来的简单化。

---

## 6.2 系统保存的是 Claim，不是 Truth

软件系统能保存的，是一句可被检查和修订的陈述，以及这句话从哪里来、适用于哪里、获得了什么支持。

本书把这样的陈述称为 Claim（主张：对具名对象、范围、时间或版本提出的、可以被支持、挑战、限定或撤回的命题）。

例如：

> Commit `abc123` 中包含从 Save v2 到 v3 的 Migration。

这是一个 State Claim（状态主张：描述某个对象在具名时间或版本下所处情况的 Claim）。它没有因为被写进 Registry 就成为事实，也不会因为 Agent 说得很有把握就获得项目权威。

State Claim 只是 Claim 的一种。Behavior Claim、Completion Claim、Risk Claim、Reliance Claim 与 Improvement Claim 也可以共享 Target、Scope、Provenance、Evidence 和 Intended Use 等关系，但它们不共享同一种验证标准。一次行为测试 PASS 不能自动验证 Improvement Claim，也不能单独完成 Completion、Acceptance 或 Release。

一条 Claim 至少要能让后来者找回几个关键条件：它在说什么对象，范围和版本是什么，谁或什么产生了它，哪些 Evidence 支持或反驳它，以及哪些结论仍然没有成立。

这里有两个问题必须始终分开：

```text
Descriptive support
这条 Claim 得到了什么范围的证据支持？

Authorized use
谁允许它被用于哪个具名决定？
```

Authority 可以允许团队在不确定条件下继续工作，但这种允许不会把不确定性变成已验证事实。反过来，一条有充分运行证据支持的 Claim，也不会自动获得产品采用或发布授权。

因此，系统必须能够诚实地表达：

```text
只在声明范围内得到验证
对当前版本尚未建立适用性
存在反向证据
冲突仍未解决
当前决定允许在某个用途下依赖
```

这些句子看起来没有一个简单的 `true` 干净，却更接近真实工程。

---

## 6.3 五种角色构成的是语义边界，不是五个文件

假设一个团队准备处理旧 Save Migration。下面五句话可能同时进入同一份任务说明：

> 希望旧版 Save 能在当前版本安全加载，同时不破坏 v3 Save。

> 在 v1.0 之前，不移除旧 Save 兼容路径。

> 当前 Repository 中存在 v2 → v3 Migration 实现。

> 仍有活跃用户持有 v2 Save。

> 三个 v2 样本经过 Migration 后都能在目标 Build 加载。

它们看起来都在描述同一件事，其实承担着五种不同角色。

第一句是 Intent Artifact（意图资产）：它记录希望达到的结果，以及为什么值得做。它不证明结果已经出现。

第二句属于 Decision Record 或 Policy Record 承担的规范性角色：它保存有权主体在具名范围内作出的要求。它告诉执行者当前应该怎样行动，但不描述世界物理上已经怎样运行。单次 Decision 与持续适用于一类未来行动的 Policy 不是同一种记录；二者在这里共享的，只是“规范性内容不等于描述性状态”这一边界。记录本身也不是 Authority 的来源。

第三句是 State Claim。它描述特定 Repository State 中可判断的实现情况，不代表该实现已经构建、部署或在真实数据上安全运行。

第四句是 Assumption（假设）：团队尚未验证，却暂时需要用来界定工作的未知。它不是“置信度较低的事实”，而是一项带有影响、验证路径和失效条件的工作输入。

第五句来自 Evidence Record（证据记录）：某次具名观察、测试、测量、截图、日志或评审形成的可检查材料。Evidence 可以支持或反驳 Claim，却不是 Claim 本身。

这五种语义必须能被区分，但不要求实现成五个数据库表或五份文件。一份任务说明可以同时引用它们，一份不可变测试报告也可以既是 Evidence Artifact，又是关于那次运行的 Primary Source。

真正危险的不是“载体合并”，而是语义静默转换：

- 把 Intent 当成 Current State；
- 把 Assumption 写成已验证 Claim；
- 把测试记录直接写成产品批准；
- 把 Decision 当作它所约束的现实已经发生；
- 把 Agent 的陈述当作项目权威。

是否值得拆成独立 Record，要看它们是否会被多处复用、是否拥有不同生命周期、冲突是否昂贵，以及以后是否需要追踪。一个局部、低风险、马上就能验证的任务，没有必要为了遵守这套区分而制造五份表单。

---

## 6.4 不要把不同问题压进一个 Status

团队很容易为 State Claim 设计一个看似方便的字段：

```text
Observed
Verified
Derived
Approved
Stale
Rejected
```

问题在于，这些词回答的并不是同一件事。

`observed` 说明主张怎样形成；`verified-for-scope` 说明验证覆盖到哪里；`stale-for-current-baseline` 说明它是否仍适用于当前基线；`approved` 则通常属于外部 Decision，而不是 Claim 的描述性状态。`rejected` 如果不说明被谁、针对什么用途拒绝，也几乎没有可操作含义。

与其寻找一个万能 Status，不如分别保留会改变判断的维度：

| 需要回答的问题 | 可能的表达 |
|---|---|
| 描述哪个状态面 | Repository、Build、Runtime、Data、Configuration、Environment |
| 主张怎样形成 | observed、measured、inferred、reported、declared |
| 验证覆盖到哪里 | unverified、partial、verified-for-scope |
| Evidence 与它是什么关系 | supporting、counterevidence、mixed |
| 是否存在竞争主张 | none detected、unresolved、resolved with record |
| 是否仍适用于当前基线 | active、stale、superseded、expired |

这些不是要求所有项目采用的固定枚举。它们只是提醒我们：形成方式、验证覆盖、证据关系、冲突和当前适用性可以独立变化。

于是，一个项目可以表达：

> 这是一条关于 Runtime 的推导性 Claim；证据只覆盖了目标场景；它对原 Build 仍有效，但与当前版本的一次新观测冲突。

这比把它写成 `verified = true` 多了几行，却少制造了一个错误结论。

至于这条 Claim 是否可以用于关闭任务、批准变更或发布产品，要由具名 Authority 针对具名 Decision Target 形成 Decision Record。Claim Use Disposition 是这份 Decision Record 对某个用途的处置关系，不是 State Claim 自身的“真值”。

---

## 6.5 “当前状态”其实由三个不同视图组成

Agent 开始任务时，我们经常说：“先把当前状态给它。”这句话至少可能指三件事。

Context Manifest（上下文清单）记录本次向 Agent 装配、传输或开放访问了哪些信息。它能保存来源、版本、选择理由和已知遗漏，也可以引用工具实际记录到的读取行为。它不能证明模型注意、理解或使用了其中每一项。

State Snapshot（状态快照）记录在声明的 Domain、Scope、采集时间和能力边界内，系统观察到哪些状态、Claim 与来源引用。一个没有进入 Snapshot 的 Feature Flag 仍然可能存在；Snapshot 是有界记录，不是项目本体。

Execution Baseline Manifest（执行基线清单）回答的是另一个问题：这次工作被授权从哪些 State、Intent、Decision、Policy 和显式 Assumption 出发。

三者可以这样连接：

```text
State Snapshot reference       有界状态观察
Context Manifest reference     本次提供的信息
Intent / Decision references   目标与规范性依据
Assumption references          明示的未知
Evidence baseline references   执行前已有的相关材料
             ↓
Execution Baseline Manifest    本次获准依赖的引用集合
```

Execution Baseline 不是把所有 Context、Evidence 和环境内容复制到一个超级对象。它更像一个带类型的索引，告诉后续 Execution Contract 从哪里开始，也让后来者知道当时依赖了什么。

它也不是用来证明变化是否改善的 Evaluation Comparator。前者回答“从什么状态开始执行”，后者回答“拿什么作为评价比较对象”；比较基线是否适用、能支持什么结论，由后续 Evidence 章节处理。

这一区分在 Dirty Worktree 中尤其重要。

一句 `dirty = true` 不足以说明风险。Agent 需要知道变化属于当前任务、用户或其他 Agent，还是临时实验；如果所有权未知，又是否与当前修改范围重叠。根据实际情况，项目可以阻断任务、隔离到另一个 Worktree、记录当前差异后限定范围继续，或明确保护无关变化。

为了得到“干净状态”而自动清理未知修改，解决的是 Agent 的操作便利，却可能破坏 Provenance 和人的工作。Dirty State 首先是所有权与授权问题，其次才是 Git 问题。

Worktree 能建立 Repository State 的隔离边界，但它不会顺便提供正确 Intent、当前 Runtime/Data/Configuration、Decision Authority 或 Evidence Coverage。隔离了一组文件，不等于隔离了整个现实。

同一份源代码也可能在不同 Build、Configuration、Environment 或 Data 上表现不同。执行前需要识别哪些 State Surface 会改变当前判断：有时只需 Commit 和 Dirty Changes；涉及部署时可能还要 Build Identity 与有效配置；涉及 Migration 时则可能需要 Data Version、代表性样本、Backup 和恢复能力。

保存的 Baseline 与当前 Observation 不一致，也不自动等于失败。差异可能来自预期变化、并发任务、过期 Snapshot 或错误环境。系统应先确认 Scope 与 Provenance，再选择重新观察、更新基线、缩小工作范围、阻断动作或进入有权裁决。

---

## 6.6 Decision 和 Assumption 让系统在未知中继续工作

信息不完整是正常状态。任何未知都阻断执行，系统会变得僵硬；让 Agent 在所有未知处自行补全，系统又会变得危险。

Assumption 提供了中间位置：团队可以明确说“我们还不知道，但当前准备怎样处理这个未知”。

一个值得保留的 Assumption 通常要说明：具体假设是什么，为什么暂时需要它，如果它错了会影响什么，谁负责验证，何时必须得到答案，以及哪些动作依赖它。

仍以 Save Migration 为例。如果“还有活跃 v2 Save”未经验证，但错误会影响不可逆的数据迁移，那么它不适合被藏在计划理由里。团队可以先检查 Save 版本分布、准备代表性样本和恢复路径；在这些信息缺失时，代码中存在 Migration 只支持“实现路径存在”，不支持“可以安全迁移生产数据”。

风险较低、容易恢复的 Assumption，可以边执行边验证。会扩大范围或影响多个依赖者的 Assumption，适合在 Checkpoint 前解决。涉及数据、发布或其他高影响状态时，依赖动作应进入项目既有的阻断或有权裁决路径。

这些不是固定的 Low / Medium / High 等级。真正起作用的是错误后果、可逆性、当前 Authority 和项目 Policy。

Assumption 得到 Evidence 以后，也不应被“原地升级成 Truth”。历史上的 Assumption 仍然是当时执行所依赖的未知；新的 Evidence 可以支持创建或更新一条有范围的 State Claim，再把原 Assumption 记为得到支持、被反驳或仍未解决。

如果它被反驳，受影响对象需要按自己的语义处理：Claim 重新验证，Plan 重新评估，Decision 重新审议，尚未执行的动作重新授权。删除旧记录只会让未来的人看不见错误路径是怎样形成的。

Decision 也有自己的生命周期。一项决定应当能够说明由谁在什么 Authority 下作出、针对哪个 Target、考虑了哪些 Evidence、适用什么 Scope、为什么选择这个方案，以及何时需要复核或被后续决定取代。

有些被否决的方案值得保留，不是为了保存所有讨论，而是为了避免 Agent 在相同条件下反复走进同一个死胡同。记录“为什么当时不选”和“什么变化后可以重新考虑”，往往比只保存最终选择更有用。

一项决定曾经被批准，也不表示它永远 Active。它可能只适用于某个版本、Sprint、平台或风险条件。历史有效与当前适用必须分开。

---

## 6.7 Evidence 首先要说明实际观察了谁

Evidence 与 Claim 的基本关系并不复杂：一次测试、测量、截图、日志或评审，在具名 Scope 与 Intended Use 中支持、挑战或限制某条 Claim。

真正容易出错的是，在解释结果之前没有先确认观察是否发生。

下面只引用几个历史片段说明局部边界。它们的完整时间线与共享 Provenance 留在第23章；来自相互反馈的项目和方法链，不等于独立的跨项目验证。

AI Game Dev OS v4.94 的 D-048 留下过一个很具体的例子。验证器在目标 Compile 运行前导入本地 Python 模块，由此在受严格清点的目录里生成了 `__pycache__` 和 bytecode 文件。第二次 exact-inventory check 正确地发现清单发生变化并停止；目标 Compile 没有执行，也没有产生 Target Result。

这次运行形成了一个有效结果：验证器改变了自己的 authority-bearing inventory。但它没有形成关于目标 Compile 成功或失败的结果。第8章把这种“目标未被观察，因此不存在目标判定结果”的情况称为 `non-result`。

后续记录提出了隔离 bytecode 副作用的修正方式，却没有在该次取证中执行一次成功重跑。因此，修正方案不能被事后写成已经验证成功。[验证器自我修改案例记录](../Evidence/receipts/ER-20260818-002__CLM-C06-004.md)

这个案例支持的边界很窄。它不说明所有验证器都必须零副作用，也不否定 exact-inventory check；恰恰是这项检查捕获了真实变化。已声明、被隔离且不改变观察对象的正常输出，不自动构成 Integrity Failure。

还要考虑另一个反例：如果验证器改变了输入，但目标随后确实运行并被观察，就不能机械地记为 `non-result`。此时应记录实际 `observed_subject`，说明结果属于改变后的对象，并解释为什么它不能支持原预期对象的 Claim。

因此，一个 Evidence Record 至少需要能够回答：实际观察了谁，观察是否完成，生成过程是否保持了声明边界，目标得到什么结果，这份材料准备支持哪个用途，以及它绑定什么 Scope、Revision、Time 与 Provenance。具体字段可以按风险和 Evidence 类型裁剪。

即使生成过程完整、测试也 PASS，Evidence 的作用仍然有限。D-079 中，一个候选实现通过了 42 项 focused tests，但有权人类仍然拒绝把它作为当前 E1 的实现范围，因为其中混入了更后阶段的工作。后续前向修正删除了 262 行，并保留当前契约需要的 8 个回归用例。

这个记录不证明更小的实现长期质量更高，也不证明更少测试更好。它只说明：测试是否通过、实现范围是否合适、Evidence 是否可被接受，以及 Change 是否进入采用或发布，是不同问题。[D-079 测试与范围裁决记录](../Evidence/receipts/ER-20260818-003__CLM-C09-001.md)

只有当项目明确把某个窄 Decision Target 委托给自动 Gate 时，测试结果才能按既定规则直接形成相应处置；这份委托不能自动扩张到 Adoption 或 Release。

这也是为什么要区分三种能力：谁能改变代码、配置、数据或部署状态；谁能提交某类 Claim 或 Observation；谁能针对具名用途作出有权处置。它们可能由 Agent、Test、Git、Gate 和 Human 分别承担，不能统称为“写入 Truth”。

---

## 6.8 冲突不是总要被解决，旧 Claim 也不总要被删除

当两份来源冲突时，最先要检查的不是哪一份语气更确定，而是它们是否真的在回答同一个问题。

Scope、Version 和时间不同，可能只是两个状态并存；规范性决定与运行时观察不同，可能是“应该怎样”和“实际怎样”之间的真实偏差；同一来源的后续版本，只有在明确覆盖相同范围时，才可能 supersede 旧记录。

冲突有时可以按有效 Authority 解决，有时可以用新的直接 Observation 检查，也可能需要产品、风险或体验责任人裁决。但当证据不足、来源分属不同范围，最诚实的结果就是：

```text
Conflict unresolved
Dependent action blocked or narrowed
```

让 Agent 知道“不知道”，至少不会把尚未解决的材料静默改写成确定答案。

Freshness 也需要同样的克制。

一条“Commit `abc123` 上所有 Migration Tests PASS”的 Claim，不会因为后来代码变化就变成历史上的 False。它仍然描述那次运行；只是如果变化触及它依赖的代码、数据、环境或观察条件，它对当前 Baseline 的适用性已经不再成立。

所以应当区分：

```text
historical validity
这条 Claim 是否仍准确描述原来的版本与运行？

applicability to current baseline
它是否还能支持现在的工作？
```

只有变化触及声明的依赖、Scope 或观察条件时，系统才有理由传播 `needs revalidation`。复杂、高风险项目可以记录 Claim Dependency；小任务直接重新检查当前文件和测试往往更便宜。

长期项目也可以维护一个很小的 State Index，帮助人和 Agent 找到当前 Snapshot、关键 State Claim、已知冲突和来源记录。它应当是导航，不是把全部项目知识复制进一个 Truth Registry。Decision 与 Assumption 继续由 Execution Baseline 引用，不能因为对当前任务重要，就被悄悄改写成描述性 State。

---

## 6.9 保存外部决策环境，而不是隐藏推理

Agent 的执行路径具有概率性。保存相同 Prompt、模型名称和代码版本，也不保证下一次得到相同过程或输出。

隐藏推理不是项目能够稳定读取和治理的工程对象。更实际的目标，是让后来者能够找到当时的外部决策环境：目标版本、起始状态、实际提供的 Context、适用的 Contract 与 Policy、模型和工具版本、需要形成的 Evidence，以及最后由谁作出了什么处置。

本书把这称为 Decision Environment Traceability（外部决策环境的可追踪性），并把有限重建当作目标，而不是保证。

SP122 的一次具名工作保存了预执行计划 Commit、修复 Revision、各 Lane 的 Owner 与允许写入面、运行身份、机器检查、Human Review、非结论和 Artifact Hash。后来者因此可以检查这次执行的边界，而不需要假装读取 Agent 当时的隐藏思考。[SP122 可追踪决策环境案例记录](../Evidence/receipts/ER-20260810-003__CLM-C06-003.md)

同一案例也保存了 active、superseded 和 conflicted 的来源。一个实现 Commit 可以说明实际实现过什么，却没有因此覆盖已批准的设计方向；Human 接受具名 Evidence Chain，也没有同时批准项目采用或生产发布。这两部分边界分别保存在 [SP122 权威冲突案例记录](../Evidence/receipts/ER-20260810-001__CLM-C06-001.md)与[结果包和 Human 处置记录](../Evidence/receipts/ER-20260810-002__CLM-C06-002.md)中。

这些记录说明外部依据可以被保存和复查。它们没有证明固定 Schema 能保证恢复成功，也没有测量这套做法是否降低了成本。外部服务会变化，工具可能消失，Snapshot 也可能过期或为空。所谓 Reconstructability，只能是“尽可能找回并识别缺失条件”，不能承诺重新运行得到同一结果。

---

## 6.10 架构的重量应由错误成本决定

Truth and State Architecture 的目标不是最大化元数据。治理本身会产生维护成本，也会过期，也可能建立新的错误权威。

修正文档中的一个错字，通常只需要确认当前文件、完成修改并检查结果。跨文件任务如果涉及多个 Decision、Dirty Worktree 或状态分歧，可能需要保存更清楚的 Baseline、Assumption 与 Evidence。面对数据迁移、生产配置、安全边界或难以恢复的状态，才更可能需要版本化 Snapshot、显式 Authority、独立 Review 和恢复路径。

任务时长、Agent 数量或对象数量都不能单独决定治理强度。真正重要的是：错误影响什么，动作能否撤回，现有 Observation 能否回答关键 Claim，冲突会不会被后续工作继续依赖，以及谁有权决定下一步。

因此，本章不要求每个项目建设 Authority Matrix、Claim Graph、State Index 或 Registry。它要求的是一种更基本的纪律：在需要作出高影响判断时，能够知道当前在谈哪条 Claim，它来自哪里，适用于什么版本，哪些未知仍未解决，以及谁可以决定怎样使用它。

Intent Engineering 回答我们希望到达哪里。Context Engineering 决定这次工作获得哪些信息。Truth and State Architecture 则阻止这些信息因为同时出现，就被合并成同一种现实。

Agent 不需要生活在一个看起来没有矛盾的世界里。它需要一个能够指出：这是目标，这是决定，这是状态主张，这是尚未验证的假设，这是只覆盖某个范围的证据，而这里仍然存在冲突的工程环境。

有了这样的起点，第7章才可以讨论如何打开一次有边界的执行；第8章再说明 Attempt 实际发生了什么、目标是否形成结果；第9章则处理这些结果如何成为 Evidence，以及有权主体最终允许它们进入哪一种下游决定。

执行动作本身不会直接产生“经过验证的 State Transition”，Test PASS 也不会替我们完成采用或发布。它们只是让下一步判断有了可以检查的依据。
