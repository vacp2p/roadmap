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

### How Fast Is Codex?
> *Note*: This needs more input from project

* fully qualified name: `vac:dst:codex:2025q1-codex-comparison:how-fast-is-codex`
* owner: Wings
* status: 0% // Previously: 0%
* start-date: <yyyy/mm/dd> // Previously: 2024/10/18
* end-date: <yyyy/mm/dd> // Previously: 2024/10/25

#### Description

We will test and compare the following properties in Codex:

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
