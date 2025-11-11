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
This commitment involves two main objectives: implementing nim-kademlia-dht, integrating this in nim-libp2p and making sure there is interoperability with other libp2p implementations.
This deliverable continues the work started in 2025q2

## Task List

### Routing table and RPC Protocol

* fully qualified name: `vac:p2p:ift:2025q2-nimlibp2p-kad-dht:routing-and-rpc`
* owner: Gabe
* status: 100%
* start-date: 2025-04-08
* end-date: ??

#### Description
Implement Kademlia’s XOR-based routing table with bucket management.
Define RPC messages (`PING`, `PUT_VALUE`, `GET_VALUE`, `ADD_PROVIDER`, `GET_PROVIDERS`, `FIND_NODE`) for node communication.

#### Deliverables


### Bootstrapping & Lookup Mechanism

* fully qualified name: `vac:p2p:ift:2025q3-nimlibp2p-kad-dht:bootstraping-and-lookup`
* owner: Gabe
* status: 100%
* start-date: 2025-05-05
* end-date: ??

#### Description
Enable nodes to join the network via bootstrap peers.
Implement iterative lookup for efficient key discovery and retrieval.

#### Deliverables


### Network Maintenance & Node Management

* fully qualified name: `vac:p2p:ift:2025q3-nimlibp2p-kad-dht:network-maintenance-node-management`
* owner: Gabe
* status: 60%
* start-date: 2025-10-01
* end-date:

#### Description
Handle bucket refresh, node eviction, and periodic pings to maintain an active routing table. 
Implement bucket splitting and adaptive refresh strategies.

#### Deliverables

### PING
* fully qualified name: `vac:p2p:ift:2025q3-nimlibp2p-kad-dht:ping`
* owner: Gabe
* status: 100%
* start-date: 
* end-date:

#### Description
Implement `PING` RPC message and tests.

#### Deliverables
- `handlePing`
- `sendPing`
- Tests
  
### PUT_VALUE
* fully qualified name: `vac:p2p:ift:2025q3-nimlibp2p-kad-dht:put-value`
* owner: Gabe
* status: 100%
* start-date: 
* end-date:

#### Description
Implement `PUT_VALUE` RPC message and tests.

#### Deliverables
- `handlePutValue`
- `sendPutValue`
- Tests

### GET_VALUE
* fully qualified name: `vac:p2p:ift:2025q3-nimlibp2p-kad-dht:get-value`
* owner: Gabe
* status: 100%
* start-date: 
* end-date:

#### Description
Implement `GET_VALUE` RPC message and tests.

#### Deliverables
- `handleGetValue`
- `sendGetValue`
- Tests
  
### ADD_PROVIDER
* fully qualified name: `vac:p2p:ift:2025q3-nimlibp2p-kad-dht:add-provider`
* owner: Gabe
* status: 100%
* start-date: 
* end-date:

#### Description
Implement `ADD_PROVIDER` RPC message and tests.

#### Deliverables
- `handleAddProvider`
- `sendAddProvider`
- `ProviderManager`
- Tests
  
### GET_PROVIDERS
* fully qualified name: `vac:p2p:ift:2025q3-nimlibp2p-kad-dht:get-providers`
* owner: Gabe
* status: 80%
* start-date: 2025-11-07 
* end-date:

#### Description
Implement `GET_PROVIDERS` RPC message and tests.

#### Deliverables
- `handleGetProviders`
- `sendGetProviders`
- Tests
  
### Interoperability Tests
* fully qualified name: `vac:p2p:ift:2025q3-nimlibp2p-kad-dht:interop`
* owner: Gabe
* status: 0%
* start-date: 
* end-date:

#### Description
Implement interoperability tests between nim-libp2p's kad implementation and others.

#### Deliverables
- interop with Go
- interop with Rust
