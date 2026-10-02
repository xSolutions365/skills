# Georgia — no state gaming-control regulator for RMG online; Georgia Lottery Corporation (GLC) administers the state lottery only

**Code:** GA · **Products:** none — no legal online or retail sports betting, no legal online or retail casino gaming (constitutional amendment required and repeatedly rejected, most recently March 2026); state lottery (draw games + lottery-authorized electronic games) exists under GLC; DFS is an unresolved gray area (2016 informal AG opinion said DFS is "not authorized," but no enforcement and major operators still serve GA); sweepstakes/social casino platforms are untested/unregulated, no ban in force · **Key authority:** Ga. Const. art. I, §II, ¶VIII (gambling prohibition + lottery/bingo exceptions only); O.C.G.A. §16-12-20 et seq. (criminal gambling statutes); O.C.G.A. §50-27-1 et seq. (Georgia Lottery for Education Act); 2026 session: House Resolution 450 (constitutional amendment for sports betting, FAILED 3/6/2026) and Senate Bill 386 (non-constitutional lottery-framework sports betting bill, passed Senate, stalled in House)

## Payments-relevant requirements

**Threshold finding (verify before using any subsection below):** Georgia's constitution prohibits "all forms of pari-mutuel betting and casino gambling" except where specifically carved out, and the only carve-outs exercised to date are the state lottery (1992 amendment) and nonprofit bingo — sports betting and casino gaming have neither (HIGH — [Ga. Const. art. I, §II, ¶VIII, FindLaw](https://codes.findlaw.com/ga/constitution-of-the-state-of-georgia/ga-const-art-1-sect-2-viii/)). Georgia has rejected sports-betting legalization for multiple consecutive sessions; in the 2026 session, House Resolution 450 (a constitutional amendment, needing a 2/3 supermajority) failed on the House floor on Crossover Day, March 6, 2026, by a vote of 63–98 against a 120-vote threshold, despite having cleared the Senate and polling ~63% public support (HIGH — [Georgia Recorder](https://georgiarecorder.com/briefs/house-lawmakers-overwhelmingly-reject-proposal-to-legalize-sports-betting-in-georgia/), [The Current GA](https://thecurrentga.org/2026/03/07/efforts-to-legalize-sports-betting-in-georgia-stall-as-lawmakers-reject-bill/)). A parallel non-constitutional path — Senate Bill 386, which would authorize sports betting under the Georgia Lottery Corporation's existing statutory authority without amending the constitution — passed the Senate but stalled in the House; as of Aug. 2026 it has not been enacted (MEDIUM — trade press, [Gambling Insider](https://www.gamblinginsider.com/news/103736/georgia-sports-betting-bill-hb910-2026-lottery), corroborate against Georgia General Assembly's bill tracker before relying on exact status). There is no tribal Class III gaming in Georgia (no federally recognized gaming tribe with land in the state), so unlike CA/FL there is not even a retail tribal-casino carve-out.

- **DFS (daily fantasy sports):** No Georgia statute addresses DFS. In 2016 the Georgia Lottery Corporation asked the Attorney General's office for a position; the AG's office responded with "informal advice" (explicitly not a formal opinion) that DFS contests "are not authorized under Georgia law." No enforcement has followed, and major DFS operators (DraftKings, FanDuel, and pick'em-style platforms) continue to serve Georgia residents. Legalization bills (HB 118 in 2017, HB 1329 in 2024) both died before passage (MEDIUM — multiple secondary sources agree on the fact pattern; the underlying 2016 informal-advice letter itself was not independently retrieved, so treat exact wording as LOW/verify).
- **Sweepstakes / social casino (dual-currency):** No Georgia law specifically addresses dual-currency sweepstakes platforms; no enforcement action has been taken by the Georgia AG, and some operators that had paused GA availability during 2025 legal uncertainty elsewhere resumed GA operations in August 2025. Georgia is named in trade press as one of several states with an active bill or task force "examining" sweepstakes casinos as of mid-2026, but nothing has passed (MEDIUM — trade/industry sources only, e.g. [bettorsinsider.com](https://bettorsinsider.com/sweepstakes/legal/georgia/); no primary legislative or AG source confirmed a pending GA sweepstakes bill by name — LOW/verify if this becomes decision-relevant).

### Licensing & change management

N/A — no legal online or retail sports betting or casino product exists to license. The Georgia Lottery Corporation licenses lottery retailers under O.C.G.A. §50-27-1 et seq., which is out of scope for a sports betting/casino payments product.

### Deposits & permitted payment methods

N/A — no legal online RMG deposit channel exists. As in other no-legal-market states, the operative payments requirement is the inverse: GA must be geo-blocked from any online sports betting / online casino deposit flow.

### Withdrawals & payout timelines

N/A — no legal online RMG product; no withdrawal SLA exists in Georgia law for this codebase's products.

### Player funds segregation / reserve

N/A — no statewide RMG online licensee; no state-mandated reserve regime for online sports betting/casino.

### Responsible gambling

N/A — no state-run online RMG self-exclusion/limits regime for sports betting or casino exists to integrate with.

### KYC / age / geolocation

N/A as a compliance obligation (no licensed product to gate), but — as with CA — this is the highest-priority code-review item: sports betting and casino gaming are criminal offenses in Georgia absent the (not-yet-existing) constitutional/statutory carve-out (O.C.G.A. §16-12-20 et seq.), so GA needs a hard geofence, not a "state not yet launched" placeholder.

### AML overlays

N/A — no state gaming AML overlay exists beyond general federal BSA obligations; no Georgia gaming regulator issues gaming-specific AML rules because there is no licensed GA online sports betting/casino product. (The GLC's lottery-specific controls are out of scope.)

### Records, reporting & data

N/A for online sports betting/casino. GLC lottery retailer records under O.C.G.A. §50-27-1 et seq. are out of scope for this codebase.

## Code review focus

- **Hard DEFAULT-DENY geo/jurisdiction block for GA** on every deposit, wager-placement, and account-creation path for online sports betting and online casino products — Georgia gambling is a criminal offense absent a specific statutory/constitutional exception (Ga. Const. art. I, §II, ¶VIII; O.C.G.A. §16-12-20 et seq.), and no such exception exists for sports betting or casino gaming as of Aug. 2026. Treat GA as permanently blocked, not "pending launch," subject to the SB 386 / future constitutional-amendment tracker below.
- **Track SB 386 (non-constitutional lottery-framework sports betting bill) and any successor constitutional amendment resolution** as the two live legalization vehicles — either passing would be the trigger to move GA off DEFAULT-DENY; confirm current session status against the Georgia General Assembly's official bill tracker before any launch-readiness decision, since trade-press "stalled" status can change between legislative sessions.
- **If any DFS product is in scope:** GA's 2016 AG informal-advice letter is not enforced and not binding case law, but flag it as a known legal-gray-area jurisdiction alongside CA's more recent, more formal 2025 opinion — do not treat GA as automatically "safe" for DFS without a compliance/legal sign-off, since the underlying legal theory (DFS-as-wagering) mirrors the reasoning used elsewhere to restrict DFS.
- **If any sweepstakes/social-casino product is in scope:** no GA-specific vendor/payment-processor liability clause was found (unlike California's AB 831), so no equivalent hard block is currently required by statute — but confidence on "no pending GA sweepstakes bill" is MEDIUM/LOW; re-check before each release since multiple neighboring/comparator states enacted bans in 2025-2026 and GA is reported to be one of several states "examining" the issue.
- No withdrawal-SLA, reserve, or RG-limits code paths need GA-specific logic today — the only required GA-specific logic is the deny-block plus periodic re-verification of the SB 386 / constitutional-amendment and sweepstakes-bill status.

## Sources & confidence

- [Ga. Const. art. I, §II, ¶VIII FindLaw](https://codes.findlaw.com/ga/constitution-of-the-state-of-georgia/ga-const-art-1-sect-2-viii/) — HIGH, gambling prohibition + lottery/bingo-only exceptions.
- [O.C.G.A. §16-12-20, Definitions Justia](https://law.justia.com/codes/georgia/2022/title-16/chapter-12/article-2/part-1/section-16-12-20/) — HIGH, gambling statute framework; lottery carve-out for GLC games.
- [Georgia Recorder, House rejects sports betting, March 2026](https://georgiarecorder.com/briefs/house-lawmakers-overwhelmingly-reject-proposal-to-legalize-sports-betting-in-georgia/) · [The Current GA, HR 450 fails 3/6/2026](https://thecurrentga.org/2026/03/07/efforts-to-legalize-sports-betting-in-georgia-stall-as-lawmakers-reject-bill/) — HIGH, HR 450 failed 63–98 on Crossover Day.
- [Gambling Insider, GA renews push via HB 910/SB 386 lottery framework](https://www.gamblinginsider.com/news/103736/georgia-sports-betting-bill-hb910-2026-lottery) — MEDIUM, trade press; verify SB 386/HB 910 exact status against the Georgia General Assembly's official bill tracker (not independently retrieved here).
- [Daniel C. Collins Paralegal Services, GA DFS-vs-sports-betting explainer](https://danielccollinsparalegal.com/online-gambling-in-georgia-why-sleeper-style-fantasy-is-legal-but-game-betting-is-not-and-how-tn-fl-differ/) · [bettingusa.com GA DFS status](https://www.bettingusa.com/states/ga/daily-fantasy/) — MEDIUM, secondary sources on the 2016 AG informal-advice letter and 2017/2024 failed DFS bills; the original 2016 letter was not independently retrieved — LOW/verify if a specific DFS compliance decision hinges on its exact wording.
- [bettorsinsider.com, GA sweepstakes casino legal status guide](https://bettorsinsider.com/sweepstakes/legal/georgia/) — LOW/trade-press only; no primary GA statute or AG action confirmed a pending sweepstakes bill — re-verify before relying on this for a launch decision.
- No 403 blocks encountered. No statute or bill numbers were invented; HR 450 and SB 386 numbers are corroborated across independent trade-press sources but were not cross-checked against the Georgia General Assembly's own bill-tracking site in this pass — confidence MEDIUM on exact bill numbers/status, recommend a direct legislature.ga.gov check before treating as final.
