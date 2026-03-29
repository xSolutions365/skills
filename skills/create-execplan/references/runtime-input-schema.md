# Runtime Input Schema

`workspace/execplan-runtime-input.json` is the machine-readable companion artifact for tooling. It is generated from `execplan.md` and must stay narrower than the markdown plan while remaining explicit enough for a packet-only executor.

## Top-level fields

- `schemaVersion`
- `generated`
- `editPolicy`
- `generatedAt`
- `sourceExecplan`
- `requirements`
- `tasks`

Current canonical schema version: `4.0`.

## Derivation rules

- `requirements` come from `## Requirements Freeze`.
- `tasks` come from the structured `## Task Table (single source of truth)`.
- `sourceExecplan` should be repo-relative for in-repo plan packages and absolute only when the source plan is genuinely external.
- `commands` come from the task row itself, not from late inference at harness runtime.
- Brownfield source plans are expected to be packet-ready before rendering: `Code` rows should already carry concrete edit targets, supporting context should remain read-only navigation, and executable rows should already name the exact command set the harness may run.
- No plan-level logs, decisions, findings, or standalone verification inventories belong in the runtime artifact.
- No policy blocks may be injected into the runtime artifact unless they are explicitly authored in the source ExecPlan.

## Task shape

Each task object must contain only derived execution structure:

- `taskRef`
- `status`
- `phaseNumber`
- `taskNumber`
- `type`
- `requirementIds`
- `editTargets`
- `supportingContextAnchors`
- `commands`
- `expectedOutput`
- `action`

## Packet executability rules

- `editTargets` are the files the executor is expected to modify for that task.
- `supportingContextAnchors` are read-only anchors that provide local context and do not imply edit permission.
- `commands` are the only task-local shell commands permitted for the task.
- `expectedOutput` must describe an observable completion signal and must not be a placeholder.
- Runtime tasks must be executable packet work; standalone onboarding or human-only rows do not belong in the runtime artifact.
- In-repo anchors should stay repo-relative so the package can be replayed in a fresh worktree without localization.
- A brownfield `Code` task that cannot name concrete `editTargets` is under-scoped and should be blocked during planning rather than deferred to execution.

## Canonical example

- Canonical source ExecPlan: [../examples/canonical/execplan.md](../examples/canonical/execplan.md)
- Canonical runtime input example: [../examples/canonical/workspace/execplan-runtime-input.json](../examples/canonical/workspace/execplan-runtime-input.json)
- Project-mode differences are documented in [step-2-context-pack-workflow.md](step-2-context-pack-workflow.md).
