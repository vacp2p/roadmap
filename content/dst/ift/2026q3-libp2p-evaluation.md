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
* status: in progress (75%)
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
  - [vacp2p/nim-libp2p#2967](https://github.com/vacp2p/nim-libp2p/pull/2967) fix(kad): keep peer addresses when the admission probe cap is full
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
  - [vacp2p/10ksim#366](https://github.com/vacp2p/10ksim/pull/366) Degraded-network, churn and partition regression scenarios
  - [vacp2p/10ksim#377](https://github.com/vacp2p/10ksim/pull/377) Scrape the settled window for Shadow runs
  - [vacp2p/10ksim#380](https://github.com/vacp2p/10ksim/pull/380) Fix broken imports and add tests for all imports
  - [vacp2p/10ksim#383](https://github.com/vacp2p/10ksim/pull/383) Report Shadow mesh state under load, not at the end of the run
  - [vacp2p/dst-libp2p-test-node#43](https://github.com/vacp2p/dst-libp2p-test-node/pull/43) Ping every connection until traffic starts
  - [vacp2p/10ksim#386](https://github.com/vacp2p/10ksim/pull/386) Record the image digest the nodes actually pulled
  - [vacp2p/10ksim#387](https://github.com/vacp2p/10ksim/pull/387) Bound the publish request and fail a run that lost messages
  - [vacp2p/10ksim#375](https://github.com/vacp2p/10ksim/pull/375) Stop dropping deliveries whose measured delay is negative
  - [nimble#1837](https://github.com/nim-lang/nimble/issues/1837) Nimble lockfile URL bug
  - [dst-libp2p-test-node#50](https://github.com/vacp2p/dst-libp2p-test-node/pull/50) Nim-libp2p regression node 2.1.6
  - [dst-libp2p-test-node#51](https://github.com/vacp2p/dst-libp2p-test-node/pull/51) Update lockfile for v2.1.6
  - [dst-libp2p-test-node#52](https://github.com/vacp2p/dst-libp2p-test-node/pull/52) Nim-libp2p regression node 2.2.1
  - [dst-libp2p-test-node#53](https://github.com/vacp2p/dst-libp2p-test-node/pull/53) Nim-libp2p regression 2.3.1
  - [dst-libp2p-test-node#46](https://github.com/vacp2p/dst-libp2p-test-node/pull/46) Improve regression node
  - [dst-libp2p-test-node#49](https://github.com/vacp2p/dst-libp2p-test-node/pull/49) Update README.md with tags info
  - [dst-libp2p-test-node#54](https://github.com/vacp2p/dst-libp2p-test-node/pull/54) Fix regression build
  - [dst-libp2p-test-node#55](https://github.com/vacp2p/dst-libp2p-test-node/pull/55) Nim-libp2p regression 2.4.0
  - [10ksim#390](https://github.com/vacp2p/10ksim/pull/390) Cross-check log-derived delivery against the nodes' received counter
  - [10ksim#389](https://github.com/vacp2p/10ksim/pull/389) Capture pod logs with the run as a collector fallback
  - [10ksim#388](https://github.com/vacp2p/10ksim/pull/388) Verify each scenario's disturbance actually happened
  - [10ksim#384](https://github.com/vacp2p/10ksim/pull/384) Read a scrape's metric folder as well as a plain CSV path
  - [10ksim#392](https://github.com/vacp2p/10ksim/pull/392) Write scraped CSVs with a .csv suffix
- Reports:
  - [Regression testing rulebook](https://app.notion.com/p/39b8f96fb65c809e9fa7fdb075c30cfc)
  - [Nim-libp2p v2.2.0 Regression Report](https://app.notion.com/p/3978f96fb65c8042ae7dd621decae98a)
  - [Nim-libp2p v2.3.0 Regression Report](https://app.notion.com/p/Nim-libp2p-v2-3-0-Regression-Report-39b8f96fb65c80519e7ef2fc97683811)


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
