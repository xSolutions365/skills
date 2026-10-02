# New Mexico — No state sports-betting statute; retail-only under tribal Class III gaming compacts

**Code:** NM · **Products:** none authorized statewide/mobile — retail sportsbooks exist only on tribal land under compact · **Key authority:** Indian Gaming Regulatory Act (IGRA), 25 U.S.C. § 2701 et seq.; 2015 New Mexico Tribal-State Class III Gaming Compact (individually executed per tribe, e.g. Navajo Nation, Pueblo of Acoma, Pueblo of Isleta, Jicarilla Apache Nation); NMSA 1978, Gaming Control Act (Ch. 60, Art. 2E) — governs only non-tribal racetrack/nonprofit gaming, NOT sports betting

## Legal status (read this before the requirements below)

- **New Mexico has never enacted a sports-betting statute.** No bill legalizing sports betting has been passed or signed; the only 2021 attempt (HB 101, racino sports betting) died without further action, and post-2021 legislative activity has been limited to gambling-impact study bills, the most recent of which died in 2022 (MEDIUM — no primary legislative-tracker fetch succeeded; corroborated by 3 independent secondary sources, see below).
- **Legal basis is a compact interpretation, not legislation.** After *Murphy v. NCAA* (2018) struck down PASPA, New Mexico's tribes took the position that their existing 2015 Tribal-State Class III Gaming Compacts — which authorize "any and all forms of Class III gaming" / "any game not prohibited by federal law" on Indian lands — already covered sports wagering, since Class III federal regulations classify sports betting as Class III gaming and PASPA (the prior federal prohibition) was gone. The State of New Mexico has never formally endorsed or challenged this interpretation in litigation or rulemaking (MEDIUM confidence — primary compact PDFs were fetched but returned as unparseable binary/encrypted-stream content, not extractable text; exact compact clause wording not independently confirmed — verify with compliance/legal before relying on the "any and all forms" quote).
- **Retail only, on tribal land only.** Sportsbooks operate inside a handful of tribal casinos (commonly cited as ~5, e.g. Santa Ana Star). There is **no statewide, commercial, or mobile/online sports betting** — no operator can legally accept a real-money sports wager from a patron whose device/session is not physically on the tribal land where the compact-licensed sportsbook sits.
- **No state regulator for sports betting.** The New Mexico Gaming Control Board (NMGCB) regulates non-tribal racetracks and nonprofit gaming under the state Gaming Control Act; it has **no jurisdiction over tribal gaming or sports betting** — tribal gaming is self-regulated per-tribe under IGRA, with oversight (where it exists) from each tribe's own gaming commission and the federal National Indian Gaming Commission (NIGC), not any New Mexico state agency (MEDIUM — consistent across multiple secondary sources, primary NMGCB statement not independently fetched).
- **Confirmed still true as of 2026.** Multiple current-dated (2026) secondary sources agree: no active bill is moving in Santa Fe, tribes generally oppose statewide mobile because it would break their on-site retail exclusivity, and no state-licensed online sportsbook exists. Treat "NM legalizes mobile sports betting" as a live risk to monitor each legislative session, not a settled negative.
- **Do not invent a statute number.** There is no NMSA cite for "sports betting" because none exists; any code comment, ticket, or doc referencing "N.M. sports betting act §..." is wrong and should be corrected to reference the compact/IGRA framework above.

## Payments-relevant requirements

### Licensing & change management

