---

title: GossipSub Priority Queues
tags:
  - "2026q2"
  - "p2p"
  - "ift"
draft: false
description: GossipSub Priority Queues

---

`ift-ts:p2p:ift:2026q2-nimlibp2p-gossipsub-queues`

## Description

This commitment focuses on making nim-libp2p GossipSub outbound queues bounded
under load. The current implementation disconnects a peer when the non-priority
queue reaches its hardcoded limit, while the priority queue can grow without bound. 
This is acceptable for low-priority gossip traffic only as an initial solution, 
but it is not a complete queueing strategy for GossipSub in general.

The work is to separate outbound traffic by semantics and give each class an 
explicit policy. Protocol-critical messages must not be dropped because 
doing so can leave peers out of sync, so when there is no room left for them the 
correct response is to disconnect the peer. Best-effort traffic such as rebroadcasts 
can instead be dropped under pressure, because gossip remains resilient when individual 
messages are lost.

## Task List

### Queue Priorities And Limits

* fully qualified name: `ift-ts:p2p:ift:2026q2-nimlibp2p-gossipsub-queues:queue-priorities`
* owner: richard
* status: done
* start-date: 2026/04/01
* end-date: 2026/04/14

#### Description
Audit the current outbound message classification and replace the existing
two-level behavior with explicit priorities:
- high priority for protocol critical messages,
- medium priority for locally published messages, which should be sent before
  rebroadcast traffic but may still be dropped under pressure,
- low priority for rebroadcast and other best-effort gossip traffic.

All classes should have explicit bounds so large messages or slow peers cannot
cause unbounded memory growth.

#### Deliverables
- Outbound GossipSub traffic split into queue priorities
- Explicit queue limits for every outbound priority level
- Documentation of the intended behavior for each queue priority


### Priority Queue Semantics

* fully qualified name: `ift-ts:p2p:ift:2026q2-nimlibp2p-gossipsub-queues:control-queue`
* owner: richard
* status: done
* start-date: 2026/04/01
* end-date: 2026/04/14

#### Description
Implement bounded handling for priority messages. If the priority queue is full,
the peer should be disconnected instead of dropping the message, because
messages such as subscription updates must be delivered to keep the protocol in
sync. If possible, improve the priority path by refreshing or consolidating pending updates
when possible, so redundant sequences such as subscribe followed by unsubscribe
do not consume queue space unnecessarily.

#### Deliverables
- Disconnect-on-full policy for priority-message overflow
- Refresh logic for pending priority updates
- Tests covering priority-message overflow and queue refresh behavior


### Best-Effort Queue Policy

* fully qualified name: `ift-ts:p2p:ift:2026q2-nimlibp2p-gossipsub-queues:best-effort-policy`
* owner: richard
* status: done
* start-date: 2026/04/01
* end-date: 2026/04/21

#### Description
Define drop-on-full behavior for non-priority traffic. Rebroadcast traffic is
expected to have high queue usage, and gossip can tolerate losing some of
these messages. Locally published messages should be prioritized over
rebroadcasts, but they should not be allowed to grow an unbounded queue either.
Revisit the current hardcoded low-priority threshold and document whether queue
depth should also contribute to peer scoring as a secondary pruning signal.

#### Deliverables
- Drop-on-full behavior for non-priority outbound traffic
- Updated thresholds for non-priority queues
- Clear policy for how queue pressure interacts with peer scoring
- [vacp2p/nim-libp2p#2269](https://github.com/vacp2p/nim-libp2p/pull/2269) feat(gossip): reduce score of slow peers


### Validation And Interop

* fully qualified name: `ift-ts:p2p:ift:2026q2-nimlibp2p-gossipsub-queues:validation`
* owner: richard
* status: in progress (20%)
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description
Validate the new queue behavior with targeted tests and interoperability
checks. Cover slow or stalled peers, large message bursts, and queue-pressure
scenarios where rebroadcast traffic is dropped while priority traffic still
forces a disconnect on overflow. Compare the resulting behavior with other
implementations especially in areas where aggressive dropping may
affect mesh stability.

#### Deliverables
- [vacp2p/nim-libp2p#2241](https://github.com/vacp2p/nim-libp2p/pull/2241) feat(gossipsub): extend message priorities to H/M/L
- Unit or integration tests for queue-pressure behavior
- Interoperability checks for queue overflow and message dropping
- Queue behavior validated for slow-peer and large-message scenarios
