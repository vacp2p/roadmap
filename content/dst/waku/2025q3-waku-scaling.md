---
title: Waku Scaling
tags:
  - "2025q3"
  - "dst"
  - "waku"
draft: false
description: "Use experiments determine and
improve Waku's scaling properties.
Find the limits of Waku's capabilities
and measure them in different scenarios.
Deliver hard numbers and actionable insights.
Confirm or reject our ideas or presented ones."
---

`vac:dst:waku:2025q3-waku-scaling`

## Description

We will use realistic Waku node experiments to evaluate
and improve Waku's scalability by conducting
performance measurements across its key components and tasks.
These efforts contains supporting on-chain RLN memberships,
strengthening the foundations for private chats, optimize 
browser bootstrapping for improved responsiveness, 
integrate nwaku in Status Desktop for seamless relay functionality,
and implement the SDS protocol for group messaging reliability and recovery.


### Background

### Narratives

These efforts will support the Conduit of Expertise narrative by
accelerating Waku Improvements,
providing measurable insights
to enhance developer experience
within and beyond the IFT ecosystem.
Enhancing RFC Development by enabling faster,
more informed RFC development
through performance insights during the drafting process.

## Task list

### Implementing Waku API in REST
> *Note*: This needs more input from project

[TODO: Link to Waku FURPS]()

* fully qualified name: `-`
* owner: -
* status: -
* start-date: -
* end-date: -

#### Description

Make use of Waku API in rest in DST experiments. Also provide feedback of 
its functionality.

#### Deliverables
- Code:
- Report


### TWN supports RLN onchain tree and deposits, existing memberships only
> *Note*: This needs more input from project

[TODO: Link to Waku FURPS]()

* fully qualified name: `-`
* owner: -
* status: -
* start-date: -
* end-date: -

#### Description
Waku estimated date of completion: 30 June 2025

Prove that a new node setup with an RLN membership can be ready
to verify RLN proof within 5s, no matter the size of the tree.

#### Deliverables
- Code: 
- Report:



### Hardening and Scaling Foundations for Private Chats
> *Note*: This needs more input from project

[TODO: Link to Waku FURPS]()

* fully qualified name: `-`
* owner: -
* status: -
* start-date: -
* end-date: -

#### Description

To have: Vac-DST: status-backend benchmarks

#### Deliverables
- Code: 
- Report:


### Optimise Browser Bootstrapping
> *Note*: This needs more input from project

[TODO: Link to Waku FURPS]()

* fully qualified name: `-`
* owner: -
* status: -
* start-date: -
* end-date: -

#### Description
Waku estimated date of compeltion: 31 Aug

Using js-waku, prove that:
- From an operating state, a node can 
resume transmitting messages within 1 second 
after disconnection; in a network with 1 bootstrap node,
100 service nodes and 500 browser nodes.

- From a cold start, a node can start transmitting 
messages within 5 seconds; in a network with 1 bootstrap
node, 100 service nodes and 500 browser nodes.

#### Deliverables
- Code: 
- Report:



### Integrate nwaku in Status Desktop, relay mode only
> *Note*: This needs more input from project

[TODO: Link to Waku FURPS]()

* fully qualified name: `-`
* owner: -
* status: -
* start-date: -
* end-date: -

#### Description

Waku estimated date of completion: 30 June

Vac-DST to complete go-waku-based benchmark works and proceed with
nwaku-based vs go-waku-based status-backend comparisons.

#### Deliverables
- Code: 
- Report:


### SDS protocol in Status - basic integration

> *Note*: This needs more input from project

[TODO: Link to Waku FURPS]()

* fully qualified name: `-`
* owner: -
* status: -
* start-date: -
* end-date: -

#### Description
Waku estimated date of completion: 31 Aug

Prove that:
- When sending a message in a group, the publisher
can ensure the message was received by at least one 
recipient within `S` seconds

- When receiving messages in a group, the receiver
can detect 90% of missed messages within `3*S` seconds


#### Deliverables
- Code:
- Report:



### SDS protocol in Status - basic recovery

> *Note*: This needs more input from project

[TODO: Link to Waku FURPS]()

* fully qualified name: `-`
* owner: -
* status: -
* start-date: -
* end-date: -

#### Description
Waku estimated date of completion: 31 Aug 2025

Prove that:
- When receiving messages in group, the receiver can 
- reach eventual consistency within `6*S` seconds

#### Deliverables
- Code:
- Report: