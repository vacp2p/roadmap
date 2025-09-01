---
title: DST Tooling
tags:
  - "2025q3"
  - "dst"
  - "ift"
draft: false
description: "Creating tools that allow
DST to easily work with other IFT projects.
This includes functionalities such as deployments,
monitoring, analysis, and control of aforementioned software's."
---

`vac:dst:ift:2025q3-dst-tooling`

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

* fully qualified name: `vac:dst:ift:2025q3-dst-tooling:general-tooling`
* owner: Alberto
* status: recurring
* start-date: 2025/07/01
* end-date: 2025/09/30

#### Description
Group of utilities that are added to the main repository.
Should be made general when possible.

#### Deliverables
- PRs:
  - [Github PR: Scale x axis](https://github.com/vacp2p/10ksim/pull/76)
  - [Github PR: Add events logging for waku regression experiment](https://github.com/vacp2p/10ksim/pull/78)
  - [Github PR: Update getenr](https://github.com/vacp2p/10ksim/pull/127)
  - [Github PR: Better query parsing](https://github.com/vacp2p/10ksim/pull/128)
  - [Github PR: Debug mode to msg_retriever](https://github.com/vacp2p/10ksim/pull/129)
  - [Github PR: Make _metadata_event use dict events](https://github.com/vacp2p/10ksim/pull/131)
  - [Github PR: Deploy base experiment and dry run](https://github.com/vacp2p/10ksim/pull/132)
  - [Github PR: Add cls.name when registering experiments](https://github.com/vacp2p/10ksim/pull/136)
- Documents:
  - [Notion WIP document: Deployment workflow discussion](https://www.notion.so/Deployment-Workflow-25d8f96fb65c80f7801ce9a06dede8a4)

### Improve tooling

* fully qualified name: `vac:dst:ift:2025q3-dst-tooling:improve-tooling`
* owner: Pearson
* status: 100%
* start-date: 2025/07/01
* end-date: 2025/07/04

#### Description
Move values.yamls to same place under experiments (instead of spread throughout node/publisher/etc.)
Ensure fixes made during regression testing are merged in.
Add get-filter-messages and get-store-messages images.
Create, organize and prioritize nice-to-haves in the codebase.

#### Deliverables
- PRs:
  - [Github PR: Add images](https://github.com/vacp2p/10ksim/pull/74)
  - [Github PR: Experiments self contained](https://github.com/vacp2p/10ksim/pull/75)
- Related Documents:


### Status-Waku log parser

* fully qualified name: `vac:dst:ift:2025q3-dst-tooling:status-waku-log-parser`
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

* fully qualified name: `vac:dst:ift:2025q3-dst-tooling:scenario-workflow-manager`
* owner: Alberto
* status: 0%
* start-date: -
* end-date: -

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


### Shadow integration scaffold

* fully qualified name: `vac:dst:ift:2025q3-dst-tooling:shadow-integration-scaffold`
* owner: Farooq
* status: 80%
* start-date: 2025/08/11
* end-date: 2025/08/22

#### Description
Include shadow simulations in the DST experiments. Following the current workflow, when regression experiments
are launch in the lab, set up at the same time similar experiments using shadow.
Configurations should be similarly set up to the regression ones and modular because they will depends on the project.
Do it in a way that grabbing the results for the analysis can be also coupled with the main tool workflow.
Ideally, the DST node with nim-libp2p is a nice place for starting the scaffold.

#### Deliverables
- PRs:
- Related Documents:


### Deployment updates

* fully qualified name: `vac:dst:ift:2025q3-dst-tooling:deployment-updates`
* owner: Pearson
* status: 100%
* start-date: 2025/08/11
* end-date: 2025/08/15

#### Description
Enhance documentation clarity and streamline usability workflows, 
reducing friction for new users.

#### Deliverables
- PRs:
  - [Github PR: Organize Repo](https://github.com/vacp2p/10ksim/pull/124)
- Related Documents:


### Python uv

* fully qualified name: `vac:dst:ift:2025q3-dst-tooling:python-uv`
* owner: Alberto
* status: 100%
* start-date: 2025/08/12
* end-date: 2025/08/22

#### Description
Get rid of the multiple requirement.txt and set uv for the repository.
Also, get rid of utilities that are not currently being used (message explorer,
topology generator).

#### Deliverables
- PRs:
  - [Github PR: Add uv](https://github.com/vacp2p/10ksim/pull/130)
- Related Documents:


### Workdir experiments track

* fully qualified name: `vac:dst:ift:2025q3-dst-tooling:workdir-experiments-track`
* owner: Pearson
* status: 100%
* start-date: 2025/08/12
* end-date: 2025/08/22

#### Description
Keep track of values and logs of previous experiments in an automatized and cross platform way.

#### Deliverables
- PRs:
  - [Github PR: Organize experiments output](https://github.com/vacp2p/10ksim/pull/134)
- Related Documents: