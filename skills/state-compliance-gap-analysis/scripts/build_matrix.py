#!/usr/bin/env python3
"""Condense per-state findings JSON into a decision matrix (.xlsx) + executive summary (.md).

Usage:
  python build_matrix.py <workspace>            # build outputs from <workspace>/findings/*.json
  python build_matrix.py <workspace> --check    # validate findings files only, no outputs

Outputs (written into <workspace>):
  decision_matrix.xlsx        - Decision Matrix / Findings / Summary sheets (client-safe: no individual names)
  executive_summary.md        - narrative summary skeleton with computed stats
  attribution_internal.xlsx   - ONLY if attribution.json exists. Named authors per finding, for
                                internal triage. Deliberately a separate file so the shared
                                workbook can be sent to the client without naming individuals.

Run scripts/blame_attribution.py first if you want the Origin column and the internal workbook.

Requires: openpyxl  (pip install openpyxl --break-system-packages)
"""
import json
import sys
from collections import Counter
from datetime import date
from pathlib import Path

AREAS = [
    "deposits_payment_methods",
    "withdrawals_payouts",
    "funds_segregation_reserve",
    "responsible_gambling",
    "kyc_age_identity",
    "geolocation_jurisdiction",
    "aml_reporting",
    "change_management_certification",
    "records_data",
]
EXTRA_AREAS = ["engineering_integrity", "pci_card_networks"]  # FED lanes only
AREA_LABELS = {
    "deposits_payment_methods": "Deposits & methods",
    "withdrawals_payouts": "Withdrawals & payouts",
    "funds_segregation_reserve": "Funds segregation",
    "responsible_gambling": "Responsible gambling",
    "kyc_age_identity": "KYC / age / identity",
    "geolocation_jurisdiction": "Geolocation",
    "aml_reporting": "AML & reporting",
    "change_management_certification": "Change mgmt / certification",
    "records_data": "Records & data",
    "engineering_integrity": "Engineering integrity",
    "pci_card_networks": "PCI & card networks",
}
RATINGS = {"red", "amber", "green", "unknown"}
CONTROL = {"present", "partial", "missing", "not_found"}
# "unit_tested" = isolated/deterministic. "fast_tested" is the legacy spelling, still accepted so
# refresh runs can read findings from earlier runs; it is normalised to "unit_tested" on load.
TESTS = {"unit_tested", "integration_only", "untested", "unknown", "fast_tested"}
LEGACY_TESTS = {"fast_tested": "unit_tested"}
RISKS = {"high", "medium", "low"}
# Federal/cross-cutting lanes are not jurisdictions and must not be averaged in with them.
# "fed" = US baseline, "fed_ca" = Canadian baseline; any code starting "fed" is treated as a lane.
FED_LABELS = {"fed": "FED-US", "fed_ca": "FED-CA"}


def is_fed(doc):
    return str(doc.get("state", "")).lower().startswith("fed")


def display_code(doc):
    code = str(doc.get("state", ""))
    return FED_LABELS.get(code.lower(), code)


ORIGIN_LABELS = {
    "create_future": "Create Future",
    "client": "Client",
    "mixed": "Mixed (CF + client)",
    "no_code": "No code (control absent)",
    "unknown": "Unattributed",
}
RATING_ORDER = {"red": 0, "amber": 1, "unknown": 2, "green": 3}
FILLS = {"red": "F4CCCC", "amber": "FCE8B2", "green": "D9EAD3", "unknown": "E0E0E0"}


def validate(doc, path):
    errs = []
    for key in ("state", "state_name", "areas"):
        if key not in doc:
            errs.append(f"{path.name}: missing top-level key '{key}'")
    seen = set()
    for a in doc.get("areas", []):
        area = a.get("area")
        if area not in AREAS + EXTRA_AREAS:
            errs.append(f"{path.name}: unknown area '{area}'")
        if area in seen:
            errs.append(f"{path.name}: duplicate area '{area}'")
        seen.add(area)
        if a.get("rating") not in RATINGS:
            errs.append(f"{path.name}: area '{area}' bad rating '{a.get('rating')}'")
        for f in a.get("findings", []):
            if f.get("control_status") not in CONTROL:
                errs.append(f"{path.name}: {f.get('id')} bad control_status")
            if f.get("test_status") not in TESTS:
                errs.append(f"{path.name}: {f.get('id')} bad test_status")
            if f.get("risk") not in RISKS:
                errs.append(f"{path.name}: {f.get('id')} bad risk")
    if doc.get("state", "").lower() != "fed":
        missing = [a for a in AREAS if a not in seen]
        if missing:
            errs.append(f"{path.name}: missing areas {missing} (include them as green/unknown)")
    return errs


