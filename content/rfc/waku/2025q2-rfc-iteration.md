---
title: RFC Iteration
tags:
  - rfc
  - waku
draft: false
description: "Iteration commitments generally comprise: through discussion and curation, support the process of auditing raw, draft, mature selected Waku RFCs."
---

`vac:rfc:waku:2025q2-rfc-iteration`

Iteration commitments generally comprise:
through discussion and curation,
support the process of auditing raw, draft, mature selected Waku RFCs.

## Description

This commitment supports the audit of mature RFCs, which are 
either in draft or raw states. The audit comprises of:
- Reading through the spec;
- Checking the relevant codebase;
- Changing the parts of the spec (descriptions and codebase) where applicable;
- Updates of relevant links;
- Changing the RFC status (optional);
- Going through rounds of feedback with the relevant project team;
- Adding clarifications where needed in the spec;
- Checking for inconsistencies with other documentation/codebase.

The following RFCs will be worked on in this quarter:
- 30/ADAPTIVE-NODES
- 66/WAKU2-METADATA
- 53/WAKU2-X3DH
- 54/WAKU2-X3DH-SESSIONS
- WAKU2-ENR
- WAKU2-DEVICE-PAIRING

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
- We aim to provide feedback on specifications
from the point of view of a new developer.

## Task List

### 30/ADAPTIVE-NODES

- Fully qualified name:
  `vac:rfc:waku:2025q2-rfc-iteration:30/adaptive-nodes`
- Owner: jimstir
- Status: 100% (https://github.com/vacp2p/rfc-index/pull/147)
- Start date: 2025/04/04
- End date: 2025/04/18

#### Description

This is an informational spec that showcases the concept of adaptive nodes.

In this task, our focus will be on updating the relevant links, the codebase
as well as any other outdated parts of the specification.

#### Deliverables

- Updated RFC document (potentially with an upgraded status).

### 66/WAKU2-METADATA

- Fully qualified name:
  `vac:rfc:waku:2025q1-rfc-iteration:66/waku2-metadata`
- Owner: cofson
- Status: 100% (https://github.com/vacp2p/rfc-index/pull/148)
- Start date: 2025/04/04
- End date: 2025/04/18

#### Description

This specification describes the metadata
that can be associated with a [10/WAKU2](https://rfc.vac.dev/waku/standards/core/10/waku2) node.

In this task, our focus will be on updating the relevant links, the codebase
as well as any other outdated parts of the specification.

#### Deliverables

- Updated RFC document (potentially with an upgraded status).

### 53/WAKU2-X3DH

- Fully qualified name:
  `vac:rfc:waku:2025q1-rfc-iteration:53/waku2-x3dh`
- Owner: cofson
- Status: 100% (https://github.com/vacp2p/rfc-index/pull/150)
- Start date: 2025/04/20
- End date: 2025/05/05

#### Description

This document describes a method
that can be used to provide a secure channel between two peers,
and thus provide confidentiality, integrity, authenticity and forward secrecy.
It is transport-agnostic and works over asynchronous networks.

In this task, our focus will be on updating the relevant links, the codebase
as well as any other outdated parts of the specification.

#### Deliverables

- Updated RFC document (potentially with an upgraded status).

### 54/WAKU2-X3DH-SESSIONS

- Fully qualified name:
  `vac:rfc:waku:2025q1-rfc-iteration:54/waku2-x3dh-sessions`
- Owner: cofson
- Status: 100% (https://github.com/vacp2p/rfc-index/pull/151)
- Start date: 2025/04/20
- End date: 2025/05/05

#### Description

This document specifies how to manage sessions
based on an X3DH key exchange.
This includes how to establish new sessions,
how to re-establish them, how to maintain them
and how to close them.

In this task, our focus will be on updating the relevant links, the codebase
as well as any other outdated parts of the specification.

#### Deliverables

- Updated RFC document (potentially with an upgraded status).

### WAKU2-RLN-CONTRACT

- Fully qualified name:
  `vac:rfc:waku:2025q1-rfc-iteration:waku2-rln-contract`
- Owner: jimstir
- Status: 100% (https://github.com/waku-org/specs/pull/62)
- Start date: 2025/04/20
- End date: 2025/05/05

#### Description

This document describes membership management
within the RLN smart contract.

In this task, our focus will be on updating the relevant links, the codebase
as well as any other outdated parts of the specification.

#### Deliverables

- Updated RFC document (potentially with an upgraded status).

### WAKU2-ENR

- Fully qualified name:
  `vac:rfc:waku:2025q1-rfc-iteration:waku2-enr`
- Owner: jimstir
- Status: 95% (https://github.com/waku-org/specs/pull/67)
- Start date: 2025/05/15
- End date: 2025/05/25

#### Description

This RFC describes the usage of the ENR (Ethereum Node Records) format
for [10/WAKU2](https://github.com/vacp2p/rfc-index/blob/main/waku/standards/core/10/waku2.md) purposes.
The ENR format is defined in [EIP-778](https://eips.ethereum.org/EIPS/eip-778) [3](https://github.com/waku-org/specs/blob/master/standards/core/enr.md#references).

In this task, our focus will be on updating the relevant links, the codebase
as well as any other outdated parts of the specification.

#### Deliverables

- Updated RFC document (potentially with an upgraded status).

### WAKU2-DEVICE-PAIRING

- Fully qualified name:
  `vac:rfc:waku:2025q1-rfc-iteration:waku2-device-pairing`
- Owner: jimstir
- Status: 100% (https://github.com/waku-org/specs/pull/63)
- Start date: 2025/05/09
- End date: 2025/05/20

#### Description

In this document we describe a compound protocol
for enabling two devices
to mutually authenticate
and securely exchange (arbitrary) information
over the Waku network.

In this task, our focus will be on updating the relevant links, the codebase
as well as any other outdated parts of the specification.

#### Deliverables

- Updated RFC document (potentially with an upgraded status).