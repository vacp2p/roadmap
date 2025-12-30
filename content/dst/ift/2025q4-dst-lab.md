---
title: DST Lab
tags:
  - "2025q4"
  - "dst"
  - "ift"
draft: false
description: "Scale and apply the VacLab to IFT's needs.
Anticipate untapped use cases and needs from other teams.
Improve the usage of the lab by optimizing resources and time allocation."
---

`vac:dst:ift:2025q4-dst-lab`

## Description

DST lab is a set of machines that are mainly used in a composed Kubernetes cluster.
In this environment, we can do a set of experiments to test regressions,
new functionalities and features, or experimental changes on any decentralized system.
In these experiments, we look for abnormal behaviors, we do measurements to study
the performance and robustness of the system. These results can be also used to compare
with theoretical results and analyze the scaling behaviors of the systems.
At the same time, we will work on improving the lab's resources and time allocation,
while allow provisioning to other teams dedicated machines if they are needed.


## Task list

### Local lab

* fully qualified name: `vac:dst:ift:2025q4-dst-lab:local-lab`
* owner: Mamoutou
* status: done
* start-date: 2025/10/24
* end-date: 2025/12/16

#### Description
We want a local replica of the DST lab so that tests and changes can be tried out 
safely before they reach the main environment. This local setup mirrors the 
structure of the real lab.
We want to have the same monitoring system, while also having public endpoints that
allow us to test functionalities of data analysis (Prometheus) or log parsing (VictoriaLogs).
Provide all needed resources to do this deployment, and also document how it can be used.

#### Deliverables
- Code:
  - [Created vaclab-local repository with local lab setup](https://github.com/vacp2p/vaclab-local/pull/1)
  - [Exclude system namespaces and import remaining dashboards](https://github.com/vacp2p/vaclab-local/pull/2)
- Reports:
  - [Notion vaclab-local documentation: Local Vaclab usage information](https://www.notion.so/Local-Vaclab-usage-information-2c38f96fb65c80dd9e7df7294fdbdf72)


### Lab duplication

* fully qualified name: `vac:dst:ift:2025q4-dst-lab:lab-duplication`
* owner: Mamoutou
* status: done
* start-date: 2025/12/01
* end-date: 2025/12/30

#### Description
Gather information and take as reference the current structure of the DST lab
to create a new setup.
Document what is the current stack of the lab, what is the plan for the new setup,
and also note what are the changes/improvements that are done in the stack, so everything
is documented for future reference.

#### Deliverables
- Code:
- Reports:
  - [Notion: Vaclab 2.0 - Bandwidth-Aware Scheduling](https://www.notion.so/Vaclab-2-0-Bandwidth-Aware-Scheduling-2d08f96fb65c804eb44fdc7b75e079f9)
  - [Notion: CNI Comparison for reproducible P2P Experiments](https://www.notion.so/Vaclab-2-0-Multi-tenancy-Pod-Networking-2c98f96fb65c817c819ffc0923d28092?source=copy_link#2c98f96fb65c814d9978cd0246c61e06)
  - [Notion: Vaclab 1.0 - Current Stack](https://www.notion.so/Vaclab-1-0-Current-Stack-2c98f96fb65c8020abadfcb9494a9711)
  - [Notion: Vaclab 2.0 - Multi-tenancy & Pod Networking](https://www.notion.so/Vaclab-2-0-Multi-tenancy-Pod-Networking-2c98f96fb65c817c819ffc0923d28092)
