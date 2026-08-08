# Beyond Code: AI-Native Software Engineering

## 附录扩展资料：Claude Code、Codex 与 AI 原生软件工程实践映射

> 本文档是《Beyond Code: AI-Native Software Engineering》的配套附录草案，用于分析当前主流 Agentic Coding 产品如何映射到 AI 原生软件工程理论框架，以及哪些问题仍需由项目、组织或上层 Operating Model 解决。

---

## 文档信息

- **文档类型**：书籍附录 / 扩展研究资料
- **对应主文档**：《Beyond Code: AI-Native Software Engineering》
- **中文标题建议**：《超越代码：AI 原生软件工程》
- **附录主题**：Claude Code、Codex、Agent Runtime、AI Game Dev OS 与 AI-Native Software Engineering 的关系
- **评估日期**：2026-08-06
- **资料性质**：基于官方公开资料、产品能力观察与实际工程推演
- **重要说明**：产品能力变化很快，本附录描述的是特定时间点的能力快照，不应替代理论正文中的长期原则

---

# 一、为什么把产品分析放在附录

## 1. 理论正文需要长期稳定

正文应讨论长期有效的问题：

- Intent Engineering
- Context Engineering
- Truth Architecture
- Agent Reliability
- Evidence Engineering
- Review Engineering
- Cognitive Overload
- Governed Autonomy
- Observability
- Memory Governance
- Self-Evolution
- Multi-Agent Organization
- Traceability
- Security
- AgentOps

这些问题不应绑定某个模型、工具或厂商。

## 2. 产品能力具有明显时效性

Claude Code、Codex 等产品会持续增加：

- Worktree
- Skills
- Hooks
- Subagents
- Agent Teams
- Memory
- Automations
- Review
- Sandbox
- Permission Controls
- IDE / CLI / App Integration

如果把具体产品能力直接写入理论主体，正文会迅速过时。

## 3. 附录的作用

附录不是为了回答：

> Claude Code 和 Codex 谁更强？

而是为了回答：

> 当前 Agentic Coding 产品已经覆盖了 AI 原生软件工程中的哪些问题，哪些问题仍需由外部系统、项目治理和组织设计解决？

## 4. 正文、案例框与附录的分工

### 正文

定义：

- 稳定问题
- 工程原则
- 通用模式
- 方法论
- 生命周期
- 成熟度模型

### 正文案例框

提供简短现实映射，例如：

> Codex Worktree 解决并行执行的文件隔离问题，但不能自动解决 Intent 冲突和合并治理。

### 附录

提供：

- 产品级详细分析
- 当前能力快照
- 成熟度评分
- 外部系统缺口
- 实验方法
- 更新记录

---

# Appendix A  
# AI 原生开发工具统一评估方法

---

## A.1 评估目的

建立统一评估标准，避免产品分析退化为：

- 功能清单
- 主观体验
- 模型排名
- 厂商营销复述
- 简单横向比较

评估目标是判断：

1. 产品原生解决了哪些 AI 原生软件工程问题；
2. 哪些能力只能通过 Prompt、配置或人工约定实现；
3. 哪些能力需要外部 OS、Workflow 或组织制度补充；
4. 哪些问题目前仍是开放研究问题。

---

## A.2 统一评估维度

建议采用以下十四个维度。

### 1. Intent Management

评估：

- 任务目标如何表达；
- 是否支持结构化计划；
- 是否支持 Non-goals；
- 是否支持长期 Intent Registry；
- 是否检测 Intent Drift；
- 是否能明确 Human Decision Point。

### 2. Context Engineering

评估：

- 项目规则如何注入；
- Repo 如何读取；
- Context 是否可分层；
- 是否支持 Skill；
- 是否支持动态上下文；
- 是否记录 Context Provenance；
- 是否处理过期和冲突。

### 3. Truth and State Resolution

评估：

- 是否读取当前 Git 状态；
- 是否识别当前 Commit、Branch 和 Worktree；
- 是否区分文档意图与代码现实；
- 是否验证 Runtime；
- 是否显式标记 Assumption；
- 是否能处理多来源状态冲突。

### 4. Agent Execution

评估：

- 是否支持计划、执行、观察和修正；
- 是否支持工具调用；
- 是否支持长任务；
- 是否支持并行任务；
- 是否支持中途停止和接管；
- 是否具备明确停止条件。

### 5. Reliability and Recovery

评估：

- Sandbox；
- Retry；
- Rollback；
- Checkpoint；
- Tool Failure Handling；
- Model Fallback；
- Scope Control；
- Blast Radius。

### 6. Verification and Evidence

评估：

- 是否能运行测试；
- 是否执行静态分析；
- 是否收集运行时证据；
- 是否支持截图或产物证据；
- 是否将验收标准映射到证据；
- 是否区分自述与独立证据。

### 7. Review Lifecycle

评估：

- 是否只有事后 Review；
- 是否支持 Plan Review；
- 是否支持中途 Checkpoint；
- 是否支持 Post-execution Review；
- 是否根据风险调整 Review 强度；
- 是否支持独立 Review Agent。

### 8. Cognitive Compression

评估：

- 是否提供变更摘要；
- 是否提供 Architecture Impact；
- 是否提供 Risk Map；
- 是否提供 Decision Surface；
- 是否支持 Progressive Disclosure；
- 是否跟踪 Cognitive Debt。

### 9. Autonomy Governance

评估：

- 权限等级；
- 审批策略；
- 自动执行边界；
- 高风险操作升级；
- Stop-the-line；
- Human-in-the-loop；
- Automation Default Off 能否实现。

