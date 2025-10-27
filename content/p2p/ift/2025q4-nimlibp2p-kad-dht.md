---

title: Kademlia DHT
tags:
  - "2025q4"
  - "p2p"
  - "ift"
draft: false
description: Implement Kademlia DHT

---

`vac:p2p:ift:2025q4-nimlibp2p-kad-dht`

## Description

Implement Kademlia Distributed Hash Table in nim-libp2p, based on the [libp2p specification](https://github.com/libp2p/specs/blob/master/kad-dht/) as an additional discovery mechanism.
This commitment involves two main objectives: implementing nim-kademlia-dht, integrating this in nim-libp2p and making sure there is interoperability with other libp2p implementations.
This deliverable continues the work started in 2025q2

## Task List

### Routing table and RPC Protocol

* fully qualified name: `vac:p2p:ift:2025q4-nimlibp2p-kad-dht:routing-and-rpc`
* owner: rramos
* status: in progress (50%)
* start-date: 2025/10/01
* end-date: 2025/12/31

#### Description
Implement Kademlia’s XOR-based routing table with bucket management. Define RPC messages (`PING`, `SET_VALUE`, `GET_VALUE`, `SET_PROVIDERS`, `GET_PROVIDERS`, `FIND_NODE`) for node communication.

Schedule note: Dates reflect quarter bounds; update when actual timing is known.
#### Deliverables
- PRs/Issues/Docs/Reports


### Bootstrapping & Lookup Mechanism

* fully qualified name: `vac:p2p:ift:2025q4-nimlibp2p-kad-dht:bootstraping-and-lookup`
* owner: rramos
* status: in progress (35%)
* start-date: 2025/10/01
* end-date: 2025/12/31

#### Description
Enable nodes to join the network via bootstrap peers. Implement iterative lookup for efficient key
discovery and retrieval 

Schedule note: Dates reflect quarter bounds; update when actual timing is known.
#### Deliverables
- PRs/Issues/Docs/Reports


### Network Maintenance & Node Management

* fully qualified name: `vac:p2p:ift:2025q4-nimlibp2p-kad-dht:network-maintenance-node-management`
* owner: rramos
* status: not started
* start-date: 2025/10/01
* end-date: 2025/12/31

#### Description
Handle bucket refresh, node eviction, and periodic pings to maintain an active routing table. 
Implement bucket splitting and adaptive refresh strategies.

Schedule note: Dates reflect quarter bounds; update when actual timing is known.
#### Deliverables
- PRs/Issues/Docs/Reports


### Data Storage & Replication

* fully qualified name: `vac:p2p:ift:2025q4-nimlibp2p-kad-dht:data-storage`
* owner: rramos
* status: not started
* start-date: 2025/10/01
* end-date: 2025/12/31

#### Description
Implement the logic for `SET_VALUE` and `SET_PROVIDERS`. Store key-value pairs with expiration and replication mechanisms. 
Ensure values persist despite churn, using periodic re-publication and redundancy strategies

Schedule note: Dates reflect quarter bounds; update when actual timing is known.
#### Deliverables
- PRs/Issues/Docs/Reports


### Data Retrieval

* fully qualified name: `vac:p2p:ift:2025q4-nimlibp2p-kad-dht:data-retrieval`
* owner: rramos
* status: not started
* start-date: 2025/10/01
* end-date: 2025/12/31

#### Description
Implement the logic for `GET_VALUE` and `GET_PROVIDERS`. Implement validation and quorum mechanisms for queries

Schedule note: Dates reflect quarter bounds; update when actual timing is known.

#### Deliverables
- PRs/Issues/Docs/Reports


### Discovery
* fully qualified name: `vac:p2p:ift:2025q4-nimlibp2p-kad-dht:discovery`
* owner: rramos
* status: in progress (15%)
* start-date: 2025/10/01
* end-date: 2025/12/31

#### Description
Extend nim-libp2p discovery mechanism by providing a discovery interface that will use Kademlia DHT to advertise nodes and find peers

Schedule note: Dates reflect quarter bounds; update when actual timing is known.

#### Deliverables
- PRs/Issues/Docs/Reports