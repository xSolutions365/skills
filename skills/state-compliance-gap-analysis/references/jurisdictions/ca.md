# California — no state gaming-control regulator for RMG online; oversight split between CA Dept. of Justice / Bureau of Gambling Control (card rooms), California Gambling Control Commission (card rooms), and tribal gaming compacts under IGRA

**Code:** CA · **Products:** none — no legal online sports betting or online casino of any kind; retail-only tribal Class III casinos (slots, banking/percentage card games) and state-licensed card rooms (non-banked card games) exist but are out of scope for an online payments product; DFS is AG-opinioned illegal (untested); sweepstakes/social casino dual-currency platforms are a criminal misdemeanor as of 1/1/2026 · **Key authority:** Cal. Const. art. IV, §19 (gambling framework + tribal compacts); Penal Code §337a (bookmaking/pool-selling); Business & Professions Code §19800 et seq. (Gambling Control Act — card rooms); Business & Professions Code §17539.1 + Penal Code §337o (AB 831, sweepstakes ban, eff. 1/1/2026); 2022 Propositions 26 and 27 (both FAILED at the Nov. 8, 2022 general election)

## Payments-relevant requirements

**Threshold finding (verify before using any subsection below):** California has **no legal online sports betting and no legal online casino**, tribal or commercial. Proposition 26 (in-person tribal/racetrack sports betting) was rejected by ~68% of voters and Proposition 27 (online/mobile sports betting) was rejected by ~83% of voters at the November 8, 2022 general election — both FAILED (HIGH — [Wikipedia Prop 27 summary](https://en.wikipedia.org/wiki/2022_California_Proposition_27), corroborated by [NPR](https://www.npr.org/2022/11/09/1133986282/california-gambling-prop-26-27-midterm-results)). Cal. Const. art. IV, §19 permits only tribal-compact Class III gaming (slot machines, lottery games, banking/percentage card games) on Indian lands, plus non-bank card rooms and pari-mutuel horse racing wagering under separate statutory schemes — none of which is online sports betting or online casino (HIGH — [Cal. Const. art. IV, §19, Justia](https://law.justia.com/constitution/california/article-iv/section-19/)). Momentum for a renewed 2026/2028 ballot measure exists but nothing has passed as of Aug. 2026 (MEDIUM — trade press, [sportsepreneur.com](https://sportsepreneur.com/california-sports-betting-standoff/)).

- **DFS (daily fantasy sports):** No statute either authorizes or bans DFS. In July 2025 CA Attorney General Rob Bonta issued a formal legal opinion that paid DFS contests (draft-style and pick'em) can constitute illegal sports wagering under existing law; the opinion is not self-enforcing and no direct enforcement action against DFS operators has been reported as of Aug. 2026, but it materially raises legal risk for any DFS product touching CA (HIGH on the opinion's existence and content — [NBC San Diego](https://www.nbcsandiego.com/news/local/california-attorney-general-says-daily-fantasy-sports-are-illegal-in-the-state/3863225/); MEDIUM on real-world enforcement posture — trade press only).
- **Sweepstakes / social casino (dual-currency):** AB 831 (Ch. 623, Statutes of 2025, signed 10/11/2025, effective 1/1/2026) makes it unlawful to operate, conduct, or offer an online sweepstakes game that mimics casino or sports-betting products in California, and separately makes it unlawful for **any financial institution, payment processor, geolocation provider, gaming content supplier, platform provider, or media affiliate to "knowingly and willfully" support** such a platform directly or indirectly. Violations are misdemeanors: up to 1 year jail and $1,000–$25,000 per violation (HIGH — [LegiScan bill text](https://legiscan.com/CA/text/AB831/id/3272819); [ZwillGen summary](https://www.zwillgen.com/gaming/californias-ab-831-bans-sweepstakes-casinos-expands-liability-vendors/)). This is a direct payments-rail liability exposure, not just an operator-side ban — vendor/processor knowledge-based liability is the salient point for this codebase.

### Licensing & change management

N/A — no legal online sports betting or online casino to license (see status above). If a DFS or sweepstakes-adjacent product is contemplated for CA, treat AB 831 and the AG's DFS opinion as active legal risk, not settled law — escalate to compliance/legal before any CA-facing launch.

### Deposits & permitted payment methods

N/A — no legal online RMG deposit channel exists to regulate. The operative payments requirement is the inverse: CA must be geo-blocked from any online sports betting / online casino deposit flow, and — per AB 831 — the payment rail itself carries misdemeanor exposure if it knowingly and willfully processes deposits for a sweepstakes-casino-style product accessible from CA.

### Withdrawals & payout timelines

N/A — no legal online RMG product; no withdrawal SLA exists in CA law for this codebase's products.

### Player funds segregation / reserve

N/A — no statewide RMG online licensee; no state-mandated reserve regime for online sports betting/casino (card rooms and tribal gaming have their own, separate financial-integrity rules under the Gambling Control Act / tribal compacts, which are out of scope for an online payments rail).

### Responsible gambling

N/A — no state-run online RMG self-exclusion/limits regime for sports betting or casino exists to integrate with. (California's Office of Problem Gambling operates public-health-style prevention programs, not a wagering account self-exclusion list, because there is no regulated online wagering to exclude from.)

### KYC / age / geolocation

N/A as a compliance obligation (no licensed product to gate), but this is the highest-priority code-review item: any nationwide sports betting/casino product must have a hard, non-bypassable CA geofence, because CA is an outright-illegal-to-operate jurisdiction under Penal Code §337a, not merely an unregulated one.

### AML overlays

N/A — no state gaming AML overlay exists beyond general federal BSA obligations that would apply to any money-services activity; no CA gaming regulator issues gaming-specific AML rules because there is no licensed CA gaming product.

### Records, reporting & data

N/A for online sports betting/casino. Card rooms and tribal operators have Gambling Control Act / compact-level reporting duties (Bus. & Prof. Code §19800 et seq.) that are out of scope for this codebase.

## Code review focus

- **Hard DEFAULT-DENY geo/jurisdiction block for CA** on every deposit, wager-placement, and account-creation path for online sports betting and online casino products — CA is an illegal, not merely unregulated, market (Penal Code §337a bookmaking; Cal. Const. art. IV §19 limits legal gaming to tribal-compact and card-room channels that exclude online sports betting/casino). Do not treat CA like an "unlaunched" state — treat it like a permanently-blocked one absent a future ballot measure.
- Confirm the geofence keys off real-time geolocation (not just billing/mailing address) consistent with the Wire Act / UIGEA illegal-market rationale used elsewhere in this skill's DEFAULT-DENY guidance.
- **If any DFS product is in scope:** flag CA as elevated legal risk given the AG's July 2025 opinion; do not silently allow CA in a DFS-specific config without a compliance sign-off gate, since the opinion (though not self-enforcing yet) reclassifies paid DFS as wagering.
- **If any sweepstakes/social-casino (dual-currency) product is in scope:** AB 831's vendor-liability clause reaches "payment processor" and "geolocation provider" directly — audit whether this codebase's payment rails or geolocation services could be characterized as "knowingly and willfully" supporting a dual-currency sweepstakes platform accessible from CA, and ensure CA is excluded from that product's serviceable region before 1/1/2026 style features ship.
- No withdrawal-SLA, reserve, or RG-limits code paths need CA-specific logic (nothing to comply with) — the only required CA-specific logic is the deny-block plus the AB 831 vendor-liability audit above.

## Sources & confidence

- [Cal. Const. art. IV, §19 Justia](https://law.justia.com/constitution/california/article-iv/section-19/) — HIGH, tribal-compact-only gaming framework.
- [2022 California Proposition 27 Wikipedia](https://en.wikipedia.org/wiki/2022_California_Proposition_27) · [NPR Prop 26/27 results](https://www.npr.org/2022/11/09/1133986282/california-gambling-prop-26-27-midterm-results) — HIGH, both propositions failed Nov. 2022.
- [Penal Code §337a bookmaking Justia CALCRIM](https://www.justia.com/criminal/docs/calcrim/2900/2990/) — HIGH.
- [Business & Professions Code §19800 et seq., Gambling Control Act CGCC](https://www.cgcc.ca.gov/documents/enabling/California_Gambling_Law_Regulations_and_Resource_Information.pdf) — HIGH, card-room licensing (out of scope for online product but confirms no online carve-out).
- [AB 831 bill text, Ch. 623 Stats. 2025 LegiScan](https://legiscan.com/CA/text/AB831/id/3272819) · [ZwillGen AB 831 analysis](https://www.zwillgen.com/gaming/californias-ab-831-bans-sweepstakes-casinos-expands-liability-vendors/) · [Newsom signs sweepstakes ban iGaming Business](https://igamingbusiness.com/gaming/gaming-regulation/newsom-california-sweepstakes-casinos-ban/) — HIGH, sweepstakes ban + vendor/payment-processor liability, effective 1/1/2026.
- [CA AG DFS opinion coverage NBC San Diego](https://www.nbcsandiego.com/news/local/california-attorney-general-says-daily-fantasy-sports-are-illegal-in-the-state/3863225/) · [ZwillGen DFS regulatory uncertainty](https://www.zwillgen.com/publication/regulatory-uncertainty-daily-fantasy-sports-california/) — HIGH on opinion existing/content, MEDIUM on enforcement posture.
- [2026 outlook / ballot-measure momentum sportsepreneur.com](https://sportsepreneur.com/california-sports-betting-standoff/) — LOW/trade-press only; verify against primary CA Secretary of State ballot-measure filings before relying on any 2026/2028 launch-timing assumption.
- No 403 blocks encountered. No statute numbers were invented; where a specific code section could not be confirmed from a primary source, the requirement is marked N/A with the reasoning stated rather than a guessed citation.