### 10. Observability and Intervention

评估：

- 任务时间线；
- 当前状态；
- Agent 活动；
- 工具调用；
- 风险变化；
- 成本；
- 人工暂停；
- 人工接管；
- 回滚和重规划。

### 11. Memory Governance

评估：

- 项目记忆；
- 自动记忆；
- Skill；
- 来源追踪；
- 过期；
- 冲突；
- Memory Pollution；
- Memory Review；
- 项目与跨项目隔离。

### 12. Self-Evolution

评估：

- 是否能从经验提取规则；
- 是否能更新 Skill；
- 是否有基线对比；
- 是否需要审批；
- 是否可回滚；
- 是否能监控演化后的回归；
- 是否支持跨项目受治理迁移。

### 13. Multi-Agent Organization

评估：

- Subagents；
- Agent Teams；
- Controller；
- Worker；
- 角色权限；
- Structured Handoff；
- 冲突处理；
- 责任升级；
- 输出汇总。

### 14. Traceability、Security and AgentOps

评估：

- 完整执行轨迹；
- Decision Graph；
- 权限审计；
- Data Boundary；
- Model Boundary；
- Supply Chain；
- 成本与延迟；
- 模型和工具漂移；
- 项目级 Benchmark。

---

## A.3 单项评估模板

每个维度统一使用以下结构：

```text
理论要求
当前产品实现
实际工作方式
解决了什么问题
没有解决什么问题
需要外部系统补充什么
成熟度判断
官方证据
版本与日期
```

---

## A.4 成熟度模型

| 等级 | 定义 |
|---|---|
| M0 | 没有对应能力 |
| M1 | 依赖 Prompt、人工约定或非结构化实践 |
| M2 | 有基础产品能力 |
| M3 | 有结构化工作流、权限或控制机制 |
| M4 | 可形成组织级、可验证的闭环 |
| M5 | 能持续评估，并在治理下进行自我改进 |

### 评分注意事项

- 评分针对某一时间点；
- 评分针对某一理论维度；
- 不等于厂商整体评分；
- 不等于模型智力评分；
- 不等于用户体验总评分。

---

## A.5 能力来源分类

每项能力应标记来源：

### Native

产品原生支持。

### Configurable

可通过配置、Hook、Skill 或规则实现。

### External

需要外部系统或组织流程。

### Open

目前仍无成熟答案。

---

# Appendix B  
# Claude Code：AI 原生软件工程案例研究

---

## B.1 产品定位

Claude Code 可以视为：

> Agentic Coding Environment + Tool Runtime + Context / Skill Extension Surface

其核心价值不只是生成代码，而是：

- 读取代码库；
- 编辑文件；
- 运行命令；
- 使用工具；
- 调用 Subagent；
- 维护项目指令；
- 通过 Hook 增加确定性控制；
- 通过 Skill 封装可复用工作方式。

它已经明显超过传统代码补全工具。

---

## B.2 Intent Management

### 当前能力

Claude Code 支持：

- 自然语言任务输入；
- Plan Mode；
- 任务分解；
- 执行前方案展示；
- 用户批准后执行；
- 项目规则和长期指令。

### 解决的问题

- 在执行前暴露 Agent 对任务的理解；
- 允许用户检查计划；
- 降低直接误改的风险；
- 支持较复杂任务的步骤化执行。

### 尚未完整解决

- 长期 Intent Registry；
- Intent Version；
- Non-goals 的结构化保存；
- Intent Drift 自动检测；
- Acceptance Criterion 与 Evidence 的系统映射；
- 多个任务之间的目标依赖关系。

### 需要外部系统补充

- Issue / Registry；
- 项目级目标树；
- 决策记录；
- Gate；
- 版本化 Intent；
- Controller 层。

### 初步成熟度

**M2–M3**

有任务级计划和控制，但未形成完整项目级意图治理。

---

## B.3 Context Engineering

### 当前能力

可分析：

- `CLAUDE.md`
- 项目级规则
- 组织级规则
- Skills
- 自动记忆
- Subagent 独立上下文
- MCP
- 动态 Context Injection

### 解决的问题

- 让 Agent 理解项目规范；
- 减少每次重复说明；
- 将领域经验封装为可复用能力；
- 为不同 Agent 提供不同上下文；
- 在长期项目中保留部分项目知识。

### 尚未完整解决

- 事实与推断的正式区分；
- Context Provenance；
- 过期管理；
- 冲突裁决；
- 旧规则和新代码不一致时的优先级；
- 自动记忆的验证；
- 跨项目污染。

### 需要外部系统补充

- Context Registry；
- Truth Hierarchy；
- Memory Review；
- 过期策略；
- 项目与组织知识分层；
- Assumption Layer。

### 初步成熟度

**M3**

上下文机制较强，但 Context Governance 仍需外部设计。

---

## B.4 Truth and State Resolution

### 当前能力

Claude Code 能：

- 读取当前文件；
- 运行 Git 命令；
- 检查测试；
- 读取构建状态；
- 根据工具返回调整；
- 在当前环境中观察结果。

### 解决的问题

- 不是仅依赖用户描述；
- 能从代码和运行环境获得 Grounding；
- 可以验证部分任务结果。

### 尚未完整解决

- 自动建立 Truth Hierarchy；
- 显式区分 Doc as Intent 与 Code as Truth；
- 对 Assumption 做统一标记；
- 自动识别过期截图、旧分支和历史状态；
- 形成 State Snapshot。

### 初步成熟度

**M2–M3**

具备读取现实状态能力，但缺少系统性的事实裁决架构。

