---
name: adaptive-prose
description: Draft or redraft context-bound prose using explicit style presets and judgment-based validation. USE WHEN the user needs stronger prose for a specific audience, or needs existing text redrafted without drifting from the source intent.
---

# Adaptive Prose

Draft or redraft prose with an explicit preset, a context-bound writing style, and a human-judged review gate instead of scripted checkers.

- Use this when the task is writing new prose from context, not just outlining.
- Use this when the task is improving existing prose while preserving meaning or audience fit.
- Use this when preset selection must be explicit through `--preset` and validated before drafting.
- Accepted canonical presets and shorthand selectors:
  - `operator-brief`: `operator`, `brief`
  - `technical-deep-dive`: `technical`, `deep-dive`
  - `narrative-explainer`: `narrative`, `explainer`
  - `executive-decision-brief`: `executive`, `exec`, `exec-summary`
  - `surgical-redraft`: `surgical`
  - `voice-shift-redraft`: `voice-shift`

## Workflow

### Step 0: Preflight preset, mode, and output target

- **Purpose**: Confirm the selected preset, classify the run as create or redraft, and verify enough input exists to proceed.
- **When**: Run once at the start of each request.
- Require a valid `--preset`, identify whether the job is create or redraft, and set `@ARTIFACT_ROOT` plus target output path before any drafting.
- Workflow: [references/step-0-preflight-workflow.md](references/step-0-preflight-workflow.md)

### Step 1: Load universal and preset guidance

- **Purpose**: Translate the chosen preset into live drafting rules for the current task.
- **When**: Run after preflight inputs are complete.
- Read the universal prose guide, the preset-selection guide, the chosen preset guide, and the redraft-integrity guide when source text must be preserved.
- Workflow: [references/step-1-load-guidance-workflow.md](references/step-1-load-guidance-workflow.md)

### Step 2: Draft or redraft the prose

- **Purpose**: Produce one coherent piece of prose that matches the preset and the task context.
- **When**: Run after guidance is loaded and the output target is confirmed.
- Write from the current context rather than from generic templates, and keep structure, tone, and claim strength consistent with the selected preset.
- Workflow: [references/step-2-draft-or-redraft-workflow.md](references/step-2-draft-or-redraft-workflow.md)

### Step 3: Apply natural-language review and revision

- **Purpose**: Use judgment-based review questions to catch vagueness, drift, and weak prose before finalizing.
- **When**: Run immediately after Step 2 and repeat until the draft is genuinely ready.
- Apply the prose review guide as a binary pass/fail gate, with special emphasis on factual parity and commitment parity during redrafts.
- Workflow: [references/step-3-review-and-validation-workflow.md](references/step-3-review-and-validation-workflow.md)

### Step 4: Finalize and save output

- **Purpose**: Persist the approved prose and capture the preset used for downstream workflows.
- **When**: Run only after Step 3 passes.
- Save the final prose to the agreed artifact-root-relative path and note the preset and mode used for the run.
- Workflow: [references/step-4-finalize-output-workflow.md](references/step-4-finalize-output-workflow.md)
