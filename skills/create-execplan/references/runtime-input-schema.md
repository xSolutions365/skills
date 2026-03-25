# Runtime Input Schema

`workspace/execplan-runtime-input.json` is the machine-readable companion artifact for tooling. It is generated from the finalized ExecPlan and must stay narrower than the markdown plan.

## Top-level fields

- `schemaVersion`
- `generated`
- `editPolicy`
- `generatedAt`
- `sourceExecplan`
- `requirements`
- `tasks`
- `verificationScenarios`

## Derivation rules

- `requirements` come from `## Requirements Freeze`.
- `tasks` come from the structured `## Task Table (single source of truth)`.
- `verificationScenarios` come from `## Test Plan`.
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
- `fileAnchors`
- `command`
- `expectedOutput`
- `action`

## Verification scenario shape

Each verification scenario object must contain:

- `scenarioId`
- `priority`
- `given`
- `when`
- `then`
- `evidenceCommand`
- `taskRefs`

## Golden example

- Source ExecPlan: [../examples/finalized-execplan.md](../examples/finalized-execplan.md)
- Expected runtime input: [../examples/expected-runtime-input.json](../examples/expected-runtime-input.json)
