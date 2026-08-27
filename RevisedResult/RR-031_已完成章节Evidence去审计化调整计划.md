# RR-031：已完成章节 Evidence 去审计化调整计划

- 计划日期：2026-08-25
- 计划状态：`proposed / unreviewed`
- 调整对象：`OptimizedDocs/` 已完成工作稿、Evidence 写作规则及其索引
- 原稿边界：不修改 `OringinalDocs/`
- Evidence 边界：不删除 Receipt，不重写历史 Claim，不虚构 Human Disposition
- 本轮性质：调整计划，不执行章节改稿

## 1. 结论

已完成章节不需要因 Evidence 方法过严而整体重写。

需要做的是一次范围受控的 **Narrative De-auditing（正文去审计化：把研究和治理所需的状态元数据移出读者叙事，同时保留事实来源、适用边界和反例）**。

本次调整解决两个不同问题：

1. 已有工作稿中，部分 `Receipt ID / partial / unreviewed / unsupported / hold` 状态已经进入读者正文；
2. 当前写作规则容易把纯理论模型也送入正式 Evidence Receipt，形成过早形式化和 Meta-work。

调整后仍保留三层工作面：

~~~text
OringinalDocs
  author source material

OptimizedDocs
  reader-facing argument and working prose

RevisedResult + Evidence
  editorial decisions, receipts, claim status and audit detail
~~~

正文可以引用外部来源和案例，但不展示内部 Evidence Workflow 的实时状态。

## 2. 目标

### 必须达到

- 理论、案例事实、事后推导和当前建议仍然可区分；
- Reader-facing Chapter 不再依赖 `partial / unreviewed / narrow` 等内部状态才能被理解；
- 第17章不再把缺少效果实验误写成理论模型没有提出资格；
- 第19章不再在正文重复三份 Receipt 的 Coverage Assessment；
- Security、Privacy、IP、历史事实和跨项目推广仍保留必要来源与限定；
- Evidence Receipt、Claim Ledger 和 RevisedResult 继续保存完整研究依据；
- 后续章节只有满足明确 Trigger 时才建立正式 Receipt。

### 不属于本计划

- 不重新设计全书大纲；
- 不删除既有核心概念；
- 不降低安全、隐私或法律事实的来源要求；
- 不把 `partial` 机械升级为 `verified`；
- 不把 `unreviewed` 自动改为 `accepted`；
- 不验证各章对象模型的完整性或最优性；
- 不对 AI Game Dev OS 或 lessismore 做任何修改；
- 不自动创建 Git Commit。

## 3. 统一原则

### 3.1 Reader-facing Prose 与 Editorial Metadata 分离

正文回答：

- 本章观察了什么；
- 本书提出什么；
- 为什么这样区分；
- 适用范围是什么；
- 哪些结论仍不能推出。

Evidence / RevisedResult 回答：

- Claim ID；
- Receipt ID；
- Coverage Status；
- Human Status；
- Git Revision；
- Counterevidence 明细；
- 历次处置变化。

### 3.2 理论模型不以 Receipt 作为准入证

纯理论或概念模型可以使用：

> 本书提出……

> 当前模型用于区分……

> 该模型尚未得到跨项目效果比较。

它不需要先取得 `verified` 才能进入书稿。

只有当理论被进一步表述为以下效果 Claim 时，才需要更强 Evidence：

- 提高质量；
- 降低成本；
- 减少缺陷；
- 优于替代方法；
- 适用于整个行业；
- 已被某个工程实现或验证。

### 3.3 “没有验证”与“没有意义”分开

使用下列读者语言：

| 内部状态 | 正文表达 |
|---|---|
| `partial` | 现有案例只支持其中的有限边界 |
| `unsupported` | 当前没有适配该效果或一般化主张的直接证据 |
| `unreviewed` | 不进入正文；保留在编辑工作面 |
| `accepted` | 不进入正文；只把接受后的观点自然写入正文 |
| `narrow` | 直接写出收窄后的适用条件 |
| `hold` | 暂不把该 Claim 当成事实或效果结论；理论模型可继续作为 Proposal 讨论 |

### 3.4 事实限制保留，工作流标签移除

以下内容必须保留：

- D-048 没有产生 Target Result；
- SP122 的 Adoption 与 Production 仍被阻止；
- OWASP 是安全指南，不是效果证明；
- NIST AI 600-1 是自愿风险管理 Profile；
- SLSA Provenance 不证明行为安全；
- U.S. Copyright Office 结论具有美国法域和时间边界。

