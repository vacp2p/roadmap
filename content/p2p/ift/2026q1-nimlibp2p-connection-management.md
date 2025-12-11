---

title: nim-libp2p Connection Management
tags:
  - "2026q1"
  - "p2p"
  - "ift"
draft: false
description: Improved connection management in nim-libp2p

---

`vac:p2p:ift:2026q1-nimlibp2p-connection-management`

Improve nim-libp2p’s connection manager to provide hi/lo watermarks, score-driven pruning, decaying tags, and protected connections

## Description


The current connection manager is limited to cap total connections but doesn’t maintain a healthy steady state, doesn’t distinguish valuable peers, and keeps stale or useless connections. With this commitment new behavior will be introduced by having the connection manager maintain connection counts within configurable low/high watermarks and prune excess connections based on peer scores. It's tagging and decay system will prioritize valuable peers while ensuring unused or low-value connections are gracefully trimmed.

## Task List

### Hi/Lo limits
* fully qualified name: `vac:p2p:ift:2026q1-nimlibp2p-connection-management:limits`
* owner: not assigned yet
* status: not started
* start-date: 2026/01/01
* end-date: 2026/03/31

#### Description
Implement a hi/lo watermark subsystem. When connections exceed the higher limit, trigger a pruning cycle that continues until below the lower limit. Expose configuration options and allow switching between watermark mode and simple max-limit mode.

#### Deliverables
Hi-Lo watermark behavior for managing number of connections

### Connection score
* fully qualified name: `vac:p2p:ift:2026q1-nimlibp2p-connection-management:score`
* owner: not assigned yet
* status: not started
* start-date: 2026/01/01
* end-date: 2026/03/31

#### Description
Implement a per-connection scoring system with static and ephemeral tags. Ephemeral tags decay linearly (or by chosen function) so its importance decreases overtime. Allow marking connections as “protected” to exempt them from pruning. Outbound connections should naturally have a higher score than incoming connections

#### Deliverables
- API for adding/removing tags, setting weights, toggling decay  
- Protected-peer mechanism with hard guarantees  

### AutoPrune
* fully qualified name: `vac:p2p:ift:2026q1-nimlibp2p-connection-management:autoprune`
* owner: not assigned yet
* status: not started
* start-date: 2026/01/01
* end-date: 2026/03/31

#### Description
Implement pruning logic driven by the connection score. During pruning cycles, sort peers by score; Trim the lowest first with ties broken by heuristics such as connection age. Emit connection events once connections are pruned

#### Deliverables
- Automatically prune connections
