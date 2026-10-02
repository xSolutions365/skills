# Prohibited-state / ineligible-jurisdiction geofencing & exclusion

**Lane:** GEOFENCE · **Authority:** UIGEA (31 USC 5361-5367); Federal Wire Act (18 USC 1084); state prohibitions; per-product eligibility · **Researched:** Aug 2026

For any jurisdiction the operator cannot legally serve (no framework, or not-yet-live, or wrong product for that state), the ONLY compliance obligation is to **block** — correctly, fail-closed, server-side. This lane captures the exclusion controls that a full per-state lane would otherwise repeat 26×. It is where the "geo fail-open" concern lives.

## Key requirements

- **Block money movement outside eligible jurisdictions (UIGEA/Wire Act):** the eligibility decision must happen BEFORE payment acceptance; wagering-related transactions must be intrastate/eligible. Transactions from outside eligible jurisdictions, over VPN/proxy, or where the user cannot be located must be blocked and enforced server-side.
- **Fail-CLOSED on geo error:** a geolocation service error/timeout/unenumerated result must **block**, not allow (deny-by-default). Allow-listing only a few error codes is fail-open.
- **Per-product eligibility:** a state may permit OSB but not iGaming (or DFS but not OSB). Eligibility must be evaluated per product, not per state uniformly.
- **Prohibited-state travel handling:** balances funded by methods banned in a state (credit-card, gift-card) must be non-wagerable while the user is in that state; no deposits/withdrawals in an ineligible state.
- **Correct jurisdiction attribution:** attribute transactions to the correct jurisdiction (avoid hardcoded defaults when location/jurisdiction data is missing); capture the actual transaction location.
- **Proxy/VPN/spoof detection → block/suspend**, not soft-log (CT 12-865-3(q)).

## Code review focus

- **Fail-open vs fail-closed geo** on deposit AND withdrawal: does a geo error/timeout/null/unenumerated result block or proceed? A common anti-pattern is a geo helper that returns null on exception while the controller blocks only a few enumerated codes (fail-open). Grep `geolocation`, `geoError`, `proxyScore`, and any missing-geo sentinel.
- **VPN/proxy** signal read and enforced (not just captured).
- **Jurisdiction attribution** correctness — watch for a resolver that falls back to a hardcoded default jurisdiction when a real code is present but unread (an inverted branch).
- **Per-product** eligibility branch (OSB/iGaming/DFS) in gating.
- **Prohibited-state balance** handling (non-wagerable funds on travel).

## Test coverage focus

- **Unit** tests asserting geo **fail-closed**: a geo-service exception / null / unenumerated code → deposit AND withdrawal blocked. (The single highest-value all-state test.)
- Proxy/VPN high-score → block/suspend asserted.
- Jurisdiction resolver returns the real state, not a hardcoded default, when a code exists.
- Per-product eligibility (DFS-legal / OSB-prohibited same state) asserted.
- These are pure-logic → all belong in unit tests, not integration/e2e.

## Sources & confidence

- UIGEA 31 USC 5361-5367; Wire Act 18 USC 1084; state prohibition statutes; the codebase's own geo path and any internal geo-eligibility design docs.
- Confidence: HIGH — geo fail-open is a commonly found gap; this lane makes these controls first-class + test-driven. Not legal advice on the live-jurisdiction map — confirm the eligible state × product matrix with compliance.
