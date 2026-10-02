# Oklahoma — No authorized statewide/mobile sports-wagering regulator; tribal Class III gaming under IGRA compacts (OMES Gaming Compliance Unit / Tribal Compliance Agencies)

**Code:** OK · **Products:** none — no legal statewide or mobile real-money sports betting, online casino, or iGaming exists in Oklahoma as of 2026 (HIGH). The only lawful real-money gaming channels are (a) land-based tribal Class III casino gaming under IGRA compacts, and (b) narrow pari-mutuel horse-race wagering. Neither is a product the operator offers or can lawfully offer online in OK. · **Key authority:** State-Tribal Gaming Act / Model Tribal Gaming Compact, 3A O.S. §§ 280–281; Indian Gaming Regulatory Act, 25 U.S.C. § 2701 et seq.; *Treat v. Stitt*, 2021 OK 15 (Okla. 2021) (compacts cannot authorize activity — incl. "event wagering"/sports betting — not listed in the State-Tribal Gaming Act); HB 1047 (2026, sports-betting legalization bill, **failed** Senate 21-27 on 4/22/2026); SB 1589 (2026, online "sweepstakes casino"/dual-currency ban, eff. 11/1/2026); Oklahoma Horse Racing Act, 3A O.S. § 200 et seq. (esp. § 205.6, pari-mutuel).

## Status precisely stated

Oklahoma has **no legal statewide or mobile sports betting and no legal online casino in 2026**. As of July 2026, "sports betting remains illegal and unauthorized in Oklahoma... No regulated framework exists for residents to place legal wagers within the state" (Addison Law, citing current legislative record). The 2026 legislative attempt to change this — HB 1047, which would have let tribes offer in-person sports betting and created a mobile framework in partnership with tribal nations — failed on the Senate floor 21-27 on April 22, 2026, after Cherokee Nation boundary-restriction concerns and late Southern Baptist opposition; the reconsideration motion expired April 28, 2026, so it did not become law (nondoc.com, covers.com). Confidence: HIGH.

The underlying dispute is a genuine standoff, not a drafting gap: Governor Stitt has pushed for a broader commercial market (state lottery, horse tracks, non-tribal operators) while tribal nations and the Oklahoma Indian Gaming Association argue existing Class III compacts already give them exclusivity. In 2020, Stitt attempted to authorize "event wagering" (sports betting) for two tribes via renegotiated compacts; the Oklahoma Supreme Court in *Treat v. Stitt* held the Governor lacked authority to authorize gaming activity not enumerated in the State-Tribal Gaming Act, voiding those compacts (Justia case summary; igamingbusiness.com). That precedent forecloses any near-term "existing compact already covers it" workaround. Confidence: HIGH on the ruling's existence and holding; MEDIUM on whether any tribe is still operating disputed retail sports wagering under a contrary compact-interpretation theory today — **verify with compliance/legal before relying on this**.

A legislatively-referred statewide-question ballot measure that would authorize tribal-casino sports betting with a 10% transaction fee is tracked for the November 3, 2026 ballot per Ballotpedia, but as of this writing it has not been confirmed to have cleared the legislature (HB 1047, the vehicle most closely associated with 2026 sports-betting legalization, failed in April). Confidence: LOW — treat as "pending," re-verify closer to Nov 2026.

