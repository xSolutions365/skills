# Virginia — Virginia Lottery Board (VA Lottery)

**Code:** VA · **Products:** sportsbook · **Key authority:** Va. Code § 58.1-4030 et seq. (Ch. 40, Sports Betting); 11VAC5-70 (Sports Betting) and 11VAC5-80 (Consumer Protection Program)

## Payments-relevant requirements

### Licensing & change management

- Permit application must describe internal control standards, including controls that keep prohibited and self-excluded persons out of wagering (11VAC5-70-50(B)).
- Within 90 days of launch and at least annually thereafter, an independent firm must perform security/vulnerability and penetration assessments of the platform (11VAC5-70-200); material platform changes are subject to Lottery approval under the internal-controls framework.

### Deposits & permitted payment methods

- 11VAC5-70-290(G) permits funding by debit card, credit card, electronic bank transfer (ACH), online/mobile payment systems, winnings, bonus/promo credit, reloadable prepaid card, and "any other means approved by the board." Credit cards ARE permitted for deposits.
- A permit holder may not extend its own credit to a bettor (11VAC5-80-130), and the platform must let players restrict/prohibit credit access, fund transfers and automatic deposits as self-limiting tools (11VAC5-80-90).

### Withdrawals & payout timelines

- Withdrawal channels include cashier's check, wire, money order, credit/debit card credit, electronic transfer, prepaid card (11VAC5-70-290(H)).
- Withdrawal requests must be completed within 10 days absent an unresolved dispute (11VAC5-70-290(I)); consumer-protection rules require honoring the request by the later of 5 days after receipt or 10 days after tax paperwork, unless a documented fraud investigation is open (11VAC5-80-100(E)).

### Player funds segregation / reserve

- Reserve (cash, cash equivalents, letter of credit, bond, or combination) must be at least $500,000 AND ≥ the sum of player account balances + pending wagers + unpaid winnings; held in FDIC-insured institutions, recalculated daily, deficiency reported to the Director within 24 hours (11VAC5-70-140).
- Player accounts unclaimed for 5 years are presumed abandoned and escheat to the State Treasurer (11VAC5-80-100(G)).

### Responsible gambling (deposit/spend/time limits, cooling-off, self-exclusion, reverse withdrawal rules)

- Players must be able to set deposit limits and total betting-activity limits, take timeouts/cooling-off breaks, and self-suspend for a specified period of not less than 72 hours (11VAC5-80-120; 11VAC5-70-290(R)).
- Statewide Voluntary Exclusion Program under Va. Code § 58.1-4015.1 plus operator-level self-exclusion; players may permanently close the account at any time (11VAC5-80-100(E)(6)).
- System must detect and block player-initiated wagering or withdrawal activity that would create a negative balance (11VAC5-70-290(P)).

### KYC / age / geolocation

- Minimum age 21; permit holder must verify age/identity and prevent minors and prohibited persons from wagering or collecting winnings (11VAC5-70-210); one account per player per permit holder (11VAC5-70-290(F)).
- Wagers must be placed within the Commonwealth; geolocation is embedded in platform/system definitions and internal control requirements rather than a standalone section.

### AML overlays (state-specific, beyond federal BSA)

- Suspicious wagering activity must be identified and reported immediately to the Lottery Director; integrity-monitoring association membership required (11VAC5-70-220). No state SAR regime beyond this; federal BSA/Title 31 applies.

### Records, reporting & data

- Books and records per standard accounting practice, retained 5 years (11VAC5-70-160); segregated escrow for taxes/fees with the Department as beneficiary; daily reserve recalculation records.

## Code review focus

- Deposit-method allowlist includes credit cards for VA (unlike VT) but must expose player-level toggles to block credit deposits/auto-deposits as a self-limiting control.
- Withdrawal pipeline SLA: assert completion ≤ 10 days (and 5-day honor rule post-request) with an explicit, logged fraud-investigation hold state as the only allowed suspension.
- Daily job computing reserve target (player balances + pending wagers + unpaid winnings, floor $500,000) and 24-hour deficiency alerting.
- Negative-balance guard: reject wagers/withdrawals that would overdraw the wallet at authorization time (11VAC5-70-290(P)).
- Deposit/spend-limit and 72-hour-minimum self-suspension enforcement in the payments path; VEP-listed users blocked from deposits and from collecting winnings.
- Dormancy tracking: 5-year unclaimed-funds escheatment workflow to the VA State Treasurer.

## Sources & confidence

- [11VAC5-70-290 Player accounts](https://law.lis.virginia.gov/admincode/title11/agency5/chapter70/section290/) · [11VAC5-70 full chapter](https://law.lis.virginia.gov/admincodefull/title11/agency5/chapter70/) · [11VAC5-70-140 reserve](https://law.lis.virginia.gov/admincode/title11/agency5/chapter70/section140/) · [11VAC5-80 Consumer Protection](https://law.lis.virginia.gov/admincodefull/title11/agency5/chapter80/) · [Va. Code Ch. 40](https://law.lis.virginia.gov/vacodefull/title58.1/chapter40/)
- HIGH: deposit methods, 10-day withdrawal, reserve formula, no-credit-extension, 72-hour self-suspension (read from official VA admin code). VERIFY with compliance team: exact $500,000 reserve floor language, geolocation ICS detail, and current amendments post-2020 (chapter has been amended several times).
