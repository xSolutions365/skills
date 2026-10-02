# Ohio — Ohio Casino Control Commission (OCCC)

**Code:** OH · **Products:** sportsbook · **Key authority:** Ohio Rev. Code Chapter 3775; Ohio Admin. Code Chapters 3775-16 & 3775-17

## Payments-relevant requirements

### Licensing & change management

- OAC 3775-16-02 (change management): "High Impact" changes (affecting operational integrity of the system) require 5 business days' advance notice to the Commission, which may deny/delay; emergency changes for immediate threat/liability may go live at once with notice within 48 hours.
- Executive director may require independent certified lab testing of any change, results due to the Commission within 90 days; documented change policies must cover segregated test environments, classification, rollback, full change logging and segregation of duties.

### Deposits & permitted payment methods

- OAC 3775-16-03(E)(1): funding via credit or debit card, cash/vouchers, promotional credit, winnings, ACH, wire, corrections, and other approved methods — credit cards CURRENTLY permitted.
- PENDING CHANGE: OCCC has approved (post-comment, July 2026) an amendment to 3775-16-03 removing credit cards as an acceptable deposit method; awaiting CSI and JCARR review with possible late-summer/fall 2026 effectiveness — build should be ban-ready.

### Withdrawals & payout timelines

- 3775-16-03(E)(7): patrons may withdraw funds within 5 business days of request; delay only for investigation of suspected fraud/legal violation, with written status updates to the patron every 10 business days.

### Player funds segregation / reserve

- OAC 3775-16-06: reserve ≥ (open wagers on undetermined events + unpaid winnings + patron account funds); forms = cash, cash equivalents, payment processor reserves/receivables, irrevocable LOC, bonds; "Reserve funds must be held separate from operational funds in a manner approved by the executive director."
- 90-day advance notice and a written wind-down plan (settle liabilities, refund player funds) before ceasing operations.

### Responsible gambling (deposit/spend/time limits, cooling-off, self-exclusion, reverse withdrawal rules)

- 3775-16-03(E)(3): self-imposed limitations on deposits, wagers and time-based parameters must be offered at registration and remain continuously accessible on the platform.
- Statewide Voluntary Exclusion Program (VEP) administered by OCCC applies to sports gaming; enrolled patrons must be blocked from accounts, deposits and wagering (program rules under OAC 3772-12 family — confidence MEDIUM on cite).
- Reverse-withdrawal/cool-down mechanics not explicitly verified in rule text — confidence LOW.

### KYC / age / geolocation

- 3775-16-03(D)(2): identity verified via digital/physical exam of government ID with authentication software, or approved multi-source methodology (third-party + governmental databases); 21+.
- OAC 3775-17-01 location-based technology: wagers must be placed within Ohio using approved geolocation systems.

### AML overlays (state-specific, beyond federal BSA)

- No standalone state AML program identified beyond federal BSA; state overlay is via incident reporting (3775-16-17), accounting/revenue audit (3775-16-18) and internal/external audit rules (3775-16-19/20) — confidence MEDIUM.

### Records, reporting & data

- 3775-16-16 security/safety of confidential information; 3775-16-17 incident reporting to the Commission; 3775-16-18 accounting and revenue audit standards; full change logs per 3775-16-02.

## Code review focus

- Credit card deposit support behind a feature flag: currently legal, but ban amendment is imminent — verify rapid disable path and BIN-level credit detection.
- Withdrawal SLA: payout within 5 business days; fraud-hold workflow must generate written patron status updates every 10 business days.
- Deposit/wager/time self-limit settings available at registration and always reachable in-session; enforcement server-side.
- Change-management gates in CI/CD: classify High vs Low Impact payment-system changes, enforce 5-business-day notice artifacts, 48-hour emergency notice logging, rollback and segregation-of-duties controls.
- Reserve feed: real-time patron balance + open liability + unpaid winnings totals segregated from operational accounting.
- Geolocation verification prior to wager placement; VEP list screening on registration, deposit and wager.

## Sources & confidence

- [OAC 3775-16-03 accounts codes.ohio.gov](https://codes.ohio.gov/ohio-administrative-code/rule-3775-16-03) · [OAC 3775-16-02 change management](https://codes.ohio.gov/ohio-administrative-code/rule-3775-16-02) · [OAC 3775-16-06 reserve Justia](https://regulations.justia.com/states/ohio/title-3775/chapter-3775-16/section-3775-16-06) · [Chapter 3775-16 index Justia](https://regulations.justia.com/states/ohio/title-3775/chapter-3775-16/) · [OAC 3775-17-01 geolocation](https://law.cornell.edu/regulations/ohio/Ohio-Admin-Code-3775-17-01) · [Credit card ban rule status, July 2026](https://bettorsinsider.com/sports-betting/2026/07/09/ohio-regulator-moves-to-ban-credit-card-funding-for-sports-betting-accounts-as-rule-advances-toward-late-summer-vote/)
- HIGH: 5-business-day withdrawal, change-management tiers/notice windows, reserve composition, self-limit offering. Verify with compliance team: final effective date/text of the credit card ban, VEP rule cites, reverse-withdrawal treatment.