---

## B.5 Agent Execution

### 当前能力

包括：

- Agent Loop；
- 文件操作；
- 命令执行；
- 测试运行；
- MCP；
- Subagents；
- Agent Teams；
- Worktree 场景；
- 工具权限控制。

### 解决的问题

- 能完成端到端工程任务；
- 可以将不同任务分给专用 Agent；
- 可以减少主 Agent 的上下文压力；
- 支持更复杂工作流。

### 尚未完整解决

- 统一 Agent Contract；
- 全局 Controller 状态；
- 标准化 Handoff；
- 多 Agent 目标冲突；
- 长任务的统一 Checkpoint；
- 输出洪水控制。

### 初步成熟度

**M3**

是强执行环境，但不是完整生产组织。

---

## B.6 Reliability and Recovery

### 当前能力

可分析：

- 权限模式；
- Plan Mode；
- Hooks；
- Git；
- Worktree；
- 工具限制；
- 人工终止；
- 测试反馈；
- 命令失败后的调整。

### 优势

Hooks 提供确定性生命周期节点，可以强制：

- 格式化；
- Lint；
- 测试；
- 安全检查；
- 日志；
- 自定义 Gate。

这体现了一个重要原则：

> 概率性推理应由确定性机制约束。

### 尚未完整解决

- 统一 Retry Policy；
- 失败分类；
- Checkpoint Recovery；
- 模型切换策略；
- 自动 Blast Radius 分级；
- 可靠性指标体系。

### 初步成熟度

**M3**

有较强控制面，但可靠性工程仍需项目化实现。

---

## B.7 Verification and Evidence

### 当前能力

- 运行测试；
- 静态检查；
- 代码 Review；
- Hook 验证；
- Diff；
- 命令输出；
- 可能的自动 PR Review。

### 解决的问题

- 可以获得比文本自述更强的证据；
- 能执行自动化质量检查；
- 可让 Reviewer Agent 独立检查部分问题。

### 尚未完整解决

```text
Acceptance Criterion A → Evidence A
Acceptance Criterion B → Evidence B
Risk C → Regression Evidence C
```

尚缺：

- Evidence Schema；
- Evidence Provenance；
- 当前 Commit 绑定；
- 未覆盖风险提示；
- 可复现证据包；
- Evidence-Driven DoD 的统一强制执行。

### 初步成熟度

**M2–M3**

可以生成证据，但尚未形成完整 Evidence Engineering。

---

## B.8 Review Lifecycle

### 当前能力

- Plan Mode；
- 执行前方案检查；
- 执行后 Diff；
- 自动 Review；
- Hook 检查；
- 人工交互。

### 仍需加强

- 标准 Pre-execution Review；
- In-process Checkpoint；
- Review Budget；
- 风险自适应 Review；
- 独立 Cognition Agent；
- Review 结果与 Evidence Mapping。

### 初步成熟度

**M2–M3**

具备 Review 组件，但尚未成为完整 Review Lifecycle。

---

## B.9 Cognitive Engineering

### 当前能力

- 修改摘要；
- Diff；
- 任务说明；
- 进度输出；
- Subagent 结果汇总；
- 可能的解释性输出。

### 已解决

- 比原始代码输出更易理解；
- 可以降低部分 Review 成本；
- 可让主 Agent 汇总 Worker 结果。

### 尚未解决

- Architecture Impact View；
- Risk Map；
- Decision Surface；
- Cognitive Debt；
- Review Fatigue；
- Cognitive Load Budget；
- 人类是否仍保持系统心智模型的评估。

### 初步成熟度

**M1–M2**

已有摘要和 Diff，但距离完整 Cognitive Engineering 仍较远。

---

## B.10 Governed Autonomy

### 当前能力

- Plan；
- Manual；
- Permission；
- Hook；
- 工具控制；
- 人工确认；
- 可能的组织级策略。

### 已解决

- 可以避免默认完全自治；
- 可将高风险步骤交给人确认；
- 可在特定生命周期节点强制执行控制。

### 尚未解决

- 通用 Autonomy Level；
- Risk-based Autonomy Model；
- 组织级 Decision Right；
- 权限动态升级；
- 统一 Stop-the-line 标准。

### 初步成熟度

**M3**

具备较强治理基础，但需要上层风险模型。

---

## B.11 Observability and Intervention

### 当前能力

- 命令和工具输出；
- 任务状态；
- Agent 活动；
- 终止；
- 交互式修正；
- 可能的团队协调信息。

### 尚未解决

- 统一 Dashboard；
- 风险趋势；
- 成本趋势；
- 多 Agent 总览；
- Checkpoint 可视化；
- 组织级 Intervention Policy。

### 初步成熟度

**M2**

可观察单次执行，但组织级可观测性仍不足。

---

## B.12 Memory Governance

### 当前能力

- 项目记忆；
- 自动记忆；
- Skills；
- 项目规则；
- 会话历史。

### 优势

- 有能力沉淀项目经验；
- 可减少重复说明；
- Skill 能封装可复用流程。

### 风险

- 记忆可能未经验证；
- 错误经验可能被长期复用；
- 过期知识可能持续影响执行；
- 项目特殊规则可能被泛化；
- 用户未必知道 Agent 写入了什么。

### 尚需补充

- Memory Provenance；
- Memory Approval；
- Memory Expiry；
- Conflict Detection；
- Project / Cross-project Isolation；
- Memory Rollback。

### 初步成熟度

**M2–M3**

具备记忆能力，但 Memory Governance 仍不成熟。

---

## B.13 Self-Evolution

### 当前能力

