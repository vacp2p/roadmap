---
title: nim-libp2p Address Manager
meta-description: Revamp the observed address manager into a unified address manager and add a pluggable reachability verifier.
---

# nim-libp2p Address Manager

`ift-ts:p2p:ift:2026q3-nimlibp2p-address-manager`

Revamp nim-libp2p's observed address manager into a unified address manager that owns the announce path, separate address discovery from reachability confirmation, and add a pluggable per-address reachability verifier backed by AutoNATv2.

## Description

nim-libp2p's `ObservedAddrManager` lives inside Identify as a flat list of observed IP/ports used only to guess one external NAT address, announce-address logic is spread across independent `AddressMapper`s registered by `NATService`, `AutoRelayService`, and `AutonatV2Service`, and `AutonatV2Service` collapses AutoNAT v2's per-address protocol into a single node-level reachability flag. With this commitment (1) the observed address manager is relocated out of Identify and revamped into the authoritative address manager that owns the announce path, (2) address discovery (always on) is separated from reachability confirmation (opt-in), and (3) confirmation becomes a pluggable per-address verifier. With no verifier registered the manager announces all candidates as `unknown`, so disabling AutoNATv2 degrades gracefully instead of breaking announcement. This follows go-libp2p's extraction of the observed address manager into its own package and its split of discovery from confirmation.

## Task List

### Decouple & Relocate ObservedAddrManager

- fully qualified name: `ift-ts:p2p:ift:2026q3-nimlibp2p-address-manager:obsaddr-decouple`
- owner: gabe
- status: planned
- start-date: 2026/07/01
- end-date: 2026/07/14

#### Description

Move `ObservedAddrManager` ownership out of Identify to a switch-level component, with Identify keeping a reference and feeding observations via `addObservation`. The observed-address mapper is also registered on the `PeerStore` (`addressMappers`), so relocation extracts it from there as well, not only from Identify. Behavior-preserving relocation, but the change in construction and teardown order is treated as a tracked deliverable rather than assumed free.

#### Deliverables

- `ObservedAddrManager` owned by the Switch; Identify holds a reference and feeds observations
- Observed-address mapper extracted from the `PeerStore` (`addressMappers`) as well as from Identify; the manager owns it post-relocation
- Manager start/stop sequenced relative to Identify and transports; clean cancellation on teardown with no dangling futures
- `withObservedAddrManager` builder hook deprecated as a warning shim (not removed) so downstream builds don't break mid-cycle; removal deferred to consumer migration
- Thresholds become switch-level config; direct `ObservedAddrManager.new(...)` retained for unit tests
- `guessDialableAddr` / `getMostObservedProtosAndPorts` behavior preserved
- Existing observed-addr tests pass unchanged, plus start/stop ordering and double-stop / stop-before-start tests

### Revamp into Address Manager

- fully qualified name: `ift-ts:p2p:ift:2026q3-nimlibp2p-address-manager:obsaddr-revamp`
- owner: gabe
- status: planned
- start-date: 2026/07/14
- end-date: 2026/08/04

#### Description

Restructure the relocated manager into the authoritative address manager. Replace the flat IP seq with a candidate model carrying source and reachability state, track a local-listen to observed-external mapping, accept candidates from NAT and circuit sources, and become the single owner of the announce path. Explicitly announced addresses currently bypass the mappers entirely and must be folded into the model; the wildcard address resolver is another mapping path that has to move under the manager; and `NATService` is not a simple feeder — on mapping refresh it can change or withdraw addresses, so candidate sources must be able to remove and update, not only add. Default reachability is `unknown` and all candidates are announced, reproducing today's output with no verifier present.

#### Deliverables

- Candidate model `(addr, source, state, lastChecked, ttl)`; `source` enum (`identifyObserved`, `upnp`, `natpmp`, `circuit`, `listen`, `announced`); `state` enum (`unknown`, `confirmed`, `unreachable`)
- Local-listen to observed-external mapping replacing the flat IP list
- Explicitly announced addresses (which today bypass the mappers) folded into the candidate model and the single announce path
- Wildcard address resolver brought under the manager's mapper rather than running as a separate mapping step
- Feeder entrypoints so `NATService` / `AutoRelayService` contribute candidates instead of registering their own mappers; the entrypoint supports add, update, and remove so `NATService` can withdraw or rewrite addresses on mapping refresh, with stale candidates expiring rather than lingering
- Address policy application (announce filters / allow-deny) owned by the manager, applied as the candidate set resolves to the announce set
- Single authoritative `AddressMapper` owned by the manager; per-source mappers migrated and removed in the same phase
- `confirmedAddrs()` query (reachable / unreachable / unknown, split by family); default = announce-all-as-unknown
- `PeerInfoObserver` fires on candidate-set change, debounced/coalesced so observed-addr flap and TTL churn don't trigger identify-push storms
- Tests: candidate dedup across sources, listen-to-observed mapping, wildcard resolution, announced-addr inclusion, `NATService` refresh that adds/removes/rewrites candidates, address-policy filtering, family split, push coalescing under flap

### Verifier Interface & AutoNATv2 Implementation

- fully qualified name: `ift-ts:p2p:ift:2026q3-nimlibp2p-address-manager:verifier`
- owner: gabe
- status: planned
- start-date: 2026/08/04
- end-date: 2026/08/25

#### Description

Add a `Verifier` interface the manager calls on a heartbeat to confirm individual candidates, plus an AutoNATv2-backed implementation. The verifier is optional: with none registered, candidates stay `unknown` and announcement is unaffected. Confirmation annotates state only and never drops addresses from announcement.

#### Deliverables

- `Verifier` abstraction (`verify(candidates)` returning per-addr results, cancellable); manager heartbeat via `utils/heartbeat` + cancellable `scheduleHandle`, cancellation wired to manager stop
- AutoNATv2 verifier: priority-ordered `sendDialRequest`, bucket by `DialStatus` (OK → confirmed, dial error → unreachable, timeout/ambiguous → stays unknown, never dropped), per-addr TTL re-confirmation, per family
- Backpressure: cap concurrent dial requests, skip candidates already in flight (no overlapping verify rounds)
- Graceful degrade: no verifier ⇒ all `unknown` ⇒ announce-all, asserted against phase-2 output
- Tests via autonatv2 `mockclient`/`mockserver`: confirm, dial-fail, ambiguous, re-confirm on expiry, candidate removed mid-round, no server response, verify cancelled at shutdown, no-verifier path

### Verifier Wiring & Consumer Migration

- fully qualified name: `ift-ts:p2p:ift:2026q3-nimlibp2p-address-manager:consumers`
- owner: gabe
- status: planned
- start-date: 2026/08/25
- end-date: 2026/09/08

#### Description

Register the AutoNATv2 verifier with the manager, derive a node-level reachability summary for back-compat, and migrate existing consumers off the old paths. The per-address state stays authoritative; the node-level summary is a read-only view computed from it, not stored truth.

#### Deliverables

- AutoNATv2 verifier registered with the manager; `AutonatV2Service` v1-style confidence `Deque` retired
- Derived node-level `NetworkReachability` summary (any confirmed ⇒ Reachable) computed from per-address state for back-compat
- `AutoRelayService` + `hpservice` read `confirmedAddrs()` where per-family detail matters, the summary only where a single flag suffices
- identify-push triggered on confirmed-addr change, reusing the phase-2 debounce
- `withObservedAddrManager` shim removed now that consumers are migrated; changelog entry + migration note
- Integration test: multi-source candidates (identify + upnp + circuit) → verify → announce, asserting only confirmed/unknown addrs announce with correct per-family state
