---
title: Discovery
tags:
  - "2025q4"
  - "acz"
  - "ift"
draft: false
description: "Specifying disc-NG and releasing a document that collects the requirements of discovery"

---
 
`vac:acz:ift:2025q4-discovery`

Specifying a KAD-DHT–based, disc-NG–like Logos discovery capability 
and releasing a document that collects the requirements of discovery
## Description

This commitment entails specifying a KAD-DHT–based, disc-NG–like Logos discovery capability 
specification with a focus on implementability (see [the paper](https://sonnino.com/papers/disc-ng.pdf));
we will also collect requirements and assess their suitability for IFT projects.

### Narratives

By utilizing discovery exploration commitment, 
We will reinforce the Conduit of Expertise narrative by:
* Providing the KAD-DHT–based disc-NG-like RFC that will be tailored for Logos applications. 

We will also strengthen the Premier Research Destination narrative by:
* Provides open-source KAD-DHT–based disc-NG-like RFC information to the community.

## Task List

### Draft RFC

* fully qualified name: `vac:acz:ift:2025q4-discovery:draft-RFC`
* owner: Arunima
* status: started (%10)
* start-date: 2025/10/01
* end-date: 2025/10/30

#### Description

This task involves specifying disc-NG-like LOGOS discovery capabilities on top of KAD-DHT
(see [the paper](https://sonnino.com/papers/disc-ng.pdf)) in an implementable way,
extracting key components such as the registrar and advisor and drafting them into an RFC;
once the draft RFC is assembled, the task also includes preparing the final RFC
as a pull request by incorporating review feedback.

#### Deliverables

* A notion document contains a draft RFC with its feedback.

### Registrar Module

* fully qualified name: `vac:acz:ift:2025q4-discovery:registrar-module`
* owner: Arunima
* status: started (%0)
* start-date: 2025/10/20
* end-date: 2025/10/27

#### Description

In this task, the modular registrar module will be implemented in Golang to handle node registration,
admission policies, and identity management.
The module will manage how new participants join the network,
enforce admission control rules derived from the RFC, and maintain metadata about registered nodes.
The implementation will include validation logic, registration lifecycle handling,
and interactions with the core routing layer.
The goal is to ensure controlled participation and maintain the stability and trust of the system.  
The task is complete when nodes can register, be validated, and interact
with the network under enforced admission control rules.

#### Deliverables

* A PR to the [vacp2p/disc-NG](https://github.com/vacp2p/disc-ng/) repo.

### Advertiser Module

* fully qualified name: `vac:acz:ift:2025q4-discovery:advertiser-module`
* owner: Arunima
* status: started
* start-date: 2025/10/27
* end-date: 2025/11/03

#### Description

This task involves developing the advertiser component, which is responsible for broadcasting
and maintaining service or capability advertisements across the network.
The module will manage how nodes announce their presence and update their advertised information over time.
It will interact closely with both the registrar and routing infrastructure to ensure
that advertisements are discoverable and correctly propagated.
Emphasis will be placed on efficient dissemination, freshness of information, and resilience to network churn.  
The task is complete when advertisements can be created,
updated, and distributed correctly through the routing layer.

#### Deliverables

* A PR to the [vacp2p/disc-NG](https://github.com/vacp2p/disc-ng/) repo.

### Discoverer Module

* fully qualified name: `vac:acz:ift:2025q4-discovery:discoverer-module`
* owner: Arunima
* status: started
* start-date: 2025/11/03
* end-date: 2025/11/10

#### Description

Here, the discoverer module will be implemented to enable nodes
to search for and locate advertised services or peers in the network.
It will interpret discovery queries, match them against active advertisements,
and handle query routing through the established infrastructure.
The module should also implement caching and fallback mechanisms to optimize performance.
The focus will be on correctness, minimal latency in lookups,
and adherence to the discovery semantics outlined in the RFC.  
The task is complete when discovery queries consistently
return accurate and timely results for active advertisements.

#### Deliverables

* A PR to the [vacp2p/disc-NG](https://github.com/vacp2p/disc-ng/) repo.

### Integration and Validation

* fully qualified name: `vac:acz:ift:2025q4-discovery:integration-validation`
* owner: Arunima
* status: started
* start-date: 2025/11/10
* end-date: 2025/11/24

#### Description

This final phase integrates all core modules into a cohesive system
and validates their behavior through simulations.
The components (registrar, advertiser, discoverer, and routing layer)
will be connected and tested together under various scenarios.
Simulations will cover registration, advertisement propagation,
discovery requests, and network dynamics.
Validation will focus on functional correctness, protocol compliance, and performance metrics.  
The task is complete when all modules operate together seamlessly
and the integrated system passes functional and performance validation tests.

#### Deliverables

* A PR to the [vacp2p/disc-NG](https://github.com/vacp2p/disc-ng/) repo.

### Logos Discovery Capability Spec

* fully qualified name: `vac:acz:ift:2025q4-discovery:logos-disc-specs`
* owner: Arunima
* status: not started
* start-date: 2025/10/30
* end-date: 2025/11/30

#### Description

This task involves addressing the feedback from the draft RFC task, 
organizing it into a draft PR, and then going through another review phase. 
It also includes discussing and addressing any newly identified or initiative-requiring topics. 
The task concludes with the merge of the PR.


#### Deliverables

* A PR to the [vacp2p/rfc-index](https://github.com/vacp2p/rfc-index/) repo. 