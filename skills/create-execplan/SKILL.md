---
name: "create-execplan"
description: "Create or update a structured execution-plan package with a living ExecPlan and derived runtime input. USE WHEN create-execplan skill is requested."
---

# Create ExecPlan

Create a structured plan package that separates durable context, living execution state, and derived runtime input for tooling.

- Use this when planning must be deterministic, auditable, and updated in place.
- Use this when the plan will be handed to a lower-reasoning implementer that needs explicit task rows and traceability.
- Use this when the change requires a Context Pack plus a living ExecPlan rather than a one-off markdown note.
- Keep initial brief design parent-owned and iterative, then run phase work through the deterministic controller plus fresh subagent workers once the planning brief is approved.
- Keep the parent skill-running agent as the only user-facing layer; normalize approvals and checkpoint results into workspace artifacts before launching the next phase.
- Before any user-facing approval gate, run the skeptical translation-validation check and resolve findings before surfacing the candidate artifact.

## Behavior Rules

- **NEVER** weaken required language into optional, advisory, deferred, or exploratory language unless the source explicitly does so.
- **NEVER** introduce optionality, fallback paths, or "may/should consider" wording where the user request or supplied artifact defines a required outcome.
- **ALWAYS** preserve action precision. If the source says `supersede`, `remove`, `fail closed`, `pin`, `verify before activation`, or similar lifecycle or control terms, keep that exact intent rather than replacing it with a looser synonym.
- **ALWAYS** preserve explicit specificity. If the source names concrete checks, tools, protocols, or artifacts, keep them explicit in the freeze unless the user explicitly approves abstraction.
- **NEVER** infer a missing decision, soften an ambiguity, or pick between plausible interpretations silently. Ask the user for clarification before freezing requirements.

## Workflow

### Step 0: Preflight and scaffold

- **Purpose**: Establish the caller project root, resolve the helper runtime, and scaffold authoring artifacts.
- **When**: Run first.
- Use the skill-local runtime resolver and scaffold the plan package under the caller project root, including the phase manifest/result files and the intermediate research/design/structure artifacts.
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
