# Maryland — Maryland Lottery and Gaming Control Agency / Commission (MLGCA/MLGCC)

**Code:** MD · **Products:** sportsbook · **Key authority:** Md. Code, State Gov't Title 9, Subtitle 1E; COMAR 36.10 (esp. 36.10.13, 36.10.14, 36.10.18)

## Payments-relevant requirements

### Licensing & change management

- COMAR 36.10.18.03: platform and updates must be submitted "to an independent certified testing laboratory prior to their use for sports wagering"; software validated at least every 24 hours via cryptographic hash to detect unauthorized modification.
- Odds/material transaction aspects may not be altered post-acceptance without Commission approval.

### Deposits & permitted payment methods

- COMAR 36.10.18.05(H): debit cards, credit cards (subject to 36.10.13.28), electronic bank transfers, online/mobile payment systems, winnings, bonuses, non-transferable reloadable prepaid cards; Commission may approve others.
- 36.10.13.28: retail/in-person wagers may NOT be accepted by credit card or EFT from a credit card; ONLINE operators MAY accept credit card funding but must require the bettor to acknowledge the transaction may be treated as a cash advance with additional fees.

### Withdrawals & payout timelines

- 36.10.18.05(J): "Within 7 days of a bettor request for withdrawal of funds, the sports wagering licensee shall complete the withdrawal," unless a pending unresolved dispute or investigation; withdrawal rails mirror funding (cash, check, wire, electronic transfer) (36.10.18.05(I)).

### Player funds segregation / reserve

- COMAR 36.10.14.06: reserve ≥ $500,000 AND ≥ (liability on pending/undetermined wagers + unpaid winnings), recalculated daily; forms = cash (FDIC-insured institution), cash equivalents, irrevocable LOC, surety bond; no withdrawal from reserve without written Commission approval; shortfall notice to Commission within 24 hours.
- 36.10.13.40 imposes security-of-funds-and-data obligations on licensees.

### Responsible gambling (deposit/spend/time limits, cooling-off, self-exclusion, reverse withdrawal rules)

- Statewide voluntary exclusion program administered by MLGCA (COMAR 36.01.03); on self-exclusion with pending wagers, "the funds and account balance shall be returned to the bettor" (36.10.18.03).
- 36.10.13.41 consumer protection: facility ATM cash withdrawal cap of $2,500 per sports wagering day; ATMs may not accept temporary-cash-assistance benefit cards; promotion terms filed 2 days ahead with clear cancellation method and 1-800-GAMBLER messaging.
- Self-imposed deposit/wager/time limit offering expected under responsible gaming plan requirements — exact cite not verified, confidence LOW.

### KYC / age / geolocation

- 36.10.18.05(C): identity verified via government-issued credential or multi-source authentication (third-party + governmental databases); one account per licensee (G); account lock after 3 failed logins with MFA to recover/reset (S); immediate re-verification if compromise suspected (P); 21+.
- 36.10.18.03: all wagers must be initiated, received and otherwise made within Maryland (geofencing).

### AML overlays (state-specific, beyond federal BSA)

- No distinct state AML program verified beyond federal BSA; state overlay is limited to security-of-funds rules, benefits-card blocking and Commission reporting — confidence LOW/MEDIUM.

### Records, reporting & data

- Daily reserve recalculation records, 24-hour software hash-validation logs, promotion filings, and Commission audit access; account transaction records per 36.10.18.05.

## Code review focus

- Credit card deposit path (online only) must display and record a cash-advance-fee acknowledgment before first (ideally every) credit card deposit; block credit cards entirely for retail wagering flows.
- Withdrawal SLA: complete within 7 days; only dispute/investigation status may pause the clock.
- Single-account enforcement per patron; lockout after 3 failed logins; MFA on credential recovery/reset.
- Daily reserve/liability calculation feed (account balances + pending wager liability + unpaid winnings) with $500k floor and 24-hour shortfall alerting.
- Geolocation gate on wager placement and account funding events; block out-of-state transactions.
- Self-exclusion flow: immediately settle/void pending wagers and auto-return full account balance to the bettor.

## Sources & confidence

- [COMAR 36.10.18.05 Bettor Accounts Cornell LII](https://www.law.cornell.edu/regulations/maryland/COMAR-36-10-18-05) · [COMAR 36.10.13.28 Use of Credit regs.maryland.gov](https://regs.maryland.gov/us/md/exec/comar/36.10.13.28) · [COMAR 36.10.14.06 Reserve Justia](https://regulations.justia.com/states/maryland/title-36/subtitle-10/chapter-36-10-14/section-36-10-14-06) · [COMAR 36.10.18.03 Platform Requirements Cornell LII](https://www.law.cornell.edu/regulations/maryland/COMAR-36-10-18-03) · [COMAR 36.10.13.41 Consumer Protection Cornell LII](https://www.law.cornell.edu/regulations/maryland/COMAR-36-10-13-41) · [36.10.13.40 Security of Funds](https://regs.maryland.gov/us/md/exec/comar/36.10.13.40)
- HIGH: 7-day withdrawal, $500k+ daily reserve, credit card cash-advance acknowledgment, single account, MFA/lockout. Verify with compliance team: whether any post-2025 rulemaking restricts credit cards further, self-imposed limit cites, dormant-account treatment.
