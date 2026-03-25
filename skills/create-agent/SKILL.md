---
name: "create-agent"
description: "Create portable agent files from a supplied YAML request or guided intake with explicit approval before generation. USE WHEN you need a reusable agent or subagent contract for a defined task."
---

# Create Agent

Create a reusable agent file set from either a supplied YAML request or a guided intake flow that freezes one contract before preview and generation.

- Use this when you need deterministic agent artifacts instead of a one-off prompt.
- Use this when the request may arrive as either structured YAML or natural-language requirements.
- Use this when generation must stop at a final contract review gate before any files are written.

## Resources

Read only the files needed for the current request.

### Core references

- Request schema: [references/agent-request-schema.md](references/agent-request-schema.md)
- Validation checklist: [references/validation-checklist.md](references/validation-checklist.md)

### Base templates

- System contract: [assets/templates/system-contract-template.md](assets/templates/system-contract-template.md)
- Task packet: [assets/templates/task-packet-template.md](assets/templates/task-packet-template.md)
- Verification checklist: [assets/templates/verification-checklist-template.md](assets/templates/verification-checklist-template.md)
- Subagent spec: [assets/templates/subagent-spec-template.md](assets/templates/subagent-spec-template.md)

### Role profiles

- Custom: [assets/templates/role-profiles/custom.md](assets/templates/role-profiles/custom.md)
- Implementer: [assets/templates/role-profiles/implementer.md](assets/templates/role-profiles/implementer.md)
- Operator: [assets/templates/role-profiles/operator.md](assets/templates/role-profiles/operator.md)
- Planner: [assets/templates/role-profiles/planner.md](assets/templates/role-profiles/planner.md)
- Researcher: [assets/templates/role-profiles/researcher.md](assets/templates/role-profiles/researcher.md)
- Reviewer: [assets/templates/role-profiles/reviewer.md](assets/templates/role-profiles/reviewer.md)
- Skeptical evaluator: [assets/templates/role-profiles/skeptical-evaluator.md](assets/templates/role-profiles/skeptical-evaluator.md)

## Workflow

Use this section for step context only. Keep detailed mechanics in the referenced workflow files.

### Step 0: Preflight local context

- **Purpose**: Confirm the skill root, local references/templates, and the target output path before request handling.
- **When**: Run first.
- Treat the directory that contains `SKILL.md` as the working root for every relative path in this workflow.
- Confirm the target relative output directory for generated agent files before any drafting.
- Workflow: [references/step-0-preflight-workflow.md](references/step-0-preflight-workflow.md)

### Step 1: Capture request source

- **Purpose**: Normalize YAML-driven and guided-intake requests into one intake path.
- **When**: Run after Step 0 and before contract drafting.
- Detect whether the user supplied YAML or needs structured intake.
- Ask only for missing or ambiguous required fields.
- Workflow: [references/step-1-capture-request-workflow.md](references/step-1-capture-request-workflow.md)

### Step 2: Build and freeze the agent contract

- **Purpose**: Convert the intake into one deterministic source-of-truth contract.
- **When**: Run only after Step 1 is complete.
- Normalize role, objective, deliverables, constraints, tools, approvals, memory, verification, and optional subagents into one contract.
- Apply role profiles as overlays only; explicit user inputs override profile defaults.
- **STOP** and ask the user for confirmation and wait for the response: "Is this agent contract approved as the source of truth for preview and generation?"
- End the turn immediately after asking for confirmation.
- Workflow: [references/step-2-freeze-agent-contract-workflow.md](references/step-2-freeze-agent-contract-workflow.md)

### Step 3: Preview generated files

- **Purpose**: Review the exact file package before any write.
- **When**: Run only after Step 2 approval.
- Build the preview in fixed file order and keep paths relative to the chosen output root.
- Preview system contract, task packet, verification checklist, and optional subagent specs.
- Workflow: [references/step-3-preview-package-workflow.md](references/step-3-preview-package-workflow.md)

### Step 4: Validate preview with checklist

- **Purpose**: Apply a binary natural-language validation gate to the preview.
- **When**: Run immediately after Step 3 and repeat until the preview passes.
- Evaluate the preview with the local checklist and reject vague or internally inconsistent contracts.
- Do not write files while any checklist item is failing.
- Workflow: [references/step-4-validate-preview-workflow.md](references/step-4-validate-preview-workflow.md)

### Step 5: Generate files and return links

- **Purpose**: Write the approved package, revalidate it, and hand back file links.
- **When**: Run only after Step 4 returns `PASS`.
- Write files exactly as approved, rerun the checklist against the written files, and return links instead of dumping full file contents.
- Workflow: [references/step-5-generate-workflow.md](references/step-5-generate-workflow.md)
