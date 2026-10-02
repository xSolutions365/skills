# Minnesota — Minnesota Department of Public Safety, Alcohol & Gambling Enforcement Division (AGED) / Minnesota Gambling Control Board (MGCB)

**Code:** MN · **Products:** none authorized online (no legal statewide sports betting or online casino); DFS operates without a specific statute (unregulated, "game of skill" reliance) · **Key authority:** Minn. Stat. §§ 609.75-609.76 (general gambling prohibition & exemptions); Minn. Stat. § 3.9221 (tribal-state compact authorization); Minn. Stat. ch. 240 (pari-mutuel horse racing); Minn. Stat. ch. 349 (lawful/charitable gambling); Minn. Stat. ch. 349A (State Lottery)

## Status (read before the subsections below)

Minnesota has **no authorized statewide online real-money-gaming (RMG) channel** of any kind — no sports betting, no online casino, no iLottery. Minn. Stat. § 609.755 makes placing a bet a misdemeanor and § 609.76 escalates unlicensed bookmaking/wagering-business activity to a gross misdemeanor or felony, unless the activity falls within an enumerated exemption: the state lottery (ch. 349A), licensed charitable gambling (ch. 349, bingo/raffles/pull-tabs incl. handheld electronic pull-tabs under § 349.12/§ 349.1721 — a bar-tablet product, not internet wagering), pari-mutuel horse racing (ch. 240), and tribal Class III gaming conducted under a compact negotiated per § 3.9221. Minnesota's 11 tribal nations operate ~20 retail casinos (blackjack, video games of chance) under 22 compacts (HIGH — verified via MN DPS/Federal Register compact filings), but **no compact authorizes online or mobile wagering**, and the legislature has not broken the long-running impasse between tribes (who want mobile-betting exclusivity) and the state's two horse tracks (Canterbury Park, Running Aces, who want a cut) — SF 4139 / HF 4204 ("Minnesota Sports Betting Act 3.0," tribal-exclusive mobile framework, 22% tax) stalled again when the 94th Legislature adjourned 5/18/2026 without a floor vote in either chamber (HIGH). DFS (DraftKings, FanDuel, PrizePicks, Underdog, Thrillzz) continues to operate on the "game of skill" / UIGEA-carveout theory with no MN-specific statute addressing it either way (MEDIUM — DPS has not issued a binding opinion). The MN Attorney General has actively pursued enforcement against unlicensed online gambling sites taking MN bettors (AG press release, 11/5/2025, citing §§ 609.75-.76) — treat MN as an enforcement-active illegal-market state, not a dormant one.

## Payments-relevant requirements

### Licensing & change management

N/A — no online RMG licensing regime exists to review code against. Tribal compacts under § 3.9221 govern retail-only Class III systems and are outside a payment gateway's scope; charitable-gambling electronic pull-tab systems (§ 349.12, § 349.1721, Minn. R. 7864.0235) are a bar-tablet product, not an online channel the operator would integrate with.

### Deposits & permitted payment methods

N/A — see status. No statute authorizes a real-money online deposit channel for sports betting or casino play in MN; any such deposit from an MN-located bettor is itself evidence of the prohibited predicate act under § 609.755. DFS deposits are unaddressed by MN gaming law (no gaming-specific payment-method rule to satisfy) but remain in scope for FED-US/PCI/AML baseline treatment.

### Withdrawals & payout timelines

N/A — no statutory withdrawal SLA exists because no licensed online RMG product exists to have one.

### Player funds segregation / reserve

N/A — no state-mandated reserve/segregation formula for online RMG. (Charitable-gambling proceeds accounting under ch. 349 and tribal compact revenue-sharing are separate regimes, not applicable to a payment gateway.)

### Responsible gambling

N/A for online RMG — no statewide self-exclusion program exists; where tribal casinos offer self-exclusion it is a per-property voluntary contract with the individual casino, not a statutory or centralized MGCB/AGED list (MEDIUM — confirmed no statewide list found; verify no newer legislative addition).

### KYC / age / geolocation

**Not N/A — this is the control that matters for MN.** Because no online RMG is authorized, the only correct code behavior is to refuse MN-located sessions/deposits for sportsbook and casino products entirely; there is no "verify age 21+ then allow" path to build, only a jurisdiction gate that blocks. Treat any evidence of an MN-reachable deposit/wager path for sportsbook or casino as a `red` finding regardless of KYC quality behind it. DFS may be geo-permitted per product policy given the unregulated status, but confirm against current company policy before treating it as safe-by-default (MEDIUM).

