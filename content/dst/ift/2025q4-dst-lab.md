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
* status: in progress (0%)
* start-date: 2025/10/24
* end-date: 2025/12/05

#### Description
We want a local replica of the DST lab so that tests and changes can be tried out 
safely before they reach the main environment. This local setup mirrors the 
structure of the real lab.
We want to have the same monitoring system, while also having public endpoints that
allow us to test functionalities of data analysis (Prometheus) or log parsing (VictoriaLogs).
Provide all needed resources to do this deployment, and also document how it can be used.

#### Deliverables
- Code:
- Reports:


### Lab duplication

* fully qualified name: `vac:dst:ift:2025q4-dst-lab:lab-duplication`
* owner: Mamoutou
* status: in progress (0%)
* start-date: 2025/12/01
* end-date: 2025/12/31

#### Description
Gather information and take as reference the current structure of the DST lab
to create a new setup.
Document what is the current stack of the lab, what is the plan for the new setup,
and also note what are the changes/improvements that are done in the stack, so everything
is documented for future reference.

#### Deliverables
- Code:
- Reports: