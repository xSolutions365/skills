# Step 6 Workflow: Generate files and revalidate

## Objective

Write approved skill files and confirm the written result still satisfies the checklist.

## Required actions

1. Write only the files approved in Step 4.
2. Do not write `generation-summary.md` or any retained summary artifact.
3. Rerun the checklist in [validation-checklist.md](validation-checklist.md) against the written files.
4. If any rule fails after writing:
   - report `FAIL`
   - list failing rule IDs
   - return to Step 3, Step 4, or Step 5
5. Do not hand off results until the written files pass validation.

## Done when

- Files are written at approved relative paths.
- No summary artifact is generated.
- Revalidation reports `PASS`.
- Handoff includes explicit validation evidence.
