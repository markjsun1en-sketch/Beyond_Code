# 第23章 纵向实践：AI Game Dev OS 与 lessismore
## 当自己的项目不能替自己的理论作证

写到这本书的最后一章，一个无法回避的事实摆在这里：AI Game Dev OS 是许多概念长出来的地方，却也是最不适合拿来证明这些概念正确的案例。

最初的大纲采用过一种很自然的写法。左边列 Intent、Context、Truth、Review、Memory、Governance，右边列 AI Game Dev OS 里的对应机制；然后再用 PlayerStatus 的十三步理想流程，说明这些机制怎样从 Human Intent 一直走到 Review、Human Decision 和 Skill 更新。

这种结构很完整，甚至过于完整。那十三步后来只能保留为一种重构说明，不能当成已经被观察到的执行历史。

如果一个项目的经验先产生了概念，概念又影响了系统的命名和设计，最后再用系统中出现的同名机制验证概念，我们得到的主要是设计意图的一致性。它不能告诉我们机制是否进入了真实工作，是否保护了正确的决定，是否制造了新的成本，更不能证明这套做法对其他项目有效。

真正改变第23章的，不是又找到了一组更漂亮的成功材料，而是两段看起来已经完成、实际仍保留着不同决定的历史。

SP122 留下了第一个冲突：PlayerStatus 的 18 项限定机器检查全部通过，可见候选也已经形成，Human 的视觉判断却仍然是另一个问题。v4.94 留下了第二个冲突：48 项限定测试全部通过，后来的 Development Closure 也接受了有范围的开发 Evidence，却仍明确标为 `NON_QUALIFYING`（不承担资格证明）。

两个数字看起来都很完整，却分别止步于不同的决定边界。失败、开放项和未获批准的下游决定没有因此消失；后文会按具名 Episode 展开它们怎样限制结论。

这两段历史没有证明本书正确。它们做了更重要的事：逼迫本书说明自己不能从案例中推出什么。

数字最容易掩盖这些边界。`18/18` 和 `48/48` 都只表示预先选定的检查全部通过；这里的“全部”属于分母，不代表项目整体通过。

一个 Test Result 可以成为后续决定的依据，却不能单独回答当前范围是否应被接受、视觉体验是否符合产品判断、这条路径是否应被采用或发布，也不能证明这套方法更快、更好或更安全。

只有当项目明确授权一个机器 Gate 处理某个限定的 Decision Target 时，PASS 才能按既定规则触发相应处置；这份授权不会因为测试全部通过而自然扩大。

第23章的中心问题因此不是“系统有没有 PASS”，而是：这个 PASS 支持哪个判断，谁有权作出下一项决定，还有哪些决定根本没有开始。

---

## 23.1 这是一条纵向历史，不是两个独立样本

AI Game Dev OS 与 lessismore 在案例里承担不同角色。

AI Game Dev OS 是方法与基础设施仓库。它提供 Workflow、Schema、Policy、Runtime，也留下了 v4.94 开发自身的 Proposal、Review、Incident、Test 和 Closure。lessismore 是产品与运行时仓库。它提供 Godot 游戏、UI、Art、Game Design、QA，以及 SP122 中真实发生的视觉和体验判断。

但两者共享作者、方法背景和版本反馈链。游戏项目中的问题会影响 OS 的设计，OS 的机制又会进入游戏项目，后来的写作还会改变我对早期事件的解释。

这叫 Longitudinal Case（纵向案例：沿着具名版本和事件观察问题、修正与判断如何变化）。它适合展示概念怎样从实践中产生，也适合保存失败和反例；它不构成两个独立团队对同一理论的重复验证。

为了避免把“整个项目”写成一个无法判断的对象，本章只讨论 Case Episode（案例事件单元：绑定具名 Work、版本、结果、决定和非结论的一段有限历史）。每个 Episode 都需要让读者分辨四层语言：当时留下了什么可观察记录，当时的人怎样处置，后来可以怎样有限解释，以及本书现在提出什么建议。

这四层不必并排出现，危险在于它们被揉成一句顺滑的“经验告诉我们”。