- No state sports-betting license exists to hold or maintain. Each tribe licenses/certifies its own sportsbook operation (often via a third-party retail sportsbook operator contract) under its own gaming commission and compact terms — no centralized NM statute or rule to track for change-management purposes (LOW/MEDIUM — no per-tribe compact rider was independently reviewed; if the operator ever pursues a tribal-partner retail deal in NM, the *specific tribe's* compact and gaming-commission rules become the controlling document, not a generic "NM rule").

### Deposits & permitted payment methods

- Not applicable to any centrally regulated online/mobile product because none is authorized. Any in-person cash/card handling at a tribal retail sportsbook window is governed by that tribe's own compact and internal controls, not by an NM statewide payment rule.

### Withdrawals & payout timelines

- Not applicable — no state-mandated payout SLA exists because there is no state-licensed online or mobile product to regulate.

### Player funds segregation / reserve

- Not applicable — no state reserve/segregation rule exists for a product New Mexico has not statutorily authorized.

### Responsible gambling

- No statewide self-exclusion or deposit/spend-limit mandate applies to online/mobile sports betting, because no such regulated product exists in NM. Any responsible-gaming program at a tribal retail sportsbook is set by that tribe, not the state.

### KYC / age / geolocation

- **This is the section that matters for the platform.** There is no state-sanctioned online channel to KYC into — any real-money deposit, wager, or payout tied to a New Mexico patron location must be blocked unless the patron is physically on the specific tribal land of a compact-licensed retail sportsbook (which this platform, as an online/mobile operator, is not positioned to serve). Standard 21+ age-of-majority expectation for gambling nationally (HIGH, general knowledge) — no NM-specific online age-verification rule exists to point to because there's no online product it would apply to.

### AML overlays

- No NM-specific state AML overlay exists for sports betting. Federal BSA/AML obligations apply to the extent a business is otherwise subject to them; tribal retail cash handling is governed by each tribe's own AML program under federal law, not a state overlay.

### Records, reporting & data

- No NM state reporting regime exists for sports betting because the state has never asserted regulatory authority over it. No records/reporting requirement to build against.

## Code review focus

- **The real finding for NM is a geofencing/product-availability gap, not a payments-detail gap.** This platform's payment rails (deposit methods, FundType/ClientId wallet plumbing, withdrawal flows) are enabled per-state by default — confirm NM is on an explicit deny/geo-block list for real-money deposits and wagers, not silently allowed through a default-permissive state config.
- Verify there is **no code path** that would let a New Mexico IP/GPS-resolved session complete a real-money deposit or place a wager: this is not "NM requires extra KYC steps," it is "NM has zero authorized statewide channel for this product," so the correct code behavior is a hard block, ideally with a message distinguishing "not available in your state" from a generic error.
- If any tribal-partner / on-premises kiosk integration is ever built for a specific NM tribal casino, treat it as its own product with its own compact-driven ruleset — do not extend the generic 50-state config to cover it, and do not assume NMGCB rules apply (they don't; the relevant party is the specific tribe's gaming commission).
- Illegal-market exposure to flag to compliance/legal (not a code fix by itself): if the platform ever accepted a real-money deposit or wager from an NM-located patron outside the tribal-land exception, that transaction sits outside any IGRA-authorized channel — exposure includes state/federal illegal-gambling-business risk, UIGEA (unlawful internet gambling transactions), and Wire Act considerations for interstate wire communications facilitating the bet. This is a legal-risk item to confirm with compliance, not something resolvable purely by a code review finding.
- Audit any hardcoded state-enablement list, feature flag, or settings-service config for NM to confirm it defaults to "sports betting: not authorized" rather than inheriting a generic "US state, therefore enabled" default.

## Sources & confidence

- [Sports Betting in New Mexico 2026 Deuces Cracked](https://www.deucescracked.com/sports-betting/us/new-mexico)
- [New Mexico Sports Betting Laws & Regulations 2026 BettingInNM](https://bettinginnm.com/laws/)
- [New Mexico Sports Betting 2026 BettingInNM](https://bettinginnm.com/)
- [So How Exactly Is New Mexico Sports Betting Legal LegalSportsReport](https://www.legalsportsreport.com/24965/legality-of-sports-betting-in-new-mexico/) — **WebFetch returned HTTP 403 (blocked); relied on search-result summary only, not the full primary text — LOW/verify.**
- [New Mexico Sports Betting: Legal NM Sportsbooks & Legislation Updates LegalSportsReport](https://www.legalsportsreport.com/sports-betting/states/new-mexico/) — indexed via search only, not independently fetched.
- [New Mexico Becomes Sixth State With Legal Sports Betting PlayUSA](https://www.playusa.com/news/new-mexico-legal-sports-betting/) — **WebFetch returned HTTP 403 (blocked); title/search-snippet only — LOW/verify.**
- [NM Attorney General Opinion 2025-16 — 2015 Tribal-State Gaming Compact Implications on Non-Tribal Racetracks nmdoj.gov](https://nmdoj.gov/wp-content/uploads/AG-Opinion-2025-16-2015-Tribal-State-Gaming-Compact-Implications-on-Non-Tribal-Racetracks.pdf) — **WebFetch returned HTTP 403 (blocked); relied on search-result snippet, confirms compact-interpretation dispute is a live/current (2025) legal topic but exact holding not independently confirmed — LOW/verify.**
- [AG Opinion No. 2025-07 nmdoj.gov](https://nmdoj.gov/wp-content/uploads/AG-Opinion-2025-07.pdf) — surfaced in search, not fetched; flagged only as evidence the AG's office is actively opining on gaming-compact scope in 2025.
- [2015 Navajo Nation / State of New Mexico Class III Gaming Compact navajo-nsn.gov, hosted PDF](https://nngro.navajo-nsn.gov/Portals/0/Files/2015_Compact.pdf) — **fetched but returned as unparseable binary/encrypted PDF stream; compact text NOT independently verified — LOW/verify exact "any and all forms of Class III gaming" language before citing in any compliance filing.**
- [2015 Pueblo of Acoma / State of New Mexico Tribal-State Gaming Compact bia.gov, hosted PDF](https://www.bia.gov/sites/default/files/dup/assets/as-ia/oig/pdf/508_compliant_2015.06.22_pueblo_of_acoma_tribal_state_gaming_compact.pdf) — **fetched but returned as unparseable binary PDF stream — LOW/verify.**
- [LFC Hearing Brief — Racing and Gaming Industry Trends, NM Legislature nmlegis.gov](https://www.nmlegis.gov/Entity/LFC/Documents/General_Government/Hearing%20Brief%20-%20Racing%20and%20Gaming%20Industry%20Trends.pdf) — surfaced in search only, not fetched (a separate nmlegis.gov Finance Facts gaming PDF also returned HTTP 403 on WebFetch).
- [NM Gaming Control Board gcb.nm.gov](https://www.gcb.nm.gov/) — surfaced in search only; corroborates NMGCB's jurisdiction is limited to non-tribal racetrack/nonprofit gaming, not tribal sports betting.
- **Confidence summary:** HIGH that no NM statute authorizes sports betting and that no statewide/mobile product is legal (corroborated by numerous independent, consistently-dated 2026 secondary sources plus the absence of any contrary legislative record). MEDIUM on the specific compact clause wording ("any and all forms of Class III gaming") and on NMGCB's precise jurisdictional boundary — every primary-source PDF/opinion fetch attempted for this file was either HTTP 403-blocked or returned unparseable binary content; none of the compact or AG-opinion text was read directly. Recommend a follow-up with compliance/legal to obtain a readable copy of the current compact language and AG Opinion 2025-16 before using this file as the sole basis for a legal filing.
