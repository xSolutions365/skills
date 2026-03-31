# Artifact Contract

The `create-execplan` package is an artifact set, not a single markdown file.

Reference baseline: this document and the retained workflow references are the canonical artifact contract for the skill.

## Canonical artifact layout

Root artifacts:

- `context-pack.md`
- `execplan.md`
- `review-checklist.md`
- `context-pack-validation.json` (generated during readiness audit)
- `execplan-validation.json` (generated during readiness audit)

Workspace artifacts:

- `workspace/context-discovery.md`
- `workspace/context-evidence.json`
- `workspace/context-codemap.md`
- `workspace/requirements-freeze.md`
- `workspace/planning-brief.md`
- `workspace/draft-review.md`
- `workspace/phase-manifest.json`
- `workspace/phase-result.json`
- `workspace/phases/<phase>/phase-worker-input.json` (generated during `prepare` for subagent phases)
- `workspace/phases/<phase>/phase-worker-result.json` (captured before `apply`; internal audit artifact)
- `workspace/research-questions.md`
- `workspace/research-findings.md`
- `workspace/design-options.md`
- `workspace/structure-outline.md`
- `workspace/execplan-runtime-input.json` (generated after finalization; do not edit)

## Rules

- `execplan.md` is the living human document.
- `context-pack.md` is the durable context artifact.
- `workspace/phase-manifest.json` is the deterministic phase-routing contract for fresh-session execution.
- `workspace/phase-result.json` is the latest normalized checkpoint result surfaced back to the parent agent.
- `workspace/planning-brief.md` is the user-approved source of truth for upstream planning subagent phases.
- `workspace/phases/<phase>/phase-worker-input.json` is the staged worker packet used to launch one fresh worker subagent.
- `workspace/phases/<phase>/phase-worker-result.json` is the raw per-phase worker handoff captured for audit and validation.
- `workspace/execplan-runtime-input.json` is derived from `execplan.md` and must not be user-edited.
- The runtime input artifact is not generated during scaffold.
- The old artifact name `execplan-task-packets.json` is obsolete and must not appear in the rewritten skill.

## Canonical example

- Canonical example package index: [../examples/canonical/README.md](../examples/canonical/README.md)
- Canonical Context Pack example: [../examples/canonical/context-pack.md](../examples/canonical/context-pack.md)
- Canonical ExecPlan example: [../examples/canonical/execplan.md](../examples/canonical/execplan.md)
- Live repro fixture package index: [../examples/live-repro-green/README.md](../examples/live-repro-green/README.md)
- Project-mode differences are documented in [step-2-context-pack-workflow.md](step-2-context-pack-workflow.md) rather than a second full example package.
