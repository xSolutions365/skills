# Step 5 Workflow: Generate files and revalidate

## Objective

Write approved files and confirm the written result still satisfies the checklist.

## Required actions

1. Write files exactly as approved in Step 3.
2. Rerun the checklist in [validation-checklist.md](validation-checklist.md) against the written files.
3. If any rule fails after writing:
   - report `FAIL`
   - list failing rule IDs
   - return to Step 2, Step 3, or Step 4
4. Do not hand off results until the written files pass validation.

## Done when

- Files are written at approved relative paths.
- Revalidation reports `PASS`.
- Handoff includes explicit validation evidence.
