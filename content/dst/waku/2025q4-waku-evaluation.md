---
title: Waku Evaluation
tags:
  - "2025q4"
  - "dst"
  - "waku"
draft: false
description: "Test Waku on each new version or requested feature
and look for regressions,
learn scaling properties and run scaling studies."
---

`vac:dst:waku:2025q4-waku-evaluation`

## Description
Test Waku on each new version or requested feature
and look for regressions,
learn scaling properties and run scaling studies,
understand the limits of Waku and its behaviour.
Deliver reports and actionable insights.
Do this monthly, reliably, with documentation of findings.

### Background

We want to learn specific, actionable information
about Waku's behaviour
and how it is evolving over time
with each new release
and with each thing we are specifically asked to check and test.

We will use a combination of real world testing,
theoretical analysis and simulation
to determine and measure the success,
side effects and other factors of Waku and its evolution.

## Task list

### Regression testing (recurring)

* fully qualified name: `vac:dst:waku:2025q4-waku-evaluation:regression-testing`
* owner: Alberto/Farooq
* status: in progress (70%)
* start-date: 2025/10/01
* end-date: 2025/12/31

#### Description
Run different scenarios
and collect evidence and data
of Waku's behaviour.

Test for known regressions
that have occurred in the past
and ensure they don't happen again.

Schedule note: Dates reflect quarter bounds; update when actual timing is known.
#### Deliverables
- Reports:
- [nwaku regression testing v0.37 findings](https://www.notion.so/nwaku-regression-testing-v0-37-October-2025-29c8f96fb65c80de9314c66dd3698b69)
- [Waku regression testing v0.37 – November 2025](https://www.notion.so/Waku-regression-testing-v0-37-November-2025-2b18f96fb65c80ec8f54d4eee93fabb7)
- [nWaku v0.37 regression report: Mixed environment](https://www.notion.so/Waku-v0-37-Bandwidth-Conasumption-Analysis-November-2025-2b58f96fb65c804fbe17ec493b827130)
- Related PRs if apply:


### Quic-vs-tcp

* fully qualified name: `vac:dst:waku:2025q4-waku-evaluation:quic-vs-tcp`
* owner: Alberto
* status: not started
* start-date: 2025/10/01
* end-date: 2025/12/31

#### Description

Perform a comparison between Waku using quic and waku using mplex and yamux.

Schedule note: Dates reflect quarter bounds; update when actual timing is known.
#### Deliverables
- Reports:
- Related PRs if apply:


### nWaku API docker image

* fully qualified name: `vac:dst:waku:2025q4-waku-evaluation:nwaku-api-image`
* owner: TBD
* status: not started
* start-date: 2025/10/01
* end-date: 2025/12/31

#### Description

Merge all utilities from DST/nWaku into a single docker image.
This involves images that are used to interact with store, filter and lightpush protocols.
It should be investigated if adding the Waku publisher here is also a useful idea.
Documentation and code clarity is required, as this could be used by the waku team, or other projects.

Schedule note: Dates reflect quarter bounds; update when actual timing is known.
#### Deliverables
- Reports:
- Related PRs if apply:



### nWaku v0.37 bandwidth regression

* fully qualified name: `vac:dst:waku:2025q4-waku-evaluation:nwaku-v0.37-bandwidth-regression`
* owner: Farooq
* status: in progress (75%)
* start-date: 2025/11/27
* end-date: 2025/12/12

#### Description
Set a baseline 1K nodes 1msg/s 1KB scenario with only relay nodes, + 3 bootstrap nodes.
Get per a complete per protocol metric plots with the image provided by Waku. The plots in 
the v0.37 notion report have missing protocols.
After the previous run, do another one with rendezvous set to False. This protocol metric 
should appear in the previous point plots, if it is not there, check why. 
Also, check if this flag affects bandwidth and latency performance.
Depending on the results, we will iterate on further followups.

#### Deliverables
- Reports:
- [Notion: 1K Relay + 3-Bootstrap Nodes](https://www.notion.so/1K-Relay-3-Bootstrap-Nodes-2bb8f96fb65c8036b66ef85fff17c515)
- Related PRs if apply:


### nWaku v0.37 store regression

* fully qualified name: `vac:dst:waku:2025q4-waku-evaluation:nwaku-v0.37-store-regression`
* owner: Farooq
* status: in progress (65%)
* start-date: 2025/11/27
* end-date: 2025/12/12

#### Description
Experiment with different sizes of an experiment setup to better test store protocol. 
For example, 500 nWaku relay nodes and 5 store nodes (+2 bootstrap nodes) should be enough.
Inject a bunch of messages, and then query. Scenario should be is fast and reproducible.
Understand what is the behavior of get store messages. The intention is to query nodes that 
are not store nodes, to see if they are able to retrieve the messages.
Document different responses of the query. Analyze the behavior.

#### Deliverables
- Reports:
- [Notion nwaku regression report: Get Store Messages Issue](https://www.notion.so/Get-Store-Messages-Issue-2bb8f96fb65c80bc8e0fdb7801cd0c79)
- Related PRs if apply: