# Pennsylvania — Pennsylvania Gaming Control Board (PGCB)

**Code:** PA · **Products:** sportsbook + iGaming · **Key authority:** 4 Pa.C.S. Ch. 13B (interactive gaming) & Ch. 13C (sports wagering) + 58 Pa. Code Part VII (esp. Subpart L "a" chapters: 809a–812a interactive gaming; Chapters 1401a–1408a sports wagering)

## Payments-relevant requirements

### Licensing & change management

- iGaming operates under an interactive gaming certificate (land-based licensee) with interactive gaming operator licenses for platforms; sports wagering under a sports wagering certificate/operator license. Suppliers of payment-adjacent services generally need gaming service provider certification or registration (58 Pa. Code Ch. 437a; sports wagering service providers per § 1405a.1) — confirm the exact tier for a pure payment processor with compliance (MEDIUM confidence on tier).
- All interactive games/platforms must pass testing under 58 Pa. Code Chapter 810a (Interactive Gaming Testing and Controls) before use, including software authentication (§ 810a.6) and RNG standards (§ 810a.5); PGCB uses Board-approved/registered gaming labs (GLI, BMM et al.).
- Changes/modifications to an interactive game "shall be handled in accordance with the Change Management guidelines" issued by PGCB to certificate holders, operators, and manufacturers (§ 810a.7) — i.e., PA change control lives in Board-issued guidelines, not in the code itself; obtain the current PGCB Change Management guidelines (HIGH confidence on § 810a.7 text, the guideline content itself must come from PGCB/compliance).
- Player-file encryption is subject to annual verification tied to § 809a.6 software authentication obligations (per § 812a.2(d)) — verify current scope (MEDIUM).

### Deposits & permitted payment methods

- Permitted funding (§ 812a.7(a)): cash deposits with the certificate holder/operator; personal checks, cashier's checks, money orders, wire transfers; credit cards and debit cards (including prepaid); cash/vouchers/chips at approved cashiering locations; verified non-transferable reloadable prepaid cards; complimentaries, promotional or bonus credit; winnings; ACH (with fraud-prevention controls); documented dispute adjustments; other Board-approved means. Credit cards are allowed.
- No extension of credit to players, and no deposits derived from credit extended by affiliates (§ 812a.7(b)).
- A player account may not carry a negative balance as a result of any wager (§ 812a.7(c)).
- Account adjustments under $500 require periodic supervisory review; larger adjustments require prior supervisory authorization (§ 812a.7(f)).
- No wagers may be accepted from self-excluded/excluded persons or certain prohibited licensed employees (§ 812a.7(e)).

### Withdrawals & payout timelines

- Permitted withdrawal channels (§ 812a.10(c)): funding of game play; cage cash-out; check issuance; transfer to reloadable prepaid card; transfer to a verified bank account; documented dispute adjustments; other Board-approved means.
- Operators must establish withdrawal protocols and controls preventing unauthorized withdrawals (§ 812a.10); the regulation sets NO explicit day-count deadline for completing withdrawals — internal controls and Board guidance govern speed (HIGH confidence that no day-count appears in § 812a.10; confirm any guidance-based SLA with compliance).
- Player-to-player fund transfers are prohibited (§ 812a.10(d)).
- Reverse withdrawals are not expressly regulated in § 812a.10 — treat cancellation-of-withdrawal features as a compliance question for PGCB guidance (LOW confidence area).

### Player funds segregation / reserve

- Interactive gaming certificate holders/operators must maintain a bank account for player funds separate from all other operating accounts (§ 811a.5).
- The segregated balance must at all times be ≥ the sum of the daily ending cashable balance of all player accounts, funds on game, and pending withdrawals (§ 811a.5).
- The CFO must file a quarterly attestation with the Board that player funds are safeguarded; the operator must have unfettered access to account/transaction data to prove sufficiency (§ 811a.5).
- Sports wagering has a parallel segregation/reserve rule at § 811.5 (sports wagering accounting chapter) (MEDIUM confidence on exact parallel cite).

### Responsible gambling

- Required configurable player controls (§ 812a.9(g)): daily/weekly/monthly deposit limits; daily/weekly/monthly spend (at-risk) limits; single-wager limit (not applicable to peer-to-peer poker); daily time-based limits.
- Limit decreases take effect immediately upon next login; increases take effect only after the previous limit's time period has expired (§ 812a.9(g)(1)); a single-wager limit increase additionally requires a 24-hour waiting period (§ 812a.9(g)(4)(ii)).
- Cooling off: players must be able to suspend their account for a defined period or indefinitely (§ 812a.9(i)(1)); during suspension no new bets or deposits, but withdrawals of remaining funds stay available (§ 812a.9(i)(2)(i)).
- PGCB maintains a distinct iGaming self-exclusion list (separate from the casino list); operators must check it and deny accounts/wagers to listed persons (§ 812a.6, § 812a.7(e)) (list-separation detail: MEDIUM confidence).
- Responsible gaming page with risk information, protective measures, and unauthorized-use detection mechanisms must be displayed (§ 812a.9(e)(3)).
- Dormant and suspended account handling per §§ 812a.12–812a.13 (details not verified here — pull full text before coding against them).

