# Louisiana — Louisiana Gaming Control Board (LGCB)

**Code:** LA · **Products:** sportsbook · **Key authority:** La. R.S. 27:601–629; LAC Title 42, Part VI (Sports Wagering) and Part XV (platforms, e.g. 42:XV.1135)

## Payments-relevant requirements

### Licensing & change management

- LGCB licenses operators/platform providers; internal controls and comprehensive house rules required (LAC 42:VI.501).
- Independent lab testing of platforms is required via LGCB technical standards; specific GLI-33 adoption citation not verified here (LOW — confirm with LGCB tech standards).

### Deposits & permitted payment methods

- LAC 42:VI.507.E permits: cash or check at licensee premises, online/mobile payment systems supporting online money transfers, winnings, adjustments/refunds, promotional play credits, reloadable prepaid cards (per internal controls), and board-approved methods.
- Credit cards and ACH are NOT expressly enumerated in 42:VI.507.E; statute separately contemplates accounts "established with a line of credit or as an advance deposit wagering account" (R.S. 27:609). Treat credit-card acceptance as configuration requiring compliance sign-off (MEDIUM).
- Kiosk wagers may be funded by cash, vouchers, or the player's wagering account (R.S. 27:609).

### Withdrawals & payout timelines

- Player funds must be withdrawable within 5 business days of request; withholding only on good-faith belief of fraud/violation pending reasonable investigation (LAC 42:VI.509.A.9).
- Winnings must be credited to the player account within one day of the event unless under investigation (LAC 42:XV.1135.E(3)).

### Player funds segregation / reserve

- Operator must either segregate sports wagering player funds from operational funds OR maintain a reserve of not less than the greater of $100,000 or the outstanding sports wagering liability (open wagers + unpaid winnings + account balances); reserve cannot fund operations (LAC 42:VI.705.A).
- Monthly reserve documentation due to the division by the 10th of the following month; deficiency notice within 48 hours (LAC 42:VI.705.C–D). Special purpose entity structure allowed (42:VI.705.B).
- Funds in a wagering account are not the property of the operator (LAC 42:XV.1135.E).

### Responsible gambling (deposit/spend/time limits, cooling-off, self-exclusion, reverse withdrawal rules)

- One active account per player; player-to-player transfers prohibited (LAC 42:VI.509.A.1, A.7).
- Parental-control publication required to exclude minors from platforms (LAC 42:VI.509.A.3); statewide self-exclusion program operated by LGCB (confirm rule cite — MEDIUM).

### KYC / age / geolocation

- 21+ with commercially reasonable age confirmation before wagering; KYC file must capture name, DOB, SSN/equivalent, address, email, phone, with encrypted sensitive data (LAC 42:VI.507).
- PARISH-LEVEL GEOFENCING: no wager may be accepted when the player is out of state OR in any of the 9 parishes that rejected sports wagering in the 2020 elections (Caldwell, Catahoula, Franklin, Jackson, LaSalle, Sabine, Union, West Carroll, Winn); operator bears all geofencing/geolocation costs (R.S. 27:609).

### AML overlays (state-specific, beyond federal BSA)

- No distinct LA AML statute for sports wagering identified; suspicious-activity handling via internal controls and State Police Gaming Enforcement oversight (LOW — verify).

### Records, reporting & data

- Privacy policy must disclose data collected and disclosure conditions; complaint records retained 5 years (LAC 42:XV.1135.C, F).

## Code review focus

- Geofence logic must exclude the 9 opted-out parishes, not just enforce the state boundary — verify polygon/parish lookup and that deposits made in-state but wagers attempted in an excluded parish are blocked.
- Withdrawal SLA 5 business days; winnings-crediting job must post within 1 day of event settlement.
- Deposit method registry matches 42:VI.507.E; any credit-card or ACH rail enabled for LA must show board approval/internal-controls basis.
- Single-account enforcement and hard block on player-to-player balance transfers.
- Reserve/liability reporting: daily liability snapshot (open wagers, unpaid winnings, balances) exportable for the monthly filing; 48-hour deficiency alerting.
- PII encryption at rest for SSN/DOB in the patron file.

## Sources & confidence

- [La. R.S. 27:609 Justia](https://law.justia.com/codes/louisiana/revised-statutes/title-27/rs-27-609/) · [LAC 42:VI.507 Justia](https://regulations.justia.com/states/louisiana/title-42/part-vi/chapter-5/section-vi-507) · [LAC 42:VI.509 Justia](https://regulations.justia.com/states/louisiana/title-42/part-vi/chapter-5/section-vi-509) · [LAC 42:VI.705 Justia](https://regulations.justia.com/states/louisiana/title-42/part-vi/chapter-7/section-vi-705)
- [LAC 42:XV.1135 Cornell LII](https://www.law.cornell.edu/regulations/louisiana/La-Admin-Code-tit-42-SS-XV-1135) · [Ballotpedia 2020 parish measures](https://ballotpedia.org/Louisiana_Sports_Betting_Parish_Measures_(2020)) · [LGCB laws & regulations](https://lgcb.dps.louisiana.gov/laws-regulations/)
- Confidence: parish list, 5-day withdrawal, reserve/segregation, funding list, 21+ KYC are HIGH (primary text). Credit-card permissibility, self-exclusion rule cites, and GLI adoption are MEDIUM/LOW — verify with the client's compliance team.