- 人工维护 Skills；
- 自动记忆；
- 通过 Hook 改进流程；
- 通过项目规则持续优化 Agent 行为。

### 不等于完整演化

完整 Self-Evolution 需要：

```text
Experience
→ Candidate Rule
→ Baseline Comparison
→ Evaluation
→ Approval
→ Skill Update
→ Regression Monitoring
→ Rollback
```

### 初步成熟度

**M1–M2**

有演化素材和扩展机制，但治理闭环主要依赖人类。

---

## B.14 Multi-Agent Organization

### 当前能力

- Subagents；
- Agent Teams；
- Lead Agent；
- 角色化工具权限；
- 独立上下文。

### 优势

- 支持专业分工；
- 降低单一 Context 压力；
- 支持并行探索；
- 允许不同工具权限。

### 尚未完整解决

- 标准角色责任；
- 冲突裁决；
- Structured Handoff；
- 输出压缩；
- Controller 的全局 Intent 保持；
- 多 Agent 成本与认知管理。

### 初步成熟度

**M3**

具备多 Agent 能力，但完整组织模型仍需外部设计。

---

## B.15 综合结论

> Claude Code 已经是强 Agentic Execution Environment，具备丰富的 Context、Tool、Hook、Subagent、Memory 和 Permission 能力。但项目级 Intent Governance、Truth Architecture、Evidence-Driven DoD、Cognitive Governance、Memory Pollution Control 和受治理 Self-Evolution，仍主要需要外部工程体系补充。

---

# Appendix C  
# Codex：AI 原生软件工程案例研究

---

## C.1 产品定位

Codex 可以视为：

> Agent Runtime + Parallel Task Interface + Worktree / Git Integration + Skill Extension Surface

核心能力包括：

- Repo 理解；
- 文件编辑；
- 命令和测试执行；
- Thread；
- 并行 Agent；
- Worktree；
- Skills；
- Automations；
- Git Diff 和 Review；
- IDE / CLI / App 形态。

其演进方向已经明显从“代码生成模型”转向“软件工程执行 Agent”。

---

## C.2 Intent Management

### 当前能力

- Thread 任务输入；
- 自然语言目标；
- 任务规划；
- 多任务并行；
- 主线程与 Worker 任务分配；
- 用户交互修正。

### 已解决

- 每个 Thread 可以承载独立任务；
- 可以把复杂工作拆给多个 Worker；
- 用户可以在执行中调整方向。

### 尚未完整解决

- 长期 Intent Registry；
- 跨 Thread 目标依赖；
- Non-goals；
- Intent Drift；
- Acceptance / Evidence Mapping；
- 主线程是否始终维持完整全局目标。

### 初步成熟度

**M2–M3**

任务级 Intent 很强，项目级意图治理仍需外部系统。

---

## C.3 Context Engineering

### 当前能力

- Repo Context；
- Instructions；
- Skills；
- 渐进式加载；
- Thread Context；
- Worktree 状态隔离；
- 可能的外部工具和 MCP。

### 优势

- Skill 可封装任务专用说明和资源；
- 渐进式加载可减少上下文污染；
- Worktree 让不同任务具有独立工作状态；
- Thread 使任务上下文相对隔离。

### 尚未完整解决

- Context Provenance；
- 冲突检测；
- 过期；
- 推断与事实分离；
- 不同 Thread 的全局 Context 同步；
- 主线变更后 Worker Context 是否及时刷新。

### 初步成熟度

**M3**

上下文与执行隔离较强，但治理仍需要上层设计。

---

## C.4 Truth and State Resolution

### 当前能力

- 读取当前 Repo；
- Git 状态；
- Branch / Worktree；
- 测试和命令输出；
- 当前文件状态；
- 线程内执行环境。

### 优势

Worktree 明确提供：

- 独立文件状态；
- 并行修改隔离；
- 降低 Worker 相互覆盖风险；
- 更清晰的任务边界。

### 尚未完整解决

- 全局 Truth Hierarchy；
- 文档与代码冲突裁决；
- Worker 是否基于正确 Commit；
- 脏改是否属于当前任务；
- Runtime 与代码状态一致性；
- Assumption Layer。

### 初步成熟度

**M3**

状态隔离强，但事实裁决仍需 OS 或项目规则。

---

## C.5 Agent Execution

### 当前能力

- Thread；
- Worker；
- 并行 Agent；
- Worktree；
- Skills；
- 命令；
- 测试；
- Git；
- Automations；
- IDE / App / CLI。

### 已解决

- 多任务并行；
- Agent 隔离执行；
- 可复用技能；
- 长任务工作台；
- 结果可进入 Git 流程。

### 尚未完整解决

- Controller / Worker 标准协议；
- Worker 开启模板；
- 任务回传格式；
- 全局依赖管理；
- 冲突协调；
- 输出洪水；
- 多 Agent 结果合并策略。

### 初步成熟度

**M3–M4**

执行基础设施非常强，但组织治理依赖上层设计。

---

## C.6 Reliability and Recovery

### 当前能力

可分析：

- Worktree；
- Git；
- Sandbox；
- Approval；
- 文件边界；
- 网络权限；
- 高风险操作审核；
- 独立线程；
- 用户接管。

### 已解决

- 并行任务隔离；
- 修改可回滚；
- 风险操作可审批；
- Agent 不必直接污染主工作区；
- 可通过 Git 建立恢复点。

### 尚未完整解决

- 统一 Retry Policy；
- 失败分类；
- 自动 Checkpoint；
- Thread 间依赖失败处理；
- 模型降级；
- 长任务恢复；
- 可靠性指标。