以下内容从 Reader-facing Chapter 移出：

- `Coverage 为 partial`；
- `Human Status 为 unreviewed`；
- `当前处置为 narrow / hold`；
- Receipt ID 列表；
- 对同一 Claim 的完整 Supported / Unsupported 重复审计。

### 3.5 Evidence 强度按风险升级

后续采用四种写作模式，但不新增目录或新的 Skill：

| 模式 | 用途 | 最小记录 |
|---|---|---|
| Exploratory | 新概念、类比、早期推导 | 在正文或 RR 标明“候选／推导／开放问题” |
| Source Note | 标准、论文、公开事实 | 来源、实际支持内容、一句局限 |
| Conceptual Review | 核心理论模型 | 定义、解释目标、最强反例、适用边界、替代模型 |
| Formal Receipt | 历史事实、跨项目推广、高风险结论、OS 反馈 | 完整 Evidence Receipt 与 Claim Ledger |

不创建第五套 Claim Card 工作面，避免用新流程解决流程过重。

## 4. Evidence Receipt 的启动条件

以后只有满足至少一项时，才默认建立正式 Receipt：

1. 主张依赖 AI Game Dev OS、lessismore 或 Beyond Code 的精确历史事实；
2. 从一个项目案例推广到多个项目、组织或行业；
3. 涉及 Security、Privacy、Legal、IP 或其他高风险的具体事实；
4. 主张将直接反馈并改变 AI Game Dev OS 的 Workflow、Authority 或 Runtime；
5. 主张声称某机制提高质量、效率、成本、可靠性或安全性；
6. 不同来源发生实质冲突，需要保存裁决依据；
7. 作者明确要求正式取证或独立审阅。

下列情况默认不建立 Receipt：

- 术语定义；
- 候选对象模型；
- 章节结构选择；
- 解释性类比；
- 作者经验和审美判断；
- 已明确写成 Proposal 的工程建议；
- 不影响外部工程的普通叙事修改。

## 5. Reader-facing Chapter 统一头部

各章工作稿最终统一为最多三类头部信息：

~~~markdown
> 工作稿状态：首轮逻辑修订稿，不替代原始材料。
> 修订说明：对应 `RR-NNN`。
> 适用边界：仅在本章确有高风险误读时保留一句读者需要知道的限制。
~~~

不得在正文头部继续罗列：

- Claim ID；
- Receipt ID；
- `partial / unreviewed / accepted / unsupported / hold`；
- 多份 RR 的审计链；
- Git Commit 和 Worktree Status。

`OptimizedDocs/README.md`、`RevisedResult/` 和 `Evidence/` 是编辑工作面，可以继续显示这些状态。

## 6. 文件级调整范围

### 6.1 第1–5章：只做回归检查

涉及文件：

- `第1章_软件工程角色演进_首轮修订稿.md`
- `第2章_传统软件工程操作条件_首轮修订稿.md`
- `第3章_AI原生软件工程定义_首轮修订稿.md`
- `第4章_Intent与Agent_Input对象边界回接稿.md`
- `第5章_Context对象边界回接稿.md`

动作：

- 不改理论内容；
- 不因 Evidence 规则变化删除 Claim、Context、Authority 等概念；
- 检查头部是否仅保留工作稿状态和必要 RR Link；
- 检查正文没有内部 Coverage / Human Status；
- 保留第3章 Control and Evidence Plane 的理论内容。

### 6.2 第6章：只移除编辑状态，不削弱 Truth 模型

动作：

- 将头部 `核心 Claim` 和 `Evidence：五条 Claim...` 移至对应 RR；
- 保留 State Claim、Evidence Generation、Coverage、Authority 和 Conflict 等正文；
- 保留“不要注册所有 Claim”的反模式；
- 不因本计划压缩第6章已经恢复的原稿内容；
- 不重新打开对象模型重构。

### 6.3 第9章：移除顶部处置清单，保留 Evidence 理论

动作：

- 从正文头部移除已接受／待裁决 Claim 与 Receipt ID 列表；
- 保留 Evidence Coverage、Evidence Portfolio、Decision Disposition 和 Evidence-driven DoD；
- 不把 `Evidence` 词频视为审计泄漏；
- 确认 Evidence 不被重新解释成统一强弱等级。

### 6.4 第11–12章：轻量头部清理

动作：

