---
title: Waku Scaling
tags:
  - "2025q1"
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

`vac:dst:waku:2025q1-waku-scaling`

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

* fully qualified name: `vac:dst:waku:2025q1-waku-scaling:scale-one-to-one`
* owner: Alberto
* status: 0%
* start-date: <yyyy/mm/dd>
* end-date: <yyyy/mm/dd>

#### Description

#### Deliverables

<!--
Will be this done in Q2?

### Nwaku in status mobile

* fully qualified name: `vac:dst:waku:2025q1-waku-scaling:waku-in-status-mobile`
* owner: Alberto
* status: 0%
* start-date: <yyyy/mm/dd>
* end-date: <yyyy/mm/dd>

#### Description

#### Deliverables

### Logos forum

* fully qualified name: `vac:dst:waku:2025q1-waku-scaling:logos-forum`
* owner: Alberto
* status: 0%
* start-date: <yyyy/mm/dd>
* end-date: <yyyy/mm/dd>

#### Description

#### Deliverables
-->

### Messaging API
> *Note*: This needs more input from project

* fully qualified name: `vac:dst:waku:2025q1-waku-scaling:messaging-api`
* owner: Alberto
* status: 0%
* start-date: <yyyy/mm/dd>
* end-date: <yyyy/mm/dd>

#### Description
- Includes compare gowaku with nwaku replacement?

#### Deliverables

### Direct message reliability

* fully qualified name: `vac:dst:waku:2025q1-waku-scaling:direct-message-reliability`
* owner: Alberto
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

Store message time range queries
of less than 24 hours,
with less than 10 content topics,
are served under 400 ms,
as long as the database
is less than 250 GB size
and average message size under 500KiB.

#### Deliverables
- Analysis report
- Code

### Decentralized storage dogfooding
> *Note*: This needs more input from project

* fully qualified name: `vac:dst:waku:2025q1-waku-scaling:decentralized-storage-dogfooding`
* owner: Alberto
* status: 0%
* start-date: <yyyy/mm/dd>
* end-date: <yyyy/mm/dd>

#### Description

#### Deliverables

### Contact discovery app features
> *Note*: This needs more input from project

* fully qualified name: `vac:dst:waku:2025q1-waku-scaling:discovery-app-features`
* owner: Alberto
* status: 0%
* start-date: <yyyy/mm/dd>
* end-date: <yyyy/mm/dd>

#### Description

#### Deliverables

### Store sync
> *Note*: This needs more input from project

* fully qualified name: `vac:dst:waku:2025q1-waku-scaling:store-sync`
* owner: Alberto
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

### Waku Shard Scaling

* fully qualified name: `vac:dst:waku:2025q1-waku-scaling:waku-shard-scaling`
* owner: Alberto
* status: 100%
* start-date: 2025/01/06
* end-date: 2025/01/24

#### Description

Address feedback from `vac:dst:waku:2024q4-waku-scaling:waku-shard-reliability-vs-scale`.
Increase the number of shards up to the highest possible value.


#### Additional info
Blocked by a nwaku issue. Another task will be created to keep requested work.

#### Deliverables
- [ ] Reports:
  - Issue found: [Issue](https://github.com/waku-org/nwaku/issues/3245)
- [ ] Related PRs if apply:
  - Time to get healthy plot PR: [PR](https://github.com/vacp2p/10ksim/pull/48)
  - Blocking issue found: [Github Issue](https://github.com/waku-org/nwaku/issues/3250)