游戏开发之所以对本章有用，不是因为它代表整个软件行业，而是因为几种通常分开的判断会在同一个迭代中碰到一起。代码和数据会影响系统在特定环境中的运行；界面和美术影响玩家看到什么；自动测试检查事先写进规则的行为；截图和试玩则把仍需 Human 判断的体验问题带到眼前。

以 PlayerStatus 为例，机器可以检查布局、资源绑定和已经定义的回归行为，却不能因为这些检查通过，就替项目决定战斗中是否易读、视觉层级是否可以接受，或当前版本是否应该发布。机器结果与 Human 判断之间的边界，因此能在一个具体对象上被看见。

这就是本章所说的“高解释密度”：一段有限历史可以同时暴露机器结果、Human 判断、范围关闭和后续采用之间的差异。它描述的是案例为什么便于解释，不是这个案例能够代表多少行业。

换到其他领域，真正限制结论迁移的也不是行业名称，而是本章没有覆盖那些关键条件。

本章没有覆盖以不可逆外部伤害为主要约束、并形成相应证据的案例。它也没有覆盖需要在不同地区处理数据使用、隐私、版权或责任边界的案例。对于跨大型组织和多年运行周期的决策交接，本章同样没有可用观察。

医疗、金融或公共基础设施项目可能包含其中一项或多项，但哪些条件真正起作用，仍要回到具体项目判断。

因此，游戏项目在这里更像一面放大镜：它能让某些工程关系变得清楚，却不能替其他环境给出答案。它同时包含的工作表面较多，也不等于它比所有其他软件更复杂；复杂性有不同来源，不能只按表面数量排序。

本章只讨论这些事件发生时的历史切片。后来的版本可以修正当前系统，却不能回填早期尚未知道的内容；同一个文件名或同一句 `PASS` 如果绑定了不同版本、输入与用途，也不是同一份 Evidence。版本和决定对象本身就是案例事实的一部分。

---

## 23.2 SP122：机器已经交卷，Human 还没有作出同一个决定

SP122 的 PlayerStatus 不是一个抽象 UI 练习。它处在战斗界面里，牵涉布局、资源绑定、状态显示、消耗品交互、视觉层级和战斗可读性。

2026 年 7 月留下的 [PlayerStatus v035 当时项目记录](../Evidence/receipts/ER-20260827-001__CLM-C23-001.md) 里，候选实现已经提交，绑定和几何边界也已检查。更关键的是，记录把机器已经确认的部分，以及仍需 Human 决定的部分并排写在了一起：

> **PlayerStatus v035｜2026 年 7 月 19 日同期记录**
>
> **当时已有的结果**
>
> - 本次限定范围内的 18 项检查：`18/18 PASS`；
> - 在实际图形界面中完成的视觉捕获（非 Headless）：`QA_RESULT: PASS`；
> - 人工检查：未发现插槽裁切、重叠或状态漂移。
>
> **仍待 Human 决定**
>
> - 是否接受无底板分组与 `4px` 间距，作为最终的消耗品视觉层级；
> - 正式支持多个 Potion（药水）时，生命周期与容量如何设计。本次记录不对此作出结论。
>
> *根据当时项目记录节选并译述。*

这份记录有价值，不是因为十八项检查都通过，而是因为它没有把机器已经确认的部分，与仍需 Human 决定的部分写成同一个结果。

这里没有“机器做完了，人再盖章”那么简单。

Machine Check 判断的是被编码的断言。Visual Capture 为 Human 判断提供具名、可比较的输入。Human Aesthetic Decision 处理的是另一件事：当前视觉层级、可读性和体验是否可以在这个产品范围内接受。

截图可以证明候选确实产生过可见输出，也可以暴露遮挡和状态差异。它不能单独证明界面美观、所有战斗状态都易读、玩家偏好一致，或者 Production Art 已经完成。

这也是 Visual Capture 最容易被高估的地方。它是 Human Decision Interface 的输入，不是 Human 决定本身。

回头看，v035 让这种区别变得很具体：可机器检查的部分已经形成，视觉候选也已经可见，但具名 Human Gate 仍然打开。

---

## 23.3 一个 Sprint 可以关闭，而四件事仍然打开

