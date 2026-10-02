# Maine — Maine Gambling Control Unit (GCU), Dept. of Public Safety

**Code:** ME · **Products:** sportsbook (mobile + retail, tribal-tied, live since ~Nov 2023); iGaming/online poker legalized (LD 1164, became law w/o signature ~Jan 2026, tribal-exclusive) but **not yet launched** — rules/licensing pending · **Key authority:** 8 M.R.S. ch. 31 (Gambling Control Board) & ch. 35 (Sports Wagering); 16-633 C.M.R. ch. 50-66 (Sports Wagering Rules, eff. 11/1/2023); **LD 2080 (2026) — credit-card deposit ban, sports wagering + iGaming**

## Payments-relevant requirements

### Licensing & change management

- Equipment/software must be certified by a Director-approved independent testing laboratory (incorporating GLI-33 v1.1 Event Wagering Systems standard + GLI-CMP v1.0 Change Management Program Guide) before offering wagering; no wagering without certification (ch. 57 §1-2).
- Internal controls must be submitted for and receive Director approval before wagering commences (ch. 53 §2); amendments filed on form MGCU-8400 with strike-through/underline markup, Director targets a determination within 30 days, no change effective until approved in writing (ch. 53 §8-9).
- Primary wagering server must be physically located in Maine with 24-hour surveillance and Director access on request (ch. 57 §6).
- Geolocation systems must independently certify (ch. 62 §6) and the supplier must itself be licensed as a sports wagering supplier (ch. 62 §5).

### Deposits & permitted payment methods

- Mobile account funding sources (ch. 60 §7): patron's deposit account; cash/gaming chips deposited at a facility lounge; promotional/bonus credit; winnings; operator adjustments with documented patron notification; or any other Director-approved means. Rule text does not itself enumerate "credit card" or "debit card" as a named mobile funding rail.
- Retail lounge wagers (ch. 58 §11): cash, cash equivalent, promotional funds, sports wagering vouchers/tickets, value casino gaming chips, or other Director-approved means — no card payment rail named for in-person wagering.
- Operator-extended credit to a patron's sports wagering account is strictly prohibited (ch. 60 §14) — this is about the operator floating credit, distinct from card-network funding.
- **LD 2080, signed by Gov. Mills 4/3/2026 (sponsor Rep. Marc Malon): prohibits licensed operators and management services providers from accepting credit cards to fund BOTH sports wagering and internet gaming (iGaming) accounts** — explicitly targeting branded/rewards-linked cards as well as general credit-card funding. Effective 90 days after the 132nd Legislature's second session adjourned sine die on 4/29/2026, i.e. **≈ 7/28/2026 — by the current date this file was written (8/26/2026) the ban should already be in force** (MEDIUM confidence on the exact calculated date — verify the enacted effective date against the Public Law chapter number with the GCU or Maine Secretary of State; statute section amended not confirmed, mark LOW + verify). Debit cards, ACH/bank transfer, and cash remain permitted.

### Withdrawals & payout timelines

- **No explicit statutory or rule-based payout SLA (e.g., a "must pay within N hours/days of demand" clause) was located in 16-633 C.M.R. ch. 50-66** — unlike Colorado's 24-hour or Maryland's 7-day rules, Maine's regulations appear silent on a numeric withdrawal-processing deadline (confidence LOW — verify against any GCU internal-control template or bulletin not indexed here; industry reporting shows real-world operator payout times in ME ranging ~24 hours to 7 business days by method, which is operator practice, not a codified requirement).
- ch. 64 §6(E): promotions/bonuses may NOT restrict a patron from withdrawing the patron's own funds or winnings from bets placed with the patron's own funds; ch. 64 §5(D) requires any withdrawal restriction to be disclosed in the offer terms.
- ch. 60 §20: on patron-initiated account closure, any remaining balance must be refunded per the operator's approved internal controls.
- ch. 60 §28(C): even a suspended account must permit withdrawal once the operator determines the funds have cleared and the suspension reason wouldn't otherwise prohibit it (negative-balance suspensions are the main carve-out).
- ch. 60 §11: system must detect/prevent any wagering or withdrawal activity that would drive a patron's account balance negative.

### Player funds segregation / reserve

- ch. 60 §21: operators must obtain a **$500,000 surety bond** (A-rated-or-better carrier, licensed/admitted in Maine, Director as obligee, annually renewable, cancellable only with Director approval) specifically to fund the reserve.
- ch. 60 §22-23: additionally maintain a reserve (cash, cash equivalents, and/or irrevocable letter of credit) ≥ outstanding liability, where outstanding liability = patron account balances + aggregate wagers on undetermined outcomes + unpaid winning wagers.
- ch. 60 §24: Director approval required before withdrawing/releasing reserve funds in excess of the requirement.
- ch. 60 §25: reserve requirement recalculated daily; a shortfall must be reported to the assigned Unit auditor within 24 hours along with remediation steps; reserve funds held only at an FDIC/NCUA-insured institution lawfully operating in Maine.
- ch. 60 §18: a segregated account (separate from all other operating accounts) must be ≥ the sum of the daily ending cashable balance of all patron accounts + funds on game + pending withdrawals; operator must have unfettered access to account/transaction data to verify sufficiency; a **monthly attestation** of safeguarding is filed with the Director.

### Responsible gambling

- ch. 63: a responsible wagering program is required at licensure and maintained continuously; amendments need Director approval ≥30 calendar days before the effective date.
- Unauthorized (self-exclusion) list: requestable in person at a GCU office/licensed facility, via a Problem Gambling Services Provider (Maine CDC affiliate) office, or online; terms of 1/3/5 years that auto-terminate at month-end, or (after completing a term) a lifetime option requiring 10 years before a removal request may be made (ch. 63 §2.H-J). List is maintained by GCU and pushed to operators monthly (ch. 63 §3).
- ch. 63 §4: restriction options must be offered at minimum on wager amounts, wagering time, deposit amounts, and session time.
- 1-800-GAMBLER helpline disclosure required on ads/site (ch. 63 §5, ch. 64 §3.I); RG messaging font size must be ≥ the majority body text size (ch. 63 §6).
- ch. 60 §27: patron-requested account suspension (a self-imposed "time-out") must be honored for a minimum of 72 hours; while suspended, deposits/wagers/withdrawals/account changes/closure are blocked per ch. 60 §28 (deposits are permitted only to zero out a negative balance).
- Winnings are subject to interception for child support debt under 8 M.R.S. §1217 (ch. 53 §4.M, ch. 63 §2.I).

### KYC / age / geolocation

- ch. 60 §5.A: electronic patron file must capture legal name, DOB, full or last-4 SSN (or foreign-patron passport/TIN equivalent), account number, residential address (no PO box), email, phone, ID-verification method, and verification date.
- ch. 60 §5.B: SSN/equivalent, passwords/PINs, and credit/debit card numbers or bank account/financial info must be **encrypted** in the patron file.
- Identity verified via examined government-issued credential or remote multi-source authentication (incl. third-party/governmental databases) approved by the Director (ch. 60 §5.C); password + MFA or equivalent required (ch. 60 §5.D); patron confirmed 21+ and not on the unauthorized list (ch. 60 §5.E).
- One non-transferable account per patron per operator (ch. 60 §6); re-verification required on reasonable suspicion of compromise (ch. 60 §19); 15-minute inactivity timeout requiring re-authentication (ch. 60 §15).
- ch. 62: geolocation check required before the first wager of a session, recurring rechecks (≤20 min for static connections, 5 min if within 1 mile of the state border; velocity-based intervals for mobile connections, capped at 20 min), and a mandatory recheck on any IP address change; up to 5 rechecks in 5 minutes permitted on momentary location loss before wagering must cease.
- All wagers must be initiated/received/made within Maine (ch. 57 §4), consistent with UIGEA's routing-doesn't-determine-location framing.

### AML overlays

- ch. 53 §4.J requires documented federal + state AML compliance standards, specifically: a process for wagers/payouts over $10,000; a log of wagers ≥ $5,000; detection of structured multiple wagers within a 24-hour period used to evade reporting; and a reporting-to-authorities process.
- ch. 60 §17.E flags patron activity originating from an OFAC-restricted region as a "high-risk transaction" requiring enhanced mitigation (biometrics/device fingerprinting/location intelligence); ch. 60 §26 requires SAR capability and real-time fraud/AML monitoring including fraudulent chargebacks and payment fraud detection.
- No Maine-specific AML statute beyond the federal BSA/SAR framework was located — the state overlay appears to be these rule-level reporting/logging thresholds rather than an independent state AML statute (confidence LOW/MEDIUM — verify with compliance/legal).

### Records, reporting & data

- 5-year retention: all transactional wagering data (ch. 57 §7, ch. 53 §4.S); system malfunction/deviation logs (ch. 57 §5); advertising/marketing materials and targeting logs (ch. 64 §1); complaint/dispute correspondence (ch. 66 §8).
- 14-calendar-day minimum retention for continual video surveillance recordings of wagering areas (ch. 53 §4.K.6).
- Dormant accounts (no activity for 1 year) must be closed out and remaining funds returned to the patron (ch. 53 §4.T).
- Account statements: detailed activity for the trailing 6 months (as of 24 hours before the request) on demand, plus a past-year summary statement on request (ch. 60 §16).
- Patron complaint response within 10 calendar days generally (ch. 53 §7); the dedicated complaints chapter sets a 48-hour acknowledgment + 10-business-day substantive response with a copy to the Director, a further 10-business-day Director decision window on appeal, and a right of appeal to the Commissioner of Public Safety and ultimately Superior Court (ch. 66 §3-7).

