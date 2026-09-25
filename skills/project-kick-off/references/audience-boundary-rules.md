# Audience Boundary Rules

## Objective

Keep commercial and internal context out of the client pack. Kick-off inputs mix both audiences, so every fact must be tagged before it is used.

## Required actions

1. Tag every extracted fact with exactly one of these:
   - `client-safe`: scope, objectives, success measures, deliverables, plan, roles, prerequisites, methods, dates the client already knows, and facts the client told us.
   - `internal-only`: price negotiation, budget pressure, margin, day rates, utilisation, follow-on or pull-through ambitions, account strategy, opinions about individual client stakeholders, internal staffing issues, and anything said about other clients.
2. When a fact could fit either tag, tag it `internal-only`.
3. Build the client pack from `client-safe` entries only.
4. Rewrite stakeholder dynamics for the client pack as neutral roles and responsibilities. For example, "Sponsor wants to look good to the exec" becomes "Sponsor presents the case for investment to the executive team".
5. Name other clients in the client pack only when the proposal already cites them as case studies.
6. Leave out of both packs any small talk from the transcripts, personal anecdotes, and health, family, or HR details.
7. Make `INTERNAL: do not share with client` the first line of every internal file.
8. If a client-pack statement depends on an `internal-only` fact, delete the statement rather than softening it.

## Done when

- Every ledger entry carries exactly one tag.
- The Step 4 boundary check (V1) finds no `internal-only` content in the client pack.
- Every internal file starts with the internal marker.
