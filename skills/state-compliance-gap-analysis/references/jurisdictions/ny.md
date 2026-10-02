# New York — New York State Gaming Commission (NYSGC)

**Code:** NY · **Products:** sportsbook · **Key authority:** Racing, Pari-Mutuel Wagering & Breeding Law § 1367/1367-a; 9 NYCRR Parts 5329 (retail) & 5330 (mobile)

## Payments-relevant requirements

### Licensing & change management

- Mobile operators ("skins") operate under platform providers; internal controls must be filed and approved (9 NYCRR 5330.8) and systems must meet 5330.10 system requirements.
- Wagering system components require independent testing-lab certification before deployment; material software changes need Commission/lab sign-off (confidence MEDIUM — exact change-classification tiers not verified).

### Deposits & permitted payment methods

- 9 NYCRR 5330.37 authorizes debit cards, prepaid cards, e-wallets, ACH/bank wire, cash at a casino cage, checks, promotional credits and gift cards.
- Credit cards are PERMITTED but capped: "credit card, up to $2,500 per year in any single account" (5330.37). Bills to ban credit card deposits entirely (e.g. A7962) are pending, not enacted, as of Aug 2026.

### Withdrawals & payout timelines

- Bettor must receive requested funds within 7 days (5330.37); permitted rails include bank transfer, check, debit-card credit, casino cage.
- Withdrawals may be delayed up to 14 days for suspected unusual wagering activity, account disputes, unexpired chargeback windows, or mailed checks.

### Player funds segregation / reserve

- 5330.24 incorporates 5329.24: operator must maintain a cash reserve "necessary to ensure the ability to cover outstanding sports pool liability, as approved by the commission" — amount is Commission-approved, not formulaic.

### Responsible gambling (deposit/spend/time limits, cooling-off, self-exclusion, reverse withdrawal rules)

- 5330.34 requires a public responsible-play page describing self-imposed responsible gaming limits, plus an annual problem-gaming plan.
- **Lifetime-deposit acknowledgment (in the STATUTE, not the 9 NYCRR regs): Racing, Pari-Mutuel Wagering & Breeding Law §1367-a(4)(a)(xiii)** — when an account holder's **lifetime deposits exceed $2,500**, the operator must **prevent all wagering until the patron acknowledges** the threshold and the option to set RG limits or close the account (+ problem-gambling info); repeated **annually** thereafter. 9 NYCRR §5330.29 only cross-references it for RG reporting; §5330.34 does not contain it. (HIGH — validated, statutory.)
- Self-exclusion/excluded persons handled via cross-referenced Parts 5325, 5327 and 5402; self-excluded persons must be blocked from wagering and account access.
- Specific limit mechanics (cool-down on limit increases, reverse-withdrawal ban) are not spelled out in 5330.34 — confidence LOW on exact parameters.

### KYC / age / geolocation

- Pre-activation KYC via verification software: full name, residential address, DOB, SSN (last 4 minimum), email, phone (5330.37); 21+ only.
- Geolocation required per 5330.44 — all wagers must originate within New York State using approved geofencing.

### AML overlays (state-specific, beyond federal BSA)

- 5330.43 requires each skin to comply with the casino AML rule (5315.17) "as if such skin were a gaming facility licensee" — a state-filed AML program on top of federal BSA obligations (program details per 5315.17; confidence MEDIUM).

### Records, reporting & data

- Internal controls, transaction logging and account records per 5330.8/5330.10; retention and Commission audit access required (retention period not verified — LOW).

## Code review focus

- Enforce a rolling $2,500/year per-account cap on credit card deposits (aggregated across cards, per account, per calendar year).
- **Lifetime-deposit-ack gate:** once cumulative lifetime deposits cross $2,500, block ALL wagering until the patron acknowledges (RG-limits/close-account offer + PG info); re-prompt annually. Distinct from the $2,500/yr credit-card cap.
- Withdrawal SLA timer: funds delivered ≤7 days; any hold >7 days must map to an allowed delay reason and cap at 14 days.
- Geolocation check before deposit-funded wager placement; block transactions resolving outside NY.
- KYC gate: account cannot fund or wager until name/address/DOB/SSN-last-4 verified; age ≥21.
- AML hooks: structuring detection and SAR-referral flags on deposits/withdrawals consistent with the state AML program.
- Self-excluded patron check on every deposit and withdrawal attempt (Parts 5325/5402 lists).

## Sources & confidence

- [9 NYCRR Part 5330 index Cornell LII](https://www.law.cornell.edu/regulations/new-york/title-9/subtitle-T/chapter-IV/subchapter-B/part-5330) · [5330.37 accounts](https://www.law.cornell.edu/regulations/new-york/9-NYCRR-5330.37) · [5330.34 responsible gaming](https://www.law.cornell.edu/regulations/new-york/9-NYCRR-5330.34) · [5329.24 reserve](https://www.law.cornell.edu/regulations/new-york/9-NYCRR-5329.24) · [5330.43 AML](https://www.law.cornell.edu/regulations/new-york/9-NYCRR-5330.43) · [NYSGC sports wagering](https://gaming.ny.gov/sports-wagering) · [Pending bill A7962](https://www.nysenate.gov/legislation/bills/2025/A7962/amendment/A) · [RPWBL §1367-a NY Senate](https://www.nysenate.gov/legislation/laws/PML/1367-A)
- HIGH: credit card $2,500/yr cap, 7-day withdrawal, AML cross-reference, reserve language. Verify with compliance team: current status of credit-card-ban bills, exact self-imposed-limit mechanics, record-retention periods, lab change-management tiers. **Lifetime-deposit-ack ($2,500/annual) HIGH but lives in RPWBL §1367-a, not Part 5330.**
