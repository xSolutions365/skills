# Step 6 Workflow: Complete the handoff checklist

## Objective

Enforce the final review gate before the plan package is handed off.

## Required actions

1. Review the package using [review-checklist.md](review-checklist.md).
2. Record results in `<artifact-root>/review-checklist.md` using [review-checklist-template.md](review-checklist-template.md).
3. Confirm `context-pack-validation.json` exists and reports `status: pass`.
4. Confirm `execplan-validation.json` exists and reports `status: pass`.
5. Confirm `workspace/execplan-runtime-input.json` exists and was regenerated from the approved `execplan.md`.
6. Confirm Step 1 and Step 3 checkpoint evidence exists in the workspace artifacts.
7. Resolve every failing `P*` check before handoff.

## Done when

- Checklist evidence is complete.
- All required `P*` checks are `pass`.
- The package is ready for handoff without unresolved audit failures.