- 移除顶部 `accepted + split / narrowed` 与 `partial`；
- 保留 Decision-sufficient Understanding、Compression Validation 和 HCP Projection；
- 不修改已接受的 `CLM-C11-001` 与 `CLM-C12-001` 理论边界；
- 在 RR-022、RR-023 中继续保存完整处置。

### 6.5 第13–16章：把 Evidence Boundary 改成读者边界

共同动作：

- 压缩顶部多条 Claim / Receipt / Status；
- 只保留一条自然语言适用边界；
- 保留正文内与章节对象直接相关的 Evidence 讨论；
- 不改变对象模型。

逐章边界：

- 第13章保留 Capability、Permission、Authority、Autonomy 与 Protected Control Floor；
- 第14章保留 Observation、Detector、Signal、Exception 与 Intervention；
- 第15章将“没有正式 Receipt 证明完整实现”改成“本章提出候选 Memory Governance 模型，不声称三个工程已经完整实现”；
- 第16章保留 v4.94 Candidate / Baseline / Adoption 案例和长期效果未知，但删除顶部内部状态标签。

### 6.6 第17章：核心语义修正

当前问题：

- 纯理论组织模型被 `unsupported / unreviewed / hold` 状态支配；
- 缺少单 Agent／多 Agent 效果比较，被误读成模型本身缺少提出资格。

必须调整：

1. 从 Reader-facing Header 删除 `CLM-C17-001` 的内部状态；
2. 将 Evidence Boundary 改为：

   > 本章提出一个候选组织模型，用于区分 Work、Role、Assignment、Authority、Handoff、Conflict 与 Integration；它不声称多 Agent 必然提高质量、速度或成本表现。

3. 审查正文中的 `必须 / 至少 / 本质上 / 只有`：
   - 若是本书工作定义，可以保留并明确 Scope；
   - 若是效果或行业普遍性 Claim，改为条件式表述；
4. 不删除 `CLM-C17-001` Ledger 历史行；
5. 不自动改变 `human_status`；
6. 在 RR-028 追加 Narrative Cleanup Addendum，说明：Coverage Status 约束效果和一般化主张，不限制候选概念模型进入正文。

### 6.7 第18章：压缩审计头部

动作：

- 将四条 Trace / Accountability Claim 状态压缩为一句读者边界；
- 保留 SP122 只能支持有限重建、不能支持隐藏推理或确定性 Replay 的限制；
- 保留 Traceability、Attribution、Reconstructability 与 Accountability 的概念区分；
- 保留 Evidence Link、Invalidation Link 等本章主题内容；
- RR-029 继续保存完整 Receipt 映射。

建议头部语义：

> 本章保存可观察的外部决策环境，不声称恢复隐藏推理或保证确定性重放；Accountability 仍由具名 Human／组织 Authority 分配。

### 6.8 第19章：删除重复 Coverage 审计

必须调整：

1. 从头部移除三个 Claim 的 `partial / unreviewed` 状态；
2. 保留 RR-030 Link、法律边界和必要外部来源；
3. 删除 `19.34 三条核心 Claim 的当前证据状态` 整节；
4. 将其必要限制分别留在相关正文：
   - Prompt Injection 控制不能被写成完整解决；
   - Provenance 不证明安全和适用；
   - U.S. Copyright Office 不能推出全球 IP 结论；
   - D-048 不是 Prompt Injection 或恶意供应链事件；
5. 顺延章节编号：
   - 原 19.35 → 19.34；
   - 原 19.36 → 19.35；
   - 原 19.37 → 19.36；
   - 原 19.38 → 19.37；
6. 更新 RR-030 中如有涉及旧章节编号的引用；
7. 三份 Receipt 与 Ledger 行全部保留。

### 6.9 第2章证据化修订样例：明确豁免

`第2章_证据化修订样例.md` 的用途就是展示 Evidence Workflow。

它不是 Reader-facing Chapter 主稿，不参加去审计化清理。

## 7. 写作基础设施调整

### 7.1 `AGENTS.md`

新增 `Evidence Intensity Routing`：

- Receipt 不是理论进入正文的许可证；
- 每章 `0–3` 个正式 Claim，而不是必须 `1–3` 个；
- 纯理论模型优先 Conceptual Review；
- 只有满足第4节 Trigger 才建立 Receipt；
- Reader-facing Chapter 不显示内部 Evidence Status；
- Security、Legal、Historical Fact 与 Cross-project Generalization 仍维持严格来源要求。

### 7.2 `.agents/skills/evidence-receipt/SKILL.md`

