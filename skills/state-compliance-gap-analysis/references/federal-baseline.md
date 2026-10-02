# Federal & Cross-Cutting Baseline — UNITED STATES (applies in every US state)

> **This is the US federal lane.** For Ontario or any other Canadian jurisdiction use `canada-federal-baseline.md` instead — there is no BSA, no FinCEN CTR/SAR and no OFAC in Canada, and applying this file there produces false green ratings.

These obligations apply regardless of jurisdiction. One dedicated subagent should review the codebase against this file (the "FED" lane) while state subagents handle state-specific rules. State files may add overlays on top of these.

## UIGEA / Regulation GG

- Payments for internet gambling must be correctly coded so financial institutions can identify them: gambling MCCs (7995; 7801/7802 for licensed US online gambling/sports betting), accurate merchant descriptors.
- Transactions must be blocked for players in states where the operator is not licensed. The eligibility decision must happen BEFORE payment acceptance.

## Federal Wire Act

- Sports wagering transactions must be intrastate: geolocation verification tied to the transaction, not just login. Look for location-token freshness checks on deposit/wager paths.

## Bank Secrecy Act / FinCEN (31 CFR Chapter X)

- Operators with >$1M gross annual gaming revenue are "financial institutions": AML programme, KYC/CIP before account funding, ongoing monitoring.
- CTR: currency/cash-equivalent transactions aggregating >$10,000 in a single gaming day (aggregation across methods and sessions — boundary cases $9,999/$10,000/$10,001 should be tested).
- SAR: suspicious activity ≥$5,000 (structuring, minimal-play laundering: rapid deposit→withdraw with little wagering).
- Record retention: 5 years minimum for relevant records.

## OFAC

- Sanctions screening of customers and payout counterparties; blocked-party handling on both deposit and withdrawal paths.

## IRS

- W-2G reporting thresholds and backup withholding on qualifying wins; TIN collection logic.

## PCI DSS v4.0.1 (current; all requirements mandatory since 31 March 2025)

- PAN never stored/logged outside tokenised scope — check serializers, log statements, error dumps, analytics events.
- Requirement 6 (secure SDLC): the unit-test suite, the client's FAST (Functional Automation and Service Testing) suites, and CI gates ARE evidence here; note their health — and which layer actually covers each control — in findings.
- Tokenisation boundary clearly defined; card data flows documented.

## Card network & ACH rules

- Visa/Mastercard gambling programme registration; correct MCC per product; quasi-cash rules; chargeback/representment handling.
- Nacha rules for ACH/e-check: authorization records, return-code handling (R01 NSF vs R10 unauthorized have different obligations), velocity handling for repeated failed attempts.

## Cross-cutting engineering expectations (reviewed once, reported in the FED lane)

- Money represented as integer minor units or exact decimal — never binary floats.
- Idempotency on all money-moving endpoints (deposits, withdrawals, refunds, webhook handlers).
- Payment state machine rejects illegal transitions (double capture, refund > capture, capture after void).
- Ledger invariants: double-entry balance, no negative player balance under concurrent operations.
- Error/decline/timeout paths handled and tested; webhook replay and out-of-order delivery tolerated.
- Per-state configuration matrix: every live state has a complete rule set; missing-state behaviour is fail-closed.
