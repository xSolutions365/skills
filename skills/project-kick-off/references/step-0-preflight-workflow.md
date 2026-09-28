# Step 0 Workflow: Preflight inputs and boundaries

## Objective

Confirm that the inputs are good enough to build both packs, fix the engagement shape, and load the audience boundary rules before reading anything.

## Required actions

1. Load [audience-boundary-rules.md](audience-boundary-rules.md), [missing-data-rules.md](missing-data-rules.md), [cross-reference-rules.md](cross-reference-rules.md), and [reading-guide-rules.md](reading-guide-rules.md). Apply all four to every later step.
2. Collect the required inputs and confirm each one:
   - the signed SoW, or the latest proposal version if signature is pending (record which version)
   - casting: name, role, allocation %, start date, known leave, for every person
   - at least one of: pitch transcripts, scope-call transcripts, internal pitch notes
   - client name and the brands or business units in scope
3. Collect optional inputs when they exist:
   - client-supplied materials such as briefs, decks, research, data, or journey maps
   - the internal kick-off notes and any prerequisites already sent
   - the CreateFuture playbook or method the proposal names, such as a design sprint
4. If the SoW or proposal, or casting, is missing, stop and ask for it. If casting lacks start dates, allocation, or leave, continue and mark each gap `TO CONFIRM` for `casting`.
5. Rate context coverage for every input category, using the missing data rules. If pitch or scope calls are `missing`, tell the user that the pitch-lead questions will be generated.
6. When the proposal and a later transcript disagree, treat the later source as current but log the disagreement in Step 1.
7. Classify the engagement as `discovery`, `build`, or `strategic` with [engagement-shape-guide.md](engagement-shape-guide.md). Record a hybrid as its primary shape plus the secondary shape.
8. Record the lifecycle position: the skill assumes pitch, sign (or intent to sign), and casting are done. If casting is not done, tell the user that the plan-and-ownership output will be provisional.
9. Write the packs locally only. Set `@OUTPUT_ROOT` to `kick-off/<client-slug>/` in the working directory unless the user names another local folder. Create `internal/` and `client/` under it. Never write to Google Drive, SharePoint or any other shared store from this skill.
   - On the first line under each file's title, add the stamp `DRAFT · run by <name> on <date> · inputs: <list>`, so parallel runs by different people are easy to tell apart.
10. Ask the user for the kick-off date and the week-one start date if the inputs don't state them.

## Done when

- Every required input is present or explicitly waived by the user.
- The SoW version, engagement shape, kick-off date, and `@OUTPUT_ROOT` are recorded.
- Context coverage is rated for every input category.
- The audience boundary rules are loaded.
