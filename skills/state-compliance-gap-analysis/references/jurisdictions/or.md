# Oregon — Oregon State Lottery / Oregon Lottery Commission

**Code:** OR · **Products:** sportsbook (mobile + retail, operated as a state lottery game; DraftKings is the exclusive vendor/"Official Provider" since Jan 2022) · **Key authority:** Or. Const. Art. XV §4; ORS Chapter 461 (Oregon State Lottery); ORS 167.109 (Internet gambling — Lottery exempt); OAR Chapter 177, Division 93 (DraftKings Sportsbook game rules) and Division 46 (general digital player-account rules)

**Framework note (structural, not a gap):** Unlike commercial-license states, Oregon has no privately-licensed sportsbook operator and no commercial license regime for online sports betting. Sports betting is a **state lottery game** the Lottery Commission authorizes and DraftKings runs under an exclusive vendor agreement; the Lottery itself is statutorily exempt from Oregon's general gambling-crime statutes (ORS 167.108–167.167) per ORS 167.109. Tribal casinos (9 federally recognized tribes, IGRA + tribal-state compacts) operate retail casino gaming separately and are excluded from Lottery mobile-betting geofencing. There is consequently no commercial "license," no bond/reserve statute of the CO/MD type, and no state-specific AML/MSB statute located for the sportsbook product — confidence LOW/MEDIUM on those gaps; treat "no code" as "verify with compliance," not as evidence of compliance. (HIGH on the structural framework itself — corroborated by ORS 167.109 and ORS 461 authority chain.)

## Payments-relevant requirements

### Licensing & change management

