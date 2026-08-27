# 第11章 Cognitive Overload
## 当需要判断的变化超过合格审阅容量

> 工作稿状态：首轮逻辑修订稿，不替代 [全书大纲](../OringinalDocs/beyond_code_ai_native_software_engineering_outline_zh.md) 或 [Cognitive Control、Trust 与 Human Control Plane v0.1](../OringinalDocs/ai_native_cognitive_control_trust_human_control_plane_v0.1.md)。
> 回接说明：[RR-022](../RevisedResult/RR-022_第11章Cognitive_Overload首轮回接说明.md)。
> 适用边界：本章把 Cognitive Overload 写成“在相关决策时间窗内，判断需求持续超过合格审阅容量”的条件风险；AI Game Dev OS v4.94 与 lessismore SP122 只提供局部案例，不证明 AI 必然造成认知过载，也不证明 Human Control Plane 或里程碑审阅普遍更优。

上一章讨论 Review Engineering（审阅工程）：在执行前、执行中和执行后，怎样根据风险、影响、可逆性和 Evidence 调整 Review 强度。

但 Review Budget 暗含一个前提：

> 项目拥有足够的合格审阅能力，能够在需要作出决定的时间窗口内处理真正重要的变化。

这个前提并不总是成立。

AI 可以扩大代码、测试、文档、规则和工作流的生成能力，也可以扩大搜索、分析和验证能力。与此同时，项目规模、并行任务、历史状态、治理对象和外部依赖也会继续增长。

因此，本章不从“AI 一定比人快”直接推出“人必然失控”。它讨论一个更窄、也更可检查的问题：

> **当需要人类判断的、被保留的变化持续超过可用的合格审阅容量时，项目会出现什么认知风险？又可以通过哪些不同路径响应？**

这两个问题必须拆开。

诊断出带宽失配，不会自动证明 Human Control Plane 是唯一方案；减少在制工作、缩小变更、扩充审阅能力、加强确定性验证、按风险选择直接审阅范围，也都可能是更合适的答案。

---

# 11.1 Cognitive Overload 是一种条件，不是一句时代口号

本书所说的 **Cognitive Overload（认知过载：当前需要理解和判断的工程变化，超过团队在给定时间与风险条件下形成足够可靠判断的能力）**，不是简单的“信息很多”。

它至少包含三个限定。

第一，必须存在实际的判断需求。

一万个自动生成但未被采用的候选文件，可能只构成存储与筛选成本；一个涉及不可逆数据迁移的十行修改，却可能要求高强度人工判断。对象数量不是判断负担的充分代理。

第二，失配必须发生在相关时间窗口内。

短时突发不一定形成持续问题。项目可以暂停新工作、延长 Review、引入专项专家或缩小 Release Scope。只有当变化到达率长期高于可用处理能力，或者决定必须在能力恢复前作出，认知过载才成为结构性风险。

第三，所谓“理解”必须绑定当前决策。

团队通常不需要记住每一行实现，也从未真正理解所有编译器、依赖库和运行平台内部细节。工程上需要的是：

> 对当前 Claim、风险和责任足够的 Decision-sufficient Understanding（决策充分理解）。

因此，不能直接使用下面的口号作为已验证事实：

~~~text
AI Output
    >
Human Capacity
~~~

更有意义的条件式表达是：

~~~text
Judgment-bearing retained change arrival
                    >
Available qualified review capacity
over the relevant decision window
~~~

这里的两边都不是固定常数，也不应被压成一个未经校准的统一分数。

---

# 11.2 先区分五种不同的“吞吐”

“AI 生成得更快”容易把不同对象混在一起。至少应区分以下五种吞吐。

| 对象 | 回答的问题 | 不能自动推出什么 |
|---|---|---|
| Gross Output Throughput | 系统一共生成了多少候选输出 | 有多少被采用或需要人工判断 |
| Retained Change Throughput | 有多少变化进入了当前工作树、Baseline 或运行环境 | 这些变化都正确、必要或高风险 |
| Machine-checked Throughput | 有多少变化经过具名自动检查 | 自动检查覆盖了所有相关 Claim |
| Judgment-bearing Throughput | 有多少变化仍需要产品、架构、安全、体验或责任判断 | 每个判断具有相同难度和风险 |
| Qualified Review Capacity | 团队在当前时间窗内能完成多少与 Claim 和风险匹配的审阅 | 人类容量永远固定不变 |

