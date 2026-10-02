# Illinois — Illinois Gaming Board (IGB)

**Code:** IL · **Products:** sportsbook · **Key authority:** Sports Wagering Act, 230 ILCS 45; 11 Ill. Adm. Code Part 1900

## Payments-relevant requirements

### Licensing & change management

- Master sports wagering licensees operate under IGB-approved internal controls; sports wagering systems and material changes require IGB approval and independent testing-lab certification (Part 1900 technical/testing subparts; confidence MEDIUM on exact section numbers).
- IGB adopted complementary 2025 rules on cashless wagering and record retention alongside the credit card ban.

### Deposits & permitted payment methods

- 11 Ill. Adm. Code 1900.1220(d): permitted funding = debit cards, in-person cash, ACH, licensed money transmitters, verified non-transferable reloadable prepaid cards, promotional credits, adjustments/refunds. Credit cards are NOT a permitted method.
- IGB **adopted** the rule prohibiting credit-card funding of sports wagering at its **April 24, 2025** meeting (proposal stage); after JCAR/public comment it became **effective ~November 7, 2025**, with IGB directing licensee compliance by **November 10, 2025**. Do NOT treat April 2025 as the effective date. (HIGH that the ban is in force; effective date per the Illinois Register publication — validated 2026-08.)
- Since July 1, 2025 Illinois levies a per-wager transaction fee on licensees ($0.25 per wager up to 20M wagers/yr, $0.50 thereafter); several operators pass this to patrons as a per-bet fee — fee itemization is payments-relevant (confidence MEDIUM on figures).

### Withdrawals & payout timelines

- 1900.1220(e): withdrawal via cashier at in-person locations, transfer to verified reloadable prepaid card or bank account, and kiosk withdrawals up to $3,000.
- A hard statewide payout-SLA (days) was not verified in 1900.1220 — confidence LOW; check internal controls/IGB minimum standards.

### Player funds segregation / reserve

- 1900.1050 Reserve Requirements: reserve covering player account balances and liability on determined-but-unpaid wagers; cash component plus cash equivalents/insurance/"other commercially reasonable means"; theoretical maximum exposure recalculated at least monthly; reserve assets "may not be applied to other purposes" (confidence MEDIUM on the cash-percentage split).

### Responsible gambling (deposit/spend/time limits, cooling-off, self-exclusion, reverse withdrawal rules)

- Statewide IGB Sports Wagering Self-Exclusion Program: operators must block registration, deposits and wagering by enrolled persons and return account balances (IGB-administered list).
- Self-imposed deposit/wager/time limit offerings are expected under IGB rules/internal controls but exact rule cite not verified — confidence LOW.
- Confirmation emails required for account transactions and on-demand 6-month statements (1900.1220(f)) support RG transparency.

### KYC / age / geolocation

- 1900.1220(b): identity verified in person (signature + government photo ID) or remotely via multi-source authentication; patron file must hold legal name, DOB, SSN (last 4 acceptable), residential address, verification method/date; 21+.
- Wagers must be placed within Illinois with approved geolocation/geofencing on the mobile platform (confidence MEDIUM on rule cite).

### AML overlays (state-specific, beyond federal BSA)

- No distinct state AML program requirement verified beyond federal BSA/Title 31; IGB relies on internal controls, suspicious-transaction reporting to the Board, and the new record-retention rules — confidence LOW/MEDIUM.

### Records, reporting & data

- Transaction confirmation emails, on-demand statements (6 months of activity) and semi-annual summaries showing deposits, withdrawals, win/loss and balances (1900.1220(f)).

## Code review focus

- Hard-block credit cards as a funding instrument, including indirect routes (credit-funded wallets/prepaid where detectable via BIN checks).
- Kiosk withdrawal path enforces the $3,000 cap; prepaid-card withdrawal only to verified, non-transferable cards owned by the patron.
- Per-wager transaction fee: correct itemization/accounting if passed through to patrons; fee tier switch at 20M annual wagers.
- Transaction confirmation email dispatch on deposits/withdrawals; statement generation covering 6 months on demand.
- Self-exclusion list check on registration, deposit and wager; auto-refund of balances on enrollment.
- Reserve/liability feeds: daily account-balance and open-liability reporting to support monthly max-exposure calculation.

## Sources & confidence

- [1900.1220 Sports Wagering Accounts ILGA/JCAR](https://ilga.gov/commission/jcar/admincode/011/011019000L12200R.html) · [1900.1050 Reserve Requirements Cornell LII](https://www.law.cornell.edu/regulations/illinois/Ill-Admin-Code-tit-11-SS-1900.1050) · [IGB credit card ban adopted Apr 2025, effective ~Nov 2025](https://www.rockfordnewsfirst.com/2025/04/29/illinois-gaming-board-adopts-new-rule-banning-credit-card-use-sports-betting/) — NOTE: Cornell LII's §1900.1220 mirror is STALE (still shows pre-ban text permitting cards); the ban rests on the Nov-2025 Illinois Register publication · [IGB sports wagering FAQ](https://igb.illinois.gov/sports-wagering/sports-faq.html) · [230 ILCS 45](https://www.ilga.gov/legislation/ILCS/details?ActID=3996&ChapterID=25)
- HIGH: permitted funding list, kiosk cap, KYC elements, credit card exclusion from funding list. Verify with compliance team: credit-card-ban effective date/final text, withdrawal SLA, self-imposed limit rule cites, per-wager fee mechanics.
