# Per-lane fan-out orchestration

How the orchestrator spawns and drives the per-lane subagents, and what each subagent is told.

## Fan out

Spawn one general-purpose subagent per lane, in parallel batches of ~6-8 (a batch per message;
wait for a batch before the next so failures are visible early). Prompt template, filling
`{...}`:

```text
You are reviewing the operator payments codebase for compliance with {LANE NAME} — a PAYMENT-
LEGISLATION lane (financial-services law, not per-state gaming operating rules). Read, in order:
1. {SKILL_DIR}/references/review-checklist.md    (method — code compliance AND test coverage)
2. {SKILL_DIR}/references/lanes/{lane}.md         (the requirements you are checking)
3. {SKILL_DIR}/references/findings-schema.md      (output contract)
4. {WORKSPACE}/repo-map.md                        (repo orientation — do not redo discovery)

Codebase roots: {CODEBASE_PATHS}. Web verification: {ON/OFF}. If ON, spend at most 2-3 searches
checking whether this lane's key rules changed after the reference's Researched date; record changes
in `legislation_refreshed` and in findings rather than trusting either source blindly.

Cover every requirement area in the lane file. For each: assess CODE compliance (present/partial/
missing/not_found) AND TEST coverage (does a test assert the CORRECT behavior + its failure mode; at
what layer). Evidence rules: cite real files/lines only; `not_found` + where-you-looked beats a
guessed `present`; a green test over non-compliant behavior is a finding, not a pass. Upstream-owned
controls -> `not_found` + external-ownership note. Prefer noting where a UNIT test should
assert the behavior over an integration test.

Write findings to {WORKSPACE}/findings/{lane}.json following the schema exactly (valid JSON,
enumerated values only). Final message: 2-3 sentences — overall RAG, worst finding, biggest test-
coverage gap. Do not paste the JSON.
```

## If no Agent tool is available

If no Agent tool is available (e.g. this skill is itself running inside a subagent), run the
lanes yourself sequentially with the same method and contract — findings are equally valid,
only wall-clock suffers.

## Eager-to-please failure mode

Subagents can be eager to please — rating things green/present without evidence, or counting a
passing test as compliance. The checklist's honesty rules exist for that; if a returned summary
is all-green with no `not_found` and no test caveats, treat it as suspect during spot-checking.
