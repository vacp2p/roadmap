---
title: VacLab
tags:
  - "2025q1"
  - "dst"
  - "ift"
draft: false
description: "Scale and apply the VacLab to IFT's needs.
Anticipate untapped use cases and needs from other teams."
---

`vac:dst:ift:2025q1-vaclab`

## Description
Vaclab will enable large-scale simulations and deployments.
This involves chores like the maintenance of the lab,
software updates and replacements if it does not meet the requirements,
monitoring systems and independent core contributor virtual machine
assigment with maintenance.

### Background
[Vaclab 2024](2024q4-vaclab.md)
The VacLab, provided by Riff Labs Limited,
supports the Vac team
by enabling large-scale simulations
and deployments of distributed systems.
As VacLab matures,
we aim to maximize its use for IFT research,
testing, and quality control.
Initially, VacLab will operate
as an IaaS service
developed in collaboration with Riff Labs,
ensuring reliability. 
Over time, we plan to evolve 
into a PaaS or SaaS model,
enabling teams to access resources
without managing infrastructure.

VacLab will accelerate IFT development
by offering self-service testing,
enhancing efficiency and reducing costs
compared to cloud services.
By leveraging many smaller,
low-cost nodes and building resilience
against hardware failures,
VacLab provides a reliable environment for experimentation.


### Narratives

VacLab supports the Conduit of Expertise by
lowering infrastructure barriers
for IFT teams and offering flexible,
cost-effective resources,
encouraging extensive testing
and simulation across teams
within DST's capacity.

It also supports the Premier Research narrative
by making non-sensitive telemetry
and metrics publicly accessible,
promoting transparency and collaboration.

### Additional info

## Task List
 
### Better Time Slicing
> *Note*: Will be moved to Q2

* fully qualified name: `vac:dst:ift:2025q1-vaclab:better-time-slicing`
* owner: Wings
* status: 0%
* start-date: <yyyy/mm/dd> // Previously: 2024/12/01
* end-date: <yyyy/mm/dd> // Previously: 2024/12/14

#### Description
Optimize the scheduling and allocation of lab resources
to maximize their efficient use. 
Where possible, make the lab available for running
multiple tasks in parallel, 
balancing workloads to make the most of available lab capacity.
Detect if multiple users are affecting each other, 
and ensure that the projects can share infrastructure.

#### Deliverables
* A report on the current state of time slicing in the lab.
* A plan for how to improve time slicing in the lab.
* A timeline for implementing the plan.
* Measurable improvements in usage of the lab
  that aims for an initial target of 25% of real world time
  being used for useful workloads and tests

Later repeats in the VacLab commitment will aim to improve this to 50%,
then 75%, then as far as possible
to the limits of the underlying infrastructure and our actual needs.

### Automation Uplift
<!-- technically sort of external
and will be done outside of normal DST cadence
but will be managed so as not to disrupt other works
-->
> *Note*: Will be moved to Q2

* fully qualified name: <vac:dst:ift:2025q1-vaclab:automation-uplift>
* owner: Wings
* status: 0%
* start-date: <yyyy/mm/dd> // Previously: 2024/12/01
* end-date: <yyyy/mm/dd> // Previously: 2024/12/31

#### Description
Significantly improve the automation and management of the VacLab,
freeing up resources for Wings to focus on other work.

#### Deliverables
- [ ] Full automation for anything we know needs doing regularly
  - [ ] Automated patching for security updates (Debian, Authentik, SeaweedFS)
  - [ ] Secure key management and rotation automation (for SSH keys)
- [ ] A report on what was learned in this process
      and how we believe it improved VacLab support and operations
  - What was automated? Why? What did that change?
  - What remains manual and needs improving?
- [ ] Improvements to the lab that are documented, implemented and recorded.

### Deployment utilities

* fully qualified name: `vac:dst:ift:2025q1-vaclab:deployment-utilities`
* owner: Wings
* status: 100%
* start-date: 2025/03/17
* end-date: 2025/03/28

#### Description

Help the DST team to automatize the deployment of experiments.
Investigate and decide the best way to automatically perform
experiments, setting up different scenarios, and allowing
important parameters to be also modifiable.
Also, if the experiments require a post analysis, automatically
trigger the needed post-experiments scripts in the correspondant experiment.
This will be as abstract as possible, as there can be different
experiments for different other units that DST can be working on.

#### Deliverables
- Notion report with example:
- Code:
  - [Github Repo](https://github.com/vacp2p/dst-argo-workflows)
- Documentation:
  - [Notion notes](https://www.notion.so/Argo-Workflow-Automation-1bf8f96fb65c804f948ed9dbb279fa77)

### Concurrent experiments
> *Note*: End time is an estimation, still needs to be coordinated

* fully qualified name: `vac:dst:ift:2025q1-vaclab:concurrent-experiments`
* owner: Wings
* status: 100%
* start-date: 2025/03/24
* end-date: 2025/03/31

#### Description

Allow different experiments to be run at the same time.
In order to do this, create a process or automatically
estimate how much resources an experiment will need,
and if there are enough resources to run several experiments
at the same time, trigger them.
A report with an example baseline of this could be done either
with nimlibp2p or waku.

#### Deliverables
- Notion report with example:
- Code:
  - [Github Repo](https://github.com/vacp2p/dst-argo-workflows/blob/43d5b8b556aa5011fc865956c97d4d35d80a2a97/prefect/run.py#L604-L610)
- Documentation:
  - [Notion notes](https://www.notion.so/Argo-Workflow-Automation-1bf8f96fb65c804f948ed9dbb279fa77)