# North Dakota — Tribal-State Class III Gaming Compacts (ND Attorney General Gaming Division / Tribal Gaming Commissions / NIGC)

**Code:** ND · **Products:** sportsbook — **tribal retail-only; NO statewide/commercial or mobile sports-betting market exists** · **Key authority:** N.D. Const. art. XI, § 25 (gambling prohibition, charitable-gaming carve-out only); N.D. Cent. Code ch. 12.1-28 (gambling offenses, Class A misdemeanor); 2022 Tribal-State Class III Gaming Compacts between the Governor and ND's 5 federally recognized tribes, approved by U.S. DOI 12/19/2022 (term through 2032); Indian Gaming Regulatory Act, 25 U.S.C. § 2710

## Payments-relevant requirements

North Dakota has **no state-licensed commercial or mobile sportsbook of any kind**. Sports wagering — including the compacts' own "mobile gaming" clause — is authorized only for in-person and account-based play physically on one of the five tribes' reservations, under Class III compacts with the state. A 2025 attempt to put a statewide-mobile constitutional amendment before voters (HCR 3002) was rejected 70-24 in the House; because the Legislature sits only in odd years, the next possible attempt is the 2027 session, with a public referendum no earlier than 2028 (MEDIUM-HIGH — legislative outcomes are not guaranteed). The eight subsections below are kept short because most standard payments-relevant regulatory apparatus (licensing tiers, statewide reserve rules, statewide payout SLAs) simply does not exist here yet.

### Licensing & change management