生成能力可能同时提高 Gross Output 和 Machine-checked Throughput。

更好的工具、模块化、影响分析、测试生成和摘要，也可能提高 Qualified Review Capacity。相反，大范围修改、共享状态、过度治理、文档债和不清晰的 Authority 会降低有效审阅能力。

所以，真正需要观察的不是：

> AI 生成了多少？

而是：

> 经过筛选、验证和风险分流后，还有多少被保留的变化需要哪一种人类判断？这些判断能否在失效前完成？

---

# 11.3 Review 不等于阅读全部内容

第10章拥有 Review、Review Target、Finding、Review Budget、Review Independence 与 Review Disposition 的正式定义。本章只讨论这些对象对人类判断容量的消耗。阅读是 Review 的一种输入活动，不是 Review 的完整定义。

一次合格审阅可能包含：

1. 确认当前 Review Target 与 Intended Decision Use；
2. 理解 Intent、Scope 与 Non-goal；
3. 识别实际发生的 Change；
4. 检查与目标 Claim 匹配的 Evidence；
5. 判断风险、替代方案和未知；
6. 确认 Authority 与 Intended Use；
7. 形成 Finding 与 Disposition Recommendation；只有同时持有相应 Authority Grant 的主体，才可通过 Decision Record 作出 Review Disposition；
8. 保留必要的下钻、接管和恢复能力。

不同任务对直接阅读的要求并不相同。

## 低风险、局部、可逆的变化

可能主要依赖：

- 小范围 Diff；
- 确定性检查；
- focused tests；
- 自动影响分析；
- 抽样审阅；
- 明确的 Rollback。

## 高风险或高主观性的变化

可能仍需要：

- 逐行代码审阅；
- 安全边界检查；
- 数据迁移演练；
- 架构判断；
- 产品体验评审；
- 创意与审美裁决；
- 独立专家复核。

因此，“人不应阅读一切”不能被改写成“人不再阅读实现”。

更准确的原则是：

> **直接检查的深度与范围，应由 Claim、Risk、Reversibility、Evidence Coverage 和 Human Authority 决定。**

同样，Review 也不要求 Reviewer 在脑中保存整个系统的完整镜像。一个复杂系统更现实的控制方式，是让人能够重建当前决策所需的局部模型，并知道如何继续下钻。

---

# 11.4 五类 Overload 是诊断视角，不是成熟分类学

认知过载可以从五个互相重叠的视角观察。

它们不是已经通过跨项目研究验证的固定分类，也不是五个互斥状态。它们的作用是帮助团队定位负担发生在哪个界面。

## 11.4.1 Output Overload（输出过载）

系统生成或暴露的对象太多：

~~~text
Code
Tests
Rules
Documents
Plans
Reports
Evidence
Logs
Assets
Configuration
~~~

常见症状包括：

- Review Queue 持续增长；
- 同类文档和报告重复；
- Reviewer 只读摘要，不再检查来源；
- 低价值变化与高风险变化争夺同一注意力；
- 大量候选从未被明确采用或撤销。

Output Overload 只说明入口或展示面过大，不说明所有输出都有同等价值。它的第一响应通常是筛选、去重、限流和缩小 Scope，而不是建设更大的 Dashboard。

## 11.4.2 State Overload（状态过载）

团队无法快速回答当前系统处于什么状态：

- 哪些规则仍有效；
- 哪个 Workflow 版本正在使用；
- 哪个 Baseline 已被接受；
- 哪些 Assumption 仍未验证；
- 哪些 Capability 获得了什么 Authority；
- 哪些 Evidence 已过期；
- 当前 Worktree、Runtime 与已发布状态是否一致。

State Overload 不是单纯记忆力不足。它往往意味着状态被复制在多个表面、缺乏版本身份、更新责任不清，或历史与当前状态混在一起。

增加更多状态摘要可能暂时减轻查找成本，也可能制造新的竞争性状态源。第6章讨论的 Source、Version、Scope、Freshness 和 Conflict 边界，在这里成为认知控制的前提。

## 11.4.3 Dependency Overload（依赖过载）

一个局部变化的影响需要跨多个系统推导：

