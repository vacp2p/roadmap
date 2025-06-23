---
title: DST Tooling
tags:
  - "2025q2"
  - "dst"
  - "ift"
draft: false
description: "Creating tools that allow
DST to easily work with other IFT projects.
This includes functionalities such as deployments,
monitoring, analysis, and control of aforementioned software's."
---

`vac:dst:ift:2025q2-dst-tooling`

## Description

We will create tools to help DST efficiency.
These tools can be composed of utilities for Kubernetes,
or any other kind that fits the necessities of DST and other projects.
As projects might share common necessities, this tasks will be considered
as a scaffold for DST tools, adapting the tools for each project if it needs.
The primary focus will be on creating a Kubernetes-based deployment utility 
to simplify and standardize the process of launching experiments in 
a distributed environment. This tool will aim to reduce manual setup 
time and ensure consistency across different test scenarios.
In addition, we will develop a general-purpose log parser capable
of extracting and structuring logs in a way that supports analysis
and debugging across DST initiatives. This parser will help streamline
workflows for developers and researchers by making log data more 
accessible and actionable.

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

### Python deployment scaffold

* fully qualified name: `vac:dst:ift:2025q2-dst-tooling:python-deployment-scaffold`
* owner: Pearson
* status: 100%
* start-date: 2025/05/12
* end-date: 2025/05/30

#### Description
Design and code an initial structure to create deployments in a Kubernetes environment with Python.
Taking as initial example nWaku deployments in bash, create a system where 
statefulset can be deployed and controlled/configured easily. 
Take into account that this should remain a general tool, considering
other kind of deployments (PODs) with any other pieces of software that might run inside.
This should substitute the usage of bash scripts, allowing a better configuration
and usability. Note that the deployment/s should also be controlled by the user if required, in the future.
Apart from the configuration of the deployment, it should be considered a way to continue the workflow with 
the next steps of the experiments (scraping and plotting).
If possible, adapt this to be able to run it from inside and outside the cluster.


#### Deliverables
- PRs:
  - [Github: PR](https://github.com/vacp2p/10ksim/pull/68)
- Related Documents:
  - [Notes.status: Design Notes](https://notes.status.im/rdzaX1TVQ0KnUXfCAWBegQ?view)

### Analysis refactor

* fully qualified name: `vac:dst:ift:2025q2-dst-tooling:analysis-refactor`
* owner: Alberto
* status: 100%
* start-date: 2025/05/20
* end-date: 2025/06/06

#### Description
In order to have a more extensible codebase, refactor the analysis part of the DST analysis
codebase to improve modularity and reusability. Remove code that is tightly coupled 
(Waku-Victoria, Victoria-Vaclab). Allow to switch between monitoring stacks easily, while maintaining
cross-project functionality as independent as possible. Allow new functionality regarding other 
project analysis to be integrated seamlessly.
Also provide examples of usage, and documentation.


#### Deliverables
- PRs:
  - [Github: PR](https://github.com/vacp2p/10ksim/pull/66)
- Related Documents:


### Python deployment scaffold

* fully qualified name: `vac:dst:ift:2025q2-dst-tooling:adapt-experiments`
* owner: Pearson
* status: 75%
* start-date: 2025/06/02
* end-date: 2025/06/20

#### Description
Adapt previous experiments that were realized by DST with the deployment
system created in `vac:dst:ift:2025q2-dst-tooling:python-deployment-scaffold`.
If necessary, realize changes to the code structure to allow better integration
ot the aforementioned experiments, while maintaining adaptability for new ones.

#### Deliverables
- PRs:
  - [Github: PR](https://github.com/vacp2p/10ksim/pull/70)
- Related Documents:
