---

title: Nim-libp2p maintenance
tags:
  - "2026q2"
  - "p2p"
  - "ift"
draft: false
description: Maintain nim-libp2p through improvements, bug fixes, and user support

---

`ift-ts:p2p:ift:2026q2-nimlibp2p-maintenance`

Maintain nim-libp2p through improvements, bug fixes, and user support

## Description

Continue supporting and maintaining the nim-libp2p repository through ongoing improvements, refactoring, and bug fixes.
This includes a range of ad-hoc tasks critical to sustaining code quality, overall stability, correct functionality,
and performance of the project.
Additionally, it provides a platform for addressing small developer requests,
ensuring that nim-libp2p remains functional and usable for its primary users, Nimbus and Waku, as their needs evolve.

## Task List

### Maintenance

* fully qualified name: `ift-ts:p2p:ift:2026q2-nimlibp2p-maintenance:maintenance`
* owner: rramos
* status: not started
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description
Maintain the [nim-libp2p](https://github.com/vacp2p/nim-libp2p) repository via improvements, refactors, and bug fixes.

#### Deliverables
List of maintenance-related PRs


### Peerstore Address TTL

* fully qualified name: `ift-ts:p2p:ift:2026q2-nimlibp2p-maintenance:peerstore-address-ttl`
* owner: not assigned yet
* status: not started
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description
Add TTL support for addresses stored in the peerstore. Addresses should no
longer be stored indefinitely by default. Instead, use different TTLs
depending on how trustworthy the address is: 
- use shorter TTLs for unverified addresses, like those coming from
  discovery mechanism or from identify (unless it's the address used in 
  the active connection), 
- longer TTLs for addresses that have been confirmed as valid or 
   successfully connected to, 
- infinite TTL when explicitly requested.

#### Deliverables
- Peerstore support for address TTLs
- Different TTL policies for unverified, validated, connected, and permanent addresses
- Expiration logic to remove stale addresses automatically


### IdentifyPush

* fully qualified name: `ift-ts:p2p:ift:2026q2-nimlibp2p-maintenance:identify-push`
* owner: not assigned yet
* status: not started
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description
Enable the IdentifyPush protocol so connected peers receive protocol and
address updates when local capabilities change. Maintain a set of connected
peers that advertise the IdentifyPush protocol. After running Identify on a
peer, if its protocol list includes the IdentifyPush codec, store its peer ID
in that set. If the peer disconnects or later re-identifies without that
protocol, remove it. Whenever our multiaddresses change or new protocols are
mounted, send IdentifyPush updates to every peer in the set.

#### Deliverables
IdentifyPush protocol is mounted and used


### Quic Multiaddress Support

* fully qualified name: `ift-ts:p2p:ift:2026q2-nimlibp2p-maintenance:quic-maddrs`
* owner: not assigned yet
* status: not started
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description
Add support for multiple QUIC v1 multiaddresses in the QUIC transport.

#### Deliverables
Switch can listen on multiple QUIC v1 addresses


### Kademlia Interop tests

* fully qualified name: `ift-ts:p2p:ift:2026q2-nimlibp2p-maintenance:kademlia-interop-tests`
* owner: not assigned yet
* status: not started
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description
Integrate libp2p test plans' Kad-DHT interop tests as part of the CI tests executed on each PR.
If these tests are available during Q2, integrate them into CI. Otherwise,
prepare the CI integration work and defer execution until the tests are
available. This task was originally planned for 2026q1, but the Kademlia
interop tests were not available.

#### Deliverables
- New github workflow: `Interoperability Tests / Run Kad-dht interoperability tests`

### ORC in CI

* fully qualified name: `ift-ts:p2p:ift:2026q2-nimlibp2p-maintenance:orc-ci`
* owner: not assigned yet
* status: not started
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description
Nimbus is evaluating ORC. Some previous work has already been done in this regard in
- https://github.com/vacp2p/nim-libp2p/issues/2077
- https://github.com/vacp2p/nim-libp2p/pull/2148
Nim 2.2.8 cannot be used with ORC at the moment, but the fix has already been
applied to the Nim branch that will become 2.2.10. Once Nim 2.2.10 is
available, test this version and memory model to ensure nim-libp2p works with
ORC. If Nim 2.2.10 is not released during Q2, prepare the CI changes and defer
execution to the next quarter.

#### Deliverables
nim-libp2p CI jobs work with both `--mm:refc` and `--mm:orc`


### Exception Review

* fully qualified name: `ift-ts:p2p:ift:2026q2-nimlibp2p-maintenance:exception-review`
* owner: not assigned yet
* status: not started
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description
Review the exceptions currently being traced in nim-libp2p and related
flows, especially where excessive tracing adds noise. Reduce unnecessary tracing so logs provide better signal.

#### Deliverables
- Review of the most frequent traced exceptions and affected code paths
- Changes to reduce noisy or redundant exception traces


### WSS handler socket leak

* fully qualified name: `ift-ts:p2p:ift:2026q2-nimlibp2p-maintenance:wss-socket-leak`
* owner: not assigned yet
* status: not started
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description
Review how to complete [logos-delivery#3634](https://github.com/logos-messaging/logos-delivery/issues/3634),
validate the proposed solutions already documented in the related PRs and discussions,
and decide whether nim-libp2p should take ownership of part of the fix. This
should also assess whether Chronos accept concurrency work is required as part
of the solution.
Some related work available is:
- https://github.com/status-im/nim-websock/pull/181
- https://github.com/vacp2p/nim-libp2p/pull/1937

#### Deliverables
- Agreed technical direction for `logos-delivery#3634`
- Ownership decision between nim-libp2p and the relevant dependent components
- Follow-up issue or PR breakdown, including Chronos work if needed