### KYC / age / geolocation

- Account registration before any interactive gaming: legal name, DOB, last four of SSN (or foreign equivalent), address, email, phone, plus any data needed to verify identity; verification must complete at account setup, before play (§ 812a.2(a)-(b), (e)-(f)).
- Minimum age 21; registration barred for self-excluded/prohibited persons (§ 812a.2(f)).
- All player file information must be encrypted (§ 812a.2(d)).
- Wagers only from within Pennsylvania via geolocation controls (4 Pa.C.S. Ch. 13B and platform requirements in Ch. 809a) — exact section not verified here (MEDIUM confidence).

### AML overlays (state-specific)

- Federal BSA/Title 31 applies; PA regulations layer internal-controls and reporting duties (accounting chapters 811a/811) but the research did not surface a PA-unique SAR/CTR overlay beyond federal law — treat as federal-baseline plus internal controls, and confirm PGCB expectations for suspicious-transaction notification (LOW confidence).

### Records, reporting & data

- Required reports and reconciliation of interactive gaming accounts per § 811a.9 (daily/periodic reconciliation reports to the Board) — pull full text for report inventory (MEDIUM).
- Quarterly CFO attestation on player-fund safeguarding (§ 811a.5).
- Use of player data restricted per § 812a.14; account statements must be available to players per § 812a.11.

## Code review focus

- Verify limit engine: increases dormant until prior period expiry; single-wager limit increases additionally gated by a 24-hour delay; decreases effective at next login.
- Verify no code path allows a negative account balance from wager settlement, and no credit extension or affiliate-credit-funded deposits.
- Confirm adjustment workflow: adjustments ≥$500 require prior supervisory authorization recorded before posting; <$500 flagged for periodic supervisory review.
- Confirm suspension/cooling-off state blocks deposits and wagers but still permits withdrawal of remaining balance.
- Check self-exclusion screening uses the PA-specific iGaming self-exclusion list at registration, deposit, and wager acceptance.
- Verify player-fund ledger supports the § 811a.5 sufficiency test (daily ending cashable balance + funds on game + pending withdrawals) and feeds the quarterly attestation.
- Confirm deployments touching wagering/payment logic follow PGCB Change Management guidelines (lab re-certification for regulated components) before production release.
- Ensure player file fields (SSN last-4, financial data) are encrypted at rest and player-to-player transfers are impossible.

## Sources & confidence

- [58 Pa. Code Ch. 812a section list Cornell LII](https://www.law.cornell.edu/regulations/pennsylvania/title-58/part-VII/subpart-L/chapter-812a) · [§ 812a.7 Player funding](https://www.law.cornell.edu/regulations/pennsylvania/58-Pa-Code-SS-812a-7) · [§ 812a.10 Player withdrawals](https://www.law.cornell.edu/regulations/pennsylvania/58-Pa-Code-SS-812a-10) · [§ 812a.9 Player account controls](https://www.law.cornell.edu/regulations/pennsylvania/58-Pa-Code-SS-812a-9) · [§ 812a.2 Registration](https://www.law.cornell.edu/regulations/pennsylvania/58-Pa-Code-SS-812a-2) · [§ 811a.5 Segregation & reserve](https://www.law.cornell.edu/regulations/pennsylvania/58-Pa-Code-SS-811a-5) · [Ch. 810a Testing & Controls](https://www.law.cornell.edu/regulations/pennsylvania/title-58/part-VII/subpart-L/chapter-810a) · [§ 810a.7 Changes to game](https://www.law.cornell.edu/regulations/pennsylvania/58-Pa-Code-SS-810a-7) · [PGCB sports wagering temporary regulations Ch. 1401a et seq.](https://pgcb.pa.gov/files/legislation/125-220_temp_Sports_Wagering.pdf)
- Confidence: HIGH on §§ 812a.2/812a.7/812a.9/812a.10/811a.5/810a.7 items (verified text); MEDIUM on service-provider tiering, sports-wagering parallel cites, geolocation cite, self-exclusion list mechanics; LOW on AML overlay and reverse-withdrawal treatment — route those to the client's compliance team and obtain the current PGCB Change Management guidelines.
