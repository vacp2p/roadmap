---

title: nim-libp2p Dial Ranking And Backoffs
tags:
  - "2026q3"
  - "p2p"
  - "ift"
draft: false
description: Add opt-in dial ranking, dial racing, and backoff behavior

---

`ift-ts:p2p:ift:2026q3-nimlibp2p-dial-ranking-backoffs`

Add opt-in dial ranking and backoff behavior so nim-libp2p applications can
improve connection setup latency when peers have multiple candidate addresses.

## Description

Dialing currently tries candidate addresses and transports sequentially until
one succeeds. This is simple and predictable, but it can make connection setup
slower when the first few candidates are poor or unreachable.

This commitment introduces an opt-in policy for ranking and racing dial
attempts. The feature must stay opt-in because it changes dialing semantics and
some applications may prefer the current deterministic behavior.

## Task List

### Dial Racing And Cancellation

* fully qualified name: `ift-ts:p2p:ift:2026q3-nimlibp2p-dial-ranking-backoffs:dial-racing`
* owner: not assigned yet
* status: not started
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Design and implementthe opt-in dial ranking policy, including address grouping, 
transport preference, parallelism limits, cancellation behavior, and compatibility
with existing dial APIs.

The implementation should prefer direct addresses over relay addresses where 
appropriate, prefer QUIC over TCP when both are available and configured, and cancel
outstanding attempts once a connection succeeds.

#### Deliverables
- Opt-in ranked dial path
- Optional parallel dialing for selected candidate groups
- Successful dial cancels outstanding attempts
- Tests for direct, relay, QUIC, TCP, and mixed candidate behavior


### Failed Address Backoffs

* fully qualified name: `ift-ts:p2p:ift:2026q3-nimlibp2p-dial-ranking-backoffs:backoffs`
* owner: not assigned yet
* status: not started
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Track failed addresses and peers so repeated dial failures can back off instead
of repeatedly trying the same bad candidates. Backoff state should reset when a
dial succeeds.

#### Deliverables
- Failed-address cache or equivalent backoff state
- Per-peer backoff after repeated failures or total dial timeout
- Exponential or configurable backoff policy
- Backoff reset after successful dial
- Metrics or logs for ranked dial decisions and backoff behavior
