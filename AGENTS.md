# Beyond Code Writing Rules

## 1. Purpose

This repository is a living knowledge base and book workspace for
`Beyond Code: AI-Native Software Engineering`. Its primary purpose is to
preserve the author's experience, test the resulting ideas against evidence,
and feed validated lessons back into later AI Game Dev OS design.

Publication readiness is not the default optimization target. Prefer faithful
reasoning, traceable evidence, and explicit uncertainty over polished certainty.

## 2. Repository Surfaces

- `OringinalDocs/` contains original source material. Treat it as immutable
  unless the user explicitly asks to edit an original document.
- `OptimizedDocs/` contains revised or reconstructed working drafts. Do not
  silently replace the author's original voice or overwrite an original file.
- `PolishedDocs/` contains reader-facing manuscript candidates derived from an
  accepted `OptimizedDocs/` baseline. It may change narrative structure,
  rhythm, and presentation, but it is not a second source of truth for claims,
  evidence, object boundaries, or case facts.
- `Evidence/` contains the Claim Ledger, Evidence Receipts, counterevidence,
  and human dispositions.
- `.agents/skills/` contains repository-scoped writing workflows.
- `.codex/agents/` contains repository-scoped, explicitly invoked subagents.

The spelling `OringinalDocs` is an existing repository contract. Do not rename
it incidentally.

## 3. Epistemic Labels

Keep these categories separate in analysis and prose:

1. **Observable fact**: directly supported by a cited file, commit, artifact,
   test, tool output, or visible task record.
2. **Contemporaneous judgment**: a decision or interpretation recorded by a
   human or agent at the time.
3. **Retrospective inference**: a later explanation derived from one or more
   observations.
4. **Current recommendation**: a proposed action or design choice.

Do not present an inference as an observed fact. Do not infer general validity
from one project without either corroborating cases or a clearly stated scope.

## 4. Evidence Rules

- Register important formal claims that meet the routing conditions below in
  `Evidence/claim-ledger.md`.
- Use `$evidence-receipt` for a formal Evidence Receipt.
- Bind repository evidence to project, path, branch, commit, and worktree
  status. If a file is uncommitted, say so explicitly.
- Match evidence to the claim type: runtime claims need runtime evidence;
  historical decisions need contemporaneous records; experience and aesthetics
  require human review.
- Record counterevidence, alternative explanations, and limitations even when
  evidence supports the claim.
- Treat Codex task transcripts as observable messages, tool activity, outputs,
  and file changes only. Never claim access to hidden chain-of-thought.
- Treat task summaries as supporting context rather than independent proof when
  stronger primary artifacts exist.
- Reference large external artifacts in place. Do not duplicate them into this
  repository unless the user asks for an archival copy.

### Evidence Intensity Routing

An Evidence Receipt is an audit tool, not permission for a theory to enter the
book. A chapter may have zero to three formal Claims; do not create them merely
to satisfy a chapter workflow.

Use a formal Receipt when at least one of these conditions applies:

- the Claim depends on precise repository history, runtime behavior, an
  artifact, or a contemporaneous decision;
- one project case is being generalized across projects, organizations, or an
  industry;
- the Claim states a concrete security, privacy, legal, IP, financial, or other
  high-risk fact;
- the conclusion will directly change AI Game Dev OS Workflow, Authority, or
  Runtime behavior;
- the Claim asserts an effect such as improved quality, speed, cost,
  reliability, or safety;
- material sources conflict, or the user explicitly requests formal evidence
  collection or audit.

Do not create a Receipt by default for terminology, a candidate conceptual
model, chapter structure, explanatory analogy, ordinary prose, lived
experience, aesthetics, or a recommendation explicitly presented as a
proposal. Evaluate those through definition quality, internal consistency,
counterexamples, alternatives, scope, and Human review.

Absence of empirical validation limits an effect or generalization Claim; it
does not by itself make a conceptual model ineligible for discussion.

### Reader-facing Boundary

Keep Claim IDs, Receipt IDs, Git metadata, Coverage Status, Human Status, and
disposition history in `Evidence/`, `RevisedResult/`, or editorial indexes.
Reader-facing chapter prose should instead state the source, observable case,
inference, proposal, scope, and material limitation in natural language.

