---
title: Waku Scaling
tags:
  - "2026q1"
  - "dst"
  - "waku"
draft: false
description: "Use experiments determine and
improve Waku's scaling properties.
Find the limits of Waku's capabilities
and measure them in different scenarios.
Deliver hard numbers and actionable insights.
Confirm or reject our ideas or presented ones."
---

`vac:dst:waku:2026q1-waku-scaling`

## Description

We will use realistic Waku node experiments to evaluate
and improve Waku's scalability by conducting
performance measurements across its key components and tasks.
These efforts contains supporting on-chain RLN memberships,
strengthening the foundations for private chats, optimize 
browser bootstrapping for improved responsiveness, 
integrate nwaku in Status Desktop for seamless relay functionality,
and implement the SDS protocol for group messaging reliability and recovery.

## Task list

### scalable data sync

* fully qualified name: `vac:dst:waku:2026q1-waku-scaling:scalable-data-sync`
* owner: TBD
* status: not started
* start-date: 2026/01/01
* end-date: 2026/03/31

#### Description

1. When sending a message in a group, the publisher can ensure the message 
was received by at least one recipient within `S` seconds **(Vac-DST)**.
3. When receiving messages in group, the receiver can reach eventual 
consistency within `6*S` seconds **(Vac-DST)**.

#### Deliverables
- PRs:
- Related Documents:


### Status communities

* fully qualified name: `vac:dst:waku:2026q1-waku-scaling:status-communities`
* owner: TBD
* status: not started
* start-date: 2026/01/01
* end-date: 2026/03/31

#### Description
Logos-messaging specific FURPS, before Chat SDK integration.

1. Time to setup filter subscriptions for Communities has improved by >20% (**Vac-DST**).
2. Time to retrieve 24 hours of Communities messages has improved by >20% (**Vac-DST**).
3. Increased community traffic does not increase bandwidth usage of 1:1 chat (**Vac-DST**).

#### Deliverables
- PRs:
- Related Documents:

### Status private chats

* fully qualified name: `vac:dst:waku:2026q1-waku-scaling:status-private-chats`
* owner: TBD
* status: not started
* start-date: 2026/01/01
* end-date: 2026/03/31

#### Description
1. 99% of one-to-one user messages are eventually received by their recipient, within 5 minutes of being online (**Vac-DST**).
2. One-to-one chat’s non-user messages do not consume over 20% of the allocated quota (**Vac-DST**).

#### Deliverables
- PRs:
- Related Documents:

### Incentivisation

* fully qualified name: `vac:dst:waku:2026q1-waku-scaling:incentivisation`
* owner: TBD
* status: not started
* start-date: 2026/01/01
* end-date: 2026/03/31

#### Description
Reliability
3. In a stable network, a client can find, pay and send a message via a RLNaaS provider (**Vac-QA**)
   in 90% of cases **(Vac-DST)**
3. A client can assess whether an RLNaaS provider has relayed their message (**Vac-QA**)
   in 90% of cases **(Vac-DST)**.

Performance:
1. Assuming a block time of 5 seconds,
   a user can execute an RLNaaS payment and send a message within 30 seconds (Vac-DST)

#### Deliverables
- PRs:
- Related Documents:

### Rendezvous

* fully qualified name: `vac:dst:waku:2026q1-waku-scaling:rendezvous`
* owner: TBD
* status: not started
* start-date: 2026/01/01
* end-date: 2026/03/31

#### Description
1. In an established network of 1k relay nodes on 10 shards with 1 bootstrap node,
   100 new relay nodes (relay + discv5 + Waku PX + rendezvous)
   can connect to 20 relay peers in the right shard within 1 minute (**Vac-DST**)
   ; run simulation without rendezvous to see the difference

#### Deliverables
- PRs:
- Related Documents:

### RLN Relay

* fully qualified name: `vac:dst:waku:2026q1-waku-scaling:rln-relay`
* owner: TBD
* status: not started
* start-date: 2026/01/01
* end-date: 2026/03/31

#### Description
1. In a network of 10k RLN Relay nodes with each node sending one 1-100KB message every 10-30s,
   messages are propagated within 500ms, with 99.9% success **(Vac-DST)**.
2. In a network of 10k RLN Relay nodes,
   a spamming node will be disconnected from its peers in under 1 min. **(Vac-DST)**

#### Deliverables
- PRs:
- Related Documents:

### Store

* fully qualified name: `vac:dst:waku:2026q1-waku-scaling:store`
* owner: TBD
* status: not started
* start-date: 2026/01/01
* end-date: 2026/03/31

#### Description
5. 95th percentile of hash queries are served in less than 10ms of less than 10 hashes;
for a database less than 250 GB size and average message size under 500KiB **(Vac-DST)**.
6. 90th percentile of time range queries are served in less than 10ms; if the query is 
less than 1 hour, using up to 10 content topics, for a database less than 250 GB size 
and average message size under 500KiB  **(Vac-DST)**.

#### Deliverables
- PRs:
- Related Documents:

### Store sync

* fully qualified name: `vac:dst:waku:2026q1-waku-scaling:store-sync`
* owner: TBD
* status: not started
* start-date: 2026/01/01
* end-date: 2026/03/31

#### Description
1. A sync of a 60 minutes time window happens under 60 seconds, assuming 15 msgs/second (total), 
150KB message size and a maximum of 10% pre-existing message discrepancy (**Vac-DST**).

#### Deliverables
- PRs:
- Related Documents: