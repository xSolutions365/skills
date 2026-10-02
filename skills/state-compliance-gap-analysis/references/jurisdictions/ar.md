# Arkansas — Arkansas Racing Commission (ARC)

**Code:** AR · **Products:** sportsbook (retail + mobile; no online casino/iGaming) · **Key authority:** Ark. Const. Amend. 100 (2018, "Arkansas Casino Gaming Amendment"); Ark. Code Ann. Title 23, Ch. 117 (Casino Gaming); Arkansas Racing Commission Casino Gaming Rules, codified at 23 CAR Ch. 238 (Code of Arkansas Rules) / Ark. Admin. Code 006.06.21 — mobile ("online sports pool") wagering launched 3/20/2026 via FanDuel and DraftKings, each partnered with a licensed casino (Oaklawn, Southland)

## Payments-relevant requirements

### Licensing & change management

- Only the state's licensed casinos (Oaklawn, Southland, Saracen) may hold a sports-pool license; a casino must already operate and continue operating an in-person sports pool before it (or a third-party "online sports pool" partner such as FanDuel/DraftKings) may offer mobile wagering.
- Unlike the standard "skin fee" model used elsewhere, the casino licensee must retain **at least 51% of net revenue** from any mobile sports-wagering partnership — a revenue-share floor, not a pure platform-certification regime (secondary-source confirmed, MEDIUM — verify exact percentage against current ARC-approved agreements).
- No independent-testing-lab certification requirement or defined change-tiering for platform updates was located in the sections reviewed (confidence LOW — verify against the full current Casino Gaming Rules text; AR's rule book is shared across pari-mutuel, table games, and sports wagering, so relevant certification language may sit in a section not yet located).

### Deposits & permitted payment methods

- General rule: "Deposits, withdrawals, credits, and debits to wagering accounts shall be made in accordance with these Rules" — the enumerated list of permitted instruments for **individual** patron accounts was not located in the sections reviewed (confidence LOW — verify; no explicit credit-card ban language found, unlike CO/MD).
- **Notable outlier:** AR's account-wagering rule text permits wagering-account transactions funded by "the extension of credit to the patron by the licensee" under Commission-approved terms — i.e., licensee-extended credit financing of wagers, which most other legal sports-betting states explicitly prohibit as an RG safeguard (secondary-source + partial primary-text corroboration, MEDIUM/LOW — confirm this applies to the *sports* wagering account rule specifically and not only the off-track pari-mutuel account-wagering rule it was sourced from).
- **Business-entity accounts** (non-individual wagering accounts) are restricted: deposits and withdrawals "may only be made by transfers to and from the bank or financial institution account maintained by the business entity" and "may not be made in cash" (HIGH — explicit rule text).

### Withdrawals & payout timelines

- No fixed regulator-mandated withdrawal SLA (unlike CO's 24-hour or MD's 7-day rule) was located. The rule instead requires the licensee to "comply with a request for a withdrawal of funds by a patron from the patron's wagering account in accordance with the terms of the wagering account agreement between the licensee and its patron," unless there is a pending unresolved player dispute or investigation (MEDIUM — this is itself notable: the SLA is contract-defined by the operator's own account-agreement terms rather than a statewide fixed clock, so verify each operator's filed wagering-account-agreement SLA rather than assuming a state-set number).

### Player funds segregation / reserve

- "Each book shall at all times maintain a reserve of not less than the greater of $25,000 or the sum of" patron wagering-account balances, amounts accepted on wagers not yet determined, and amounts due on determined wagering events; acceptable forms are cash, cash equivalents, an irrevocable letter of credit, a bond, or a combination (MEDIUM/HIGH — text confirmed sourced from the account-wagering rule; verify identical language appears in the sports-wagering-specific rule section rather than only the off-track pari-mutuel section it was drawn from). The **$25,000 floor is materially lower** than CO's liability-based reserve or MD's $500,000 floor — flag for compliance review if this is unexpectedly low relative to AR wagering volume.

### Responsible gambling (limits, cooling-off, self-exclusion, reverse-withdrawal)

- Self-exclusion (23 CAR § 358-514): licensee must maintain a **register** of self-excluded individuals (name, address, account details), **close the interactive gaming account** of anyone who self-excludes, bar re-enrollment in gambling until **at least 30 days** have passed, and take reasonable steps to stop marketing material reaching self-excluded individuals (HIGH — explicit rule text).
- No patron-settable deposit/spend/time-limit provision, cooling-off mechanism, or reverse-withdrawal rule was located in the sections reviewed (confidence LOW — verify; AR's RG framework may be thinner than CO/MD's or simply not yet indexed by the sources checked).

### KYC / age / geolocation

- Minimum wagering age is 21 (widely corroborated secondary sources; confidence MEDIUM — verify against current Title 23 Ch. 117 text).
- Enhanced KYC triggers at high-value wagers: before accepting a wager **over $10,000**, the book must obtain the patron's name, permanent address, SSN or passport number, and a government-issued ID, and examine that credential to verify identity (HIGH — explicit rule text, Casino Gaming Rule 20).
- Remote/mobile wagers may only be accepted from patrons **physically present in Arkansas** at the time of the wager. Notably, the "reasonable assurance of patron location" standard cited in the account-wagering rule includes "an inquiry process through electronic or voice-only means in which patrons affirm their physical location at the time of each wagering communication" — i.e., the rule text contemplates patron self-affirmation as a compliant method, not necessarily mandating third-party GPS/geofencing tech (MEDIUM — verify current ARC guidance on accepted geolocation vendors/methods for mobile sports wagering specifically, since this text was sourced from the account-wagering rule).

### AML overlays (state-specific, beyond federal BSA)

- No AR-specific AML program beyond federal BSA/CTR obligations was located. The $10,000-wager KYC trigger functions similarly to a CTR threshold but is framed as a per-wager identity-verification rule, not a confirmed aggregated-transaction reporting regime (confidence LOW/MEDIUM — verify with compliance team whether ARC layers any additional SAR/CTR-style reporting on top of federal requirements).

### Records, reporting & data

- Wagering-account rules (the operator's own account-agreement terms) must be submitted to the Commission for approval before adoption or amendment.
- Licensees must maintain records of gaming-credit collection arrangements and contracts available for ARC inspection.
- No explicit retention period (e.g., CO's 3-year malfunction-log rule) was located for sports-wagering records specifically (confidence LOW — verify).

## Code review focus

- **New-state onboarding check:** AR mobile sports wagering only went live 3/20/2026 — confirm AR is actually present in the platform's per-state jurisdiction/feature-flag config, payment-method rail table, and reserve-calc engine; do not assume it inherited defaults correctly from a template state.
- **Credit-funded-deposit outlier:** if the code has a global "licensee-extended-credit" or BNPL-style deposit rail that is blocked by default for RG reasons, AR may be the one state where the primary-law text does not prohibit it — do NOT silently enable this for AR without compliance/legal sign-off given the RG risk is unchanged even where technically permitted, and given the sourcing caveat above (MEDIUM/LOW confidence it applies to sports wagering).
- **No hardcoded fixed withdrawal SLA for AR:** unlike CO (24h) or MD (7-day), verify the withdrawal engine does not impose an incorrect state-specific SLA constant for AR — the governing clock is the operator's own filed wagering-account agreement, gated only by pending-dispute/investigation holds.
- **Reserve floor:** ensure the reserve-calculation service treats AR's $25,000-or-liability-sum floor as a per-state configurable value, not a copy of a higher-floor state's constant (and flag if AR's floor is lower than the platform's global minimum default).
- **Self-exclusion:** implement/verify a hard 30-day minimum lockout before an AR self-excluded account can be reactivated (not just a standard reinstatement flow), account closure (not just a wager block) on enrollment, and suppression of marketing communications to the excluded list; confirm registry export capability exists for ARC.
- **Business-entity account type:** if the platform supports non-individual wagering accounts, confirm AR enforces bank-transfer-only / no-cash for deposits and withdrawals on that account type, distinct from individual patron rules.
- **Geolocation:** confirm the standard third-party geolocation/geofencing vendor check (e.g., GeoComply) still runs for AR mobile wagers even though the primary-rule-text bar appears lower (self-affirmation-compliant) — do not disable or downgrade geo-verification for AR based on the letter of this one rule without compliance sign-off.
- **$10,000 KYC trigger:** verify enhanced-KYC collection (SSN/passport + government ID) fires correctly at the $10,000 single-wager threshold for AR, separate from any global platform KYC tiering.

## Sources & confidence

WebSearch/WebFetch were available and used for this file; however, several findings rely on secondary sources or on primary-rule text sourced from AR's off-track pari-mutuel account-wagering rule section (Casino Gaming Rule 24) rather than a confirmed sports-wagering-specific section, because the sports-wagering rule sections could not be independently isolated in full from the sources reached. Treat MEDIUM/LOW-tagged items above as needing direct confirmation against the current Arkansas Racing Commission Casino Gaming Rules PDF (which could not be parsed as text from the version fetched) or the Code of Arkansas Rules site before relying on them for a compliance decision.

- [Code of Arkansas Rules — Racing Commission, Title 23 Ch. 238 Casino Gaming Rules, Part 358](https://codeofarrules.arkansas.gov/Rules/Rule?levelType=part&titleID=23&chapterID=238&subChapterID=295&partID=1258&subPartID=&sectionID=)
- [23 CAR § 358-514 — Self-exclusion](https://codeofarrules.arkansas.gov/Rules/Rule?levelType=section&titleID=23&chapterID=238&subChapterID=295&partID=1258&subPartID=7968&sectionID=52253)
- [23 CAR § 358-418 — Collection of gaming credit](https://codeofarrules.arkansas.gov/Rules/Rule?levelType=section&titleID=23&chapterID=238&subChapterID=295&partID=1258&subPartID=7967&sectionID=52227)
- [Ark. Code Ann. Title 23, Subtitle 4, Ch. 117 — Casino Gaming Justia](https://law.justia.com/codes/arkansas/title-23/subtitle-4/chapter-117/)
- [006.06.21 Ark. Code R. 011 — Casino Gaming Rule 24 Cornell LII](https://www.law.cornell.edu/regulations/arkansas/006-06-21-Ark-Code-R-011)
- [006.06.21 Ark. Code R. 013 — Casino Gaming Rule 20 Cornell LII](https://www.law.cornell.edu/regulations/arkansas/006-06-21-Ark-Code-R-013)
- [Arkansas Racing Commission Casino Gaming Rules PDF DFA](https://www.dfa.arkansas.gov/wp-content/uploads/2025ArkansasCasinoGamingRules.pdf) — fetched but rendered as non-extractable/garbled text; not usable as a direct quote source this pass.
- [sportshandle.com — Arkansas mobile sportsbook operators launch coverage](https://sportshandle.com/mobile-sportsbook-operators-arkansas-mixed-reviews/)
- [Arkansas Department of Finance and Administration — Racing Commission](https://www.dfa.arkansas.gov/office/racing-commission/)
- Confidence: HIGH on self-exclusion registry/30-day rule, $10,000 KYC trigger, and business-entity bank-transfer-only rule. MEDIUM on the $25,000 reserve floor and the "no fixed withdrawal SLA / contract-defined" finding (sourced from the account-wagering rule, not confirmed identical in the sports-wagering-specific section). LOW/MEDIUM — and flagged for verification — on: licensee-extended-credit deposits applying to sports wagering specifically, the geolocation self-affirmation standard, minimum age, deposit/cooling-off/reverse-withdrawal RG provisions, state-specific AML overlay, and records-retention period. Verify all MEDIUM/LOW items against the current full Casino Gaming Rules text (not just the sections indexed by the search/fetch tools used) before treating this file as compliance-final.
