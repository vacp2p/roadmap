---
title: AMM Core Improvements
tags:
  - "2026q1"
  - "sc"
  - "logos"
draft: false
description: Research and implement core improvements to the LEZ AMM program addressing pool security, swap safety, and token handling.
---

`ift-ts:sc:logos:2026q1-amm-core-improvements`

## Description

Research and implement core improvements to the LEZ AMM (Automated Market Maker) program.
The AMM currently has several known vulnerabilities and missing features that must be resolved before it can be considered production-ready.

This commitment focuses on foundational fixes and research-driven improvements.

Several items require research first to determine the exact impact and whether implementation is necessary, before proceeding with implementation.

## Task List

### Research dead shares and first-depositor attack impact

* fully qualified name: `ift-ts:sc:logos:2026q1-amm-core-improvements:research-dead-shares`
* owner: Ricardo
* status: in progress (5%)
* start-date: 2026/03/01
* end-date: 2026/03/31

#### Description

Research whether dead shares are needed for the AMM, what the exact impact is of not having them, and how they prevent pool draining via a new LP setting the price ratio.
Currently, pools can be purposefully drained because a new LP sets a new price ratio (which should not happen).
Produce a findings document with a clear recommendation on whether and how to implement protection.

#### Deliverables

- [logos-blockchain/lssa#344](https://github.com/logos-blockchain/lssa/issues/344)
- [ ] Research document outlining first-depositor attack vectors and impact
- [ ] Recommendation on implementation approach

### Implement dead shares / first-depositor protection

* fully qualified name: `ift-ts:sc:logos:2026q1-amm-core-improvements:implement-dead-shares`
* owner: TBD
* status: not started
* start-date: 2026/03/01
* end-date: 2026/03/31

#### Description

Based on research findings, implement dead shares or an alternative protection mechanism against pool draining and new LP price ratio manipulation.
This addresses the vulnerability where pools can be purposefully drained because a new LP sets a new price ratio.

#### Deliverables

- [ ] Implementation of first-depositor protection mechanism
- [ ] Test coverage for attack vectors
- [ ] PRs with code reviews


### Research post-swap k invariant check necessity

* fully qualified name: `ift-ts:sc:logos:2026q1-amm-core-improvements:research-post-swap-k-check`
* owner: TBD
* status: not started
* start-date: 2026/03/01
* end-date: 2026/03/31

#### Description

Research whether a post-swap k invariant check is needed for the AMM, what the impact of not having it is, and document findings with a clear recommendation.
The constant product invariant (k = x * y) should be maintained after every swap to ensure no value is leaked from the pool.

#### Deliverables

- [ ] Research document outlining risks of missing post-swap k check
- [ ] Analysis of attack vectors enabled by missing invariant check
- [ ] Recommendation on implementation approach

### Implement post-swap k invariant check

* fully qualified name: `ift-ts:sc:logos:2026q1-amm-core-improvements:implement-post-swap-k-check`
* owner: TBD
* status: not started
* start-date: 2026/03/01
* end-date: 2026/03/31

#### Description

Based on research findings, implement a post-swap k invariant check if deemed necessary.
This ensures the constant product invariant is maintained after every swap operation.

#### Deliverables

- [ ] Implementation of post-swap k invariant check
- [ ] PRs with code reviews


### Research recovery of directly transferred pool tokens

* fully qualified name: `ift-ts:sc:logos:2026q1-amm-core-improvements:research-token-recovery`
* owner: Ricardo
* status: in progress (5%)
* start-date: 2026/03/01
* end-date: 2026/03/31

#### Description

Research whether and how directly transferred pool tokens can be recovered, what the impact of not handling this is, and document findings with a recommendation.
Currently, tokens sent directly to the pool (outside the AMM program interface) are unrecoverable and effectively lost.

#### Deliverables

- [logos-blockchain/lssa#342](https://github.com/logos-blockchain/lssa/issues/342)
- [ ] Research document outlining the impact of unrecoverable tokens
- [ ] Recommendation on implementation approach

### Implement token recovery mechanism

* fully qualified name: `ift-ts:sc:logos:2026q1-amm-core-improvements:implement-token-recovery`
* owner: TBD
* status: not started
* start-date: 2026/03/01
* end-date: 2026/03/31

#### Description

Based on research findings, implement a recovery mechanism for directly transferred pool tokens if deemed necessary.
This addresses the issue where tokens sent directly to the pool contract are currently unrecoverable.

#### Deliverables

- [ ] Implementation of token recovery mechanism
- [ ] Test coverage for recovery scenarios
- [ ] PRs with code reviews

### Fix initial LP calculation to include tokenB amount

* fully qualified name: `ift-ts:sc:logos:2026q1-amm-core-improvements:fix-initial-lp-calc`
* owner: Andrea
* status: in progress (5%)
* start-date: 2026/03/01
* end-date: 2026/03/31

#### Description

Fix the initial LP calculation which currently ignores the tokenB amount.
The initial liquidity provision should properly account for both token amounts to ensure correct LP token minting balance.

#### Deliverables

- [ ] Fix initial LP calculation to consider both tokenA and tokenB amounts
- [ ] Test coverage for initial LP scenarios
- [ ] PRs with code reviews

### Implement liquidity lock mechanism

* fully qualified name: `ift-ts:sc:logos:2026q1-amm-core-improvements:liquidity-lock`
* owner: TBD
* status: not started
* start-date: 2026/03/01
* end-date: 2026/03/31

#### Description

Implement a liquidity lock mechanism to prevent immediate withdrawal of provided liquidity.
This protects the pool from flash loan-style attacks and ensures a minimum commitment from liquidity providers.
Research and determine the appropriate lock duration and conditions for unlocking liquidity.

#### Deliverables

- [ ] Implementation of liquidity lock mechanism
- [ ] Test coverage for lock/unlock scenarios
- [ ] PRs with code reviews

### Add pool enumeration and discoverability

* fully qualified name: `ift-ts:sc:logos:2026q1-amm-core-improvements:pool-discoverability`
* owner: TBD
* status: not started
* start-date: 2026/04/01
* end-date: 2026/04/30

#### Description

Address the lack of pool discoverability in the PDA-based architecture.
Currently there is no way to enumerate existing pools, and PDAs are not discoverable unless ownership is queried.
Figure out if discoverability is desired.
Implement a mechanism to enumerate and discover existing pools while maintaining the PDA architecture.

#### Deliverables

- [ ] Implementation of pool enumeration mechanism
- [ ] Test coverage for discoverability scenarios
- [ ] PRs with code reviews
