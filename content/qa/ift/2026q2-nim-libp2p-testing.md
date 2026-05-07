---
title: Nim Libp2p Testing
tags:
  - "2026q2"
  - "qa"
  - "ift"
draft: false
description: Expand nim-libp2p testing coverage with focus on new protocols, test plans, and stability improvements.
---

`ift-ts:qa:ift:2026q2-nim-libp2p-testing`

## Description
Expand nim-libp2p testing coverage, documentation, and tooling with focus on new features under development.
Continue the remaining protocol coverage and interop planning work carried over from Q1.
Support additional Q2 libp2p work where QA help is expected, including service discovery, gossipsub queue behavior, connection management, peerstore TTL handling, QUIC-related validation, dual-stack IPv4/IPv6 coverage, and interop validation where useful.

## Task List

### Test Plans

* fully qualified name: `ift-ts:qa:ift:2026q2-nim-libp2p-testing:test-plans`
* owner: radek
* status: not started
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description
Develop test plans for features currently under development:
- Autotls

#### Deliverables
- Test plan docs

### Autotls Protocol Testing

* fully qualified name: `ift-ts:qa:ift:2026q2-nim-libp2p-testing:autotls`
* owner: radek
* status: not started
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description
Implement unit and integration tests for the Autotls protocol.

#### Deliverables
- PRs with links to added tests

### Gossipsub Queue Work Testing

* fully qualified name: `ift-ts:qa:ift:2026q2-nim-libp2p-testing:gossipsub-queue`
* owner: radek
* status: not started
* start-date: 2026/04/06
* end-date: 2026/04/24

#### Description
Implement or extend tests for the Q2 gossipsub queue work.
Cover explicit outbound queue priorities and limits, disconnect-on-full behavior for protocol-critical traffic, drop-on-full behavior for best-effort traffic, and validation of queue behavior under slow-peer and burst scenarios.

#### Deliverables
- PRs with tests covering queue priorities and limits
- Tests for priority-message overflow and queue refresh behavior
- Tests for best-effort dropping under queue pressure
- Issues / reports for interop risks, instability, or uncovered edge cases

### Connection Management Testing

* fully qualified name: `ift-ts:qa:ift:2026q2-nim-libp2p-testing:connection-management`
* owner: radek
* status: not started
* start-date: 2026/04/27
* end-date: 2026/05/15

#### Description
Implement tests for the Q2 connection management work.
Cover hi/lo watermarks, score-driven pruning, decaying and static tags, protected peers, and pruning behavior under realistic connection churn.

#### Deliverables
- PRs with tests for hi/lo limits and pruning triggers
- Tests for connection scoring, tag decay, and protected-peer handling
- Tests for automatic pruning and peer selection behavior
- Issues / reports for uncovered edge cases or regressions

### Peerstore TTL Testing

* fully qualified name: `ift-ts:qa:ift:2026q2-nim-libp2p-testing:peerstore-ttl`
* owner: radek
* status: not started
* start-date: 2026/05/18
* end-date: 2026/06/05

#### Description
Implement tests for peerstore TTL handling, including expiration behavior, refresh semantics, and correctness of peer data retention and cleanup.

#### Deliverables
- PRs with peerstore TTL tests
- Issues / reports for behavioral gaps or flaky scenarios

### QUIC Repository Testing

* fully qualified name: `ift-ts:qa:ift:2026q2-nim-libp2p-testing:quic-repo`
* owner: radek
* status: not started
* start-date: 2026/06/08
* end-date: 2026/06/19

#### Description
Add QA coverage in the QUIC repository where it would be most useful for the broader libp2p effort.
Focus on targeted tests that can catch transport-level issues earlier and complement the nim-libp2p coverage.

#### Deliverables
- PRs with tests added or improved in the QUIC repository
- Issues / reports for uncovered transport bugs, edge cases, or missing scenarios

### Dual-Stack IPv4 and IPv6 Testing

* fully qualified name: `ift-ts:qa:ift:2026q2-nim-libp2p-testing:dual-stack-ipv4-ipv6`
* owner: radek
* status: not started
* start-date: 2026/06/15
* end-date: 2026/06/26

