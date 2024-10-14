---
title: Marketplace and Client 2024q4
tags:
  - 2024q4
  - rfc
  - codex
draft: false
description: Write raw RFCs based on the documentation for Codex Marketplace and Codex Client through discussion and support.
---

`ift:rfc:codex:marketplace-and-client-2024q4`

Provide the service of writing raw RFCs
based on the documentation for Codex Marketplace and Codex Client
through discussion and support.

## Description

This commitment revolves around delivering of raw RFCs for Codex 
Marketplace and Codex Client via helping with discussion,
supporting the team and inquiring about project updates.
The goal is to establish an RFC culture within the Codex ecosystem
to standardize specifications across all IFT ecosystems.

The initial focus will be on Codex Client (Erasure Coding), Codex Manifest, and 
Codex Marketplace. Codex Marketplace is a focal point within the ecosystem, and 
Erasure Coding and Manifest are referenced within it. These may become separate 
RFCs, though it's still open for discussion.

Through our efforts in driving and supporting discussions with the Codex team, 
we aim to achieve:

- Raw RFCs  

**Alignment with VAC Narratives:**

- Through the service of writing raw RFCs with having the original documentation and codebase as the source,
the VAC RFC team aims to be a repository for RFCs across all IFT projects.
- We aim to encourage projects to submit RFCs to the team of rfc-editors.
- The long-term goal is to have the broader web3 community use our RFCs within 
  their projects, similar to how [IETF](https://www.ietf.org/) operates.

## Task List

### Codex Client - Erasure Coding

- Fully qualified name: `ift:rfc:codex:marketplace-and-client:erasure-coding`
- Owner: jimstir
- Status: 50%
- Start date: 2024/10/01
- End date: 2024/11/15

#### Description 

This task includes writing a raw RFC based on the specifications
that outline the erasure coding technique used in the Codex protocol.
The Codex client encodes datasets presented to the marketplace
using this technique.
Storage providers agree to store encoded datasets for a period, 
and client nodes can restore datasets abandoned by providers.
Validator nodes detect missing data.
#### Deliverables 

- Raw RFC  

### Codex Client - Manifest

- Fully qualified name: `ift:rfc:codex:marketplace-and-client:manifest`
- Owner: jimstir
- Status: not started
- Start date: 2024/10/01
- End date: 2024/11/15

#### Description 

This task includes writing a raw RFC based on the specification
that describe the parameters used in the manifest
for Codex client applications.
The manifest encodes datasets within a Codex client node.

#### Deliverables 

- Raw RFC  

### Codex Marketplace

- Fully qualified name: `ift:rfc:codex:marketplace-and-client:marketplace`
- Owner: jimstir
- Status: not started
- Start date: 2024/12/15
- End date: 2024/12/29

#### Description 

This task includes auditing a raw RFC of the Codex Marketplace
based on the submission by the Codex team.
The Marketplace is crucial to the network, enabling data persistence
by facilitating interactions among participants.
It provides mechanisms for enforcing agreements
and repairing data when storage providers fail. 

The marketplace is defined by smart contracts on an EVM-compatible blockchain, 
and this specification describes interactions for various network roles.

#### Deliverables 

- Raw RFC  