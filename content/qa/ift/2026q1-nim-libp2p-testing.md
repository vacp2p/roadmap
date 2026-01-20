---
title: Nim Libp2p Testing
tags:
  - "2026q1"
  - "qa"
  - "ift"  
draft: false  
description: Expand nim-libp2p testing coverage with focus on new protocols, test plans, and stability improvements. 

---

`ift-ts:qa:ift:2026q1-nim-libp2p-testing`

## Description
Expand nim-libp2p testing coverage, documentation, and tooling with focus on new features under development.  
Create test plans for Kad DHT, Mix, Autotls and AutonatV2.  
Extend coverage for Mix, Kad DHT, Autotls, Identify/Push and Connectivity protocols.

## Task List

### Test Plans

* fully qualified name: `ift-ts:qa:ift:2026q1-nim-libp2p-testing:test-plans`
* owner: radek
* status: not started
* start-date: 2026/01/01
* end-date: 2026/03/31

#### Description
Develop test plans for features currently under development:  
- Mix  
- Kad DHT  
- Autotls

#### Deliverables
- Test plan docs

### Mix Protocol Testing

* fully qualified name: `ift-ts:qa:ift:2026q1-nim-libp2p-testing:mix`
* owner: radek
* status: not started
* start-date: 2026/01/01
* end-date: 2026/01/25

#### Description
Implement unit and integration tests for the Mix protocol.

#### Deliverables
* PRs with links to added tests

### Kad DHT Protocol Testing

* fully qualified name: `ift-ts:qa:ift:2026q1-nim-libp2p-testing:kad-dht`
* owner: radek
* status: in progress (45%)
* start-date: 2026/01/25
* end-date: 2026/02/15

#### Description
Implement unit and integration tests for the Kad DHT protocol.

#### Deliverables
* PRs with links to added tests
    * [vacp2p/nim-libp2p#2030](https://github.com/vacp2p/nim-libp2p/pull/2030) test(kad): put value 2 - new tests + small fix
    * [vacp2p/nim-libp2p#2029](https://github.com/vacp2p/nim-libp2p/pull/2029) test(kad): put value 1 - refactor
    * [vacp2p/nim-libp2p#2025](https://github.com/vacp2p/nim-libp2p/pull/2025) test(interop): Kad test template
    * [vacp2p/nim-libp2p#2023](https://github.com/vacp2p/nim-libp2p/pull/2023) test(kad): bootstrap and refactor find tests
    * [vacp2p/nim-libp2p#2022](https://github.com/vacp2p/nim-libp2p/pull/2022) fix(kad): Bootstrap
    * [vacp2p/nim-libp2p#2018](https://github.com/vacp2p/nim-libp2p/pull/2018) test(kad): find & lookup 2
    * [vacp2p/nim-libp2p#2014](https://github.com/vacp2p/nim-libp2p/pull/2014) test(kad): find & lookup
    * [vacp2p/nim-libp2p#1996](https://github.com/vacp2p/nim-libp2p/pull/1996) test(kad): Key conversion
    * [vacp2p/nim-libp2p#1998](https://github.com/vacp2p/nim-libp2p/pull/1998) test(kad): Routing table and refresh bucket
    * [vacp2p/nim-libp2p#2005](https://github.com/vacp2p/nim-libp2p/pull/2005) fix(kad): GetProviders test hanging forever
* Issues tracked
    * [vacp2p/nim-libp2p#2006](https://github.com/vacp2p/nim-libp2p/issues/2006) Kad: Lookup random PeerId for each non-empty bucket during bootstrap
    * [vacp2p/nim-libp2p#2003](https://github.com/vacp2p/nim-libp2p/issues/2003) flaky test(kad): Get providers

### Autotls Protocol Testing

* fully qualified name: `ift-ts:qa:ift:2026q1-nim-libp2p-testing:autotls`
* owner: radek
* status: not started
* start-date: 2026/02/15
* end-date: 2026/03/01

#### Description
Implement unit and integration tests for the Autotls protocol.

#### Deliverables
* PRs with links to added tests

### Identify/Push Protocol Testing

* fully qualified name: `ift-ts:qa:ift:2026q1-nim-libp2p-testing:identify-push`
* owner: radek
* status: not started
* start-date: 2026/03/01
* end-date: 2025/03/15

#### Description
Implement unit and integration tests for the Identify/Push protocol,  
covering peer identification, metadata exchange, push updates, and error handling.

#### Deliverables
* PRs with links to added tests

### Connectivity Protocol Testing

* fully qualified name: `ift-ts:qa:ift:2026q1-nim-libp2p-testing:connectivity`
* owner: radek
* status: not started
* start-date: 2026/03/15
* end-date: 2025/03/31

#### Description
Implement tests for the Connectivity protocol to validate connection management,  
connection limits, peer lifecycle handling, and resilience under different network conditions.

#### Deliverables
* PRs with links to added tests

### Interop Test Plans

* fully qualified name: `ift-ts:qa:ift:2026q1-nim-libp2p-testing:interop-test-plans`
* owner: radek
* status: in progress (5%)
* start-date: 2026/02/01
* end-date: 2026/02/28

#### Description
Integrate [libp2p test plans](https://github.com/libp2p/test-plans) and run into nim-libp2p

#### Deliverables
- [vacp2p/nim-libp2p#1993](https://github.com/vacp2p/nim-libp2p/pull/1993) test(interop): Autonatv2 test template
- [vacp2p/nim-libp2p#1994](https://github.com/vacp2p/nim-libp2p/pull/1994) docs: Improve Development section visibility
