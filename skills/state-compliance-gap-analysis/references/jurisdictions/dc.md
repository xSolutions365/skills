# District of Columbia — Office of Lottery and Gaming (OLG)

**Code:** DC · **Products:** sportsbook · **Key authority:** D.C. Law 22-312 (Sports Wagering Lottery Amendment Act of 2018), as amended 2024 (citywide multi-operator model); 30 DCMR Ch. 21 (Privately Operated Sports Wagering) and related chapters

## Payments-relevant requirements

### Licensing & change management

- Sports wagering systems must meet GLI standards or other OLG-approved standards (30 DCMR 2119.2); systems must prevent past-posting and post-outcome voids (2119.13).
- Operators run under OLG-approved written Minimum Internal Controls; material system changes flow through OLG/lab review (description-level, confidence MEDIUM — tiering not enumerated in Ch. 21 text reviewed).

### Deposits & permitted payment methods

- Accounts may be funded by credit cards, debit cards, ACH bank transfers, or approved e-wallets (e.g., Skrill); cryptocurrency is explicitly prohibited (per ICLG summary of OLG rules; 2122.10/2122.13 also allow "any other means approved by the Office"). Credit cards ARE allowed in DC.

### Withdrawals & payout timelines

- No fixed statutory day-count payout SLA identified in Ch. 21; payouts ≥$10,000 require obtaining and recording payor/patron information (2118.2); tickets up to $10,000 redeemable by mail (2119.7).
- Title 31 federal ID requirements apply to transactions over $5,000 (referenced in 2118.2).

### Player funds segregation / reserve

- Cash reserve requirement with a $25,000 floor plus OLG formula determining the actual amount (2117.1); operator must notify OLG within 24 hours if the cash reserve becomes insufficient (2117.2). Full liability-coverage formula: verify current text (confidence MEDIUM).

### Responsible gambling (deposit/spend/time limits, cooling-off, self-exclusion, reverse withdrawal rules)

- OLG statewide voluntary self-exclusion program (1-year, 18-month, 3-year, 5-year, lifetime); systems must prevent self-excluded persons from wagering (2129.31); excluded patrons cannot collect winnings (2114.9 context).
- Patron-settable deposit/wager/time limits: not located in reviewed Ch. 21 text — likely in internal-control standards; confidence LOW, verify.
- No reverse-withdrawal provision identified.

### KYC / age / geolocation

- Minimum age is 18 (21 only for kiosks at lottery retailers) — lowest in the operator footprint; identity verification requires resolving full 9-digit SSN (last-4 acceptable only if remaining factors resolve the full SSN within 4 minutes) (2122.3(d)).
- Geofencing to DC boundaries required, with exclusionary zones (e.g., federal enclaves and around competing Class A facilities under the pre-2024 model) (2120.1-2120.4); post-2024 amendments allow licensed operators citywide — confirm current zone logic (confidence MEDIUM).

### AML overlays (state-specific, beyond federal BSA)

- Compliance with applicable federal requirements (BSA/Title 31) mandated (2118.2); comprehensive AML program, SARs/CTRs and detailed customer/transaction records expected; no DC-specific thresholds beyond federal identified.

### Records, reporting & data

- Detailed customer and transaction records required for AML and OLG audit; security footage retained minimum 7 days (2109.1(f)); financial/reserve reporting to OLG incl. the 24-hour insufficiency notice (2117.2).

## Code review focus

- Age gate set to 18 for DC online (not 21) — check hardcoded 21+ assumptions in shared KYC config; kiosk channel, if any, stays 21.
- SSN resolution logic: full-9 SSN capture path with the 4-minute last-4 resolution fallback per 2122.3(d).
- Crypto deposit rails disabled for DC; card/ACH/e-wallet allow-list matches OLG approvals.
- Reserve monitor with alerting: insufficiency must trigger a 24-hour OLG notification workflow.
- $10,000 payout threshold triggers enhanced info capture; $5,000+ transactions trigger Title 31 ID logging.
- Geofence polygon and exclusion zones current with the 2024 citywide multi-operator amendments.

## Sources & confidence

- [30 DCMR Ch. 21 — Privately Operated Sports Wagering adopted rules](https://dclottery.com/sites/default/files/2023-01/Privately-Operated-Sports-Wagering-Rules-ADOPTED-30-DCMR-Ch-21_0.pdf)
- [OLG Regulations hub](https://dclottery.com/olg/regulations) · [D.C. Law 22-312](https://code.dccouncil.gov/us/dc/council/laws/22-312)
- [ICLG Gambling 2026 — Washington, D.C.](https://iclg.com/practice-areas/gambling-laws-and-regulations/usa-washington-d-c/)
- Confidence: HIGH on age 18, self-exclusion tiers, GLI standard, $25k reserve floor + 24h notice; MEDIUM on funding-method list (secondary source) and post-2024 geofence rules; LOW on deposit-limit tooling — verify all against current OLG rules/ICS with compliance team.
