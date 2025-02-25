---

title: Nim-libp2p maintenance
tags:
  - "2025q1"
  - "p2p"
  - "ift"
draft: false
description: Maintain nim-libp2p through improvements, bug fixes, and user support

---

`vac:p2p:ift:2025q1-nimlibp2p-maintenance`

Maintain nim-libp2p through improvements, bug fixes, and user support

## Description

Continue supporting and maintaining the nim-libp2p repository through ongoing improvements, refactoring, and bug fixes.
This includes a range of ad-hoc tasks critical to sustaining code quality, overall stability, correct functionality,
and performance of the project.
Additionally, it provides a platform for addressing small developer requests,
ensuring that nim-libp2p remains functional and usable for its primary users — Nimbus and Waku — helping to meet their evolving needs."

## Task List

### Maintenance

* fully qualified name: `vac:p2p:ift:2025q1-nimlibp2p-maintenance:maintenance`
* owner: rramos
* status: ongoing
* start-date: 2025/01/13
* end-date: 2025/03/31

#### Description
Maintain [nim-libp2p](https://github.com/vacp2p/nim-libp2p) repository via improvements, refactors and bug fixes.

#### Deliverables
- [[Deliverable] Maintenance 2025Q1](https://github.com/vacp2p/nim-libp2p/issues/1239)


### Async exception tracking

* fully qualified name: `vac:p2p:ift:2025q1-nimlibp2p-maintenance:async-exceptions`
* owner: vlado
* status: 73%
* start-date: 2025/02/10
* end-date: 2025/02/27

#### Description
Specify exceptions being raised in `{.async.}` functions. See [nimlibp2p#962](https://github.com/vacp2p/nim-libp2p/issues/962)

#### Deliverables
- PR:
  - chore(dialer): list raised exceptions [PR#1264](https://github.com/vacp2p/nim-libp2p/pull/1264)
  - chore(connmanager): specify raised exceptions [PR#1263](https://github.com/vacp2p/nim-libp2p/pull/1263)
  - chore(protocol): list raised exceptions [PR#1260](https://github.com/vacp2p/nim-libp2p/pull/1260)
  - chore(transports): list raised exceptions [PR#1255](https://github.com/vacp2p/nim-libp2p/pull/1255)
  - chore: list raised exceptions in utils module [PR#1252](https://github.com/vacp2p/nim-libp2p/pull/1252)
  - chore: list raised exceptions in switch services [PR#1251](https://github.com/vacp2p/nim-libp2p/pull/1251)
  - chore: specify raising exceptions in daemon module [PR#1249](https://github.com/vacp2p/nim-libp2p/pull/1249)


### nim-protobuf-serialization

* fully qualified name: `vac:p2p:ift:2025q1-nimlibp2p-maintenance:nim-protobuf-serialization`
* owner:
* status:
* start-date: 
* end-date:

#### Description
Determine maturity level of [nim-libp2p-protobuf](https://github.com/status-im/nim-protobuf-serialization) and consider replacing
minprotobuf usage within nim-libp2p with this library. In case we decide to go with this change, it will need a security audit
afterwards. See [nim-libp2p#841](https://github.com/vacp2p/nim-libp2p/issues/841)

#### Deliverables
- PR:
