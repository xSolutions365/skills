#!/usr/bin/env python3
"""Derive code-origin attribution for findings from git blame.

Why this is a script and not a subagent job: every finding already cites file+lines, so
attribution is a deterministic lookup. Having 25 subagents each shell out to git blame and
eyeball the output invites inconsistent parsing and invented names. Run this once over the
collected findings instead.

Usage:
  python blame_attribution.py <workspace> --repo <codebase-path> [options]

Reads  <workspace>/findings/*.json
Writes <workspace>/attribution.json   (keyed by finding ID; findings files are left untouched)

Options:
  --cf-pattern REGEX   Regex marking a Create Future address. Default: \\.xc@
                       (matches firstname.lastname.xc@example.com). Case-insensitive.
  --cf-domain DOMAIN   Additional whole-domain match, repeatable (e.g. --cf-domain createfuture.com).
  --quiet              Suppress the per-finding progress lines.

Attribution semantics, so the output is read correctly:
  last_toucher   the author of the most recent commit touching the cited lines
  contributors   every author appearing in the blame of the cited lines
  origin         create_future | client | mixed | no_code | unknown

`no_code` is not a gap in the data — it is the correct answer for a `missing` control. Nobody
wrote code that does not exist, so no one can be attributed for it; that gap belongs to whoever
owns the roadmap, not to a commit. `unknown` means blame genuinely failed (file gone, path not
in the repo, unparseable range) and is reported honestly rather than guessed.

Blame runs with -w -M -C so whitespace reformatting and file/code moves do not reassign
authorship to whoever last ran a formatter. Even so, blame identifies the last person to touch
a line, which is not the same as the person who caused a compliance gap. Treat the output as a
routing hint for remediation ownership, never as an individual performance judgement.
"""
import argparse
import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

DEFAULT_CF_PATTERN = r"\.xc@"


def parse_ranges(lines_field):
    """Turn a cited line reference into [(start, end), ...].

    Subagents write these by hand, so accept the shapes they actually produce:
    "88-104", "88–104" (en dash), "88,104", "88", "88-104; 120-130", "L88-L104".
    Returns [] when nothing parseable is found, which callers treat as whole-file blame.
    """
    if not lines_field:
        return []
    text = str(lines_field).replace("–", "-").replace("—", "-")
    out = []
    for chunk in re.split(r"[;&]|\band\b", text):
        nums = re.findall(r"\d+", chunk)
        if not nums:
            continue
        if len(nums) == 1:
            out.append((int(nums[0]), int(nums[0])))
        else:
            a, b = int(nums[0]), int(nums[1])
            out.append((min(a, b), max(a, b)))
    return out


def commit_ranks(repo):
    """Map commit -> recency rank (0 = tip).

    Author timestamps are an unreliable recency signal: rebases, cherry-picks and commits landed
    in the same second all tie, and a tie silently picks an arbitrary author as "last toucher".
    The repo's own topological order is the honest answer to "who touched this most recently".
    """
    try:
        res = subprocess.run(["git", "-C", str(repo), "rev-list", "--topo-order", "HEAD"],
                             capture_output=True, text=True, timeout=120)
    except (subprocess.TimeoutExpired, OSError):
        return {}
    return {c: i for i, c in enumerate(res.stdout.split()) if c}


def recency_key(rec, ranks):
    """Lower sorts as more recent. rec = (email, name, time, commit, summary)."""
    return (ranks.get(rec[3], len(ranks) + 1), -rec[2])