~~~text
Intent / Policy
       ↓
Workflow
       ↓
Agent / Skill / Tool
       ↓
Product Change
       ↓
Runtime / User Experience
       ↓
Evidence / Decision
~~~

当依赖关系隐含、动态或跨 Repository 时，人很难持续维护完整因果图。

Dependency Overload 的风险不是“人没有背下所有依赖”，而是：

- 关键影响路径没有被识别；
- Reviewer 不知道还应检查哪个系统；
- 一项局部成功被误当成端到端成功；
- 变化经过多个中间层后失去 Intent 与 Authority 绑定；
- 恢复动作只覆盖了表面结果，没有覆盖下游状态。

更小的组件、更明确的 Contract、影响分析和可追踪引用可以降低这种负担。把所有依赖复制进一个超级 Manifest 通常只会改变负担的位置。

## 11.4.4 Judgment Overload（判断过载）

真正稀缺的往往不是阅读时间，而是高质量判断：

~~~text
这个变化是否必要？
当前 Scope 是否合理？
这项 Evidence 足以支持什么决定？
安全边界是否需要更严格？
体验取舍是否符合产品方向？
继续迭代、回退还是停止？
~~~

Judgment Overload 发生在大量变化都无法仅靠确定性规则完成处置时。

它不等于“Human Judgment Capacity 恒定”。团队可以通过培训、工具、分工、专家参与和更好的信息接口提高能力。但涉及价值、责任、风险接受和创意方向的判断，不会仅因生成成本下降而自动消失。

## 11.4.5 Meta-level Overload（元层过载）

项目不仅需要判断 Product Change，还要判断生产系统本身：

- Agent Contract 是否合理；
- Workflow 是否仍适合当前阶段；
- Gate 是否保护真实风险；
- Validator 是否观察了正确对象；
- Memory 是否放大了过期结论；
- Governance 是否正在增加证明对象而不增加交付 Evidence；
- Self-evolution 是否把一次局部成功推广成一般规则。

Governance Overload（治理过载）属于这一视角。

更多 Gate、Review、Manifest 和 Evidence Request 不一定带来更多理解。它们也会生成新的状态、依赖和判断对象。

因此：

> **治理成本本身必须进入 Cognitive Load Budget，而不能被假设为免费的安全增量。**

---

# 11.5 带宽失配不只有一个原因

AI 生成速度是可能原因之一，但不是唯一原因，也不是所有项目中的主要原因。

| 可能来源 | 它怎样形成负担 | 可替代解释或检查 |
|---|---|---|
| 生成候选过多 | Gross Output 增长快于筛选 | 实际被保留的比例是多少 |
| Change Scope 过大 | 单次判断需要重建过多上下文 | 是否可以拆分并保持端到端意义 |
| 并行任务过多 | 多条状态和决策链同时等待处理 | WIP 是否超过团队协作能力 |
| 模块耦合 | 局部变化具有广泛不确定影响 | Contract 和影响分析是否缺失 |
| 状态表面重复 | Reviewer 无法确定当前有效记录 | 是否存在竞争性 Source |
| Evidence 与 Claim 不匹配 | 材料很多，但不能回答当前问题 | Intended Use 是否明确 |
| 治理对象膨胀 | Review 转向审阅未来证明义务 | 当前危险或交付 Claim 是什么 |
| Reviewer 能力不足 | 专业知识、时间或 Authority 不够 | 是否需要专家、培训或重新分工 |
| 文档与历史债 | 每次判断都要重建背景 | 当前状态与历史是否分层 |
| 工具接口不良 | 关键差异和风险难以下钻 | 是信息缺失还是展示方式错误 |

这些来源可能同时存在。

如果问题主要是 WIP 失控，建立 HCP 不会替代限流。

如果问题主要是模块耦合，摘要不会替代架构修复。

如果问题主要是 Evidence 不匹配，增加更多日志不会产生更好的判断。

如果问题主要是缺少安全专家，自动压缩也不会生成所需 Authority。

诊断必须先于方案命名。

---

# 11.6 Review Fatigue 会改变处置质量

**Review Fatigue（审阅疲劳：持续审阅压力下注意力、辨别力和风险敏感度下降的状态）**，不应只通过“Review 数量多”推断。

它可能表现为：

- 批准速度越来越快，但返工与例外增加；
- Reviewer 对相似警告逐渐失去反应；
- 大多数处置只复述 Agent Summary；
- 重要限制被固定模板掩盖；
- 大变更因“已经投入很多”而更容易被接受；
- Reviewer 很少再提出替代方案或 Scope 收窄；
- Independent Review 逐渐变成格式确认。

这些信号仍然可能有其他解释，例如任务变简单、自动化证据变强或团队更熟练。因此，不能把 Review 时间缩短自动解释为疲劳，也不能把 Review 时间变长自动解释为质量提高。

更可靠的观察需要同时考虑：

~~~text
review latency
decision reversals
escaped incidents
rework
scope corrections
evidence drill-down rate
high-risk finding rate
reviewer disagreement
~~~

这些都是候选观测，不是统一评分公式。

Automation Bias（自动化偏见）同样需要具体化。问题不是“人相信 AI”本身，而是：

- Reviewer 不知道摘要由谁、基于哪些 Source 生成；
- Builder 与 Reviewer 共享同一错误假设；
- 机器 PASS 被用于它没有 Authority 的 Decision；
- 没有保留反证、未知和下钻路径；
- 低告警率来自 Detector 缺失或失效。

---

# 11.7 Cognitive Debt 不是“没有读过的所有内容”

本书将 **Cognitive Debt（认知债：已经进入当前系统、但其理由、影响或约束尚未被团队吸收到足以支持预期决策的变化）** 与一般信息缺口区分。

不是每一段未被人工阅读的代码都形成认知债。

编译器输出、成熟依赖和低风险生成代码可以通过 Contract、测试、版本与替换边界被控制。认知债更关心：

- 变化已经被接受或进入运行；
- 未来存在可预见的维护、风险或责任决策；
- 团队缺少作出该类决策所需的解释、Evidence 或 Owner；
- 现有摘要无法可靠地下钻到来源；
- 关键 Assumption 与限制没有被保存。

## 与相邻问题的区别

| 问题 | 核心问题 | 典型后果 |
|---|---|---|
| Technical Debt | 实现和架构选择增加未来修改成本 | 脆弱、重复、难以扩展 |
| Cognitive Debt | 团队无法重建未来决策所需的模型 | 误判、接管困难、过度依赖原执行者 |
| State Management Gap（状态管理缺口） | 当前状态缺少可靠身份、更新和冲突规则 | 恢复错误、使用过期记录 |
| Evidence Gap（证据缺口） | 重要 Claim 缺少与用途匹配的可检查依据 | 无法验证、无法作出有边界处置 |

这些问题可能互相放大，但不应被合并成一个“认知债”总称。

## 认知债怎样积累

~~~text
Change accepted
→ rationale not retained
→ impact and assumptions remain implicit
→ original context disappears
→ next maintainer reconstructs from fragments
→ uncertainty and review cost increase
~~~

## 认知债怎样偿还

偿还不等于补写所有文档。更有效的方式可能是：

- 收窄当前 Claim；
- 删除不再需要的对象；
- 将历史与当前状态分层；
- 补充 Decision、Assumption 与 Evidence 引用；
- 建立可复现的验证路径；
- 指定 Owner 和接管边界；
- 重构高耦合实现；
- 把无法维持的 Capability 降级或撤销。

文档只有在改善未来判断时才是在偿还认知债。重复描述同一状态可能继续增加它。

---

# 11.8 Ownership Erosion 不是“不知道每一行代码”

**Ownership Erosion（所有权侵蚀：有责任的团队逐渐失去解释、判断、改变和接管系统的实际能力）**，比“没有亲自编写实现”更具体。

一个团队即使没有阅读所有依赖内部实现，也可能仍然拥有系统，因为它能够：

- 说明系统的目标和关键约束；
- 定位当前 State Claim 与 Source；
- 判断 Evidence 支持什么、不支持什么；
- 找到重要 Decision 与 Authority；
- 识别高风险 Capability；
- 暂停、拒绝或收窄变化；
- 在失败时隔离、回退或前向恢复；
- 更换 Agent、模型、工具或 Workflow；
- 在原执行者离开后继续维护。

相反，如果团队只能重复“测试都通过了”或“Agent 说完成了”，却不能说明测试覆盖的 Claim、当前运行身份、风险和恢复路径，那么即使代码仍在自己的 Repository 中，也可能已经发生实际所有权侵蚀。

