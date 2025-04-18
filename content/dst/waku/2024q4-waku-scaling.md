---
title: Waku Scaling
tags:
  - "2024q4"
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

`vac:dst:waku:2024q4-waku-scaling`

## Description
Use realistic (running actual Waku nodes, no abstraction) testing,
theoretical analysis and simulation
to determine and improve Waku's scaling properties.
Find the limits of Waku's capabilities
and measure them in different scenarios.
Deliver hard numbers and actionable insights.
Confirm or reject our ideas.

Through this we will, among other things,
research and find the limits of Waku's capabilities
and measure them in different scenarios.
We will work with the Waku team to improve and measure Waku
and allow for deep examination of a wide range of networks
from sizes anywhere from small (< 500 nodes)
to midscale (500-5000 nodes)
to large (10,000+ nodes).

We will in some ways
provide a parallel to the Vac QA team's efforts -
while their focus is on individual low level
or individual parts of Waku
and other software within the IFT ecosystem,
ours will be on the realistic behaviour of Waku as a whole system -
at different scales and with different configurations,
mesh structure and shape -
and how that maps to our theoretical work.

We will support the Conduit of Expertise narrative directly
by providing valuable insights to Waku
and the ability to theorise, reason about, test, measure and improve
the performance, stability and scalability of Waku.

These efforts will contribute in these ways to the Conduit of Expertise narrative:

* Accelerate improvements to Waku,
  improving the developer community's experience and satisfaction
  both inside and outside of IFT's ecosystem,
  through allowing repeatable, measureable and realistic insights into Waku,
  all the way from theory to practice and back.

* Improve the RFC culture by allowing for faster and easier development of RFCs
  with the aid of rapidly accelerated insights
  into how an RFC in development
  will perform as it's being expanded
  and as it goes through the draft process.

* Allow easier post-mortem analysis
  of the success or relative performance
  of a given RFC -
  does this change use more or less bandwidth?
  Did it improve things?
  Seeing the effects of changes at scale
  allows for a greater ability
  to usefully wrap up work on, and conclude, an RFC process
  and document and absorb what we learned in the process
  into further improvements.

## Task List

<!--
This will occur 2025Q1, this is kept for later

### High Scalability Waku Demonstration

* fully qualified name: `vac:dst:waku:waku-scaling:high-scalability-waku-demonstration`
* owner: Wings
* status: 95%
* start-date: TBD
* end-date: TBD

Measure its performance
and attempt to support the assertion
that Waku is a scalable solution
that can work in networks at sizes
that push the limits of what the theoretical work we did predicted is possible.

Specifically, we want to deploy a 10,000 node Waku network
and measure its performance in terms of message delivery,
bandwidth usage, and other metrics.
We want to deliver a report on what we learned,
what we tested and what we found.

The report should include analysis of the performance of Waku at extreme scale,
providing insights that allow people to see significant supporting evidence
that Waku can in fact scale to these sizes and perform reliably.

#### Deliverables
- [x] An infrastructure setup, whether on-prem or cloud,
  that can support deployments of a 10,000 node Waku network.

- [x] https://github.com/vacp2p/10ksim - A working set of bundled and compatible Kubernetes manifests
  that allow for up to a 10,000 node Waku network
  to be reliably created and measured.
  The manifests should be compatible with [vac|dst|deployer-tool|deployer-tool]
  and flexible.

- [ ] A useful set of measurements taken with the monitoring system and tooling we have available.

- [ ] The monitoring system stays stable the entire time, providing useful information and metrics.
-->

### Test Store Protocol At Scale

* fully qualified name: `vac:dst:waku:2024q4-waku-scaling:test-store-protocol-at-scale`
* owner: Alberto
* status: Done
* start-date: 2024/10/07
* end-date: 2024/10/18

#### Description
Test the Store protocol at scale.

