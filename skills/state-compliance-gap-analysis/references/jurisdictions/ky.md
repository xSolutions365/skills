# Kentucky — Kentucky Horse Racing and Gaming Corporation (KHRGC)

**Code:** KY · **Products:** sportsbook · **Key authority:** KRS 230.800–230.830 (2023 HB 551); 809 KAR Chapter 10 (esp. 10:004 wagering accounts, 10:006 internal controls/audit, 10:007 responsible gaming)

## Payments-relevant requirements

### Licensing & change management

- Regulator transitioned from KHRC to the Kentucky Horse Racing and Gaming Corporation (KHRGC) effective July 2024; sports wagering rules live in 809 KAR ch. 10.
- Internal control amendments must be submitted for approval; regulator has 30 days to approve/deny; emergency temporary amendments require immediate notification and 24-hour documentation (809 KAR 10:006 §1).
- Wagering procedures/practices must comply with GLI-33 standards unless the commission permits otherwise (809 KAR 10:006 §§1(3)(g), 3).

### Deposits & permitted payment methods

- 809 KAR 10:004 §6(2)(a) permits: all payment forms authorized in KRS 230.805, cash equivalents, EFTs, promotional/bonus credit, winnings, licensee adjustments, and other approved forms; debit and credit cards are generally treated as permitted (MEDIUM — verify exact KRS 230.805 list).
- Licensee-extended credit is prohibited: no wager or deposit may be funded from credit extended by the licensee, its affiliates, or agents (809 KAR 10:006 §14).

### Withdrawals & payout timelines

- Withdrawal requests must be honored within 5 business days, except where a good-faith fraud investigation is underway (809 KAR 10:004 §6(4)(c)).

### Player funds segregation / reserve

- Reserve equal to the greater of $25,000 or the sum of daily cashable balances + pending withdrawals + outstanding wagers + unpaid winnings; forms: cash, cash equivalents, payment processor receivables/reserves, irrevocable letter of credit, bond, or combination; monthly attestation of safeguarding required (809 KAR 10:006 §6).

### Responsible gambling (deposit/spend/time limits, cooling-off, self-exclusion, reverse withdrawal rules)

- Operator-maintained self-exclusion list required; licensees must honor self-exclusion requests (809 KAR 10:007 §§1–2).
- Independent third-party review of the responsible gaming program every 5 years (809 KAR 10:007 §2(3)).
- Player-set deposit/wager/time limits are industry-standard in KY apps but a specific limit-mandate citation was not verified (LOW).

### KYC / age / geolocation

- Statutory minimum age is 18 (many operators voluntarily gate at 21); registration must be denied where birth date indicates an underage person (809 KAR 10:004 §1(3)(a)).
- Electronic age/identity verification at account establishment via commission-approved independent reference companies (809 KAR 10:004 §2(2)).
- Wagering restricted to persons located within Kentucky's authorized geographic boundaries; account terms must state this (809 KAR 10:004 §4(1)(a)).

### AML overlays (state-specific, beyond federal BSA)

- No distinct state AML statute identified; anti-fraud/suspicious activity handling flows through internal controls and the 5-business-day withdrawal fraud-hold provision (LOW — verify ICS requirements).

### Records, reporting & data

- Test-account procedures, fund issuance records, and auditing of testing activity must be documented (809 KAR 10:004 §13); audit/ICS standards per 809 KAR 10:006.

## Code review focus

- Age gate must support a state-configurable minimum of 18 (not hard-coded 21) while allowing operator policy overrides per brand.
- No deposit path may draw on operator-extended credit (e.g., negative-balance top-ups, credit lines, affiliate-financed deposits).
- Withdrawal SLA timer: 5 business days (business-day calendar logic, not calendar days as in KS/TN comparisons).
- Reserve calculation feed: daily cashable balances, pending withdrawals, open wagers, unpaid winnings must be separately queryable for the monthly attestation.
- Self-exclusion list checks on deposit and registration; exclusion data honored across the operator's KY skins.
- KYC integration calls a commission-approved verification vendor before account activation.

## Sources & confidence

- [809 KAR 10:004 Justia](https://regulations.justia.com/states/kentucky/title-809/chapter-10/004/) · [809 KAR 10:006 Justia](https://regulations.justia.com/states/kentucky/title-809/chapter-10/006/) · [809 KAR 10:007 Justia](https://regulations.justia.com/states/kentucky/title-809/chapter-10/007/)
- [KY LRC 809 KAR 10:007 official](https://apps.legislature.ky.gov/law/kar/titles/809/010/007/REG/) · [RotoWire on KY 18+ age](https://www.rotowire.com/news/what-is-the-minimum-sports-betting-age-in-kentucky-18-or-21-75286)
- Confidence: 5-business-day withdrawals, reserve formula, GLI-33 reference, credit-extension ban, self-exclusion are HIGH. Exact permitted card types under KRS 230.805 and any mandated player-limit tooling are MEDIUM/LOW — verify with compliance.
