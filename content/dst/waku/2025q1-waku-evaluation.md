---
title: Waku Evaluation
tags:
  - "2025q1"
  - "dst"
  - "waku"
draft: false
description: "Test Waku on each new version or requested feature
and look for regressions,
learn scaling properties and run scaling studies."
---

`vac:dst:waku:2025q1-waku-evaluation`

## Description
Test Waku on each new version or requested feature
and look for regressions,
learn scaling properties and run scaling studies,
understand the limits of Waku and its behaviour.
Deliver reports and actionable insights.
Do this monthly, reliably, with documentation of findings.

### Background

We want to learn specific, actionable information
about Waku's behaviour
and how it is evolving over time
with each new release
and with each thing we are specifically asked to check and test.

We will use a combination of real world testing,
theoretical analysis and simulation
to determine and measure the success,
side effects and other factors of Waku and its evolution.

### Narratives
We will support the Conduit of Expertise narrative directly
by analysing and evaluating new Waku releases and their features,
both with regards to features they have today
and with regards to how that compares to past behaviour.

We will:

* Enable improvements to Waku
  by allowing for repeatable, measureable
  and real world insights into Waku,
  all the way from theory to practice and back.
* Reduce the risk of a Waku regression
  making it into a new release of Waku.

Additionally, these efforts will contribute
to the Premier Research destination narrative by:

* Improving and strengthening our relationship with the Waku team
  and improving the quality and reputation of IFT's work, inside
  and outside of Waku.

### Additional info

## Task list

### Regression testing (recurring)

* fully qualified name: `vac:dst:waku:2025q1-waku-evaluation:regression-testing`
* owner: Alberto
* status: Ongoing
* start-date: 2025-01-01
* end-date: 2025-03-31

#### Description
Run different scenarios
and collect evidence and data
of Waku's behaviour.

Test for known regressions
that have occurred in the past
and ensure they don't happen again.

#### Deliverables
* Analysis done
  * [Simulation length vs message delay](https://www.notion.so/Simulation-length-vs-message-delay-1858f96fb65c80f58b81dec6841764c6)
  * [nWaku v0.35 WIP](https://www.notion.so/Waku-regression-testing-v0-35-February-2025-1908f96fb65c802aaec6fdb5028a167b)
  * [Lightpush Issue v0.35](https://www.notion.so/Lightpush-Unable-to-deserialize-1a08f96fb65c80c5ae3bc9f49ca01504)
* Report published with all relevant details
* Vac Roadmap updated regularly
  with links to the analysis and results.
  * [REST Issue](https://github.com/waku-org/nwaku/pull/3286)

### Block issue: I/O load

* fully qualified name: `vac:dst:waku:2025q1-waku-evaluation:block-io-load`
* owner: Alberto
* status: 100%
* start-date: 2025-01-20
* end-date: 2025-01-31

#### Description

Investigate if a blocking issue found
is related to I/O capacity instead of CPU capacity.
Reproduce the issue while measuring I/O 
per VM where the nodes are being run
and analyze if there is a relation between I/O
and the nodes that are blocked.
Report findings.

#### Deliverables
- Reports:
  - [Notion report](https://www.notion.so/Stuck-Issue-Finished-2fb05e6b5cfb4c3c820865e5bf2eef11)
- Related PRs if apply:
  - [Github Issue](https://github.com/waku-org/nwaku/issues/2921)

### Discovery speed time

* fully qualified name: `vac:dst:waku:2025q1-waku-evaluation:discovery-speed-time`
* owner: Alberto
* status: 50%
* start-date: 2025-02-03
* end-date: 2025-02-14

#### Description

It is being noticed that some peers
can take up to 10 minutes to find peers
to establish full-mesh connections.
Dissection if this happens on the same shard,
what are the causes if any,
and what could be the improvements, if any.
Report findings.

#### Deliverables
- Reports:
- Related PRs if apply:

### Message latency

* fully qualified name: `vac:dst:waku:2025q1-waku-evaluation:message-latency`
* owner: Alberto
* status: 50%
* start-date: 2025-02-03
* end-date: 2025-02-14

#### Description

Investigate situations where a message
takes up to 2 seconds to arrive to all nodes.
Analyze if this is dependant on number of nodes,
if the messages that take longer have a correlation
with being the latest injected, and so on.
Determine what can be the causes,
and report findings.

#### Deliverables
- Reports:
- Related PRs if apply: