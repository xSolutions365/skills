# Iowa — Iowa Racing and Gaming Commission (IRGC)

**Code:** IA · **Products:** sportsbook · **Key authority:** Iowa Code ch. 99F (esp. § 99F.9); 491 IAC ch. 13 (Sports Wagering), ch. 5 (records)

## Payments-relevant requirements

### Licensing & change management

- All sports wagering equipment/systems must be tested and certified by a commission-designated independent testing laboratory before use (491—13.6(1)).
- A change control process must be submitted to the IRGC 30 days before operation; updates are classified by risk, which determines whether independent lab review is required (491—13.6(2)(b)-(c)).
- Annual geolocation system testing required (491—13.6(3)(b)).

### Deposits & permitted payment methods

- STATUTORY CREDIT CARD BAN: a licensee "shall not accept a credit card... for sports wagering or to purchase coins, tokens, or other forms of credit to be wagered" (Iowa Code § 99F.9). Debit/ACH/cash and similar are permitted; credit cards must be blocked.
- Operators must provide at least one fee-free method to deposit and withdraw funds (491—13.5(4)(g)).

### Withdrawals & payout timelines

- Withdrawals must be completed "in a timely manner" (491—13.5(4)(f)); funds go to a financial-institution account in the player's name or by check mailed to the player's verified address (491—13.5(4)(b)).
- Positive player identification (PIN or approved secure method) required before withdrawal (491—13.5(4)(a)).

### Player funds segregation / reserve

- Reserve of cash or cash equivalents segregated from operational funds covering vendor and advance-deposit liabilities (491—13.2(6)); if the reserve is not held as cash, player account funds must themselves be segregated from operational funds (491—13.5(4)(h)).
- Monthly attestation to the IRGC that player funds are safeguarded (491—13.2(6)(d)).

### Responsible gambling (deposit/spend/time limits, cooling-off, self-exclusion, reverse withdrawal rules)

- Easy process for players to impose deposit and wager limitations (491—13.5(3)(h)); limits apply automatically and immediately, and cannot be relaxed for at least 24 hours (491—13.5(3)(i)).
- Indefinite self-exclusion triggers payout of the full account balance within a reasonable timeframe (491—13.5(3)(i)); IRGC statewide self-exclusion program also applies.
- Dormant accounts: no activity for 3 years (491—13.2(9)(b)); no maintenance fees may be charged on inactive Iowa accounts (491—13.2(9)(c)). No explicit reverse-withdrawal rule found.

### KYC / age / geolocation

- Account registration requires full legal name, residential address, DOB, last-4 SSN; age verification must prevent under-21 wagering (491—13.5(2), (2)(a)); matching rules: exact match on DOB/last-4/last name, flexible on nicknames and address abbreviations (491—13.5(2)(b)-(c)).
- Dynamic geolocation monitoring; the confidence radius must lie entirely within the permitted Iowa boundary; out-of-bounds wagers rejected with player notification (491—13.5(3)(b)).

### AML overlays (state-specific, beyond federal BSA)

- Operators must report abnormal wagering activity, suspicious/illegal wagering including use of funds derived from illegal activity and wagers used to conceal or launder funds (491—13.2(7)(d)) — a state reporting duty alongside federal BSA/Title 31.

### Records, reporting & data

- Wagering data must be available by wagering day/month/year and may not be purged without commission approval (491—13.2(8)); retention per 491—subrule 5.4(14) (491—13.7(7)(b)).

## Code review focus

- Hard block on credit-card-funded deposits for IA accounts (BIN-level credit vs. debit detection); statutory, not just policy.
- At least one deposit and one withdrawal rail must be fee-free for IA players — check fee engine configuration.
- Withdrawal destination restricted to accounts in the player's own name or mailed check to verified address; re-auth (PIN/step-up) before withdrawal.
- Monthly player-funds safeguarding attestation: wallet ledger must reconcile balances vs. segregated bank account.
- Limit engine: immediate application, 24-hour minimum before any relaxation; indefinite self-exclusion auto-triggers full balance payout.
- Geolocation: reject when confidence radius crosses the state boundary (not center-point-only logic); no data purge without IRGC approval.

## Sources & confidence

- [Iowa Code § 99F.9 Justia](https://law.justia.com/codes/iowa/title-iii/chapter-99f/section-99f-9/)
- [491 IAC ch. 13 — Sports Wagering Iowa Legislature](https://www.legis.iowa.gov/docs/aco/chapter/491.13.pdf)
- [491—13.5 Advance deposit sports wagering](https://www.legis.iowa.gov/docs/iac/rule/04-08-2020.491.13.5.pdf)
- Confidence: HIGH on credit-card ban, segregation/attestation, limit mechanics, lab certification and 30-day change control; MEDIUM on exact retention periods (cross-ref 491—5.4(14)) — verify with compliance team.
