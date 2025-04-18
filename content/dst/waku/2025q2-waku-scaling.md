---
title: Waku Scaling
tags:
  - "2025q2"
  - "dst"
  - "waku"
draft: false
description: "Use testing,
theoretical analysis and simulation
to determine and improve Waku's scaling properties.
Find the limits of Waku's capabilities
and measure them in different scenarios.
Deliver hard numbers and actionable insights.
Confirm or reject our ideas."
---

`vac:dst:waku:2025q2-waku-scaling`

## Description

We will use realistic Waku node testing,
theoretical analysis, and simulations
to evaluate and improve Waku's scalability.
Performance measurements 
in waku components will be also done.
This includes identifying Waku’s limits
and measuring performance in various scenarios,
delivering concrete data and actionable insights
to validate or challenge our ideas.


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


### Scale one to one chat
> *Note*: This needs more input from project

* fully qualified name: `vac:dst:waku:2025q2-waku-scaling:scale-one-to-one`
* owner: TBA
* status: 0%
* start-date: <yyyy/mm/dd>
* end-date: <yyyy/mm/dd>

#### Description

#### Deliverables


### Messaging API
> *Note*: This needs more input from project

* fully qualified name: `vac:dst:waku:2025q2-waku-scaling:messaging-api`
* owner: TBA
* status: 0%
* start-date: <yyyy/mm/dd>
* end-date: <yyyy/mm/dd>

#### Description
- Includes compare gowaku with nwaku replacement?

#### Deliverables

### Direct message reliability

* fully qualified name: `vac:dst:waku:2025q2-waku-scaling:direct-message-reliability`
* owner: TBA
* status: 0%
* start-date: <yyyy/mm/dd>
* end-date: <yyyy/mm/dd>

#### Description
Store message hash queries 
of less than 10 hashes
are served (wire-to-wire) under 400 ms,
as long as the database
is less than 250 GB size
and average message size under 500KiB.
This refers to message-hash-queries 
that have `include-data=true`.

Wire-to-wire includes the whole storage time, as in
database-time + transport-time + node-time.

Store message time range queries
of less than 24 hours,
with less than 10 content topics,
are served under 400 ms,
as long as the database
is less than 250 GB size
and average message size under 500KiB.

To validate this, it will be used
against a status-prod-like database.

#### Deliverables
- Analysis report
- Code

### Decentralized storage dogfooding
> *Note*: This needs more input from project

* fully qualified name: `vac:dst:waku:2025q2-waku-scaling:decentralized-storage-dogfooding`
* owner: TBA
* status: 0%
* start-date: <yyyy/mm/dd>
* end-date: <yyyy/mm/dd>

#### Description

#### Deliverables

### Contact discovery app features
> *Note*: This needs more input from project

* fully qualified name: `vac:dst:waku:2025q2-waku-scaling:discovery-app-features`
* owner: TBA
* status: 0%
* start-date: <yyyy/mm/dd>
* end-date: <yyyy/mm/dd>

#### Description

#### Deliverables

### Store sync
> *Note*: This needs more input from project

* fully qualified name: `vac:dst:waku:2025q2-waku-scaling:store-sync`
* owner: TBA
* status: 0%
* start-date: <yyyy/mm/dd>
* end-date: <yyyy/mm/dd>

#### Description
Analyze store sync Waku's functionality,
where store nodes get in sync.
This should happen after a disconnection,
or when a fresh node is joined to the network.

#### Deliverables
- Analysis report
- Code


### Discv5 initial activity

* fully qualified name: `vac:dst:waku:2025q2-waku-scaling:discv5-initial-activity`
* owner: TBA
* status: 0%
* start-date: TBA
* end-date: TBA

#### Description

Ensure data before stable mesh do not skew results.
Also, analyze Discv5 usage in this scenario.
Create a simulation without traffic,
where nodes are leaving and joining the network,
once the mesh is healthy. 
Compare these results from initial state and healthy state.
Try this with different network sizes.
Help to identify scenarios that are most realistic.


#### Deliverables
- Reports:
- Related PRs if apply:


### Nwaku in status mobile

* fully qualified name: `vac:dst:waku:2025q2-waku-scaling:waku-in-status-mobile`
* owner: TBA
* status: 0%
* start-date: <yyyy/mm/dd>
* end-date: <yyyy/mm/dd>

#### Description

#### Deliverables