---
title: RFC Iteration
tags:
  - rfc
  - waku
draft: false
description: "Iteration commitments generally comprise: through discussion and curation, support the process of auditing raw, draft, mature selected Waku RFCs."
---

`vac:rfc:waku:2025q1-rfc-iteration`

Iteration commitments generally comprise:
through discussion and curation,
support the process of auditing raw, draft, mature selected Waku RFCs.

## Description

This commitment supports the audit of the following mature RFCs, which are 
either in draft or raw states:
- 10/WAKU2 
- 20/TOY-ETH-PM
- 21/WAKU2-FAULT-TOLERANT-STORE
- 26/WAKU2-PAYLOAD
- 33/WAKU2-DISCV5
- 36/WAKU2-BINDINGS-API
- 23/WAKU2-TOPICS
- 27/WAKU2-PEERS
- 29/WAKU2-CONFIG

We will also include specification validation - 
editorial work through previous and future RFCs to improve them
(identify edge cases for example)

**Alignment with VAC Narratives:**

- The VAC RFC team plans to become a repository
for RFCs regarding all IFT 
  projects.
- By promoting the RFC culture,
we hope to incentivize projects to submit their RFCs
to the rfc-editors team.
- We aim to have the broader web3 community use our RFCs
in their projects, similar to [IETF](https://www.ietf.org/).

## Task List

### 10/WAKU2

- Fully qualified name: 
  `vac:rfc:waku:2025q1-rfc-iteration:10/waku2`
- Owner: jimstir
- Status: 95%
- Start date: 2025/01/01
- End date: 2025/01/31

#### Description

Waku v2 is a family of modular peer-to-peer protocols for secure communication.

#### Deliverables

- Updated RFC document (potentially with an upgraded status).


### 20/TOY-ETH-PM

- Fully qualified name: 
  `vac:rfc:waku:2025q1-rfc-iteration:20/toy-eth-pm`
- Owner: jimstir
- Status: not started
- Start date: 2025/02/14
- End date: 2025/02/28

#### Description

This specification explains the Toy Ethereum Private Message protocol
which enables a peer to send an encrypted message to another peer
using the Waku v2 network, and the peer's Ethereum address.

#### Deliverables

- Updated RFC document (potentially with an upgraded status).


### 21/WAKU2-FAULT-TOLERANT-STORE

- Fully qualified name: 
  `vac:rfc:waku:2025q1-rfc-iteration:21/waku2-fault-tolerant-store`
- Owner: jimstir
- Status: not started
- Start date: 2025/02/28
- End date: 2025/03/14

#### Description

The reliability of [13/WAKU2-STORE](https://rfc.vac.dev/waku/standards/core/13/store) protocol heavily relies on the fact
that full nodes i.e., those who persist messages have high availability
and uptime and do not miss any messages.

#### Deliverables

- Updated RFC document (potentially with an upgraded status).


### 26/WAKU2-PAYLOAD

- Fully qualified name: 
  `vac:rfc:waku:2025q1-rfc-iteration:26/waku2-payload`
- Owner: jimstir
- Status: not started
- Start date: 2025/03/07
- End date: 2025/03/21

#### Description

This specification describes how Waku provides confidentiality, authenticity
and integrity, as well as some form of unlinkability.

#### Deliverables

- Updated RFC document (potentially with an upgraded status).


### 33/WAKU2-DISCV5

- Fully qualified name: 
  `vac:rfc:waku:2025q1-rfc-iteration:33/waku2-discv5`
- Owner: jimstir
- Status: not started
- Start date: 2025/03/14
- End date: 2025/03/31

#### Description

This document specifies a modified version of [Ethereum's Node Discovery Protocol v5](https://github.com/ethereum/devp2p/blob/master/discv5/discv5.md)
as a means for ambient node discovery.

#### Deliverables

- Updated RFC document (potentially with an upgraded status).


### 36/WAKU2-BINDINGS-API

- Fully qualified name: 
  `vac:rfc:waku:2025q1-rfc-iteration:36/waku2-bindings-api`
- Owner: Filip
- Status: 75%
- Start date: 2025/02/07
- End date: 2025/02/31

#### Description

This specification describes the C API that SHOULD be implemented by native Waku library
and that SHOULD be used to consume them.

#### Deliverables

- Updated RFC document (potentially with an upgraded status).

### 23/WAKU2-TOPICS

- Fully qualified name: 
  `vac:rfc:waku:2025q1-rfc-iteration:23/waku2-topics`
- Owner: jimstir
- Status: 0%
- Start date: 2025/02/07
- End date: 2025/03/31

#### Description

This document outlines recommended usage of topic names in Waku v2.
In [10/WAKU2 spec](https://github.com/vacp2p/rfc-index/blob/main/waku/standards/core/10/waku2.md) there are two types of topics:

- pubsub topics, used for routing
- Content topics, used for content-based filtering

#### Deliverables

- Updated RFC document (potentially with an upgraded status).

### 27/WAKU2-PEERS

- Fully qualified name: 
  `vac:rfc:waku:2025q1-rfc-iteration:27/waku2-peers`
- Owner: jimstir
- Status: 0%
- Start date: 2025/02/01
- End date: 2025/03/31

#### Description

`27/WAKU2-PEERS` describes a recommended minimal set of peer storage
and peer management features to be implemented by Waku v2 clients.

#### Deliverables

- Updated RFC document (potentially with an upgraded status).


### 29/WAKU2-CONFIG

- Fully qualified name: 
  `vac:rfc:waku:2025q1-rfc-iteration:29/waku2-config`
- Owner: jimstir
- Status: 0%
- Start date: 2025/02/01
- End date: 2025/03/31

#### Description

`29/WAKU2-CONFIG` describes the RECOMMENDED values
to assign to configurable parameters for Waku v2 clients.
Since Waku v2 is built on [libp2p](https://github.com/libp2p/specs), most of the parameters
and reasonable defaults are derived from there.

#### Deliverables

- Updated RFC document (potentially with an upgraded status).