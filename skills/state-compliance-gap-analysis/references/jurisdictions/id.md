# Idaho — No licensed regulator for commercial real-money sports betting/casino/DFS (state lottery + tribal Class III gaming only)

**Code:** ID · **Products:** none for sportsbook/online casino/DFS — the only legal RMG in Idaho is the state lottery (Idaho Lottery Commission) and tribal Class III gaming under IGRA compacts, neither of which is a commercial online product this codebase would integrate · **Key authority:** Idaho Const. art. III, §20 (Gambling Not to Be Authorized); Idaho Code Title 18, ch. 38, §§18-3801 et seq. (Gaming); Idaho Code Title 67, ch. 74 (Idaho State Lottery); 2016 Idaho AG opinion (Wasden) — paid DFS is illegal gambling

## Payments-relevant requirements

### Status (read first — governs every subsection below)

- Idaho's constitution (art. III, §20) declares gambling "contrary to public policy" and permits only three narrow carve-outs by enabling legislation: a state lottery, pari-mutuel betting, and charitable bingo/raffle games — and expressly bars any of those carve-outs from employing casino-style games (blackjack, craps, roulette, poker, baccarat, keno, slots) or electronic simulations thereof. Because this restriction is constitutional, not merely statutory, legalizing sports betting/online casino in Idaho would require a constitutional amendment (voter referendum), a materially higher bar than an ordinary legislative session. (HIGH.)
- Idaho Code §18-3801 defines "gambling" broadly — risking value for gain contingent on "lot, chance, the operation of a gambling device or the happening or outcome of an event, **including a sporting event**" — with narrow exemptions for bona fide skill contests, bona fide business transactions, and merchant promotions with no participant consideration. There is no sports-betting, online-casino, or DFS carve-out. (HIGH.)
- **DFS status (explicit bar):** in a May 2016 opinion, Idaho AG Lawrence Wasden concluded paid daily fantasy sports contests are illegal gambling under Idaho law, holding that chance plays too substantial a role for DFS to qualify for the skill-contest exemption. DraftKings and FanDuel both exited Idaho in 2016 and DFS has not been re-legalized since. This is an AG interpretive opinion (not a court ruling or DFS-specific statute), but it is the operative, enforced position — treat DFS in Idaho as barred with the same severity as sports betting. (HIGH.)
- Only lawful real-money gambling in Idaho: the Idaho State Lottery (Idaho Code Title 67, ch. 74) and Class III tribal gaming conducted under NIGC-approved tribal ordinances and negotiated tribal-state compacts (~7 tribal casinos, incl. Coeur d'Alene, Kootenai, Nez Perce) per IGRA — neither is a commercial third-party online sportsbook/casino/DFS product and neither is relevant to this codebase's payment rails. (HIGH.)
- No 2026 legislative movement toward legalizing sports betting or online casino was found. Idaho AG Raul Labrador has been active on a *related but distinct* front: joining a multistate coalition (March 2026) challenging CFTC/federal authority over sports-event prediction-market contracts (e.g., Kalshi-style products) — this is about **preserving Idaho's state authority to keep such products out**, not legalizing anything. Treat prediction-market/event-contract products the same as sports betting for Idaho purposes. (MEDIUM — recheck each session and monitor the CFTC litigation, since its outcome could affect how "sports event contracts" are treated nationally.)

### Licensing & change management

- N/A — no legal RMG online gaming (see status). No regulator, licensing regime, or platform-certification process exists for any commercial online real-money gambling product in Idaho.

### Deposits & permitted payment methods

- N/A — no legal RMG online gaming (see status).

### Withdrawals & payout timelines

- N/A — no legal RMG online gaming (see status).

### Player funds segregation / reserve

- N/A — no legal RMG online gaming (see status).

### Responsible gambling

- N/A — no legal RMG online gaming (see status).

### KYC / age / geolocation

- N/A — no legal RMG online gaming (see status) for any state-licensed KYC/age/geo regime. Federal exposure (Wire Act, UIGEA illegal-market risk) applies to any operator accepting wagers, deposits, or account registrations from Idaho-located patrons regardless of state licensing status; Idaho's history of proactive AG enforcement (2016 DFS cease-and-desist precedent) indicates real enforcement risk, not just theoretical exposure.

### AML overlays

- N/A — no legal RMG online gaming (see status).

### Records, reporting & data

- N/A — no legal RMG online gaming (see status).

## Code review focus

- Idaho has no authorized online RMG rails, so the default posture must be a hard **DEFAULT-DENY geo/jurisdiction block** for ID-located sessions, accounts, deposits, withdrawals, and wager placement across every product line — not a soft warning.
- **DFS entry points are the single highest-specific risk item for Idaho**: because Idaho bars DFS by AG opinion rather than a DFS-named statute, a jurisdiction-gate implementation that only keys off "sportsbook"/"casino" product flags and treats DFS as ungated will silently permit an illegal-market DFS flow for ID patrons. Confirm DFS is explicitly enumerated in the same deny-list as sportsbook/casino for ID.
- If the platform or a planned feature offers sports-event prediction-market/event-contract products, include those in the ID deny-block too — Idaho's AG is actively litigating to keep this category out, signaling elevated enforcement attention.
- Every money-movement entry point (registration, deposit, withdrawal, wager/contract placement) must consult the same jurisdiction allowlist; the main code risk is config drift where ID is "unlisted therefore allowed."
- Idaho's bar is constitutional, not just statutory — near-term legalization is far less likely than in states like Hawaii that only need a legislative vote. This lowers the priority of watching for a legalization bill, but does not lower the priority of the deny-block itself, given Idaho's track record of active enforcement (2016 DFS cease-and-desist).
- Geolocation/IP allowlisting should treat ID identically to other never-legal states; billing-address checks alone are insufficient — device/GPS-based geolocation is needed to catch travelers and VPN circumvention.

## Sources & confidence

- [Idaho Constitution art. III, §20 Idaho State Legislature](https://legislature.idaho.gov/statutesrules/idconst/artiii/sect20/) · [Idaho Const. art. III, §20 Justia](https://law.justia.com/constitution/idaho/article-iii/section-20/)
- [Idaho Code §18-3801 Gambling Defined Idaho State Legislature](https://legislature.idaho.gov/statutesrules/idstat/title18/t18ch38/sect18-3801/) · [Idaho Code Title 18, Ch. 38 Gaming Justia](https://law.justia.com/codes/idaho/title-18/chapter-38/)
- [Idaho Code Title 67, Ch. 74 Idaho State Lottery Justia](https://law.justia.com/codes/idaho/title-67/chapter-74/) · [§67-7402 Idaho Lottery Agency Created Idaho State Legislature PDF](https://legislature.idaho.gov/wp-content/uploads/statutesrules/idstat/Title67/T67CH74.pdf)
- [DraftKings/FanDuel exit Idaho after 2016 AG opinion LegalSportsReport](https://www.legalsportsreport.com/sports-betting/states/idaho/) · [Idaho AG DFS illegal-gambling opinion context LegalClarity](https://legalclarity.org/idaho-gambling-laws-definitions-regulations-and-enforcement/)
- [Idaho tribal Class III gaming compacts / IGRA framework background](https://www.federalregister.gov/documents/2024/02/21/2024-03456/class-iii-tribal-state-gaming-compacts) · [Coeur d'Alene Tribe–Idaho 1993 Class III compact BIA](https://www.bia.gov/sites/default/files/dup/assets/as-ia/oig/pdf/508_compliant_1993.02.12_coeur_d_alene_tribe_tribal_state_gaming_comapct.pdf)
- [Idaho joins 39-state coalition vs. CFTC on sports-event contracts, March 2026 Covers](https://www.covers.com/betting/usa/idaho)
- Confidence: HIGH on the constitutional/statutory prohibition, the absence of any legal commercial online RMG product, and the 2016 AG DFS opinion still being the operative position. MEDIUM on the exact current list of tribal Class III compact-holders (count/names may have changed) and on the precise status/outcome of the CFTC prediction-market litigation — verify both with compliance/legal before final sign-off; neither affects the code-review recommendation (default-deny) either way.
