---
title: VacLab
tags:
  - "2025q2"
  - "dst"
  - "ift"
draft: false
description: "Scale and apply the VacLab to IFT's needs.
Anticipate untapped use cases and needs from other teams.
Improve the usage of the lab by optimizing resources and time allocation."
---

`vac:dst:ift:2025q2-vaclab`

## Description
Vaclab will enable large-scale simulations and deployments.
This involves chores like the maintenance of the lab,
software updates and replacements if it does not meet the requirements,
monitoring systems and independent core contributor virtual machine
assigment with maintenance.
Also, tools for increasing the speed and quality of life for
core contributors will be implemented. These tools will be related
to a better usage of the resources available in the lab,
both in computer intensive tasks and parallel workload.

### Background
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
 
### Concurrent experiments

* fully qualified name: `vac:dst:ift:2025q2-vaclab:concurrent-experiments`
* owner: Wings
* status: Suspended
* start-date: 2025/04/01
* end-date: 2025/04/05

#### Description

Make sure that within the same automated deployment,
if the lab has room to run several experiments at the same time,
the lab resources could be used efficiently to increase
the number of experiments concurrently.
The scope of this task will remain under the scope of the same deployment,
not taking into account several deployments. This will be enhanced in 
other task, where different approaches like a queueing system could 
be used.

#### Deliverables
- Code:
- Documentation:

### Queueing system

* fully qualified name: `vac:dst:ift:2025q2-vaclab:queueing-system`
* owner: Wings
* status: Suspended
* start-date: 2025/04/07
* end-date: 2025/04/18

#### Description

Create a queueing system, or something alike, that can perform
a similar functionality. The scope of this automated utility can
group different kind of deployments. 
A priority system should also be taken into consideration, 
where a mix between when the deployment was required,
and the amount of resources it would need needs to be taken into account.

#### Deliverables
- Code:
  - https://github.com/vacp2p/dst-lars
  - https://github.com/Zorlin/larstesting
- Documentation:

### Better Time Slicing

* fully qualified name: `vac:dst:ift:2025q2-vaclab:better-time-slicing`
* owner: Wings
* status: Suspended
* start-date: <yyyy/mm/dd>
* end-date: <yyyy/mm/dd>

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

* fully qualified name: <vac:dst:ift:2025q2-vaclab:automation-uplift>
* owner: Wings
* status: Suspended
* start-date: <yyyy/mm/dd>
* end-date: <yyyy/mm/dd>

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