### AML overlays

N/A beyond federal BSA — no MN-specific AML statute for RMG identified; general MGCB oversight of charitable-gambling cash handling is a separate regime.

### Records, reporting & data

N/A for online RMG. AG enforcement precedent (11/5/2025 action against illegal gambling websites) is the closest analog to a "records" requirement: expect MN regulators/AG to request evidence of how MN traffic was identified and blocked, not transaction records for a licensed product.

## Code review focus

- **Default-deny, not default-allow:** confirm the state/jurisdiction config for MN defaults sportsbook and online-casino rails to blocked, not merely "unconfigured" — a payments platform that is default-on everywhere else must special-case MN to closed rather than relying on a state-config row that doesn't exist yet. Verify this at the geolocation gate, not just at a UI/marketing layer.
- Cross-check any illegal-market / UIGEA / Wire Act block-list logic against MN explicitly — the AG's active enforcement posture (11/5/2025 action) makes an accidental MN-reachable deposit path a real regulatory-exposure finding, not a theoretical one.
- DFS carve-out: if the operator's DFS product (`FundType.FANTASY_*` / `ClientId.FANTASY_PAYMENTS` per this repo's wallet conventions) is enabled in MN, confirm that's a deliberate, documented product decision (unregulated-but-tolerated) rather than an accidental fallthrough of the same code path used for sportsbook/casino.
- Sweepstakes-casino ("sweeps") dual-currency products: MN has not legislated on sweeps casinos either way (LOW — verify current status; treat as a monitoring item, not a green light) — if the operator or any integrated partner offers a sweeps-style product reachable from MN, flag for legal review rather than assuming the DFS carve-out logic applies.
- Watch SF 4139 / HF 4204 (tribal-exclusive mobile sports betting): if either advances, MN flips from "block everything" to "tribal-operator-only licensing," which would need a net-new state-config row, not a relaxation of the current block — do not pre-build a deposit path speculatively.

## Sources & confidence

- [Minn. Stat. § 609.75 Revisor](https://www.revisor.mn.gov/statutes/cite/609.75) · [§ 609.755](https://www.revisor.mn.gov/statutes/?id=609.755&view=full) · [§ 609.76](https://www.revisor.mn.gov/statutes/cite/609.76) · [§ 609.761 exemptions](https://www.revisor.mn.gov/statutes/cite/609.761)
- [Minn. Stat. ch. 349 Lawful Gambling, 2025](https://www.revisor.mn.gov/statutes/cite/349/pdf) · [§ 349.12](https://codes.findlaw.com/mn/gaming-ch-349-350/mn-st-sect-349-12.html) · [§ 349.1721](https://www.revisor.mn.gov/statutes/cite/349.1721)
- [MN AG press release, illegal gambling websites, 11/5/2025](https://www.ag.state.mn.us/Office/Communications/2025/11/05_IllegalGamblingWebsites.asp) (page unreachable at fetch time — connection refused; cited via search-result excerpt, confidence MEDIUM, re-verify directly before external use)
- [MN Dept. of Public Safety — Tribal-State Gaming Compacts](https://dps.mn.gov/divisions/age/gambling/tribal-state-gaming-compacts) (404 at fetch time; compact facts corroborated via Federal Register filings and MN Senate research page below)
- [MN Senate — American Indian Communities in MN: Gaming](https://www.senate.mn/departments/scr/report/bands/gaming.htm) · [Federal Register — Fond du Lac Class III compact](https://www.federalregister.gov/documents/2024/10/17/2024-23989/indian-gaming-approval-of-tribal-state-class-iii-gaming-compact-between-the-fond-du-lac-band-of-lake)
- [SF 4139 bill status MN Revisor](https://www.revisor.mn.gov/bills/94/2026/0/SF/4139/) · [HF 4204 MN Revisor](https://www.revisor.mn.gov/bills/94/2026/0/HF/4204) · [Legal Sports Report — 2026 session outcome](https://www.legalsportsreport.com/258345/minnesota-sports-betting-bill-avoids-committee-change/)
- Confidence: HIGH on the general prohibition/exemption structure (§§ 609.75-.761), tribal compact scope (retail Class III only), and the 2026 legislative-session outcome (adjourned without passage). MEDIUM on DFS's precise legal footing (no MN statute or binding AG/DPS opinion located) and on AG enforcement specifics (source page unreachable at fetch time, relying on search-engine excerpt — verify directly). LOW on sweepstakes-casino treatment in MN (no dedicated legislation found either way) — flag for compliance-team verification before relying on it.