def load(workspace):
    fdir = workspace / "findings"
    docs, errors = [], []
    files = sorted(fdir.glob("*.json")) if fdir.exists() else []
    if not files:
        print(f"ERROR: no findings JSON in {fdir}", file=sys.stderr)
        sys.exit(1)
    for p in files:
        try:
            doc = json.loads(p.read_text())
        except json.JSONDecodeError as e:
            errors.append(f"{p.name}: invalid JSON — {e}")
            continue
        errors.extend(validate(doc, p))
        normalise_legacy(doc)
        docs.append(doc)
    return docs, errors


def normalise_legacy(doc):
    """Rewrite retired enum spellings in place so old and new findings mix cleanly."""
    for a in doc.get("areas", []):
        for f in a.get("findings", []) or []:
            ts = f.get("test_status")
            if ts in LEGACY_TESTS:
                f["test_status"] = LEGACY_TESTS[ts]


def load_attribution(workspace):
    """attribution.json is optional; absent simply means the Origin column is skipped."""
    p = workspace / "attribution.json"
    if not p.exists():
        return {}
    try:
        return json.loads(p.read_text())
    except json.JSONDecodeError:
        print(f"WARNING: {p} is not valid JSON — continuing without attribution.", file=sys.stderr)
        return {}


def overall_rating(doc):
    ratings = [a.get("rating", "unknown") for a in doc.get("areas", [])]
    return min(ratings, key=lambda r: RATING_ORDER.get(r, 2)) if ratings else "unknown"


def all_findings(docs, attribution=None):
    attribution = attribution or {}
    rows = []
    for doc in docs:
        for a in doc.get("areas", []):
            for f in a.get("findings", []):
                ev = "; ".join(
                    f"{e.get('file')}:{e.get('lines', '?')} — {e.get('note', '')}" for e in f.get("evidence", [])
                )
                rows.append({
                    "state": doc.get("state"), "area": a.get("area"), "id": f.get("id"),
                    "requirement": f.get("requirement"), "citation": f.get("citation", ""),
                    "citation_confidence": f.get("citation_confidence", ""),
                    "control_status": f.get("control_status"), "test_status": f.get("test_status"),
                    "risk": f.get("risk"), "evidence": ev, "recommendation": f.get("recommendation", ""),
                    "attr": attribution.get(f.get("id")) or {},
                })
    risk_order = {"high": 0, "medium": 1, "low": 2}
    rows.sort(key=lambda r: (risk_order.get(r["risk"], 3), r["state"] or "", r["id"] or ""))
    return rows


