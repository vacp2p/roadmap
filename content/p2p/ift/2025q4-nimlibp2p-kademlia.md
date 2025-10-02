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

Implement Kademlia Distributed Hash Table in nim-libp2p, based on the [libp2p specification](https://github.com/libp2p/specs/blob/master/kad-dht/) as an additional discovery mechanism.
This commitment involves two main objectives: implementing nim-kademlia-dht, integrating this in nim-libp2p and making sure there is interoperability with other libp2p implementations.
This deliverable continues the work started in 2025q2

## Task List

### Routing table and RPC Protocol

* fully qualified name: `vac:p2p:ift:2025q2-nimlibp2p-kad-dht:routing-and-rpc`
* owner:
* status: 50%
* start-date: 2025-04-08
* end-date:

#### Description
Implement Kademlia’s XOR-based routing table with bucket management. Define RPC messages (`PING`, `SET_VALUE`, `GET_VALUE`, `SET_PROVIDERS`, `GET_PROVIDERS`, `FIND_NODE`) for node communication.

#### Deliverables



### Bootstrapping & Lookup Mechanism

* fully qualified name: `vac:p2p:ift:2025q4-nimlibp2p-kad-dht:bootstraping-and-lookup`
* owner:
* status: 35%
* start-date: 2025-05-05
* end-date:

#### Description
Enable nodes to join the network via bootstrap peers. Implement iterative lookup for efficient key
discovery and retrieval 

#### Deliverables



### Network Maintenance & Node Management

* fully qualified name: `vac:p2p:ift:2025q4-nimlibp2p-kad-dht:network-maintenance-node-management`
* owner:
* status: not started
* start-date:
* end-date:

#### Description
Handle bucket refresh, node eviction, and periodic pings to maintain an active routing table. 
Implement bucket splitting and adaptive refresh strategies.

#### Deliverables



### Data Storage & Replication

* fully qualified name: `vac:p2p:ift:2025q4-nimlibp2p-kad-dht:data-storage`
* owner:
* status: started
* start-date: 2025-07-28
* end-date:

#### Description
Implement the logic for `SET_VALUE` and `SET_PROVIDERS`. Store key-value pairs with expiration and replication mechanisms. 
Ensure values persist despite churn, using periodic re-publication and redundancy strategies

#### Deliverables


### Data Retrieval

* fully qualified name: `vac:p2p:ift:2025q4-nimlibp2p-kad-dht:data-retrieval`
* owner:
* status: not started
* start-date: 2025-07-28
* end-date:

#### Description
Implement the logic for `GET_VALUE` and `GET_PROVIDERS`. Implement validation and quorum mechanisms for queries

#### Deliverables

### Discovery
* fully qualified name: `vac:p2p:ift:2025q4-nimlibp2p-kad-dht:discovery`
* owner:
* status: 15%
* start-date: 2025-07-20
* end-date:

#### Description
Extend nim-libp2p discovery mechanism by providing a discovery interface that will use Kademlia DHT to advertise nodes and find peers