# South Carolina — South Carolina Law Enforcement Division (SLED) / South Carolina Education Lottery Commission (SCEL)

**Code:** SC · **Products:** none authorized (no legal casino, no legal sports betting, no legal online RMG of any kind); DFS operates in an unaddressed gray area (not explicitly legal or illegal) · **Key authority:** S.C. Const. art. XVII, § 7 (lottery ban + Education Lottery carve-out); S.C. Code Title 16, Ch. 19 (criminal gambling: §§ 16-19-10, -30, -40, -60, -130); S.C. Code Title 59, Ch. 150 (Education Lottery Act, incl. § 59-150-210 sales restrictions); S.C. Code Title 33, Ch. 57 (nonprofit raffles, § 33-57-100); S.C. Code Title 12, Ch. 21, Art. 24 (Bingo Tax Act of 1996)

## Status (read before the subsections below)

South Carolina is one of the most restrictive gaming states in the country. Its constitution (art. XVII, § 7) prohibits lotteries outright and permits **only** a state-operated Education Lottery, added by a 2000 voter-approved amendment, plus a narrow bingo carve-out for charitable/religious/fraternal organizations and recognized state/county fairs (HIGH — Justia constitutional text, corroborated by SC AG opinions). Title 16, Ch. 19 separately criminalizes lotteries (§ 16-19-10), gaming tables/devices (§ 16-19-40, the archaic "A, B, C, or E, O" games language, still in force), and bookmaking/pool-selling on races, elections, and contests (§ 16-19-130) (HIGH — direct primary-source fetch of scstatehouse.gov). **There is no casino gaming and no sports betting of any kind, retail or online, anywhere in South Carolina** — no tribal gaming compacts, no commercial casino statute, no riverboat/cruise-ship carve-out. Lottery tickets may only be sold by licensed in-state retailers for cash; § 59-150-210 and SCEL's own FAQ confirm **no internet/online lottery ticket sales** are permitted (HIGH). Repeated legislative attempts fail: the furthest any sports-betting bill has gotten is S.444 (2026, up to 8 licensed online operators, 12.5% tax on AGR), which cleared a Senate Labor, Commerce & Industry Committee hearing in Feb 2026 but had not reached a floor vote as of March 2026; companion casino bill H.4176 (I-95 casino) and companion sports-betting bill H.3625 remain stalled in committee (HIGH — CDC Gaming, casino.org, SCCG Management). Term-limited Governor Henry McMaster has opposed gambling expansion throughout his tenure (he campaigned against the 2000 lottery referendum) and has given no indication he would sign a sports-betting bill even if it passed, effectively requiring a two-thirds override (HIGH — multiple 2026 political-coverage sources). DFS (DraftKings, FanDuel, etc.) operates in an explicit gray area: the SC AG's office has stated it is "not taking action on online gambling" and has received no complaints or opinion requests specifically on DFS (MEDIUM — SC Public Radio reporting; no statute or AG opinion squarely addresses DFS).

## Payments-relevant requirements

### Licensing & change management

N/A — no online RMG licensing regime exists in SC to review code against. There is no gaming commission analog to certify a wagering platform.

### Deposits & permitted payment methods

N/A — see status. No statute authorizes a real-money online sports-betting or casino deposit channel; any such deposit accepted from an SC-located bettor is itself the predicate act for the Title 16, Ch. 19 offenses above. Lottery deposits are moot since tickets are cash-only, in-person, and never sold online (§ 59-150-210). DFS deposits are unaddressed by SC gaming law specifically (no gaming-specific payment-method rule to satisfy) but remain in scope for FED-US/PCI/AML baseline treatment.

### Withdrawals & payout timelines

N/A — no statutory withdrawal SLA exists because no licensed online RMG product exists to have one.

### Player funds segregation / reserve

N/A — no state-mandated reserve/segregation formula for online RMG. (Bingo Tax Act proceeds accounting under Title 12, Ch. 21, Art. 24 and lottery-fund allocation under Title 59, Ch. 150 are separate regimes, not applicable to a payment gateway.)

### Responsible gambling

N/A — no statewide self-exclusion list or RG program exists for online RMG because no such product is authorized. SCEL's own responsible-play messaging applies to lottery-ticket purchase only, which is cash/in-person.

### KYC / age / geolocation

**Not N/A — this is the control that matters for SC.** Because no online RMG is authorized in any form, the only correct code behavior is a hard block of SC-located sessions/deposits for sportsbook and casino products; there is no "verify age 21+ then allow" path to build, only a jurisdiction gate that refuses. Treat any evidence of an SC-reachable deposit/wager path for sportsbook or casino as a `red` finding regardless of KYC quality behind it. DFS may be geo-permitted per product policy given the unaddressed/gray status, but confirm against current company policy before treating it as safe-by-default (MEDIUM) — the AG's "not taking action" stance is not the same as legality, and could reverse.

