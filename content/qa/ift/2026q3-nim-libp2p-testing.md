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
Support libp2p work where QA help is expected, including Autotls, opt-in dial ranking and backoffs, QUIC-related validation, dual-stack IPv4/IPv6 coverage, and maintenance work.

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
* owner: Radek
* status: in progress (80%)
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Implement tests for dual-stack IPv4 and IPv6 behavior on the libp2p side.
Cover scenarios that can catch UDP and address-family issues, especially around mixed IPv4/IPv6 environments and regressions that should be detected by unit or integration tests.

#### Deliverables
- PRs with dual-stack IPv4 and IPv6 tests
- Issues / reports for regressions or uncovered gaps in mixed-stack behavior
- [vacp2p/nim-libp2p#2698](https://github.com/vacp2p/nim-libp2p/pull/2698) test(transports): dual stack 1
- [vacp2p/nim-libp2p#2704](https://github.com/vacp2p/nim-libp2p/pull/2704) test(transports): dual stack 2
- [vacp2p/nim-libp2p#2712](https://github.com/vacp2p/nim-libp2p/pull/2712) test(ipaddr): dual stack 3
- [vacp2p/nim-libp2p#2733](https://github.com/vacp2p/nim-libp2p/pull/2733) test(autonat): dual stack 4
- [vacp2p/nim-libp2p#2703](https://github.com/vacp2p/nim-libp2p/issues/2703) transports: tcp port reuse binds the wrong address family on dual-stack nodes
- [vacp2p/nim-libp2p#2710](https://github.com/vacp2p/nim-libp2p/issues/2710) ipaddr: isPrivate classifies every IPv6 address as public, so autonat canDial dials private IPv6 targets
- [vacp2p/nim-libp2p#2711](https://github.com/vacp2p/nim-libp2p/issues/2711) ipaddr: hasPublicIPAddress only accepts IPv4, so IPv6-only public hosts fail autotls setup
- [vacp2p/nim-libp2p#2731](https://github.com/vacp2p/nim-libp2p/issues/2731) ipaddr: ipAddrMatches only compares the ip4 component, so autonat v2 never skips amplification attack prevention for IPv6 clients

### Maintenance

* fully qualified name: `ift-ts:qa:ift:2026q3-nim-libp2p-testing:maintenance`
* owner: radek
* status: in progress (20%)
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Provide ongoing QA maintenance support for nim-libp2p throughout Q3.
Cover small regression fixes, flaky-test follow-ups, test updates needed by upstream code changes, and issue-driven validation work that does not fit a larger feature-specific task.

#### Deliverables
- [vacp2p/nim-libp2p#2725](https://github.com/vacp2p/nim-libp2p/pull/2725) test(transports): improve hanging test
- [vacp2p/nim-libp2p#2714](https://github.com/vacp2p/nim-libp2p/pull/2714) test(transports): multiple addresses
- [vacp2p/nim-libp2p#2713](https://github.com/vacp2p/nim-libp2p/issues/2713) transports: inconsistency when stopping pending accept

