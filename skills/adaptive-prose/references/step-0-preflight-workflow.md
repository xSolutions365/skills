# Step 0 Workflow: Preflight preset, mode, and output target

## Objective

Confirm the selected preset, identify whether the job is create or redraft, and verify that enough input exists to produce a credible result.

## Required actions

1. Require `--preset` and reject the run if it is absent.
2. Confirm `--preset` is one of the allowed canonical values or shorthand selectors in [preset-selection-guide.md](preset-selection-guide.md).
3. Normalize any shorthand selector to its canonical preset name before continuing.
4. Set `@ARTIFACT_ROOT` for the run.
5. Confirm the target output path as an artifact-root-relative file such as `@ARTIFACT_ROOT/prose-output.md`.
6. Classify the run as:
   - `create` when the job is to generate new prose from context, or
   - `redraft` when the job is to improve existing text.
7. For `create`, confirm the minimum drafting inputs:
   - clear task or objective,
   - intended audience or reader type,
   - source context, notes, or constraints.
8. For `redraft`, confirm the minimum drafting inputs:
   - source text,
   - intended audience or retained audience,
   - any non-negotiable claims, constraints, or phrases to preserve.
9. If any required input is missing or the chosen preset does not fit the job, stop and clarify before proceeding.

## Done when

- `--preset` is present, valid, and normalized to a canonical preset name.
- The run is clearly classified as `create` or `redraft`.
- `@ARTIFACT_ROOT` and target output path are confirmed.
- Required inputs are sufficient for the selected mode.
