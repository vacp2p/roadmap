---
title: de-MLS Multi Admin
tags:
  - "2025q1"
  - "acz"
  - "ift"
draft: false
description: "involves finalizing the de-MLS RFC with multi-admin support, 
implementing by extending the single admin approach with on-chain admin consensus, 
and also submitting to the EF grant program with a messaging application project 
that introduces decentralization, censorship resistance, and DAO coordination, or DeFi alerts"

---

`vac:acz:ift:2025q1-de-mls-multi-admin`

involves finalizing the de-MLS RFC with multi-admin support, 
implementing by extending the single admin approach with on-chain admin consensus, 
and also submitting to the EF grant program with a messaging application project 
that introduces decentralization, censorship resistance, and DAO coordination, or DeFi alerts
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
* status: on-hold (70%)
* start-date: 2025/01/06
* end-date: 2025/01/20

#### Description

This task is scheduled to be completed in 2025q2 due to the architectural change.

Writing a blog post about implementation details of single admin de-MLS with Waku node 
as delivery service based on [this PR](https://github.com/vacp2p/de-mls/pull/29)     

#### Deliverables

A blogpost to [vac.dev/rlog/](https://vac.dev/rlog/)
 
### Update de-MLS RFC with multi admins 

* fully qualified name: `vac:acz:ift:2025q1-de-mls-multi-admin:multi-admin-rfc`
* owner: Ugur
* status: on-hold (30%)
* start-date: 2025/01/13
* end-date: 2025/01/27

#### Description

This task is scheduled to be completed in 2025q2 due to building consensus RFC has just finished.

Update and reorganize the RFC with the single and multi admin options.  

#### Deliverables

* PR to vacp2p/rfc-index repo with related updates. 

### Update Waku Node Connection

* fully qualified name: `vac:acz:ift:2025q1-de-mls-multi-admin:waku-node-connection`
* owner: Ekaterina
* status: done
* start-date: 2025/01/20
* end-date: 2025/02/24

#### Description

The current version of the Waku Node setting, and subscribing to content topics 
entails receiving the same message multiple times. 
The task plans to fix this and also add the ability to connect more than one node. 
Also rust bindings have been updated over time and will be moving to the current version.

This task's end-date is expanded due to the blocker from the waku Rust bindings. 

#### Deliverables

A [PR](https://github.com/vacp2p/de-mls/pull/32) to the 
[de-MLS](https://github.com/vacp2p/de-mls) repository 
updating the Waku node connection and enabling multiple node usage.

### Benchmark Coverage

* fully qualified name: `vac:acz:ift:2025q1-de-mls-multi-admin:benchmark-coverage`
* owner: Ekaterina
* status: done
* start-date: 2025/01/20
* end-date: 025/01/27

#### Description

Expand benchmark coverage in the [de-MLS](https://github.com/vacp2p/de-mls) repository. 
Identify untested scenarios, document them, and implement corresponding benchmarks.

#### Deliverables
[A PR](https://github.com/vacp2p/de-mls/pull/31) to the [de-MLS](https://github.com/vacp2p/de-mls) repository with 

* A document outlining benchmark scenarios.
* PRs with benchmark tests for uncovered scenarios.

### Processing Of Key Packages In Batch 

* fully qualified name: `vac:acz:ift:2025q1-de-mls-multi-admin:batch-key-package`
* owner: Ekaterina
* status: done
* start-date: 2025/01/27
* end-date: 2025/02/10

#### Description

Expand the [de-MLS](https://github.com/vacp2p/de-mls) codebase by implementing multi-admin support. 
The implementation with a single admin allowed for the instantaneous processing of requests to join the group. 
When moving to multiple admins, the ability to collect requests in batches and then process them as one should be added. 

#### Deliverables

[A PR](https://github.com/vacp2p/de-mls/pull/34) to the [de-MLS](https://github.com/vacp2p/de-mls) repository, 
updating the API for handling key packages from users 
before joining the group not in each coming message but once in the epoch. 

### Test Deployment

* fully qualified name: `vac:acz:ift:2025q1-de-mls-multi-admin:test-deployment`
* owner: Ekaterina
* status: on-hold
* start-date: 2025/02/03
* end-date: 2025/02/10

#### Description

This task is re-scheduled in 2025q2 due to the architectural changes.

Set up test deployment for the [de-MLS](https://github.com/vacp2p/de-mls) repository. 
Docker containers have been made to run PoCs, 
but they assume a single node operation and do not run nodes within themselves.

#### Deliverables
A PR to the [de-MLS](https://github.com/vacp2p/de-mls) repository with 
* Docker configurations for deployment and testing.
* Documentation for test deployment setup.

### Extend API To Multiple Admin

* fully qualified name: `vac:acz:ift:2025q1-de-mls-multi-admin:extend-api`
* owner: Ekaterina
* status: on hold
* start-date: 2025/02/10
* end-date: 2025/03/03

#### Description

Expand the [de-MLS](https://github.com/vacp2p/de-mls) codebase by implementing multi-admin support. 
In preparation for working with multiple admins, 
extend API for the following processes: processing invitations to a group, applying commits, 
and preparing a separate channel for exchanging messages between admins. 

This task is postponed to the 2025q2 since Zerokit was prioritized.  

#### Deliverables

A PR to the [de-MLS](https://github.com/vacp2p/de-mls) repository 
updating the API for separate commit and proposal messages. 

### CI Setup

* fully qualified name: `vac:acz:ift:2025q1-de-mls-multi-admin:ci-setup`
* owner: Ekaterina
* status: on hold
* start-date: 2025/02/10
* end-date: 2025/02/17

#### Description

This task is re-scheduled in 2025q2 due to the priority changes.

Set up continuous integration for the [de-MLS](https://github.com/vacp2p/de-mls) repository, 
including automated testing and code validation. 

#### Deliverables
A PR to the [de-MLS](https://github.com/vacp2p/de-mls) repository 
with a new CI pipeline for the repository that includes the waku node.

### Consensus Research

* fully qualified name: `vac:acz:ift:2025q1-de-mls-multi-admin:consensus-research`
* owner: Ugur
* status: done
* start-date: 2025/02/10
* end-date: 2025/02/24

#### Description

Conducting research on-chain and off-chain solutions for multi-admin consensus mechanisms. 
   
#### Deliverables

- [A notion page](https://www.notion.so/Hashgraph-based-Scalable-Consensus-1b18f96fb65c808aacf0fe3c50aa36e1) 
that offers a few solutions that are feasible to implement.  

### Deployment

* fully qualified name: `vac:acz:ift:2025q1-de-mls-multi-admin:deployment`
* owner: Ekaterina
* status: on hold
* start-date: 2025/03/06
* end-date: 2025/03/24

#### Description

Set up final deployment for the [de-MLS](https://github.com/vacp2p/de-mls) repository, 
including Docker configurations and automation.

This task is postponed to 2025q2 since related tasks were postponed by Zerokit being prioritized.

#### Deliverables
A PRs to the [de-MLS](https://github.com/vacp2p/de-mls) repository with bug fixes and code improvements.

### EF Grant Application

* fully qualified name: `vac:acz:ift:2025q1-de-mls-multi-admin:ef-application`
* owner: Ugur
* status: on hold
* start-date: 2025/03/06
* end-date: 2025/03/24

#### Description

Finalize the grant application file including the answers to EF questions and start the process
with having meetings during office hours for possible questions.  

This task is postponed to 2025q2 because related tasks must be completed first.

#### Deliverables

Submitting EF grants using the application document and keeping an eye on the process.