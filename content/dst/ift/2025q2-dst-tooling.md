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
Among tools that can be useful, we consider deployment utilities
to facilitate the launch of experiments, general log parser for
project analysis, and any other kind of utilities that may
appear depending on the needs of the projects.

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
* status: 0%
* start-date: 2025/05/12
* end-date: 2025/05/23

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
- Related Documents:
