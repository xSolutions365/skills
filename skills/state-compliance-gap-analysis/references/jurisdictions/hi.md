# Hawaii — No licensed gaming regulator (comprehensive prohibition on real-money gambling)

**Code:** HI · **Products:** none — no legal regulated real-money gaming of any kind (no casino, lottery, sports betting, or DFS) · **Key authority:** HRS Title 37, Chapter 712, §§712-1220–712-1231 (Offenses Against Public Health and Morals — Gambling); no state lottery statute exists; 2026 HB 2570 (online sports betting) did not pass

## Payments-relevant requirements

### Status (read first — governs every subsection below)

- Hawaii is one of only two US states (with Utah) with essentially zero legal gambling: no casinos, no state lottery, no sports betting, no legal DFS. HRS §712-1221 (Promoting Gambling 1st Degree — class B felony per 2022 Act 111), §712-1222 (Promoting Gambling 2nd Degree — misdemeanor), and §712-1223 (Gambling — participant-level offense) criminalize operating and participating in gambling activity. A narrow "social gambling" affirmative defense exists at §712-1231 (no rake, equal-terms peer play, not at a business/hotel) — it does not create any B2C real-money product exception. (HIGH.)
- **DFS status:** outlawed via a January 2016 Hawaii Attorney General opinion (AG Doug Chin) concluding paid DFS contests are unlicensed gambling under HRS ch. 712; Honolulu's prosecuting attorney followed with cease-and-desist letters and DraftKings/FanDuel voluntarily exited the state. A same-year bill to legalize and regulate DFS died. No DFS-specific statute exists — the general gambling law is what bars it — and no legalization has occurred since. (HIGH.)
- **2026 legislative activity:** HB 2570 (online-only sports betting, 6 mobile licenses, 15% GGR tax, new DCCA-housed regulator) advanced out of an early House committee in June 2026 amid strong opposition, but multiple 2026 gambling proposals (casino, state lottery, cruise-ship gambling, prediction markets, and ultimately sports betting) failed to advance past committee deadlines as legislative focus shifted to fiscal/tax matters; the 2026 regular session has adjourned without any gambling-expansion bill reaching the Governor. A prior sports-betting effort (HB 1308) died in a 2025 conference committee over tax-rate/licensing-fee disagreements. **No RMG product of any kind is authorized in Hawaii as of Aug 2026.** (HIGH on current non-passage; MEDIUM on whether any bill remains technically alive in a carryover/interim posture — verify current bill status at capitol.hawaii.gov / LegiScan before final sign-off.)

### Licensing & change management

- N/A — no legal RMG online gaming (see status). No regulator, licensing regime, platform-certification, or change-management process exists for any online real-money gambling product in Hawaii.

### Deposits & permitted payment methods

- N/A — no legal RMG online gaming (see status). No payment method, deposit channel, or funding rail is authorized because no underlying product is legal.

### Withdrawals & payout timelines

- N/A — no legal RMG online gaming (see status).

### Player funds segregation / reserve

- N/A — no legal RMG online gaming (see status).

### Responsible gambling

- N/A — no legal RMG online gaming (see status). HB 2570, had it passed, would have required standard RG provisions (self-exclusion, limits) typical of newly-legalized states — not currently in force and not code-actionable.

### KYC / age / geolocation

- N/A — no legal RMG online gaming (see status) for any state-licensed KYC/age/geo regime. Federal exposure (Wire Act, UIGEA illegal-market risk) applies to any operator that accepts wagers, deposits, or account registrations from Hawaii-located patrons regardless of state licensing status.

### AML overlays

- N/A — no legal RMG online gaming (see status).

### Records, reporting & data

- N/A — no legal RMG online gaming (see status).

## Code review focus

- Hawaii has no authorized online RMG rails whatsoever, so the default posture must be a hard **DEFAULT-DENY geo/jurisdiction block** for HI-located sessions, accounts, deposits, withdrawals, and wager placement across every product line (sportsbook, casino, DFS) — not a soft warning or opt-out.
- Every money-movement entry point (registration, deposit, withdrawal, wager/bet placement) must consult the *same* jurisdiction allowlist. The primary code risk is config drift where HI is "unlisted therefore allowed" rather than explicitly denied — this creates Wire Act/UIGEA illegal-market exposure and HRS ch. 712 promoting-gambling exposure for the operator.
- If the platform has a distinct DFS product line, it must be included in the same HI deny-block even though there's no DFS-specific statute — Hawaii bars DFS purely through the 2016 AG opinion applying the general gambling law.
- Geolocation/IP allowlisting should treat HI identically to other never-legal states; billing-address checks alone are insufficient — device/GPS-based geolocation is needed to catch travelers and VPN circumvention attempts.
- Re-check HB 2570 (or any successor) each legislative session — if Hawaii legalizes online sports betting, this file and the jurisdiction gate both need prompt updates. HB 2570's design (DCCA regulator, 6 mobile licenses, 15% GGR tax) is not yet code-actionable since it never became law.

## Sources & confidence

- [HRS §712-1223 Gambling Justia](https://law.justia.com/codes/hawaii/title-37/chapter-712/section-712-1223/) · [HRS §712-1221 Promoting Gambling 1st Degree official capitol.hawaii.gov](https://www.capitol.hawaii.gov/hrscurrent/vol14_ch0701-0853/HRS0712/HRS_0712-1223.htm) · [HRS §712-1222 Promoting Gambling 2nd Degree Onecle](https://law.onecle.com/hawaii/title-37/712-1222.html) · [HRS §712-1231 Social gambling affirmative defense capitol.hawaii.gov](https://www.capitol.hawaii.gov/hrscurrent/Vol14_Ch0701-0853/HRS0712/HRS_0712-1231.htm)
- [Hawaii AG rules DFS illegal, Jan 2016 Hawaii News Now](https://www.hawaiinewsnow.com/story/31074584/attorney-general-rules-daily-fantasy-sports-contests-illegal-in-hawaii/) · [Honolulu prosecutor cease-and-desist to DFS operators Star-Advertiser](https://www.staradvertiser.com/2016/02/02/breaking-news/honolulu-prosecutor-tells-fantasy-sports-companies-to-cease-and-desist/)
- [HB 2570 advances amid opposition, 2026 CBS Sports](https://www.cbssports.com/betting/news/hawaii-sports-betting-takes-small-step-forward-despite-opposition/) · [HB 2570 background SCCG Management](https://sccgmanagement.com/sccg-articles/2026/2/19/hawaii-sports-betting-bill-advances/) · [Hawaii 2026 gambling proposals halted / session status LegiScan](https://legiscan.com/HI) · [HB 1308 dies in 2025 conference committee SBC Americas](https://sbcamericas.com/2025/04/29/hawaii-online-sports-betting-bill-fails/) · [Hawaii lawmakers reject sports gambling bill Courthouse News](https://www.courthousenews.com/hawaii-lawmakers-reject-bill-to-legalize-sports-gambling/)
- Confidence: HIGH that no RMG online gaming product (sportsbook, casino, DFS) is legally authorized in Hawaii as of Aug 2026, and that DFS is barred via the 2016 AG opinion. MEDIUM on the precise procedural status of HB 2570/any successor in the closing weeks of the 2026 session — verify current bill text/status directly on capitol.hawaii.gov or LegiScan before relying on "dead" for a compliance sign-off, since this is the one area of active legislative motion in this file.
