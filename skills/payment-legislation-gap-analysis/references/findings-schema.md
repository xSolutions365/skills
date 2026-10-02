# Findings JSON Schema (per-lane subagent output)

Each lane subagent writes exactly one file: `<workspace>/findings/<lane>.json` (lowercase lane code). `build_matrix.py` consumes these, so field names matter. Areas are **lane-defined** (each lane names its own 3-6 requirement areas — unlike the state skill's fixed 9).

```json
{
  "lane": "EFTA",
  "lane_name": "EFTA / Regulation E",
  "reviewed_at": "2026-08-14",
  "codebase_ref": "<paths or commit reviewed>",
  "legislation_refreshed": "not-refreshed | 2026-08-14: <what changed, or 'no change since Researched date'>",
  "areas": [
    {
      "area": "error_resolution",
      "rating": "amber",
      "requirement_summary": "10-day investigation / provisional credit on disputed EFT (12 CFR 1005.11)",
      "findings": [
        {
          "id": "EFTA-ER-01",
          "requirement": "Provisional credit within 10 business days on a disputed ACH deposit",
          "citation": "Reg E, 12 CFR 1005.11(c)",
          "citation_confidence": "high",
          "control_status": "not_found",
          "test_status": "unknown",
          "evidence": [
            {"file": "shared/pay/refund/impl/RefundServiceImpl.java", "lines": "264-305", "note": "refund path exists but no consumer-dispute/provisional-credit flow; likely upstream"}
          ],
          "risk": "medium",
          "recommendation": "Confirm dispute/error-resolution ownership (support/ops system). If any timer lives here, drive it from config; add a unit test asserting provisional-credit deadline math."
        }
      ]
    }
  ],
  "notes": "free text: anything that didn't fit",
  "confidence_caveats": "which conclusions need legal/compliance verification",
  "suite_health_observations": ["reg tests for X only run on the Paysafe rail (QE-Tnnnn)"]
}
```

## Enumerations (use exactly these values)

- `area` — **lane-defined** lowercase snake_case string (e.g. `error_resolution`, `return_code_handling`, `backup_withholding`, `mcc_accuracy`, `sanctions_screening`, `prohibited_state_block`). Keep 3-6 per lane; be consistent within a lane.
- `rating` (area-level, worst-of its findings): `red` (any high-risk finding), `amber` (medium, no high), `green` (reviewed, no material gap — code present AND correct-behavior tested), `unknown` (couldn't assess — say why).
- `control_status`: `present` | `partial` | `missing` | `not_found`
- `test_status`: `unit_tested` | `integration_only` | `untested` | `unknown`  (remember: a green test over non-compliant behavior is `untested` + a finding, not coverage)
- `risk`: `high` | `medium` | `low`
- `citation_confidence`: `high` | `medium` | `low`

## Rules

- Include an `areas` entry for every requirement area in the lane file, even when `green`/`unknown` — the matrix needs a complete row. `findings` may be empty for green areas.
- IDs: `<LANE>-<AREA ABBREV>-<NN>`, unique within the file.
- Valid JSON, UTF-8, no comments, no trailing commas. Parse it before writing if unsure.
- Keep `evidence.note` under 200 chars; put longer analysis in `notes`.
- `green` requires BOTH code present/correct AND the correct behavior tested (prefer unit) — otherwise it's `amber` at best.
