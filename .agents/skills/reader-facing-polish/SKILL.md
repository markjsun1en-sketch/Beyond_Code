---
name: reader-facing-polish
description: Pilot the Human-authorized derivation or revision of Beyond Code chapter candidates under PolishedDocs from an explicitly accepted OptimizedDocs baseline. Use for reader-facing narrative restructuring, density reduction, and author-voice recovery while preserving claims, evidence, cases, object boundaries, and uncertainty. Do not use for new theory, evidence collection, original-source edits, or unsanctioned batch rewriting.
---

# Reader-facing Polish

Turn an accepted logic draft into a chapter that one engineering practitioner can read continuously, without creating a second source of truth.

This is pilot v0.1. Until the Human closes RR-039 Phase 3, use it only for the named chapter 12, 17, and 23 trials or for a separately authorized isolated evaluation. Do not infer that it is ready for whole-book expansion.

## Route Before Writing

Use this Skill only when the Human has authorized polishing a named chapter and both an explicitly accepted `OptimizedDocs/` logic baseline and its primary review record can be identified. If either is missing, stop and request logic-layer routing rather than judging the baseline stable yourself.

Do not start or continue the prose pass when it would require any of the following:

- a new or enlarged factual, causal, effect, trend, or generalization Claim;
- a changed definition, object owner, Authority boundary, Lifecycle relation, or Human Decision;
- a new external case fact, disputed project history, or changed case-study boundary;
- deletion of counterevidence, Shared Provenance, legal or safety limits, or a material unresolved question.

Route those items back to the main task for `OptimizedDocs/`, `RevisedResult/`, or `Evidence/` handling. Do not invoke `$evidence-receipt` merely because prose is being polished.

This Skill never performs external research or formal Evidence work. If the Human authorizes either, the main task must run it as a separate workflow, update the accepted logic／Evidence layer, and only then resume polishing. A private Source Map, case-role label, comparison note, or polished candidate is not Evidence.

## Read the Required Sources

Before editing a chapter:

1. read the repository `AGENTS.md` completely;
2. read the target `OptimizedDocs/` chapter and its primary `RevisedResult/` record;
3. read the corresponding original chapter, supplements, and only the Evidence needed to preserve facts, counterexamples, and limitations; if no standalone original chapter exists, use the relevant outline section and named source or supplement files;
4. read [references/chapter-polish-protocol.md](references/chapter-polish-protocol.md) and complete its private core Chapter Source Map plus only the conditional sections that apply;
5. use the accepted chapter 1 and chapter 6 candidates only to understand the permitted range of voices, never as structural templates.

Do not edit `OringinalDocs/`. Treat `/Users/macsun/lessismore` and `/Users/macsun/Documents/AI_DEV_OS_Evolve` as read-only. Unless a separate request changes scope, write only the named candidate under `PolishedDocs/`. For a separately authorized isolated evaluation, the protocol's outside-repository test path takes precedence; never copy that artifact into `PolishedDocs/` automatically.

## Choose a Narrative Center

The following are common narrative centers, not a closed taxonomy. Select a primary center when it helps the chapter make coherent tradeoffs, and use another source-grounded center when the material requires it:

- **author judgment**: a problem changed the author's interpretation;
- **technical model**: a concrete engineering conflict requires distinctions;
- **design hypothesis**: an unfinished problem motivates a testable candidate design;
- **comparison case**: an external case supplies a precedent, mechanism comparison, counterexample, or transfer test;
- **longitudinal case**: events across the author's projects constrain the theory.

Use secondary modes where they add necessary resistance or explanation. Do not force every chapter through the same sequence or give every chapter an external case.

## Rewrite Without Changing the Model

- Begin from a real reader problem, project tension, or judgment change rather than a definition inventory when the source permits it.
- When the sources contain a genuine judgment change, preserve the movement from observation to inadequate explanation, revised boundary, usable conclusion, and remaining uncertainty. Do not manufacture that movement in chapters whose material has a different shape.
- Keep macro navigation clear while allowing paragraph length, emphasis, examples, and section shape to vary with the material.
- Let Chinese carry the explanation and English preserve stable identifiers, following the repository bilingual terminology rules.
- Retain a Schema, table, Checklist, principle, or Anti-pattern when it adds operational, reference, or model-precision value. Preserve the Canonical owner expression and any consumer Bridge required for Model Fidelity even when prose overlaps its semantics.
- Use first person only when it is traceable to original material or a contemporaneous record. Never invent dialogue, emotion, chronology, or a moment of realization.
- Do not use AI-detector scores, word blacklists, forced informality, sentence-length randomization, or deliberate digressions as quality targets.

## Preserve Material Roles

- Treat an ongoing author project as a point-in-time longitudinal observation, not a completed success proof.
- For the author's own material, record `longitudinal case` as the narrative role and state whether the episode generates a question, constrains a theory, or exposes a boundary. The external-case role vocabulary below does not replace this provenance rule.
- Keep a Design Hypothesis visibly conditional. Preserve its premise, expected mechanism, main failure condition, and signal that could change the recommendation.
- Give every external case one primary role: `precedent`, `mechanism comparison`, `counterexample`, or `transfer test`. Add a secondary role only when it contributes a distinct constraint. State the source type, relevant difference, what the case can support, and what it cannot support.
- Treat a vendor or project team's first-party engineering record as the primary source for what that team reported or recorded at the time. It does not automatically prove the underlying runtime behavior, causal mechanism, effect, or general validity.
- Use textbook facilities for navigation and practice only. They must not flatten all chapters into the same micro-structure.

## Verify and Hand Back

Run all six checks in the protocol: Source, Epistemic, Model, Hypothesis, Case Role / Provenance, and Reader Fidelity.

The candidate must not expose Claim IDs, Receipt IDs, Git metadata, Coverage or Human Status, or disposition history. Express reader-relevant sources, scope, and limitations in natural language.

Create or revise the single canonical candidate path `PolishedDocs/第N章_主题_成书候选稿.md`; do not create parallel versions unless the Human asks. Report any issues routed out of the prose pass. Voice acceptance closes only that Human voice review. The file remains a reader-facing candidate unless the Human separately decides its logic, Evidence, and publication status; do not infer any acceptance from successful checks.
