---
title: Libp2p Evaluation
tags:
  - "2024q4"
  - "dst"
  - "vac"
draft: false
description: "Test libp2p on a regular basis
and look for regressions,
learn scaling properties and run scaling studies,
understand the limits of libp2p and its behaviour.
Deliver hard numbers and actionable insights.
Do this monthly, reliably, with strong documentation of findings."
---

`vac:dst:vac:2024q4-libp2p-evaluation`

## Description
Test libp2p on a regular basis
and look for regressions,
learn scaling properties and run scaling studies,
understand the limits of libp2p and its behaviour.

We want to learn specific, actionable information
about libp2p's behaviour
and how it is evolving over time
with each new release
and with each thing we are specifically asked to check and test.

We will use a combination of real world testing,
theoretical analysis and simulation
to determine and measure the success,
side effects and other factors of libp2p and its evolution.

We will support the Conduit of Expertise narrative directly
by analysing and evaluating new libp2p releases and their features,
both with regards to features they have today
and with regards to how that compares to past behaviour.

We will:

* Enable improvements to libp2p
  by allowing for repeatable, measureable
  and real world insights into libp2p,
  all the way from theory to practice and back.
* Reduce the risk of a libp2p regression
  making it into a new release of our product

Additionally, these efforts will contribute
to the Premier Research destination narrative by:

* Improving and strengthening our relationship with the libp2p team
  and thus increasing the reach and influence of the IFT,
  and improving the chances
  that we successfully grow our ecosystem's products and collaborations
  and especially those we want to work with externally.

## Task List

### Regression testing (recurring)

* fully qualified name: `vac:dst:vac:2024q4-libp2p-evaluation:regression-testing`
* owner: Alberto
* status: Done
* start-date: 2024-10-01
* end-date: 2024-12-31

#### Description
Run different scenarios
and collect evidence and data
of libp2p's behaviour.

Test for known regressions
that have occurred in the past
and ensure they don't happen again.

#### Deliverables
* Analysis done
  * [October report](https://www.notion.so/Nim-libp2p-v1-6-0-regression-testing-October-2024-1308f96fb65c80869c97e373a6c7cfc8)
  * [November report](https://www.notion.so/Nim-libp2p-v1-7-0-regression-testing-November-2024-1518f96fb65c802883ebcfaa1b8b851f)
  * [November report 2](https://www.notion.so/Nim-libp2p-v1-7-1-regression-testing-November-2024-1518f96fb65c80359615e646eaac0c79)
* Report published with all relevant details
* RFC's GitHub issue updated
  with links to the analysis and results.