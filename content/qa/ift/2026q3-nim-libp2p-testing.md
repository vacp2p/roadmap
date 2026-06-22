---
title: Nim Libp2p Testing
tags:
  - "2026q3"
  - "qa"
  - "ift"
draft: false
description: Expand nim-libp2p testing coverage with focus on new protocols and stability improvements.
---

`ift-ts:qa:ift:2026q3-nim-libp2p-testing`

## Description
Continue expanding nim-libp2p testing coverage, documentation, and tooling with focus on feature work and stability improvements carried from Q2.
Support libp2p work where QA help is expected, including Autotls, gossipsub queue behavior, opt-in dial ranking and backoffs, peerstore TTL handling, QUIC-related validation, dual-stack IPv4/IPv6 coverage, and maintenance work.

## Task List

### Autotls Protocol Testing

* fully qualified name: `ift-ts:qa:ift:2026q3-nim-libp2p-testing:autotls`
* owner: radek
* status: not started
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Implement unit and integration tests for the Autotls protocol.

#### Deliverables
- PRs with links to added tests

### Gossipsub Queue Work Testing

* fully qualified name: `ift-ts:qa:ift:2026q3-nim-libp2p-testing:gossipsub-queue`
* owner: radek
* status: not started
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Implement or extend tests for the gossipsub queue work.
Cover explicit outbound queue priorities and limits, disconnect-on-full behavior for protocol-critical traffic, drop-on-full behavior for best-effort traffic, and validation of queue behavior under slow-peer and burst scenarios.

#### Deliverables
- PRs with tests covering queue priorities and limits
- Tests for priority-message overflow and queue refresh behavior
- Tests for best-effort dropping under queue pressure
- Issues / reports for interop risks, instability, or uncovered edge cases

### Peerstore TTL Testing

* fully qualified name: `ift-ts:qa:ift:2026q3-nim-libp2p-testing:peerstore-ttl`
* owner: radek
* status: not started
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Implement tests for peerstore TTL handling, including expiration behavior, refresh semantics, and correctness of peer data retention and cleanup.

#### Deliverables
- PRs with peerstore TTL tests
- Issues / reports for behavioral gaps or flaky scenarios

### Opt-in Dial Ranking and Backoffs Testing

* fully qualified name: `ift-ts:qa:ift:2026q3-nim-libp2p-testing:opt-in-dial-ranking-and-backoffs`
* owner: radek
* status: not started
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Implement tests for opt-in dial ranking and backoff behavior.

#### Deliverables
- PRs with dial ranking and backoff tests
- Issues / reports for uncovered edge cases or regressions

### QUIC Repository Testing

* fully qualified name: `ift-ts:qa:ift:2026q3-nim-libp2p-testing:quic-repo`
* owner: radek
* status: not started
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Add QA coverage in the QUIC repository where it would be most useful for the broader libp2p effort.
Focus on targeted tests that can catch transport-level issues earlier and complement the nim-libp2p coverage.

#### Deliverables
- PRs with tests added or improved in the QUIC repository
- Issues / reports for uncovered transport bugs, edge cases, or missing scenarios

### Dual-Stack IPv4 and IPv6 Testing

* fully qualified name: `ift-ts:qa:ift:2026q3-nim-libp2p-testing:dual-stack-ipv4-ipv6`
* owner: radek
* status: not started
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Implement tests for dual-stack IPv4 and IPv6 behavior on the libp2p side.
Cover scenarios that can catch UDP and address-family issues, especially around mixed IPv4/IPv6 environments and regressions that should be detected by unit or integration tests.

#### Deliverables
- PRs with dual-stack IPv4 and IPv6 tests
- Issues / reports for regressions or uncovered gaps in mixed-stack behavior

### Maintenance

* fully qualified name: `ift-ts:qa:ift:2026q3-nim-libp2p-testing:maintenance`
* owner: radek
* status: not started
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Provide ongoing QA maintenance support for nim-libp2p throughout Q3.
Cover small regression fixes, flaky-test follow-ups, test updates needed by upstream code changes, and issue-driven validation work that does not fit a larger feature-specific task.

#### Deliverables
- PRs / Issues / Reports
