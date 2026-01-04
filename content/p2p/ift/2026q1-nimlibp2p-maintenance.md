---

title: Nim-libp2p maintenance
tags:
  - "2026q1"
  - "p2p"
  - "ift"
draft: false
description: Maintain nim-libp2p through improvements, bug fixes, and user support

---

`ift-ts:p2p:ift:2026q1-nimlibp2p-maintenance`

Maintain nim-libp2p through improvements, bug fixes, and user support

## Description

Continue supporting and maintaining the nim-libp2p repository through ongoing improvements, refactoring, and bug fixes.
This includes a range of ad-hoc tasks critical to sustaining code quality, overall stability, correct functionality,
and performance of the project.
Additionally, it provides a platform for addressing small developer requests,
ensuring that nim-libp2p remains functional and usable for its primary users — Nimbus and Waku — helping to meet their evolving needs."

## Task List

### Maintenance

* fully qualified name: `ift-ts:p2p:ift:2026q1-nimlibp2p-maintenance:maintenance`
* owner: rramos
* status: not started
* start-date: 2026/01/01
* end-date: 2026/03/31

#### Description
Maintain [nim-libp2p](https://github.com/vacp2p/nim-libp2p) repository via improvements, refactors and bug fixes.

#### Deliverables
- [[Deliverable] Maintenance 2026q1]

### Kademlia Interop tests

* fully qualified name: `ift-ts:p2p:ift:2026q1-nimlibp2p-maintenance:kademlia-interop-tests`
* owner: rramos
* status: not started
* start-date: 2026/01/01
* end-date: 2026/03/31

#### Description
Integrate libp2p test plans' Kad-DHT interop tests as part of the CI tests executed on each PR.
This task will depend whether these tests are available during Q1 or not

#### Deliverables
- New github workflow: `Interoperability Tests / Run Kad-dht interoperability tests`
