# Per-jurisdiction fan-out orchestration

How the orchestrator spawns and drives the per-jurisdiction subagents plus the federal lane(s),
and the traps that decide whether a Canadian finding is valid.

## Fan out

Spawn one general-purpose subagent per jurisdiction **plus one FED lane** subagent, in parallel
batches of ~6-8 (a batch per message; wait for a batch to finish before the next, so the machine
isn't oversubscribed and failures are visible early). Prompt template, filling `{...}`:

```text
You are reviewing a payment gateway codebase for compliance with {STATE NAME} gaming
regulations. Read these files first, in order:
1. {SKILL_DIR}/references/review-checklist.md      (your method — follow it)
2. {SKILL_DIR}/references/jurisdictions/{code}.md   (the requirements you are checking)
2b. {SKILL_DIR}/references/{FEDERAL_BASELINE}       (the federal layer for this jurisdiction — skim, don't review against it)
3. {SKILL_DIR}/references/findings-schema.md        (your output contract)
4. {WORKSPACE}/repo-map.md                          (repo orientation — do not redo discovery)

Codebase root: {CODEBASE_PATH}. Web verification: {ON/OFF}. If ON, spend at most 2-3
searches checking whether this state's key payment rules changed after Aug 2026; note
changes in your findings rather than trusting either source blindly.

Review the codebase against every requirement area in the jurisdiction file. Evidence rules:
cite real files/lines only; `not_found` plus where-you-looked beats a guessed `present`.
Cover all nine areas even if some end up green/unknown.

Write your findings to {WORKSPACE}/findings/{code}.json following the schema exactly
(valid JSON, enumerated values only). Your final message: 2-3 sentences — overall RAG
for the state, the single worst finding, and anything that blocked you. Do not paste
the JSON back.
```

## Federal lanes — pick by country, don't mix them

There are two, and which one a jurisdiction gets is not a detail:

- **FED-US** — `references/federal-baseline.md`, output `fed.json`. BSA/FinCEN CTRs and SARs,
  OFAC, PCI, engineering integrity.
- **FED-CA** — `references/canada-federal-baseline.md`, output `fed_ca.json`. PCMLTFA/FINTRAC,
  Canadian sanctions regimes, privacy, RPAA. **There is no BSA, no FinCEN CTR/SAR and no OFAC in
  Canada.** One FED-CA lane serves both provinces, but the provincial layers are not
  interchangeable.

Run FED-US whenever any US state is in scope and FED-CA whenever any Canadian jurisdiction is;
both if the run spans both countries. Set `{FEDERAL_BASELINE}` in each jurisdiction subagent's
prompt to match its country so the reviewer skims the right federal layer.

For either FED lane, add: "Also assess overall test-suite health under `engineering_integrity`:
unit-suite runtime and isolation, whether FAST/service suites are standing in as the only
evidence for money-path controls, flakiness signals, and assertion quality."

## Unpublished rules and Canadian traps

- **Some jurisdictions' payment rules are not published.** Ontario's prepaid-card cap
  (CAD $250 / 5 cards per rolling 7 days) exists nowhere in the AGCO Standards but is enforced in
  production, and was only recovered from a client's internal requirements page. When a
  jurisdiction file marks a requirement as sourced from internal/client material rather than a
  regulator publication, do not "correct" it against the public standards and do not drop it —
  flag it and keep it. Searching the client's wiki/requirements tracker is part of the job.
- **Two Canadian provinces is not one Canadian lane.** Alberta launched 13 July 2026 on a
  deliberately Ontario-like model (AGLC regulates, AiGC conducts). A shared `CANADA` branch is
  the likely shape of the code and the likely source of defects: age is 18 in Alberta vs 19 in
  Ontario, self-exclusion is AGLC's registry vs iGO's BetGuard with different term enums and an
  extra prohibited-persons feed, Ontario's prepaid cap has no published Alberta counterpart,
  cross-province wallets are prohibited, and the governing privacy statute differs. Run them as
  separate lanes and read `ab.md`'s "Ontario contrasts" section before letting any finding cross
  the border.
- **The US-first failure mode.** The codebase is US-first, so the failure mode is not "Ontario
  was skipped" — it is Ontario being reviewed against BSA and rated green because CTR and SAR
  emitters exist. If an Ontario finding cites FinCEN, OFAC or a CTR, the lane used the wrong
  baseline and the whole jurisdiction needs re-running.

## If no Agent tool is available

If no Agent tool is available (e.g. this skill is itself running inside a subagent), run the
lanes yourself sequentially, following the same per-lane method and output contract. Findings are
equally valid; only wall-clock time suffers.

## Eager-to-please failure mode

Subagents can be eager to please — rating things green without evidence or inventing citations.
The checklist's honesty rules exist for that; if a returned summary smells too clean (all green,
no `not_found` anywhere), treat it as suspect during spot-checking.