### AML overlays

N/A beyond federal BSA — no SC-specific AML statute for RMG identified; general Bingo Tax Act cash-handling oversight is a separate charitable-gambling regime.

### Records, reporting & data

N/A for online RMG. No SC regulator maintains records-retention rules for a product that cannot legally exist in the state.

## Code review focus

- **Default-deny, not default-allow:** confirm the state/jurisdiction config for SC defaults sportsbook and online-casino rails to blocked, not merely "unconfigured" — the platform is default-on everywhere else, so SC must be an explicit closed state in config rather than an absent row that silently falls through to an allowed default.
- Cross-check illegal-market / UIGEA / Wire Act block-list logic against SC explicitly — with no tribal or commercial carve-out anywhere in the state, an SC-reachable deposit path has no mitigating context the way it might in a state with at least some legal retail gaming.
- DFS carve-out: if the operator's DFS product (`FundType.FANTASY_*` / `ClientId.FANTASY_PAYMENTS` per this repo's wallet conventions) is enabled in SC, confirm that's a deliberate, documented product decision resting on the AG's non-enforcement posture, not an accidental fallthrough of the same code path used for sportsbook/casino — and flag that posture as reversible, unlike a statutory carve-out.
- Sweepstakes-casino ("sweeps") dual-currency products: multiple sweeps operators (e.g., Pulsz, McLuck, NoLimitCoins) currently serve SC players and a federal lawsuit naming a sweeps operator has been filed in SC alleging the model is illegal RMG (MEDIUM — verify current litigation status before treating SC as settled either way). If the operator or an integrated partner offers a sweeps-style product reachable from SC, flag for legal review rather than assuming the DFS carve-out logic applies.
- Watch S.444 / H.3625 (sports betting) and H.4176 (I-95 casino): even if either clears the legislature, Gov. McMaster's opposition makes a veto override the likely blocker through at least Jan 2027 — do not pre-build a deposit path speculatively, and treat any change here as a net-new state-config addition, not a relaxation of the existing block.

## Sources & confidence

- [S.C. Const. art. XVII, § 7 Justia](https://law.justia.com/constitution/south-carolina/a17.html) (direct scstatehouse.gov PDF fetch failed at run time — binary/unparseable; corroborated via Justia + multiple secondary legal-summary sources, confidence HIGH on substance, re-verify exact text against the official PDF before external citation)
- [S.C. Code Title 16, Ch. 19 — Gambling and Lotteries scstatehouse.gov, primary, fetched directly](https://www.scstatehouse.gov/code/t16c019.php)
- [S.C. Code § 59-150-210, Sales restrictions Justia](https://law.justia.com/codes/south-carolina/title-59/chapter-150/section-59-150-210/) · [S.C. Education Lottery Act, Title 59 Ch. 150 scstatehouse.gov](https://www.scstatehouse.gov/code/t59c150.php)
- [S.C. Code § 33-57-100, Lotteries or raffles unlawful unless authorized Justia](https://law.justia.com/codes/south-carolina/title-33/chapter-57/section-33-57-100/)
- [S.C. Code Title 12, Ch. 21, Bingo Tax Act of 1996 / § 12-21-4020 Justia](https://law.justia.com/codes/south-carolina/title-12/chapter-21/section-12-21-4020/)
- [CDC Gaming — SC gambling bills hit early roadblocks, 2026 session](https://cdcgaming.com/brief/south-carolina-gambling-bills-hit-early-roadblocks-in-2026-session/) · [Casino.org — Sports betting fight renews in SC](https://www.casino.org/news/sports-betting-fight-renews-in-south-carolina/) · [SCCG Management — Political hurdles for SC sports betting bill, Feb 2026](https://sccgmanagement.com/sccg-news/2026/2/19/political-hurdles-for-south-carolina-sports-betting-bill/)
- [SC Public Radio — DFS remains in gray territory](https://www.southcarolinapublicradio.org/sc-news/2024-03-26/sc-fantasy-sports-betting-future)
- Confidence: HIGH on the constitutional lottery ban + Education Lottery carve-out, the Title 16 Ch. 19 criminal-gambling provisions, the online-lottery-sales ban, and the 2026 legislative stalemate (S.444/H.3625/H.4176 stalled, McMaster opposed). MEDIUM on DFS's precise legal footing (AG non-enforcement stance, not a binding opinion or statute) and on sweepstakes-casino litigation status (actively moving — re-check before external use). LOW on nothing invented here; every statute cite above was independently located via a primary scstatehouse.gov page or a direct Justia codification — flag any future addition without such a source as LOW + verify.
