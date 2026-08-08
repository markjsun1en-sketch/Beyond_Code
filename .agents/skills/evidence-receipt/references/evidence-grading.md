# Evidence Assessment Reference

Evidence strength is claim-dependent. Do not compress every source into a
single universal score.

## Match Evidence to the Claim

| Claim type | Preferred evidence | Insufficient on its own |
|---|---|---|
| Runtime behavior | Reproducible test, build, validator, runtime log, captured artifact, bound to a revision | Design document or completion statement |
| Code or architecture state | Versioned code, schema, contract, config, and relevant test | Roadmap or intended design |
| Historical sequence | Commit history, contemporaneous plan, handoff, issue, review, timestamped artifact | Later recollection without source binding |
| Historical decision | Contemporaneous human decision or authority record with stated scope | Agent summary of what the human probably meant |
| Experience or aesthetics | Human review, playtest, interview, or decision record | Machine check substituting for human judgment |
| Cross-project generalization | Multiple independent cases or a deliberately case-scoped claim | A single AI Game Dev OS or lessismore example |
| Recommendation | Stated objective, tradeoffs, evidence, alternatives, and failure modes | Description of current practice treated as necessity |

## Source Roles

- **Primary**: directly records the behavior, state, decision, or result in the
  claim.
- **Corroborating**: independently supports part of the same claim.
- **Contextual**: explains surrounding intent or chronology but does not prove
  the claim.
- **Counterevidence**: conflicts with, narrows, or supplies an alternative
  explanation for the claim.

A human review is primary for an experience or authority decision, but it is not
automatically primary for a runtime fact outside the review's stated scope.

## Coverage Status

- `verified`: the exact, appropriately scoped claim is directly supported by
  suitable primary evidence; material counterevidence has been addressed.
- `partial`: evidence supports only part of the claim, one case, or a narrower
  boundary than the wording asserts.
- `counterevidence`: available evidence materially conflicts with the claim;
  preserve both the claim and conflict for human review.
- `unsupported`: no suitable evidence was found. Absence of evidence is not
  proof that the claim is false.

## Git and Artifact Rules

- Record the current repository HEAD and worktree status separately from the
  commit that introduced or last changed a source.
- An uncommitted file may support a current-state observation, but not a claim
  about a historical milestone without an immutable source.
- A revision named inside a manifest is not necessarily the commit containing
  that manifest. Record both when relevant.
- If the repository is behind or ahead of its upstream, state that when it may
  affect completeness.
- Never clean, checkout, stash, fetch, pull, or otherwise mutate a source
  repository while collecting evidence.

## Codex Task Records

Use visible prompts, responses, tool calls, outputs, and resulting file changes.
Do not claim access to hidden chain-of-thought. A task summary is contextual or
corroborating evidence unless it points to a stronger primary artifact.

## Conflict and Uncertainty

Preserve conflicting sources. Explain whether the conflict comes from version,
scope, authority, timing, or interpretation. Use `unknown` rather than filling
missing metadata from memory.