def build_xlsx(docs, rows, out, with_origin=False):
    from openpyxl import Workbook
    from openpyxl.styles import Alignment, Font, PatternFill
    from openpyxl.utils import get_column_letter

    wb = Workbook()

    # --- Decision Matrix ---
    ws = wb.active
    ws.title = "Decision Matrix"
    fed = sorted((d for d in docs if is_fed(d)), key=lambda d: str(d.get("state", "")).lower())
    states = sorted((d for d in docs if not is_fed(d)), key=lambda d: d.get("state", ""))
    cols = AREAS + (EXTRA_AREAS if fed else [])
    header = ["State"] + [AREA_LABELS[a] for a in cols] + ["Overall", "High", "Med", "Low"]
    ws.append(header)
    for c in ws[1]:
        c.font = Font(bold=True)
        c.alignment = Alignment(wrap_text=True, vertical="center")
    for doc in states + fed:
        amap = {a["area"]: a for a in doc.get("areas", [])}
        counts = {"high": 0, "medium": 0, "low": 0}
        for a in doc.get("areas", []):
            for f in a.get("findings", []):
                counts[f.get("risk", "low")] = counts.get(f.get("risk", "low"), 0) + 1
        row = [display_code(doc)]
        for area in cols:
            row.append(amap.get(area, {}).get("rating", "—"))
        row += [overall_rating(doc), counts["high"], counts["medium"], counts["low"]]
        ws.append(row)
        for idx, area in enumerate(cols, start=2):
            cell = ws.cell(row=ws.max_row, column=idx)
            if cell.value in FILLS:
                cell.fill = PatternFill("solid", fgColor=FILLS[cell.value])
        oc = ws.cell(row=ws.max_row, column=len(cols) + 2)
        if oc.value in FILLS:
            oc.fill = PatternFill("solid", fgColor=FILLS[oc.value])
    ws.freeze_panes = "B2"
    ws.column_dimensions["A"].width = 10
    for i in range(2, len(header) + 1):
        ws.column_dimensions[get_column_letter(i)].width = 13

    # --- Findings ---
    wf = wb.create_sheet("Findings")
    fheader = ["Risk", "State", "Area", "ID", "Requirement", "Citation", "Cite conf",
               "Control", "Testing", "Evidence", "Recommendation"]
    if with_origin:
        # Org label only. Names live in attribution_internal.xlsx so this workbook stays shareable.
        fheader.insert(9, "Origin")
    wf.append(fheader)
    for c in wf[1]:
        c.font = Font(bold=True)
    for r in rows:
        vals = [r["risk"], r["state"], AREA_LABELS.get(r["area"], r["area"]), r["id"], r["requirement"],
                r["citation"], r["citation_confidence"], r["control_status"], r["test_status"],
                r["evidence"], r["recommendation"]]
        if with_origin:
            vals.insert(9, ORIGIN_LABELS.get(r["attr"].get("origin"), "Unattributed"))
        wf.append(vals)
        fill = {"high": "F4CCCC", "medium": "FCE8B2", "low": "D9EAD3"}.get(r["risk"])
        if fill:
            wf.cell(row=wf.max_row, column=1).fill = PatternFill("solid", fgColor=fill)
    wf.freeze_panes = "A2"
    widths = [8, 7, 18, 12, 40, 22, 9, 10, 14, 50, 50]
    if with_origin:
        widths.insert(9, 20)
    for i, w in enumerate(widths, start=1):
        wf.column_dimensions[get_column_letter(i)].width = w
        for cell in wf[get_column_letter(i)]:
            cell.alignment = Alignment(wrap_text=True, vertical="top")
    wf.auto_filter.ref = f"A1:{get_column_letter(len(fheader))}{wf.max_row}"

    # --- Summary ---
    wsum = wb.create_sheet("Summary")
    wsum.append(["Generated", date.today().isoformat()])
    wsum.append(["Jurisdictions reviewed", len(states) + len(fed)])
    wsum.append(["Total findings", len(rows)])
    for risk in ("high", "medium", "low"):
        wsum.append([f"{risk.capitalize()}-risk findings", sum(1 for r in rows if r["risk"] == risk)])
    wsum.append([])
    wsum.append(["Findings by area", "high", "medium", "low"])
    wsum.cell(row=wsum.max_row, column=1).font = Font(bold=True)
    for area in AREAS + EXTRA_AREAS:
        arows = [r for r in rows if r["area"] == area]
        if arows:
            wsum.append([AREA_LABELS[area]] + [sum(1 for r in arows if r["risk"] == k) for k in ("high", "medium", "low")])
    wsum.column_dimensions["A"].width = 32

    wb.save(out)


