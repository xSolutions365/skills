# Step 4 Workflow: Validate preview with checklist

## Objective

Apply a binary natural-language validation gate to the preview before any file write.

## Required actions

1. Evaluate the full preview against [validation-checklist.md](validation-checklist.md).
2. Record one evidence line for every checklist group:
  - frontmatter integrity
  - workflow structure
  - step integrity
  - link and path integrity
  - self-contained constraint
  - runtime-locality constraint
  - natural-language quality
3. Return `PASS` only when every deterministic and natural-language rule passes.
4. If any rule fails:
   - return `FAIL`
   - identify the failing rule IDs
   - list corrective actions tied to the preview
5. Revise payload or preview and rerun validation until the result is `PASS`.

## Done when

- Validation result is binary: `PASS` or `FAIL`.
- Evidence exists for every rule group.
- Any failure includes corrective actions.
- Preview is approved for file generation only after `PASS`.
