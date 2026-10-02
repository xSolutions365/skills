# Vermont — Vermont Department of Liquor and Lottery (DLL)

**Code:** VT · **Products:** sportsbook (online only; contract/revenue-share model, 3 operators incl. the operator) · **Key authority:** 31 V.S.A. ch. 25 (Act 63 of 2023); DLL "Vermont Sports Wagering Procedures" (approved 7/19/2023; revised version approved 5/13/2026, effective 10/1/2026)

## Payments-relevant requirements

### Licensing & change management

- Operators run under a competitive DLL operating contract (min. $550,000 fee, ≥20% revenue share — 31 V.S.A. § 1320); platform requirements and controls live in the DLL Sports Wagering Procedures rather than a codified admin rule.
- A revised Procedures document takes effect Oct 1, 2026 — change-management, testing-lab (GLI-style) and ICS details must be confirmed against that version (document text not directly retrievable; confidence LOW on specifics).

### Deposits & permitted payment methods

- STATUTORY CREDIT CARD BAN: the platform must prohibit an individual "from using a credit card to establish an account or place wagers" (31 V.S.A. § 1340(d)(2), per statute text; ban corroborated by industry sources). Debit, ACH/bank transfer, online payment systems and prepaid remain in use.
- Crypto cannot be accepted directly; operators may offer third-party crypto-to-cash conversion that funds the wallet in USD (e.g., DraftKings' Feb 2026 rollout listed Vermont) — treat as a payment-processor flow, not a crypto deposit.

### Withdrawals & payout timelines

- Operators may not restrict a player "from withdrawing the player's own funds or withdrawing winnings from wagers placed using the player's own money" (31 V.S.A. § 1303(b)(7)(C)).
- No statutory payout SLA located; any specific business-day timeline sits in the DLL Procedures — confidence LOW, verify exact SLA with compliance team.

### Player funds segregation / reserve

- No segregation/reserve requirement located in statute; under the contract model, funds-protection terms are expected in the operator contract/Procedures. Confidence LOW — verify contract terms.

### Responsible gambling (deposit/spend/time limits, cooling-off, self-exclusion, reverse withdrawal rules)

- Platform must allow a person to limit the amount of money deposited and spent per day (31 V.S.A. § 1340(d)(3)); daily/weekly/monthly wager limits consistent with problem-gambling best practice required (§ 1302(c)(4)).
- Statewide voluntary self-exclusion program: exclusion from account creation and/or wagering, or spend limitation (§ 1340(d)(4)); operator-level self-restriction "for a period of time the player specifies" also required; published exclusion terms are 1/3/5 years or lifetime.
- No explicit reverse-withdrawal rule found in statute — check Procedures; confidence LOW.

### KYC / age / geolocation

- Minimum age 21 (persons under 21 are "prohibited sports bettors," § 1301); identity verification via secure online databases or photo-ID examination (§ 1302(c)(2)).
- Wagers must be initiated and received within Vermont and "may not be intentionally routed outside the State" (§ 1302(c)(3)).

### AML overlays (state-specific, beyond federal BSA)

- No state-specific AML overlay identified beyond federal BSA; integrity/suspicious-wagering reporting handled through DLL Procedures. Confidence LOW on any state SAR-type duty.

### Records, reporting & data

- Operators report and remit ≥20% of adjusted gross sports wagering revenue to the State (§ 1320(d)); DLL Procedures govern reconciliation/reporting cadence (verify current version).

## Code review focus

- Hard block on credit-card BIN ranges for deposits AND account creation in VT — this is statutory, not configurable; ensure card-type detection distinguishes credit vs. debit.
- Per-day deposit-limit AND per-day spend-limit controls must exist and be player-configurable (statute is explicit about "per day").
- Withdrawal path must never gate a player's own funds/winnings behind play-through or promo conditions (§ 1303(b)(7)(C)).
- Statewide self-exclusion list integration (DLL list) checked at account creation, deposit, and wager time; support 1/3/5-year and lifetime terms.
- Geolocation gating inside VT with no routing of wager traffic out of state; age gate at 21.
- Crypto flows only as pre-converted USD via third-party processor, never direct crypto acceptance.

## Sources & confidence

- [31 V.S.A. ch. 25](https://legislature.vermont.gov/statutes/fullchapter/31/025) · [DLL Sports Wagering Procedures page](https://liquorandlottery.vermont.gov/sports-wagering-procedures) · [DLL sports wagering](https://liquorandlottery.vermont.gov/sports-wagering) · [BettingUSA VT overview](https://www.bettingusa.com/states/vt/) · [Casino.org — DraftKings crypto-to-cash Feb 2026](https://www.casino.org/news/draftkings-launching-crypto-to-cash-deposits-in-quartet-of-states/)
- HIGH: credit-card ban, age 21, deposit/spend limits, self-exclusion, in-state geolocation, 20% revenue share. LOW/VERIFY: exact statutory section numbering (pulled programmatically), payout SLA, reserve/segregation, reverse withdrawals, AML — these live in the DLL Procedures PDF (robots-blocked) and the Oct 2026 revision; confirm with the client's compliance team.
