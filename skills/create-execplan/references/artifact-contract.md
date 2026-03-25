# Artifact Contract

The `create-execplan` package is an artifact set, not a single markdown file.

Reference baseline: [openai-codex-exec-plans.md](openai-codex-exec-plans.md).

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
- `workspace/draft-review.md`
- `workspace/execplan-runtime-input.json` (generated after finalization; do not edit)

## Rules

- `execplan.md` is the living human document.
- `context-pack.md` is the durable context artifact.
- `workspace/execplan-runtime-input.json` is derived from the finalized ExecPlan and must not be user-edited.
- The runtime input artifact is not generated during scaffold.
- The old artifact name `execplan-task-packets.json` is obsolete and must not appear in the rewritten skill.

## Examples

- Finalized Context Pack example: [../examples/finalized-context-pack.md](../examples/finalized-context-pack.md)
- Finalized ExecPlan example: [../examples/finalized-execplan.md](../examples/finalized-execplan.md)
