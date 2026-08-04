---
title: Libp2p Evaluation
tags:
  - "2026q3"
  - "dst"
  - "ift"
draft: false
description: "Test libp2p on each new version or feature
and look for regressions,
learn scaling properties and run scaling studies."
---

`ift-ts:dst:ift:2026q3-libp2p-evaluation`


## Description

Test libp2p on each new version or requested feature
and look for regressions,
learn scaling properties and run scaling studies,
understand the limits of Waku and its behaviour.
Deliver reports and actionable insights.
Do this monthly, reliably, with documentation of findings.

The scope of this commitment depends on the P2P team
work and improvements, and it is subjected to change.

## Task list
> Schedule note: Dates reflect quarter bounds; update when actual timing is known.

### Regression testing (recurring)

* fully qualified name: `ift-ts:dst:ift:2026q3-libp2p-evaluation:regression-testing`
* owner: Alan
* status: in progress (50%)
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Run different scenarios
and collect evidence and data
of libp2p's behaviour.

Test for known regressions
that have occurred in the past
and ensure they don't happen again.

#### Deliverables
- Code:
  - [vacp2p/10ksim#362](https://github.com/vacp2p/10ksim/pull/362) Generate latency plots from the regression pipeline
  - [vacp2p/10ksim#370](https://github.com/vacp2p/10ksim/pull/370) Move the box plot legend outside the axes
  - [vacp2p/dst-libp2p-test-node#42](https://github.com/vacp2p/dst-libp2p-test-node/pull/42) Shadow quic: floor lsquic engine tick re-arms
  - [vacp2p/10ksim#356](https://github.com/vacp2p/10ksim/pull/356) k8s: optional bandwidth cap on the network-delay init container
  - [vacp2p/10ksim#358](https://github.com/vacp2p/10ksim/pull/358) Regression analysis: plot delivery latency as a CDF
  - [vacp2p/10ksim#360](https://github.com/vacp2p/10ksim/pull/360) shadow: give relays a realistic IP plan
  - [vacp2p/10ksim#361](https://github.com/vacp2p/10ksim/pull/361) metrics: track mesh degree and connections as first-class gauges
  - [vacp2p/10ksim#353](https://github.com/vacp2p/10ksim/pull/353) Shadow WAN network model
  - [vacp2p/10ksim#359](https://github.com/vacp2p/10ksim/pull/359) nimlibp2p: outlast a metrics scrape before teardown
  - [vacp2p/10ksim#352](https://github.com/vacp2p/10ksim/pull/352) k8s: scrape gossipsub detail from cluster regression runs
  - [vacp2p/10ksim#316](https://github.com/vacp2p/10ksim/pull/316) shadow-gossipsub: select muxer and discovery (static | kad-dht)
  - [vacp2p/10ksim#351](https://github.com/vacp2p/10ksim/pull/351) Shadow: scrape gossipsub control/efficiency metrics
- Reports:
  - [Regression testing rulebook](https://app.notion.com/p/39b8f96fb65c809e9fa7fdb075c30cfc)
  - [Nim-libp2p v2.2.0 Regression Report](https://app.notion.com/p/3978f96fb65c8042ae7dd621decae98a)


### Interop at scale

* fully qualified name: `ift-ts:dst:ift:2026q3-libp2p-evaluation:interop-at-scale`
* owner: TBD
* status: not started
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Run different scenarios
and collect evidence and data
of libp2p's behaviour using 
different implementations.


#### Deliverables
- Code:
- Reports:
