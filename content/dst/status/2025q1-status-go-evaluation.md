---
title: Status evaluation
tags:
  - "2025q1"
  - "dst"
  - "status"
draft: false
description: "Test Status-go on each new version or feature
and look for regressions,
learn scaling properties and run scaling studies."
---

`vac:dst:status:2025q1-status-go-evaluation`

## Description

Test Status-go on each new version or requested feature
and look for regressions,
learn scaling properties and run scaling studies,
understand the limits of Status-go and its behaviour.
Deliver reports and actionable insights.
Do this monthly, reliably, with documentation of findings.

### Background

We want to learn specific, actionable information
about Status-go's behaviour
and how it is evolving over time
with each new release
and with each thing we are specifically asked to check and test.

We will use a combination of real world testing,
theoretical analysis and simulation
to determine and measure the success,
side effects and other factors of Status-go and its evolution.

### Narratives

We will support the Conduit of Expertise narrative directly
by analysing and evaluating new Status-go releases and their features,
both with regards to features they have today
and with regards to how that compares to past behaviour.

Additionally, these efforts will contribute
to the Premier Research destination narrative by
improving and strengthening our relationship with the Status-go team
and thus increasing the reach and influence of the IFT,
and improving the chances
that we successfully grow our ecosystem's products and collaborations
and especially those we want to work with externally.

## Task list

### Status-backend baseline

* fully qualified name: `vac:dst:status:2025q1-status-go-evaluation:status-backend-baseline`
* owner: Wings
* status: 100%
* start-date: 2025/02/06
* end-date: 2025/02/11

#### Description
Use status-backend in a Kubernetes deployment.
Detect if it can run normally, 
similarly to nWaku deployments.
Document what utilities provide to work with,
and detect missing or nice-to-have ones.
Report differences with nWaku.

#### Deliverables
* [ ] Reports:
* [ ] Related PRs if apply:
  * https://github.com/vacp2p/status-go-test


### Status-backend subscription performance

* fully qualified name: `vac:dst:status:2025q1-status-go-evaluation:subscription-performance`
* owner: Wings
* status: 60%
* start-date: 2025/02/17
* end-date: 2025/02/21

#### Description
**Goal:** measure time to readiness to receive live messages.

**Setup:**
- 10 relay nodes
    - including 1 publisher node
- 5 service nodes
    - We may want to play with relay/service node ratios
    - service nodes may not be strictly needed
- 500 light nodes
- One community setup
- All relay and light nodes have joined the community

**Test:**
- Relay and service nodes are running
- 1 relay node is injecting messages
- Start light nodes
- Measure time from start to time messages are being received on filter
    - for example, looking at the earliest timestamp of the **first** message received

#### Deliverables
* [ ] Reports:
  * [Report WIP](https://www.notion.so/Status-Backend-Chat-Protocol-Benchmarks-Issues-1ab8f96fb65c80429833e945827d33e7)
* [ ] Related PRs if apply:

### Regression testing (recurring)

* fully qualified name: `vac:dst:status:2025q1-status-go-evaluation:regression-testing`
* owner: Wings
* status: recurring
* start-date: 2025/01/01
* end-date: 2025/03/31

#### Description
Run different scenarios
and collect evidence and data
of Status-go's behaviour.

Test for known regressions
that have occurred in the past
and ensure they don't happen again.


#### Deliverables
* [ ] Reports:
  * Notion report: [Report](https://www.notion.so/Status-Go-Test-18c8f96fb65c807c8ae4e4f20a60799c)
* [ ] Related PRs if apply:
  * Repository: [Github repo](https://github.com/vacp2p/status-go-test)