SP122 最终没有留下一个可以覆盖所有关系的 `approved`。相反，[当时的 Closure 与 R2 记录](../Evidence/receipts/ER-20260827-001__CLM-C23-001.md) 保存了两项分开的 Human 决定：

> **SP122｜2026 年 7 月 29 日的两项 Human 决定**
>
> **当前阶段 Closure**
>
> - 接受包含 PlayerStatus v035 与生命周期标签修复（lifecycle-tag repair）的当前 D2 Battle 视觉／可读性基线；
> - 四项 Follow-up 对当前决定保持非阻塞；
> - 最终生产美术、Supported Adoption（纳入受支持项目路径）、Production Release（生产发布）和 v4.94 Kickoff 没有获得批准。
>
> **修复后的资格证据**
>
> - 接受用于声明用途的 qualifying evidence chain（资格证据链）；
> - Supported Adoption 仍然 blocked，Production Release 仍未批准。
>
> *根据当时项目记录节选并译述。*

第一项决定回答的是：当前 D2 Battle 的视觉与可读性范围，是否已经足以结束这轮 Sprint。四项 Follow-up 没有消失；Human 判断的是，它们不阻断这个具名目标。换一个 Claim、风险或 Decision Target，同样的 Open Item 仍可能成为阻塞项。

所以，Closure 在这里不是“零剩余工作”。它只关闭当前阶段范围。若记录最终只剩一个 `closed = true`，后来者就很容易把它误读成“可以采用”或“可以发布”。

为什么还需要第二项决定？因为第一次 Closure 从未拥有资格判断、Adoption 或 Production 的 Decision Target；与此同时，项目还保存了一段 Authority 冲突历史。早期的冲突来源曾影响运行路径，项目随后选择 Human-approved Source Chain，完成修复，并把当前 Authority 重新绑定到修正后的来源。

Source 改变以后，旧 Evidence 仍然可以说明历史上发生过什么，却不能自动承担“当前 Authority 下的 qualifying result”。项目需要重新判断哪些材料仍适用于历史事实，哪些必须绑定修正后的来源重新生成。

post-repair R2 因此回答的是另一个问题：修复后的资格证据链，是否适合它声明的用途。Human 接受了这条 Evidence Chain，但没有借此批准 Supported Adoption 或 Production Release。同一个 Human、同一个项目，甚至相邻发生的两项处置，都不会让 Decision Target 自动合并。

Evidence 获得接受而 Adoption 仍然 blocked，不是“Evidence 不够好”的同义表达。它说明这份 Evidence 的用途止于当前决定。常规 UI／QA 流程同样可以形成这种 Scoped Closure 与独立 Review；没有匹配对照，本案例不能把结果归因给 AI、Multi-Agent 或 AI Game Dev OS。

这也不意味着每一步都要等待 Human 点击。获得明确委托的机器 Gate 仍然可以处置低风险、可逆、边界清楚的结果。Human Control 保留的是未被委托的产品、体验、Scope、风险、Adoption 与 Release 决定，而不是最大化 Human Activity Volume。只有一个脱离对象和下游含义的 `approved` 按钮，并不能形成这种控制。

---

## 23.4 v4.94：当治理系统开始治理自己

第二条时间线把问题推得更远。

AI Game Dev OS v4.94 在开发自己的治理能力时，既是被修改对象，也提供一部分计划、审查、证据和处置语言。[当时的开发与 Closure 记录](../Evidence/receipts/ER-20260818-001__CLM-OUTLINE-002.md) 留下了下面这条时间线。治理 Artifact 越完整，越容易产生一种错觉：既然系统能够如此详细地说明自己，就说明治理正在有效工作。

历史没有那么配合。

```text
D-048   verifier self-mutation; target not observed
  ↓
D-073–D-075   governance activity expands; delivery evidence does not appear
  ↓
D-076   scoped and retractable recovery candidate
  ↓
D-077   two confined execution attempts fail
  ↓
D-079   selected tests pass; candidate scope rejected
  ↓
F1–F4a   source, replay, identity and 48/48 bounded evidence
  ↓
development closure remains NON_QUALIFYING
```

