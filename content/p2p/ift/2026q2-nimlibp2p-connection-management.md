---

title: nim-libp2p Connection Management
tags:
  - "2026q2"
  - "p2p"
  - "ift"
draft: false
description: Improved connection management in nim-libp2p

---

`ift-ts:p2p:ift:2026q2-nimlibp2p-connection-management`

Improve nim-libp2p’s connection manager to provide hi/lo watermarks, score-driven pruning, decaying tags, and protected connections. This task was moved from 2026q1

## Description

The current connection manager is limited to cap total connections but doesn’t maintain a healthy steady state, doesn’t distinguish valuable peers, and keeps stale or useless connections. With this commitment new behavior will be introduced by having the connection manager maintain connection counts within configurable low/high watermarks and prune excess connections based on peer scores. Its tagging and decay system will prioritize valuable peers while ensuring unused or low-value connections are gracefully trimmed.

## Task List

### Hi/Lo limits
* fully qualified name: `ift-ts:p2p:ift:2026q2-nimlibp2p-connection-management:limits`
* owner: vlado
* status: done
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description
Implement a hi/lo watermark subsystem. When connections exceed the higher limit, trigger a pruning cycle that continues until below the lower limit. Expose configuration options and allow switching between watermark mode and simple max-limit mode.

#### Deliverables
- [vacp2p/nim-libp2p#2325](https://github.com/vacp2p/nim-libp2p/pull/2325)
- [vacp2p/nim-libp2p#2344](https://github.com/vacp2p/nim-libp2p/pull/2344) fix(connmanager): max conns per peer limit
- [vacp2p/nim-libp2p#2363](https://github.com/vacp2p/nim-libp2p/pull/2363) refactor(connmanager): add limits config

### Connection score
* fully qualified name: `ift-ts:p2p:ift:2026q2-nimlibp2p-connection-management:score`
* owner: vlado
* status: done
* start-date: 2026/04/01
* end-date: 2026/04/28

#### Description
Implement a per-connection scoring system with static and ephemeral tags. Ephemeral tags decay linearly (or by chosen function) so its importance decreases over time. Allow marking connections as “protected” to exempt them from pruning. Outbound connections should naturally have a higher score than incoming connections

#### Deliverables
- [vacp2p/nim-libp2p#2316](https://github.com/vacp2p/nim-libp2p/pull/2316) feat(connmanager): ephemeral tags
- [vacp2p/nim-libp2p#2372](https://github.com/vacp2p/nim-libp2p/pull/2372) chore(connmanager): naming improvements
- [vacp2p/nim-libp2p#2356](https://github.com/vacp2p/nim-libp2p/pull/2356) chore(examples): add peer scoring examples

### AutoPrune
* fully qualified name: `ift-ts:p2p:ift:2026q2-nimlibp2p-connection-management:autoprune`
* owner: vlado
* status: done
* start-date: 2026/04/01
* end-date: 2026/04/28

#### Description
Implement pruning logic driven by the connection score. During pruning cycles, sort peers by score; Trim the lowest first with ties broken by heuristics such as connection age. Emit connection events once connections are pruned

#### Deliverables
- [vacp2p/nim-libp2p#2316](https://github.com/vacp2p/nim-libp2p/pull/2327)
- [vacp2p/nim-libp2p#2362](https://github.com/vacp2p/nim-libp2p/pull/2362) chore(examples): tidy