新增 Routing Boundary：

- 若输入是纯概念模型、章节结构或作者经验，不创建正式 Receipt；
- 返回主笔，建议放入正文 Proposal 或 RevisedResult；
- 只有效果、历史、一般化或高风险事实 Claim 才继续完整流程。

不改变现有 Receipt 字段和 Coverage Status，避免破坏历史收据。

### 7.3 `Evidence/README.md`

新增：

- 何时需要 Receipt；
- 何时不需要 Receipt；
- `partial` 不等于观点不可写；
- Human Acceptance 不改变 Evidence Coverage；
- 理论模型不使用 `unsupported` 作为正文标签。

### 7.4 不增加新的 Agent 或 Skill

本次问题来自流程适用范围过宽，不需要通过新增 Agent、Claim Card Skill 或目录解决。

## 8. 实施阶段

### Phase 0：建立差异基线

1. 记录当前 Branch、HEAD 和 Worktree Status；
2. 记录所有待修改文件的 Line Count 与 Heading；
3. 确认 `OringinalDocs/` 当前 tracked diff；
4. 保存本计划涉及文件清单；
5. 不 Stash、不 Clean、不 Checkout 外部工程。

### Phase 1：调整写作规则

修改：

- `AGENTS.md`；
- `.agents/skills/evidence-receipt/SKILL.md`；
- `Evidence/README.md`。

先修正未来行为，再清理现有正文，防止执行过程中继续产生新 Receipt。

### Phase 2：处理高优先级章节

顺序：

1. 第17章；
2. 第19章；
3. RR-028 Addendum；
4. RR-030 Addendum 或后续实施记录。

这一阶段只处理真正影响读者理解的内容。

### Phase 3：统一章节头部

依次处理：

1. 第11–16章；
2. 第18章；
3. 第6章；
4. 第9章；
5. 第1–5章只检查、不主动改正文。

### Phase 4：索引与记录

- 更新 `OptimizedDocs/README.md` 的状态说明；
- 更新 `RevisedResult/README.md`；
- 新建一份实施结果记录，建议编号 `RR-032`；
- Claim Ledger 只在处置语义确实变化且有 Human Decision 时修改；
- 不覆盖 RR-022 至 RR-030 的历史内容，使用 Addendum 记录变化。

### Phase 5：验证

执行结构、链接、差异和语义验证，见第10节。

## 9. 修改规则

### 可以删除

- Reader-facing Header 中的内部 Claim Status；
- 正文重复的 Receipt Coverage Assessment；
- 已在 RR 中完整存在的审计列表；
- `等待作者裁决` 之外更细的机器工作流状态；
- 对同一限制在章首、正文和章末的三次重复。

### 不能删除

- 事实来源；
- 案例实际结果；
- `non-result`；
- 反例和适用边界；
- 安全与法律的法域／时间限制；
- 对“本书提出”的明确声明；
- 失败模式；
- 读者需要理解的方法边界。

### 不能静默改变

- Claim 的原文；
- Human Disposition；
- Coverage Status；
- D-048、SP122、D-079 等历史事实；
- 已接受的 `split / narrowed` 边界；
- 原稿内容。

## 10. 验收标准

### 10.1 Reader-facing 状态检查

完成后，主章节头部不应出现：

~~~text
partial
unreviewed
accepted +
unsupported
hold
Human Status
Coverage Status
~~~

允许这些词出现在：

- `Evidence/`；
- `RevisedResult/`；
- `OptimizedDocs/README.md`；
- 第2章证据化修订样例；
- 第9章正文对 Coverage 概念的理论说明，但不是本章编辑状态。

### 10.2 内容保真

- 第17章组织对象集不减少；
- 第19章五个候选工作对象不减少；
- 第6章恢复内容不减少；
- 第9章 Evidence / Decision 边界不减少；
- 第11–18章已接受的核心边界不改变；
- 删除内容可以在 RR 或 Evidence 中找到对应来源。

### 10.3 结构检查

- 所有 Chapter Heading 连续；
- 第19章删除 19.34 后完成后续编号顺延；
- Markdown Fence 成对；
- 相对链接可解析；
- README 索引指向现存文件；
- 无重复 RR ID 或 Claim ID。

### 10.4 Git 检查

- `git diff --check` 无错误；
- `git diff -- OringinalDocs` 无新增 tracked diff；
- 外部两个 Repository 保持只读；
- 修改只落在计划列出的文件；
- 不自动 Commit。