这些箭头只表示历史先后与后续关系，不表示前一步单独造成了后一步。尤其不能因为最后形成 Closure，就把前面所有治理活动重新解释成正确铺垫。

---

## 23.5 D-048：这一次，失败发生在观察者身上

在 [D-048 的观察者完整性记录](../Evidence/receipts/ER-20260818-002__CLM-C06-004.md) 里，任务原本准备运行 Target Compile Harness。Target 尚未执行，本地 Python import 已经产生 bytecode 文件，改变了受 exact-inventory check 保护的清单。第二次检查按设计 Fail Closed。

如果只给整个 Attempt 写一个 `FAIL`，读者会自然理解成“目标 Compile 失败”。实际发生的是另一件事：Verifier 改变了自己要保护的 Authority-bearing Surface，Target 根本没有被观察。

因此，这次运行同时留下了：

```text
verifier integrity failure   yes
target compile PASS          unknown
target compile FAIL          unknown
target observation result    none
```

关于 Verifier 的失败是有效结果；关于 Target，则是 `non-result`。

这个区分并不削弱严格检查。恰恰相反，exact-inventory check 捕获了真实的 Self-mutation。反例就在事件内部：严格控制有价值，控制的对象与记录方式仍然可能需要修正。

后来记录提出隔离 bytecode 副作用、保持执行前后清单检查的修正方式，但修正请求本身不是一次成功的 Target Run。本章也不把它补写成已经验证的结果。

更窄的建议是：当 Verifier 在观察前阻断 Target，或改变具有 Authority 意义的输入和表面时，Evidence Generation Integrity 与 Target Observation Result 必须分开。已声明、被隔离且不改变 Claim 输入的正常输出，不自动构成 Integrity Failure。

---

## 23.6 活动越来越多，交付证据却没有出现

D-048 暴露的是一个具体缺陷。后续工作却逐渐扩大了证明面。

D-073、D-074 和 D-075 连续增加 Governance、Proposal、Review 与 Transaction Artifact，却没有在这段序列中形成 Package Source、Runtime、Test、Qualification 或 Gate Evidence。D-075 的合并审阅最后记录的是 `0 blocker / 5 major / 0 minor`。

项目后来把这段序列称为 Governance Livelock。这个名字是事后诊断，不是版本历史天然携带的因果事实。可以直接观察到的是：治理路径继续前进，当前目标所需的交付结果没有出现。

这不等于文档和 Review 没有价值。它们可能澄清了风险，暴露了约束冲突，也可能为后来的恢复积累了知识。问题在于，当 Decision Target 是形成一个可运行、可观察的 Development Candidate 时，治理活动是否持续推迟了能产生这类 Evidence 的动作。

D-076 随后提出 Function-first（功能优先：先形成受限、可运行、可观察的 Development Candidate，再按具名阶段追加相称证明）。在本章里，它只能作为 Design Hypothesis（设计假设：尚待后续观察保持、收窄或撤回的工程候选）来读。它成立的前提，是当前停滞确实来自开发与后期证明义务的阶段失配；预期机制，是先让低风险候选产生可观察结果，再把 Qualification 所需的证明放回相应阶段。它被明确写成 Scoped and Retractable，而不是“以后先写代码再谈安全”；原有 Safety Envelope 与 Protected Floor 并没有被这项计划取消。计划本身也不授权结果。

如果这是一篇成功案例，下一段应该直接到达 Closure。实际出现的是 D-077：架构拆分以后，两次受限执行仍以 `SIGABRT/-6` 结束。

这两次失败不能被后续 PASS 擦掉。它们也阻止我们把 Stage Split 写成即时生效的唯一原因。Scope 收窄、调试积累、执行环境变化、前期治理知识和 Human Direction 的变化，都可能参与后续恢复。现有材料不足以分配这些因素的因果权重。

现有记录还没有给出一套完整标准，用来决定这项假设何时应保持、收窄或撤回。安全证明被不当地推迟、Qualification Debt 持续累积，或后续采用没有获得预期的可操作性，都足以触发重新评估；阈值和长期观察窗口仍然未知。它不能因为最终出现 PASS 就自动固化。

