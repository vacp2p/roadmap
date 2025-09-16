---
title: de-MLS testnet
tags:
  - "2025q4"
  - "acz"
  - "ift"
draft: false
description: "Releasing de-MLS with the multi-steward support and ethereum authentication mechanism."

---

`vac:acz:ift:2025q4-de-mls-tesnet`

## Description
This commitment involves releasing de-MLS poc with the multi-steward configurations.
The process includes presenting the findings such as MLS over Waku and benchmarking,
then achive better iteration for the EF grant.

### Background
de-MLS is a decentralized, scalable, end-to-end encrypted (E2EE)
group messaging application with Ethereum-based authentication.
The primary goal of this project is to develop a comprehensive
and mature RFC that outlines decentralized, secure, and scalable group key generation, 
designed to accommodate large numbers of users within a single group.
 
During 2025q3, we released multi-steward de-MLS RFC including consensus implementation.
The implementation plan for this quarter is to release multi-steward with single consensus
version with ethereum authentication factor by operating across the Waku network. 

### Narratives
we will reinforce the Conduit of Expertise narrative by:
* Develop the foundational framework for a decentralized, scalable messaging application 
* Research and implement the scalable and decentralized consensus mechanism.

We will also strengthen the Premier Research Destination narrative by:
* Develop a standardized decentralized messaging application over the Waku network, by providing a well-structured RFC and a proof of concept (PoC) that demonstrates its base functionality within the ecosystem. This will allow teams and organizations to build their own messaging applications while benefiting from these features.
* Create a proposal for the Ethereum Foundation (EF) to apply for EF grants to promote the project and gain support from the Ethereum ecosystem.

## Task List

### Maintain de-MLS RFC with multi stewards 

* fully qualified name: `vac:acz:ift:2025q4-de-mls-tesnet:multi-steward-rfc`
* owner: Ugur
* status: not started
* start-date: 2025/10/25
* end-date: 2025/11/25

#### Description

Maintain and develop the decentralized MLS RFC with adressing feedbacks.
The RFC needs to contain concrete flow, and explaination.   

#### Deliverables

* PR to vacp2p/rfc-index repo with related updates.

### Multi-steward integration

* fully qualified name: `vac:acz:ift:2025q4-de-mls-tesnet:multi-steward-integration`
* owner: Ekaterina
* status: not started
* start-date: 2025/10/01
* end-date: 2025/11/01

#### Description

The multi-steward settings allows de-MLS that multiple steward manages the group
changes to protect single point of failure, better availability and decentralization.

#### Deliverables

* A PR to the [de-MLS repository](https://github.com/vacp2p/de-mls) 
containing update of message processing 

### de-mls maintance

* fully qualified name: `vac:acz:ift:2025q4-de-mls-tesnet:de-mls-maintaining`
* owner: Ekaterina
* status: not started 
* start-date: 2025/06/30
* end-date: 2025/09/30

#### Description

This task encompasses all maintenance updates for de-mls, including CI updates,
testing, small issues and the creation of future issues.

#### Deliverables

A set of PRs and issues to  [de-MLS repository](https://github.com/vacp2p/de-mls)