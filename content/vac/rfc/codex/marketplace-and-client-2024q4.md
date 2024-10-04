---
title: Marketplace and Client 2024q4
tags:
  - 2024q4
  - rfc
  - codex
draft: false
description: Help deliver raw and draft RFCs for Codex Marketplace and Codex Client through discussion and support.
---

`ift:rfc:codex:marketplace-and-client-2024q4`

Help deliver raw and draft RFCs for Codex Marketplace and Codex Client through discussion and support.
## Description

This commitment revolves around supporting the delivery of a raw RFCs for Codex Marketplace and Codex Client through discussion, support and inquiring about the updates. The team plans to start establishing the RFC culture within the Codex ecosystem, in order to have standardized specifications within all IFT ecosystems.

The initial RFCs we will be focusing on are Codex Client - Erasure Coding, Codex Manifest and Codex Marketplace. Codex Marketplace has been chosen due to it being one of the focal points within the ecosystem. Erasure Coding and Manifest are referenced within the Marketplace and were discussed to become separate RFCs (it is still open for discussion). 

What we want to have, through our effort of driving and supporting the discussion with the Codex team: 
- Raw RFCs,  
- Draft RFCs (dependable on the state of Codex as well)
- Iterations of versions of draft RFCs (dependable on the state of Codex as well)

What we will not have: 
- Stable RFCs, that will be part of a future commitment.

**Alignment with VAC Narratives:**

* The VAC RFC team plans to become a repository for RFCs regarding all the IFT projects.
* By providing information and benefits of the RFC Culture, we want to have projects apply their RFCs to the team of rfc-editors, in the future.
* One of our ideals is to have the broader web3 community utilize our RFCs to potentially implement within their projects and ecosystems (similar to how [IETF](https://www.ietf.org/) works). 

## Task List

### Codex Client - Erasure Coding

* fully qualified name: `ift:rfc:codex:marketplace-and-client:erasure-coding`
* owner: jimstir
* status: not started
* start-date: 2024/08/16
* end-date: 2024/12/31

#### Description 
This specification describes the erasure coding technique used in the Codex protocol. Erasure coding is used by the Codex client to encode datasets being presented to the marketplace. 

Codex uses storage proofs to determine whether a storage provider is storing a certain dataset. Storage providers agree to store dataset for a period of time and store an encoded dataset provided by the requester. Using erasure coding, client nodes will be able to restore datasets that are abandoned by storage providers. Also validator nodes are able to detect whether data is missing within a slot.

#### Deliverables 
* Raw RFC 
* Draft RFC (potentially)

### Codex Client - Manifest

* fully qualified name: `ift:rfc:codex:marketplace-and-client:manifest
* owner: jimstir
* status: not started
* start-date: 2024/09/01
* end-date: 2024/12/31

#### Description 
This specification describes the parameters used in the manifest for a Codex client application. The manifest is used to encode datasets with a Codex client node. 

#### Deliverables 
* Raw RFC 
* Draft RFC (potentially)
### Codex Marketplace

* fully qualified name: `ift:rfc:codex:marketplace-and-client:marketplace`
* owner: jimstir
* status: not started
* start-date: 2024/06/15
* end-date: 2024/12/31

#### Description 
The marketplace is a critical component of the Codex network, serving as a platform where all involved parties interact to ensure data persistence. It provides mechanisms to enforce agreements and facilitate data repair when storage providers (SPs), fail to fulfill their duties.

Codex Marketplace and its interactions are defined by a smart contract deployed on an EVM-compatible blockchain. This specification describes these interactions for the various roles within the network.

#### Deliverables 
* Raw RFC 
* Draft RFC (potentially)