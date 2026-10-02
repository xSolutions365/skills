# Code Review Checklist (how to review the codebase for one state)

You are reviewing a payment gateway codebase against ONE jurisdiction's requirements — a US state, or a Canadian province (Ontario or Alberta). Work from the jurisdiction's reference file plus this method. Your goal is evidence, not vibes: every finding should point at specific files/lines, or state clearly that you searched and found nothing.

## Terminology — read this before classifying any test

The client (the operator) uses **FAST** as an internal programme name: **Functional Automation and Service Testing**. FAST suites exercise assembled services end-to-end — they typically talk to real or stubbed services over the network, and they are *not* what this review means by an isolated unit test. Because "fast test" is widely used elsewhere to mean the opposite (a quick in-process unit test), never use the bare word "fast" to describe a test in your findings. Say **unit test** when you mean the isolated kind, and write **FAST** in capitals only when referring to the client's programme.

Mapping rule: a test living in a FAST suite counts as `integration_only` evidence unless you verify it actually meets the isolation bar below (deterministic, no network/DB/filesystem/clock), in which case classify it `unit_tested` and note the discrepancy. Judge by what the test does, not by which suite or folder it sits in — this is the single most common source of over-optimistic coverage claims in a codebase like this.

## Method

1. **Read the repo map** provided by the orchestrator (module layout, where per-state config lives, test suite layout). Don't redo whole-repo discovery.
2. **For each requirement area** in the jurisdiction file, locate the implementing control in code:
   - Per-state config: grep for the state code (e.g. `"MI"`, `state == StateCode.MI`, YAML/JSON config keys) and for domain terms (`self_exclusion`, `deposit_limit`, `withdrawal`, `reserve`, `geolocation`, `kyc`, `credit_card`).
   - Follow the money path: entry point → validation/gating → processor call → ledger write → webhook/settlement.
3. **Classify the control**: `present` (implements the requirement), `partial` (implements some of it, or hardcodes what should be per-state), `missing` (requirement has no implementing code), `not_found` (you could not locate it — say where you looked).
4. **Classify the testing**: `unit_tested` (an isolated unit test would fail if the control broke), `integration_only` (covered only by service-level/FAST/e2e tests), `untested`, `unknown`. A test only counts as `unit_tested` if it is deterministic and touches no network/DB/filesystem/clock. A test that merely exercises the code without asserting the required behaviour does not count, whatever suite it lives in.
5. **Rate risk** (likelihood × impact): `high` = regulator-visible failure plausible (missing control on a live-state requirement, or untested control on a money path); `medium` = control present but untested/partially tested, or evidence unclear; `low` = tested but flaky/slow/weakly asserted, or documentation gap.
6. **Recommend concretely**: name the test to add or change to make, not "improve coverage".

## What to look at per area

- **Deposits & payment methods**: permitted-method enforcement (credit-card bans/caps vary hugely by state), fee handling, deposit limit checks ordered BEFORE processor call, velocity rules.
- **Withdrawals & payouts**: state SLA timers, reverse-withdrawal restrictions, closed-loop refund rules, pending-withdrawal handling during limit/exclusion changes.
- **Funds segregation / reserve**: ledger separation of player funds, reserve calculation inputs, deficiency alerting hooks.
- **Responsible gambling**: limit types (deposit/spend/wager/time), decrease-immediate vs increase-delayed semantics, cooling-off, self-exclusion checked on DEPOSIT (not just wager), per-state list integration.
- **KYC / age / identity**: gating order (no funding before CIP passes), state age minimum (18 in DC/KY/WY, 21 most others), re-verification triggers.
- **Geolocation / jurisdiction**: location check tied to the payment/wager transaction with freshness window; fail-closed when the location service errors; parish-level rules for LA.
- **AML**: threshold aggregation logic and boundary tests, structuring detection hooks, state overlays.
- **Retail cash kiosk & cage** (only for states where the operator runs a retail/cage/kiosk cash channel): the per-state kiosk/cage rules — self-redemption / TITO kiosk withdrawal caps (e.g. IL/IN ~$3,000), anonymous-play / no-KYC kiosk limits, large cage-payout identity capture, on-premises live-geolocation on retail funding (not static venue metadata), cashless-wagering-kiosk definitions, retail funding-source restrictions. Capture these in the jurisdiction file so the rule lives with the state, not the federal lane. The federal cash-handling reporting (Title 31 CTR/SAR aggregation across cage + kiosk + digital) is NOT a state rule — it belongs to the FED baseline / the legislation skill's `aml-bsa-depth` lane; note it here only as "see FED/AML" so the two don't duplicate.
- **Change management / certification**: is there a mechanism to gate or flag changes to certified components (tags, CODEOWNERS, pipeline gates)? Absence is a finding in states with strict change control.
- **Records & data**: retention configuration, audit-log coverage of money events, timestamping/timezone handling.

## Test-suite health signals to note as you go

Misclassified unit tests (network/DB/sleep inside a suite billed as isolated), FAST suites standing in as the only evidence for a money-path control, retry-on-flaky config in CI, assertion-free tests, over-mocked tests that verify wiring not behaviour, fixtures with unrealistic amounts/states. Record these in your notes even when the specific state requirement is covered — they feed the cross-cutting lane.

## Honesty rules

- A requirement the jurisdiction file attributes to internal or client-held material (rather than a regulator URL) is still a requirement. Ontario's prepaid-card cap is the worked example: absent from the public Standards, enforced in production. Don't downgrade or drop such a requirement because you cannot find it on a regulator site — carry its provenance caveat into the finding instead.
- Never invent file paths, line numbers, or rule citations. If the jurisdiction file's citation is marked low-confidence, carry that caveat into the finding.
- If your jurisdiction is Ontario or Alberta, a finding that cites the BSA, FinCEN, a CTR/SAR or OFAC is a sign you reached for the US baseline out of habit. The Canadian AML layer is PCMLTFA/FINTRAC and the sanctions layer is SEMA/UN Act — see `canada-federal-baseline.md`. Say "the US control exists but does not satisfy the Canadian obligation" where that is what you found; that is a real and valuable finding, not a technicality.
- `not_found` + where-you-looked is a perfectly good result; a false `present` is the worst possible result.
- If the codebase genuinely doesn't handle this jurisdiction at all (not in config), report ONE high finding saying so and mark remaining areas `unknown` rather than fabricating per-area detail.
- Where the jurisdiction file says a requirement does not exist — Ontario has no numeric withdrawal SLA and no operator reserve formula, for instance — the correct rating is `green` or `unknown` with a note, not `missing`. Absence of a regulatory obligation is not an absence of control. Rating a jurisdiction red for failing to implement a rule it does not have is the fastest way to lose a client's trust in the whole matrix.
