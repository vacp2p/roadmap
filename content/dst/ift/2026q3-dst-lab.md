---
title: DST Lab
tags:
  - "2026q3"
  - "dst"
  - "ift"
draft: false
description: "Scale and apply the VacLab to IFT's needs.
Anticipate untapped use cases and needs from other teams.
Improve the usage of the lab by optimizing resources and time allocation."
---

`ift-ts:dst:ift:2026q3-dst-lab`

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

### Analyze current stack (recurrent)

* fully qualified name: `ift-ts:dst:ift:2026q3-dst-lab:analyze-current-stack`
* owner: Mamoutou
* status: in progress (25%)
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Compare the current stack with new stack proposals.
Study if changes are helpful and improve overall performance of the lab.
Report findings with analysis and benchmarks of the results.

#### Deliverables
- Code:
  - [vacp2p/vaclab-2#41](https://github.com/vacp2p/vaclab-2/pull/41) Deploy DST Dashboard and Update HomePage
- Reports:
  - [DST Dashboard](https://dashboard.lab.vac.dev) deployed with production and development infrastructure.
  - [DST Dashboard Admin UI](https://api.dashboard.lab.vac.dev/admin/token) protected by Authentik authentication.
  - [VacLab Home](https://lab.vac.dev) updated with dashboard shortcuts and status.
