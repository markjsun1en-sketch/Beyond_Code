# RR-006：写作 Agent 与 Skill 体系审阅

- 记录日期：2026-08-08
- 审阅对象：[AGENTS.md](../AGENTS.md)、项目 agents、`evidence-receipt` skill、Evidence 工作面
- 记录性质：既有方案判断与实施结果的结构化重建
- Human Disposition：`unreviewed`

## 核心结论

专职 Agent 和 Skill 对跨工程取证、反证和保持写作规则一致有用，但不是写书本身的必要条件。首版应维持“一个主笔、两个按需只读子代理、一个 Evidence Skill”的最小体系，避免基础设施膨胀和多写者声音漂移。

## 当前职责边界

### 主任务

- 唯一正文作者与整合者；
- 选择 Claim；
- 判断证据是否接受；
- 解决证据冲突；
- 写入 `OptimizedDocs/`；
- 接受作者最终裁决。

### Evidence Curator

- 只读收集 Beyond Code、lessismore、AI_DEV_OS_Evolve、Git、产物和可见任务记录；
- 返回结构化 Evidence Receipt 草案；
- 不修改正文，不发展理论，不写外部工程。

### Critical Reviewer

- 检查循环论证、概念膨胀、过度一般化、事实与推论混合及前后矛盾；
- 输出 survives / narrow / split / unsupported / contradicted；
- 不直接润色正文。

### Evidence Receipt Skill

- 固化 Claim 到证据收据的流程；
- 记录来源、版本、dirty 状态、观察、推导、反证、替代解释和人工状态；
- 不把所有证据机械排成单一强弱等级。

## 为什么保持最小体系

- 写作的核心瓶颈是判断和论证，不是 Agent 数量。
- 多个写作 Agent 会产生声音漂移、重复概念和责任不清。
- 每章单独建立 Agent 会增加配置维护成本，却不保证章节质量。
- 只有取证和正式反证具有明确、可分离、只读的专职边界。

## 启动规则

- 小型文字修改和普通讨论：不启动子代理。
- 跨三个工程收集证据：显式启动 Evidence Curator。
- 核心理论或正式章节反证：显式启动 Critical Reviewer。
- 两者同时使用：主任务等待双方结果后再裁决，不让代理直接写正文。
- 重复工作流在至少一至两个真实章节中稳定出现后，才考虑增加 Skill。

## 主要失败模式

- Agent 输出被当作独立证据，而没有追溯原始文件或产物。
- Reviewer 变成第二位作者，直接改变作者声音。
- Evidence 流程覆盖所有句子，造成写作成本失控。
- 为基础设施建立基础设施，迟迟不进入章节修改。
- 子代理对外部工程执行 checkout、format、commit 等写操作。

## 已形成的工作面

- 仓库级写作规则：`AGENTS.md`；
- 两个只读项目 Agent：`.codex/agents/`；
- Evidence Skill：`.agents/skills/evidence-receipt/`；
- Claim Ledger 与 Receipts：`Evidence/`；
- 工作稿：`OptimizedDocs/`；
- 审阅依据：`RevisedResult/`。

## 后续修改依据

正式章节循环仍保持：

```text
选择 1–3 个 Claim
→ 取证
→ Evidence Receipt
→ 反证
→ 主笔裁决
→ OptimizedDocs
→ 作者裁决
```

## 当前裁决建议

不增加结构编辑 Agent、章节专属 Agent、自动写作 Agent 或额外 Skill。先用第二章样例和第四章的一条核心主张验证完整闭环，再决定是否需要固化新的重复流程。

