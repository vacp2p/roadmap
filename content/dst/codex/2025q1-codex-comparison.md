---
title: Codex Comparison
tags:
  - "2025q1"
  - "dst"
  - "codex"
draft: false
description: "Measure Codex against BitTorrent and see how it compares."
---

`vac:dst:codex:2025q1-codex-comparison`


## Description
We will assist Codex
with creating a comparison against other systems -
for this initial phase, BitTorrent -
to see how it performs in comparison.

Together we will compare on things such as:
* Time to first byte
* Bandwidth usage
* Stability
* Reliability

We'll provide space and tools for Codex to build a speed test
comparing download speeds of Codex against other systems.

Specifically, we will:

* Provide solutions for running the many complicated tests that Codex will need to perform.
  * This will be in the form of automated deployment (ArgoCD)
  * And matrices test deployment systems (via Matrices Deployments / Argo Workflow)
  * And measurements (Prometheus, Grafana, VictoriaMetrics)
  * Assistance with building a set of Helm charts that, together, form the test harness.
  * Assistance with questions as to the best way to approach each subtask.
* Allow Codex access to Kubernetes to run the tests.
* Assist with, observe and help reason about the results of the testing.

Finally, together we'll help in writing the final report at the end of the process.

### Background

### Narratives

We will support the Conduit of Expertise narrative directly
by providing valuable insights to Codex
that allow them to understand how Codex performs
in comparison to common and popular systems in the "altruistic" space.

### Additional info
This commitment has been rescheduled
from 2024Q4 to 2025Q1
due to unforeseen circumstances, 
including an extended sick leave of a CC.

## Task List

### Matrices Deployments

* fully qualified name: `vac:dst:codex:2025q1-codex-comparison:matrices-deployments`
* owner: Wings
* status: 0% // Previously: 90%
* start-date: <yyyy/mm/dd> // Previously: 2024/10/01
* end-date: <yyyy/mm/dd> // Previously: 2024/10/18

#### Description

Expand upon the current deployment work
that uses Kubernetes manifests
to deploy and measure complex simulations
by implementing a combination of ArgoCD or some similar deployment tool,
and standardised Helm, Kustomize or plain manifests,
and devise a way to both script and control simulations
in a repeatable, easy way.

Build a system that can deploy and measure
a matrix of different scenarios and configurations.

It must allow multiple unrelated deployments,
to exist and interact
in the course of a single test.

#### Deliverables
* Example Helm charts or Kustomize for deploying Codex.
* Customisations to those Helm or Kustomize charts that allow tuning them to meet specific scenarios such as number of nodes, amount of data.
* Automated systems for running a matrix of tests and measuring them.

This will build on prior work by DST that benefits from this work as well (ArgoCD work).

#### Status
* We have working deployments for Waku, which will be adapted to Codex soon
* We have a theoretically working system for matrices deployments, with a few tweaks and tests needed

### How Fast Is Codex?

* fully qualified name: <vac:dst:codex:2025q1-codex-comparison:how-fast-is-codex>
* owner: Wings
* status: 0% // Previously: 0%
* start-date: <yyyy/mm/dd> // Previously: 2024/10/18
* end-date: <yyyy/mm/dd> // Previously: 2024/10/25

#### Description

Related to Codex Comparison, 
we simply want to find out fast Codex is, at various things 
under different kinds of stress and load.

We will use the Base Capacity.

We will test and compare the following:

* Upload speed (1 client)
* Download speed
* Time to first byte
* Time to 50%
* Time to 90%
* Time to 100

We would also like to collect all data from the items in this matrix:

**Benchmark conditions**:
  * total size: 2, 8, 16, 32
  * seeders: 1, 2, 4, 8, 16
  * file size: 
      100
     MB, 
      1
     GB, 
      5
     GB

#### Deliverables

- [ ] Reports from how each item in the matrix performed.
- [ ] A general writeup


### ArgoCD Or Similar

* fully qualified name: <vac:dst:codex:2025q1-codex-comparison:argocd-or-similar>
* owner: Wings
* status: 0% // Previously: 95%
* start-date: <yyyy/mm/dd> // Previously: 2024/10/04
* end-date: <yyyy/mm/dd> // Previously: 2024/12/31

#### Description

Get ArgoCD or a similar tool up and running.

Use it to demonstrate deploying a simulation from a Git repo
with a Helm chart or plain manifests in it.

#### Deliverables

* The demonstrated ability to run a simulation.
* Deployed Codex comparison test harness.

#### Status
* We have demonstrated the ability to run simulations, spawning a deployment from a GitHub issue
* Deploying a Codex comparison harness is next
* as is full documentation.

### Working Matrices

* fully qualified name: <vac:dst:codex:2025q1-codex-comparison:working-matrices>
* owner: Wings
* status: 0% // Previously 90%
* start-date: <yyyy/mm/dd> // Previously: 2024/10/04
* end-date: <yyyy/mm/dd> // Previously: 2024/12/31

#### Description

Ensure that deployment matrices work once `ArgoCD Or Similar` is completed.

Test some basic deployments and record findings.

#### Deliverables

* A report on the findings of the tests and the current state of the deployment matrices.
* A deployment matrix tool or set of instructions/documentation.
* Deployments tested and working with a 3x3 matrix of different configurations.
* Used by us or Codex to test Codex and answer questions about it.

#### Status
* We have a working system for matrices deployments, with a few tweaks and tests needed
* Needs heterogeneous support added