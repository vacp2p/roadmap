---
title: Libp2p Evaluation
tags:
  - "2025q2"
  - "dst"
  - "vac"
draft: false
description: "Test libp2p on each new version or feature
and look for regressions,
learn scaling properties and run scaling studies."
---

`vac:dst:vac:2025q2-libp2p-evaluation`


## Description

Test libp2p on each new version or requested feature
and look for regressions,
learn scaling properties and run scaling studies,
understand the limits of Waku and its behaviour.
Deliver reports and actionable insights.
Do this monthly, reliably, with documentation of findings.

The scope of this commitment depends on the P2P team
work and improvements, and it is subjected to change.

### Background

We want to learn specific, actionable information
about libp2p's behaviour
and how it is evolving over time
with each new release
and with each thing we are specifically asked to check and test.

We will use a combination of real world testing,
theoretical analysis and simulation
to determine and measure the success,
side effects and other factors of libp2p and its evolution.

### Narrative

We will support the Conduit of Expertise narrative directly
by analysing and evaluating new libp2p releases and their features,
both with regards to features they have today
and with regards to how that compares to past behaviour.

Additionally, these efforts will contribute
to the Premier Research destination narrative by
improving and strengthening our relationship with the libp2p team
and thus increasing the reach and influence of the IFT,
and improving the chances
that we successfully grow our ecosystem's products and collaborations
and especially those we want to work with externally.

### Additional info

## Task list

### Regression testing (recurring)

* fully qualified name: `vac:dst:vac:2025q2-libp2p-evaluation:regression-testing`
* owner: Alberto
* status: recurring
* start-date: 2025-04-01
* end-date: 2025-06-30

#### Description
Run different scenarios
and collect evidence and data
of libp2p's behaviour.

Test for known regressions
that have occurred in the past
and ensure they don't happen again.

#### Deliverables
* Analysis done
  * [Notion: Quic Issues](https://www.notion.so/List-of-Issues-1ca8f96fb65c801b9c9ad4cceb16fa72)
  * [Notion: Nim-libp2p 1.10.0](https://www.notion.so/Nim-libp2p-v1-10-0-regression-testing-May-2025-1f28f96fb65c80d58334f0c1a98ba23b)
* Report published with all relevant details
* RFC's GitHub issue updated
  with links to the analysis and results.

### Mix protocol analysis

* fully qualified name: `vac:dst:vac:2025q2-libp2p-evaluation:mix-analysis`
* owner: Alberto
* status: 100%
* start-date: 2025-05-12
* end-date: 2025-05-16

#### Description
Make use of mix protocol in DST experiments.
Make use of 500~ hundreds of nodes, where some (10~)
of them are using mix protocol.
Study it's behavior, as in message reliability is consistent,
how much latency mix is adding in the network, calculate
how much time a message takes to traverse te mixnet, and
compare same scenario with and without using mix.

#### Deliverables
* Analysis done:
  * [Notion: Mix analysis](https://www.notion.so/Nim-libp2p-Mix-May-2025-1f38f96fb65c800a8466f68472e799db)

### Mix-gossipsub investigation

* fully qualified name: `vac:dst:vac:2025q2-libp2p-evaluation:mix-gossipsub`
* owner: Alberto
* status: 50%
* start-date: 2025-06-02
* end-date: 2025-06-13

#### Description
Investigate mix behavior with gosspsipsub.
Previous results shown that gossipsub instance within a node
might not be getting triggered when a message takes the exit 
route in the mix protocol. 
Detect if this is an error from the analysis, or provide accurate 
information as in the gossipsub instance is handling the message
as it should.

#### Deliverables
* Analysis done:

### IDontWant statistical analysis

* fully qualified name: `vac:dst:vac:2025q2-libp2p-evaluation:idontwant-statistical-analysis`
* owner: Pearson
* status: 15%
* start-date: 2025-06-09
* end-date: 2025-06-20

#### Description
The aim of this task is to model the impact of `IDontWant` 
control messages in the context of Waku scalability research,
as detailed in the following link: [Waku Scalability Research](https://github.com/vacp2p/research/tree/master/waku_scalability).
The first step is to integrate the influence of these control 
messages into the model provided in the reference, 
simplifying where necessary. Any simplifications should be clearly 
explained and justified to ensure a proper understanding of the trade-offs involved.
The focus then shifts to determining the overhead imposed by `IDontWant` control 
messages on the network and subtracting these costs from the total bandwidth
usage to quantify their net benefits in terms of traffic reduction.
In this phase, we can assume that all messages are small and later analyzing
scenarios assuming all messages are large. Latency effects also need to be addressed, 
particularly the case where multiple control messages arrive at varying times. 
To start, the model should simulate situations where three messages are received at once,
while two additional messages arrive later and are discarded by gossipsub
due to their lateness. A refined approach must consider how to reduce these
losses, potentially by introducing a probability distribution to predict 
late arrivals and better handle them in the network.

#### Deliverables
* PRs:
* Documents:

