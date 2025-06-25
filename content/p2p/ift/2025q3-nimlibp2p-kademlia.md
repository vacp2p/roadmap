---

title: Kademlia DHT
tags:
  - "2025q3"
  - "p2p"
  - "ift"
draft: false
description: Implement Kademlia DHT

---

`vac:p2p:ift:2025q3-nimlibp2p-kad-dht`

Implement Kademlia Distributed Hash Table in nim-libp2p, based on the [libp2p specification](https://github.com/libp2p/specs/blob/master/kad-dht/) as an additional discovery mechanism.
This commitment involves two main objectives: implementing nim-kademlia-dht, and integrating this in nim-libp2p
This deliverable continues the work started in 2025q2

## Task List

### Routing table and RPC Protocol

* fully qualified name: `vac:p2p:ift:2025q2-nimlibp2p-kad-dht:routing-and-rpc`
* owner: rramos
* status: 50%
* start-date: 2025-04-08
* end-date:

#### Description
Implement Kademlia’s XOR-based routing table with bucket management. Define RPC messages (`PING`, `STORE`, `FIND_NODE`,
`FIND_VALUE`) for node communication.

#### Deliverables



### Bootstrapping & Lookup Mechanism

* fully qualified name: `vac:p2p:ift:2025q3-nimlibp2p-kad-dht:bootstraping-and-lookup`
* owner: rramos
* status: 35%
* start-date: 2025-05-05
* end-date:

#### Description
Enable nodes to join the network via bootstrap peers. Implement iterative lookup for efficient key
discovery and retrieval 

#### Deliverables



### Network Maintenance & Node Management

* fully qualified name: `vac:p2p:ift:2025q3-nimlibp2p-kad-dht:network-maintenance-node-management`
* owner: rramos
* status: not started
* start-date:
* end-date:

#### Description
Handle bucket refresh, node eviction, and periodic pings to maintain an active routing table. 
Implement bucket splitting and adaptive refresh strategies.

#### Deliverables



### Data Storage & Replication

* fully qualified name: `vac:p2p:ift:2025q3-nimlibp2p-kad-dht:data-storage`
* owner: rramos
* status: not started
* start-date:
* end-date:

#### Description
Store key-value pairs with expiration and replication mechanisms. Ensure values persist despite churn, using periodic
re-publication and redundancy strategies.

#### Deliverables

