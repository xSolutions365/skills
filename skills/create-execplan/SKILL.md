---
name: create-execplan
description: Create a two-part execution plan (Context Pack + ExecPlan) optimized for low-reasoning executors and living-document tracking. USE WHEN the user calls for the creation or update of an execplan.
---

# Create ExecPlan

Create a two-artifact plan package that turns validated context into an executable, update-in-place implementation plan.

- Use this when planning must be deterministic and auditable.
- Use this when implementation will be delegated to a low-reasoning executor that needs explicit, unambiguous steps.
- Use this when the plan must include context discovery output (greenfield or brownfield) and then drive tracked execution as a living document.

## Workflow

Use this section for step context only. Use each step reference for detailed execution.
Treat the directory containing `SKILL.md` as the skill root for bundled workflow resources (`scripts/`, `references/`, `templates/`). Resolve artifact output paths from the caller project root instead.

```bash
python3 scripts/scaffold_execplan.py --artifact-root ".plan/create-execplan/<timestamp>"
```

Reference baseline: [references/openai-codex-exec-plans.md](references/openai-codex-exec-plans.md).

### Step 0: Preflight + scaffold artifacts

- Establish deterministic artifact root and scaffold outputs.
- Details: [references/step-0-preflight.md](references/step-0-preflight.md).

### Step 1: Intake + freeze requirements

- Run clarifying rounds to derive concrete requirements.
- Hard stop: always play back captured inputs and require explicit user confirmation on `Requirements Freeze` before proceeding, even when the user provides drafts or artifacts.
- **STOP** and @ASK_USER_CONFIRMATION, then end the turn immediately before Step 2.
- Do not treat the initial task request as requirements-freeze confirmation.
- Capture online research permissions and recency expectations before Step 2.
- Details: [references/step-1-intake-freeze.md](references/step-1-intake-freeze.md).

### Step 2: Build Context Pack

- Run Step 2 core guidance first, then branch by project mode.
- Greenfield path: option comparison, established library reuse, recency-backed recommendation.
- Brownfield path: deep existing-code analysis, line-anchored change surface, integration risk control.
- Hard stop: when brownfield has no existing verification and the user declines change-scoped verification onboarding, stop and escalate to the user before drafting.
- **STOP** and @ASK_USER_CONFIRMATION when the brownfield-no-verification path is blocked, then end the turn immediately.
- Details: [references/step-2-context-pack.md](references/step-2-context-pack.md).

### Step 3: Clarify + draft review loop

- Resolve any new questions or blockers surfaced by Context Pack formation before draft creation; if none surfaced, proceed directly.
- Generate a draft `execplan.md`, then run multi-round user review and amend loops until the draft is explicitly approved.
- Hard stop: do not proceed to Step 4 until surfaced blockers are resolved and the user confirms the reviewed draft.
- **STOP** and @ASK_USER_CONFIRMATION, then end the turn immediately before Step 4 finalization.
- Details: [references/step-3-draft-review.md](references/step-3-draft-review.md).

### Step 4: Finalize approved ExecPlan

- Convert the approved draft into a handoff-ready living execution document and normalize required sections.
- Keep tasks explicit with dependency preflight and verification gates aligned to the selected scenario.
- Hard stop: do not introduce new discovery or requirement changes in Step 4; return to Step 3 when new clarifications are required.
- **STOP** and @ASK_USER_CONFIRMATION when Step 4 encounters new blockers or unresolved clarifications, then end the turn immediately.
- Details: [references/step-4-execplan.md](references/step-4-execplan.md).

### Step 5: Run readiness audit

- Verify self-containment, success-criteria coverage, and executor-readiness.
- Fail if any task requires undefined discovery.
- Details: [references/step-5-readiness-audit.md](references/step-5-readiness-audit.md).

### Step 6: Complete required review checklist

- Hard stop: do not hand off until checklist `P*` checks pass and `context-pack-validation.json` reports `status: pass`.
- Details: [references/step-6-checklist.md](references/step-6-checklist.md).