def build_attribution_xlsx(rows, attribution, out):
    """Internal-only workbook: named authors per finding.

    Kept out of decision_matrix.xlsx on purpose. The point of attribution here is deciding which
    gaps Create Future absorbs internally versus raises with the client — that is a routing
    decision, and it does not require putting individual names in front of the client next to a
    regulatory gap.
    """
    from openpyxl import Workbook
    from openpyxl.styles import Alignment, Font, PatternFill
    from openpyxl.utils import get_column_letter

    meta = attribution.get("_meta", {})
    wb = Workbook()
    ws = wb.active
    ws.title = "Attribution (INTERNAL)"

    banner = ("INTERNAL USE ONLY — not for client distribution. git blame shows the last author to "
              "touch a line, which is not necessarily who introduced the gap; reformatting, file "
              "moves and squashed history all shift blame. Use for routing remediation, not appraisal.")
    ws.append([banner])
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=10)
    ws["A1"].font = Font(bold=True, color="9C0006")
    ws["A1"].fill = PatternFill("solid", fgColor="FCE8B2")
    ws["A1"].alignment = Alignment(wrap_text=True, vertical="center")
    ws.row_dimensions[1].height = 42
    ws.append([f"Repo: {meta.get('repo', '?')} @ {(meta.get('commit') or '?')[:12]} | "
               f"CF pattern: {meta.get('cf_pattern', '?')} | domains: {', '.join(meta.get('cf_domains') or []) or 'none'}"])

    header = ["Risk", "State", "Area", "ID", "Origin", "Last toucher", "Email", "CF?",
              "CF line share", "All contributors", "Commit", "Unresolved evidence"]
    ws.append(header)
    hrow = ws.max_row
    for c in ws[hrow]:
        c.font = Font(bold=True)
    for r in rows:
        a = r["attr"]
        lt = a.get("last_toucher") or {}
        share = a.get("cf_share")
        ws.append([
            r["risk"], r["state"], AREA_LABELS.get(r["area"], r["area"]), r["id"],
            ORIGIN_LABELS.get(a.get("origin"), "Unattributed"),
            lt.get("name", "—"), lt.get("email", "—"),
            "yes" if lt.get("is_create_future") else ("—" if not lt else "no"),
            "" if share is None else share,
            a.get("contributor_summary", ""),
            lt.get("commit", ""),
            "; ".join(a.get("unresolved") or []),
        ])
        if a.get("origin") in ("create_future", "mixed"):
            ws.cell(row=ws.max_row, column=5).fill = PatternFill(
                "solid", fgColor="D9E2F3" if a.get("origin") == "create_future" else "FCE8B2")
    ws.freeze_panes = f"A{hrow + 1}"
    for i, w in enumerate([8, 7, 18, 12, 22, 20, 30, 6, 12, 42, 14, 30], start=1):
        ws.column_dimensions[get_column_letter(i)].width = w
    ws.auto_filter.ref = f"A{hrow}:{get_column_letter(len(header))}{ws.max_row}"

    # Per-person roll-up: the practical pre-filter view — how much sits with CF at all.
    wp = wb.create_sheet("By person")
    wp.append(["Person", "Email", "Create Future?", "Findings (last toucher)", "High", "Medium", "Low"])
    for c in wp[1]:
        c.font = Font(bold=True)
    people = {}
    for r in rows:
        lt = (r["attr"].get("last_toucher") or {})
        if not lt.get("email"):
            continue
        rec = people.setdefault(lt["email"], {"name": lt.get("name", ""), "cf": lt.get("is_create_future"),
                                              "n": 0, "high": 0, "medium": 0, "low": 0})
        rec["n"] += 1
        rec[r["risk"]] = rec.get(r["risk"], 0) + 1
    for email, rec in sorted(people.items(), key=lambda kv: (-kv[1]["high"], -kv[1]["n"])):
        wp.append([rec["name"], email, "yes" if rec["cf"] else "no", rec["n"],
                   rec["high"], rec["medium"], rec["low"]])
    for i, w in enumerate([24, 32, 16, 22, 8, 10, 8], start=1):
        wp.column_dimensions[get_column_letter(i)].width = w

    wb.save(out)


