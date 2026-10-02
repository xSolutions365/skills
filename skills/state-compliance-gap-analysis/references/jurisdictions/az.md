# Arizona — Arizona Department of Gaming (ADG)

**Code:** AZ · **Products:** sportsbook · **Key authority:** A.R.S. Title 5, Ch. 10 (Event Wagering); Ariz. Admin. Code R19-4 Art. 1; ADG Event Wagering Appendix K (Standards for Event Wagering)

## Payments-relevant requirements

### Licensing & change management

- Systems must be tested by an independent test lab against GLI-33 (2019); recertification at least every 15 months unless no updates were made (Appendix K Part IV.D, IV.F(1)).
- Tiered change management (Part IV.E): high-impact changes (new wagering features, geolocation, PII handling) need written ADG approval within 5 days; low-impact need prior notification; no-impact (OS patches, UI) none; emergency changes may go live with notice ASAP. A change log with approval date/time, components, category, and authorizer is mandatory (IV.E(5)).

### Deposits & permitted payment methods

- Broad funding permitted: cash, cash equivalent, EFT/ACH, credit card, debit card, wire, winnings, promo/bonus credit, personal check, or other ADG-approved method (Appendix K Part VII.D(2)). Credit cards ARE allowed in AZ.

### Withdrawals & payout timelines

- Withdrawal requests must be honored within 7 days (Part VII.D(3)(a)); may be withheld only on suspicion of fraud/violation, with expeditious investigation and patron notification (VII.D(3)(b)).
- Winning tickets honored ≥1 year post-event; mail redemptions paid within 10 days of receipt (Part VI.E(12)).

### Player funds segregation / reserve

- Reserve (cash, LOC, bond, or combination) of the greater of $500,000 or the amount covering all outstanding event-wagering liability plus funds held in player accounts (Appendix K Part II.I).

### Responsible gambling (deposit/spend/time limits, cooling-off, self-exclusion, reverse withdrawal rules)

- ADG operates a statewide event wagering self-exclusion list; wagers from self-excluded patrons prohibited (Part VI.C(2)(b)); platforms must display helpline messaging (Part II.H).
- Player-set deposit/wager/time limits and cooling-off are offered in practice but not explicitly enumerated in Appendix K — confirm in operator's approved internal controls (confidence LOW).
- Dormant accounts closed after 3 years' inactivity; funds treated as abandoned after 120 days of contact attempts (Part VII.D(4)). No explicit reverse-withdrawal rule found.

### KYC / age / geolocation

- Verify age (21+) and identity before account use; account record must hold legal name, DOB, last-4 SSN (or equivalent), address, email, verification method/date (Part VII.B(2), VII.B(5)); re-verify on suspicion of compromise (VII.B(7)).
- Dynamic geofencing required: location checked before each wager and throughout the session; out-of-state (and non-permitted tribal-land) patrons blocked (Part III.C(2)-(3)).

### AML overlays (state-specific, beyond federal BSA)

- Operator internal controls must include Bank Secrecy Act procedures (Part II.F(1)(k)); no AZ-specific thresholds beyond federal BSA identified (confidence MEDIUM).

### Records, reporting & data

- Internal controls must include record-retention procedures (Part II.F(1)(y)); ADG has access rights to daily activity/accounting records, security and surveillance reports (Part II.D). Exact retention period not stated in Appendix K — verify.

## Code review focus

- Withdrawal pipeline SLA: requests must complete (or enter a documented fraud-hold workflow with patron notification) within 7 calendar days.
- Deposit method allow-list includes credit card; ensure card-network sportsbook MCC/flags handled but no state-level block needed for AZ.
- Reserve/liability reporting job: player balances + open wagers + unpaid wins aggregated for the $500k-or-liability reserve calculation.
- Geolocation re-check on session and per-wager (not deposit-only); block list for self-excluded patrons enforced before deposit AND wager acceptance.
- Change-classification metadata in release pipeline: payment/PII-touching changes flagged high-impact → ADG approval gate before deploy.
- Dormancy timer (3 years) and abandoned-funds handling (120-day contact window) on account/wallet records.

## Sources & confidence

- [ADG Appendix K — Standards for Event Wagering](https://gaming.az.gov/sites/default/files/Appendix%20K%20-%20Revised%20Generic.pdf)
- [ADG Event Wagering Final Rules R19-4](https://gaming.az.gov/sites/default/files/Event%20Wagering%20Final%20Rules.pdf) (fetch blocked; rule-number mapping to R19-4-1xx not independently verified)
- [Ariz. Admin. Code R19-4-101 LII](https://www.law.cornell.edu/regulations/arizona/Ariz-Admin-Code-SS-R19-4-101)
- Confidence: HIGH on Appendix K items (deposits, 7-day withdrawals, reserve, geofencing, change tiers); LOW on player-set limit specifics and retention periods — confirm against the operator' ADG-approved internal controls.
