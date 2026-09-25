# Step 1 Workflow: Build the evidence ledger

## Objective

Extract everything the later steps need into one sourced ledger, so no artefact states anything the inputs don't support.

## Required actions

1. Create `@OUTPUT_ROOT/internal/evidence-ledger.md` and put `INTERNAL: do not share with client` as its first line.
2. Read the inputs in date order, oldest first, so later decisions override earlier ones.
3. Record each finding as one table row with these columns: `ID`, `Type`, `Statement`, `Source`, `Date`, `Tag`.
   - `Source` is the file name plus the speaker, slide, or section, e.g. `scope call 28 Apr, client sponsor`.
   - `Tag` is `client-safe` or `internal-only`, following the audience boundary rules.
4. Capture these `Type` values:
   - `objective`: business goals, north-star measures, success criteria, and baselines with figures
   - `deliverable`: every deliverable, with format and week, numbered as in the SoW
   - `commitment`: anything we promised, including counts such as "6–8 interviews", and anything we asked the client to provide
   - `scope`: in-scope, out-of-scope, and "keep in mind for later" items
   - `stakeholder`: name, role, organisation, their relationship to the work, and what they care about
   - `expectation`: what a named stakeholder expects us to produce or prove
   - `person`: CreateFuture team member with role, allocation, start date, and leave
   - `date`: kick-off, week starts, playbacks, exec slots, leave, and holiday periods
   - `dependency`: data, access, people, or decisions we need from the client
   - `decision`: decisions already made, with who made them
   - `open-question`: decisions not yet made, including method, fidelity, and tooling choices
   - `opportunity`: adjacent work, future phases, or wider programme ambitions
   - `glossary`: brands, systems, acronyms, and people who share a name
5. Compare the SoW or proposal against every transcript and note. For each difference, add a `scope` or `expectation` row starting `DRIFT:` that names both sources. Typical drift includes a deliverable added on a scope call but missing from the SoW, a role promised but not in casting, and a fidelity change such as "clickable prototype" becoming "working app".
6. When two people share a name, give each one a disambiguating label in the `glossary` rows and use that label everywhere.
7. Put the context coverage table at the top of the ledger. Add a `TO CONFIRM` row for every critical fact the inputs don't state, naming who can answer it.
8. Do not summarise small talk. Skip anything the audience boundary rules exclude.

## Done when

- Every deliverable, commitment, stakeholder, CreateFuture team member, and date in the inputs has a row.
- Every row has a source and a tag.
- Every SoW-versus-transcript difference is logged as a `DRIFT:` row.
