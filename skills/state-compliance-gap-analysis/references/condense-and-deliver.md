# Validate, spot-check, condense, deliver, refresh

The back half of the run: verifying findings, then turning `findings/*.json` (plus an optional
`attribution.json`) into the decision matrix and executive summary.

## Validate and retry

After each batch:

```bash
python {SKILL_DIR}/scripts/build_matrix.py {WORKSPACE} --check
```

For invalid/missing files, re-run just that state's subagent once, telling it what was wrong with
its output. A state that fails twice gets recorded as `unknown` with a note — never hand-fabricate
its findings.

## Spot-check before reporting (do not skip)

Findings drive client decisions, so verify before condensing. Pick 3-5 findings — every `red`
area rating gets at least one, plus one suspiciously-green state — and check the evidence
yourself: open the cited file/lines; confirm the control really is missing/partial/present as
claimed and that any cited test really would fail if the behaviour broke. Correct or downgrade
findings that don't hold, and note corrections in the executive summary. If more than ~1 in 3
spot-checks fail, the batch is unreliable — re-run those states with a sharper prompt rather than
shipping bad findings.

## Condense

Run the matrix builder (install openpyxl with `pip install openpyxl --break-system-packages` if
missing):

```bash
python {SKILL_DIR}/scripts/build_matrix.py {WORKSPACE}
```

This writes the decision matrix (RAG matrix of states × areas, filterable findings sheet, summary
sheet) and an executive summary with computed stats. When `attribution.json` exists it also adds
an Origin column (org labels only) to the findings sheet, an origin roll-up to the summary, and a
separate `attribution_internal.xlsx` holding the named attribution — kept out of the shared
workbook so the matrix stays sendable without putting individuals' names beside regulatory gaps.
Replace the marked placeholder in the summary with 2-3 paragraphs of real synthesis: the
cross-state patterns (a control missing everywhere beats 53 per-state repeats), the
untested-vs-missing split, and what to fix first and why. Cross-state patterns are the
highest-value output of the whole exercise.

## Deliver

Send the decision matrix and executive summary to the user. If attribution ran, send
`attribution_internal.xlsx` too but label it plainly as internal-only — it is the file that names
people, and the whole reason it is separate is that the other two can go to the client as-is.
Close with the standing caveat: citations and thresholds were researched Aug 2026 and spot-verified
at run time; confirm with the client's compliance team before anything goes in an external
deliverable.

## Refresh runs

When re-running after code changes, reuse the same workspace layout, compare new `findings/*.json`
against the previous run's, and lead the summary with what changed (resolved / new / still-open
findings). Re-run `blame_attribution.py` rather than reusing the old `attribution.json`:
remediation commits move the last-toucher, and a gap that was CF-origin and is now client-patched
(or vice versa) changes who owns it.
