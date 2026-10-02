# Indiana — Indiana Gaming Commission (IGC)

**Code:** IN · **Products:** sportsbook · **Key authority:** IC 4-38 (Sports Wagering); 68 IAC 27 (Sports Wagering); 68 IAC 15-2 (currency transaction reporting); 68 IAC 6 (Voluntary Exclusion Program)

## Payments-relevant requirements

### Licensing & change management

- Annual certification testing of the sports wagering system by an IGC-approved independent testing laboratory (68 IAC 27-6-1(a)); federal compliance mandated (68 IAC 27-6-4(d)).
- Internal controls must require commission notification of system changes and updates (68 IAC 27-5-2(II)); material changes routed through lab/IGC review per internal controls (tiering not enumerated — confidence MEDIUM).

### Deposits & permitted payment methods

- Permitted funding: cash, cash equivalents, credit/debit cards, promotional funds, sports wagering vouchers, value gaming chips, other IGC-approved methods (68 IAC 27-7-5).
- Credit/debit card wagering REQUIRES an established patron sports wagering account — no cardless/anonymous card wagers (68 IAC 27-7-6).

### Withdrawals & payout timelines

- Refunds for canceled events must be made in full "as soon as reasonably possible" (68 IAC 27-7-10); no fixed day-count withdrawal SLA in 68 IAC 27 — verify in approved internal controls.
- Payouts over $10,000 require additional documented controls (68 IAC 27-5-2(J)); winning tickets expire 1 year after the event (68 IAC 27-5-3).

### Player funds segregation / reserve

- Patron funds defined as cash/cash equivalents held in segregated patron accounts, not commingled with operational funds (68 IAC 27-1-2(25)).
- Reserve of at least $500,000 or the amount sufficient to cover outstanding wagering liabilities, whichever is greater (68 IAC 27-3-1).

### Responsible gambling (deposit/spend/time limits, cooling-off, self-exclusion, reverse withdrawal rules)

- Internal controls must address self-restriction and exclusion procedures and a problem gambling program (68 IAC 27-5-2); IGC's statewide Voluntary Exclusion Program (68 IAC 6) must be enforced across accounts.
- Helpline "1-800-9-WITH-IT" must be displayed prominently (68 IAC 27-7-17).
- Deposit-limit/cooling-off specifics are set via operator internal controls rather than enumerated in 68 IAC 27; no reverse-withdrawal rule found (confidence LOW — verify ICs).

### KYC / age / geolocation

- Age (21+) and identity verification required before account wagering (68 IAC 27-1-2(4) definition; applied via 68 IAC 27-7 account rules).
- Geofence system must detect patron location and block wager attempts from outside Indiana (68 IAC 27-11-1).

### AML overlays (state-specific, beyond federal BSA)

- AML standards required in internal controls, including limits on anonymous kiosk wagering (68 IAC 27-5-2(H)).
- State currency transaction reporting regime: sports wagering payments cross-reference 68 IAC 15-2 CTR requirements (68 IAC 27-7-9) — an IGC reporting overlay parallel to federal Title 31.

### Records, reporting & data

- System malfunctions/deviations retained at least 3 years (68 IAC 27-6-1(c)); transaction report documentation requirements per 68 IAC 27-8-4.

## Code review focus

- Card deposits/wagers only through an established, verified patron account (68 IAC 27-7-6) — no guest-checkout card wagering path.
- Segregated wallet ledger: patron funds never commingled; reserve monitor against max($500k, outstanding liability).
- $10,000+ payout path triggers enhanced controls/documentation; ticket redemption cutoff at 1 year post-event.
- Voluntary Exclusion Program list sync (68 IAC 6): block deposits and wagers, route winnings per VEP forfeiture rules.
- State CTR generation per 68 IAC 15-2 in addition to FinCEN filings — dual-reporting logic for cash-equivalent transactions.
- Event-cancellation refund job: full refunds issued promptly and idempotently to original funding source.

## Sources & confidence

- [68 IAC Article 27 — Sports Wagering rules IGC](https://www.in.gov/igc/files/sportswagering/Rules-for-Sports-Wagering.PDF)
- [68 IAC 27-7-6 — account required for credit/debit card wagering LII](https://www.law.cornell.edu/regulations/indiana/68-IAC-27-7-6)
- [IGC sports wagering emergency rules LSA #21-170E](https://www.in.gov/igc/files/LSA-21-170E-Emergency-Rules-for-Sports-Wagering.pdf)
- Confidence: HIGH on funding methods, account-required card rule, $500k/liability reserve, segregation, annual lab certification, 68 IAC 15-2 CTR cross-reference; LOW on deposit-limit/cooling-off specifics and withdrawal SLAs — confirm against the operator' IGC-approved internal controls.
