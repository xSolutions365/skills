# Colorado — Colorado Division of Gaming / Limited Gaming Control Commission (CDOG/LGCC)

**Code:** CO · **Products:** sportsbook · **Key authority:** C.R.S. 44-30-15xx (Sports Betting); Sports Betting Regulations 1 CCR 207-2 (Rules 1-9, esp. Rules 6 & 7); **SB 26-131 (2026) — credit-card ban + deposit-frequency cap, eff 8/12/2026**

## Payments-relevant requirements

### Licensing & change management

- Entire sports betting system must be certified by a Colorado-approved independent testing laboratory before launch (Rule 7.6(1)(a)-(b)); kiosks separately certified (Rule 7.7(2)).
- System integrity and security assessment by a Director-approved independent professional within 90 days of launch and annually thereafter (Rule 7.2).
- Internal control procedures (Rule 7.5) must be documented and approved; changes to the system generally require lab/Division involvement — exact change-tiering not enumerated in Rule 7.6 (confidence MEDIUM).

### Deposits & permitted payment methods

- Historically (1 CCR 207-2 Rule 7.6(5)-(6)) wagers could be funded by cash, cash equivalents, credit OR debit cards, vouchers, chips, or other Director-approved means. **SUPERSEDED for credit cards by SB 26-131 (signed 6/2/2026, effective 8/12/2026): online sportsbooks are PROHIBITED from accepting credit-card deposits, directly or indirectly (incl. credit-funded prepaid / e-payment routes); breach up to $25,000 + Class 2 misdemeanor.** Debit cards, ACH and cash remain permitted. (HIGH — validated against CO General Assembly.)
- **SB 26-131 deposit-frequency cap (eff 8/12/2026):** at most **6 separate deposits per gaming day** (a continuous 24-hour period the operator defines); cap is on COUNT, not dollar amount. Credit-funded prepaid must be disabled.

### Withdrawals & payout timelines

- Winners must be paid within 24 hours of a bona fide demand for payment, or within a Division-approved timeframe if secured by bond (Rule 6.9).
- Checks issued must be backed by sufficient funds until cashed or 6 months elapse (Rule 6.9).

### Player funds segregation / reserve

- Operators must maintain reserves sufficient to cover outstanding sports betting liability: player account balances + undetermined open wagers + unpaid winning wagers; acceptable forms include segregated cash/cash equivalents, irrevocable letter of credit, payment-processor reserves/receivables, or a combination (Rule 6.9).

### Responsible gambling (deposit/spend/time limits, cooling-off, self-exclusion, reverse withdrawal rules)

- Internal controls must include a secure online and on-location responsible gaming and self-exclusion program, including patron-settable account limits (Rule 7.5(23)) and detailed problem gambling program procedures (Rule 7.5(22)).
- On an operator-imposed exclusion, no new wagers or deposits may be accepted immediately upon execution, but the patron may still withdraw their balance (Rule 7.5(7)).
- No explicit cooling-off or reverse-withdrawal rule located in 1 CCR 207-2 (confidence LOW — check current rule version and CO statewide self-exclusion program mechanics).

### KYC / age / geolocation

- No bets from persons under 21 or bets not originating in Colorado (Rule 1.3(4)); operators must use an age and identity verification method/system (Rule 1.4(3) definition; applied via Rule 7.5 ICMPs).
- Internal controls must include a method for verifying geolocation systems establishing patron location for online betting (Rule 7.5(20)).

### AML overlays (state-specific, beyond federal BSA)

- Internal controls must include AML compliance standards, including limits on anonymous kiosk betting (Rule 7.5(8)); CTRs and multiple-transaction logs subject to Division requirements (Rule 7.6(9)).

### Records, reporting & data

- System malfunctions/deviations must be documented and retained at least 3 years (Rule 7.6(1)(d)); wagering/accounting data reportable to the Division per Rules 6-7.

## Code review focus

- 24-hour payout SLA on demanded winnings: withdrawal queue must not batch beyond 24h for cleared, verified winners.
- Liability snapshot (balances + open bets + unpaid wins) computed and exportable for the Rule 6.9 reserve calculation, including payment-processor receivables if counted toward reserve.
- Deposit/wager block (with withdrawal still permitted) on operator-imposed and self-excluded accounts — asymmetric account state, not a full freeze.
- Patron-settable account limits API (deposit at minimum) wired into deposit authorization path per Rule 7.5(23).
- Geolocation gate on wager placement for patrons ≥21 located in CO; log evidence for Division audit.
- CTR/multiple-transaction aggregation logs for cash-adjacent flows and kiosk limits on anonymous play.
- **Block credit-card + credit-funded-prepaid (BIN) deposits for CO effective 8/12/2026 (SB 26-131)** — the legacy 'credit cards allowed' path must be date-gated per-state.
- **Enforce <=6 deposits per gaming day for CO (SB 26-131)** — count-based cap keyed to the operator's 24h gaming-day window; failed deposits should not count.

## Sources & confidence

- [1 CCR 207-2 Sports Betting Regulations CO SoS](https://www.sos.state.co.us/CCR/GenerateRulePdf.do?ruleVersionId=8934)
- [CO Division of Gaming Rule 7.5 Internal Control Procedures](https://sbg.colorado.gov/sites/sbg/files/documents/Internal%20Control%20Procedures%20Rule%207.5.pdf)
- [CO Sports Betting Rules & Regulations hub](https://sbg.colorado.gov/sports-betting-rules-and-regulations) · [SB 26-131 CO General Assembly](https://leg.colorado.gov/bills/sb26-131)
- Confidence: HIGH on funding methods, 24-hour payout, reserve composition, lab certification, annual security assessment; MEDIUM/LOW on change-management tiers, cooling-off/reverse-withdrawal — verify current rule version with compliance team. **UPDATE 2026-08 (validated vs primary law): credit-card funding is now PROHIBITED eff 8/12/2026 (SB 26-131), superseding Rule 7.6(6); a 6-deposit/gaming-day cap also applies.**
