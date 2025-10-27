---
title: DST Tooling
tags:
  - "2025q4"
  - "dst"
  - "ift"
draft: false
description: "Creating tools that allow
DST to easily work with other IFT projects.
This includes functionalities such as deployments,
monitoring, analysis, and control of aforementioned software's."
---

`vac:dst:ift:2025q4-dst-tooling`

## Description

We will create tools to help DST efficiency.
These tools can be composed of utilities for Kubernetes,
or any other kind that fits the necessities of DST and other projects.
As projects might share common necessities, this tasks will be considered
as a scaffold for DST tools, adapting the tools for each project if it needs.
The primary focus will be on adapting the necessities of the Waku team for
the log parser tool. This will comprise retrieving information from a given
message id, history of discovered peers, subscriptions, while having good 
performance and supportability.
Additionally, the project will define workflows that facilitate the creation
and execution of specialized scenarios. These scenarios will assist in 
the analysis of libp2p and Gossipsub, supporting studies focused on 
adversarial conditions and control message behavior.


### Background

### Narratives

These efforts will support the Conduit of Expertise narrative by
accelerating DST/IFT Improvements,
providing measurable insights
to enhance developer experience
within and beyond the IFT ecosystem.
Also, ideally these tools can be shared across projects, 
reinforcing cross project collaboration.


## Task list

### General tooling (recurring)

* fully qualified name: `vac:dst:ift:2025q4-dst-tooling:general-tooling`
* owner: Alberto
* status: recurring
* start-date: 2025/10/01
* end-date: 2025/12/31

#### Description
Group of utilities that are added to the main repository.
Should be made general when possible.

#### Deliverables
- PRs:
    - [Github PR: Fix nimlibp2p tracer #161](https://github.com/vacp2p/10ksim/pull/161)
    - [Github PR: Move metadata helpers to base_experiment #162](https://github.com/vacp2p/10ksim/pull/162)
    - [Github PR: nimlibp2p mix node deployment changes #137](https://github.com/vacp2p/10ksim/pull/137)
    - [Github PR: Mixnet analysis changes #163](https://github.com/vacp2p/10ksim/pull/163)
    - [Github PR: Allow multiple match groups for the same query in victoria_reader.py #164](https://github.com/vacp2p/10ksim/pull/164)
- Documents:

### General log parser

* fully qualified name: `vac:dst:ift:2025q4-dst-tooling:general-log-parser`
* owner: Alberto
* status: 0%
* start-date: -
* end-date: -

#### Description
The goal of this task is to extend the DST log parser tool to 
assist developers in debugging and analyzing message histories and activity 
within the Waku and Status ecosystems. The tool should consolidate and 
process data from diverse log sources, including Status app logs, 
nWaku application logs, nWaku fleet logs (via Kibana API), and 
Status mobile logs.
The tool’s primary focus is to support developers by retrieving the 
complete lifecycle and related histories for given Waku message IDs or 
Status envelope IDs. This will empower developers to better understand 
network events, troubleshoot issues, and optimize usage scenarios within 
libp2p, Gossipsub, MVDS, and SDS protocols.

#### Deliverables
- PRs:
- Related Documents:


### Scenario workflow manager

* fully qualified name: `vac:dst:ift:2025q4-dst-tooling:scenario-workflow-manager`
* owner: TBD
* status: 0%
* start-date:
* end-date:

#### Description
The objective of this task is to create a workflow management tool to design, 
execute, and evaluate specialized network scenarios tailored to the analysis of 
libp2p and Gossipsub protocols. The tool will enable developers and researchers
to simulate and study adversarial conditions and control message patterns in a 
controlled and reproducible manner.
The scenarios will provide insights into network behavior under various conditions, 
facilitating performance optimizations, behavioral analysis, and the exploration of
message interactions in distributed environments. This tool aims to 
improve understanding of protocols like Gossipsub and libp2p, both in regular 
workflows and edge-case scenarios.

#### Deliverables
- PRs:
- Related Documents:


### Scenario workflow manager

* fully qualified name: `vac:dst:ift:2025q4-dst-tooling:local-stack-analysis`
* owner: TBD
* status: 0%
* start-date:
* end-date:

#### Description
Improve the main repository with a local stack for deploying experiments in local.
This will allow developers to run experiments locally and test their changes,
while also monitoring the components, being able to see if analysis updates
are also working properly.
This stack should be easy to build, with documentation and examples.
Ideally it is done with Docker Desktop, or any other light Kubernetes solution.

#### Deliverables
- PRs:
- Related Documents:

### Complete deployment refactor

* fully qualified name: `vac:dst:ift:2025q4-dst-tooling:complete-deployment-refactor`
* owner: Pearson
* status: 30%
* start-date: 2025/10/06
* end-date: 2025/10/24

#### Description
After refactor feasibility was done in `vac:dst:ift:2025q3-dst-tooling:deployment-refactor`, continue
this line of work to complete the refactor. 
Keep following the discussions on the [deployment document](https://www.notion.so/Deployment-Workflow-25d8f96fb65c80f7801ce9a06dede8a4).
To not keep extending new functionalities with new projects, Waku will be added as baseline 
for the refactor functionalities to be tested. Other projects will be  added in other tasks.

#### Deliverables
- PRs:
- Related Documents:

