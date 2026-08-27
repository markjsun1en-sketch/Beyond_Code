---
name: evidence-receipt
description: Create or audit formal Evidence Receipts for repository-bound facts, cross-project generalizations, high-risk claims, or conclusions intended to change AI Game Dev OS. Do not use as a default gate for conceptual models, chapter structure, ordinary prose, or author experience.
---

# Evidence Receipt

Turn one bounded claim into a traceable record that another task or human can
inspect without trusting the writer's confidence.

## Route Before Capture

Use a formal Receipt when at least one condition applies:

- the Claim depends on precise Git history, runtime behavior, an artifact, or a
  contemporaneous decision;
- one project case is being generalized beyond its observed scope;
- the Claim states a concrete security, privacy, legal, IP, financial, or other
  high-risk fact;
- the conclusion will directly change AI Game Dev OS Workflow, Authority, or
  Runtime behavior;
- the Claim asserts an effect such as improved quality, speed, cost,
  reliability, or safety;
- material sources conflict, or the user requests formal evidence collection.

Do not create a Receipt by default for terminology, a candidate conceptual
model, chapter structure, explanatory analogy, ordinary prose, lived
experience, aesthetics, or a recommendation explicitly presented as a
proposal. Route those to the main writer for conceptual review using
definitions, counterexamples, alternatives, scope, and Human judgment.

If no formal trigger applies, do not allocate an ID, write a draft Receipt, or
label the proposal `unsupported`. Return the routing conclusion and stop the
formal workflow.

Receipt status constrains the exact Claim. It is not a publication gate and
does not determine whether a clearly labeled conceptual proposal may be
discussed in the book.

## Workflow

1. After routing confirms a formal Receipt is appropriate, require a Claim ID,
   exact Claim text, target chapter, and Claim type. If an ID is missing, use
   `PENDING` in a draft; only the main writer allocates permanent IDs.
2. Read `references/evidence-grading.md` before assessing coverage.
3. Resolve source identity before interpretation:
   - repository and project;
   - source path or artifact path;
   - branch and commit;
   - clean or dirty worktree;
   - relevant project or AI Game Dev OS version;
   - visible Codex task/thread identity when applicable.
4. Collect evidence appropriate to the claim type. Prefer primary artifacts
   over summaries, and cite only the smallest relevant portion.
5. Keep observable facts, contemporaneous judgments, retrospective inference,
   and current recommendations in separate sections.
6. Actively search for counterevidence and plausible alternative explanations.
7. Assign exactly one coverage status:
   `verified`, `partial`, `counterevidence`, or `unsupported`.
8. Copy `assets/evidence-receipt-template.md` and complete every field. Never
   delete an unknown field; write `unknown` and explain why it could not be
   resolved.
9. If authorized to write this repository, save the receipt as
   `Evidence/receipts/<receipt_id>__<claim_id>.md` and update
   `Evidence/claim-ledger.md`. Otherwise return the completed Markdown to the
   parent task.

## Identifier Rules

- Receipt: `ER-YYYYMMDD-NNN`.
- Numbered chapter claim: `CLM-CNN-NNN`, for example `CLM-C02-001`.
- Preface or appendix claim: `CLM-PREFACE-NNN` or `CLM-APP-X-NNN`.
- Cross-book structural claim: `CLM-OUTLINE-NNN`.

Never reuse an existing identifier.

## Boundaries

- Do not edit `OringinalDocs/` or `OptimizedDocs/` as part of evidence capture.
- Treat `/Users/macsun/lessismore` and
  `/Users/macsun/Documents/AI_DEV_OS_Evolve` as read-only evidence sources.
- Do not infer hidden reasoning from Codex tasks. Record only visible messages,
  tool activity, outputs, and file changes.
- Do not copy large artifacts into the book repository. Reference them in place.
- Do not convert one case study into a universal conclusion. Mark it `partial`
  unless the claim itself is explicitly case-scoped or corroborated.
- Leave `human_status` as `unreviewed` until the human author decides.
- Do not expose Claim IDs, Coverage Status, Human Status, or Receipt audit
  details in reader-facing prose unless the chapter itself teaches that
  evidence concept. Give the main writer a natural-language source and scope
  boundary instead.

## Final Check

Confirm that:

- every factual statement has a source location;
- commit identity and current worktree status are not conflated;
- the source supports the exact claim rather than an adjacent claim;
- contrary evidence and limitations are visible;
- the coverage status follows the definitions in the grading reference;
- the human decision has not been invented or inferred.
