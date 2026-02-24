---
title: DST Lab
tags:
  - "2026q1"
  - "dst"
  - "ift"
draft: false
description: "Scale and apply the VacLab to IFT's needs.
Anticipate untapped use cases and needs from other teams.
Improve the usage of the lab by optimizing resources and time allocation."
---

`ift-ts:dst:ift:2026q1-dst-lab`

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

### Lab deployment code

* fully qualified name: `ift-ts:dst:ift:2026q1-dst-lab:lab-deployment-code`
* owner: Mamoutou
* status: done
* start-date: 2026/01/05
* end-date: 2026/02/10

#### Description
Complete the deployment and configuration of the remaining lab components using fleet, 
and deliver a one-click Ansible playbook that fully provisions and configures the 
new DST lab in a repeatable, automated way.
Also, update BW resources during the scheduling cycle to avoid race conditions.

#### Deliverables
- Code:
  - [vacp2p/vaclab-2#3](https://github.com/vacp2p/vaclab-2/pull/3) Add Lab Components - Part 1
- Reports:
  - [Notion: Vaclab 2.0 - Full Software Stack: Physical Infra Layer](https://www.notion.so/Vaclab-2-0-Full-Software-Stack-2d08f96fb65c8008abfdcfe86a2c3324?source=copy_link#2dc8f96fb65c809eaa4ef61286c663c2)


### Analyze current stack

* fully qualified name: `ift-ts:dst:ift:2026q1-dst-lab:analyze-current-stack`
* owner: Mamoutou
* status: in progress (95%)
* start-date: 2026/01/01
* end-date: 2026/03/31

#### Description
Compare the current stack with new stack proposals.
Study if changes are helpful and improve overall performance of the lab.
Report findings with analysis and benchmarks of the results.

#### Deliverables
- Fixed metal-01 pods internet issues (by restarting kubernetes and kube-proxy)
- Scheduled Grafana an Authentik on the master node (using soft affinity weight => k3s will rescheduled on other nodes in case of issues)
- [Notion: Current Vaclab Scheduler Benchmark](https://www.notion.so/Vaclab-2-0-Bandwidth-Aware-Scheduling-2d08f96fb65c804eb44fdc7b75e079f9?source=copy_link#2d88f96fb65c80f0ba35f55c22b87692)
- Added tags to longhorn storage and nodes (for automatic definition of secondary data disk)
- Updated Storage Classes to use only worker nodes as storage for monitoring components (using longhorn NodeSelector) and enabled data-locality for components scheduled on master node
- Created Grafana panels to vizualise vaclab scheduler metrics
- Code:
  - [vacp2p/vaclab-2#11](https://github.com/vacp2p/vaclab-2/pull/11) Improve Runtime Settings
  - [vacp2p/vaclab-2#6](https://github.com/vacp2p/vaclab-2/pull/6) Add External DST Node
  - [status-im/infra-misc#457](https://github.com/status-im/infra-misc/pull/457) vacdst: Open Required Ports for Kube-OVN CNI
- Reports:
  - [Notion: External node as K3S Master - System Components Traffic Share](https://www.notion.so/External-node-as-K3S-Master-2fe8f96fb65c80a49316ec4a3841f317?source=copy_link#3098f96fb65c80b5b713e86c4ddaa749)
  - [Google Slides: DST Kubernetes Cluster](https://docs.google.com/presentation/d/1-L_hxYv61fVA_n5nBKLw8cMpZUzB0ilx/edit?usp=sharing&ouid=103968234498493387312&rtpof=true&sd=true)
  - [Recording: DST Kubernetes Cluster](https://drive.google.com/file/d/1CiEujizGM9QO12s_Zo4d0ZWt-uMdci5w/view)
  - [Notion: Vaclab 2.0 - Iperf Bandwidth Measurements](https://www.notion.so/Vaclab-2-0-Iperf-Bandwidth-Measurements-2f88f96fb65c808d88d9c53b595f3326)
- Other:
  - Deployed vaclab-2 stack on available nodes, exposed lab.vac.dev, and validated basic workloads


### Optimize data scrapping

* fully qualified name: `ift-ts:dst:ift:2026q1-dst-lab:optimize-data-scrapping`
* owner: Mamoutou
* status: done
* start-date: 2026/02/02
* end-date: 2026/02/24

#### Description
Improve the monitoring system of the lab. Adjust scraping frequency and selected metrics.
Design a storage solution to store the data so it can be retrieved if necessary.
Optimize the storage to reduce used space if data is older than a certain period.

#### Deliverables
- [vacp2p/vaclab-2#5](https://github.com/vacp2p/vaclab-2/pull/5)
- [Notion: Vaclab 2.0 - Full Software Stack #Getting Metrics and Logs](https://www.notion.so/Vaclab-2-0-Full-Software-Stack-2d08f96fb65c8008abfdcfe86a2c3324?source=copy_link#2dd8f96fb65c80c9909af30df5726e26)
- Code:
- Reports:


### Lab health monitoring

* fully qualified name: `ift-ts:dst:ift:2026q1-dst-lab:lab-health-monitoring`
* owner: Mamoutou
* status: in progress (25%)
* start-date: 2026/02/02
* end-date: 2026/02/13

#### Description
Design a set of metrics/dashboards that can be used to monitor the health of the lab.
The metrics should be useful to detect abnormal behaviors and to detect potential issues.
What we want to achieve with this is to be sure that we can compare experiments from one
week to a different week being confident that the results can be trusted, without the need
of repeat the same experiment again.

#### Deliverables
- [Notion: Vaclab 2.0 - Health Monitoring](https://www.notion.so/Vaclab-2-0-Health-Monitoring-30d8f96fb65c80e9b69ec23c03045d2a)
- Code:
- Reports:


### Fleet workshop

* fully qualified name: `ift-ts:dst:ift:2026q1-dst-lab:fleet-workshop`
* owner: Mamoutou
* status: done
* start-date: 2026/02/05
* end-date: 2026/02/17

#### Description
Prepare a workshop to teach fleet basics to infra-team.

#### Deliverables
- Slides:
  - [Google Slide: Rancher Fleet Tuto](https://docs.google.com/presentation/d/13rNYB4mRKB587WmAlQlDm6gXYsZZCz1M/edit?usp=sharing&ouid=103968234498493387312&rtpof=true&sd=true)
- Presentation:
  - [mamoutou-diarra/rancher-fleet-tuto](https://github.com/mamoutou-diarra/rancher-fleet-tuto) Rancher Fleet Hands-On Tutorial
