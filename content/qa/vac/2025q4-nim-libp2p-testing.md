---
title: Nim Libp2p Testing
tags:
  - "2025q4"
  - "qa"
  - "vac"  
draft: false  
description: Expand nim-libp2p testing coverage with focus on new protocols, test plans, and stability improvements. 

---

`vac:qa:vac:2025q4-nim-libp2p-testing`

## Description
Expand nim-libp2p testing coverage, documentation, and tooling with focus on new features under development.  
Create test plans for AutonatV2, Quic, Mix, and Kademlia.  
Improve stability by addressing flaky tests and extend coverage for Identify/Push and Connectivity protocols.

## Task List

### Test Plans for New Features

* fully qualified name: `vac:qa:vac:2025q4-nim-libp2p-testing:test-plans`
* owner: radek
* status: in progress (30%)
* start-date: 2025/10/01
* end-date: 2025/10/20

#### Description
Develop test plans for features currently under development:  
- AutonatV2  
- Quic  
- Mix  
- Kademlia  

#### Deliverables
- [QUIC test plan](https://www.notion.so/QUIC-28b8f96fb65c8018b6cdc21882cfd98a)

---

### Flaky Test Fixes

* fully qualified name: `vac:qa:vac:2025q4-nim-libp2p-testing:flaky-tests`
* owner: radek
* status: in progress (99%)
* start-date: 2025/10/20
* end-date: 2025/10/31

#### Description
Identify, investigate, and fix flaky tests in nim-libp2p to improve test reliability and CI stability.

#### Deliverables
* [test: only failed test in report](https://github.com/vacp2p/nim-libp2p/pull/1932)
* [test(switch): improve flaky test](https://github.com/vacp2p/nim-libp2p/pull/1928)
* [test: dynamic imports](https://github.com/vacp2p/nim-libp2p/pull/1918)
* [test(coverage): ignore tests](https://github.com/vacp2p/nim-libp2p/pull/1922)
* [test: fix logs](https://github.com/vacp2p/nim-libp2p/pull/1920)
* [Check `chronicles` exports](https://github.com/vacp2p/nim-libp2p/issues/1941)
* [Find solution for `chronicles` in `kademlia` tests workaround](https://github.com/vacp2p/nim-libp2p/issues/1940)
* [test: report](https://github.com/vacp2p/nim-libp2p/pull/1912)
* [test: Organise test files - Multiformat and Services](https://github.com/vacp2p/nim-libp2p/pull/1909)
* [test: Organise test files - final rename](https://github.com/vacp2p/nim-libp2p/pull/1914)
* [test: reorganise libp2p tests](https://github.com/vacp2p/nim-libp2p/pull/1911)
* [test(autotls): Organise test files](https://github.com/vacp2p/nim-libp2p/pull/1905)
* [test(mix): improve flaky test](https://github.com/vacp2p/nim-libp2p/pull/1896)
* [test(transports): Generate cert for WSS](https://github.com/vacp2p/nim-libp2p/pull/1894)

---

### Identify/Push Protocol Testing

* fully qualified name: `vac:qa:vac:2025q4-nim-libp2p-testing:identify-push`
* owner: radek
* status: not started
* start-date: 2025/11/01
* end-date: 2025/11/15

#### Description
Implement unit and integration tests for the Identify/Push protocol,  
covering peer identification, metadata exchange, push updates, and error handling.

#### Deliverables
* PRs with links to added tests

---

### Connectivity Protocol Testing

* fully qualified name: `vac:qa:vac:2025q4-nim-libp2p-testing:connectivity`
* owner: radek
* status: not started
* start-date: 2025/11/15
* end-date: 2025/12/01

#### Description
Implement tests for the Connectivity protocol to validate connection management,  
connection limits, peer lifecycle handling, and resilience under different network conditions.

#### Deliverables
* PRs with links to added tests

---

### GossipSub Performance Testing Enhacements

* fully qualified name: `vac:qa:vac:2025q4-nim-libp2p-testing:gossipsub-performance`
* owner: radek
* status: done
* start-date: 2025/10/01
* end-date: 2025/10/15

#### Description: 
Update GossipSub performance tests based on dev feedback and existing data gathered so far.

#### Deliverables:
- [test(performance): Add QUIC scenario](https://github.com/vacp2p/nim-libp2p/pull/1631)
- [test(performance): chart generation refactor](https://github.com/vacp2p/nim-libp2p/pull/1718)
- [test(performance): Refactor runner](https://github.com/vacp2p/nim-libp2p/pull/1735)
- [test(performance): reliability workflow](https://github.com/vacp2p/nim-libp2p/pull/1729)

---

### QUIC Protocol Testing

* fully qualified name: `vac:qa:vac:2025q4-nim-libp2p-testing:quic`
* owner: radek
* status: in progress (70%)
* start-date: 2025/10/16
* end-date: 2025/11/25

#### Description
Improve QUIC transport test coverage for handshake enforcement (TLS, ALPN, transport parameters), 
stream and connection lifecycle, resilience/error paths, metrics, and interoperability.

#### Deliverables
- [test(performance): use p95 instead of max](https://github.com/vacp2p/nim-libp2p/pull/1883)
- [test(quic): Misc tests](https://github.com/vacp2p/nim-libp2p/pull/1879)
- [test: add more parallel streams test](https://github.com/vacp2p/nim-libp2p/pull/1861)
- [Tor transport: Server with multiple connections processes data sequentially in the tests](https://github.com/vacp2p/nim-libp2p/issues/1859)
- [test(transports): add parallel stream tests](https://github.com/vacp2p/nim-libp2p/pull/1838)
- [chore: use test_all in coverage workflow](https://github.com/vacp2p/nim-libp2p/pull/1855)
- [test(transports): stream tests](https://github.com/vacp2p/nim-libp2p/pull/1829)
- [test: too many global vars workaround](https://github.com/vacp2p/nim-libp2p/pull/1816)
- [Transports: Inconsistent EOF behavior between QUIC and Mplex: first readOnce after EOF](https://github.com/vacp2p/nim-libp2p/issues/1833)
- [Transports: Inconsistent EOF behavior between QUIC and Mplex: consecutive readOnce after EOF](https://github.com/vacp2p/nim-libp2p/issues/1834)
- [fix(quic): GossipSub outbound peers](https://github.com/vacp2p/nim-libp2p/pull/1768)
- [test(quic): Add tests 1](https://github.com/vacp2p/nim-libp2p/pull/1772)
- [test: organise transports tests](https://github.com/vacp2p/nim-libp2p/pull/1776)
- [test(quic): Add Multiaddress Handling tests](https://github.com/vacp2p/nim-libp2p/pull/1784)
- [test: Refactor common transports tests](https://github.com/vacp2p/nim-libp2p/pull/1786)
- [Transports tests: Inconsistent behaviour for writes when EOF](https://github.com/vacp2p/nim-libp2p/issues/1788)
