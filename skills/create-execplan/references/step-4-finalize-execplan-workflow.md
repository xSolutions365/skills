# Step 4 Workflow: Finalize the approved ExecPlan

## Objective

Normalize the approved draft into the canonical living execution document and generate the derived runtime input from the approved `execplan.md`.

## Required actions

1. Confirm Step 3 approval is recorded in `workspace/draft-review.md` and the latest checkpoint state has been normalized into `workspace/phase-result.json`.
2. Finalize `execplan.md` against [execplan-template.md](execplan-template.md).
3. Keep information placement aligned with [information-placement.md](information-placement.md):
   - ExecPlan owns tasks, task-local commands, progress, decisions, findings, and scenario verification coverage.
   - Context Pack owns shared verification posture, evidence traceability, and code-map context.
4. Ensure the top metadata references the generated runtime artifact:
   - `<artifact-root>/workspace/execplan-runtime-input.json`
5. Ensure the task table is fully structured:
   - `Req IDs`
   - `Edit Targets`
   - `Supporting Context Anchors`
   - `Commands`
   - `Expected Output`
   - `Action`
6. Ensure every runtime task is packet-executable:
   - `Code` tasks name concrete `Edit Targets`
   - `Supporting Context Anchors` does not hide edit scope
   - `Commands` is explicit when shell execution is required
   - the row can be executed from the row plus its listed supporting context anchors without additional discovery
   - standalone onboarding or human-only rows do not appear in the task table
   - in-repo anchors remain repo-relative
7. Ensure dependency preflight rows are complete for required external tools or libraries.
8. Ensure `Test Plan` remains scenario-focused BDD coverage with executable evidence commands and valid `Task Ref` mappings.
9. Generate or refresh the machine-readable runtime artifact using the standard runtime contract from [runtime-resolution.md](runtime-resolution.md) and the schema in [runtime-input-schema.md](runtime-input-schema.md).
10. Do not introduce new discovery or new requirements in Step 4. Route blockers back to Step 3 and stop when approval is needed.
11. If a row still needs search, inference, or missing command context, split and tighten it before finalization.

## Done when

- `execplan.md` is approved against the new lean contract.
- `workspace/execplan-runtime-input.json` is regenerated from the approved `execplan.md`.
- Task packets are explicit enough to satisfy a packet-only harness without implicit discovery.
- The runtime artifact remains derived structure only and does not become a second plan.
