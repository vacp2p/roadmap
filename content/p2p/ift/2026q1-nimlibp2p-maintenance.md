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
* status: in progress (36%)
* start-date: 2026/01/01
* end-date: 2026/03/31

#### Description
Maintain [nim-libp2p](https://github.com/vacp2p/nim-libp2p) repository via improvements, refactors and bug fixes.

#### Deliverables
- [vacp2p/nim-libp2p#2059](https://github.com/vacp2p/nim-libp2p/pull/2059) chore: bump lsquic
- [status-im/nimbus-eth2#7898](https://github.com/status-im/nimbus-eth2/pull/7898) fix: lsquic nasm file compilation
- [vacp2p/nim-lsquic#61](https://github.com/vacp2p/nim-lsquic/pull/61) chore: use static to compile windows assembly
- [vacp2p/nim-libp2p#2057](https://github.com/vacp2p/nim-libp2p/pull/2057) chore: set build env for windows to match nimbus
- [vacp2p/nim-lsquic#60](https://github.com/vacp2p/nim-lsquic/pull/60) fix: use pthread instead of winpthread
- [status-im/nimbus-eth2#7892](https://github.com/status-im/nimbus-eth2/pull/7892) fix: lsquic XXH_HEADER_NAME on windows+clang
- [vacp2p/nim-lsquic#59](https://github.com/vacp2p/nim-lsquic/pull/59) chore: set build env for windows to match nimbus
- [status-im/nimbus-eth2#7890](https://github.com/status-im/nimbus-eth2/pull/7890) chore: add winpthread
- [vacp2p/nim-lsquic#33](https://github.com/vacp2p/nim-lsquic/pull/33) fix: use brackets
- [vacp2p/mix#91](https://github.com/vacp2p/mix/pull/91) chore: licenses
- [vacp2p/nim-lsquic#57](https://github.com/vacp2p/nim-lsquic/pull/57) chore: add codeowners file
- [vacp2p/nim-lsquic#56](https://github.com/vacp2p/nim-lsquic/pull/56) chore: update license header
- [vacp2p/nim-libp2p#2047](https://github.com/vacp2p/nim-libp2p/pull/2047) chore(ci): update license header
- [vacp2p/nim-libp2p#2046](https://github.com/vacp2p/nim-libp2p/pull/2046) feat: v1.15.1
- [vacp2p/nim-libp2p#2045](https://github.com/vacp2p/nim-libp2p/pull/2045) chore: bump lsquic
- [vacp2p/nim-lsquic#55](https://github.com/vacp2p/nim-lsquic/pull/55) fix: use localpassc and compile specific flags
- [vacp2p/nim-lsquic#54](https://github.com/vacp2p/nim-lsquic/pull/54) fix: raise DialError when connection fails to be established
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
