---
title: de-MLS Multi Admin
tags:
  - "2025q1"
  - "acz"
  - "ift"
draft: false
description: "involves finalizing the de-MLS RFC with multi-admin support, 
implementing by extending the single admin approach with on-chain admin consensus, 
and exploring further topic for the EF grant"

---

`vac:acz:ift:2025q1-de-mls-multi-admin`

involves finalizing the de-MLS RFC with multi-admin support, 
implementing by extending the single admin approach with on-chain admin consensus, 
and exploring further topic for the EF grant
## Description

This commitment involves completing the de-MLS RFC by incorporating 
multi-administrator configurations both onchain and offchain settings and implementing de-MLS 
with a multi-admin setup over Waku network, delegating admin consensus to on-chain components. 
The process includes presenting the findings such as MLS over Waku and benchmarking, 
then applying for the EF grant.

### Background

de-MLS is a decentralized, scalable, end-to-end encrypted (E2EE) group messaging application 
with Ethereum-based authentication. 
The primary goal of this project is to develop a comprehensive and mature RFC that outlines 
decentralized, secure, and scalable group key generation, 
designed to accommodate large numbers of users within a single group.

During 2024q4, we identified the centralized aspects of the RFC 
and the importance of a multi-admin configuration for achieving true decentralization. 
Also we achieved the first step of implementation called single-admin over Waku node proof of concept implementation. 
For implementation plan for this quarter is to extend the initial single-Waku-node approach 
to a multi-admin configuration operating across the Waku network. 

### Narratives

we will reinforce the Conduit of Expertise narrative by:
* Develop the foundational framework for a decentralized, scalable messaging application 
authenticated through Ethereum, designed to support a large user base within the IFT ecosystem.

We will also strengthen the Premier Research Destination narrative by:
* Develop a standardized decentralized messaging application over Waku network
by providing a well-structured RFC and a proof of concept (PoC) that demonstrates its base functionality 
within the ecosystem. 
This will allow teams and organizations to build their own messaging applications while 
benefiting from these features.
* Create a proposal for the Ethereum Foundation (EF) to apply for EF grants to promote the project and 
gain support from the Ethereum ecosystem.

## Task List

### Blogpost de-mls over Waku

* fully qualified name: `vac:acz:ift:2025q1-de-mls-multi-admin:blogpost-de-mls-over-waku`
* owner: Ekaterina
* status: started (10%)
* start-date: 2025/01/06
* end-date: 2025/01/20

#### Description

Writing a blog post about implementation details of single admin de-MLS with Waku node 
as delivery service based on [this PR](https://github.com/vacp2p/zerokit/pull/273)     

#### Deliverables

A blogpost to [vac-dev](https://vac.dev/rlog/)
 
### Update de-MLS RFC with multi admins 

* fully qualified name: `vac:acz:ift:2025q1-de-mls-multi-admin:multi-admin-rfc`
* owner: Ugur
* status: not started
* start-date: 2025/01/13
* end-date: 2025/01/27

#### Description

Update and reorganize the RFC with the single and multi admin options.  

#### Deliverables

* PR to vacp2p/rfc-index repo with related updates. 