### 初步成熟度

**M3**

隔离与权限较强，恢复和可靠性度量仍需补充。

---

## C.7 Verification and Evidence

### 当前能力

- 测试执行；
- Diff；
- Git；
- Commit；
- Review；
- 工具输出；
- 线程记录；
- 可能的自动 Reviewer。

### 已解决

- 修改可追踪；
- 可以执行真实测试；
- 可以形成提交；
- 可将 Worker 结果送交 Review。

### 尚未完整解决

- Evidence Schema；
- Acceptance-to-Evidence Mapping；
- 视觉和运行时证据统一；
- 未覆盖风险；
- Evidence Provenance；
- Evidence 与 Commit 强绑定；
- Evidence Bundle。

### 初步成熟度

**M2–M3**

有证据素材，但完整证据工程仍需项目层实现。

---

## C.8 Review Lifecycle

### 当前能力

- Thread 内检查；
- Diff Review；
- 用户评论；
- Git Review；
- 可能的专用 Reviewer Agent；
- 主线程汇总 Worker 结果。

### 关键现实问题

在 Controller / Worker 模式下：

- Worker 可以做很多；
- 主线程可能只收到简短汇报；
- 人类可能无法重建 Worker 完整过程；
- 事后 Review 可能过晚；
- 并行 Agent 会加速 Cognitive Overload。

### 尚需补充

- Pre-execution Review；
- Worker Plan Approval；
- In-process Checkpoint；
- Structured Return；
- Review Budget；
- Risk Escalation；
- Independent Review Agent。

### 初步成熟度

**M2–M3**

有强结果 Review 界面，但全生命周期 Review 需外部设计。

---

## C.9 Cognitive Engineering

### 当前能力

- Thread；
- Diff；
- 任务摘要；
- 并行任务可视化；
- 主线程结果汇总；
- 编辑器下钻。

### 已解决

- 比纯命令行更易理解并行任务；
- 可按 Thread 隔离查看；
- 可以下钻具体改动；
- 可减少不同任务之间的视觉混杂。

### 尚未解决

- Architecture Impact；
- Risk Map；
- Decision Surface；
- Cognitive Debt；
- 未理解改动量；
- Review Fatigue；
- 多 Worker 输出优先级；
- 人类认知预算。

### 初步成熟度

**M2**

有良好交互基础，但认知工程仍处于早期。

---

## C.10 Governed Autonomy

### 当前能力

- Sandbox；
- Approval；
- 文件范围；
- Worktree；
- 网络权限；
- 风险操作审查；
- Automations；
- 人工 Review。

### 优势

Codex 已体现：

> Agent 能力、环境权限和执行自治应分离。

### 风险

Automations 和并行 Worker 如果缺乏上层治理，可能导致：

- 任务泛滥；
- 结果洪水；
- 重复劳动；
- 隐形成本；
- 决策失控；
- 主线程无法保持全局理解。

### 初步成熟度

**M3**

底层治理能力较强，上层 Risk Model 仍需项目提供。

---

## C.11 Observability and Intervention

### 当前能力

- Thread 状态；
- Worktree；
- Diff；
- 任务活动；
- Git 状态；
- 人工评论；
- 编辑器接管。

### 尚未解决

- 全局多 Agent Dashboard；
- 风险趋势；
- 预算和成本；
- 跨 Thread 依赖；
- Context 版本；
- Agent 长时间无进展；
- 组织级 Stop-the-line。

### 初步成熟度

**M2–M3**

适合任务级观察，组织级观测仍需 OS。

---

## C.12 Memory Governance

### 当前能力

- Skills；
- Thread 历史；
- Repo Instructions；
- 可复用任务模板；
- 项目文件中的规则。

### 优势

Skill 可以：

- 封装任务步骤；
- 保存工具说明；
- 复用模板；
- 形成专业能力包；
- 跨 CLI、IDE、App 使用。

### 尚未完整解决

- Skill 来源；
- Skill Approval；
- Skill Regression；
- Skill Expiry；
- 失败 Skill 回滚；
- 自动经验提取；
- 项目 / 跨项目边界；
- Memory Pollution。

### 初步成熟度

**M2–M3**

可复用能力封装较强，但治理和演化不足。

---

## C.13 Self-Evolution

### 当前状态

Codex Skills 和项目指令提供了能力演化载体。

但真正 Self-Evolution 仍需要：

- Knowledge Miner；
- 失败分类；
- Rule Candidate；
- 基线评估；
- Approval；
- Skill Update；
- 回归监控；
- Rollback。

### 初步成熟度

**M1–M2**

具备能力载体，不具备完整演化闭环。

---

## C.14 Multi-Agent Organization

### 当前能力

- 多 Thread；
- 并行 Agent；
- Worktree；
- 主线程 / Worker 使用模式；
- Skills；
- 独立任务环境。

### 优势

- 很适合 Controller / Worker；
- 可隔离多个专业任务；
- 能并行探索；
- 结果可以分别 Review；
- Worktree 有助于减少文件冲突。

### 尚未完整解决

- Worker 开启标准；
- 主线程确认基线 Commit；
- Structured Handoff；
- Worker 回传协议；
- 任务依赖；
- 合并顺序；
- 冲突裁决；
- 主线程认知负载；
- 多 Agent 成本预算。

### 初步成熟度

**M3–M4**

是强多 Agent 执行平台，但不等于完整 Agent Organization。

---

## C.15 综合结论