控制方式不应被排成单向成熟阶梯。

~~~text
Direct implementation inspection
Component and contract review
System behavior and evidence review
Governance and authority review
~~~

这些方式可以同时存在。

安全关键代码可能需要逐行检查；低风险生成资产可能主要依赖抽样和体验评审；长期受托 Workflow 还需要治理与接管能力。更高层控制不会自动取代更低层控制。

---

# 11.9 案例只提供局部负荷信号

[认知负担案例记录](../Evidence/receipts/ER-20260824-001__CLM-C11-001.md)保存了事实、同期判断、替代解释与限制；完整事件顺序见[第23章](第23章_AI_Game_Dev_OS纵向案例_首轮修订稿.md)。本章只使用三条关系：被检查的 v4.94 package 有 `2377` 个 tracked files；D-073 至 D-075 增加治理与审阅 Artifact，却没有同步产生 Source、Runtime、Test 或 Qualification 进展；SP122 仍由 Human 直接检查一条有边界的 Evidence Chain 后再作处置。

同期 Human Judgment 记录了审阅与理解吞吐没有随生成吞吐扩展，并出现实现级控制感下降；这是作者当时的经验判断，不是由文件数测得的 Observable Fact。

这些观察允许提出一个有范围的推导：在该项目阶段，更多可审阅对象没有自动保持有效控制，Review Attention 可能从当前行为与交付 Evidence 转向未来证明义务。因此 Review Unit、Timing 与 Target 需要被明确选择。

它们不能把文件数换算成 Human Judgment Load，不能证明 AI 速度是 Governance Livelock 的唯一原因，也不能证明 Milestone Review 或 Human Control Plane 普遍更优。SP122 反而保留了重要 Counterevidence：直接、实质的 Human Review 仍可能必要且可行。

---

# 11.10 怎样诊断是否真的存在带宽失配

项目不应因为“感觉内容很多”就宣布发生结构性 Cognitive Overload。

可以依次回答六组问题。

## 1. 决策窗口是什么

- 当前判断必须在何时完成？
- 延迟会造成什么损失？
- 能否安全暂停新工作？
- 是短时 Incident，还是长期运行模式？

## 2. 哪些变化真正被保留

- 候选输出中有多少进入 Worktree、Baseline、Release 或 Runtime？
- 哪些只是临时探索？
- 哪些已经被丢弃、替代或隔离？
- 是否存在大量无人拥有的中间对象？

## 3. 哪些变化需要 Human Judgment

- 哪些 Claim 可以由确定性验证回答？
- 哪些涉及产品方向、风险接受、创意、责任或 Authority？
- 哪些只是需要更好的自动影响分析？
- 当前是否错误地把所有变化都路由给 Human？

## 4. 合格审阅容量是多少

- 需要哪一种专业能力？
- Reviewer 是否拥有作出处置的 Authority？
- Review 所需 Source、Evidence 和工具是否可用？
- AI 或自动化能否提高审阅能力，而不只是生成更多材料？

## 5. 已经出现了什么后果

- Review Backlog 是否持续增长？
- 高风险决定是否老化或被绕过？
- 是否出现机械批准、反复返工、Scope Correction 或事故逃逸？
- 原执行者离开后是否无法接管？
- 是否只能依赖无法下钻的摘要？

## 6. 有哪些替代解释

- WIP、并行 Agent 或 Change Scope 是否失控？
- 架构耦合是否让每次变化影响过广？
- 是否存在状态复制、文档债或 Governance Overload？
- Evidence 是否回答了错误的 Claim？
- Reviewer 短缺是否只是暂时资源问题？

只有把这些问题绑定到一个具体时间窗和风险面，团队才有理由决定使用哪一种响应。

---

# 11.11 响应路径一：减少进入系统的变化

最直接的响应不是压缩更多信息，而是减少同时进入判断面的工作。

**Work in Progress（在制工作：在观察窗口内仍有开放 Work 或 Attempt 关系、持续占用生产或判断容量的工作集合）** 可以通过以下方式限制。它是容量观察口径，不重新定义第7章的 Work，也不以某一种 Acceptance 或 Review Disposition 代替 Work Closure：

