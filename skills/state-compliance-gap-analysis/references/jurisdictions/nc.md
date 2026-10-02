# North Carolina — North Carolina State Lottery Commission (NCSLC, ncgaming.gov)

**Code:** NC · **Products:** sportsbook · **Key authority:** N.C.G.S. Chapter 18C, Article 9 (SL 2023-42 / HB 347); NCSLC Sports Wagering Rules Manual (Rules 1A–2D); launched March 2024

## Payments-relevant requirements

### Licensing & change management

- Interactive sports wagering operators licensed by NCSLC; independent testing labs must hold ISO/IEC accreditation and be Commission-approved (Rules Manual 1A-001(22)).
- Formal change management processes for sports wagering systems required (Rule 2D-004) — system/software changes follow the documented CM process and testing regime.

### Deposits & permitted payment methods

- Players may deposit "cash or cash equivalents" into the interactive account (G.S. 18C-912(a)); "cash equivalent" is statutorily defined to include credit cards and debit cards (G.S. 18C-901(2)) — credit cards are permitted.
- Account deposit mechanics governed by Rules Manual 1G-008 (Account Deposits).

### Withdrawals & payout timelines

- Account withdrawals governed by Rule 1G-010; on account termination the player must be given timely ability to access and withdraw remaining funds (G.S. 18C-912(f)). Specific day-count SLA sits in rule text — verify exact number (MEDIUM).

### Player funds segregation / reserve

- Statutory reserve: not less than $500,000 or outstanding liabilities, whichever is greater (G.S. 18C-904(m)); implemented via Rules Manual 1D-013 (Reserve Requirement).

### Responsible gambling (deposit/spend/time limits, cooling-off, self-exclusion, reverse withdrawal rules)

- Responsible gaming limits (deposit/wager/time) required per Rules Manual 1G-013.
- Statewide voluntary exclusion program mandated by G.S. 18C-922 and Rule 1F-002; excluded players must be blocked from wagering (and associated deposits).
- Cooling-off / limit-decrease-immediate, increase-after-delay mechanics expected in rule text (MEDIUM — verify 1G-013 details).

### KYC / age / geolocation

- 21+ and physically located in North Carolina to wager (G.S. 18C-902(c), 18C-912(a)).
- Age and identity verification required before account establishment (Rules Manual 1G-002).
- Geolocation requirements for wagering systems to confine wagers to NC (Rule 2D-005).

### AML overlays (state-specific, beyond federal BSA)

- NC rules expressly impose Bank Secrecy Act compliance (Rule 1D-016) and anti-money-laundering monitoring (Rule 1D-017) as state licensing obligations — federal BSA failures become state rule violations.

### Records, reporting & data

- Commission rules manual covers accounting/records and audit obligations under the 1D series; operators report to NCSLC (specific retention periods — verify, MEDIUM).

## Code review focus

- Credit/debit card deposits allowed; confirm card rails are enabled per 18C-901(2) but still respect any operator/brand-level restrictions.
- Reserve monitoring: liability feed supporting the $500,000-or-liabilities floor under Rule 1D-013.
- Responsible gaming limit engine (1G-013): deposit/wager/time limits enforced server-side; verify limit changes and exclusion states propagate to the payment layer.
- Voluntary exclusion program (1F-002) checked at deposit, wager, and withdrawal-of-promo flows; NC uses a Commission program, not operator-only lists.
- Geolocation check bound to wager placement within NC (2D-005); account creation/deposit from out-of-state handled per rule.
- AML monitoring hooks (1D-016/1D-017): SAR-triggering activity also generates state-facing compliance events/records.

## Sources & confidence

- [G.S. 18C Article 9](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/ByArticle/Chapter_18C/Article_9.html) · [SL 2023-42](https://www.ncleg.gov/EnactedLegislation/SessionLaws/PDF/2023-2024/SL2023-42.pdf)
- [NCSLC Rules Manual for Sports Wagering unofficial copy, 12/18/2023](https://ncgaming.gov/Content/Documents/Unofficial_Copy_of_the_NCSLC_Rules_Manual_for_Sports_Wagering_and_Pari-Mutuel_Wagering_12_18_23.pdf) · [ncgaming.gov sports wagering law](https://ncgaming.gov/sports-wagering-law/) · [ncgaming.gov responsible gaming](https://ncgaming.gov/responsible-gaming/)
- Confidence: statute-level items (credit cards as cash equivalents, $500k reserve, 21+/in-state, voluntary exclusion) are HIGH. Rule-level specifics (withdrawal SLA day-count, limit mechanics, retention periods) are MEDIUM — rule numbers verified but full text should be checked against the current rules manual with the client's compliance team.
