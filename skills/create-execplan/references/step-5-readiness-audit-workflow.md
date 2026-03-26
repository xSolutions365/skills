# Step 5 Workflow: Run the readiness audit

## Objective

Verify the plan package is self-contained, validator-clean, and ready for handoff.

## Required actions

1. Validate the Context Pack with `scripts/validate_context_pack.py` using the resolved runtime contract from [runtime-resolution.md](runtime-resolution.md).
2. Validate the ExecPlan with `scripts/validate_execplan.py` using the same resolved runtime.
3. Regenerate `workspace/execplan-runtime-input.json` from the finalized ExecPlan before declaring the package current.
4. Confirm the artifact layout matches [artifact-contract.md](artifact-contract.md).
5. Confirm the runtime artifact shape still matches [runtime-input-schema.md](runtime-input-schema.md).
6. Confirm the placement rules still match [information-placement.md](information-placement.md).
7. Fail the audit if any validator fails, if required confirmation evidence is missing, or if the runtime input is missing or stale.
8. For brownfield plans, fail the audit if any task row is still under-specified for packet-only execution.
9. Fail the audit if the runtime artifact still uses legacy packet fields such as `fileAnchors`, `command`, or `verificationScenarios`.
10. Fail the audit if any runtime row uses unsupported task kinds, standalone onboarding or human-only tasks, or absolute in-repo anchors.

## Done when

- `context-pack-validation.json` exists and reports `status: pass`.
- `execplan-validation.json` exists and reports `status: pass`.
- `workspace/execplan-runtime-input.json` exists and matches the finalized ExecPlan structure.