> Codex 已经覆盖强执行、并行隔离、Git / Worktree、技能封装和多任务界面，适合作为 AI 原生软件生产的 Execution Substrate。但完整 Controller Governance、长期 Intent、Truth Architecture、Evidence-Driven DoD、Cognitive Compression、Memory Governance 和受控 Self-Evolution，仍需上层 Operating Model 提供。

---

# Appendix D  
# Claude Code 与 Codex 的框架映射

---

## D.1 对比原则

本附录不以“谁更好”为目标。

更有价值的问题是：

- 哪种产品能力对应哪类工程问题；
- 哪些能力是 Runtime 原生能力；
- 哪些能力需要项目层补充；
- 哪些问题仍属于开放领域。

---

## D.2 总体映射

| 理论维度 | Claude Code | Codex | 外部系统仍需解决 |
|---|---|---|---|
| Intent | 任务、Plan | Thread、任务规划 | 长期 Intent Registry |
| Context | CLAUDE.md、Memory、Skills | Repo Context、Skills、Thread | Provenance、过期、事实裁决 |
| Truth | 文件、命令、测试 | Git、Worktree、测试 | Truth Hierarchy、Assumption |
| Execution | Agent、Subagent、Hook | Thread、Worker、Worktree | 组织级调度和依赖 |
| Reliability | Permission、Hook、Git | Sandbox、Approval、Worktree | Retry、Checkpoint、指标 |
| Verification | Test、Hook、Review | Test、Diff、Git、Review | Evidence Mapping |
| Review | Plan、Post-review | Thread、Diff、Reviewer | 三阶段 Review |
| Cognition | Summary、Diff | Thread、Diff、并行视图 | Risk Map、Decision Surface |
| Governance | 权限、Hook | Sandbox、审批、Worktree | 风险模型、自治等级 |
| Observability | 执行输出 | Thread / Worktree 状态 | 组织级 Dashboard |
| Memory | 自动记忆、Skills | Skills、Thread 历史 | Memory Pollution Control |
| Evolution | 人工维护 Skill | 人工维护 Skill | Evolution Gate |
| Organization | Subagents、Teams | 并行 Agent、Worktree | 权责、冲突、Handoff |
| Security / Ops | 权限、Hook | Sandbox、审批 | 企业级策略、成本治理 |

---

## D.3 能力差异不应被简化为功能数量

需要考虑：

- 能力是否原生；
- 是否稳定；
- 是否可治理；
- 是否可追踪；
- 是否有证据；
- 是否能进入组织级流程；
- 是否增加认知负担；
- 是否可以跨项目复用。

---

## D.4 Runtime 能力与 Engineering System 的区别

产品提供：

- Agent；
- Tool；
- Thread；
- Worktree；
- Skill；
- Permission；
- Diff；
- Review Surface。

工程系统还需要：

- Intent Registry；
- Truth Hierarchy；
- Context Governance；
- Evidence Schema；
- Review Lifecycle；
- Cognitive Compression；
- Risk Model；
- Memory Governance；
- Evolution Gate；
- Accountability。

---

# Appendix E  
# AI Game Dev OS 与通用 Agent Runtime 的关系

---

## E.1 三层模型

```text
Layer 1 — Model
Reasoning / Generation / Understanding

Layer 2 — Agent Runtime
Claude Code / Codex
Tools / Threads / Worktrees / Skills / Permissions

Layer 3 — Production Operating Model
AI Game Dev OS
Roles / Context Packs / Gates / Evidence / Memory / Evolution
```

---

## E.2 Model 层

负责：

- 理解；
- 推理；
- 生成；
- 规划；
- 判断；
- 文本和代码处理。

Model 本身不等于完整生产系统。

---

## E.3 Agent Runtime 层

Claude Code / Codex 主要负责：

- 环境读取；
- 工具调用；
- 文件修改；
- 命令执行；
- 多 Agent；
- Worktree；
- 权限；
- Skill；
- 结果展示。

它回答：

> Agent 如何工作？

---

## E.4 Production Operating Model 层

AI Game Dev OS 负责：

- 谁做什么；
- 按什么流程；
- 使用哪些 Context；
- 哪些 Gate 必须通过；
- 什么算完成；
- 需要哪些 Evidence；
- 如何 Handoff；
- 如何 Review；
- 如何记忆；
- 如何演化；
- 人类在哪些节点决策。

它回答：

> Agent 在长期游戏项目中应按照什么制度工作？

---

## E.5 两者不是替代关系

错误理解：

```text
Claude Code / Codex
VS
AI Game Dev OS
```

正确理解：

```text
Claude Code / Codex
作为 Execution Runtime

AI Game Dev OS
作为 Domain Operating Model
```

---

## E.6 类比

```text
Claude Code / Codex
≈ 高能力员工 + 工作台

AI Game Dev OS
≈ 组织结构 + 项目制度 + 专业流程 + 质量体系
```

---

## E.7 AI Game Dev OS 的通用映射

| AI 原生理论 | AI Game Dev OS |
|---|---|
| Intent Engineering | Doc as Intent |
| Truth Architecture | Code as Truth |
| Context Engineering | Context Packs |
| Execution | Agents / Skills / MCP |
| Review | Review Agents |
| Evidence | Evidence-Driven DoD |
| Governance | Gates / Automation Default Off |
| Cognition | Change Summary / Risk Map |
| Traceability | Registry / Handoff |
| Memory | LTM |
| Evolution | Self-Evolution |
| Organization | Controller / Leads / Workers |

---

## E.8 可移植性原则

AI Game Dev OS 不应过度绑定单一 Runtime。

理想状态应适配：

