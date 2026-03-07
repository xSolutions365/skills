# Migration Notes (V1)

## Objective

Record how source `SKILL.md` content was refactored for shared-skill pattern compliance.

## Source-to-destination decisions

- Core mission and routing intent: condensed into `SKILL.md`.
- Detailed aesthetic and anti-slop rules: retained in [libraries.md](libraries.md) and [css-patterns.md](css-patterns.md).
- Diagram routing matrix: moved into [step-1-routing-workflow.md](step-1-routing-workflow.md).
- Mode-specific execution details: consolidated in [step-3-mode-specific-workflow.md](step-3-mode-specific-workflow.md).
- Delivery and quality checklist details: moved into [step-4-deliver-workflow.md](step-4-deliver-workflow.md).
- Existing `references/*.md` and `templates/*.html`: copied as-is from source repository in V1.

## Out of scope in V1

- Source command prompt migration from `visual-explainer/prompts/*.md` into shared prompts.
