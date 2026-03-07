---
name: visual-explainer
description: Generate self-contained HTML visual explainers for technical systems and data. USE WHEN users ask for diagrams, visual technical summaries, or browser-rendered tables instead of terminal ASCII.
compatibility: Requires a browser to view generated HTML files. Optional surf-cli for AI image generation.
license: MIT
metadata:
  author: nicobailon
  version: "0.4.2"
---

# Visual Explainer

Generate self-contained HTML pages that explain technical systems, plans, diffs, and structured data with strong visual hierarchy.

- Prefer browser-rendered visuals over ASCII diagrams and box-drawing tables.
- Use mode-specific references only when the selected rendering path needs them.
- Treat `--codex` as an optional workflow enhancement flag: when present, swap the default core style references for the strict Codex variants and load `references/codex-design-guardrails.md`; otherwise ignore those Codex-only references.
- Keep outputs deterministic: one HTML file, clear path, and explicit quality checks.

## Workflow

### Step 0: Preflight context and constraints

- Confirm output destination, viewer constraints, optional flags, and optional tool availability.
- Define which references are required for the chosen mode before building.
- Workflow: [references/step-0-preflight-workflow.md](references/step-0-preflight-workflow.md)

### Step 1: Route content to rendering approach

- Classify the request and select one deterministic rendering mode.
- Prefer semantic HTML tables for table-heavy output and Mermaid for topology-centric graphs.
- Workflow: [references/step-1-routing-workflow.md](references/step-1-routing-workflow.md)

### Step 2: Build structure and style

- Build semantic HTML and a complete CSS variable theme with intentional typography and hierarchy.
- Keep anti-slop and readability guardrails aligned with canonical style references.
- Workflow: [references/step-2-build-workflow.md](references/step-2-build-workflow.md)

### Step 3: Apply mode-specific rules

- Load only the mode-specific references required for Mermaid, slides, navigation, and tables.
- Apply template guidance without duplicating deep reference content in this file.
- Workflow: [references/step-3-mode-specific-workflow.md](references/step-3-mode-specific-workflow.md)

### Step 4: Deliver and quality-check

- Write to `.visual-explainer/` in the current project root, open the file, and verify quality before handoff.
- Report the path and any unresolved limitations explicitly.
- Workflow: [references/step-4-deliver-workflow.md](references/step-4-deliver-workflow.md)
