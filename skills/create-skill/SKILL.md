---
name: "create-skill"
description: "Create or update skills through a deterministic, self-contained template workflow with natural-language validation checkpoints. USE WHEN you need portable skill authoring without repo-specific tooling."
---

# Create Skill

Create skill files through a deterministic workflow that is fully self-contained within this skill directory.

- Use this when you need to create or update a skill without relying on repo-local CLIs or scripts.
- Use this when you need predictable outputs with explicit approval checkpoints.
- Use this when validation must be performed by an LLM using a written checklist rather than tool-specific lint commands.

## Workflow

Use this section for step context only. Keep detailed mechanics in the referenced workflow files.

### Step 0: Preflight local context

- **Purpose**: Establish a deterministic working context rooted at this skill directory.
- **When**: Run once before any requirement capture.
- Treat the directory that contains `SKILL.md` as root for every path in this workflow.
- Confirm required references, templates, and the target relative output path before continuing.
- Workflow: [references/step-0-preflight-workflow.md](references/step-0-preflight-workflow.md)

### Step 1: Capture requirements and freeze intent

- **Purpose**: Capture complete requirements before drafting outputs.
- **When**: Run after Step 0 and before payload drafting.
- Capture every required field from `references/payload-schema.md`.
- **STOP** and ask the user for confirmation and wait for the response: "Are the requirements complete and frozen for payload drafting?"
- End the turn immediately after asking for confirmation.
- Workflow: [references/step-1-requirements-workflow.md](references/step-1-requirements-workflow.md)

### Step 2: Build and approve payload contract

- **Purpose**: Convert requirements into one deterministic source-of-truth payload.
- **When**: Run only after Step 1 approval.
- Build the payload using `references/payload-schema.md` and resolve all numbering, path, and link constraints.
- **STOP** and ask the user for confirmation and wait for the response: "Is this payload approved as the source of truth for preview and generation?"
- End the turn immediately after asking for confirmation.
- Workflow: [references/step-2-payload-workflow.md](references/step-2-payload-workflow.md)

### Step 3: Preview generated output

- **Purpose**: Review deterministic output before any file write.
- **When**: Run after payload approval and before validation or generation.
- Build preview content from [assets/templates/skill-output-template.md](assets/templates/skill-output-template.md) and [assets/templates/reference-workflow-template.md](assets/templates/reference-workflow-template.md).
- Present a file-by-file preview, including YAML-safe `SKILL.md` frontmatter, before any generation step.
- Workflow: [references/step-3-preview-workflow.md](references/step-3-preview-workflow.md)

### Step 4: Validate preview with checklist

- **Purpose**: Apply a natural-language validation gate to the preview before writing files.
- **When**: Run immediately after Step 3 and repeat until the preview passes.
- Evaluate the preview using `references/validation-checklist.md` and return a binary `PASS` or `FAIL` with evidence and corrective actions.
- Do not write files while any checklist item is failing.
- Workflow: [references/step-4-validation-workflow.md](references/step-4-validation-workflow.md)

### Step 5: Generate files and revalidate

- **Purpose**: Write the approved files and confirm the written result still passes the checklist.
- **When**: Run only after Step 4 returns `PASS`.
- Write files exactly as approved, then rerun the validation checklist against the written files before handoff.
- If revalidation fails, return to Step 2, Step 3, or Step 4 instead of handing off partial output.
- Workflow: [references/step-5-generate-workflow.md](references/step-5-generate-workflow.md)