项目曾激活更轻量的治理安排，也没有靠这一项改变单独阻止后来 D-079 再次出现 Over-scope。这进一步削弱了“只要治理变轻，问题就会消失”的解释。

---

## 23.7 四十二项测试通过，候选仍然被拒绝

如果只看结果，D-079 很像一次反常裁决：42 项针对性测试全部通过，Human 却没有接受这个候选。

但 Human 没有推翻测试结果。[当时的测试与范围裁决记录](../Evidence/receipts/ER-20260818-003__CLM-C09-001.md) 处理的是另一个问题：通过测试的实现，是否都应该进入当前阶段的开发基线。

> **D-079｜2026 年 8 月 15 日同期范围裁决**
>
> - 候选的 42 项针对性测试（Focused Tests）全部通过；
> - Human 没有接受它进入当时的 E1 开发基线；
> - 记录认为，候选提前带入了后续阶段的数据结构镜像和更大验证范围；
> - 后续收窄修正保留了 8 个与当前接口约定相关的回归用例。
>
> *根据当时项目记录节选并译述。*

项目把当时这个低风险开发切片称为 E1。42 项测试回答的是：候选是否满足已经写入这些测试的行为断言。范围裁决回答的是：对数据结构做完整镜像（Schema Mirroring）、扩大验证表面以及相应实现，是否都属于 E1。前一个答案是通过，后一个答案是不接受。

所以，这不是“Human 无视了客观测试”。测试结果有效，候选范围仍然可以被拒绝，因为它们对应不同的判断对象。只有当项目明确把一个具名、有限的接受决定委托给测试 Gate 时，PASS 才能在该授权范围内直接形成处置；D-079 的源代码范围（Source Scope）仍需要独立的 Human 判断。

后续的收窄修正（Forward Correction）也不是在修复一个失败行为。测试原本就没有失败。它改变的是这次提交给 Human 接受的实现范围：保留 8 个与当前接口约定直接相关的回归用例，把更后阶段的实现与验证工作移出 E1。后来 F1 使用的 Source，由这次修正后的版本继续演进而来。

这次处置不能反过来证明“更小就是更好”。被移出的检查在后续 Qualification 阶段可能重新变得适当；两个版本的长期缺陷和维护成本也没有经过比较。Human 的决定只约束这个项目当时的 E1 范围。

后来的 [F1–F4a 开发与 Closure 记录](../Evidence/receipts/ER-20260818-001__CLM-OUTLINE-002.md) 提供了另一半对照。F1、F2 和 F3 不是一串通关节点；它们共同回答 F4a 结果周围的三个问题：观察的是哪份源代码（Source），只读回放（Replay）是否会反向修改它，以及这些输入、测试集合和关闭结果是否都指向同一个 Package。

F4a 记录的 `48/48 PASS` 因而不是一个脱离对象的数字：它同时绑定了具名 Source、只读 Replay、Package Identity 和限定测试集合。Development Closure 接受了这份有范围的开发 Evidence，也关闭了当前开发范围，同时明确保留 `NON_QUALIFYING`：它没有取得 Qualification、后续 Gate 或 Production Adoption 的结论。

这里真正的对照不是四十二与四十八。两组测试的分母、对象和用途并不相同，不能排成质量高低。它们迫使同一个问题变得具体：一份有效的 Test Result，究竟被允许支持哪个 Decision Target？

D-079 给出的窄结论是，当测试 Gate 没有获得范围决定的 Authority 时，PASS 只支持被测试的行为；实现是否属于当前阶段，仍是另一个决定。F1–F4a 则说明，即使开发 Evidence 获得接受，它的用途仍然可以止于 Development Closure，而不越过 Qualification 和 Production。

这也继续限制 Function-first 的含义。更轻的治理安排没有单独阻止 D-079 再次出现 Over-scope，后来的 Closure 也不能证明这条路线提高了效率、质量或安全。现有记录最多只能说明，阶段、Evidence Use 与决定对象曾被重新分开；这样做是否长期更好，仍然没有答案。

---

## 23.8 两条历史共同留下的四个分离

SP122 与 v4.94 共享来源，不能算跨项目复现。但在同一个方法生态里，它们反复迫使几类关系分开。