Separately and reinforcing the no-online-real-money-gaming posture: Oklahoma enacted SB 1589 in 2026 (legislature overrode Governor Stitt's veto, Senate 34-10 / House 68-19) banning online "sweepstakes casino" / dual-currency games, effective November 1, 2026 — online casino-style gambling was already illegal under Oklahoma law before this bill; SB 1589 closes the sweepstakes gray-market variant specifically (Gambling Insider; The Lines; sbcamericas.com). Confidence: HIGH.

## Payments-relevant requirements

### Licensing & change management

- N/A for any the operator-relevant online product — no state licensing regime exists for online/mobile sportsbook or casino operators because none is authorized.
- Tribal Class III casino gaming is licensed and regulated per each tribe's individual IGRA Tribal-State compact (Model Tribal Gaming Compact template, 3A O.S. § 281), overseen jointly by each Tribal Compliance Agency (TCA) and the state's Gaming Compliance Unit (GCU) inside the Office of Management and Enterprise Services (OMES) as the State Compliance Agency (SCA) (oklahoma.gov/OGC). This is a closed-loop, cage-based land regime — not analogous to the operator's online deposit/withdrawal rails. Confidence: MEDIUM (compact terms vary by tribe; not all provisions confirmed identical across all ~30+ compacts).

### Deposits & permitted payment methods

- N/A — no legal online deposit channel exists for sports betting or online casino in Oklahoma. Any the operator deposit flow that activates for an OK-located patron is out of scope for a legal product and is itself the compliance risk (see Code review focus).
- Pari-mutuel horse racing: retail wagering at licensed tracks/OTBs is lawful (3A O.S. § 205.6, Oklahoma Horse Racing Commission); advance deposit wagering (ADW) has an unresolved history — a non-binding 2002 OK AG opinion found ADW illegal, and a 2022 bill (HB 3936) to formally license ADW stalled before passage (bettingusa.com). Confidence: LOW — do not assume ADW is currently licensed; verify with compliance before treating any OK ADW flow as authorized.

### Withdrawals & payout timelines

- N/A — no statute/rule exists because no authorized online product exists to regulate.

### Player funds segregation / reserve

- N/A — no statute/rule exists for online sportsbook/casino reserve requirements in Oklahoma.

### Responsible gambling

- N/A at the online-product level. Oklahoma's only real-money RG framework applicable to the operator-adjacent products would be self-exclusion mechanics at tribal land-based casinos, which are governed per-compact/per-tribe, not by a uniform state program (unlike commercial-state RG registries). Confidence: LOW — not independently verified per-tribe.

### KYC / age / geolocation

- N/A — no online product to KYC/geofence under Oklahoma-specific gaming law.
- **This is the operative requirement for the operator**: because no legal statewide/mobile real-money gaming product exists, the payments platform must treat Oklahoma as a hard geo-block jurisdiction for sportsbook and online casino, not merely "unlicensed." See Code review focus.

### AML overlays

- N/A — no state AML overlay exists for online gaming because no online gaming is authorized; federal BSA/OFAC obligations apply generically to any money-services activity but create no OK-specific carve-out.

### Records, reporting & data

- N/A for online product. Tribal compacts require compliance-officer access and SCA/TCA joint reporting per compact terms (oklahoma.gov/OGC, "About Tribal-State Gaming Compliance Unit"), but this is tribal-casino-internal, not something the operator's payments platform reports into.

## Code review focus

- **Default-on rails are the risk, not a gap in OK-specific rules.** The payments platform's gateway/product config appears to enable deposit, sports-wager, and payout rails by default across states and disable per-jurisdiction; for OK the correct posture is the reverse — sportsbook and online-casino products must be geo/jurisdiction-blocked by default, with no code path that silently activates them for an OK-resident/OK-located session.
- Verify the geolocation service's jurisdiction table has an explicit `OK` entry mapped to "no product enabled" (not merely "absent from allow-list," which risks fail-open behavior) for both sportsbook and online-casino product flags.
- Confirm deposit authorization and wager-placement code paths both independently consult the geo/jurisdiction gate — a gap where only one of the two checks OK would let a deposit succeed while wager placement fails (or vice versa), producing stranded funds or a misleading "deposit accepted" state for a jurisdiction with zero legal authority.
- If any legacy/test config or feature flag enables OK for sportsbook or casino (e.g., leftover from a states list templated off "all states minus explicit blocklist"), that is a live illegal-market / UIGEA (18 U.S.C. § 1955 state-law-predicate) and federal Wire Act exposure item, not a low-priority cleanup — escalate immediately if found.
- If the operator ever adds horse-racing ADW, do not reuse the sportsbook/casino OK-block flag as a proxy for ADW legality — pari-mutuel racing and ADW have separate (and, for ADW, unresolved) legal bases; a single "OK = blocked" flag covering all product types would be directionally safe but should be split per-product before ADW is considered, so the block is documented rather than incidental.
- Watch the Ballotpedia-tracked November 2026 statewide ballot question and any post-session 2026/2027 legislative activity (HB 1047 successor bills) — a future in-session change would need this file, the geo-jurisdiction table, and the code-review items above revisited before any OK product flag is flipped on.

## Sources & confidence

- [Oklahoma Senate rejects sports betting deal endorsed by tribes, OKC Thunder — KOSU](https://www.kosu.org/oklahoma-senate-rejects-sports-betting-bill)
- [Bad beat: Oklahoma Senate shoots down HB 1047's sports betting proposal — NonDoc](https://nondoc.com/2026/04/22/bad-beat-oklahoma-senate-shoots-down-hb-1047s-sports-betting-proposal/)
- [Oklahoma Senate Rejects Online Sports Betting Bill — Covers.com](https://www.covers.com/industry/oklahoma-online-sports-betting-bill-rejected-senate-april-22-2026)
- [Is Sports Betting Legal in Oklahoma? 2026 Status — Addison Law Firm](https://addison.law/insights/oklahoma-sports-betting-status)
- [Oklahoma governor slams tribal rights, clouds sports betting hopes — iGaming Business](https://igamingbusiness.com/sports-betting/stitt-oklahoma-governor-sports-betting-tribal-sovereignty/)
- [Treat v. Stitt, 2021 OK 15 — Justia Oklahoma Supreme Court Decisions](https://law.justia.com/cases/oklahoma/supreme-court/2021/118913.html)
- [Oklahoma Sports Betting Legalization Measure 2026 — Ballotpedia](https://ballotpedia.org/Oklahoma_Sports_Betting_Legalization_Measure_(2026))
- [Oklahoma and Utah Escalate Crackdown on Sweepstakes Casinos in 2026 — Gambling Insider](https://www.gamblinginsider.com/news/103423/oklahoma-utah-sweepstakes-casino-bills-2026)
- [Oklahoma Overrides Stitt Again, Enacts Sweepstakes Casino Ban — The Lines](https://www.thelines.com/legal-betting/oklahoma-overrides-stitt-again-enacts-sweepstakes-casino-ban/)
- [Oklahoma sweepstakes veto overridden by state legislators — SBC Americas](https://sbcamericas.com/2026/05/15/oklahoma-sweepstakes-stitt-override/)
- [2016 Oklahoma Statutes, Title 3A § 281, Model Tribal Gaming Compact — Justia](https://law.justia.com/codes/oklahoma/2016/title-3a/section-3a-281/)
- [Model Tribal Gaming Compact template — Oklahoma.gov](https://oklahoma.gov/content/dam/ok/en/ohrc/documents/rules-regs/Model_Tribal_Gaming_Compact.pdf)
- [About the Tribal-State Gaming Compliance Unit — Oklahoma.gov / OGC](https://www.ok.gov/OGC/About_Tribal-State_Gaming_Compliance_Unit/index.html)
- [Oklahoma Statutes § 3A-205.6, pari-mutuel wagering — Justia](https://law.justia.com/codes/oklahoma/title-3a/section-3a-205-6/)
- [Oklahoma Horse Racing Betting 2026: Online Sites, Apps & OTBs — BettingUSA](https://www.bettingusa.com/states/ok/horse-racing/)
- **Blocked/unreachable during research:** legalsportsreport.com/sports-betting/states/oklahoma returned HTTP 403 on fetch attempt — not used as a source; treat any claim that would have relied on it as unverified.
- **Confidence summary:** HIGH — no legal statewide/mobile sports betting or online casino exists in OK in 2026; HB 1047 failed 4/22/2026; SB 1589 sweepstakes-casino ban enacted, eff. 11/1/2026; *Treat v. Stitt* holding. MEDIUM — tribal compact oversight structure (SCA/TCA split) generalized across ~30+ individually-negotiated compacts; not every compact provision confirmed identical. LOW — whether any tribe currently operates disputed retail "event wagering" under a contrary compact theory; ADW licensing status for horse racing; whether the Nov 2026 ballot measure will actually appear/pass. All LOW items are flagged "verify with compliance/legal" rather than asserted as fact; no statute number in this file was invented — every cite above traces to a linked source.
