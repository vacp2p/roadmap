---
title: Think tank
tags:
  - "2024q4"
  - "acz"
  - "ift"
draft: false
description: "Publishing a reviewing document for the cryptography modules of IFT projects"

---

`vac:acz:ift:think-tank`

Publishing a reviewing document for the cryptography modules of IFT projects
## Description

Many IFT projects utilize the cryptography as one of the components their architecture. 
As ACZ team, we collect all the cryptographical primitives into single commitment, 
review and compare them to detect potential 
improvable and strong aspects.

By utilizing the think-tank commitment, 
we will reinforce the Conduit of Expertise narrative by:
* Create a document describing the review and compare cryptographic modules for each of Waku, 
Status, Codex, and Nimbus.
* Share the common know-how with the relevant project if needed.

We will also strengthen the Premier Research Destination narrative by: 
* Present the significant cryptographic findings on the [VAC forum](https://forum.vac.dev/) 
to initiate discussions and contribute to the benefit of the ecosystem.


## Task List

### Crypto Think Tank 

* fully qualified name: `vac:acz:ift:think-tank:crypto-think-tank`
* owner: Ramses
* status: done
* start-date: 2024/10/21
* end-date: 2024/11/04

#### Description 
Code review for a KZG implementation performed by Waku and Nomos.

#### Deliverables 

[A notion page](https://www.notion.so/WiP-Code-review-Nomos-library-1068f96fb65c80338499c9f06e702b41) 
containing the review by Ramses

### ZK Consulting Codex 1

* fully qualified name: `vac:acz:ift:think-tank:zk-consulting-codex-1`
* owner: Marvin
* status: in progress (10%)
* start-date: 2024/10/07
* end-date: 2024/12/02

#### Description 

On going explorative, provide notes on zero-knowledge techniques from the literature that seem relevant to Codex's future needs.

#### Deliverables 

* Maintain notes on commitment schemes that look promising for Codex's needs
* Investigate folding techniques and wrappers that may be useful for aggregation of proofs for Codex.

### ZK Consulting Codex 2

* fully qualified name: `vac:acz:ift:think-tank:zk-consulting-codex-2`
* owner: Marvin
* status: in progress (13%)
* start-date: 2024/10/07
* end-date: 2024/12/02

#### Description 

Provide theoretical assistance in making the [dynamic proposal](https://hackmd.io/M6uwhb0eQh2bIh5_O6AX7Q?view) concrete. 
This is the candidate for the future of Codex's design beyond the current testnet.

#### Deliverables 

* Provide theoretical methods for aggregation (in node) with space/time tradeoff analysis.
* Provide theoretical construction to fix current issues with row updates in dynamic proposal.
* Provide some computational benchmarks for various parameter sizes to help guide Codex's adoption decisions.