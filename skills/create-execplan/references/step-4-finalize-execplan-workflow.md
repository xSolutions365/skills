# Step 4 Workflow: Finalize the approved ExecPlan

## Objective

Normalize the approved draft into the canonical living execution document and generate the derived runtime input from that finalized structure.

## Required actions

1. Confirm Step 3 approval is recorded in `workspace/draft-review.md`.
2. Finalize `execplan.md` against [execplan-template.md](execplan-template.md).
3. Keep information placement aligned with [information-placement.md](information-placement.md):
   - ExecPlan owns tasks, progress, decisions, findings, and scenario verification coverage.
   - Context Pack owns verification posture, command inventory, evidence traceability, and code-map context.
4. Ensure the top metadata references the generated runtime artifact:
   - `<artifact-root>/workspace/execplan-runtime-input.json`
5. Ensure the task table is fully structured:
   - `Req IDs`
   - `File Anchors`
   - `Command`
   - `Expected Output`
   - `Action`
6. Ensure dependency preflight rows are complete for required external tools or libraries.
7. Ensure `Test Plan` remains scenario-focused BDD coverage with executable evidence commands and valid `Task Ref` mappings.
8. Generate or refresh the machine-readable runtime artifact using the standard runtime contract from [runtime-resolution.md](runtime-resolution.md) and the schema in [runtime-input-schema.md](runtime-input-schema.md).
9. Do not introduce new discovery or new requirements in Step 4. Route blockers back to Step 3 and stop when approval is needed.

## Done when

- `execplan.md` is finalized against the new lean contract.
- `workspace/execplan-runtime-input.json` is regenerated from the finalized ExecPlan.
- The runtime artifact remains derived structure only and does not become a second plan.
