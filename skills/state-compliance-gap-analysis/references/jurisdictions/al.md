# Alabama — No RMG Regulator; Alabama Attorney General administers DFS registration (AL-AG)

**Code:** AL · **Products:** none licensed (online/retail sports betting, casino, and lottery are constitutionally prohibited statewide); Daily Fantasy Sports (DFS) is the one codified RMG-adjacent product (legal since 2019); sweepstakes-casino operates via the federal sweepstakes/promotional-law channel · **Key authority:** Ala. Const. Art. IV, §65 (lottery/gift-enterprise ban, judicially extended to casino- and sports-wagering-style gaming); Ala. Code Title 13A, Ch. 12, Art. 2 (§13A-12-20 et seq., criminal gambling offenses); Ala. Code Title 8, Ch. 19F (Fantasy Contests Act — **note:** the codified chapter is **19F**, not "19G" — verified against Justia/FindLaw/AL AG primary sources)

## Payments-relevant requirements

### Licensing & change management

- No state licensing regime exists for sportsbook/casino payments — Alabama Constitution Art. IV §65 bars the Legislature from authorizing lotteries or gift enterprises; courts and lawmakers have long read that language to also bar casino-style gaming and sports wagering, and any change requires a legislative package **plus** a statewide constitutional-amendment vote (HIGH — Justia Section 65 text and commentary).
- A comprehensive 2024 package (lottery + casino at up to 7 sites + sports betting) passed the AL House but died in the Senate after the Senate stripped sports betting and downgraded casino gaming to a single Poarch Band of Creek Indians compact site; the compromise fell one vote short in the Senate (HIGH — Alabama Reflector reporting). 2025 and 2026 successor efforts have not advanced as of this writing (MEDIUM — trade-press summaries, verify current session status before relying on this).
- DFS operators must register annually with the Alabama Attorney General under Ala. Code §8-19F-3: $1,000 registration fee, or $85,000 annual renewal for operators with AL revenue exceeding $10 million; registration period runs to December 31 each year (HIGH — AL AG licensing page + Justia).
- No independent-testing-lab / change-management regime exists for DFS platforms (there is no RMG regulator to submit builds to) — N/A.

### Deposits & permitted payment methods

