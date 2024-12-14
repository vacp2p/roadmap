---
title: de-mls Testnet
tags:
  - "2024q4"
  - "acz"
  - "ift"
draft: false
description: "Implementation of a de-mls testnet, extending the previous poc and writing the corresponding RFC"

---

`vac:acz:ift:2024q4-de-mls-testnet`

Implementation of a de-mls testnet, extending the previous poc and writing the corresponding RFC
## Description

de-mls is a decentralized scalable E2EE secure group messaging with Ethereum authentication. 

With the de-mls-poc commitment, 

we will reinforce the Conduit of Expertise narrative by:
* Develop the foundational framework for a decentralized, scalable messaging application 
authenticated through Ethereum, designed to support a large user base within the IFT ecosystem.

We will also strengthen the Premier Research Destination narrative by:
* Develop a standardized decentralized messaging application with Ethereum authentication 
by providing a well-structured RFC and a proof of concept (PoC) that demonstrates its practical functionality 
within the ecosystem. 
This will allow teams and organizations to build their own messaging applications while 
benefiting from these features.
* Create a proposal for the Ethereum Foundation (EF) to apply for EF grants to promote the testnet and 
gain support from the Ethereum ecosystem.


## Task List

### de-MLS RFC

* fully qualified name: `vac:acz:ift:2024q4-de-mls-testnet:de-mls-rfc`
* owner: Ramses
* status: in progress (60%)
* start-date: 2024/10/07
* end-date: 2024/11/04

#### Description 
Creation of a detailed RFC describing the protocol for a decentralized verison of MLS. 
This proposal will include a login phase inspired by SIWE avoiding the centralized components of the latter. 

#### Deliverables 

Several PRs to the deMLS repository

### de-MLS Presentation

* fully qualified name: `vac:acz:ift:2024q4-de-mls-testnet:presentation`
* owner: Ramses
* status: done
* start-date: 2024/10/14
* end-date: 2024/10/23

#### Description 
Creation of a presentation of de-MLS for IFT research call. 

#### Deliverables 

A presentation that describes the RFC in terms of technical, usage, and implementation point of view in 
[notion](https://www.notion.so/Applied-Cryptography-ZK-870520f131954b90b1837ec4749f890f?pvs=4#12d8f96fb65c80f49f11e8e6fe7fc974)


### Login Specs

* fully qualified name: `vac:acz:ift:2024q4-de-mls-testnet:login-specs`
* owner: Ramses
* status: on-hold

* start-date: 2024/10/14
* end-date: 2024/10/28

#### Description

Specification of scalable, implementable, and decentralized authentication mechanism as login phase for the RFC. 

This task is holding for now to determine the details.

#### Deliverables

A specification [document](https://www.notion.so/WiP-SimpleLogin-protocol-1298f96fb65c8090adb2faeba7ecfb31) for scalable, implementable, and decentralized authentication mechanism as login phase for the RFC.


### EF Grant Application

* fully qualified name: `vac:acz:ift:2024q4-de-mls-testnet:ef-application`
* owner: Ugur
* status: moved to 2025q1 (30%)
* start-date: 2024/10/14
* end-date: 2024/11/18

#### Description

Creating the grant application file including the answers of EF questions and having meetings in 
office hours for possible questions.  

This task is moved to 2025q1 since the we need to obtain the PoC first. 

#### Deliverables

An submitting EF grants by the application document and keeping an eye the process.

### Testnet API

* fully qualified name: `vac:acz:ift:2024q4-de-mls-testnet:testnet-api`
* owner: Ekaterina
* status: in progress (30%)
* start-date: 2024/10/21
* end-date: 2024/11/11

#### Description

Expand the [PoC](https://github.com/vacp2p/de-mls) by replacing Redis to Waku node for 1-1 and group chat and 
testing some cases such as queue commit and concurrent application message. 
Lastly, adding the login phase to testnet application. 

#### Deliverables

Several PRs to the repository that will be created with testnet API implementation for de-mls tesnet as follows: 
* Replacing Redis with Waku nodes 
* Test modules including queue commit and concurrent messages 
* Adding login phase as the researchers determined

### Deployment Testnet

* fully qualified name: `vac:acz:ift:2024q4-de-mls-testnet:deployment-testnet`
* owner: Ekaterina
* status: not started
* start-date: 2024/11/18
* end-date: 2024/12/02

#### Description

Integrate the testnet API to smart contracts for de-mls testnet by conducting several E2E tests before the release.  

#### Deliverables

Several PRs to the de-mls testnet repository as follows: 
* Gathering all the components of testnet together such as API, on-chain components, 
and login mechanism. 
* Test module that checks E2E executions including adding/removing users. 
* Taking benchmarks such as group creation time with different numbers of users in a group. 

### Blogpost de-mls over Waku

* fully qualified name: `vac:acz:ift:2024q4-de-mls-testnet:blogpost-de-mls-over-waku`
* owner: Ekaterina
* status: not started
* start-date: 2024/12/02
* end-date: 2024/12/09

#### Description

Writing a blogpost about a de-mls messaging application over the waku nodes. 

#### Deliverables

A blogpost to [vac-dev](https://vac.dev/rlog/)

### DCGKA

* fully qualified name: `vac:acz:ift:2024q4-de-mls-testnet:dcgka`
* owner: Ramses
* status: not started
* start-date: 2024/11/18
* end-date: 2024/12/01

#### Description 
 Creation of a detailed RFC describing an alternative approach using DCGKA for a decentralized communication protocol. 
 This approach avoid the use of smart contracts and includes a login phase inspired by SIWE. 

#### Deliverables 

Several PRs to the DCGKA repository.

 