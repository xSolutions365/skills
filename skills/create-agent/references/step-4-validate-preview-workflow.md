# Step 4 Workflow: Validate preview with checklist

## Objective

Apply a binary natural-language validation gate to the preview before any file write.

## Required actions

1. Evaluate the full preview against `references/validation-checklist.md`.
2. Record one evidence line for every checklist group.
3. Return `PASS` only when every deterministic and natural-language rule passes.
4. If any rule fails:
   - return `FAIL`
   - identify the failing rule IDs
   - list corrective actions tied to the preview
5. Repeat Step 3 and Step 4 until validation returns `PASS`.

## Done when

- Validation result is binary: `PASS` or `FAIL`.
- Evidence exists for every checklist group.
- Preview is generation-ready only after `PASS`.
