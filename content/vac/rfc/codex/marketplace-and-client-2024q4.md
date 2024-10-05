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

Help deliver raw and draft RFCs for Codex Marketplace and Codex Client through 
discussion and support.

## Description

This commitment revolves around supporting the delivery of raw RFCs for Codex 
Marketplace and Codex Client via discussion, support, and inquiring about 
updates. The goal is to establish an RFC culture within the Codex ecosystem to 
standardize specifications across all IFT ecosystems.

The initial focus will be on Codex Client (Erasure Coding), Codex Manifest, and 
Codex Marketplace. Codex Marketplace is a focal point within the ecosystem, and 
Erasure Coding and Manifest are referenced within it. These may become separate 
RFCs, though it's still open for discussion.

Through our efforts in driving and supporting discussions with the Codex team, 
we aim to achieve:

- Raw RFCs  
- Draft RFCs (depending on Codex's state)
- Iterations of draft RFCs (also dependent on Codex's state)

What we will **not** achieve:

- Stable RFCs, which will be part of future commitments.

**Alignment with VAC Narratives:**

- The VAC RFC team aims to be a repository for RFCs across all IFT projects.
- We aim to encourage projects to submit RFCs to the team of rfc-editors.
- The long-term goal is to have the broader web3 community use our RFCs within 
  their projects, similar to how [IETF](https://www.ietf.org/) operates.

## Task List

### Codex Client - Erasure Coding

- Fully qualified name: `ift:rfc:codex:marketplace-and-client:erasure-coding`
- Owner: jimstir
- Status: not started
- Start date: 2024/08/16
- End date: 2024/12/31

#### Description 

This specification outlines the erasure coding technique used in the Codex 
protocol. The Codex client encodes datasets presented to the marketplace using 
this technique. Storage providers agree to store encoded datasets for a period, 
and client nodes can restore datasets abandoned by providers. Validator nodes 
detect missing data.

#### Deliverables 

- Raw RFC  
- Draft RFC (potentially)

### Codex Client - Manifest

- Fully qualified name: `ift:rfc:codex:marketplace-and-client:manifest`
- Owner: jimstir
- Status: not started
- Start date: 2024/09/01
- End date: 2024/12/31

#### Description 

This specification describes the parameters used in the manifest for Codex 
client applications. The manifest encodes datasets within a Codex client node.

#### Deliverables 

- Raw RFC  
- Draft RFC (potentially)

### Codex Marketplace

- Fully qualified name: `ift:rfc:codex:marketplace-and-client:marketplace`
- Owner: jimstir
- Status: not started
- Start date: 2024/06/15
- End date: 2024/12/31

#### Description 

The Codex Marketplace is crucial to the network, enabling data persistence by 
facilitating interactions among participants. It provides mechanisms for 
enforcing agreements and repairing data when storage providers fail. 

The marketplace is defined by smart contracts on an EVM-compatible blockchain, 
and this specification describes interactions for various network roles.

#### Deliverables 

- Raw RFC  
- Draft RFC (potentially)
