---
title: de-MLS Multi Admin
tags:
  - "2025q1"
  - "acz"
  - "ift"
draft: false
description: "involves finalizing the de-MLS RFC with multi-admin support, 
implementing by extending the single admin approach with on-chain admin consensus, 
and exploring further topics for the EF grant"

---

`vac:acz:ift:2025q1-de-mls-multi-admin`

involves finalizing the de-MLS RFC with multi-admin support, 
implementing by extending the single admin approach with on-chain admin consensus, 
and exploring further topics for the EF grant
## Description

This commitment involves completing the de-MLS RFC by incorporating 
multi-administrator configurations both onchain and offchain settings and implementing de-MLS 
with a multi-admin setup over the Waku network, delegating admin consensus to on-chain components. 
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
Also, we achieved the first step of implementation called single-admin 
over the Waku node proof of concept implementation. 
The implementation plan for this quarter is to extend the initial single-Waku-node approach 
to a multi-admin configuration operating across the Waku network. 

### Narratives

we will reinforce the Conduit of Expertise narrative by:
* Develop the foundational framework for a decentralized, scalable messaging application 
authenticated through Ethereum, designed to support a large user base within the IFT ecosystem.

We will also strengthen the Premier Research Destination narrative by:
* Develop a standardized decentralized messaging application over the Waku network
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
* status: started (60%)
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
* status: started (0%)
* start-date: 2025/01/13
* end-date: 2025/01/27

#### Description

Update and reorganize the RFC with the single and multi admin options.  

#### Deliverables

* PR to vacp2p/rfc-index repo with related updates. 

### Update Waku Node Connection

* fully qualified name: `vac:acz:ift:2025q1-de-mls-multi-admin:waku-node-connection`
* owner: Ekaterina
* status: started
* start-date: 2025/01/20
* end-date: 2025/01/27

#### Description

Update the connection to Waku nodes according to the new 
bindings updates and allow multiple nodes to be used. 

#### Deliverables

A PR to the [de-MLS](https://github.com/vacp2p/de-mls) repository 
updating the Waku node connection and enabling multiple node usage.

### Benchmark Coverage

* fully qualified name: `vac:acz:ift:2025q1-de-mls-multi-admin:benchmark-coverage`
* owner: Ekaterina
* status: not started
* start-date: 2025/01/20
* end-date: 025/01/27

#### Description

Expand benchmark coverage in the [de-MLS](https://github.com/vacp2p/de-mls) repository. 
Identify untested scenarios, document them, and implement corresponding benchmarks.

#### Deliverables
A PR to the [de-MLS](https://github.com/vacp2p/de-mls) repository with 

* A document outlining benchmark scenarios.
* PRs with benchmark tests for uncovered scenarios.

### Processing Of Key Packages In Batch 

* fully qualified name: `vac:acz:ift:2025q1-de-mls-multi-admin:batch-key-package`
* owner: Ekaterina
* status: not started
* start-date: 2025/01/27
* end-date: 2025/02/10

#### Description

Expand the [de-MLS](https://github.com/vacp2p/de-mls) codebase by implementing multi-admin support. 
Update key package handling to process packages in batches, enabling proposal formation from different admins.

#### Deliverables

This is a PR to the [de-MLS](https://github.com/vacp2p/de-mls) repository, 
updating the API for handling key packages from users 
before joining the group not in each coming message but once in the epoch. 

### Test Deployment

* fully qualified name: `vac:acz:ift:2025q1-de-mls-multi-admin:test-deployment`
* owner: Ekaterina
* status: not started
* start-date: 2025/02/03
* end-date: 2025/02/10

#### Description

Set up test deployment for the [de-MLS](https://github.com/vacp2p/de-mls) repository, 
including Docker configurations and automation.

#### Deliverables
A PR to the [de-MLS](https://github.com/vacp2p/de-mls) repository with 
* Docker configurations for deployment and testing.
* Documentation for test deployment setup.

### Extend API To Multiple Admin

* fully qualified name: `vac:acz:ift:2025q1-de-mls-multi-admin:extend-api`
* owner: Ekaterina
* status: not started
* start-date: 2025/02/10
* end-date: 2025/03/03

#### Description

Expand the [de-MLS](https://github.com/vacp2p/de-mls) codebase 
by implementing multi-admin support—update to commit handling to support more than one admin. 
Allow more than one admin to send the admin key into the welcome channel and process an incoming key package. 

#### Deliverables

A PR to the [de-MLS](https://github.com/vacp2p/de-mls) repository 
updating the API for separate commit and proposal messages. 

### CI Setup

* fully qualified name: `vac:acz:ift:2025q1-de-mls-multi-admin:ci-setup`
* owner: Ekaterina
* status: not started
* start-date: 2025/02/10
* end-date: 2025/02/17

#### Description

Set up continuous integration for the [de-MLS](https://github.com/vacp2p/de-mls) repository, 
including automated testing and code validation. 

#### Deliverables
A PR to the [de-MLS](https://github.com/vacp2p/de-mls) repository 
with a new CI pipeline for the repository that includes the waku node.

### Consensus Research

* fully qualified name: `vac:acz:ift:2025q1-de-mls-multi-admin:consensus-research`
* owner: Ugur
* status: not started
* start-date: 2025/02/10
* end-date: 2025/02/24

#### Description

Conducting research on-chain and off-chain solutions for multi-admin consensus mechanisms. 
   
#### Deliverables

A notion page that offers a few solutions that are feasible to implement.  

### Deployment

* fully qualified name: `vac:acz:ift:2025q1-de-mls-multi-admin:deployment`
* owner: Ekaterina
* status: not started
* start-date: 2025/03/06
* end-date: 2025/03/24

#### Description

Set up final deployment for the [de-MLS](https://github.com/vacp2p/de-mls) repository, 
including Docker configurations and automation.

#### Deliverables
A PRs to the [de-MLS](https://github.com/vacp2p/de-mls) repository with bug fixes and code improvements.

### EF Grant Application

* fully qualified name: `vac:acz:ift:2025q1-de-mls-multi-admin:ef-application`
* owner: Ugur
* status: not started
* start-date: 2025/03/06
* end-date: 2025/03/24

#### Description

Finalize the grant application file including the answers to EF questions and start the process
with having meetings during office hours for possible questions.  

#### Deliverables

Submitting EF grants using the application document and keeping an eye on the process.