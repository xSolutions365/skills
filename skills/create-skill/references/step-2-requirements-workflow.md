# Step 2 Workflow: Capture route-specific requirements

## Objective

Capture a complete requirement set for the selected route and freeze it before payload drafting.

## Required actions

1. Collect the shared fields from [payload-schema.md](payload-schema.md): `skill_id`, `description`, `use_when`, and `template_type`.
2. Collect only the selected route's required body and reference fields.
3. Use [authoring-rules.md](authoring-rules.md) to keep the generated layout aligned with the selected route.
4. Ask clarifying questions until every selected-route field is concrete and testable.
5. Resolve tie-break behavior for any optional runbook or workflow branch.
6. Confirm no `generation-summary.md`, retained summary path, or output contract path is part of the generated files.
7. Request explicit user approval that the route and requirements are frozen.

## Done when

- No shared or route-specific field remains ambiguous.
- File shape and reference strategy are explicit.
- User approval confirms requirements are frozen.