- Claude Code；
- Codex；
- 未来其他 Coding Agent；
- 本地 Agent Runtime；
- 企业私有 Agent；
- 不同模型组合。

需要定义稳定 Adapter：

```text
Intent Adapter
Context Adapter
Execution Adapter
Evidence Adapter
Review Adapter
Memory Adapter
```

---

## E.9 Runtime 替换测试

验证 OS 是否真正独立，可以测试：

- 同一 Context Pack 能否投递给不同 Runtime；
- 同一 Worker Contract 是否可执行；
- Evidence 是否保持统一格式；
- Handoff 是否可迁移；
- Skill 是否需要重写；
- 结果质量差异是否可评估。

---

# Appendix F  
# 实验与实证设计

---

## F.1 为什么需要实验

如果只有概念，大纲可能被批评为：

- 理论推演；
- 工程常识重新命名；
- 缺少可验证价值；
- 过度架构化。

因此需要通过真实任务检验：

> 新机制是否真的提升成功率、降低返工、减少风险或保护人类认知。

---

## F.2 实验一：无 Context Pack 与有 Context Pack

### 对照组

只提供自然语言任务。

### 实验组

提供结构化 Context Pack：

- Goal；
- Current State；
- Constraints；
- Relevant Files；
- Decisions；
- Non-goals；
- Evidence Requirement。

### 观察指标

- First-pass Success；
- 返工次数；
- Scope Drift；
- Context Error；
- Human Review Time；
- 最终质量。

---

## F.3 实验二：单 Agent 与 Controller / Worker

### 对照组

单 Agent 规划、执行、验证和汇报。

### 实验组

Controller：

- 保持 Intent；
- 分配 Worker；
- 汇总证据；
- 控制范围。

Worker：

- 限定执行；
- Structured Return。

### 观察指标

- 目标保持；
- 并行效率；
- Handoff Loss；
- 重复劳动；
- 冲突；
- Human Cognitive Load；
- 合并成本。

---

## F.4 实验三：纯事后 Review 与三阶段 Review

### 对照组

任务完成后统一 Review。

### 实验组

- Pre-execution Review；
- In-process Checkpoint；
- Post-execution Review。

### 观察指标

- 方向性错误发现时间；
- 返工量；
- 总 Review 时间；
- 高风险变更数量；
- Scope Expansion；
- 最终缺陷率。

---

## F.5 实验四：原始 Diff 与 Cognitive Compression

### 对照组

人类只看：

- Diff；
- 测试结果；
- Agent 简短总结。

### 实验组

额外提供：

- Change Narrative；
- Architecture Impact；
- Risk Map；
- Decision Surface；
- Evidence Mapping。

### 测试人类能否回答

1. 修改目的是什么？
2. 哪些模块受到影响？
3. 最大风险是什么？
4. 哪些假设尚未验证？
5. 是否应该合并？
6. 出现问题时应从哪里 Debug？

### 观察指标

- 理解正确率；
- Review 时间；
- 错误批准率；
- 主观认知负担；
- 一周后的记忆保留。

---

## F.6 实验五：自动记忆与受治理记忆

### 对照组

Agent 可自动写入长期记忆。

### 实验组

记忆需要：

- Source；
- Scope；
- Confidence；
- Validation；
- Expiry；
- Approval。

### 观察指标

- 错误记忆率；
- 过期知识复用率；
- 跨项目污染；
- 问题复发率；
- Memory Review 成本；
- Agent 成功率。

---

## F.7 实验六：Skill 演化闭环

### 对照组

人工凭感觉修改 Skill。

### 实验组

```text
Failure / Success
→ Rule Candidate
→ Baseline
→ Evaluation
→ Approval
→ Skill Update
→ Regression Test
```

### 观察指标

- 任务成功率；
- Skill Regression；
- 适用范围错误；
- 回滚次数；
- 长期稳定性；
- 跨项目迁移效果。

---

## F.8 实验七：认知债测量

尝试定义 Cognitive Debt 指标：

- 未 Review 改动数；
- 未理解模块数；
- 无人能解释的架构变化；
- Agent 生成代码占比；
- 一周后团队解释正确率；
- Debug 接管时间；
- Human Override 失败率。

### 研究问题

- Cognitive Debt 是否能量化？
- 它与缺陷率是否相关？
- 它与交付速度是否相关？
- 它是否存在阈值效应？
- 如何偿还认知债？

---

## F.9 实验八：不同自治等级

比较：

- L1：AI 建议；
- L2：AI 执行，人逐项批准；
- L3：低风险自动；
- L4：目标级自治。

### 观察指标

- 交付时间；
- 错误率；
- 人工介入；
- Review 时间；
- 风险事件；
- 总成本；
- 人类信任；
- 认知保持。

---

# Appendix G  
# Living Appendix 维护规范

---

## G.1 为什么需要动态维护

产品能力变化很快：

- 新模型；
- 新权限；
- 新 Agent；
- 新 Memory；
- 新 Worktree；
- 新 Review；
- 新 Automation；
- 新安全策略。

书籍正文不能频繁修改，但附录可以保持动态。

---

## G.2 每个产品附录必须标记

```text
评估日期
产品版本
操作系统
使用界面
模型版本
资料范围
实验 Repo
评估者
```

---

## G.3 更新规则

每次更新应记录：

- 新增能力；
- 删除能力；
- 行为变化；
- 评分变化；
- 理论映射变化；
- 新风险；
- 新实验结果。

---

## G.4 Changelog 模板

```text
Version:
Date:
Product:
Changed Capability:
Previous Assessment:
New Assessment:
Evidence:
Impact on Theory:
```

---

