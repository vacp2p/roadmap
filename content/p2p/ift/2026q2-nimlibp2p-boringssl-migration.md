---

title: nim-libp2p BoringSSL migration
tags:
  - "2026q2"
  - "p2p"
  - "ift"
draft: false
description: Replace BearSSL usage in nim-libp2p with BoringSSL-backed TLS, cryptography, and RNG paths

---

`ift-ts:p2p:ift:2026q2-nimlibp2p-boringssl-migration`

Replace BearSSL usage in nim-libp2p with BoringSSL-backed TLS,
cryptography, and RNG paths.

## Description

nim-libp2p currently depends on both BearSSL and BoringSSL. BearSSL is no
longer actively maintained by its author, while BoringSSL is already required
for QUIC support. This commitment reduces duplicated crypto dependencies by
making nim-libp2p and relevant dependencies, including nim-websocket, agnostic
with respect to the selected TLS backend, then migrating BearSSL-specific
cryptography and RNG usage toward BoringSSL-backed implementations.

The migration should preserve existing secure transport behavior while
allowing downstream users to select the backend explicitly during the transition.
BearSSL support can remain available behind the backend abstraction until all
call sites have been moved or downstream consumers no longer require it.

## Task List

### TLS Backend Abstraction

* fully qualified name: `ift-ts:p2p:ift:2026q2-nimlibp2p-boringssl-migration:tls-backend-abstraction`
* owner: richard
* status: in progress (40%)
* start-date: 2026/05/03
* end-date: 2026/06/30

#### Description

Make nim-libp2p and nim-websocket independent of a concrete TLS backend. Move
BearSSL-specific transport code behind a small backend selection layer and add
the wiring needed to use BoringSSL where QUIC already requires it.

#### Deliverables

- TLS backend selection API or configuration for nim-libp2p users
- nim-websocket changes needed to avoid hard-coding BearSSL
- BoringSSL-backed TLS path available through the shared abstraction
- Compatibility tests covering existing secure websocket and TLS behavior
- Updated dependency documentation describing backend selection and defaults

### Cryptography and RNG Migration

* fully qualified name: `ift-ts:p2p:ift:2026q2-nimlibp2p-boringssl-migration:crypto-rng-migration`
* owner: richard
* status: not started
* start-date: 2026/05/01
* end-date: 2026/06/30

#### Description

Audit direct BearSSL cryptography and RNG usage in nim-libp2p and replace the
first set of call sites with BoringSSL-backed helpers. Prioritize call sites
that are on maintained transports, test utilities, or shared security paths so
the default dependency graph can move away from BearSSL incrementally.

#### Deliverables

- Inventory of BearSSL cryptography and RNG call sites in nim-libp2p
- BoringSSL-backed helper APIs for migrated cryptography and RNG operations
- Initial set of BearSSL crypto/RNG call sites migrated to BoringSSL-backed helpers
- Tests proving migrated paths produce compatible behavior
- Follow-up cleanup plan for remaining BearSSL usage