- 限制并行 Agent 或并行 Task；
- 为高影响变化设置更小 Scope；
- 在 Review Backlog 超过阈值时暂停新 Candidate；
- 区分 Exploration 与 Production；
- 删除重复 Report、Manifest 和 Gate；
- 对未被采用的 Candidate 设置过期与清理规则；
- 先完成一个 end-to-end slice，再扩展相邻范围。

这条路径的成本是降低表面产出速度，也可能延迟探索。

它的价值在于：如果根因是到达率过高，限流直接作用于根因；任何 Dashboard 或 Brief 都不能替代它。

---

# 11.12 响应路径二：缩小判断单元与依赖面

当每次变化需要重建过大的上下文时，可以改变 Change Unit：

- 拆分可独立验证的垂直切片；
- 明确 Contract 与 Non-goal；
- 隔离实验性 Capability；
- 将历史材料移出活跃状态面；
- 减少共享可变状态；
- 为跨 Repository 影响提供显式引用；
- 把大规模迁移拆成可观察阶段。

拆分不能只追求更小 Diff。

一个过小的 slice 可能失去端到端意义，导致每一步都通过、整体仍不可用；它也可能制造过多 Handoff、Review 和 Governance 对象。

合适的判断单元需要同时满足：

~~~text
small enough to understand
large enough to carry a meaningful Claim
bounded enough to verify
recoverable enough to stop
~~~

---

# 11.13 响应路径三：扩充合格审阅能力

Human Capacity 不是完全固定的。

项目可以通过以下方式提高 Qualified Review Capacity：

- 引入领域专家或第二 Reviewer；
- 让 Reviewer 获得可复现环境；
- 改善 Diff、Impact Analysis 和 Source Linking；
- 训练团队理解新的 Production Intelligence System；
- 把 Review 职责按产品、架构、安全、体验和发布拆分；
- 让 AI 帮助定位差异、生成反例和检查遗漏；
- 将重复的确定性检查自动化；
- 为重要模式建立可复用 Review Checklist。

但“增加 Reviewer”也有协调成本。

更多人可能增加 Handoff、冲突与等待；AI Reviewer 也可能与 Builder 共享同一错误上下文。扩容只有在增加独立判断能力，而不是重复生成同类总结时才有效。

---

# 11.14 响应路径四：把可形式化判断交给机器

部分 Review 负担来自重复检查：

- Schema 是否有效；
- Build 是否通过；
- Diff 是否越界；
- Inventory 是否发生未授权变化；
- Regression 是否出现；
- Contract 字段是否缺失；
- Artifact 是否绑定正确版本。

这些问题适合进入自动验证。

但自动化必须保留三个边界：

1. Validator 实际观察了什么；
2. Evidence 支持哪个 Claim 和 Scope；
3. PASS 被授权用于哪个 Decision。

Test PASS 不自动证明：

- 当前 Scope 必要；
- 设计选择合理；
- 用户体验可接受；
- 风险可以接受；
- Candidate 应被采用、发布或推广。

自动化减少的是一部分可形式化判断，不是把所有责任转成机器结论。

---

# 11.15 响应路径五：按风险选择直接审阅与信息压缩

当全量直接审阅既不必要也不可持续时，可以按风险路由 Review。

## 仍应优先直接检查的对象

- 安全与权限边界；
- 不可逆数据变化；
- 外部发布和真实用户影响；
- 关键架构 Contract；
- 训练数据、Memory 或长期规则污染；
- 高主观性的创意与体验变化；
- Detector、Validator 和 Recovery 机制本身。

## 可以更多依赖压缩、抽样或委托的对象

- 低风险、局部、可逆变化；
- 成熟 Contract 内的重复操作；
- 已有强确定性验证的机械修改；
- 可快速回退且影响隔离的实验；
- 大量同质生成物中的统计或抽样检查。

信息压缩必须保留：

~~~text
Decision Target
Change Scope
Risk and Impact
Evidence and Limitations
Unknowns and Counterevidence
Authority
Drill-down
Stop / Recovery
~~~

压缩不等于证明。

它可能减少阅读量，也可能遗漏共同模式故障。第12章将讨论 Progressive Disclosure 与 Human Decision Interface，并解释压缩怎样保持 Source、Coverage 和 Unknown，而不建立新的 Truth Store。

