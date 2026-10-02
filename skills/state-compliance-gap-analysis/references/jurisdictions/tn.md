# Tennessee — Tennessee Sports Wagering Council (SWC, formerly SWAC)

**Code:** TN · **Products:** sportsbook (online-only state) · **Key authority:** Tennessee Sports Gaming Act, T.C.A. Title 4, Ch. 49 (recodified from 4-51); SWC Rules Chapters 1350-01 through 1350-05

## Payments-relevant requirements

### Licensing & change management

- Online-only market regulated by the Sports Wagering Council (independent agency since 2021); rules 1350-01 (licensing/accounts), 1350-03 (operational standards), 1350-05 (enforcement).
- System integrity/testing and annual audits per SWC operational standards; escrow/bond, cash-on-hand, and insurance amounts are set by Council rule under T.C.A. 4-49-109 (verify current amounts — MEDIUM).

### Deposits & permitted payment methods

- CREDIT CARDS PROHIBITED for funding wagering accounts. Rule 1350-01-.08 permits debit cards, electronic bank transfers (incl. third parties), online/mobile payment systems, winnings/payouts, and other Council-approved cash-initiated methods, and requires licensees to "segregate and prevent the use of funding originating from credit cards" (HIGH; statutory basis in the Sports Gaming Act — verify exact T.C.A. section with compliance).
- Practical rails: debit, ACH/online banking, e-wallets, prepaid/Play+, wire, cash at approved retail partners (deposit-only).

### Withdrawals & payout timelines

- Withdrawal requests must be completed within 5 business days unless another time is explicitly stated in house rules/T&Cs (Rule 1350-01-.08); methods include cashier's check, wire, money order, debit-card credit (only 48+ hours after registration), electronic bank transfer.

### Player funds segregation / reserve

- T.C.A. 4-49-109 requires a bond in escrow plus cash-on-hand in amounts prescribed by Council rule to ensure adequate reserves to pay bettors; licensee must be beneficiary of escrow interest. Exact reserve formula lives in rule/ICS (MEDIUM — verify amounts).
- Historical note: TN's former 10% minimum hold (90% aggregate payout cap) was repealed effective July 2023 by SB 475, replaced with a 1.85% tax on handle — payout-cap logic should NOT exist in current code.

### Responsible gambling (deposit/spend/time limits, cooling-off, self-exclusion, reverse withdrawal rules)

- Accounts must be suspended when the player requests self-exclusion or a cool-off period (Rule 1350-01-.08); TN program offers cool-off (24 hours–30 days) and multi-year self-exclusion (1/3/5 years) across all licensees.
- Operators must provide daily/weekly/monthly deposit, wager, and loss limit tooling (secondary-source supported; rule cite in 1350-03 — MEDIUM).

### KYC / age / geolocation

- 21+; identity verification requires name, DOB, SSN (or last 4), address, phone, email, plus at least one authenticator: KBA questions, device/phone verification, government ID, or biometric (Rule 1350-01-.08).
- Geolocation must verify the bettor is physically in Tennessee for every wager (GPS/WiFi/cellular), meeting SWC accuracy standards; no in-person deposits at casinos (none exist in TN).

### AML overlays (state-specific, beyond federal BSA)

- No distinct TN AML statute identified beyond federal BSA; SWC actively polices illegal/unlicensed operators and payment funnels to them (LOW — verify ICS suspicious-activity duties).

### Records, reporting & data

- Financial practices and audit obligations under T.C.A. 4-49-110; account and transaction records per SWC rules and minimum internal control standards.

## Code review focus

- Hard block on credit-card-funded deposits, including indirect paths: e-wallets/prepaid loaded by credit card must be detected or attested-blocked (rule requires segregating credit-originated funding).
- No 90% payout-cap / 10% hold logic remaining (repealed 2023); tax reporting keyed to 1.85% of handle.
- Withdrawal SLA 5 business days; debit-card withdrawal method only enabled 48 hours after that instrument's registration.
- Self-exclusion and cool-off statuses must immediately suspend deposits and wagering; cool-off durations 24h–30d configurable.
- Geolocation verification on every wager placement, TN boundary only.
- KYC requires SSN/last-4 capture plus at least one secondary authenticator before account activation.

## Sources & confidence

- [Rule 1350-01-.08 Sports Gaming Accounts Cornell LII](https://www.law.cornell.edu/regulations/tennessee/Tenn-Comp-R-Regs-1350-01-.08) · [T.C.A. 4-49 Part 1 index Justia](https://law.justia.com/codes/tennessee/title-4/chapter-49/part-1/) · [SWC rules 1350-01 TN SoS, June 2025 rev.](https://publications.tnsosfiles.com/rules/1350/1350-01.20250630.pdf)
- [SWAC memo on operator funding methods](https://www.tn.gov/content/dam/tn/swac/documents/posts/Memo_operators-funding-methods.pdf) · [tennessee.bet regulations summary](https://www.tennessee.bet/about-us/gambling-regulations/) · [PlayTenn deposit methods](https://www.playtenn.com/depositing/)
- Confidence: credit-card prohibition, 5-business-day withdrawals, KYC elements, self-exclusion/cool-off suspension are HIGH (rule text). Reserve/escrow amounts, deposit-limit rule cites, and the exact statutory section for the credit-card ban are MEDIUM — verify with the client's compliance team.
