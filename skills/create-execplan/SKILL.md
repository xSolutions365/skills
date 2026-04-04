---
name: "create-execplan"
description: "Create or update a structured execution-plan package with a living ExecPlan and derived runtime input. USE WHEN create-execplan skill is requested."
---

# Workflow

### Step 0: Preflight and scaffold

- **Purpose**: Establish the caller project root, resolve the helper runtime, and scaffold authoring artifacts.
- **When**: Run first.
- Use the skill-local runtime resolver and scaffold the plan package under the caller project root, including the phase manifest/result files and the intermediate research/design/structure artifacts.
- Keep the initial brief design parent-owned and iterative, keep the parent skill-running agent as the only user-facing layer, and normalize approvals and checkpoint results into workspace artifacts before launching the next phase.
- Preserve required language and explicit specificity from the source, do not introduce optionality or fallback wording, and ask for clarification instead of silently inferring missing decisions.
- Workflow: [references/step-0-preflight-workflow.md](references/step-0-preflight-workflow.md)

### Step 1: Capture and freeze requirements

- **Purpose**: Produce a user-confirmed requirement set before context analysis.
- **When**: Run after Step 0 and before Step 2.
- Run iterative clarification rounds in the parent agent, write the confirmed freeze artifacts, and stop for explicit user confirmation before any subagent planning phase begins.
- Workflow: [references/step-1-intake-freeze-workflow.md](references/step-1-intake-freeze-workflow.md)

### Step 2: Build and approve the planning brief

- **Purpose**: Convert the frozen requirements into one approved planning contract for later subagent phases.
- **When**: Run only after Step 1 confirmation.
- Build `workspace/planning-brief.md`, stop for explicit user approval, and do not start any subagent synthesis phase until that brief is approved.
- Workflow: [references/step-2-planning-brief-workflow.md](references/step-2-planning-brief-workflow.md)

### Step 3: Produce planning artifacts and the Context Pack

- **Purpose**: Complete the upstream synthesis phases and fold them into the durable Context Pack.
- **When**: Run after Step 2.
- Run `prepare -> worker -> apply` for research questions, research, design, structure, and context-pack using only the approved planning brief plus staged artifacts.
- Workflow: [references/step-2-context-pack-workflow.md](references/step-2-context-pack-workflow.md)

### Step 4: Draft and review the ExecPlan

- **Purpose**: Turn confirmed context into a reviewable ExecPlan draft and iterate until approval.
- **When**: Run after Step 3.
- Resolve surfaced blockers, generate the draft through the worker packet flow, and stop for explicit draft approval before finalization.
- Before any user-facing approval gate, run the skeptical translation-validation check and resolve findings before surfacing the candidate artifact.
- Workflow: [references/step-3-draft-review-workflow.md](references/step-3-draft-review-workflow.md)

### Step 5: Finalize the approved ExecPlan

- **Purpose**: Normalize the approved draft into the canonical living execution document.
- **When**: Run only after Step 4 approval.
- Keep execution details in the ExecPlan, keep repo/context inventories in the Context Pack, and generate the derived runtime input from the approved `execplan.md`.
- Workflow: [references/step-4-finalize-execplan-workflow.md](references/step-4-finalize-execplan-workflow.md)

### Step 6: Run the readiness audit

- **Purpose**: Verify the package is self-contained, consistent, and handoff-ready.
- **When**: Run after Step 5 and repeat until all checks pass.
- Validate the Context Pack, ExecPlan, generated runtime input, and the upstream planning artifacts using the resolved Python runtime.
- Workflow: [references/step-5-readiness-audit-workflow.md](references/step-5-readiness-audit-workflow.md)

### Step 7: Complete the handoff checklist

- **Purpose**: Enforce the final review gate before handoff.
- **When**: Run only after Step 6 passes.
- Record checklist results and do not hand off while any required plan gate is failing.
- Workflow: [references/step-6-checklist-workflow.md](references/step-6-checklist-workflow.md)

## Output

### Result Format

- Write or update the plan package under the caller project root, including the Context Pack, `execplan.md`, generated runtime input, and required phase artifacts.
- Report the approval state, audit/checklist status, and the created or updated paths needed for handoff.
- Do not hand off partial artifacts while any required gate is failing.
