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
* status: done
* start-date: 2026/01/01
* end-date: 2026/03/31

#### Description
Maintain [nim-libp2p](https://github.com/vacp2p/nim-libp2p) repository via improvements, refactors and bug fixes.

#### Deliverables
- [vacp2p/nim-libp2p#2232](https://github.com/vacp2p/nim-libp2p/pull/2232) fix(autonat): cleanup duplicated services on tests
- [vacp2p/nim-libp2p#2191](https://github.com/vacp2p/nim-libp2p/pull/2191) chore: add `with*` constructors to messages
- [vacp2p/nim-lsquic#76](https://github.com/vacp2p/nim-lsquic/pull/76) chore: README
- [vacp2p/nim-lsquic#75](https://github.com/vacp2p/nim-lsquic/pull/75) feat: tests
- [vacp2p/nim-lsquic#70](https://github.com/vacp2p/nim-lsquic/pull/70) feat: use `sendmmsg` in linux, and increase parameter values while still remaining conservative
- Ran nimbus-eth2 in kurtosis to demonstrate that QUIC integration worked.
- [vacp2p/nim-libp2p#2183](https://github.com/vacp2p/nim-libp2p/pull/2183) test(gossipsub): improve test "mesh is rebalanced during heartbeat - opportunistic grafting"
- [vacp2p/nim-libp2p#2174](https://github.com/vacp2p/nim-libp2p/pull/2174) chore: update readme packages
- [vacp2p/nim-libp2p#2168](https://github.com/vacp2p/nim-libp2p/pull/2168) chore(ai): add more instructions
- [vacp2p/nim-libp2p#2133](https://github.com/vacp2p/nim-libp2p/pull/2133) chore: add msys+gcc build target for windows
- [status-im/nim-eth#849](https://github.com/status-im/nim-eth/pull/849) fix: enrQuicPort
- [vacp2p/nim-lsquic#71](https://github.com/vacp2p/nim-lsquic/pull/71) fix: make sure ip6 addrs are used when dest is ipv6
- [vacp2p/nim-lsquic#69](https://github.com/vacp2p/nim-lsquic/pull/69) fix: various
- [vacp2p/nim-lsquic#68](https://github.com/vacp2p/nim-lsquic/pull/68) fix: call stream.doProcess after writing immediatly succesfully
- [status-im/nimbus-eth2#8064](https://github.com/status-im/nimbus-eth2/pull/8064) chore: use newer docker base images
- [vacp2p/nim-libp2p#2151](https://github.com/vacp2p/nim-libp2p/pull/2151) chore(ai): add .github/copilot-instructions.md for coding agent onboarding
- [vacp2p/nim-libp2p#2153](https://github.com/vacp2p/nim-libp2p/pull/2153) feat(ai): add suggestions from style guide
- [vacp2p/nim-libp2p#2160](https://github.com/vacp2p/nim-libp2p/pull/2160) chore: avoid using deprecated callbacks
- [vacp2p/nim-libp2p#2162](https://github.com/vacp2p/nim-libp2p/pull/2162) refactor: use results lib instead of options
- [vacp2p/nim-libp2p#2159](https://github.com/vacp2p/nim-libp2p/pull/2159) chore: utilize newFutureCompleted
- [vacp2p/nim-libp2p#2161](https://github.com/vacp2p/nim-libp2p/pull/2161) chore: fix deprecated warning for Future.cancel()
- [vacp2p/nim-libp2p#2158](https://github.com/vacp2p/nim-libp2p/pull/2158) chore: avoid using deprecated type ByteAddress
- [vacp2p/nim-libp2p#2155](https://github.com/vacp2p/nim-libp2p/pull/2155) chore: fix hints XDeclaredButNotUsed
- [vacp2p/nim-libp2p#2157](https://github.com/vacp2p/nim-libp2p/pull/2157) chore: fix hint XCannotRaiseY
- [vacp2p/nim-libp2p#2154](https://github.com/vacp2p/nim-libp2p/pull/2154) test: use rng instead of newRng
- [vacp2p/nim-libp2p#2150](https://github.com/vacp2p/nim-libp2p/pull/2150) test: hardening and cosmetics
- [vacp2p/nim-libp2p#2125](https://github.com/vacp2p/nim-libp2p/pull/2125) chore: bump lsquic
- [litespeedtech/lsquic#620](https://github.com/litespeedtech/lsquic/pull/620) fix: inconsistent capitalization fo ws2tcpip.h
- [vacp2p/nim-lsquic#65](https://github.com/vacp2p/nim-lsquic/pull/65) chore: make lpthread optional if using windows with clang
- [vacp2p/nim-lsquic#66](https://github.com/vacp2p/nim-lsquic/pull/66) fix: inconsistent capitalization of ws2tcpip.h in lsquic
- [vacp2p/nim-lsquic#63](https://github.com/vacp2p/nim-lsquic/pull/63) fix: stream creation when connections are nil
- [vacp2p/nim-libp2p#2116](https://github.com/vacp2p/nim-libp2p/pull/2116) fix: memory leak and stream removal
- [vacp2p/nim-libp2p#2109](https://github.com/vacp2p/nim-libp2p/pull/2109) refactor(conn): wait for peer-ready before handling streams
- [vacp2p/nim-lsquic#62](https://github.com/vacp2p/nim-lsquic/pull/62) fix: workaround for os module using wrong path separator when cross compiling
- Fixed issues related to QUIC
- [vacp2p/nim-libp2p#2108](https://github.com/vacp2p/nim-libp2p/pull/2108) chore(mix): reuse utilities for generating node infoextension
- [vacp2p/nim-libp2p#2106](https://github.com/vacp2p/nim-libp2p/pull/2106) fix: make storeMuxer async and not use asyncSpawn to trigger the connection events
- [vacp2p/nim-libp2p#2096](https://github.com/vacp2p/nim-libp2p/pull/2096) chore(pubsub): add topicLabel
- [status-im/nimbus-eth2#7916](https://github.com/status-im/nimbus-eth2/pull/7916) chore: bump nim-libp2p to 1.15.2
- [status-im/nimbus-eth2#7906](https://github.com/status-im/nimbus-eth2/pull/7906) fix: OPENSSL_free warning
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
- [vacp2p/nim-libp2p#2215](https://github.com/vacp2p/nim-libp2p/pull/2215) fix(autonatv2): reachability greater than expected
- [vacp2p/nim-libp2p#2204](https://github.com/vacp2p/nim-libp2p/pull/2204) fix(kad): get providers aggregates race

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
