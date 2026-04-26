# Step 5 Workflow: Validate preview with route checklist

## Objective

Apply shared and route-specific validation before any file write.

## Required actions

1. Evaluate the full preview against [validation-checklist.md](validation-checklist.md).
2. Record one evidence line for every applicable checklist group:
   - shared frontmatter
   - route classification
   - route layout and line limit
   - link and path integrity
   - self-contained constraint
   - natural-language quality
   - summary-artifact exclusion
3. Return `PASS` only when every shared and selected-route rule passes.
4. If any rule fails:
   - return `FAIL`
   - identify the failing rule IDs
   - list corrective actions tied to the preview
5. Revise payload or preview and rerun validation until the result is `PASS`.

## Done when

- Validation result is binary: `PASS` or `FAIL`.
- Evidence exists for every applicable rule group.
- Any failure includes corrective actions.
- Preview is approved for file generation only after `PASS`.