| 分离面 | SP122 | v4.94 |
|---|---|---|
| Scope | Current-stage visual acceptance、Sprint Closure、Supported Adoption、Production Release | E1 Source Scope、Development Closure、Qualification、Production Adoption |
| Authority | Machine Validator、Human Aesthetic Decision、Adoption / Release Authority | Verifier、Reviewer、Human Source-scope Decision、后续 Gate Authority |
| Result | Bounded Check、Visual Evidence、Human Acceptance、Open Follow-up | Verifier Failure、Target `non-result`、Test PASS、Scope Rejection、`NON_QUALIFYING` |
| Change | Candidate、Repair、Accepted Baseline、Adoption | Plan、Forward Correction、Source Freeze、Development Closure、Sustained Improvement |

这些不是四条从差到好的成熟度阶梯。

表中的 Failure、`non-result`、Test Result、Evidence Use 与 Decision Record 沿用前面章节的类型和关系；第23章没有再创造一个可以包住它们的 `Result` 上位对象。

一个 Attempt 可以产生有效的 Verifier Failure Evidence，同时没有 Target Result。一个 Candidate 可以 Test PASS，同时被 Human 拒绝范围。一次 Closure 可以接受当前 Evidence，同时保持 Qualification 和 Production 未成立。一个 Forward Correction 可以进入后续 Baseline，同时尚未证明是长期 Improvement。

同样，Plan、Manifest、Review、Transaction、Artifact Path 与 Decision Record 可以帮助后来者有限重建当时的外部决策环境，但它们不构成完整 Truth。未记录的 Human 对话、没有捕获的 Runtime State、Agent 实际忽略的 Context、环境和模型变化，以及未进入 Artifact 的失败，都可能缺失。本章只依赖可见记录，不声称能够访问 Agent 的隐藏思维过程。

追踪的合理目标，是让具名决定能够被有限复查，并清楚标出缺失条件，而不是把过去重新运行成完全相同的故事。

这些分离仍然没有形成效果比较。两条时间线很长，Artifact 也很多，材料数量却不能替代对照。

SP122 没有匹配的非 AI 或 Single-Agent UI 流程；v4.94 也没有定义清楚的 Old / New Workflow 对照。Workload、质量目标、环境、模型、Scope 和 Human Review 条件都没有被控制，失败与未完成工作的总成本也没有形成可比较数据。

因此，本章不能说：

- AI 或 Multi-Agent 提高了开发速度；
- Evidence-heavy Workflow 提高了质量或安全；
- Function-first 降低了治理成本；
- Human Control Plane 已降低认知负担；
- 可见 Lane 证明 Multi-Agent Organization 更有效；
- AI Game Dev OS 已达到某个统一 Capability Level；
- Self-Evolution 是组织或系统演化的终点。

SP122 R2 的可见 Lane 能说明 Work 怎样分配、输出怎样定位、Handoff 和 Integration 留下了什么记录。它不能说明多 Agent 比单 Agent 更快，也不能证明并行执行降低了 Human Load。组织效果仍取决于 Work 可分解性、共享状态、冲突风险、验证独立性和整合成本。

治理也不是免费的。Review Time、Agent Token、Waiting、Coordination、Artifact Maintenance、Repair、Retry、Context Reconstruction 和 Exit Cost 都会进入生产系统。D-048 同时提醒我们，控制成本不能单独成为删除控制的理由；某些严格检查确实保护了重要表面。

更合理的问题不是“治理越少越好”或“证据越多越好”，而是：当前控制保护哪条 Claim 和哪种风险，它在什么 Lifecycle Stage 生成哪种 Evidence，失败时阻断什么，谁能够例外或接管，哪条 Protected Floor 不能降低，以及代价是否与当前用途相称。

本章也不为 AI Game Dev OS 打 Level。机制存在不等于 Operational Use，治理活动不等于 Delivery Result，Test Evidence 不等于 Scope Acceptance，Development Closure 不等于 Qualification，Adoption 更不等于 Sustained Fitness。

---

## 23.9 带走问题，不复制模板

如果另一个项目想借用这段经验，最不可靠的做法是先复制 Manifest、Lane、Gate 和状态名。

