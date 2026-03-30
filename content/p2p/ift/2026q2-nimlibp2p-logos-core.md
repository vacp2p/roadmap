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
* status: not started
* start-date: 2026/05/15
* end-date: 2026/05/19

#### Description
Using the C bindings exposed in
`ift-ts:p2p:ift:2026q2-nimlibp2p-cbindings:peerstore`, expose a set of
functions in the Logos Core module for managing the nim-libp2p peerstore.

#### Deliverables
- Logos Core wrappers for peerstore operations
- Tests or examples covering peerstore usage through Logos Core


### Logos Core module - capability discovery

* fully qualified name: `ift-ts:p2p:ift:2026q2-nimlibp2p-logos-core:capability-discovery`  
* owner: gabe
* status: not started
* start-date: 2026/04/24
* end-date: 2026/05/01

#### Description
Using the C bindings exposed in
`ift-ts:p2p:ift:2026q2-nimlibp2p-cbindings:capability-discovery`, expose a
set of functions in the Logos Core module so capability discovery can be used
through Logos Core.

#### Deliverables
- Logos Core wrappers for capability discovery
- Tests or examples covering capability discovery through Logos Core


### Logos Core module - Custom Protocols

* fully qualified name: `ift-ts:p2p:ift:2026q2-nimlibp2p-logos-core:custom-protocols`  
* owner: gabe
* status: not started
* start-date: 2026/06/19
* end-date: 2026/06/30

#### Description
Using a set of new functions provided by Logos Core, allow registering custom protocols.
Once a stream is received, these functions should be used to notify other modules that
data might be available on a stream to write/read.

#### Deliverables
- New functions in logos core that would allow registering custom protocols
- Tests or examples covering custom protocol handling
