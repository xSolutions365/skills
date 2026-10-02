# Alaska — No RMG Regulator; charitable gaming only (Alaska Dept. of Revenue, Charitable Gaming Program) (AK-DOR)

**Code:** AK · **Products:** none licensed (online/retail sports betting, casino, and lottery are not authorized under state law); charitable gaming only (bingo, pull-tabs, raffles, and specific race/contest "classics") conducted by qualified municipalities/organizations; DFS operates in an unresolved statutory gray area; sweepstakes-casino operates via the federal sweepstakes/promotional-law channel · **Key authority:** Alaska Stat. Title 11, Ch. 66, Art. 2 (§§11.66.200–.280, gambling offenses & definitions); Alaska Stat. Title 05, Ch. 15 (Charitable Gaming Act); HB 145 (34th Legislature, 2025–2026 biennium) and companion Governor bills SB 188 / HB 246 (state lottery with sports-betting authority) — **none enacted as of this writing, verify current status**

## Payments-relevant requirements

### Licensing & change management

- No RMG licensing regime exists. AS 11.66 criminalizes gambling generally (promoting gambling, possession of gambling records/devices, etc.), with a narrow statutory carve-out under AS 05.15 (Charitable Gaming Act) limited to bingo, pull-tabs, raffles, and specific race/contest classics conducted by permitted municipalities/nonprofits — not a commercial RMG framework (HIGH — Alaska DOR Charitable Gaming Program materials + Justia AS 11.66/05.15).
- HB 145 (introduced March 2025 by Rep. David Nelson, carried over for 2026) would create up to 10 online sportsbook licenses under the AK Dept. of Revenue, a $100,000 annual license fee, and a 20% tax on adjusted gross sports-wagering revenue; it was held in the House Labor & Commerce and Finance Committees in 2025 and, per mid-2026 trade-press coverage, has still seen no floor movement (MEDIUM — verify current status directly on akleg.gov before relying on this, bill status changes quickly). Companion Governor bills SB 188 / HB 246 propose a state lottery with sports-betting authority — also not enacted (MEDIUM).
- No change-management/testing-lab regime exists because no RMG product is licensed — N/A.

### Deposits & permitted payment methods

- N/A — no legal RMG deposit channel exists to regulate.
- DFS: no AK statute regulates daily fantasy sports specifically. Operators (DraftKings, FanDuel, etc.) rely on "skill contest" reasoning traced to a 2001 Alaska Department of Law/AG opinion, but the Legislature has never codified DFS and no court or AG opinion has definitively resolved its status — this is materially weaker legal footing than Alabama's codified §8-19F carve-out (MEDIUM — multiple trade-press sources agree DFS is a "gray area" in AK; the underlying 2001 AG opinion was located but its precise scope was not independently re-verified here, confidence on the opinion's exact holding is LOW).
- Alaska's gambling test is notably stricter than most states: AS 11.66.280 defines a "contest of chance" as one where the outcome depends "in a material degree" on chance, even if skill is also a factor — a lower bar for something to count as gambling than the "predominant factor" test used elsewhere (MEDIUM, per legislative commentary/secondary sources — this is precisely why DFS legality is unresolved in AK rather than affirmatively settled as in AL).
- Sweepstakes-casino: no AK statute bans the dual-currency ("Gold Coin"/"Sweeps Coin") sweepstakes model; it is generally treated as falling outside AS 11.66's gambling definition so long as no purchase/consideration is required to enter (MEDIUM).

### Withdrawals & payout timelines

- N/A — no statewide RMG withdrawal SLA exists; there is no licensed product to impose one on.

### Player funds segregation / reserve

- N/A for sportsbook/casino.
- No AK statute requires DFS fund segregation or a reserve — in contrast to Alabama's codified §8-19F-4 requirement, DFS operators' fund-handling practices in AK are not state-mandated (MEDIUM).

### Responsible gambling

- N/A — no state deposit/spend/time-limit, cooling-off, or self-exclusion regime exists for sportsbook, casino, or DFS.
- AS 05.15 charitable gaming imposes permit/financial-reporting obligations on the *conducting nonprofit*, but has no patron-level responsible-gaming limit regime relevant to a commercial payments platform (LOW relevance here).

### KYC / age / geolocation

- N/A — no state age/ID/geolocation regime for online wagering exists, because no online RMG product is authorized.
- HB 145, if enacted, proposes a 21+ minimum age and AK DOR licensing/geolocation infrastructure — but this is pending legislation, not current law (MEDIUM, contingent).

### AML overlays

- N/A — no AK-specific gaming AML program exists. Only generally-applicable federal BSA/AML obligations would apply to any payment-processor activity; no state overlay identified (MEDIUM).

### Records, reporting & data

- AS 05.15 charitable-gaming permit holders file activity/financial reports with the AK Dept. of Revenue Charitable Gaming Program, but this is nonprofit bingo/pull-tab specific and not applicable to a commercial payments platform (LOW relevance).
- No RMG-specific payments records/reporting regime exists.

## Code review focus

- **Hard geo/jurisdiction DEFAULT-DENY for AK**: sportsbook and online-casino deposit/wager/payout endpoints must reject any AK-located account by default. AS 11.66 makes the underlying gambling activity itself a criminal offense (not merely unlicensed), so the payments platform's default-on per-state method-rail enablement is a direct illegal-market / Wire Act exposure unless AK is explicitly excluded.
- **DFS carve-out is higher-risk than Alabama's**: AK's DFS legality rests on an unresolved ~2001 AG "skill contest" opinion, not a statute. Before treating AK the same as AL's codified DFS carve-out, flag to legal/compliance whether the operator's risk appetite supports offering paid DFS contests in AK at all. If approved, there is no statutory fund-segregation or non-standard age-floor requirement to hard-code (unlike AL's 19+/reserve rule) — default to the platform's standard 21+ and general fund-segregation policy absent an AK-specific mandate, and log this as a policy choice, not a statutory requirement.
- **Sweepstakes-casino carve-out** (if offered): preserve the no-purchase-necessary / dual-currency structure in the ledger model — removing the "no consideration to enter" element risks pulling the product into AS 11.66's "contest of chance" gambling definition given AK's low "material degree of chance" bar.
- **Track HB 145 and the SB 188/HB 246 lottery-with-sports-betting companion bills each legislative session** — if any is enacted, AK flips from DEFAULT-DENY to a full licensing/payments build (reserve, withdrawal SLA, RG limits, geolocation, AK DOR reporting) similar to other regulated states; re-run this gap analysis promptly if signed into law.

## Sources & confidence

- [2025 Alaska Statutes, Title 11, Ch. 66, Art. 2, §11.66.280 — Definitions Justia](https://law.justia.com/codes/alaska/title-11/chapter-66/article-2/section-11-66-280/)
- [AS 11.66.280 FindLaw](https://codes.findlaw.com/ak/title-11-criminal-law/ak-st-sect-11-66-280/)
- [Charitable Gaming Program overview Alaska Dept. of Revenue, PDF](https://dor.alaska.gov/docs/taxdivisionlibraries/tax-type-docs/charitable-gaming/gaming-publications/2021_05-overview-of-charitable-gaming.pdf)
- [2025 Alaska Statutes, Title 5, Ch. 15, Art. 3, §05.15.620 — Local prohibition of charitable gaming Justia](https://law.justia.com/codes/alaska/title-5/chapter-15/article-3/section-05-15-620/)
- [Bill To Legalize Sports Betting In Alaska Back For 2026 — Legal Sports Report](https://www.legalsportsreport.com/253257/bill-to-legalize-sports-betting-in-alaska-back-for-2026/)
- [Alaska sports betting bill still in play as legislative session nears end — Yogonet 2025-05-21](https://www.yogonet.com/international/news/2025/05/21/105509-alaska-sports-betting-bill-still-in-play-as-legislative-session-nears-end/)
- [HB 145 bill detail — Alaska State Legislature akleg.gov](https://www.akleg.gov/basis/Bill/Detail/34?Root=hb+145)
- [Alaska Sports Betting: Legal Status, Updates, and More — Bleacher Nation 2026-06-02](https://www.bleachernation.com/betting/2026/06/02/alaska/)
- [2001 Alaska Dept. of Law opinion memo re: gaming law.alaska.gov, PDF](https://law.alaska.gov/pdf/opinions/opinions_2001/01-007_663010183.pdf)
- Confidence: HIGH on the AS 11.66/AS 05.15 statutory framework (gambling prohibited generally; charitable gaming the only carve-out) and on no lottery/casino/sports-betting being currently authorized. MEDIUM on HB 145 / SB 188 / HB 246 status — legislative status changes session-to-session, re-verify on akleg.gov before relying on this. MEDIUM/LOW on the precise scope of the 2001 AG opinion underpinning DFS's "gray area" status — the opinion was located but its holding was not independently re-verified line-by-line here; treat any DFS-in-AK product decision as needing dedicated legal review, not just this file.