更值得带走的是 Transfer Question（迁移问题：进入目标环境后必须重新回答、不能直接继承案例答案的问题）：

1. 当前 Work 与这里的 Case Episode 是否真的相似，还是只有术语相似？
2. 机器检查覆盖哪些断言，哪些体验、风险和方向仍属于 Human 判断？
3. 这份 Evidence 准备用于哪个 Decision Target，Authority 是否真的授权了这种映射？
4. Verifier 失败时，Target 实际被观察了吗？
5. Acceptance、Closure、Adoption、Qualification 与 Production 是否被一个模糊状态压在一起？
6. 失败后能否恢复，是否存在不可逆的数据、安全或外部影响？
7. Governance Artifact 的维护与等待成本由谁承担，保护的风险是否仍然存在？
8. 游戏案例没有覆盖的法律、隐私、组织和安全边界，在目标环境里会改变什么？

相似的 Work、Risk、Decision 与 Failure Surface，才可能形成有限迁移。相似的命名不够。

本章的 Case-specific Fact 仍然属于 PlayerStatus、Godot Runtime、SP122、v4.93 R2，以及 v4.94 的具名开发事件。它们不能直接升级成“适用于所有企业”的结论。公开项目案例可以在前面章节承担先例、反例或机制比较，但这里不再加入一个平行案例为 AI Game Dev OS 背书；第23章要做的是把未解决的问题交还给目标环境。

---

## 23.10 写书可以影响 OS，但不能替 OS 作决定

写作确实会反向整理 AI Game Dev OS 的问题。

例如，这两段历史会让人考虑：是否需要更明确的 Decision Target、是否应分开 Verifier Integrity 与 Target Result、是否要在 Closure 中保存 Explicit Non-claim、是否值得观察 Governance Cost。

这些都只能先成为 Change Candidate。

```text
observed case problem
→ scoped retrospective inference
→ OS change candidate
→ intended objective and protected floor
→ evidence and counterevidence plan
→ Human Decision
→ separate implementation request
→ adoption observation
```

书内推导没有外部仓库的修改 Authority。一个建议写得再完整，也不能跳过目标系统自己的 Intent、Evidence、风险和 Human Decision。否则，本章刚刚批评完“理论概念映射成 OS 功能”的循环，就会用写作结果直接制造下一轮循环。

---

## 23.11 结语：案例的任务是保留“不相等”

AI Game Dev OS 与 lessismore 没有给这本书提供一个最终验证场景。

它们留下的是几组很难再伪装成成功故事的关系。SP122 的机器结果没有替 Human 完成视觉判断，当前阶段 Closure 也没有顺带打开 Adoption 和 Production；v4.94 则保存了观察者失败、范围拒绝与非资格化 Closure。把两条时间线并在一起，三个尤其容易被误读的断点是：

```text
18/18 PASS       ≠ Human aesthetic acceptance
verifier failure ≠ target failure
48/48 PASS       ≠ qualification
```

如果最后又把这些关系压回一个 `completed`，两段历史就会再次失去作用。

这两条时间线也修正了本书早期一个过于顺滑的判断：AI 提高局部生成速度以后，软件工程的瓶颈并不会必然、同时、永久地转向 Intent、Context、Truth、Verification、Cognition、Governance、Memory 或 Traceability。

更准确的条件命题是：当 AI 扩大的提案与执行能力持续超过现有的意图形成、状态维护、验证、Human Decision、集成或恢复能力时，约束可能从局部产出转向这些控制关系。具体 Bottleneck 仍要在具名 Workload、风险面和时间窗口里观察。

有些项目的主要限制依然可能是预算、技能、数据、部署、市场或产品方向。同一个系统也可能同时有多个约束，而不是排队等待一个“下一瓶颈”。

本书最终要保留的，不是最大化 AI 替代，也不是最大化治理表面。

它保留的是一种更具体的工程选择：在可观察、可干预、可恢复并由具名 Authority 裁决的边界内使用受托智能执行，同时让 Human 继续主导方向、价值、体验、风险与责任。

这是我从这两段历史中保留下来的当前建议。

它不是两个相关仓库替我证明的经验定律。
