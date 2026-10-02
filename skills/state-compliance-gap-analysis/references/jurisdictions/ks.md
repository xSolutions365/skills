# Kansas — Kansas Lottery / Kansas Racing and Gaming Commission (KRGC)

**Code:** KS · **Products:** sportsbook · **Key authority:** K.S.A. 74-8783 et seq. (2022 SB 84); K.A.R. Agency 112, Arts. 112-201 (operations) & 112-203 (technical)

## Payments-relevant requirements

### Licensing & change management

- Sports wagering is state-owned via the Kansas Lottery; platforms operate under casino-manager contracts and KRGC certification — payments stack is part of the certified platform.
- Change management must follow GLI's Change Management Program Guide (GLI-CMP v1.0) with annual audits (K.A.R. 112-203-2); platforms must be certified to GLI-33 by an approved lab before operation (K.A.R. 112-203-7).
- Primary wagering servers must be located in Kansas with executive director approval (K.A.R. 112-203-5).

### Deposits & permitted payment methods

- K.A.R. 112-201-5 permits: cash/cash equivalents, electronic bank transfers (incl. via third parties), wire transfers, debit AND credit cards, online/mobile payment systems, promotional credits, and other executive-director-approved methods.
- Credit cards are expressly permitted in Kansas (unlike Tennessee).

### Withdrawals & payout timelines

- Withdrawals must be completed within 5 calendar days of request (K.A.R. 112-201-14); may be delayed only on a good-faith fraud/illegality belief, with investigation status updates every 10 days.

### Player funds segregation / reserve

- Reserve of not less than the greater of $500,000 or the amount covering unclaimed winnings and future liability; forms: cash, cash equivalents, letter of credit, bond, or combination (K.A.R. 112-201-3).

### Responsible gambling (deposit/spend/time limits, cooling-off, self-exclusion, reverse withdrawal rules)

- Voluntary/self-exclusion: once exclusion is executed, no new wagers OR deposits may be accepted until revocation (K.A.R. 112-201-22).
- If a self-excluding patron has pending wagers, winnings are diverted to the state problem gambling grant fund (K.A.R. 112-201-5).
- Player-set deposit/time limit tooling is expected via internal controls; specific limit-rule citation not verified — confirm with compliance (LOW).

### KYC / age / geolocation

- Full identity verification required before wagering; 21+ only; platform must deny deposit access to anyone indicating underage status (K.A.R. 112-201-5).
- Geolocation must reasonably detect patron location (IP, cell trilateration, WiFi, GPS) and block out-of-state wagers; geolocation systems require approved-lab certification (K.A.R. 112-203-6).

### AML overlays (state-specific, beyond federal BSA)

- Primarily federal BSA/FinCEN regime; state overlay is via internal control standards and reporting to KRGC — no distinct Kansas AML statute identified for sports wagering (LOW; verify ICS obligations).

### Records, reporting & data

- Internal controls and transaction records subject to KRGC audit; annual GLI-CMP change-management audit evidences software change history (K.A.R. 112-203-2).

## Code review focus

- Deposit method allow-list includes credit cards (permitted here) but must be state-configurable so the same gateway can disable them for TN.
- Withdrawal pipeline SLA: request-to-completion within 5 calendar days; delayed-withdrawal path requires fraud-flag justification and recurring (10-day) case updates.
- Self-exclusion check gates BOTH deposits and wagers; pending-wager winnings for self-excluded users route to a state fund, not the player balance.
- Age/identity verification hard-gate before first deposit/wager; underage-indicative registrations must be denied, not just flagged.
- Geolocation re-check on wager placement (not only login); out-of-state attempts blocked and logged.
- Software release process tags payment-affecting changes for GLI-CMP change classification and lab certification before production.

## Sources & confidence

- [KRGC temporary sports wagering regulations, Kansas Register Vol. 42 Issue 44](https://sos.ks.gov/publications/Register/Volume-42/Issues/Issue-44/11-02-23-51626.html)
- [KRGC sports wagering regulations page](https://krgc.kansas.gov/legal/regulations/sports-wagering/) · [SB 84 2022](https://www.kslegislature.gov/li_2022/b2021_22/measures/documents/sb84_00_0000.pdf) · [AGA Kansas fact sheet](https://www.americangaming.org/wp-content/uploads/2025/02/Kansas_AGA-Gaming-Regulatory-Fact-Sheet-Kansas-2025.pdf)
- Confidence: funding methods, 5-day withdrawal, $500k reserve, GLI-33/GLI-CMP, 21+ and geolocation are HIGH (regulation text via Kansas Register). Deposit-limit tooling details and state AML overlay are LOW — verify against current permanent K.A.R. text and operator ICS with the client's compliance team.