- No commercial operator license; DraftKings operates under an exclusive vendor/game-provider agreement with the Lottery Commission (contract terms not public — confidence LOW on any change-management/re-certification cadence).
- Oregon Lottery holds WLA (World Lottery Association) Level Four Responsible Gambling certification (2026) — RG governance/culture audit, not a technical/security certification of the betting platform (confidence HIGH on scope, per Lottery's own press release).
- Game-specific rules for the sportsbook product live in OAR 177-093 (Div. 93, "DraftKings Sportsbook"); general digital player-account/funding rules live in OAR 177-046 (Div. 46) and apply unless Div. 93 conflicts, in which case Div. 93 controls (pattern per Div. 91 Scoreboard rule; confidence MEDIUM this same supersession clause exists verbatim in Div. 93 — verify text of OAR 177-093-0000).

### Deposits & permitted payment methods

- OAR 177-046-0027 (Funding Account): players must link a bank "funding account" to their player account; Lottery charges no deposit/withdrawal fees but disclaims responsibility for payment-processor/financial-institution fees; no credit is extended — purchases are capped at account balance.
- DraftKings' OR banking rails (per Lottery/DraftKings public help content) include Play+, online bank transfer/ACH, and debit/credit card. **Whether credit cards are permitted for OR sportsbook deposits is UNCONFIRMED — sources conflict:** one third-party aggregator (bettingusa/legalsportsbetting-style summary) claims Oregon has banned credit-card funding; a general Lottery retailer rule (OAR 177-040-0055) states retailers "shall not extend credit" but that a **player's use of a credit or debit card is not itself extending credit** and is permitted for ticket/share purchases. No primary-source Div. 93/Div. 46 text was found that specifically bans credit cards for the sportsbook. **Mark LOW confidence — verify current DraftKings-OR banking page and any 2025-2026 rule change before relying on either position in code.**
- No cash-at-retail-kiosk deposit path identified for the DraftKings mobile product (tribal casinos are a separate cash-based retail channel outside this scope).

### Withdrawals & payout timelines

- No explicit numeric withdrawal-SLA (e.g., "within N days") was located in OAR 177-046 or Div. 93 text retrieved. OAR 177-046-0110 (Payment of Prizes) sets: prizes paid "within a reasonable time after validated" (no fixed day count); digital-game prizes credited to the funding account net of required withholdings; prizes ≥$50,000 require next-business-day, in-person claim (limited exceptions) — this large-prize in-person rule likely targets draw-game claims more than sportsbook payouts, but the statute doesn't carve sportsbook out — confidence LOW/MEDIUM on applicability to sportsbook wins.
- Withdrawals from the funding account are available "at any time up to the funds balance," subject to the player's bank/payment-processor limitations (OAR 177-046-0027(6)); Lottery is not liable for delays caused by incorrect player-provided payment info.
- **No fixed payout-SLA number to cite — mark LOW, "verify" against current DraftKings-OR terms of service**, unlike MD's 7-day or CO's 24-hour statutory clocks.

### Player funds segregation / reserve

- **No segregation/reserve statute or rule located for the sportsbook product.** ORS 461.543 (Sports Lottery Account) governs post-hoc revenue *distribution* to university athletics/scholarships, not player-fund custody. Because this is a state lottery game (not a privately-underwritten book), the CO/MD-style "maintain a reserve ≥ outstanding liability" framework does not appear to apply in the same form — confidence LOW/MEDIUM; this is a genuine open question for compliance/legal, not a confirmed "no requirement."

### Responsible gambling

- OAR 177-046-0155 (Responsible Gaming): at account creation, players "must establish a personal deposit limit"; players may separately set bet/time limits and select temporary or permanent self-exclusion; once limits are active, "neither the player nor the Lottery can override them" — a hard, non-overridable control (confidence HIGH on rule text, MEDIUM on exact numeric parameters).
- DraftKings-OR product-level RG tools (per Lottery/DraftKings FAQ, confidence MEDIUM — not primary rule text with numbers): daily/weekly/monthly deposit, wager, and time limits; "Cool Off" up to 1 month; self-exclusion up to 5 years or permanent, during which deposits and bets are blocked.
- A separately reported figure (confidence LOW, differing source) describes Lottery self-exclusion as "30 days or longer," extendable indefinitely or permanent — reconcile against current OAR text/DraftKings terms before building exact duration enums.
- No statewide, cross-operator self-exclusion list exists in Oregon (unlike NJ/PA-style multi-operator lists) — self-exclusion is Lottery-account-specific, consistent with the single-operator structure.
- Support referral: Oregon Problem Gambling Resource (OPGR.org / 1-877-MYLIMIT) per Lottery responsible-gaming content.

### KYC / age / geolocation

- OAR 177-093-0015 (Eligibility): player must be 21+, hold a valid personal digital player account, and not be an excluded person (Lottery/DraftKings employees, immediate family, or otherwise legally prohibited).
- OAR 177-046-0022 (Player Account): one account per individual, opened only in the player's own legal name; Lottery has up to 30 days to verify identity via third-party service and may require government photo ID / proof of address; player must consent to geolocation technology; multiple accounts and inactivity-based closure (12+ months) addressed.
- Geolocation must confirm the bettor is physically within Oregon **and not on tribal land** at the time of the bet (GeoComply cited in Lottery consumer materials) — the tribal-land carve-out is the Oregon-specific twist other states' geofencing doesn't need (confidence MEDIUM-HIGH; sourced from Lottery-facing consumer content, not primary rule text with that exact tribal-exclusion phrasing — verify against OAR 177-093-0020).

### AML overlays

- No Oregon-specific AML/BSA overlay statute or rule was located for the sportsbook product. As a state-agency-run lottery game, exposure to typical commercial-operator BSA/MSB obligations may differ from CO/MD's licensee model — confidence LOW; do not assume "no AML overlay" without compliance/legal sign-off. Large-prize (≥$600) IRS Form W-9G / SSN collection under OAR 177-046-0110 exists for tax-withholding purposes but is not itself an AML-labeled control.

### Records, reporting & data

- OAR 177-046-0110: SSN/ITIN capture on W-9G above the $600 federal reporting threshold; mandatory offset for outstanding debts (tax, child support, other state obligations) before payout.
- No sportsbook-specific record-retention period (e.g., "retain X years") was located in the Div. 93/Div. 46 text retrieved — confidence LOW, "verify" against full OAR 177-093 text and any Lottery-DraftKings vendor agreement.

## Code review focus

- Do not hardcode a CO-style 24-hour or MD-style 7-day withdrawal SLA for OR — no equivalent numeric statute was found; treat OR payout timing as "reasonable time, net of withholding" and flag any code that assumes a fixed OR withdrawal deadline as needing compliance verification.
- Deposit-method allow-list for OR: verify current DraftKings terms before asserting credit-card status one way or the other in a per-state config — sources conflict (see Deposits section). Do not silently mirror a "credit cards banned" rule copied from another state's config into OR without confirmation.
- Non-overridable limit enforcement: once a player sets a deposit/bet/time limit or self-exclusion under OAR 177-046-0155, the system must reject any override attempt by either the player or an internal ops/support action — this "neither party can override" language is stronger than a typical soft limit and should be a hard gate, not a soft warning.
- Self-exclusion block scope: confirm the code blocks both new deposits and new wagers during exclusion (per DraftKings FAQ), consistent with other states' asymmetric account-state pattern (deposits/bets blocked; balance withdrawal typically still allowed — verify OR explicitly permits withdrawal during exclusion, since this wasn't directly confirmed in primary text).
- Geolocation gate: confirm the geofence excludes tribal lands specifically (not just "outside Oregon"), since Oregon's tribal-compact carve-out is a state-specific wrinkle other jurisdictions in this matrix don't need.
- W-9G/SSN capture and payout offset (tax, child support, other state debts) must trigger before crediting any payout ≥ the applicable reporting threshold.
- Single-account-per-person enforcement and 12-month-inactivity closure logic (OAR 177-046-0022) if OR account lifecycle is modeled in this codebase.
- Flag any place the code assumes a segregation/reserve calculation (CO/MD-style) is required for OR — no such statute was found; confirm with legal whether the Lottery's own reserves/insurance (not player-funded) cover this instead.

