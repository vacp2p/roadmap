---

title: nim-libp2p logos-core
tags:
  - "2026q2"
  - "p2p"
  - "ift"
draft: false
description: Logos Core module for libp2p

---

`ift-ts:p2p:ift:2026q2-nimlibp2p-logos-core`

Extend the Logos Core libp2p module to consume the new nim-libp2p C bindings.

## Description
Extend the Logos Core module for libp2p using new functionality exposed
through the nim-libp2p C bindings.

## Task List

### Logos Core module - peerstore

* fully qualified name: `ift-ts:p2p:ift:2026q2-nimlibp2p-logos-core:peerstore`  
* owner: gabe
* status: done
* start-date: 2026/05/15
* end-date: 2026/05/19

#### Description
Using the C bindings exposed in
`ift-ts:p2p:ift:2026q2-nimlibp2p-cbindings:peerstore`, expose a set of
functions in the Logos Core module for managing the nim-libp2p peerstore.

#### Deliverables
- Logos Core wrappers for peerstore operations
- Tests or examples covering peerstore usage through Logos Core
- [logos-co/logos-libp2p-module#43](https://github.com/logos-co/logos-libp2p-module/pull/43) feat: add peerstore


### Logos Core module - capability discovery

* fully qualified name: `ift-ts:p2p:ift:2026q2-nimlibp2p-logos-core:capability-discovery`  
* owner: gabe
* status: done
* start-date: 2026/04/24
* end-date: 2026/04/28

#### Description
Using the C bindings exposed in
`ift-ts:p2p:ift:2026q2-nimlibp2p-cbindings:capability-discovery`, expose a
set of functions in the Logos Core module so capability discovery can be used
through Logos Core.

#### Deliverables
- [logos-co/logos-libp2p-module#63](https://github.com/logos-co/logos-libp2p-module/pull/63) feat(servicedisco): add discoLookup data to expected output
- [logos-co/logos-libp2p-module#60](https://github.com/logos-co/logos-libp2p-module/pull/60) fix(docs): document service_discovery example in examples README
- [logos-co/logos-libp2p-module#59](https://github.com/logos-co/logos-libp2p-module/pull/59) feat: multi-node bootstrap service discovery example
- [logos-co/logos-libp2p-module#40](https://github.com/logos-co/logos-libp2p-module/pull/40) - feat: add service discovery
- [vacp2p/nim-libp2p#2342](https://github.com/vacp2p/nim-libp2p/pull/2342) chore(service-disco): add ipSimCoefficient
- [vacp2p/nim-libp2p#2338](https://github.com/vacp2p/nim-libp2p/pull/2338) chore(cbind): add service disco headers


### Logos Core module - Custom Protocols

* fully qualified name: `ift-ts:p2p:ift:2026q2-nimlibp2p-logos-core:custom-protocols`  
* owner: gabe
* status: done
* start-date: 2026/05/19
* end-date: 2026/05/26

#### Description
Using a set of new functions provided by Logos Core, allow registering custom protocols.
Once a stream is received, these functions should be used to notify other modules that
data might be available on a stream to write/read.

#### Deliverables
- [logos-co/logos-libp2p-module#68](https://github.com/logos-co/logos-libp2p-module/pull/68) feat: decode XPR
- [logos-co/logos-libp2p-module#62](https://github.com/logos-co/logos-libp2p-module/pull/62) feat: user-provided XPRs
- [logos-co/logos-libp2p-module#65](https://github.com/logos-co/logos-libp2p-module/pull/65) chore: dedup the sync-over-async bridge, split plugin.h, surface init failure
- [logos-co/logos-libp2p-module#66](https://github.com/logos-co/logos-libp2p-module/pull/66) fix(tsan): guard emitEvent against the worker-thread data race
- [logos-co/logos-libp2p-module#67](https://github.com/logos-co/logos-libp2p-module/pull/67) test: split tests into fast (unit) and integration, cover timeout/queue gaps
- New functions in logos core that would allow registering custom protocols
- Tests or examples covering custom protocol handling
- [logos-co/logos-libp2p-module#45](https://github.com/logos-co/logos-libp2p-module/pull/45) feat: custom protocol registration
