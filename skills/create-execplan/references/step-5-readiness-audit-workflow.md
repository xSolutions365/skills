# Step 6 Workflow: Run the readiness audit

## Objective

Verify the plan package is self-contained, validator-clean, and ready for handoff.

## Required actions

1. Validate the Context Pack with `scripts/validate_context_pack.py` using the resolved runtime contract from [runtime-resolution.md](runtime-resolution.md).
2. Validate the ExecPlan with `scripts/validate_execplan.py` using the same resolved runtime.
3. Validate the upstream planning artifacts with `scripts/validate_plan_rubric.py`.
4. Regenerate `workspace/execplan-runtime-input.json` from the approved `execplan.md` before declaring the package current.
5. Confirm the artifact layout matches [artifact-contract.md](artifact-contract.md).
6. Confirm the runtime artifact shape still matches [runtime-input-schema.md](runtime-input-schema.md).
7. Confirm the placement rules still match [information-placement.md](information-placement.md).
8. Fail the audit if any validator fails, if required confirmation evidence is missing, or if the runtime input is missing or stale.
9. For brownfield plans, fail the audit if any task row is still under-specified for packet-only execution.
10. Fail the audit if the runtime artifact still uses legacy packet fields such as `fileAnchors`, `command`, or `verificationScenarios`.
11. Fail the audit if any runtime row uses unsupported task kinds, standalone onboarding or human-only tasks, or absolute in-repo anchors.
12. Fail the audit if the planning rubric detects missing phase artifacts, unresolved assumptions, biased design output, missing structure output, weak smoke proof, or missing approval evidence.

## Done when

- `context-pack-validation.json` exists and reports `status: pass`.
- `execplan-validation.json` exists and reports `status: pass`.
- the rubric validator reports `status: pass`
- `workspace/execplan-runtime-input.json` exists and matches the approved `execplan.md` structure.
