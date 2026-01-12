---
title: Implement NSSA Attestation
tags:
  - "2026q1"
  - "sc"
  - "logos"
draft: false
description: Implement NSSA attestation.
---

`vac:sc:logos:2026q1-implement-nssa-attestation`

## Description

Implement an attestation program for the Nescience State Separation Architecture (NSSA) that enables both transparent and private credential issuance and verification.
Similar to Solana's attestation service, this system will allow organizations to issue verifiable credentials, but with NSSA's unique privacy capabilities.

The attestation program must support two modes of operation:
1. **Transparent attestations** with explicit schemas for public credentials where data structure and content visibility is acceptable
2. **Private attestations** leveraging zero-knowledge proofs where credential data remains private while still being verifiable

The system will support key roles including issuers who create and issue credentials,
holders who receive and store attestations, and verifiers who validate credentials without necessarily learning their contents in private mode.

This commitment includes researching existing attestation systems and ZK approaches, designing the NSSA-specific architecture for both transparent and private attestations,
and implementing the smart contracts with comprehensive testing and documentation.

## Task List

### Research attestation systems and ZK approaches

* fully qualified name: `vac:sc:logos:2026q1-implement-nssa-attestation:research`
* owner: TBD
* status: not started
* start-date: 2026/01/01
* end-date: 2026/01/31

#### Description

Research existing attestation systems and zero-knowledge credential protocols to understand best practices for both transparent and private credential issuance.
Analyze the Solana Attestation Service for schema-based attestations and ZK credential systems for private attestations.
Identify design patterns, security considerations, and privacy guarantees applicable to NSSA.

#### Deliverables

- [ ] Research document outlining findings for both transparent and private attestations
- [ ] Security considerations and threat model documentation
- [ ] Privacy guarantees and trade-offs analysis

### Design NSSA attestation architecture

* fully qualified name: `vac:sc:logos:2026q1-implement-nssa-attestation:design`
* owner: TBD
* status: not started
* start-date: 2026/02/01
* end-date: 2026/02/14

#### Description

Design the dual-mode attestation program architecture for NSSA.
For transparent mode: define attestation schema structure, credential formats, and public verification flows.
For private mode: design zero-knowledge proof circuits, private credential structures, and privacy-preserving verification mechanisms.
Define the on-chain data structures for both modes and off-chain integration requirements.

#### Deliverables

- [ ] Architecture diagrams for transparent and private attestation flows
- [ ] Schema definitions for transparent attestations
- [ ] API design for issuer, holder, and verifier interactions
- [ ] Visual representations of attestation flows

### Implement attestation smart contracts

* fully qualified name: `vac:sc:logos:2026q1-implement-nssa-attestation:implementation`
* owner: TBD
* status: not started
* start-date: 2026/02/15
* end-date: 2026/03/31

#### Description

Implement the NSSA attestation smart contracts supporting both transparent and private modes based on the approved design.
For transparent attestations: implement schema creation, credential issuance with explicit data, and public verification.
For private attestations: implement ZK proof verification, private credential issuance, and privacy-preserving verification flows.
Include lifecycle management, expiration handling, and revocation mechanisms for both modes.
Ensure comprehensive test coverage and documentation.

#### Deliverables

- [ ] Smart contract implementation for transparent private ZK-based attestations
- [ ] Comprehensive test suite covering both modes and edge cases
- [ ] Integration tests for issuer, holder, and verifier flows
- [ ] PRs with code reviews