---

# 11.16 响应路径六：停止、重定基线或恢复

有些认知负担不能在原路径上继续消化。

当以下情况出现时，停止可能比继续总结更合理：

- 高风险决定长期无人拥有；
- 当前 Baseline 身份不清；
- Evidence 无法绑定实际运行对象；
- Change Scope 已超出可审阅范围；
- Validator 或 Detector 本身失去可信运行条件；
- Review Backlog 持续增长且新变化仍在进入；
- 团队无法说明怎样隔离或恢复。

可能的动作包括：

- Freeze 新工作；
- 收窄当前 Claim；
- 撤销或降低 Delegation；
- 回到仍安全适用的 accepted Baseline；
- 建立新的 forward-recovery Baseline；
- 隔离不可理解的 Capability；
- 重新收集与当前 Decision 匹配的 Evidence。

这里的目标不是惩罚生产速度，而是恢复可判断性。

---

# 11.17 Cognitive Load Budget 不是一个统一分数

**Cognitive Load Budget（认知负载预算：在给定风险和时间窗口内，对并行工作、未决判断、审阅延迟与信息表面设置的局部约束）**，可以帮助项目在失配前采取动作。

它不应被实现成全项目统一的“认知分数”。

一个任务或阶段可以声明：

~~~yaml
decision_window: release-candidate
scope: save-migration

max_concurrent_high_risk_tasks: 1
max_unresolved_high_risk_decisions: 2
max_review_age_hours: 24

direct_inspection_required_for:
  - irreversible_data_change
  - authority_boundary

machine_verification_allowed_for:
  - schema_conformance
  - bounded_regression

compression_requirements:
  - source_links
  - evidence_scope
  - unknowns
  - recovery_path

over_budget_actions:
  - freeze_new_candidates
  - reduce_scope
  - request_qualified_reviewer
~~~

字段只是设计示例，不是通用 Schema。

预算的阈值应来自具体风险、团队能力和历史观察。它还必须与质量和安全反指标一起看，否则团队可能通过隐藏问题、减少告警或把判断错误地委托给机器来“降低负载”。

---

# 11.18 人类角色迁移不是退出 Loop

AI-native 系统中的人类角色可能从亲自完成更多实现，转向：

- 定义 Intent 和边界；
- 选择哪些判断可以委托；
- 维护产品、架构和创意方向；
- 处理高风险例外；
- 裁决 Scope、Acceptance、Adoption 和 Release；
- 审查生产系统本身；
- 在失败时停止和接管。

这有时被称为 **Human-on-the-loop（人在监督与干预回路上，而不是每一步执行路径中）**。

这个表述只有在以下条件存在时才有意义：

- Human 能看到与决定匹配的 Evidence；
- Authority 与 Delegation 可识别；
- 异常与未知不会被摘要静默隐藏；
- 人可以下钻、质疑、否决和接管；
- Stop 与 Recovery 路径真实可用；
- 高风险领域仍保留必要的直接 Review。

如果人只看到 `SYSTEM STABLE`，却不知道 Observation Coverage、Detector Health 和 Source Freshness，那么 Human-on-the-loop 只是责任保留，控制能力并未保留。

---

# 11.19 与相邻及后续章节的边界

本章只回答两个问题：

1. 何时可以有边界地判断认知带宽发生失配；
2. 有哪些不同类别的响应可以选择。

它不在本章定义完整解决方案。

| 章节 | 承接问题 |
|---|---|
| 第10章 Review Engineering | Review Target、Finding、Review Budget、Independence 与有权 Review Disposition 如何成立；本章只使用这些对象估算判断负荷 |
| 第12章 Cognitive Compression | 怎样把执行结果变成人可判断、可下钻的信息，而不是隐藏风险 |
| 第13章 Governed Autonomy | 哪些动作可以被委托，Authority 怎样撤回，Human 怎样接管 |
| 第14章 Observability and Intervention | Coverage、Freshness、Detector Health、Exception 与 Intervention 怎样暴露 |
| 第15章 Memory Engineering | 连续性怎样保存，同时避免过期结论放大认知错误 |
| 第16章 Self-Evolution Engineering | Workflow 与生产系统变化怎样作为 Candidate 被校准，而不是自动成为 Improvement |

