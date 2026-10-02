# BSA/AML depth — casino SAR/CTR, structuring, crypto MSB

**Lane:** AML · **Authority:** BSA (31 USC 5311-5332); FinCEN casino/card-club rules 31 CFR 1021; MSB rules 31 CFR 1022 · **Researched:** Aug 2026 (cage/kiosk cash-channel refresh Sep 2026)

Goes beyond the CTR $10k line in the FED baseline: the casino-specific BSA program, SAR mechanics, structuring detection, and crypto/MSB Travel Rule. Much is owned by an AML system — but the payments code feeds it (aggregation inputs, thresholds, holds).

## Key requirements

- **AML program (31 CFR 1021.210):** written program, designated officer, training, independent testing — operators >$1M gross gaming revenue are "financial institutions."
- **CTR (Currency Transaction Report):** cash/cash-equivalent >$10,000 in a gaming day, **aggregated across methods and sessions** — boundary cases ($9,999/$10,000/$10,001) must be handled; cash-in and cash-out.
- **SAR:** suspicious activity ≥$5,000 (structuring, minimal-play deposit→withdraw laundering, rapid movement). Any fraud/AML “fail-safe” control that changes behavior at a daily deposit threshold (e.g., $10,000) should be reviewed here.
- **Structuring detection:** patterns just under $10k across a day/multiple methods.
- **Recordkeeping:** 5-year retention of CTRs/SARs/support; **MTL/Travel Rule** for transmittals ≥$3,000 (originator/beneficiary info).
- **Crypto (if offered):** MSB registration, Travel Rule on crypto transmittals, wallet attribution.
- **Retail cash channel — cage & redemption kiosk (Title 31):** the cage and self-service **redemption/recharge kiosks** are cash-in/cash-out points that count toward the **same per-patron, per-gaming-day CTR aggregation** as digital and floor activity (cash-out includes cage chip/token redemptions **and kiosk slot-ticket redemptions**). MTL/MIL logs at cage (cf. state MTL thresholds NJ/MD/OH); kiosk slot-ticket **redemption detail** records (machine, ticket #, amount, redemption time). Applies to the retail cash channel (cage/teller/kiosk endpoints and any retail service), not just the digital deposit/withdraw APIs.

## Code review focus

- **Aggregation inputs:** does the payments code expose per-gaming-day, **cross-channel** cash totals (cage + kiosk + digital) that a CTR engine needs? Grep `ctr`, `sar`, `aggregat`, `gamingDay`, `structuring`, `10000`, `travelRule`, and on the retail path `teller`, `cage`, `kiosk`, `redemption`, `TITO`, `voucher`, `cashOut`. If a fraud-service fail-safe exists, confirm its policy: when the fraud service is unavailable, deposits auto-approve only below a daily threshold (e.g. $10k) and auto-decline above it.
- **Boundary handling** at the $10,000 / $5,000 / $3,000 thresholds.
- **5-year retention** of transaction records feeding reports (overlaps records/data).
- Crypto rail attribution + Travel-Rule fields, if crypto is live.

## Test coverage focus

- **Unit** tests on threshold/aggregation boundaries ($9,999 vs $10,000 vs $10,001; single vs aggregate) wherever the aggregation lives — classic boundary tests.
- Any fraud-service fail-safe branch (fail-open below the daily threshold / fail-closed above it) asserted — incident-relevant.
- If CTR/SAR aggregation is upstream, verify the payments code emits the metadata it needs; flag ownership.

## Sources & confidence

- 31 CFR 1021 (casinos/card clubs), 1022 (MSBs), 1010 (general BSA); FinCEN casino guidance FIN-2010-G002 and SAR/CTR instructions.
- **Cage/kiosk cash-channel refresh (Sep 2026):** eCFR [31 CFR Part 1021](https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1021) + [Subpart C](https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1021/subpart-C); [FinCEN casino recordkeeping/reporting FAQs](https://www.fincen.gov/resources/statutes-regulations/guidance/frequently-asked-questions-casino-recordkeeping-reporting); [IRS ITG casino reporting FAQ](https://www.irs.gov/government-entities/indian-tribal-governments/itg-faq-8-answer-what-are-the-reporting-requirements-for-casinos). Confirmed: CTR aggregates cash-in **or** cash-out > $10k/gaming day across cage + kiosk + floor; kiosk slot-ticket redemptions are cash-out; 15-day filing; 5-yr retention. (Per-state kiosk/cage caps — IL/IN ~$3k, CO ICMP eff. 2026-04-01, NV 2026 cashless-kiosk draft — live in the state jurisdiction defs, not here.)
- Confidence: HIGH on thresholds + the cage/kiosk cash-channel obligation; MEDIUM on ownership split (AML system / retail operator / casino BSA officer vs the payments code) — verify aggregation source. Pull latest for FinCEN AML/CFT program rule (2024 proposal) and any crypto Travel-Rule updates.
