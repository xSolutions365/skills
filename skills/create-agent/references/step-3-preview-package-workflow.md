# Step 3 Workflow: Preview generated files

## Objective

Preview the exact file package before any write.

## Required actions

1. Build preview content in this fixed order:
   - `system-contract.md`
   - `task-packet.md`
   - `verification-checklist.md`
   - optional `subagents/*.md` sorted by path ascending
2. Keep every preview path relative to the approved output root.
3. Use the local templates in `assets/templates/` and the selected role-profile overlay.
4. For each file, present:
   - target relative path
   - complete proposed content
   - concise change summary: `new`, `replace`, or `no-change`
5. If preview feedback changes the contract, return to Step 2 and freeze the contract again before regenerating preview.

## Done when

- Every target file has a deterministic preview.
- File order is stable.
- Preview and frozen contract remain synchronized.
