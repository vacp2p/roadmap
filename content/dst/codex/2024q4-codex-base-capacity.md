---
title: Codex Base Capacity
tags:
  - "2024q4"
  - "dst"
  - "codex"
draft: false
description: "Provide base capacity for Codex and keep it reliable.
Study its behaviour in the process of supporting it."
---

`vac:dst:codex:2024q4-codex-base-capacity`

## Description
Provide base capacity for Codex and keep it reliable.
Study its behaviour in the process of supporting it.

We will allow Codex to scale to support large scale use cases,
test how it behaves in large 100TB+ testnet deployments,
and in various deployment setups.

We will support the Conduit of Expertise narrative directly
by providing valuable insights to Codex
and the ability to theorise, reason about,
test, measure and improve
the performance, stability and scalability of Codex.

These efforts will contribute in these ways to the Conduit of Expertise narrative:

* Accelerate adoption and development and productising of Codex
  by providing support to the Codex team
  in the form of real world testing
  to improve their efficiency and effectiveness
  in building a better product.

* Improve the RFC culture
  by allowing for faster and easier development of RFCs
  with the aid of rapidly accelerated insights
  into how an RFC in development will perform
  as it's being expanded and going through the draft process.

* Allow easier post-mortem analysis
  of the success or relative performance of a given RFC -
  does this change use more or less bandwidth?
  Did it improve things?
  Seeing the effects of changes at scale
  allows for a greater ability to usefully wrap up work on
  and conclude an RFC process
  and document and absorb what we learned
  in the process into further improvements.

Further, we will contribute both directly and indirectly
to the Premier Research destination narrative
by helping Codex build a stable base
on which other research and interesting use cases can be built.

## Task List

### Production Quality Base Capacity

* fully qualified name: <vac:dst:codex:2024q4-codex-base-capacity:deploy-base-capacity>
* owner: Wings
* status: 0%
* start-date: 2024/10/05
* end-date: 2024/10/31

#### Description

We have deployed a large set of base capacity to the Codex testnet. Now we need to keep it online, stable and prevented from losing data where possible.

It consists of 50x nodes with 10xTB of data each for now.

#### Deliverables

<!--
* Helm chart adapted to Vaclab and used to deploy the nodes.
* 50x nodes running and adopted into the testnet.
-->
* Downloads/uploads tested and working for at least 3 selected nodes.
* 🚧 Ongoing monitoring (not a one time thing)
* ✅ 500TB of overall capacity provided to the network
