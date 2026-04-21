---

title: Anoncomms Consulting
tags:
  - "2026q2"
  - "p2p"
  - "ift"
draft: false
description: P2P ad-hoc consulting for Anoncomms

---

`ift-ts:p2p:ift:2026q2-anoncomms-consulting`

P2P ad-hoc consulting for Anoncomms

## Description

P2P provides consulting and support to Anoncomms by answering implementation
questions, refining strategies for using nim-libp2p effectively, and removing
blockers related to capability discovery.
Additionally, P2P provides guidance on coding challenges that arise during
implementation.

## Task List

### Capability Discovery

* fully qualified name: `ift-ts:p2p:ift:2026q2-anoncomms-consulting:capability-discovery`
* owner: gabe
* status: in progress (85%)
* start-date: 2026/04/01
* end-date: 2026/04/17

#### Description
Implement capability discovery within nim-libp2p.
The following resources exist:
- specification: https://lip.logos.co/ift-ts/raw/logos-capability-discovery.html
- PoC implementation: [feat(kad): capability discovery](https://github.com/vacp2p/nim-libp2p/pull/2055)

#### Deliverables
- [vacp2p/nim-libp2p#2245](https://github.com/vacp2p/nim-libp2p/pull/2245) chore(crypto): add pick utilities
- [vacp2p/nim-libp2p#2237](https://github.com/vacp2p/nim-libp2p/pull/2237) chore(service-disco): add protobuf messages and utilities
- [vacp2p/nim-libp2p#2275](https://github.com/vacp2p/nim-libp2p/pull/2275) feat(service-disco): add registrar
- [vacp2p/nim-libp2p#2302](https://github.com/vacp2p/nim-libp2p/pull/2302) fix(service-disco): add missing tables import
- [vacp2p/nim-libp2p#2290](https://github.com/vacp2p/nim-libp2p/pull/2290) chore(service-disco): use ServiceId type
- [vacp2p/nim-libp2p#2274](https://github.com/vacp2p/nim-libp2p/pull/2274) feat(service-disco): routing table manager
- [vacp2p/nim-libp2p#2267](https://github.com/vacp2p/nim-libp2p/pull/2267) feat(service-disco): add ipTree, signatures
- [vacp2p/nim-libp2p#2246](https://github.com/vacp2p/nim-libp2p/pull/2246) chore(service-disco): add service discovery
- Capability discovery support implemented in nim-libp2p
- Integration guidance for Anoncomms based on the specification and PoC
