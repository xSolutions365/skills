# Step 6: Complete required checklist

Objective: enforce final quality gate before plan handoff.

## Required actions

1. Review the plan using:
   - [review-checklist.md](review-checklist.md)
   - [review-checklist-template.md](review-checklist-template.md)
2. Record results for every `P*` and applicable `E*` check in `<artifact-root>/review-checklist.md` using `pass`/`fail`/`na` plus evidence.
3. Ensure `context-pack-validation.json` exists at `<artifact-root>/context-pack-validation.json` and reports `status: pass`.
4. Ensure `execplan-validation.json` exists at `<artifact-root>/execplan-validation.json` and reports `status: pass`.
5. Ensure `<artifact-root>/workspace/execplan-task-packets.json` exists and was regenerated from the finalized `execplan.md`.
6. Ensure Step 3 draft approval evidence exists in `<artifact-root>/workspace/draft-review.md`.
7. Ensure requirements-freeze confirmation exists in `<artifact-root>/workspace/requirements-freeze.md`.
8. Ensure Step 1 and Step 3 checkpoint records include:
   - checkpoint prompt text
   - user approval response excerpt recorded after the STOP request
9. Ensure smoke gate, dependency preflight, and Test Plan BDD scenario checks pass in checklist rows before handoff.
10. Resolve any failing `P*` checks before handoff.

## Hard gate

- Do not mark the plan ready until all `P*` checks are `pass`.
- Do not mark the plan ready when `context-pack-validation.json` is missing or not `status: pass`.
- Do not mark the plan ready when `execplan-validation.json` is missing or not `status: pass`.

## Done when

- Checklist is complete and all `P*` checks are `pass`.
