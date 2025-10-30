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

**Alignment with VAC Narratives:**
* Nim-libp2p is a key component of the VAC ecosystem,  
  and improving its testing coverage and tooling strengthens our internal expertise  
  and the overall reliability of the network.  
* By enhancing these tests, and creating test plans,  
  we support the RFC culture by providing feedback to the specifications,  
  ensuring they align with real-world implementation.  
* These efforts also contribute to scaling the project's capacity,  
  as better testing tools empower the open-source community to participate effectively.  

## Task List

### Test Plans for New Features

* fully qualified name: `vac:qa:vac:2025q4-nim-libp2p-testing:test-plans`
* owner: radek
* status: in progress (20%)
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
* status: not started
* start-date: 2025/10/20
* end-date: 2025/10/31

#### Description
Identify, investigate, and fix flaky tests in nim-libp2p to improve test reliability and CI stability.

#### Deliverables
* PRs with links to fixes

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
* status: in progress (25%)
* start-date: 2025/10/16
* end-date: 2025/11/25

#### Description
Improve QUIC transport test coverage for handshake enforcement (TLS, ALPN, transport parameters), 
stream and connection lifecycle, resilience/error paths, metrics, and interoperability.

#### Deliverables
- [fix(quic): GossipSub outbound peers](https://github.com/vacp2p/nim-libp2p/pull/1768)
- [test(quic): Add tests 1](https://github.com/vacp2p/nim-libp2p/pull/1772)
- [test: organise transports tests](https://github.com/vacp2p/nim-libp2p/pull/1776)
- [test(quic): Add Multiaddress Handling tests](https://github.com/vacp2p/nim-libp2p/pull/1784)
- [test: Refactor common transports tests](https://github.com/vacp2p/nim-libp2p/pull/1786)
- [Transports tests: Inconsistent behaviour for writes when EOF](https://github.com/vacp2p/nim-libp2p/issues/1788)