def build_summary(docs, rows, out, with_origin=False):
    states = [d for d in docs if not is_fed(d)]
    feds = [display_code(d) for d in docs if is_fed(d)]
    high = [r for r in rows if r["risk"] == "high"]
    lines = [
        "# Gap Analysis — Executive Summary", "",
        f"*Generated {date.today().isoformat()} from {len(docs)} review lanes "
        f"({len(states)} jurisdictions{' + ' + ', '.join(feds) if feds else ''}).*", "",
        "> ORCHESTRATOR: replace this note with 2-3 paragraphs of narrative synthesis. The stats below are computed.", "",
        "## Headline numbers", "",
        f"- Findings: **{len(rows)}** total — **{len(high)} high**, "
        f"{sum(1 for r in rows if r['risk'] == 'medium')} medium, {sum(1 for r in rows if r['risk'] == 'low')} low.",
        f"- Jurisdictions rated red overall: **{', '.join(d['state'] for d in states if overall_rating(d) == 'red') or 'none'}**.",
        f"- Untested controls (control present/partial but with no isolated unit test): "
        f"{sum(1 for r in rows if r['control_status'] in ('present', 'partial') and r['test_status'] in ('untested', 'integration_only'))}.",
        "", 
    ]
    if with_origin:
        counts = Counter(r["attr"].get("origin", "unknown") for r in rows)
        high_counts = Counter(r["attr"].get("origin", "unknown") for r in rows if r["risk"] == "high")
        lines += [
            "## Origin of findings", "",
            "Where the implementing code came from, by last author of the cited lines. Counts only — "
            "named attribution is in the internal workbook, not in this deliverable.", "",
        ]
        for key in ("create_future", "client", "mixed", "no_code", "unknown"):
            if counts.get(key):
                lines.append(f"- {ORIGIN_LABELS[key]}: **{counts[key]}** findings ({high_counts.get(key, 0)} high).")
        lines += ["",
                  "*Attribution is derived from `git blame` on the cited lines and indicates the last author "
                  "to touch that code, which is not the same as who caused the gap. It is a routing signal "
                  "for who fixes what, not an assignment of fault.*", ""]
    lines += ["## Top high-risk findings", ""]
    for r in high[:10]:
        lines.append(f"- **{r['id']}** ({r['state']}, {AREA_LABELS.get(r['area'], r['area'])}): "
                     f"{r['requirement']} — control `{r['control_status']}`, testing `{r['test_status']}`. "
                     f"{r['recommendation']}")
    if len(high) > 10:
        lines.append(f"- …and {len(high) - 10} more high-risk findings (see Findings sheet).")
    lines += ["", "## Caveats", ""]
    for d in docs:
        cav = (d.get("confidence_caveats") or "").strip()
        if cav:
            lines.append(f"- **{display_code(d)}**: {cav}")
    lines.append("\n*Verify citations and thresholds with the client compliance team before external use.*")
    out.write_text("\n".join(lines))


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    workspace = Path(sys.argv[1])
    docs, errors = load(workspace)
    if errors:
        print("VALIDATION ISSUES:")
        for e in errors:
            print(f"  - {e}")
    else:
        print(f"All {len(docs)} findings files valid.")
    if "--check" in sys.argv:
        sys.exit(1 if errors else 0)
    if errors:
        print("Building anyway with valid portions; fix the issues above and re-run for a clean matrix.")
    attribution = load_attribution(workspace)
    has_attr = bool([k for k in attribution if k != "_meta"])
    rows = all_findings(docs, attribution)
    build_xlsx(docs, rows, workspace / "decision_matrix.xlsx", with_origin=has_attr)
    build_summary(docs, rows, workspace / "executive_summary.md", with_origin=has_attr)
    written = [workspace / "decision_matrix.xlsx", workspace / "executive_summary.md"]
    if has_attr:
        build_attribution_xlsx(rows, attribution, workspace / "attribution_internal.xlsx")
        written.append(workspace / "attribution_internal.xlsx")
    print("Wrote " + ", ".join(str(w) for w in written))
    if has_attr:
        print("REMINDER: attribution_internal.xlsx names individuals — internal triage only. "
              "decision_matrix.xlsx carries origin labels but no names, so it stays client-safe.")
    else:
        print("No attribution.json found — Origin column omitted. Run scripts/blame_attribution.py "
              "first if you want code-origin attribution.")


if __name__ == "__main__":
    main()