- N/A — no legal RMG online or retail sports-betting/casino channel exists to regulate deposit methods for.
- DFS (§8-19F-4): paid contests may only be offered by a registered operator to verified 19+ players; no AL-specific statutory restriction on deposit *method* was located in Chapter 19F (confidence LOW — likely governed by the operator's own card-network/payment-processor terms rather than AL statute; verify with legal).
- Sweepstakes-casino (dual "Gold Coin" / "Sweeps Coin" model) operates under federal sweepstakes/promotional law, not AL gaming statute, and AL has not enacted a law banning the model as of early 2026 — but AL is currently the leading U.S. jurisdiction for consumer class-action suits against sweepstakes operators (MEDIUM — litigation-trend risk, not itself a payments statute).

### Withdrawals & payout timelines

- N/A — no statewide RMG withdrawal SLA exists (no licensed product to impose one on).
- No AL-specific DFS withdrawal-timeline requirement located in Chapter 19F (LOW — verify).

### Player funds segregation / reserve

- N/A for sportsbook/casino — no legal product.
- DFS (§8-19F-4): operator must either segregate player funds from operational funds, **or** maintain a reserve — cash, cash equivalents, irrevocable letter of credit, bond, payment-processor reserves/receivables, or a combination — that exceeds total player account balances; reserve funds may not be used for operational activities (HIGH — mirrors the CO/MD reserve pattern). Operator must contract for an annual independent audit (AICPA standards) and submit results to the AG within 270 days of fiscal year end (HIGH).

### Responsible gambling

- N/A — no statewide deposit/spend/time-limit, cooling-off, or self-exclusion regime exists for sportsbook/casino (none is licensed).
- Chapter 19F imposes standard DFS consumer protections (age verification, a bar on operator employees playing in public cash contests, a ban on contests based on high-school/youth athletic events) but no deposit-limit or self-exclusion mandate was identified (MEDIUM — verify against full statutory text).

### KYC / age / geolocation

- DFS: players must be verified as **19 or older** (Ala. Code §8-19F-4) — notably below the 21+ floor typical of licensed sportsbook states; do not reuse a 21+ default for an AL DFS product (HIGH).
- No statutory geolocation-fencing requirement for DFS was located; AL has no RMG channel to geofence against, so this is effectively N/A (LOW).

### AML overlays

- N/A — no state gaming AML program exists. DFS/sweepstakes activity is subject only to generally-applicable federal BSA/AML obligations on the payment processor, with no AL-specific overlay identified (MEDIUM).

### Records, reporting & data

- DFS: annual independent AICPA-standard audit submitted to the AG within 270 days of fiscal year end (§8-19F-3/-4) (HIGH). No other AL-specific payments-records/reporting regime was identified.

## Code review focus

- **Hard geo/jurisdiction DEFAULT-DENY for AL**: sportsbook and online-casino deposit/wager/payout endpoints must reject any AL-located account by default. The payments platform's default-on per-state method-rail enablement is a direct illegal-market / UIGEA / Wire Act exposure here, because Art. IV §65 (as judicially extended) plus Title 13A-12 make the underlying wagering activity itself illegal in AL — not merely unlicensed/unregulated.
- **DFS carve-out** (if the operator offers or plans to offer a paid DFS product in AL): payments layer must gate on (a) confirmed AG registration on file before enabling AL, (b) a **19+** age gate distinct from the 21+ gate used in licensed-sportsbook states, (c) a player-fund segregation flag or a reserve calculation feeding an exportable liability snapshot for the §8-19F-4 reserve test, (d) an annual AICPA-standard-audit data export.
- **Sweepstakes-casino carve-out** (if offered): model the dual-currency ("Sweeps Coins" redeemable / "Gold Coins" non-redeemable, no-purchase-necessary entry) as a distinct ledger/fund-type from any AL cash-wagering product, since collapsing the distinction risks pulling the whole product into the Title 13A-12 gambling definition; flag AL's outsized sweepstakes class-action litigation exposure to legal/compliance before enabling or expanding this product in AL.
- Do not silently inherit CO/MD-style 21+ age configs or reserve/withdrawal-SLA defaults for AL — the only permitted product (DFS) has its own narrower rule set (19+, segregation-or-reserve, no codified withdrawal SLA), and everything else must default-deny.

## Sources & confidence

- [Alabama Constitution, Section 65 Justia](https://law.justia.com/constitution/alabama/CA-245600.html)
- [Gambling bills stalled in Senate as Alabama Legislature nears adjournment — Alabama Reflector 2024-05-03](https://alabamareflector.com/2024/05/03/gambling-bills-stalled-in-senate-as-alabama-legislature-nears-adjournment/)
- [Alabama House and Senate clash over budgets, gaming as 2024 session concludes — Alabama Reflector](https://alabamareflector.com/2024/05/10/alabama-house-and-senate-clash-over-budgets-gaming-as-2024-session-concludes/)
- [Gambling bill prospects uncertain as Alabama legislators return for 2025 session — Alabama Reflector](https://alabamareflector.com/2025/01/31/gambling-bill-prospects-uncertain-as-alabama-legislators-return-for-2025-session/)
- [Alabama Code Title 8, Chapter 19F — Fantasy Contests Act Justia](https://law.justia.com/codes/alabama/title-8/chapter-19f/)
- [Alabama Code §8-19F-4 — Fantasy Contest Procedure Requirements LawServer](https://www.lawserver.com/law/state/alabama/al-code/alabama_code_8-19f-4)
- [Fantasy Sports Operators — Alabama Attorney General's Office](https://www.alabamaag.gov/licensing-registration/fantasy-sports-operators/)
- [Alabama Code Title 13A, Chapter 12 — Offenses Against Public Health and Morals Justia](https://law.justia.com/codes/alabama/title-13a/chapter-12/article-2/division-1/section-13a-12-20/)
- [Alabama Sports Betting: Legal Status, Updates, and More — Bleacher Nation 2026-06-01](https://www.bleachernation.com/betting/2026/06/01/alabama/)
- Confidence: HIGH on the constitutional prohibition, the 2024 legislative failure, DFS registration fees/reserve/audit requirements (§8-19F-3/-4), and the 19+ DFS age floor. MEDIUM on 2025/2026 legislative-session status and sweepstakes-casino legal footing — re-verify current session activity and any new AL AG guidance before relying on this for a live compliance decision. LOW on whether any AL-specific DFS payment-method restriction exists beyond the fund-segregation/reserve rule — verify with legal.