#### Deliverables
- [x] [A report on the results](https://www.notion.so/Test-Store-Protocol-At-Scale-1228f96fb65c80ed9eb8ca7b1d69061d) of the test,
  including analysis, data and metrics.
- [x] [A list of any issues encountered](https://www.notion.so/Test-Store-Protocol-At-Scale-1228f96fb65c80ed9eb8ca7b1d69061d?pvs=4#1228f96fb65c8059a79cebe3b13e8ebb) (no issues reported).
- [x] [Hard data and metrics from the simulation](https://www.notion.so/Test-Store-Protocol-At-Scale-1228f96fb65c80ed9eb8ca7b1d69061d?pvs=4#1228f96fb65c8059a79cebe3b13e8ebb).

#### Status
Fully delivered.

### High Churn Relay+Store Reliability

* fully qualified name: `vac:dst:waku:2024q4-waku-scaling:high-churn-relay-store-reliability`
* owner: Alberto
* status: Done
* start-date: 2024/10/01
* end-date: 2024/12/31

#### Description
If nodes go online/offline, we should be able to retrieve missing messages from the store.

#### Deliverables
- [X] A report on the results of the test,
  including analysis, data and metrics.
  - [Notion report](https://www.notion.so/High-Churn-Relay-Store-Reliability-16c8f96fb65c8008bacaf5e86881160c)
  - [Notion public report](https://zealous-polka-dc7.notion.site/High-Churn-Relay-Store-Reliability-16c8f96fb65c8008bacaf5e86881160c)
- [X] A list of any issues encountered.
- [X] Hard data and metrics from the simulation.

### Relay/DiscV5 Resources in Heterogenous Clusters

* fully qualified name: `vac:dst:waku:2024q4-waku-scaling:relay-discv5-resources-in-heterogenous-clusters`
* owner: Wings
* status: 0%
* start-date: 2024/10/01
* end-date: 2024/12/31

#### Description
Measure Relay bandwidth usage
and DiscV5 bandwidth usage
in heterogenous clusters
involving different node implementations
such as nwaku and go-waku.

#### Deliverables
- [ ] A report on the results of each test, including analysis, data and metrics.
- [ ] A list of any issues encountered.
- [ ] Hard data and metrics from the simulation.

### Waku Shard Reliability vs Scale

* fully qualified name: `vac:dst:waku:2024q4-waku-scaling:waku-shard-reliability-vs-scale`
* owner: Alberto
* status: Done
* start-date: 2024/10/01
* end-date: 2024/12/31

#### Description
Test waku shard behaviour and stability with various of numbers of shards.

Choose a matrix to test for and then test for it.

#### Deliverables
- [X] Matrix/exact deployment script defined
- [X] A report on the results of each test, including analysis, data and metrics.
  - [Notion report](https://www.notion.so/Waku-Shard-Reliability-vs-Scale-1608f96fb65c80a684f0f7d0c0e32571)
  - [Notion public report](https://zealous-polka-dc7.notion.site/Waku-Shard-Reliability-vs-Scale-1608f96fb65c80a684f0f7d0c0e32571?pvs=74)
- [X] A list of any issues encountered.
- [x] Hard data and metrics from the simulation.

### Filter and lightpush tests

Test the performance and reliability and behaviour
of the Filter and lightpush protocols at scale.

Confirm their stability and reliability at various scales.

Adjust the specific tests involved
in response to collaboration with the Waku team's directions
and the discoveries we make during the course of this work.

* fully qualified name: `vac:dst:waku:2024q4-waku-scaling:filter-lightpush-tests`
* owner: Alberto
* status: Done
* start-date: 2024/10/18
* end-date: 2024/10/25

#### Description
Test the Filter and lightpush protocols at scale.

#### Deliverables
- [X] A report on the current reliability and performance of the protocols at scale.
  - [Report](https://zealous-polka-dc7.notion.site/Filter-and-lightpush-tests-12a8f96fb65c8041818bcd24b3b819c1)
- [X] Filed any issues encountered.
  - [Connections issue](https://github.com/waku-org/nwaku/issues/3163)
  - [Documentation issue](https://github.com/waku-org/waku-rest-api/pull/15)
- [X] Hard data and metrics from the simulation.
  - [Data](https://www.notion.so/Filter-and-lightpush-tests-12a8f96fb65c8073bb7dd9ba465a67cb?pvs=4#12a8f96fb65c807db16cf565c269bf4a)

### Measure DiscV5 bandwidth with Waku discovery

* fully qualified name: `vac:dst:waku:2024q4-waku-scaling:measure-discv5-bandwidth-with-waku-discovery`
* owner: Alberto
* status: Done
* start-date: 2024/10/01
* end-date: 2024/12/31

#### Description
Measure the bandwidth usage of the Waku discovery protocol using the DiscV5 protocol.

#### Deliverables
- [X] A report on what you've learnt
  - [Report](https://zealous-polka-dc7.notion.site/Measure-DiscV5-bandwidth-with-Waku-discovery-1698f96fb65c80659fa1fbfdac49b1ef)
- [X] Hard data and metrics from the simulation.
- [X] A documentation page with analysis and results and notes.

### Partial PeX Experimental Analysis

* fully qualified name: `vac:dst:waku:2024q4-waku-scaling:partial-pex-experimental-analysis`
* owner: Alberto
* status: Done
* start-date: 2024/10/01
* end-date: 2024/12/31

#### Description
Produce and run an experimental test environment
where a partial subset of the nodes
use Waku's Peer Exchange protocol
to share information about other nodes in the network.

Measure the bandwidth usage of DiscV5 on those nodes that use PeX
and compare it to the DiscV5 bandwidth usage of nodes that do not.

Measure overall bandwidth usage and record conclusions as to the impact of PeX.

#### Deliverables
- [X] DiscV5 bandwidth comparison document/report - PeX vs no-PeX
  - [Notion report](https://www.notion.so/Partial-PeX-Experimental-Analysis-16c8f96fb65c80e79ff7d2e941eba1b5)
  - [Notion public report](https://zealous-polka-dc7.notion.site/Partial-PeX-Experimental-Analysis-16c8f96fb65c80e79ff7d2e941eba1b5)
- [X] Overall bandwidth usage comparison document/report
- [X] Record conclusions as to the impact of PeX.

### Mixed Environment Analysis

* fully qualified name: `vac:dst:waku:2024q4-waku-scaling:mixed-environment-analysis`
* owner: Alberto
* status: Done
* start-date: 2024/10/01
* end-date: 2024/12/31

#### Description

Measure relay resource with a mix of nodes
using Resource-restricted device reliability protocol and peer exchange,
meaning a small number of nwaku nodes serve store, light push and filter protocols
and a high number of clients consume them. 
For example, 6-10 service nodes, 200 relay nodes and 1000 light nodes. 
This should include connection and node churn impact on reliability for both relay and light clients.

#### Deliverables

- [X] A report on the findings and measurements and results.
  - [Report](https://zealous-polka-dc7.notion.site/Mixed-environment-analysis-1688f96fb65c809eb235c59b97d6e15b)
- [X] A list of any issues encountered.
- [x] Analysis and actionable insights or conclusions.


<!-- Most recently blocked by metrics scaling issues, nearly through them -->

