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
* owner: gabe/rramos
* status: 75%
* start-date: 2025-04-08
* end-date:

#### Description
Implement Kademlia’s XOR-based routing table with bucket management. Define RPC messages (`PING`, `SET_VALUE`, `GET_VALUE`, `ADD_PROVIDERS`, `GET_PROVIDERS`, `FIND_NODE`) for node communication.

#### Deliverables
- [vacp2p/nim-libp2p#1454](https://github.com/vacp2p/nim-libp2p/pull/1454) feat(kad-dht): routing table
- [vacp2p/nim-libp2p#1453](https://github.com/vacp2p/nim-libp2p/pull/1453) feat(kad-dht): protobuffers
- [vacp2p/nim-libp2p#1455](https://github.com/vacp2p/nim-libp2p/pull/1455) feat(kad-dht): handler
- [vacp2p/nim-libp2p#1744](https://github.com/vacp2p/nim-libp2p/pull/1744) feat(kad): add ping

### Bootstrapping & Lookup Mechanism

* fully qualified name: `vac:p2p:ift:2025q4-nimlibp2p-kad-dht:bootstraping-and-lookup`
* owner: rramos
* status: 100%
* start-date: 2025-05-05
* end-date: 2025-08-18

#### Description
Enable nodes to join the network via bootstrap peers. Implement iterative lookup for efficient key
discovery and retrieval 

#### Deliverables
- [vacp2p/nim-libp2p#1624](https://github.com/vacp2p/nim-libp2p/pull/1624) feat(kad-dht): findPeer


### Network Maintenance & Node Management

* fully qualified name: `vac:p2p:ift:2025q4-nimlibp2p-kad-dht:network-maintenance-node-management`
* owner:
* status: 50%
* start-date: 2025-10-08
* end-date:

#### Description
Handle bucket refresh, node eviction, and periodic pings to maintain an active routing table. 
Implement bucket splitting and adaptive refresh strategies.

#### Deliverables
- [vacp2p/nim-libp2p#1746](https://github.com/vacp2p/nim-libp2p/pull/1746) chore(kad): routing table eviction policy


### Data Storage & Replication

* fully qualified name: `vac:p2p:ift:2025q4-nimlibp2p-kad-dht:data-storage`
* owner: gabe
* status: 90%
* start-date: 2025-07-28
* end-date:

#### Description
Implement the logic for `SET_VALUE` and `ADD_PROVIDERS`. Store key-value pairs with expiration and replication mechanisms. 
Ensure values persist despite churn, using periodic re-publication and redundancy strategies

#### Deliverables
- [vacp2p/nim-libp2p#1582](https://github.com/vacp2p/nim-libp2p/pull/1582) feat(kad): Initial unstable putval api
- [vacp2p/nim-libp2p#1749](https://github.com/vacp2p/nim-libp2p/pull/1749) chore(kad): tidy up putVal 
- [vacp2p/nim-libp2p#1773](https://github.com/vacp2p/nim-libp2p/pull/1773) feat(kad): addProvider
- [vacp2p/nim-libp2p#1789](https://github.com/vacp2p/nim-libp2p/pull/1789) feat(kad): add ProviderManager


### Data Retrieval

* fully qualified name: `vac:p2p:ift:2025q4-nimlibp2p-kad-dht:data-retrieval`
* owner: gabe
* status: 60%
* start-date: 2025-07-28
* end-date:

#### Description
Implement the logic for `GET_VALUE` and `GET_PROVIDERS`. Implement validation and quorum mechanisms for queries

#### Deliverables
- [vacp2p/nim-libp2p#1764](https://github.com/vacp2p/nim-libp2p/pull/1764) chore(kad): add alpha handling
- [vacp2p/nim-libp2p#1750](https://github.com/vacp2p/nim-libp2p/pull/1750) feat(kad): add getValue
- [vacp2p/nim-libp2p#1765](https://github.com/vacp2p/nim-libp2p/pull/1765) chore(kad): getVal loop improvements


### Discovery
* fully qualified name: `vac:p2p:ift:2025q4-nimlibp2p-kad-dht:discovery`
* owner: gabe
* status: 0%
* start-date:
* end-date:

#### Description
Extend nim-libp2p discovery mechanism by providing a discovery interface that will use Kademlia DHT to advertise nodes and find peers

#### Deliverables



### Interop
* fully qualified name: `vac:p2p:ift:2025q4-nimlibp2p-kad-dht:interop`
* owner: gabe
* status: 0%
* start-date:
* end-date:

#### Description
Ensure interop is achieved between nim-libp2p's kad-dht implementation and other libp2p implementations

#### Deliverables