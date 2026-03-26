---
name: "create-project-docs"
description: "Generate a concise README plus evidence-backed reference docs from repo analysis. USE WHEN you need fast-onboarding docs without burying detail."
---

# Create Project Docs

Create a progressive-disclosure documentation set for a target repository by keeping onboarding-critical material in `README.md` and moving deeper detail into focused `docs/references/*.md` files.

- Use this when a repository needs a clearer onboarding path without losing conceptual depth.
- Use this when an existing README has become overloaded and needs a clean split into entrypoint and reference docs.
- Use this when documentation must be grounded in repo evidence instead of invented commands, workflows, or examples.

## Workflow

Use this section for step context only. Keep detailed mechanics in the referenced workflow files.

### Step 0: Preflight target repo context

- **Purpose**: Confirm the target repo, output paths, and analysis boundaries before documentation work begins.
- **When**: Run first.
- Treat the caller repository as the analysis root and prefer its public entrypoint surface over implementation-detail commands.
- Confirm whether `README.md` and `docs/references/` already exist so the run can distinguish create versus update behavior.
- Workflow: [references/step-0-preflight-workflow.md](references/step-0-preflight-workflow.md)

### Step 1: Inventory repo evidence

- **Purpose**: Build a source-backed inventory of commands, concepts, workflows, and files that generated docs may cite.
- **When**: Run after Step 0 and before deciding document structure.
- Collect evidence from repo files, configs, package manifests, automation surfaces, and any user-permitted existing docs.
- Record source paths for every command, environment variable, file path, example, and concept that may appear in the generated docs.
- Workflow: [references/step-1-evidence-inventory-workflow.md](references/step-1-evidence-inventory-workflow.md)

### Step 2: Design the doc split

- **Purpose**: Decide what belongs in `README.md` versus `docs/references/`.
- **When**: Run after the evidence inventory is complete.
- Keep first-success setup, first-success execution, project purpose, and top-level nouns in the README.
- Move exhaustive, table-driven, schema-heavy, role-specific, or multi-example detail into focused reference docs.
- Workflow: [references/step-2-information-architecture-workflow.md](references/step-2-information-architecture-workflow.md)

### Step 3: Draft the README

- **Purpose**: Generate a concise README that gives a new contributor a fast path into the repository.
- **When**: Run after Step 2.
- Use the local README template and keep the mandatory sections in order: title, badges, Quick Install, Quick Start, What the project does, Core Concepts, and Go Deeper.
- Use only evidence-backed commands, paths, examples, and terminology.
- Workflow: [references/step-3-readme-drafting-workflow.md](references/step-3-readme-drafting-workflow.md)

### Step 4: Draft the reference docs

- **Purpose**: Generate only the deeper docs that the evidence inventory justifies.
- **When**: Run after the README outline is stable.
- Choose the matching local template for each deeper-doc archetype and keep one topic per file.
- Avoid duplicating onboarding material that the README already covers.
- Workflow: [references/step-4-reference-docs-workflow.md](references/step-4-reference-docs-workflow.md)

### Step 5: Select templates and examples

- **Purpose**: Use the skill's packaged templates and example snapshots to keep outputs consistent without copying blindly.
- **When**: Run while drafting README and reference docs.
- Use `assets/templates/` for structure and `examples/` for pattern guidance only.
- Treat example files as illustrative snapshots that may shape layout, flow, and tone but may not override target-repo evidence.
- Workflow: [references/step-5-templates-and-examples-workflow.md](references/step-5-templates-and-examples-workflow.md)

### Step 6: Validate accuracy and flow

- **Purpose**: Reject invented content, weak information architecture, and unresolved duplication before any write.
- **When**: Run after README and reference-doc drafts exist.
- Evaluate the draft package with the local validation checklist.
- Verify every command, path, environment variable, and example against the evidence inventory.
- Fail the run if a deeper doc lacks evidence justification or if the README becomes overloaded.
- Workflow: [references/step-6-validation-workflow.md](references/step-6-validation-workflow.md)

### Step 7: Generate files and report gaps

- **Purpose**: Write the approved docs to the target repo and hand back the evidence-backed summary.
- **When**: Run only after Step 6 passes.
- Write `README.md` and only the justified `docs/references/*.md` files.
- Report created or updated files, evidence sources used, and any unresolved gaps instead of fabricating content.
- Workflow: [references/step-7-generation-workflow.md](references/step-7-generation-workflow.md)
