# Jurisdictions index

Per-jurisdiction requirement references for all 53 jurisdictions in scope: 50 US states + DC
plus **Ontario and Alberta, Canada**. `nj`/`pa`/`mi` are the deepest; the 27 added 2026-08-25
vary in depth — states with no legal real-money online gaming (e.g. `hi`/`ut`/`id`/`tx`/`ga`/`sc`)
carry a shorter `Status`-led default-deny file. Each file ends in a "Code review focus" list, was
researched Aug 2026, and carries its own confidence notes (the 2026-08-25 batch flags LOW/verify
wherever primary-source fetch was blocked). The default scope of a run is *every* file below; a
3-5 jurisdiction pilot of `nj`, `pa`, `mi` + one or two others is a sensible first run.

The directory is named for **jurisdictions**, not states, because Ontario and Alberta are
provinces — treating them as extra US states is the specific mistake this naming prevents.

## Federal baselines — pick by country, do not mix them

- [US federal baseline, FED-US](federal-baseline.md) — BSA/FinCEN CTRs and SARs, OFAC, PCI,
  card-network, engineering integrity. Output `fed.json`. Run whenever any US state is in scope.
- [Canadian federal baseline, FED-CA](canada-federal-baseline.md) — PCMLTFA/FINTRAC, Canadian
  sanctions, PIPEDA, RPAA, and a "US-control mapping traps" section. Output `fed_ca.json`. Run
  whenever any Canadian jurisdiction is in scope. **There is no BSA, no FinCEN CTR/SAR and no
  OFAC in Canada.** One FED-CA lane serves both provinces, but the provincial layers are not
  interchangeable — read `ab.md`'s "Ontario contrasts" before letting any finding cross the
  border.

## Terminology: FAST vs unit tests

The operator uses **FAST** (Functional Automation and Service Testing) as a programme name for
suites that exercise assembled services over the network — the opposite of the industry's "fast
= quick in-process unit test". Classify coverage as `unit_tested` (isolated, deterministic, no
network/DB/filesystem/clock), `integration_only`, `untested`, or `unknown`. Coverage that lives
only in a FAST suite is `integration_only` unless a specific test provably meets the isolation
bar. Write **FAST** in capitals only for the client's programme; never use bare "fast" as a
synonym for "unit". `build_matrix.py` still accepts the retired `fast_tested` value, normalising
it to `unit_tested`; don't emit it in new findings.

## US states + DC

- [Alaska — ak](jurisdictions/ak.md)
- [Alabama — al](jurisdictions/al.md)
- [Arkansas — ar](jurisdictions/ar.md)
- [Arizona — az](jurisdictions/az.md)
- [California — ca](jurisdictions/ca.md)
- [Colorado — co](jurisdictions/co.md)
- [Connecticut — ct](jurisdictions/ct.md)
- [District of Columbia — dc](jurisdictions/dc.md)
- [Delaware — de](jurisdictions/de.md)
- [Florida — fl](jurisdictions/fl.md)
- [Georgia — ga](jurisdictions/ga.md)
- [Hawaii — hi](jurisdictions/hi.md)
- [Iowa — ia](jurisdictions/ia.md)
- [Idaho — id](jurisdictions/id.md)
- [Illinois — il](jurisdictions/il.md)
- [Indiana — in](jurisdictions/in.md)
- [Kansas — ks](jurisdictions/ks.md)
- [Kentucky — ky](jurisdictions/ky.md)
- [Louisiana — la](jurisdictions/la.md)
- [Massachusetts — ma](jurisdictions/ma.md)
- [Maryland — md](jurisdictions/md.md)
- [Maine — me](jurisdictions/me.md)
- [Michigan — mi](jurisdictions/mi.md)
- [Minnesota — mn](jurisdictions/mn.md)
- [Missouri — mo](jurisdictions/mo.md)
- [Mississippi — ms](jurisdictions/ms.md)
- [Montana — mt](jurisdictions/mt.md)
- [North Carolina — nc](jurisdictions/nc.md)
- [North Dakota — nd](jurisdictions/nd.md)
- [Nebraska — ne](jurisdictions/ne.md)
- [New Hampshire — nh](jurisdictions/nh.md)
- [New Jersey — nj](jurisdictions/nj.md)
- [New Mexico — nm](jurisdictions/nm.md)
- [Nevada — nv](jurisdictions/nv.md)
- [New York — ny](jurisdictions/ny.md)
- [Ohio — oh](jurisdictions/oh.md)
- [Oklahoma — ok](jurisdictions/ok.md)
- [Oregon — or](jurisdictions/or.md)
- [Pennsylvania — pa](jurisdictions/pa.md)
- [Rhode Island — ri](jurisdictions/ri.md)
- [South Carolina — sc](jurisdictions/sc.md)
- [South Dakota — sd](jurisdictions/sd.md)
- [Tennessee — tn](jurisdictions/tn.md)
- [Texas — tx](jurisdictions/tx.md)
- [Utah — ut](jurisdictions/ut.md)
- [Virginia — va](jurisdictions/va.md)
- [Vermont — vt](jurisdictions/vt.md)
- [Washington — wa](jurisdictions/wa.md)
- [Wisconsin — wi](jurisdictions/wi.md)
- [West Virginia — wv](jurisdictions/wv.md)
- [Wyoming — wy](jurisdictions/wy.md)

## Canadian provinces

- [Ontario, Canada — on](jurisdictions/on.md)
- [Alberta, Canada — ab](jurisdictions/ab.md)