- No state commercial/mobile sportsbook licensing regime exists; N.D. Const. art. XI, §25 and N.D. Cent. Code ch. 12.1-28 prohibit non-charitable gambling absent an express statutory or compact exception (HIGH).
- Class III sports wagering (incl. the compacts' "mobile gaming" clause, confined to reservation boundaries) is authorized only via the 2022 Tribal-State Class III Gaming Compacts between the Governor and ND's 5 tribal nations, approved by the U.S. Department of the Interior 12/19/2022, 10-year term through 2032 with automatic 10-year renewal on notice (HIGH — Federal Register 2022-27470).
- Each tribe's own Tribal Gaming Commission licenses and regulates its Class III operation day-to-day; the ND Attorney General's Gaming Division retains a state compliance-inspection right (one annual inspection at tribal expense, plus additional state-funded inspections) rather than the pre-launch independent-lab platform certification seen in commercial-market states (MEDIUM — no lab-certification requirement located for tribal sports wagering).
- Changes to compact terms (e.g., new game types) go through Legislative Management (17-legislator interim committee, 21-day review) plus U.S. DOI approval — not a unilateral tribal or state change (HIGH).

### Deposits & permitted payment methods

- No statewide/commercial deposit-rail rules exist because there is no state-licensed online or mobile sportsbook to receive deposits.
- The 2022 compact amendments specifically newly authorize tribes to accept credit and debit cards for account wagering (HIGH, per the Governor's office summary of the amendments) — but exact card-acceptance mechanics live in each tribe's own compact text and Tribal Gaming Commission rules, not in a public state regulation (MEDIUM on implementation detail; not indexed publicly per-tribe).
- Separately, ND's state-licensed charitable gaming rules (bingo/raffles, under AG Gaming Division) explicitly forbid credit cards as payment for wagers/raffle tickets and forbid "online gaming" by licensed charitable organizations (HIGH). This is **not** the rule that governs tribal sports wagering, but it is the state-law default everywhere outside the tribal-compact carve-out — worth not confusing with a sportsbook-specific restriction.

### Withdrawals & payout timelines

- No statewide payout-SLA statute or rule exists for sports wagering. Retail/tribal-casino withdrawal terms are set by each tribe's own internal controls under its Tribal Gaming Commission and are not published in state code (LOW — verify directly with the specific tribe's gaming commission if any partnership is contemplated).

### Player funds segregation / reserve

- No statewide reserve/segregation statute for sports wagering exists (there is no state-licensed commercial operator to regulate). Any reserve requirement would be internal to the specific tribal compact/Tribal Gaming Commission and was not located in public sources (LOW — mark "verify" if a tribal partnership is ever pursued).

### Responsible gambling

- 2022 compact amendments require the tribes to jointly contribute $125,000/year toward problem-gambling services (HIGH — Governor's office summary).
- The compact-governed gambling age was lowered from 21 to **19 (18 with military ID)** for tribal casino/sports wagering (HIGH) — notably below the 21+ floor most other jurisdiction configs in this codebase assume.
- No statewide self-exclusion registry or statutory deposit/time-limit mandate for sports wagering was located; ND has no public commercial-market-style responsible-gaming program of the kind seen in NJ/PA/MI (LOW — confirm with any partnering tribe's own program).

### KYC / age / geolocation

- Age gate for tribal gaming/sports wagering under the 2013/2022 compacts: **19+ generally, 18+ with military ID** (HIGH) — distinct from the 21+ assumed elsewhere in most other jurisdiction configs.
- Wagering, including the compacts' "mobile gaming" clause, must occur "within the physical boundaries of the reservation[s]" — i.e., geofenced to tribal trust land, not to the state of North Dakota generally (HIGH — Governor's office summary; the compacts leave open a future off-reservation option "if state and federal law eventually permits it," which as of 2026 it does not).
- No statewide sports-wagering KYC/identity-verification statute exists outside the tribal compacts and each tribe's own program (LOW/MEDIUM).

### AML overlays

- No ND-specific AML statute for sports wagering beyond the federal BSA/FinCEN obligations that already apply to tribal gaming operations as financial institutions under FinCEN's Indian-gaming guidance; no state-level CTR/SAR-equivalent overlay was located (MEDIUM/LOW).

### Records, reporting & data

- ND AG's Gaming Division holds a state compliance-inspection right over tribal casinos (annual, tribe-funded, plus additional state-funded inspections); no public statewide sports-wagering transaction-reporting statute exists absent a compact provision, and the full compact text is not uniformly indexed publicly across all 5 tribes (LOW — pull the specific tribe's compact/Tribal Gaming Commission rules for specifics if needed).

## Code review focus

- **Geo/jurisdiction gate is the whole story for ND.** Any statewide or mobile deposit/wagering flow must default to "NOT authorized" for ND — there is no commercial or mobile legal basis, only in-person/account wagering physically on one of the 5 tribes' reservations under compact. If ND appears "open" for online/mobile real-money deposits in any jurisdiction-enablement config, that is a compliance defect, not a coverage gap.
- Payments code reachable from an ND-resident IP/device should route through the same "prohibited/illegal market" branch used for other non-authorized states — confirm the illegal-market and UIGEA/Wire-Act exposure controls (see the FED-US baseline) apply to ND **by default**, not only via an explicit deny-list entry. ND is easy to silently omit if the mental model is "the covered states are enumerated, everything else defaults open."
- If ND is ever scoped for a tribal-partnership integration, note the compact's 19-and-18-with-military-ID age floor is materially different from the 21+ assumption baked into most other jurisdiction configs in this codebase — a shared age-gate constant would silently misfire for ND.
- Do not encode "ND = credit cards blocked" anywhere in card/BIN routing based on the charitable-gaming statute — that prohibition governs state-licensed bingo/raffles, not tribal sports wagering (which the 2022 compact amendments affirmatively allow to accept credit/debit for account wagering). Conflating the two produces a rule this codebase does not actually need to enforce, and could misfire if a tribal integration is ever built.
- Track the legislative calendar rather than treating "tribal-only" as permanent: ND's Legislature sits only in odd years; HCR 3002 (statewide-mobile constitutional referendum) was rejected 70-24 on 2025-01-22, so the earliest a statewide/mobile product could exist is a 2027 session + 2028 voter referendum. Re-check this file each even-year planning cycle.

## Sources & confidence

- [N.D. Cent. Code ch. 12.1-28, Gambling state legislature](https://ndlegis.gov/cencode/t12-1c28.pdf)
- [Federal Register: Indian Gaming; Approval of Tribal-State Class III Gaming Compacts in the State of North Dakota 2022-27470](https://www.federalregister.gov/documents/2022/12/19/2022-27470/indian-gaming-approval-of-tribal-state-class-iii-gaming-compacts-in-the-state-of-north-dakota)
- [Office of the Governor of North Dakota — Final drafts of tribal-state gaming compacts submitted for review; public comment period closes](https://www.governor.nd.gov/news/final-drafts-tribal-state-gaming-compacts-submitted-review-public-comment-period-closes)
- [North Dakota Attorney General — Gaming Gaming Division](https://attorneygeneral.nd.gov/licensing-and-gaming/gaming/)
- [North Dakota Attorney General — Charitable Gaming](https://attorneygeneral.nd.gov/licensing-and-charitable-gaming/)
- [Three Affiliated Tribes of Fort Berthold — Tribal-State Gaming Compact BIA/DOI, 2022, 508-compliant PDF](https://www.bia.gov/sites/default/files/dup/assets/as-ia/oig/pdf/508_compliant_2022.12.19_three_affiliated_tribes_of_the_fort_berthold_reservation_tribal_state_gaming_compact.pdf)
- [Spirit Lake Tribe — Tribal-State Gaming Compact BIA/DOI, 2022, 508-compliant PDF](https://www.bia.gov/sites/default/files/dup/assets/as-ia/oig/pdf/508_compliant_2022.12.19_spirit_lake_tribe_tribal_state_gaming_compact.pdf)
- [Bismarck Tribune — North Dakota Lawmakers vote against sports betting HCR 3002, 2025-01-22](https://bismarcktribune.com/news/state-regional/government-politics/north-dakota-lawmakers-vote-against-sports-betting-hcr33002/article_2c6459a4-d90b-11ef-8260-a3a918eb1281.html)
- [LegiScan — ND HCR3002, 2025-2026, 69th Legislative Assembly](https://legiscan.com/ND/bill/HCR3002/2025)
- [Legal Sports Report — North Dakota Sports Betting: Legal ND Sportsbooks & Legislation Updates](https://www.legalsportsreport.com/sports-betting/states/north-dakota/)
- Confidence: HIGH on the core legal-status finding (tribal-retail-only, no statewide/commercial/mobile market, compact term through 2032, HCR 3002 rejected 2025-01-22, 19/18-with-military-ID compact age floor, credit/debit cards newly allowed for tribal account wagering, $125k/yr addiction-services requirement). MEDIUM/LOW on anything below the compact-amendment-summary level of detail — reserve requirements, payout SLAs, and per-tribe KYC/AML mechanics live inside each tribe's own compact text and Tribal Gaming Commission rules, which are not uniformly published; **verify directly with the specific tribe if a partnership is ever scoped.** No WebFetch 403s encountered during this research pass.
