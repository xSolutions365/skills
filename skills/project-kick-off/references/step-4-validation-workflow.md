# Step 4 Workflow: Validate both packs

## Objective

Return `PASS` only when both packs are safe to share with their audiences, fully sourced, and fully owned.

## Required actions

1. Run each check below and record `PASS` or `FAIL` with one line of evidence.
   - `V1 Boundary`: verify every client-pack statement traces only to `client-safe` ledger rows. Also search for pricing models, budget pressure, day rates, margin, utilisation, follow-on, pull-through, uncited client names, and stakeholder opinions; each confirmed `internal-only` occurrence fails.
   - `V2 Markers`: every internal file starts with `INTERNAL: do not share with client`.
   - `V3 Sourcing`: every name, date, figure, and commitment in both packs traces to a ledger row, or is marked `TO CONFIRM` or `DEFAULT`.
   - `V4 Deliverable coverage`: every signed SoW deliverable appears in the plan, the RACI, and the playback skeleton, with an owner. A deliverable from a `DRIFT:` row appears there only when its expectation-register response is `meet` and the client has confirmed the scope change; `reset` and `park` items remain internal.
   - `V5 Drift coverage`: every `DRIFT:` row appears in the expectation register with a response and an owner.
   - `V6 Availability`: no week or deliverable lead is someone who is on leave or not yet started that week. List unknown availability; it never counts as a pass.
   - `V7 Prerequisite dates`: every "needed by" date falls before the session that uses it, and the checklist reaches the client at least five working days before week one.
   - `V8 Research fallback`: when research is in scope, the access plan has at least two fallback rungs with decision dates.
   - `V9 Name clarity`: people who share a name are disambiguated consistently.
   - `V10 Tone`: the RAID log describes trade-offs and fallbacks, and the client pack reads as a partner's plan, not a list of the client's failings.
   - `V11 Labels`: every inferred value carries `TO CONFIRM`, and every section fed by a missing or partial input carries `LOW CONTEXT`.
   - `V12 Gap routing`: every client-answerable `TO CONFIRM` appears in the prerequisites or the kick-off questions. Every CreateFuture-answerable one appears in the pitch-lead questions.
   - `V14 Cross-references`: every ID is named. On first use in each file, it shows its home file name and section as plain text. No prefix collides with another. No client file references an internal file or uses an internal-only prefix. Every referenced file and section exists.
   - `V15 Reading guide`: `internal/README.md` has an entry for every cast person, every uncast role, and the account lead. Each `Read first` list fits in about 15 minutes. Every deliverable, week lead, and open decision appears under exactly one entry's `You own`. Every file and section named exists.
   - `V13 Readiness`: apply the readiness verdict from the missing data rules and record `READY`, `READY WITH GAPS`, or `HOLD`, with the questions that clear any hold.
2. Fix every failure and rerun the failed checks.
3. Record the results at the end of `internal/evidence-ledger.md`.

## Done when

- `V1` to `V12`, `V14` and `V15` all pass and `V13` has a verdict.
