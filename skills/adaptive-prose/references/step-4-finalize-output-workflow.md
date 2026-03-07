# Step 4 Workflow: Finalize and save output

## Objective

Persist the approved prose and record enough run context for downstream workflows to understand what was produced.

## Required actions

1. Save the approved draft to the confirmed output path under `@ARTIFACT_ROOT`.
2. Record the selected preset and whether the run was `create` or `redraft`.
3. If the calling workflow needs traceability, include a short note with:
   - preset used,
   - audience assumption,
   - any preserved constraints,
   - any material rewrite decision made during review.
4. Do not finalize any draft that still fails the review questions from [step-3-review-and-validation-workflow.md](step-3-review-and-validation-workflow.md).

## Done when

- The final prose is saved under `@ARTIFACT_ROOT`.
- The preset and mode used for the run are clear.
- No unresolved review failure remains.