### 10.5 语义检查

每个调整章逐项回答：

1. 删除的是审计元数据还是理论内容？
2. 读者能否仅靠正文理解主张和边界？
3. 事实、推导和建议是否仍然分开？
4. 是否把“没有验证效果”误写成“不能提出模型”？
5. 是否因去审计化而形成过度确定性？

## 11. 风险与控制

| 风险 | 可能后果 | 控制 |
|---|---|---|
| 清理过度 | 法域、反例或事实限制被删 | 删除前将每条限制映射到 RR / Receipt，保留读者必要版本 |
| 清理不足 | 正文仍像审计报告 | 对 Chapter Header 和 Evidence Status 专节做模式扫描 |
| 偷改 Claim | 历史处置失真 | 不删除 Ledger 行，不改 Human Status，无决定不改 Disposition |
| 第17章变成无边界理论 | 从 Proposal 滑向普遍定律 | 明确“不声称多 Agent 必然提高效果” |
| 第19章变得过度自信 | 安全或法律误导 | 保留 OWASP / NIST / SLSA / USCO 的作用与限制 |
| 新增轻量流程再次膨胀 | Meta-work 继续增加 | 不新建 Claim Card 目录或 Skill，使用既有正文和 RR |
| 编号和链接破坏 | 索引失效 | 自动链接检查、Heading 检查与 README 校验 |

## 12. Review Gate

### Gate A：Mechanical Review

- Header 是否统一；
- Status 是否移出；
- Heading、Link、Fence 是否正确；
- OriginalDocs 是否未改。

### Gate B：Semantic Review

- 第17章是否仍是候选组织模型，而非效果承诺；
- 第19章是否仍保留安全、供应链和 IP 的关键限制；
- 第6、9章是否没有因关键词清理被误删理论内容；
- 各章是否仍区分事实、推导和建议。

### Gate C：Human Review

作者只需裁决：

- Reader-facing Header 模板是否接受；
- 第17章候选模型的表述是否符合作者观点；
- 第19章删除 Evidence Status 专节后，剩余限制是否足够；
- 是否在本轮之后统一进入第20章。

正式 `critical_reviewer` 子代理不是本次机械调整的必要条件；只有作者明确要求独立正式审阅时再调用。

## 13. 建议实施顺序

~~~text
Evidence routing rules
→ Chapter 17 semantic correction
→ Chapter 19 audit-section removal
→ Chapters 11–16 and 18 header cleanup
→ Chapters 6 and 9 metadata-only cleanup
→ Chapters 1–5 regression check
→ README and RR-032
→ mechanical + semantic validation
→ Human disposition
~~~

## 14. Git 策略

实施过程中不自动 Commit。

作者确认后，可形成一个独立 Commit：

~~~text
docs: separate evidence backplane from reader-facing chapters
~~~

该 Commit 应只包含：

- Evidence Routing 规则；
- Chapter Narrative Cleanup；
- RR Addendum / RR-032；
- README 更新。

不得夹带 `OringinalDocs/` 或外部工程修改。

## 15. 完成定义

本计划完成不等于删除 Evidence。

完成状态是：

> 研究依据仍然可以被后来者审计，作者仍能追踪 Claim 的来源与裁决；同时，读者不需要理解内部 Evidence Workflow，便能读懂理论、案例、边界与开放问题。

这次调整的目标不是降低严谨性，而是让严谨性位于正确的层。

## 2026-08-25 Implementation Status Addendum

本计划已经按 Phase 0–5 执行，实施范围、语义结果和验证记录见
[RR-032](RR-032_Evidence去审计化实施结果.md)。

“计划已执行”只描述文件调整已经发生，不自动表示作者接受任何 Review Gate。
作者随后接受了 Header 模板，记录如下；第17章候选组织模型、第19章剩余边界
和后续写作方向仍未因此获得裁决。本记录顶部的历史状态不作静默改写，整体
Human Disposition 继续保持 `unreviewed`。

### Human Decision 2026-08-25：三项 Header 模板

- Decision：`accepted`
- Scope：仅适用于 `OptimizedDocs/` 工作稿；三项分别为工作稿状态、单一 RR 回接说明和自然语言适用边界。
- Final manuscript：删除“工作稿状态”和“回接说明”，把读者仍需知道的适用边界融入正文。
- Non-decision：不自动接受第17章、第19章或开始第20章。

## Human Disposition

- Status: `unreviewed`
- Decision by:
- Decision at:
- Rationale:
