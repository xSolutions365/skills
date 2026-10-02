# Findings JSON Schema (per-state subagent output)

Each jurisdiction subagent writes exactly one file: `<workspace>/findings/<code>.json` (lowercase jurisdiction code — `mi.json`, `nj.json`, `on.json` for Ontario). The federal lanes write `fed.json` (US baseline) and `fed_ca.json` (Canadian baseline); the builder recognises any code beginning `fed` as a lane rather than a jurisdiction, so it is never averaged in with the jurisdiction rows. The build_matrix.py script consumes these, so field names matter.

```json
{
  "state": "MI",
  "state_name": "Michigan",
  "reviewed_at": "2026-08-13",
  "codebase_ref": "<path or commit reviewed>",
  "areas": [
    {
      "area": "withdrawals_payouts",
      "rating": "red",
      "requirement_summary": "Withdrawals honored within 10 business days; status updates during investigations (R 432.655d)",
      "findings": [
        {
          "id": "MI-WD-01",
          "requirement": "10-business-day withdrawal completion clock",
          "citation": "Mich Admin Code R 432.655d",
          "citation_confidence": "high",
          "control_status": "partial",
          "test_status": "untested",
          "test_evidence": [],
          "evidence": [
            {"file": "src/withdrawals/service.py", "lines": "88-104", "note": "SLA timer exists but hardcoded to 14 days for all states"}
          ],
          "risk": "high",
          "recommendation": "Drive SLA from per-state config; add unit test asserting MI=10 business days and a missing-state fail-closed case"
        }
      ]
    }
  ],
  "notes": "free text: anything that didn't fit",
  "confidence_caveats": "which conclusions need verification with client compliance team",
  "suite_health_observations": ["misclassified unit test: tests/unit/test_deposits.py hits live redis"]
}
```

## Enumerations (use exactly these values)

- `area` — one of: `deposits_payment_methods`, `withdrawals_payouts`, `funds_segregation_reserve`, `responsible_gambling`, `kyc_age_identity`, `geolocation_jurisdiction`, `aml_reporting`, `change_management_certification`, `records_data`. The FED lane may additionally use `engineering_integrity` (money arithmetic, idempotency, state machine, ledger) and `pci_card_networks`.
- `rating` (area-level, worst-of its findings): `red` (any high-risk finding), `amber` (medium but no high), `green` (reviewed, no material gaps), `unknown` (couldn't assess — say why in requirement_summary).
- `control_status`: `present` | `partial` | `missing` | `not_found`
- `test_status`: `unit_tested` | `integration_only` | `untested` | `unknown`. `unit_tested` means an isolated, deterministic test (no network/DB/filesystem/clock) that fails if the control breaks. Coverage that exists only in the client's FAST suites (Functional Automation and Service Testing) is `integration_only` unless the individual test provably meets the isolation bar. The legacy value `fast_tested` is still accepted by the builder for old findings files, but do not emit it — "fast" collides with the client's FAST programme name.
- `test_evidence` (optional array, same `{file, lines, note}` shape as `evidence`) — the file:line of the test(s) that ASSERT this control and would fail if it broke. Populate whenever `test_status` is `unit_tested` or `integration_only`; leave `[]` for `untested`/`unknown`. Cite the asserting **test**, not the control. This is deliberately tech-neutral — a path plus a line range, no tool or language assumption — so a downstream refinement layer (or a human) can confirm coverage without re-hunting for the test.
- `risk`: `high` | `medium` | `low`
- `citation_confidence`: `high` | `medium` | `low`

## Rules

- Include ALL nine jurisdiction areas in `areas`, even when `green` or `unknown` — the matrix needs a complete row. Where the jurisdiction imposes no such requirement (Ontario has no withdrawal SLA and no operator reserve formula, for example), rate the area on what the code does anyway and say in `requirement_summary` that the jurisdiction is silent — do not rate it `missing`, which reads as an operator failure. `findings` may be empty for green areas.
- IDs: `<STATE>-<AREA ABBREV>-<NN>`, unique within the file.
- Populate `test_evidence` with the asserting test's file:line whenever you mark a control `unit_tested` or `integration_only`. A test status without evidence is treated as unverified downstream, so an unbacked `unit_tested` is worse than an honest `unknown`.
- Valid JSON, UTF-8, no comments, no trailing commas. Run it through a JSON parser before writing if unsure.
- Keep `evidence.note` under 200 chars; put longer analysis in `notes`.
- Do not add attribution/authorship fields yourself. Cite `file` and `lines` accurately and the orchestrator derives origin from `git blame` afterwards (`scripts/blame_attribution.py` → `attribution.json`, keyed by finding ID). Precise line ranges are what make that attribution meaningful, so cite the lines implementing the control rather than a whole file where you can — and never cite a path you haven't confirmed exists, since a bad path shows up as an unattributable finding rather than a silent miss.