def blame(repo, rel_path, ranges):
    """Return [(email, name, unix_time, commit, summary)] for the cited lines, or None on failure."""
    cmd = ["git", "-C", str(repo), "blame", "--line-porcelain", "-w", "-M", "-C"]
    for start, end in ranges:
        cmd += ["-L", f"{start},{end}"]
    cmd += ["--", rel_path]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=90)
    except (subprocess.TimeoutExpired, OSError):
        return None
    if res.returncode != 0:
        # A bad -L range on a real file is worth one retry over the whole file: the finding is
        # still attributable, just less precisely.
        if ranges:
            return blame(repo, rel_path, [])
        return None
    records, cur = [], {}
    for line in res.stdout.splitlines():
        if re.match(r"^[0-9a-f]{40} ", line):
            cur = {"commit": line.split()[0]}
        elif line.startswith("author-mail "):
            cur["email"] = line[len("author-mail "):].strip().strip("<>").lower()
        elif line.startswith("author "):
            cur["name"] = line[len("author "):].strip()
        elif line.startswith("author-time "):
            cur["time"] = int(line[len("author-time "):].strip())
        elif line.startswith("summary "):
            cur["summary"] = line[len("summary "):].strip()
        elif line.startswith("\t") and cur.get("email"):
            records.append((cur.get("email", ""), cur.get("name", ""), cur.get("time", 0),
                            cur.get("commit", ""), cur.get("summary", "")))
    return records or None


def is_cf(email, cf_re, cf_domains):
    if not email:
        return False
    if cf_re.search(email):
        return True
    domain = email.rsplit("@", 1)[-1]
    return any(domain == d or domain.endswith("." + d) for d in cf_domains)


def classify(emails, cf_re, cf_domains):
    if not emails:
        return "unknown"
    flags = {is_cf(e, cf_re, cf_domains) for e in emails}
    if flags == {True}:
        return "create_future"
    if flags == {False}:
        return "client"
    return "mixed"


def resolve_path(repo, cited):
    """Map a cited path onto something git can blame; findings cite repo-relative paths but
    occasionally include an absolute prefix or a leading ./ or src/ duplication."""
    cited = (cited or "").strip().lstrip("./")
    if not cited:
        return None
    candidates = [cited]
    try:
        rp = Path(cited)
        if rp.is_absolute():
            try:
                candidates.insert(0, str(rp.relative_to(repo)))
            except ValueError:
                candidates.append(rp.name)
    except OSError:
        pass
    for cand in candidates:
        if (Path(repo) / cand).exists():
            return cand
    # Last resort: let git resolve by basename, but only if it is unambiguous.
    try:
        res = subprocess.run(["git", "-C", str(repo), "ls-files", f"*/{Path(cited).name}", Path(cited).name],
                             capture_output=True, text=True, timeout=30)
        hits = [h for h in res.stdout.split() if h]
        if len(hits) == 1:
            return hits[0]
    except (subprocess.TimeoutExpired, OSError):
        pass
    return None


