---
title: Waku RLN Relay
tags:
  - "2024q4"
  - "acz"
  - "waku"
draft: false
description: "Providing implementation support to Waku RLN relay for solving the related issues"

---

`vac:acz:waku:waku-rln-relay`

Providing implementation support to Waku RLN relay for solving the related issues
## Description

ACZ offers implementation support to Waku, for solving time-box issues regarding the RLN relay. 

By utilizing the Nescience Consulting commitment, 

we will reinforce the Conduit of Expertise narrative by:
* Resolving the issues that could potentially hinder Waku operations.
* Improve communication between the ACZ and Waku teams. 

We will also strengthen the Premier Research Destination narrative by: 
* Offering solutions for the latest public issues 
that could contribute to the ecosystem 
and support projects being built on the Waku network. 

## Task List

### Adding Timestamp

* fully qualified name: `vac:acz:waku:waku-rln-relay:adding-timestamp`
* owner: Ekaterina
* status: started (0%)
* start-date: 2024/10/21
* end-date: 2024/10/28

#### Description

Adding timestamp based verification feature for RLN Regarding 
[the issue](https://github.com/waku-org/nwaku/issues/2972). 
This task is also referred to in the [Zerokit v0.6](https://roadmap.vac.dev/acz/ift/zerokit-v0-6). 

#### Deliverables

A PR to Zerokit [repository](https://github.com/vacp2p/zerokit)

### Deprecate Tree Sync 

* fully qualified name: `vac:acz:waku:waku-rln-relay:deprecate-tree-sync`
* owner: Ekaterina
* status: not started
* start-date: 2024/10/28
* end-date: 2024/11/04

#### Description

Retrieving the merkleProofElements directly 
from the smart contract and utilizing them to generate RLN proofs, 
eliminating the need for external sources or manual calculation of proof elements, 
regarding to [the issue](https://github.com/waku-org/nwaku/issues/2924).

#### Deliverables

A PR to the related repository.