Do not remove factual, legal, security, or case-study limitations merely to
make prose smoother.

For current `OptimizedDocs/` working drafts, use at most three header lines:

1. work-draft status and original-material boundary;
2. one primary `RevisedResult/` link;
3. one natural-language scope or non-claim boundary.

These lines are editorial scaffolding, not final-book front matter. In a final
manuscript, remove the work-draft status and revision link, and integrate any
reader-relevant scope boundary into the chapter's opening argument or the
specific passage it constrains.

Reader-facing chapter candidates under `PolishedDocs/` must not carry the
work-draft header or revision link. Directory README files and implementation
plans remain editorial documents and may link to `RevisedResult/`. If polishing
reveals a substantive claim, definition, evidence, or case-boundary change,
route that change back through `OptimizedDocs/`, `Evidence/`, or
`RevisedResult/` before reflecting it in the reader-facing manuscript.

## 5. Agent Roles and Activation

The main task is the sole writer and integrator. It owns claim selection,
conflict resolution, Evidence Receipt persistence, and changes to
`OptimizedDocs/` and `PolishedDocs/`.

Two read-only project agents are available:

- `evidence_curator`: collect and structure evidence without writing prose or
  developing the theory.
- `critical_reviewer`: challenge claims and identify unsupported
  generalization without directly rewriting the book.

Use them only when the user explicitly requests evidence collection,
delegation, formal review, or named agent use. Do not spawn them for small edits
or ordinary conversation. When used together, they may work independently, but
the main task must wait for both and reconcile their results.

Subagents must not write this repository or any source repository. In
particular, treat these external evidence sources as read-only:

- `/Users/macsun/lessismore`
- `/Users/macsun/Documents/AI_DEV_OS_Evolve`

Do not commit, checkout, stash, clean, format, or otherwise mutate either
external repository while gathering evidence.

## 6. Formal Chapter Revision Workflow

1. Route the chapter material as exploratory writing, source note, conceptual
   review, or formal evidence work.
2. If no formal trigger applies, state the model as a proposal, test its
   definitions and counterexamples, and write without allocating a Claim ID or
   Receipt.
3. If a formal trigger applies, select no more than three core Claims, allocate
   Claim IDs, and register them in the Claim Ledger.
4. Explicitly invoke `evidence_curator` when evidence collection is requested.
5. Persist accepted source findings as Evidence Receipts.
6. Explicitly invoke `critical_reviewer` for formal falsification review.
7. Keep, narrow, split, or withdraw each formal Claim.
8. Write the accepted logic and evidence-bearing working draft under
   `OptimizedDocs/`, using natural-language evidence boundaries rather than
   internal status labels.
9. After explicit Human authorization for the polishing stage, derive the
   reader-facing chapter under `PolishedDocs/`. Change voice and structure
   there; do not silently change the accepted claim scope or object model.
10. Record the user's Human disposition in both the Receipt and Claim Ledger.
11. If a conclusion affects AI Game Dev OS, prepare a separate feedback
   proposal; do not directly edit the external OS repository without a new
   request.

## 7. Human Authority

The human author retains final authority over direction, lived experience,
aesthetics, voice, and whether a claim belongs in the book. Agent output is
analysis and evidence support, not a substitute for that decision.

## 8. Bilingual Terminology

- Treat English technical terms as stable identifiers, not decorations.
- At the first formal definition of a core, coined, ambiguous, or
  book-specific English term, add a concise Chinese semantic explanation.
- Explain the role the term plays in this book; do not add a literal
  translation that contributes no meaning.
- Do not repeat the Chinese parenthetical on every later occurrence.
- Keep code, schemas, identifiers, paths, command names, and status enum values
  in English. Define enum meanings once in the surrounding prose or table.
- Familiar engineering names such as Git, Commit, Runtime, API, and Worktree do
  not require repeated parenthetical translation.
- When an English principle sentence is worth preserving, follow its first
  occurrence with a Chinese semantic restatement. Do not force the restatement
  inside the English sentence.
- Apply the same chosen Chinese explanation across chapters. If the meaning
  changes, state the scoped difference explicitly instead of silently changing
  the translation.