def attribute_finding(f, repo, cf_re, cf_domains, ranks):
    evidence = f.get("evidence") or []
    per_ev, all_recs, unresolved = [], [], []
    for e in evidence:
        cited = e.get("file")
        rel = resolve_path(repo, cited)
        if not rel:
            unresolved.append(cited or "(no file cited)")
            per_ev.append({"file": cited, "lines": e.get("lines"), "resolved": False})
            continue
        recs = blame(repo, rel, parse_ranges(e.get("lines")))
        if not recs:
            unresolved.append(f"{rel} (blame failed)")
            per_ev.append({"file": rel, "lines": e.get("lines"), "resolved": False})
            continue
        all_recs.extend(recs)
        latest = min(recs, key=lambda r: recency_key(r, ranks))
        per_ev.append({
            "file": rel, "lines": e.get("lines"), "resolved": True,
            "last_toucher": {"name": latest[1], "email": latest[0],
                             "commit": latest[3][:12], "summary": latest[4]},
            "contributors": sorted({r[0] for r in recs}),
        })

    if not all_recs:
        # Distinguish "there is no code to attribute" from "we could not attribute the code".
        origin = "no_code" if f.get("control_status") == "missing" else "unknown"
        return {"origin": origin, "last_toucher": None, "contributors": [],
                "contributor_summary": "", "cf_share": None,
                "unresolved": unresolved, "evidence": per_ev,
                "note": "no implementing code cited — attribute to roadmap ownership, not a commit"
                        if origin == "no_code" else "blame unavailable for cited evidence"}

    latest = min(all_recs, key=lambda r: recency_key(r, ranks))
    counts = Counter(r[0] for r in all_recs)
    names = {r[0]: r[1] for r in all_recs}
    emails = list(counts)
    cf_lines = sum(n for e, n in counts.items() if is_cf(e, cf_re, cf_domains))
    return {
        "origin": classify(emails, cf_re, cf_domains),
        "last_toucher": {"name": latest[1], "email": latest[0], "commit": latest[3][:12],
                         "summary": latest[4], "is_create_future": is_cf(latest[0], cf_re, cf_domains)},
        "contributors": [{"name": names[e], "email": e, "lines": counts[e],
                          "is_create_future": is_cf(e, cf_re, cf_domains)}
                         for e in sorted(counts, key=lambda x: -counts[x])],
        "contributor_summary": ", ".join(f"{names[e]} ({counts[e]})" for e in sorted(counts, key=lambda x: -counts[x])),
        "cf_share": round(cf_lines / sum(counts.values()), 3),
        "unresolved": unresolved,
        "evidence": per_ev,
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("workspace", type=Path)
    ap.add_argument("--repo", type=Path, required=True)
    ap.add_argument("--cf-pattern", default=DEFAULT_CF_PATTERN)
    ap.add_argument("--cf-domain", action="append", default=[])
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    repo, ws = args.repo.resolve(), args.workspace
    if subprocess.run(["git", "-C", str(repo), "rev-parse", "--git-dir"],
                      capture_output=True).returncode != 0:
        print(f"ERROR: {repo} is not a git repository — attribution needs history. "
              f"Re-run the analysis without attribution, or point --repo at a clone with history.",
              file=sys.stderr)
        sys.exit(1)

    cf_re = re.compile(args.cf_pattern, re.I)
    ranks = commit_ranks(repo)
    cf_domains = [d.lower().lstrip("@") for d in args.cf_domain]
    files = sorted((ws / "findings").glob("*.json"))
    if not files:
        print(f"ERROR: no findings JSON in {ws / 'findings'}", file=sys.stderr)
        sys.exit(1)

    head = subprocess.run(["git", "-C", str(repo), "rev-parse", "HEAD"],
                          capture_output=True, text=True).stdout.strip()
    out = {"_meta": {"repo": str(repo), "commit": head, "cf_pattern": args.cf_pattern,
                     "cf_domains": cf_domains,
                     "caveat": "git blame identifies the last author to touch a line, which is not "
                               "necessarily who introduced a compliance gap. Routing hint only."}}
    tally = Counter()
    for p in files:
        try:
            doc = json.loads(p.read_text())
        except json.JSONDecodeError:
            print(f"skipping {p.name}: invalid JSON", file=sys.stderr)
            continue
        for a in doc.get("areas", []):
            for f in a.get("findings", []) or []:
                fid = f.get("id")
                if not fid:
                    continue
                attr = attribute_finding(f, repo, cf_re, cf_domains, ranks)
                attr["state"] = doc.get("state")
                attr["area"] = a.get("area")
                attr["risk"] = f.get("risk")
                out[fid] = attr
                tally[attr["origin"]] += 1
                if not args.quiet:
                    who = (attr.get("last_toucher") or {}).get("name", "—")
                    print(f"  {fid}: {attr['origin']}  (last touched by {who})")

    (ws / "attribution.json").write_text(json.dumps(out, indent=2))
    print(f"\nWrote {ws / 'attribution.json'} — " +
          ", ".join(f"{k}: {v}" for k, v in sorted(tally.items())))
    if tally.get("unknown"):
        print(f"NOTE: {tally['unknown']} finding(s) could not be attributed; they are marked "
              f"unknown rather than guessed. Check whether cited paths match the reviewed commit.")


if __name__ == "__main__":
    main()
