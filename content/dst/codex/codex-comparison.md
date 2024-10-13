---
title: Codex Comparison
tags:
  - "2024q4"
  - "dst"
  - "codex"
draft: false
description: "Measure Codex against BitTorrent and see how it compares."
---

`vac:dst:codex:codex-comparison`

Measure Codex against BitTorrent.

## Description
We will assist Codex with creating a comparison against other systems -
for this initial phase, BitTorrent -
to see how it performs in comparison.

Together we will compare on things such as:
* Time to first byte
* Bandwidth usage
* Stability
* Reliability

We'll provide space and tools for Codex to build a speed test
comparing download speeds of Codex against other systems.
This will allow us to understand where Codex needs improvement
and where it stands right now in terms of suitability for different use cases.

We will support the Conduit of Expertise narrative directly
by providing valuable insights to Codex
that allow them to understand how Codex performs
in comparison to common and popular systems in the "altruistic" space.

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

## Task List

### Matrices Deployments

* fully qualified name: <vac:dst:codex:codex-comparison:matrices-deployments>
* owner: Wings
* status: 50%
* start-date: 2024/10/01
* end-date: 2024/10/18

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
such as nwaku and gowaku, to exist and interact
in the course of a single test.

#### Deliverables
* Example Helm charts or Kustomize for deploying Codex.
* Customisations to those Helm or Kustomize charts that allow tuning them to meet specific scenarios such as number of nodes, amount of data.
* Automated systems for running a matrix of tests and measuring them.

This will build on prior work by DST that benefits from this work as well (ArgoCD work).
