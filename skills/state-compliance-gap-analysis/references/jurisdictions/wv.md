# West Virginia — West Virginia Lottery Commission (WV Lottery)

**Code:** WV · **Products:** sportsbook + iGaming · **Key authority:** W. Va. Code § 29-22D (Sports Wagering Act) & § 29-22E (Interactive Wagering Act); rules 179 CSR 9 (Sports Wagering) & 179 CSR 10 (Interactive Wagering)

## Payments-relevant requirements

### Licensing & change management

- Operators/management service providers are licensed under the Lottery; internal controls, house rules, T&Cs and a patron-protection page are required for iGaming (179-10-5), with interactive gaming system requirements at 179-10-6 and interim approvals for expedited implementation at 179-10-18.
- Mandatory interactive gaming system logging (179-10-10) and required reports/reconciliation/test accounts (179-10-11); RGS providers regulated at 179-10-14. Independent test-lab certification of systems/changes is administered through Lottery-approved labs (GLI-style) — exact rule cite not verified, confidence MEDIUM.

### Deposits & permitted payment methods

- Sports (179-9-14.4) and iGaming (179-10-7.4) accounts may be funded by: bank deposit account, credit or debit card, cash/voucher at approved locations, reloadable prepaid card, promotional credit, winnings, operator adjustments, ACH, and any other Commission-approved means. Credit cards are permitted.
- ACH fraud control (iGaming): temporary block after 5 consecutive failed ACH deposit attempts within 10 minutes; further failures trigger suspension (179-10-7.5).

### Withdrawals & payout timelines

- iGaming withdrawals via cashier cage cash-out, transfer to bank/deposit account, reloadable card, or other approved methods (179-10-7.7). Card-funded deposits: within 90 days, remaining balance up to the deposit amount is refunded back to the originating credit/debit card (closed-loop rule, 179-10-7.6).
- No explicit numeric payout SLA found in 179-9-14 for sportsbook withdrawals — confidence MEDIUM; verify ICS-level SLA with compliance team.

### Player funds segregation / reserve

- iGaming: operator must maintain a West Virginia bank account, separate from all operating accounts, with a balance matching aggregate patron account liability (179-10-7.11).
- Dormant iGaming accounts after 16 months of inactivity are handled under WV's Uniform Unclaimed Property Act (179-10-7.15).

### Responsible gambling (deposit/spend/time limits, cooling-off, self-exclusion, reverse withdrawal rules)

- Statutory responsible-gaming mandate incl. 1-800-GAMBLER messaging (§ 29-22E-4(c)); Commission and operator exclusion lists (§ 29-22E-15(d)) plus operator self-exclusion mechanics in ICS.
- Patron must acknowledge age-21 rule and no account sharing at registration (179-9-14.2); one account per patron per operator, non-transferable (179-9-14.3 / 179-10-7).
- **Lifetime-deposit acknowledgment: W. Va. C.S.R. §179-10-6.29/6.30** — when a patron's lifetime deposits exceed the **Commission-established** gaming-deposit threshold, the interactive gaming system must **immediately prevent game play until the patron acknowledges**; required **annually** thereafter, plus a Deposit-Threshold notification pop-up. ⚠️ The commonly-cited **$5,000** threshold is **Commission-set (technical standard), NOT codified in 179-10** — confirm before treating $5,000 as authoritative. (Mandate + annual cadence HIGH; $5,000 figure MEDIUM/unverified.)
- Deposit/time-limit and cooling-off specifics live in internal control standards rather than the rule text reviewed — confidence LOW on exact limit mechanics; verify.

### KYC / age / geolocation

- Minimum age 21 for both products (§ 29-22E-15(a)-(b)); identity/age verification required before wagering; account statements covering prior 6 months on demand (179-9-14).
- Wagers accepted only from patrons physically located within WV (or in a licensed facility); dedicated geolocation requirement for iGaming at 179-10-13.

### AML overlays (state-specific, beyond federal BSA)

- Operators must "immediately report any suspicious betting over a threshold set by the operator" to appropriate authorities (§ 29-22E-12(a)(2)); card numbers must be encrypted at rest/in transit per rule requirements. Federal BSA/Title 31 casino AML applies to iGaming operations.

### Records, reporting & data

- Weekly privilege-tax returns (15% of adjusted gross interactive wagering receipts) filed electronically by Wednesday for the prior week (§ 29-22E-16); comprehensive system logging (179-10-10) and reconciliation reports (179-10-11).

## Code review focus

- Closed-loop card refunds: withdrawals must route back to the originating credit/debit card up to the deposited amount within the 90-day window before alternative payout rails are used (iGaming).
- ACH velocity control: block deposits after 5 failed ACH attempts in 10 minutes; escalate to account suspension on continued failures.
- Daily reconciliation of the segregated WV patron-funds bank account against aggregate wallet liability (iGaming).
- Dormancy clock at 16 months feeding an Unclaimed Property Act workflow.
- Dual-product separation: WV sportsbook (179-9) vs. iGaming (179-10) rules differ — config must be per-product, incl. geolocation checks (179-10-13) and logging (179-10-10).
- Encryption of stored card numbers; suspicious-transaction threshold alerts wired to a reporting queue.
- **Lifetime-deposit-ack gate (annual):** once cumulative deposits cross the Commission threshold (reportedly $5,000), block game play until acknowledged + fire the Deposit-Threshold pop-up; re-prompt annually (§179-10-6.29/6.30).

## Sources & confidence

- [179-9-14 sports wagering accounts](https://www.law.cornell.edu/regulations/west-virginia/W-Va-C-S-R-SS-179-9-14) · [179-10 series index](https://www.law.cornell.edu/regulations/west-virginia/agency-179/title-179/series-179-10) · [179-10-7 patron wagers](https://www.law.cornell.edu/regulations/west-virginia/W-Va-C-S-R-SS-179-10-7) · [W. Va. Code art. 29-22E](https://code.wvlegislature.gov/email/29-22E/) · [179-10-6 responsible gaming / lifetime-deposit ack](https://www.law.cornell.edu/regulations/west-virginia/W-Va-C-S-R-SS-179-10-6) · [W. Va. Code art. 29-22D](https://code.wvlegislature.gov/29-22D/)
- HIGH: deposit-method list, ACH velocity rule, 90-day card refund rule, segregated WV bank account, 16-month dormancy, age 21, weekly tax filing. MEDIUM/LOW: sportsbook payout SLA, deposit-limit/cooling-off mechanics, lab-certification cites — confirm against Lottery ICS/MICS with the client's compliance team. **Lifetime-deposit-ack mandate + annual cadence HIGH (§179-10-6.29/6.30, validated); the $5,000 threshold is Commission-set and NOT in the public rule — confirm.**
