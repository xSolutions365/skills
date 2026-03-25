# Step 5 Workflow: Generate files and return links

## Objective

Write approved files, revalidate them, and return links instead of terminal dumps.

## Required actions

1. Write files exactly as approved in Step 3.
2. Rerun the checklist in `references/validation-checklist.md` against the written files.
3. If any rule fails after writing:
   - return `FAIL`
   - list failing rule IDs
   - return to Step 2, Step 3, or Step 4
4. Return a short summary plus file links to the generated outputs.
5. Do not print full generated files to the terminal unless the user explicitly asks for them.

## Done when

- Files are written at approved relative paths.
- Revalidation reports `PASS`.
- Handoff includes file links and validation evidence.
