---
name: "create-skill"
description: "Create or update skills through route-specific templates and validation. USE WHEN you need portable skill authoring without repo-specific tooling."
---

# Workflow

### Step 0: Preflight local context

- **Purpose**: Establish a deterministic working context rooted at this skill directory.
- **When**: Run once before any route selection or requirement capture.
- Treat the directory that contains `SKILL.md` as root for every path in this workflow.
- Confirm required references, route-specific templates, and the target relative output path before continuing.
- Workflow: [references/step-0-preflight-workflow.md](references/step-0-preflight-workflow.md)

### Step 1: Classify skill template route

- **Purpose**: Select exactly one authoring route before gathering detailed requirements.
- **When**: Run after preflight and before payload drafting.
- Classify the request as `behaviour-guidance`, `simple-task:inline`, `simple-task:runbook-index`, or `multi-step-workflow`.
- **STOP** and ask the user for confirmation when the route is ambiguous or when more than one route would be valid.
- Workflow: [references/step-1-route-selection-workflow.md](references/step-1-route-selection-workflow.md)

### Step 2: Capture route-specific requirements

- **Purpose**: Capture only the fields required by the selected route and freeze intent before payload drafting.
- **When**: Run after route selection.
- Capture the shared fields and the selected route's required fields from `references/payload-schema.md`.
- **STOP** and ask the user for confirmation and wait for the response: "Are the route and requirements complete and frozen for payload drafting?"
- End the turn immediately after asking for confirmation.
- Workflow: [references/step-2-requirements-workflow.md](references/step-2-requirements-workflow.md)

### Step 3: Build and approve typed payload

- **Purpose**: Convert requirements into one deterministic route-specific source-of-truth payload.
- **When**: Run only after Step 2 approval.
- Build the payload using `references/payload-schema.md` and resolve all route, path, and link constraints.
- **STOP** and ask the user for confirmation and wait for the response: "Is this typed payload approved as the source of truth for preview and generation?"
- End the turn immediately after asking for confirmation.
- Workflow: [references/step-3-payload-workflow.md](references/step-3-payload-workflow.md)

### Step 4: Preview route-specific output

- **Purpose**: Review deterministic output before any file write.
- **When**: Run after payload approval and before validation or generation.
- Render only the files required by the selected route using the matching template under `assets/templates/`.
- Route templates: [behaviour guidance](assets/templates/behaviour-guidance-skill-template.md), [simple task](assets/templates/simple-task-skill-template.md), [simple task runbook index](assets/templates/simple-task-runbook-index-template.md), [multi-step workflow](assets/templates/multi-step-workflow-skill-template.md), [README](assets/templates/readme-template.md), [runbook reference](assets/templates/reference-runbook-template.md), and [workflow reference](assets/templates/reference-workflow-template.md).
- Present a file-by-file preview, including YAML-safe `SKILL.md` frontmatter, before any generation step.
- Workflow: [references/step-4-preview-workflow.md](references/step-4-preview-workflow.md)

### Step 5: Validate preview with route checklist

- **Purpose**: Apply shared and route-specific validation before writing files.
- **When**: Run immediately after Step 4 and repeat until the preview passes.
- Evaluate the preview using `references/validation-checklist.md` and return a binary `PASS` or `FAIL` with evidence and corrective actions.
- Do not write files while any checklist item is failing.
- Workflow: [references/step-5-validation-workflow.md](references/step-5-validation-workflow.md)

### Step 6: Generate files and revalidate

- **Purpose**: Write the approved skill files and confirm the written result still passes validation.
- **When**: Run only after Step 5 returns `PASS`.
- Write only the approved skill artifacts, then rerun the validation checklist against the written files before handoff.
- If revalidation fails, return to Step 3, Step 4, or Step 5 instead of handing off partial output.
- Workflow: [references/step-6-generate-workflow.md](references/step-6-generate-workflow.md)

## Output

### Result Format

- Report the selected route, generated or previewed files, and validation status in the terminal.
- Do not create `generation-summary.md` or any retained summary artifact.