Human Control Plane 只是第12–14章可能采用的接口组织概念，不是本章诊断的逻辑结论。

---

# 11.20 本章原则

1. **先观察被保留、需要判断的变化。** Gross Output 不是 Human Judgment Load。
2. **把带宽失配写成条件命题。** 不把 AI 速度、项目规模或人类容量写成固定常数。
3. **Review 不等于阅读一切。** 直接检查范围由 Claim、Risk、Evidence 和 Authority 决定。
4. **五类 Overload 是诊断视角。** 不把它们写成互斥状态或已验证分类学。
5. **治理也消耗认知预算。** 更多 Gate 和 Artifact 不自动产生更多理解。
6. **诊断与响应分开。** 失配可以通过限流、拆分、扩容、验证、风险路由或恢复处理。
7. **压缩不能替代来源和下钻。** 更短的信息不自动更可信。
8. **Cognitive Debt 绑定未来决策。** 不是所有未阅读实现都形成债务。
9. **Ownership 是实际控制能力。** 不以是否亲自编写每一行判断所有权。
10. **单项目案例保持单项目边界。** v4.94 不证明普遍因果或唯一架构。

---

# 11.21 常见反模式

- 用文件数、Token 数或 Agent Task 数直接代表认知负担；
- 假设所有生成内容都会被保留并需要人工阅读；
- 把 Human Review Capacity 写成恒定值；
- 把 Review 等同于逐行阅读；
- 看到 Review Backlog 就立即建设 Dashboard；
- 用更多 Governance Artifact 治理 Governance Overload；
- 用摘要长度或告警数量衡量控制质量；
- 把低告警率解释为系统健康；
- 用 AI Reviewer 为 AI Builder 自动背书；
- 认为更高层控制可以取消安全关键实现审阅；
- 将 Cognitive Debt 定义为所有人没有读过的代码；
- 把 Human-on-the-loop 当作减少 Human Authority 的委婉表达；
- 从 v4.94 一个案例推出所有 AI-native 项目的一般规律。

---

# 11.22 本章检查清单

## 判断是否存在失配

- 当前 Decision Window 是什么？
- 生成输出中有多少真正被保留？
- 哪些变化仍需要 Human Judgment？
- 这些判断需要什么专业能力和 Authority？
- Review Backlog 是短时突发还是持续增长？
- 已经出现哪些返工、漏检、Scope Correction 或接管困难？
- 是否检查了 WIP、耦合、状态复制、治理膨胀和 Reviewer 短缺等替代解释？

## 选择响应

- 能否先停止或减少新 Candidate？
- 能否缩小 Change Unit，同时保持有意义的端到端 Claim？
- 能否增加真正独立、合格的审阅能力？
- 哪些判断可以被确定性验证？
- 哪些对象必须直接检查？
- 信息压缩是否保留 Source、Scope、Unknown 和 Drill-down？
- Baseline 是否清楚、仍安全且可以恢复？
- Governance 成本是否被计入预算？

## 防止所有权侵蚀

- 团队能否说明当前目标和关键约束？
- 能否定位 State Claim、Evidence 与 Decision？
- 能否区分 Test PASS、Acceptance、Adoption 和 Release？
- 能否暂停、否决、降级和接管？
- 原执行 Agent 或成员离开后，另一个合格角色能否继续？
- 关键高风险范围是否仍保留必要的直接 Review？

---

# 11.23 本章结论

AI 可以显著提高生成和执行能力，但认知过载不是由“AI 更快”自动推出的时代定律。

更准确的工程问题是：

> 在一个具体时间窗口中，需要人类判断的被保留变化，是否持续超过了可用的合格审阅容量？

如果答案是肯定的，项目需要恢复平衡。可选路径包括：

~~~text
reduce incoming work
reduce scope and coupling
increase qualified review capacity
automate claim-specific verification
route review by risk
compress with drill-down
stop, rebaseline or recover
~~~

这些路径可以组合，也有各自成本。

本章最重要的结论不是“人不再看代码”，而是：

> **人类的直接注意力应被配置到最需要判断、责任和不可替代经验的地方；系统必须让这种选择可见、可验证、可撤回。**

下一章将继续讨论一个更危险的问题：当系统试图压缩复杂度时，怎样避免把不确定性、反证和观测盲区一起压掉。