## G.5 理论正文与附录的版本关系

### 理论正文

只有在核心问题或原则变化时更新。

### 产品附录

随产品重大版本更新。

### 实验附录

随新实验和数据更新。

---

## G.6 官方资料与实际实验分离

每个结论应标记：

### Official

来自官方文档。

### Observed

来自实际使用。

### Inferred

根据能力做出的推断。

### Proposed

本书提出的设计建议。

---

## G.7 避免厂商绑定

附录分析应避免：

- 把某产品实现当作唯一正确答案；
- 把当前产品限制写成永久理论；
- 把厂商术语直接升级为学科概念；
- 把模型能力和工程成熟度混为一谈。

---

# Appendix H  
# 建议放入正文的产品案例框

---

## H.1 Intent Engineering 案例框

### Plan Mode 的意义

Plan Mode 体现：

> Agent 在执行前应暴露任务理解和执行方案。

但 Plan Mode 不自动等于：

- Intent Registry；
- Non-goals；
- Intent Drift Control；
- Acceptance Mapping。

---

## H.2 Context Engineering 案例框

### 项目规则与 Skill

`CLAUDE.md`、Repo Instructions 和 Skills 说明：

> Context 已经从 Prompt 附属品变成工程资产。

但仍需治理：

- 来源；
- 版本；
- 过期；
- 冲突；
- 适用范围。

---

## H.3 Truth Architecture 案例框

### Worktree 的意义

Worktree 解决：

- 并行文件状态隔离；
- 不同任务互不覆盖；
- 结果独立 Review。

它不解决：

- 任务是否基于正确 Intent；
- Worker 是否拥有正确 Context；
- 多任务如何合并；
- 哪个结果应进入主线。

---

## H.4 Evidence Engineering 案例框

### 自动测试不是完整证据

测试通过只能证明：

- 某些可执行断言成立。

它不能自动证明：

- 体验目标达成；
- 架构合理；
- 视觉质量正确；
- 未覆盖风险不存在；
- 任务符合最初 Intent。

---

## H.5 Cognitive Engineering 案例框

### Diff 不等于理解

即使工具提供优秀 Diff，当修改规模过大时，人类仍可能：

- 看不懂整体影响；
- 无法识别隐藏架构变化；
- 机械批准；
- 失去系统心智模型。

---

## H.6 Governed Autonomy 案例框

### Sandbox 与 Approval

Sandbox 和审批说明：

> 能力、权限和自治必须分离。

Agent 能做某事，不代表默认应被允许执行。

---

## H.7 Memory Engineering 案例框

### 自动记忆的双刃剑

自动记忆提高连续性，也可能固化：

- 错误判断；
- 临时 workaround；
- 过期配置；
- 不适用于其他项目的特殊经验。

---

# Appendix I  
# 附录核心结论

---

## 1. Claude Code 和 Codex 确实沿着 AI 原生软件工程方向演进

它们已经覆盖：

- Context；
- Tool Use；
- Agent Loop；
- Sandbox；
- Permissions；
- Parallel Agents；
- Worktrees；
- Skills；
- 部分 Memory；
- 部分 Review；
- 部分 Automation。

---

## 2. 它们主要是 Execution Substrate

更准确的定位是：

```text
Claude Code / Codex
=
AI-native Execution Substrate
```

而不是：

```text
Complete AI-Native Software Engineering System
```

---

## 3. 上层工程能力仍然缺失

主要缺口：

- Long-term Intent Governance；
- Truth Architecture；
- Evidence-Driven DoD；
- Full Review Lifecycle；
- Cognitive Debt；
- Human Decision Surface；
- Memory Pollution Control；
- Controlled Self-Evolution；
- Organization Accountability。

---

## 4. AI Game Dev OS 与它们是上下层关系

```text
Model
↓
Claude Code / Codex Runtime
↓
AI Game Dev OS
↓
Game Production
```

AI Game Dev OS 的价值不是重新实现 Runtime，而是：

> 在 Runtime 之上定义游戏生产领域的组织、流程、Context、Evidence、Governance、Memory 和 Evolution。

---

## 5. 产品演进本身验证了理论问题

Claude Code 和 Codex 不断增加：

- Skills；
- Worktrees；
- Hooks；
- Memory；
- Subagents；
- Review；
- Permissions；
- Automations。

这说明现实产品正在被迫解决：

- 上下文；
- 隔离；
- 可靠性；
- 治理；
- 组织；
- 可观察性。

这些正是 AI 原生软件工程的核心范畴。

---

## 6. 下一阶段的关键不再只是更强模型

下一阶段更重要的竞争可能在于：

- 谁能更准确地保持 Intent；
- 谁能更可靠地管理 Context；
- 谁能形成更强 Evidence；
- 谁能降低 Cognitive Overload；
- 谁能提供合理自治边界；
- 谁能安全积累和演化组织能力。

---

# 参考资料方向

正式写作时，建议优先引用以下类型资料：

1. Claude Code 官方文档  
2. Anthropic Agent / Tool / Memory / Hook 文档  
3. OpenAI Codex 官方文档  
4. OpenAI Codex Agent Loop、Skills、Worktree、Security 文档  
5. SWE-bench、SWE-agent 等公开研究  
6. Agent Reliability、Human-AI Collaboration、AI Governance 论文  
7. Git、CI/CD、DevOps、ADR、Distributed Systems 经典资料  
8. 实际 Repo 实验和可复现数据  

所有产品结论应明确标记：

- 日期；
- 产品版本；
- 官方能力；
- 实际观察；
- 推断；
- 外部补充建议。

