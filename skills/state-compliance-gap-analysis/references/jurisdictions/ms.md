# Mississippi — Mississippi Gaming Commission (MGC)

**Code:** MS · **Products:** retail sportsbook only (no statewide mobile — see below) · **Key authority:** Mississippi Gaming Control Act, Miss. Code Ann. § 75-76-1 et seq. (esp. §§ 75-76-89, -33, -5); MGC Regulations Title 13: Gaming, Part 9 (Racebooks and Sports Pools) & Part 3 (Operations)

## Legal-status note (read first)

Mississippi has **no statewide mobile/online sports wagering**. Sports pools must accept wagers only on the book's licensed premises (Rule 3.4(b)), and the only form of "mobile" wagering the MGC permits is **on-property electronic/mobile wagering confined to the physical casino-hotel footprint by device geofence** (Rule 3.15) — explicitly excluding parking garages/lots (Rule 3.15(c)). As of the 2026 session, **statewide mobile sports betting has again failed**: HB 1581 (the "Mississippi Mobile Sports Wagering Act") passed the MS House 85-31 for a third consecutive year but died without a Senate committee vote at the March 3, 2026 deadline; companion/competing bills (SB 2249, HB 297, SB 2104) did not advance either. (HIGH confidence — corroborated by multiple contemporaneous 2026 legal-alert and trade-press sources; verify against the final 2026 session Legislature record before relying on this for a launch decision.)

## Payments-relevant requirements

### Licensing & change management

- No person/entity may operate a race book or sports pool without a gaming license and Executive Director permission specifically for that book; third parties providing operational/technical support to a book must hold manufacturer and distributor licenses (Rule 2.1(a)-(c)).
- Each licensed book must submit an internal control system for Executive Director approval **before commencing operations** (Rule 2.1(d)); house rules changes likewise require prior Executive Director approval (Rule 3.2(a)).
- Any communications technology installed on a book's premises requires prior written Executive Director approval per unit/location, and a book must re-obtain written permission **annually by July 1** to continue using previously approved wagering-communications technology (Rule 3.14(a)-(b)) — Executive Director may order immediate removal without notice/hearing.
- New/non-standard event types (other than horse race, greyhound race, or athletic sports event) require a separate approval request describing the wagering technology and supervisability before offering wagers (Rule 3.11(b)).

### Deposits & permitted payment methods

- Wagers may be funded only by cash, chips, tokens, or other Executive-Director-approved representatives of value, or against credits to a **Wagering account**, or on credit per the licensee's approved internal controls (Rule 3.4(a)).
- A Wagering account ("an electronic account... established by a patron at a casino property," Rule 1.1(i)) **must have its initial verification done in person, on the licensee's premises**, before any wager may draw on it — this applies identically to the on-property mobile-wagering account flow (Rule 3.4(a); Rule 3.15(b)(1)).
- No specific enumerated list of card/ACH/e-wallet rails (unlike CO/MD) — the regs are payment-instrument-agnostic beyond cash/chips/tokens/account-credit/credit; any electronic deposit rail funding a Wagering account is Executive-Director-approved by internal-control submission, not by regulation text (confidence MEDIUM — no rail-level enumeration found in Part 9; verify against a specific licensee's approved internal controls if code needs a rail allow-list).

### Withdrawals & payout timelines

- Winning wagers are paid on presentation of the patron's betting ticket at the book (or an "affiliated book" sharing a common parent, with 3-year cross-accounting) (Rule 3.8(a)-(b)).
- Books must **honor winning tickets for 30 days** after the event's conclusion unless a longer period is set (stated on the ticket, in house rules, and via premises notices) (Rule 3.8(c)).
- **Payment by mail is capped at 10 days after presentment** of the ticket and required ID/documentation (Rule 3.8(c)) — this is the closest analog to a payout SLA; there is no separate "electronic withdrawal within N days" rule because there is no off-premises wagering account withdrawal channel today (confidence HIGH on the text; MEDIUM on applicability to a future mobile withdrawal flow).

### Player funds segregation / reserve

- Each book must maintain access to a cash reserve of **not less than the greater of $50,000, or** the sum of: (i) amounts held for patron accounts, (ii) aggregate wagers on undetermined outcomes, and (iii) amounts owed but unpaid on winning wagers through the honoring period (Rule 3.1(a)) — this is in addition to, not a replacement for, the licensee's general casino bankroll requirement.

### Responsible gambling

- Statewide voluntary self-exclusion program administered by MGC: minimum term **3 years**, in-person enrollment (photograph + signed form) at an MGC office, surrender of player-club cards; casinos must eject a self-excluded patron discovered on premises and notify MGC of the breach (13 Miss. Code R. §§ 3-10.2, 3-10.4). (HIGH — Cornell LII regulation text + MGC's own self-exclusion program page.)
- Casinos must post problem-gambling materials (nature/symptoms, self-exclusion procedure, MS Council on Compulsive Gambling toll-free number) at gaming-premises entrances/exits (MGC problem-gaming program page; confidence MEDIUM on exact regulatory citation — verify Part 3 chapter/rule number).
- No sports-pool-specific deposit/spend/time-limit or cooling-off/reverse-withdrawal rule located in Part 9 — Mississippi's RG framework is exclusion-list-centric rather than limits-centric (confidence LOW/MEDIUM on completeness; verify with compliance team against any newer Part 3 RG chapter).

### KYC / age / geolocation

- Minimum gaming age is **21**; a person under 21 "shall not play, be allowed to play, place wagers or collect winnings" under the Gaming Control Act, and licensees must control the gaming area to keep minors out (Rule 11.9, Part 3; also defined at Rule 9.1/definitions, "Minor" = under 21) (HIGH).
- Wagering-account identity verification is **in-person, on licensed premises**, as the sole KYC gate described in Part 9 — no digital/remote identity-verification pathway is contemplated because there is no off-premises channel (Rule 3.4(a), Rule 3.15(b)(1)).
- Geofencing is enforced at the **facility-boundary level, not the state-border level**: approved mobile gaming may occur anywhere within the casino-hotel's licensed property boundary (excluding parking garages/areas), and the Executive Director must ensure mobile gaming "shall not extend outside of the property boundaries of the casino hotel facility" (Rule 3.15(c)-(d)). This is a materially different geolocation model than the statewide geofence used in mobile-legal states — code written for a state-border geofence will silently over-authorize in MS.

### AML overlays (state-specific, beyond federal BSA)

- **$10,000 nonpari-mutuel wager/payout threshold** triggers ID collection (name, address, SSN attempt, government ID) both before acceptance and in post-transaction recordkeeping — a state-level CTR analog independent of the federal BSA CTR (Rule 3.5(a)-(b)).
- "Listed patron" exception process lets a book request MGC approval to exempt a known, vetted patron from per-transaction Rule 3.5 reporting (not from recordkeeping) — approval deemed granted if MGC doesn't deny within 15 days (Rule 3.5(d)).
- **$5,000 wagering multiple-transaction log** requirement (per 24-hour "designated period," per monitoring area) to catch structuring below the $10,000 threshold, with aggregation-triggers-Rule 3.5 logic once cumulative wagers exceed $10,000 in the period (Rule 3.6).
- Explicit **anti-structuring prohibition** — books/employees/agents may not encourage, instruct, or knowingly assist a patron in structuring wagers to evade Rule 3.5 (Rule 3.7).
- **Suspicious-wager reporting** (a SAR analog): mandatory report to MGC for any suspicious wager aggregating over $5,000, filed within 5 calendar days of detection (extendable to 10 days if no suspect identified yet); tipping-off prohibited; reports are confidential/privileged (Rule 3.12).
- Book Wagering Reports (aggregating Rule 3.5-triggering activity, excluding listed patrons) due to MGC **within 15 days after month-end** (Rule 3.5(e)).

### Records, reporting & data

- Rule 3.5/3.6 CTR-analog records and reports retained **≥3 years**, extendable at Executive Director discretion (Rule 3.5(e)).
- Suspicious-wager reports and supporting documentation retained **≥3 years** from filing (Rule 3.12(d)).
- General books-and-records retention (records/reports/forms required by Part 9) is **≥3 years** unless the Executive Director requires longer (Rule 3.16(b)); pari-mutuel wagering records separately retained **3 years** (Rule 4.7(i)).
- Accounting records (amount wagered per book, gross revenue, federal excise tax paid) must be maintained in commission-approved form (Rule 3.17).

## Code review focus

- **Geofence model mismatch (highest-priority payments/geo gap):** any the operator payment-authorization path gating deposits/wagers on "state = MS" (a statewide geofence) is wrong for this jurisdiction — MS requires a **facility-boundary geofence tied to a specific licensed casino property**, excluding that property's parking areas, with no wagering permitted off that footprint at all (Rule 3.15(c)-(d)). If the operator has no MS-licensed retail/on-premises product today, the correct code posture is: **MS should not be an enabled deposit/wager jurisdiction in the payments rail config at all** — default-on statewide rails must be explicitly denylisted for MS rather than assumed covered by a generic US-state allowlist.
- In-person account-verification gate: if any MS-adjacent flow exists, the "account established + KYC'd" precondition must require an in-person, on-premises verification event (not remote/digital KYC) before the wagering-account funds path opens (Rule 3.4(a), 3.15(b)(1)).
- $10,000 wager/payout ID-and-record trigger and the $5,000 multiple-transaction log/aggregation window (24-hour "designated period") are distinct from federal BSA CTR/SAR thresholds used elsewhere in the codebase — do not silently dedupe MS's state-specific $10k/$5k logic into the shared federal AML threshold constants without confirming the amounts and time windows match (Rule 3.5, 3.6).
- Structuring-detection logic (aggregation across a 24-hour period per "monitoring area") needs a MS-specific aggregation key if genericized AML tooling assumes a single global entity-level rolling window.
- 30-day ticket-honoring + 10-day mail-payout timers are retail/paper-ticket-shaped, not wallet-shaped — if any MS retail cash-out integrates with <wallet-api>, confirm the timers aren't silently defaulted to a shorter mobile-state SLA (e.g., MD's 7-day withdrawal) that doesn't apply here.
- $50,000-floor reserve calculation (or higher, per formula) is a MS-specific overlay on top of general bankroll — if a shared reserve-calculation service exists across jurisdictions, confirm it isn't skipping the $50k floor for MS.
- 21+ age gate and self-exclusion (3-year minimum, in-person enrollment, cross-casino statewide list) — confirm any shared RG/self-exclusion service can represent an in-person-only enrollment flow with no digital opt-in, consistent with MS having no online channel.

## Sources & confidence

- [MGC Regulations Title 13, Part 9 — Racebooks and Sports Pools primary; official MGC PDF](https://www.msgamingcommission.com/images/uploads/MGC_sports_and_race_pool_regulations.pdf) — Rules 1.1, 2.1, 3.1–3.19, 4.1–4.10 cited above; fetched and parsed directly (WebFetch could not render this PDF; extracted via local `pdftotext`).
- [MGC Regulations Title 13, Part 3 — Operations primary; official MGC PDF](https://www.msgamingcommission.com/images/uploads/MGC_RegsPart_3_Operations.pdf) — Rule 9.1/11.9 underage gaming (21+), extracted via local `pdftotext`.
- [13 Miss. Code R. § 3-10.2 — Request for Self-Exclusion Cornell LII](https://www.law.cornell.edu/regulations/mississippi/13-Miss-Code-R-SS-3-10-2)
- [13 Miss. Code R. § 3-10.4 — Duties of Casino Cornell LII](https://www.law.cornell.edu/regulations/mississippi/13-Miss-Code-R-SS-3-10-4)
- [MGC Problem Gaming / Self-Exclusion program page](https://www.msgamingcommission.com/links/problemgaming/problem_gaming)
- [Mississippi Legislature Returns to Mobile Sports Wagering and Sweepstakes Policy in 2026 Natural Law Review / Jones Walker](https://natlawreview.com/article/mississippi-legislature-returns-mobile-sports-wagering-and-sweepstakes-policy-2026)
- [Mississippi Mobile Sports Betting and Sweepstakes Ban Bills Die Again as House–Senate Divide Persists Gambling Insider, 2026](https://www.gamblinginsider.com/news/115763/mississippi-mobile-sports-betting-sweepstakes-ban-bills-die-committee-2026)
- [Mississippi House Passes Online Sports Betting Bill for Third Straight Year Gambling Insider, 2026](https://www.gamblinginsider.com/news/109067/mississippi-house-passes-online-sports-betting-bill-for-third-straight-year)
- [HB1581 2026 Regular Session — LegiScan bill tracker](https://legiscan.com/MS/bill/HB1581/2026)
- Mississippi Gaming Control Act, Miss. Code Ann. § 75-76-1 et seq. — cited throughout Part 9 as statutory source; not independently re-verified section-by-section against the Mississippi Code itself (confidence MEDIUM on exact statute-vs-regulation attribution — the regulation PDF cites the statute sections directly, so treat those citations as HIGH; any claim above *not* tied to a quoted rule number should be treated as LOW and verified).
- Confidence: **HIGH** on retail-only + on-premises-geofence model, $50k+ reserve floor, 30-day/10-day payout timers, $10k/$5k AML thresholds, 21+ age minimum, 3-year self-exclusion minimum, and 2026 statewide-mobile-bill failure (multiple corroborating primary/press sources). **MEDIUM** on payment-rail enumeration (no card/ACH-specific text found — may exist only in individual licensees' approved internal controls, which are not public), RG limits/cooling-off framework, and problem-gambling-posting rule's exact citation. **LOW / verify**: whether any 2025-2026 MGC rule amendment has updated Part 9 since this fetch, and the exact current Miss. Code Ann. section numbers for cross-references not directly quoted in the Part 9 PDF text.