## Sources & confidence

- Web search/fetch tools WERE available and used for this file (WebSearch + WebFetch, Aug 2026). Several claims rely on secondary/aggregator sources or Lottery-facing FAQ content rather than verified primary rule text with exact figures — these are explicitly flagged LOW/MEDIUM below and in-line above. **No primary full text of OAR Division 93 (177-093) itself was retrievable via the tools used** (index pages resolved, but full section text for 177-093-0015/0020/0040/0045 did not return complete text); Cornell LII gave a partial eligibility summary. Treat all Division 93 citations as MEDIUM pending direct verification against the OAR/Secretary of State rule text.
- [OAR Chapter 177, Division 93 — DraftKings Sportsbook Justia index](https://regulations.justia.com/states/oregon/chapter-177/division-93/) · [Or. Admin. Code §177-093-0015 Eligibility Cornell LII](https://www.law.cornell.edu/regulations/oregon/Or-Admin-Code-SS-177-093-0015) · [Or. Admin. Code §177-093-0000 Purpose Cornell LII](https://www.law.cornell.edu/regulations/oregon/Or-Admin-Code-SS-177-093-0000)
- [OAR 177-046-0027 Funding Account oregon.public.law](https://oregon.public.law/rules/oar_177-046-0027) · [OAR 177-046-0022 Player Account oregon.public.law](https://oregon.public.law/rules/oar_177-046-0022) · [OAR 177-046-0110 Payment of Prizes oregon.public.law](https://oregon.public.law/rules/oar_177-046-0110) · [OAR 177-046-0155 Responsible Gaming oregon.public.law](https://oregon.public.law/rules/oar_177-046-0155) · [OAR 177-040-0055 Advertising/Inducements — credit-card clarification oregon.public.law](https://oregon.public.law/rules/oar_177-040-0055)
- [ORS 167.109 Internet gambling — Lottery exemption oregon.public.law](https://oregon.public.law/statutes/ors_167.109) · [ORS 461.543 Sports Lottery Account oregon.public.law](https://oregon.public.law/statutes/ors_461.543) · [ORS 461.820 Promotion of responsible gambling oregon.public.law](https://oregon.public.law/statutes/ors_461.820) · [Oregon Revised Statutes Ch. 461 hub](https://www.oregonlegislature.gov/bills_laws/ors/ors461.html)
- [Oregon Lottery — WLA Responsible Gambling Certification 2026 press release](https://www.oregonlottery.org/press-releases/wla-certification-2026/) · [Oregon Lottery — DraftKings Transition Q&A](https://www.oregonlottery.org/sports/draftkings-qa/)
- Confidence: HIGH — state-lottery-not-commercial-license framework, ORS 167.109 exemption, 21+ age, one-account-per-person, non-overridable RG limits (OAR 177-046-0155), $600 W-9G threshold. MEDIUM — Div. 93/Div. 46 supersession relationship, tribal-land geofence exclusion, self-exclusion duration parameters, WLA certification scope. LOW — credit-card deposit permissibility (conflicting sources, unresolved), any numeric withdrawal-payout SLA, existence/absence of a reserve or segregation requirement, existence/absence of an OR-specific AML overlay, records-retention period. **All LOW items should be verified directly with Oregon Lottery counsel/compliance and against the current DraftKings-OR Terms of Use before being treated as ground truth in the code-review matrix.**