#### Description
Implement tests for dual-stack IPv4 and IPv6 behavior on the libp2p side.
Cover scenarios that can catch UDP and address-family issues, especially around mixed IPv4/IPv6 environments and regressions that should be detected by unit or integration tests.

#### Deliverables
- PRs with dual-stack IPv4 and IPv6 tests
- Issues / reports for regressions or uncovered gaps in mixed-stack behavior

### Interop Test Plans

* fully qualified name: `ift-ts:qa:ift:2026q2-nim-libp2p-testing:interop-test-plans`
* owner: radek
* status: in progress (95%)
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description
Integrate [libp2p test plans](https://github.com/libp2p/test-plans) and run them against nim-libp2p.
Revisit Kademlia interop coverage as part of this work if the upstream `libp2p/test-plans` work is ready within the quarter.
If time permits, improve the existing partial messages interop test with additional logic, since functional coverage for partial messages and extensions is already considered complete.

#### Deliverables
- [vacp2p/nim-libp2p#2313](https://github.com/vacp2p/nim-libp2p/pull/2313) test(interop): GossipSub - fixes (part 3)
- [vacp2p/nim-libp2p#2310](https://github.com/vacp2p/nim-libp2p/pull/2310) test(gossipsub): partial messages with fanout bug + fix
- [vacp2p/nim-libp2p#2240](https://github.com/vacp2p/nim-libp2p/pull/2240) test(interop): GossipSub - core instructions (part 1)
- [vacp2p/nim-libp2p#2239](https://github.com/vacp2p/nim-libp2p/pull/2239) feat: create Ed25519 key from seed
- [vacp2p/nim-libp2p#2195](https://github.com/vacp2p/nim-libp2p/pull/2195) test(multiaddress): getField protobuf tests
- [vacp2p/nim-libp2p#2189](https://github.com/vacp2p/nim-libp2p/pull/2189) test(interop): update hp script
- [vacp2p/nim-libp2p#2249](https://github.com/vacp2p/nim-libp2p/pull/2249) test(interop): GossipSub - partial messages (part 2)
- [vacp2p/nim-libp2p#2288](https://github.com/vacp2p/nim-libp2p/pull/2288) test(gossipsub): extensions race condition + fix
- [vacp2p/nim-libp2p#2364](https://github.com/vacp2p/nim-libp2p/pull/2364) test(interop): perf
- [vacp2p/nim-libp2p#2333](https://github.com/vacp2p/nim-libp2p/pull/2333) test(interop): unified-testing helpers

### Maintenance

* fully qualified name: `ift-ts:qa:ift:2026q2-nim-libp2p-testing:maintenance`
* owner: radek
* status: in progress (10%)
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description
Provide ongoing QA maintenance support for nim-libp2p throughout Q2.
Cover small regression fixes, flaky-test follow-ups, test updates needed by upstream code changes, and issue-driven validation work that does not fit a larger feature-specific task.
This includes quick-turn support for transport-start inconsistencies, protocol-level regressions, and improvements to existing unit or integration coverage where new bugs are found.

#### Deliverables
- [vacp2p/nim-libp2p#2229](https://github.com/vacp2p/nim-libp2p/pull/2229) test(transport): inconsistent start behaviour
- [vacp2p/nim-libp2p#2230](https://github.com/vacp2p/nim-libp2p/issues/2230) transports: inconsistent start behaviour
- Validation notes for fixes landed outside the main feature-track tasks

### Service Discovery Testing

* fully qualified name: `ift-ts:qa:ift:2026q2-nim-libp2p-testing:service-discovery`
* owner: radek
* status: not started
* start-date: 2026/05/04
* end-date: 2026/06/30

#### Description
Implement unit and component tests for the [Logos Service Discovery protocol](https://lip.logos.co/ift-ts/raw/logos-service-discovery.html).
Cover the main advertise and discovery flows, including compatibility with Kad DHT behavior.
Include tests for advertiser, discoverer, and registrar behavior, service ID hashing, advertisement expiry, admission control, lookups, and closer peer responses.

#### Deliverables
- PRs with added tests