## Code review focus

- **Date-gate a credit-card deposit block for ME** (LD 2080) — likely already required given the ~7/28/2026 calculated effective date vs. today; verify the exact enacted date and treat any legacy "credit card allowed" branch as stale for ME across both sports wagering AND any future iGaming/casino product.
- No coded payout-timeline SLA exists for ME in the regs as researched — do not assume a CO/MD-style hard deadline; confirm with compliance whether an internal-controls commitment (per-operator, Director-approved) imposes one privately, since ch. 53 requires the operator's own internal controls to be filed and followed.
- Reserve/liability engine: daily calculation feed (account balances + open-wager liability + unpaid winnings) against the $500k bond + reserve floor, with 24-hour shortfall alerting to the Unit auditor, and a monthly safeguarding attestation artifact.
- Segregated-account balance check ≥ (daily ending cashable balances + funds on game + pending withdrawals), independent of the reserve calc above.
- Self-exclusion / voluntary-suspension state machine: 72-hour minimum patron-requested suspension, asymmetric account state (block deposit/wager/withdraw/close/edit, but allow the negative-balance-cure exception), and auto-expiry logic keyed to term length (1/3/5-year or lifetime with 10-year minimum before removal).
- Encryption-at-rest verification for SSN/equivalent, password/PIN, and card/bank account fields in the patron file (ch. 60 §5.B) — a strict superset of typical PCI scope since SSN and bank routing/account numbers are explicitly named.
- Geolocation gate wired into wager placement with the specific recheck cadence (≤20 min / 5 min near border / on IP change) rather than a generic "checked once per session" gate.
- OFAC-region and high-risk-transaction flagging (funding-method changes, withdrawal-method changes, large withdrawals) feeding the fraud/AML monitoring pipeline, distinct from the $10k payout / $5k wager-log AML thresholds.
- Dormant-account sweep (1-year inactivity → close + refund) and 6-month/1-year account-statement generation as backend jobs, not just UI features.

## Sources & confidence

- [16-633 C.M.R. Sports Wagering Rules, Chapters 50-66 Maine DPS/GCU, eff. 11/1/2023, full consolidated PDF](https://www.maine.gov/dps/sites/maine.gov.dps/files/inline-files/Sports%20Wagering%20Rules%2011.1.23.pdf)
- [Chapter 60: Sports Wagering Accounts standalone PDF](https://www.maine.gov/dps/sites/maine.gov.dps/files/inline-files/Chapter%2060%20Wagering%20Accounts.pdf)
- [Maine Gambling Control Unit — Sports Wagering hub](https://www.maine.gov/dps/gcu/sports-wagering) · [Sports Wagering Statute and Rules index](https://www.maine.gov/dps/gcu/sports-wagering/sports-wagering-statute-and-rules)
- [8 M.R.S. Chapter 31: Gambling Control Board Maine Legislature](https://legislature.maine.gov/statutes/8/title8ch31sec0.html)
- [Governor signs Malon's bill to protect Maine consumers from gambling addiction — Maine House Democrats official, LD 2080 signing details](https://www.maine.gov/housedems/news/governor-signs-malons-bill-protect-maine-consumers-gambling-addiction)
- [Legal Sports Report — Maine governor signs sweepstakes and credit-card bans into law](https://www.legalsportsreport.com/259771/maine-governor-signs-sweepstakes-credit-card-bans-into-law/) (secondary; corroborates LD 2080 scope)
- [Pokerfuse — Maine Online Poker: Legal Status, Launch Timeline & MSIGA Outlook 2026](https://pokerfuse.com/online-poker/maine/) (LD 1164 iGaming legalization, tribal-exclusive, not yet launched)
- Confidence: HIGH on account-establishment/KYC fields, reserve/bond structure, segregated-account rule, dormant-account rule, self-exclusion term structure, geolocation cadence, AML reporting thresholds, complaint-response timelines — all read directly from the consolidated rules PDF via primary-source extraction. MEDIUM on the LD 2080 exact effective date (calculated as 90 days from the 4/29/2026 sine die adjournment; the Public Law chapter/statute-section citation was not independently confirmed — verify with GCU or Maine Sec. of State before treating 7/28/2026 as authoritative). LOW: no explicit payout/withdrawal-timeline SLA was found in the current rules — flagged as a genuine regulatory gap rather than a research miss, but verify against any non-public internal-controls template. LOW: state-specific AML statute beyond the rule-level BSA/SAR thresholds not confirmed — verify with compliance/legal before asserting "no state AML overlay."
