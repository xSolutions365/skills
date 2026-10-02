# Attribute code origin

Create Future needs to know which gaps trace back to its own engineers, because those get fixed
internally rather than raised with the client. CF addresses carry `.xc` before the `@`
(e.g. `firstname.lastname.xc@operator.example`); everyone else is treated as client-side. Skip
this step entirely if attribution is off.

## Run it once over the collected findings

The findings already cite file and line ranges, so this is a deterministic lookup rather than
something subagents should each attempt:

```bash
python {SKILL_DIR}/scripts/blame_attribution.py {WORKSPACE} --repo {CODEBASE_PATH}
```

Add `--cf-pattern` if the marker differs on this engagement (a case-insensitive regex, default
`\.xc@`), and `--cf-domain createfuture.com` — repeatable — if some CF staff commit from a
separate domain. Confirm the pattern against a couple of real commit emails in the repo before
trusting a full run; a wrong pattern produces a confidently mislabelled matrix, which is worse
than no attribution at all.

## Reading the labels

This writes `attribution.json` and labels each finding `create_future`, `client`, `mixed`,
`no_code`, or `unknown`. Two deserve attention:

- `no_code` is the right answer for a `missing` control. Nobody wrote code that does not exist,
  so no commit can be attributed; that gap belongs to whoever owned the roadmap. Don't let it
  read as "unattributed data quality problem".
- `unknown` means blame genuinely failed — usually a cited path that doesn't exist at the
  reviewed commit. A cluster of these signals that subagents cited stale or invented paths, worth
  checking before you ship anything.

## Grain of salt

`git blame` identifies the last author to touch a line, not the person who caused a compliance
gap. Whoever last reformatted a file, resolved a merge, or moved code between modules can surface
as the "last toucher" of logic they never designed (the script passes `-w -M -C` to suppress the
worst of this, but cannot eliminate it). `mixed` and the CF line share exist precisely so a
CF-authored control later patched by client staff doesn't get filed as wholly one side's problem.
This is a routing signal for who fixes what — not an input to anyone's performance review, and
worth saying out loud if the output ever gets discussed as though it were.
