---
name: showcase-publish
description: Synchronize Beyond Code reader-facing manuscript or mechanism-figure changes to its existing Showcase, verify completeness and publish. Use after chapter, figure, caption, export or Showcase reader changes, or when asked to reconcile online freshness. Editorial-only notes and explicit local-only work do not require deployment.
---

# Beyond Code Showcase publication

Read [the repository runbook](../../../Showcase/README.md) for commands and completion criteria. The repository root is three levels above this skill directory. The author’s standing authorization is in [AGENTS.md §9](../../../AGENTS.md); do not add another routine publishing confirmation. Explicit no-publish/local-only instructions override it.

Use the currently installed **Sites** skill for source checkout, credentials, packaging and native publication. Discover its current location/tools instead of hardcoding a plugin version. Keep the exact Site identity and current audience; `Showcase/publication.json` names the existing Site. Credentials stay in tool memory/stdin only.

The maintained entry point is `tools/showcase_workflow.py`:

1. `status --online` establishes whether current inputs match the last verified release. A pending result is work to reconcile, not permission to rewrite old records.
2. Open the same Site’s latest source with the Sites workflow. If figure source/title/caption/export checks fail, identify the owning phase manifest, regenerate only affected figures with the existing renderer and its `--batch`/`--figures` options, inspect the result and recheck. Never patch hashes to make stale images pass.
3. `prepare --checkout <path>` synchronizes, rebuilds and validates all chapters and figures. It freezes current source/snapshot/output fingerprints. Source edits after this point require preparation again.
4. Review actual rendered pages in the supported browser: affected prose and figure, a real search hit including a long code/table target where relevant, desktop and phone widths. Keep actual screenshots and a browser review tied to the prepared output fingerprint. Browser limitations are reported as unverified, never filled in as passing.
5. Use the Sites source helper to push/package the exact prepared source. Run `check --checkout <path>` after push and before save/deploy. Save the helper’s exact commit/archive, deploy the returned version with the tool appropriate to the existing audience, and retain actual version/deployment JSON (without credentials).
6. Review affected interactions at the production URL after deployment; record `production: true`, the actual URL and saved version ID in the browser review only after observing success. `finish` consumes those tool results and that review, then reads back every published HTML/JSON/CSS/JS/SVG/PNG asset. It records `verified` only on success; failures retain `deployed_unverified`. Resume the existing version/deployment rather than creating duplicate Sites or blind retries.
7. `status --online` must report `current` before claiming that current book changes are online. Final response gives the URL/version, actual checks and any remaining gap.

This is a task-completion workflow. It does not start a background watcher or scheduled automation. Do not modify book arguments, evidence dispositions, original documents or unrelated repositories to satisfy publication checks. Keep private editorial paths and evidence records outside the public output.
