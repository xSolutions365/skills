# Review Checklist — how to review one payment-legislation lane (code + tests)

You are reviewing the payments codebase against ONE legislation lane. Work from the lane's reference file plus this method. Goal: evidence, not vibes. Every finding points at specific files/lines or states clearly that you searched and found nothing.

## Method

1. **Read the repo map** (module layout, entry points, where per-state config lives, unit-vs-integration test split). Don't redo whole-repo discovery.
2. **For each requirement area** in the lane file, locate the implementing control:
   - Follow the money path: entry point (deposit/withdraw/refund/webhook) → validation/gating → processor call → ledger write → reporting.
   - Grep the domain terms the lane file names (e.g. `returnCode`/`R01`/`R10` for Nacha; `W-2G`/`backupWithholding` for tax; `OFAC`/`sanction`/`blocked` for sanctions; `idempotency`; `MCC`; `AFT`/`OCT`).
3. **Classify the control** — `present` (implements it), `partial` (some of it, or hardcodes what should be per-state/config), `missing` (no implementing code), `not_found` (couldn't locate — say where you looked / whether it looks upstream-owned).
4. **Classify the test coverage** — this lane cares about tests as much as code:
   - `unit_tested` = a **unit** (deterministic, no network/DB/filesystem/clock) test would fail if the control broke.
   - `integration_only` = covered only by end-to-end/integration tests (networked, multi-service) rather than an isolated unit test.
   - `untested` = no test exercises it, or a test exercises it without asserting the required behavior.
   - `unknown` = couldn't assess.
   - **A test that asserts the CURRENT behavior when that behavior is non-compliant is NOT coverage — it is a finding** (it locks in the wrong behavior). Say so explicitly.
   - Check the *failure mode*, not just the happy path: fail-closed on error, boundary values ($9,999/$10,000/$10,001), replay/idempotency, per-state/per-rail variation.
5. **Rate risk** (likelihood × impact): `high` = regulator-visible or financial-loss failure plausible (missing control on a money path, or a green-over-wrong-behavior test); `medium` = present but untested/partial, or evidence unclear; `low` = tested but weakly, or documentation gap.
6. **Recommend concretely** — name the exact test to add (prefer a **unit** test and say which class/method), and the code change. "Add coverage" is not a recommendation.

## Test-layer preference (important for this codebase)

Unit tests run early, are deterministic, and gate the build cheaply (in a Maven repo that's the surefire phase, but the principle is toolchain-agnostic); integration/e2e tests are slow, networked, and retry-wrapped. When you recommend a test, prefer the unit layer wherever the logic is unit-testable (validators, pure calculations, state machines, resolvers). Reserve integration/FAST only for genuine cross-service seams (webhook authenticity end-to-end, kiosk caller identity, multi-rail behavior). Note when an existing "reg" test only runs on one rail/gateway but the rule applies to all.

## Ownership boundary

Much of this bounded context delegates: KYC/CIP/age → ats-accounts; RG limit semantics + statewide lists → the RG service; reserve/segregation → finance; some AML/tax reporting → dedicated systems. When a control is genuinely owned upstream, report `control_status: not_found` with a note that it appears externally owned and where the boundary is — do NOT fabricate `present`. An accurate "owned elsewhere, confirm it exists + is tested there" is more useful than a false green.

## Honesty rules

- Never invent file paths, line numbers, or legal citations. If the lane file marks a citation low-confidence, carry that caveat.
- `not_found` + where-you-looked is a good result; a false `present` is the worst result.
- A passing test is not proof of compliance — verify what it asserts.
- If the codebase genuinely doesn't touch this lane at all (e.g. no crypto rail), say so in ONE finding and mark remaining areas `unknown`/`not_found` rather than padding.

## Legislation refresh (if web verification is ON)

Spend at most 2-3 searches confirming whether this lane's key rules changed since the reference's "Researched" date. Record any change in `legislation_refreshed` and in the affected finding (cite the new rule + its confidence). Don't blindly trust either the bundled reference or a single search result — note the discrepancy for the compliance team.
