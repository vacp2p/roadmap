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
* owner: gabe/rramos
* status: in progress (75%)
* start-date: 2025/10/01
* end-date: 2025/12/31

#### Description
Implement Kademlia’s XOR-based routing table with bucket management. Define RPC messages (`PING`, `PUT_VALUE`, `GET_VALUE`, `ADD_PROVIDER`, `GET_PROVIDERS`, `FIND_NODE`) for node communication.

Schedule note: Dates reflect quarter bounds; update when actual timing is known.
#### Deliverables
- [vacp2p/nim-libp2p#1454](https://github.com/vacp2p/nim-libp2p/pull/1454) feat(kad-dht): routing table
- [vacp2p/nim-libp2p#1453](https://github.com/vacp2p/nim-libp2p/pull/1453) feat(kad-dht): protobuffers
- [vacp2p/nim-libp2p#1455](https://github.com/vacp2p/nim-libp2p/pull/1455) feat(kad-dht): handler
- [vacp2p/nim-libp2p#1744](https://github.com/vacp2p/nim-libp2p/pull/1744) feat(kad): add ping


### Bootstrapping & Lookup Mechanism

* fully qualified name: `vac:p2p:ift:2025q4-nimlibp2p-kad-dht:bootstraping-and-lookup`
* owner: rramos
* status: done
* start-date: 2025/10/01
* end-date: 2025/12/31

#### Description
Enable nodes to join the network via bootstrap peers. Implement iterative lookup for efficient key
discovery and retrieval

Schedule note: Dates reflect quarter bounds; update when actual timing is known.
#### Deliverables
- [vacp2p/nim-libp2p#1624](https://github.com/vacp2p/nim-libp2p/pull/1624) feat(kad-dht): findPeer


### Network Maintenance & Node Management

* fully qualified name: `vac:p2p:ift:2025q4-nimlibp2p-kad-dht:network-maintenance-node-management`
* owner: gabe
* status: in progress (50%)
* start-date: 2025/10/01
* end-date: 2025/12/31

#### Description
Handle bucket refresh, node eviction, and periodic pings to maintain an active routing table.
Implement bucket splitting and adaptive refresh strategies.

Schedule note: Dates reflect quarter bounds; update when actual timing is known.
#### Deliverables
- [vacp2p/nim-libp2p#1746](https://github.com/vacp2p/nim-libp2p/pull/1746) chore(kad): routing table eviction policy


### Data Storage & Replication

* fully qualified name: `vac:p2p:ift:2025q4-nimlibp2p-kad-dht:data-storage`
* owner: gabe
* status: in progress (90%)
* start-date: 2025/10/01
* end-date: 2025/12/31

#### Description
Implement the logic for `PUT_VALUE` and `ADD_PROVIDER`. Store key-value pairs with expiration and replication mechanisms.
Ensure values persist despite churn, using periodic re-publication and redundancy strategies

Schedule note: Dates reflect quarter bounds; update when actual timing is known.
#### Deliverables
- [vacp2p/nim-libp2p#1582](https://github.com/vacp2p/nim-libp2p/pull/1582) feat(kad): Initial unstable putval api
- [vacp2p/nim-libp2p#1749](https://github.com/vacp2p/nim-libp2p/pull/1749) chore(kad): tidy up putVal
- [vacp2p/nim-libp2p#1773](https://github.com/vacp2p/nim-libp2p/pull/1773) feat(kad): addProvider
- [vacp2p/nim-libp2p#1789](https://github.com/vacp2p/nim-libp2p/pull/1789) feat(kad): add ProviderManager
- [vacp2p/nim-libp2p#1843](https://github.com/vacp2p/nim-libp2p/pull/1843) chore(kad): ProviderManager limits
- [vacp2p/nim-libp2p#1848](https://github.com/vacp2p/nim-libp2p/pull/1848) chore(kad): Provider manager touchups


### Data Retrieval

* fully qualified name: `vac:p2p:ift:2025q4-nimlibp2p-kad-dht:data-retrieval`
* owner: gabe
* status: in progress (90%)
* start-date: 2025/10/01
* end-date: 2025/12/31

#### Description
Implement the logic for `GET_VALUE` and `GET_PROVIDERS`. Implement validation and quorum mechanisms for queries

Schedule note: Dates reflect quarter bounds; update when actual timing is known.
#### Deliverables
- [vacp2p/nim-libp2p#1764](https://github.com/vacp2p/nim-libp2p/pull/1764) chore(kad): add alpha handling
- [vacp2p/nim-libp2p#1750](https://github.com/vacp2p/nim-libp2p/pull/1750) feat(kad): add getValue
- [vacp2p/nim-libp2p#1765](https://github.com/vacp2p/nim-libp2p/pull/1765) chore(kad): getVal loop improvements
- [vacp2p/nim-libp2p#1773](https://github.com/vacp2p/nim-libp2p/pull/1773) feat(kad): addProvider
- [vacp2p/nim-libp2p#1783](https://github.com/vacp2p/nim-libp2p/pull/1783) chore(kad): make key field mandatory
- [vacp2p/nim-libp2p#1852](https://github.com/vacp2p/nim-libp2p/pull/1852) feat(kad): get providers


### Discovery

* fully qualified name: `vac:p2p:ift:2025q4-nimlibp2p-kad-dht:discovery`
* owner: gabe
* status: in progress (45%)
* start-date: 2025/10/01
* end-date: 2025/12/31

#### Description
Extend nim-libp2p discovery mechanism by providing a discovery interface that will use Kademlia DHT to advertise nodes and find peers

#### Deliverables
- [chore(discovery): remove unused discovery interface](https://github.com/vacp2p/nim-libp2p/pull/1890)


### Interop
* fully qualified name: `vac:p2p:ift:2025q4-nimlibp2p-kad-dht:interop`
* owner: gabe
* status: in progress (70%)
* start-date: 2025/10/01
* end-date: 2025/12/31

#### Description
Ensure interop is achieved between nim-libp2p's kad-dht implementation and other libp2p implementations

#### Deliverables
- [Kad PUT_VALUE response deviating from the spec](https://github.com/libp2p/rust-libp2p/issues/6217)
- [Re-enable rust interop kad tests when they adhere to the spec](https://github.com/vacp2p/nim-libp2p/issues/1915)
- [LPProtocol should have `method handler`](https://github.com/vacp2p/nim-libp2p/issues/1913)
- [chore(kad): bootstrap does not need peerinfo](https://github.com/vacp2p/nim-libp2p/pull/1903)
- [feat(kad): client mode](https://github.com/vacp2p/nim-libp2p/pull/1908)
- [chore(kad): bootstrap on switch start](https://github.com/vacp2p/nim-libp2p/pull/1906)
- [chore(kad): add withKademlia to SwitchBuilder](https://github.com/vacp2p/nim-libp2p/pull/1907)
