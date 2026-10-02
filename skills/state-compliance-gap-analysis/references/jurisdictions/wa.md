# Washington — Washington State Gambling Commission (WSGC)

**Code:** WA · **Products:** none for commercial/online operators — statewide, online and mobile real-money sports wagering is PROHIBITED; the only lawful sports wagering is tribal, retail/on-premises, under Class III gaming compacts · **Key authority:** RCW 9.46 (Gambling—1973 act), esp. RCW 9.46.240 (Gambling information — transmitting or receiving, class C felony) and RCW 9.46.0364 / 9.46.0368 (Sports wagering authorized via tribal compact); Tribal-State Class III Gaming Compact sports wagering amendments (WSGC)

## Payments-relevant requirements

### Licensing & change management

- There is no commercial or state-issued online/mobile sportsbook or iGaming license class in Washington. A federally recognized WA tribe may add sports wagering only by amending its existing Class III gaming compact under the Indian Gaming Regulatory Act; the amendment must address licensing, WSGC regulatory fees, operational procedures, money-laundering/sport-integrity provisions, and responsible/problem gambling (RCW 9.46.0364). (HIGH — confirmed against app.leg.wa.gov primary text.)
- WSGC approved sports wagering compact amendments/initial rules for 15 tribes, with additional tribes negotiating since; each amendment is negotiated and administered per-tribe, not as a single statewide ruleset (HIGH, WSGC press releases).
- No path exists for a non-tribal commercial operator (the operator's typical licensing model) to obtain a WA sports-wagering or iGaming license under current law — confidence HIGH for the absence of such a license class in RCW 9.46's sports wagering sections reviewed.

### Deposits & permitted payment methods

- No centrally published state statute/rule specifies permitted payment rails for tribal sports wagering deposits; these are set at the individual tribal compact / internal-control-standard level, which WSGC does not publish centrally (LOW — verify directly with any specific tribal partner's internal controls before assuming a payment method is allowed).
- Payments-relevant consequence for a statewide/mobile-first operator: a WA bettor located off tribal premises has **no lawful real-money deposit path** with any commercial online operator. Any deposit funding an online/mobile real-money wager placed from within WA but off-reservation is not just "unlicensed" — the underlying data transmission is itself criminalized (see Records below) (HIGH).

### Withdrawals & payout timelines

- No state-level payout-timeline statute or rule for tribal sports wagering was located in WSGC's public sports-wagering materials; timelines are set per-tribe in compact/internal-control documents not centrally published (LOW — verify).

### Player funds segregation / reserve

- No state-level reserve/segregation requirement for tribal sports wagering was located in WSGC's public sports-wagering materials; reserve requirements, if any, would live in tribal internal control standards (LOW — verify).

### Responsible gambling

- Compact amendments must address "responsible and problem gambling," and participating tribes make annual contributions toward problem-gambling and smoking-cessation services payable within one year of the tribe's fiscal year close (MEDIUM — statutory obligation confirmed via RCW 9.46.0364 and WSGC compact materials; per-tribe implementation mechanics not centrally published).
- WSGC operates a statewide self-exclusion program, but **tribal casinos are not currently participants** in that statewide list (HIGH, WSGC self-exclusion program materials) — a WA self-exclusion-list check is not sufficient RG gating for any tribal wagering context.

### KYC / age / geolocation

- WSGC's published sports-wagering rules summary states operations must make reasonable efforts to prevent wagering by anyone under 18 (note: this differs from the 21+ minimum typical of commercial sportsbooks elsewhere in this matrix — do not assume 21 is the WA floor without checking the specific compact/rule text) (MEDIUM).
- Any mobile component of sports wagering must be geofenced to the physical boundary of the specific tribal gaming facility — patrons off that property cannot place mobile wagers; this is enforced via GPS/Wi-Fi triangulation tied to the casino property line, not a statewide boundary (HIGH, WSGC).
- There is no legal basis for geolocating a WA bettor as "in-state and eligible" for a statewide mobile product, because no such product is authorized in Washington — this is the core payments/compliance risk for this jurisdiction (HIGH).

### AML overlays

- Compact amendments must address money-laundering and sport-integrity provisions (RCW 9.46.0364), but the specific overlay content is negotiated per-tribe and not centrally published; presumably tribal gaming AML/BSA (Title 31) obligations apply independently at the tribal-facility level rather than as an operator-facing state rule (MEDIUM — verify per compact if a tribal partnership is contemplated).

### Records, reporting & data

- No centrally published state-level records/reporting standard for tribal sports wagering payment data was located; this would live in per-tribe internal control standards (LOW — verify).
- **RCW 9.46.240** makes it a class C felony (penalty per RCW 9A.20.021) to "knowingly transmit or receive gambling information" by telephone, internet, or similar means, or to knowingly install/maintain equipment for that transmission or receipt — with a narrow exception carved out only for activities authorized under RCW 9.46, including sports wagering authorized under RCW 9.46.0364/9.46.0368. Outside that narrow compact-based exception, the data transmission itself — not merely the wager — is the criminal act (HIGH, confirmed against the primary statute text on app.leg.wa.gov).

## Code review focus

- **Hard geo/jurisdiction block required**: WA must default to blocking all real-money deposits and wagers for any statewide/commercial mobile product. This is not a "not yet launched" state to soft-gate behind a feature flag — it is a "must not enable" state absent a direct on-premises tribal-facility integration.
- If a tribal on-premises integration is ever built, deposit/wager authorization must be gated on a **facility-level geofence** (GPS/Wi-Fi confirming physical presence on the specific tribal property), not a statewide WA boundary check — a WA-wide IP/GPS pass is insufficient and would itself be evidence of unauthorized online gambling.
- Treat WA as the **highest illegal-market / criminal-exposure jurisdiction** in this matrix: RCW 9.46.240 criminalizes the underlying gambling-information transmission (class C felony, up to 5 years / $10,000 per offense) outside the narrow compact exception, so a mis-configured state allow-list or geofence bug here carries felony exposure, not just a licensing or civil violation.
- Do not hardcode a 21+ age floor as universal — the WA tribal-rules summary reviewed cites 18+; verify against the live compact/rule text before any WA-facing launch.
- Do not let a generic per-state payment config silently default WA to another state's deposit methods, withdrawal SLA, or reserve requirement — WA has no centrally published state-level rule for any of these; they live in individual tribal compacts/internal controls, not in a state rule this codebase should assume.
- Do not treat WSGC's statewide self-exclusion list as sufficient RG gating for WA — tribal casinos do not currently participate in it.

## Sources & confidence

- [RCW 9.46.240 — Gambling information, transmitting or receiving app.leg.wa.gov](https://app.leg.wa.gov/rcw/default.aspx?cite=9.46.240)
- [RCW 9.46.0364 — Sports wagering authorized app.leg.wa.gov](https://app.leg.wa.gov/rcw/default.aspx?cite=9.46.0364)
- [WSGC — Sports wagering requirements and rules](https://wsgc.wa.gov/tribal-partnerships/sports-wagering/sports-wagering-requirements-and-rules)
- [WSGC — Gambling Commission approves fifteen Tribal sports wagering compacts and initial sports wagering rules](https://wsgc.wa.gov/news/press-releases/gambling-commission-approves-fifteen-tribal-sports-wagering-compacts-and-initial)
- [WSGC — Statewide Self-Exclusion Program Launch](https://wsgc.wa.gov/news/press-releases/wsgc-statewide-self-exclusion-program-launch)
- [WSGC — Self-exclusion: Voluntarily exclude yourself from gambling activities](https://wsgc.wa.gov/responsible-gaming-self-exclusion/self-exclusion-voluntarily-exclude-yourself-gambling-activities)
- Confidence: HIGH on the tribal-only/on-premises-geofence legal status and on the RCW 9.46.240 class C felony transmission prohibition and its narrow compact-based exception (verified against primary statute text) — this is the single most important payments-compliance fact for WA. LOW on payment methods, withdrawal timelines, reserve/segregation, and detailed records/reporting requirements, since these are set per-tribe in compact/internal-control documents that WSGC does not publish centrally; verify directly with compliance/legal and any specific tribal partner before treating WA as anything other than a hard block for standard commercial online/mobile real-money flows. RCW 9.46.0368 is referenced in the RCW 9.46.240 exception clause but was not independently fetched/verified in this pass (LOW — verify).
