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
* status: in progress (21%)
* start-date: 2026/01/01
* end-date: 2026/03/31

#### Description
Maintain [nim-libp2p](https://github.com/vacp2p/nim-libp2p) repository via improvements, refactors and bug fixes.

#### Deliverables
- [[Deliverable] Maintenance 2026q1]
- [vacp2p/nim-libp2p#2035](https://github.com/vacp2p/nim-libp2p/pull/2035) test: improving flakines for floodPublish with bandwidthEstimatebps
- [vacp2p/nim-libp2p#2020](https://github.com/vacp2p/nim-libp2p/pull/2020) fix(kad-dht): stop condition on find_node and track whether node responded succesfully or not
- [vacp2p/nim-libp2p#2019](https://github.com/vacp2p/nim-libp2p/pull/2019) feat: v1.15.0
- [status-im/nim-eth#846](https://github.com/status-im/nim-eth/pull/846) fix(nat): use shared mem to send port mapping and description to thread
- [vacp2p/nim-lsquic#53](https://github.com/vacp2p/nim-lsquic/pull/53) feat(win): keep asm list in a separate file that is used both in the makefile and .nimble
- [vacp2p/nim-libp2p#2007](https://github.com/vacp2p/nim-libp2p/pull/2007) chore(ConnManager): avoid exposing impl details

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
