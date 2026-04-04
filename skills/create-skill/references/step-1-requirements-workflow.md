# Step 1 Workflow: Capture requirements and freeze intent

## Objective

Capture a complete requirement set and freeze it before payload drafting.

## Required actions

1. Collect every required field from [payload-schema.md](payload-schema.md).
2. Use [authoring-rules.md](authoring-rules.md) to keep the generated `SKILL.md` on the minimal structure `frontmatter -> # Workflow -> ## Output`.
3. Ask clarifying questions until each field is concrete and testable.
4. Require deterministic workflow boundaries:
   - contiguous step numbering
   - exactly one workflow reference file per step
   - no external path dependencies
5. Require a deterministic output contract with a relative retained path and fixed result-format blocks.
6. Resolve tie-break behavior for any branching rule.
7. Request explicit user approval that requirements are frozen.

## Done when

- No required field remains ambiguous.
- Numbering and reference strategy are explicit.
- User approval confirms requirements are frozen.
