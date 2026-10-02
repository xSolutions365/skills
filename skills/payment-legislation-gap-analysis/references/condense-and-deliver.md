# Validate, spot-check, condense, deliver, refresh

The back half of the run: turning raw `findings/*.json` into the decision matrix and executive
summary, after verifying the findings hold.

## Validate and retry

After each batch, validate the findings against the schema:

```bash
python {SKILL_DIR}/scripts/build_matrix.py {WORKSPACE} --check
```

Re-run any invalid/missing lane once, telling it what was wrong. A lane that fails twice is
recorded `unknown` with a note — never hand-fabricate findings.

## Spot-check before reporting (do not skip)

Findings drive remediation and can touch security/financial exposure, so verify before
condensing. Pick 3-5 findings — every `red` gets at least one, plus one suspiciously-clean lane
— and check the cited file/lines yourself: confirm the control really is missing/partial/present
and that any cited test really asserts the required behavior (and would fail if it broke).
Correct or downgrade findings that don't hold; note corrections in the summary. If more than
~1 in 3 spot-checks fail, re-run those lanes rather than shipping bad findings.

## Condense

Run the matrix builder (install openpyxl with `pip install openpyxl --break-system-packages`
if missing):

```bash
python {SKILL_DIR}/scripts/build_matrix.py {WORKSPACE}
```

It writes the decision matrix (lanes x areas RAG, filterable findings sheet, summary) and an
executive summary. Replace the marked placeholder in the summary with 2-3 paragraphs of real
synthesis: the cross-lane patterns (a control missing across many lanes beats N per-lane
repeats), the **code-gap vs test-gap split** (present-but-untested vs missing entirely vs
green-over-wrong-behavior), and what to fix first and why. Cross-lane patterns are the
highest-value output.

## Deliver

Send both output files to the user. Close with the standing caveat: citations were
researched/refreshed as of the run date and spot-verified; this is not legal advice — confirm
with the client's compliance/legal team before anything external. Where a lane is
upstream-owned, say so plainly so it becomes an ownership-map item, not a false red.

## Refresh runs

When re-running after code or legislation changes, reuse the workspace layout, compare new
`findings/*.json` against the prior run, and lead the summary with **what changed** — resolved /
new / still-open findings, and any lane whose *legislation* moved (with the updated citation).
That delta is what stakeholders want from run two onward.
