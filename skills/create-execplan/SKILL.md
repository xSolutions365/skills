---
name: "create-execplan"
description: "Create or update a structured execution-plan package with a living ExecPlan and derived runtime input. USE WHEN you need a deterministic implementation handoff."
---

# Create ExecPlan

Create a structured plan package that separates durable context, living execution state, and derived runtime input for tooling.

- Use this when planning must be deterministic, auditable, and updated in place.
- Use this when the plan will be handed to a lower-reasoning implementer that needs explicit task rows and traceability.
- Use this when the change requires a Context Pack plus a living ExecPlan rather than a one-off markdown note.

## Workflow

Use this section for step context only. Keep detailed mechanics in the referenced workflow files.

### Step 0: Preflight and scaffold

- **Purpose**: Establish the caller project root, resolve the helper runtime, and scaffold authoring artifacts.
- **When**: Run first.
- Use the skill-local runtime resolver and scaffold the plan package under the caller project root.
- Workflow: [references/step-0-preflight-workflow.md](references/step-0-preflight-workflow.md)

### Step 1: Capture and freeze requirements

- **Purpose**: Produce a user-confirmed requirement set before context analysis.
- **When**: Run after Step 0 and before Step 2.
- Capture scope, constraints, research policy, and verification baseline, then stop for explicit user confirmation.
- Workflow: [references/step-1-intake-freeze-workflow.md](references/step-1-intake-freeze-workflow.md)

### Step 2: Build the Context Pack

- **Purpose**: Create the durable context artifact that removes repeat discovery.
- **When**: Run only after Step 1 confirmation.
- Complete the shared context requirements, select one project mode, and fill the Context Pack with verification posture and change-surface evidence.
- Workflow: [references/step-2-context-pack-workflow.md](references/step-2-context-pack-workflow.md)

### Step 3: Draft and review the ExecPlan

- **Purpose**: Turn confirmed context into a reviewable ExecPlan draft and iterate until approval.
- **When**: Run after Step 2.
- Resolve surfaced blockers, generate the draft, and stop for explicit draft approval before finalization.
- Workflow: [references/step-3-draft-review-workflow.md](references/step-3-draft-review-workflow.md)

### Step 4: Finalize the approved ExecPlan

- **Purpose**: Normalize the approved draft into the canonical living execution document.
- **When**: Run only after Step 3 approval.
- Keep execution details in the ExecPlan, keep repo/context inventories in the Context Pack, and generate the derived runtime input from the finalized plan.
- Workflow: [references/step-4-finalize-execplan-workflow.md](references/step-4-finalize-execplan-workflow.md)

### Step 5: Run the readiness audit

- **Purpose**: Verify the package is self-contained, consistent, and handoff-ready.
- **When**: Run after Step 4 and repeat until all checks pass.
- Validate the Context Pack, ExecPlan, and generated runtime input using the resolved Python runtime.
- Workflow: [references/step-5-readiness-audit-workflow.md](references/step-5-readiness-audit-workflow.md)

### Step 6: Complete the handoff checklist

- **Purpose**: Enforce the final review gate before handoff.
- **When**: Run only after Step 5 passes.
- Record checklist results and do not hand off while any required plan gate is failing.
- Workflow: [references/step-6-checklist-workflow.md](references/step-6-checklist-workflow.md)
