---
title: Waku Tooling
tags:
  - "2025q1"
  - "dst"
  - "waku"
draft: false
description: ""
---

`vac:dst:waku:2025q1-waku-tooling`

## Description

We will create tools that allow
DST and Waku teams to analyze and test
Waku scaling properties.
This includes tooling like a general lor parser,
a black-box bandwidth monitor, and other
utilities that may appear 
depending on the needs of the projects.

### Background

### Narratives

These efforts will support the Conduit of Expertise narrative by
accelerating Waku Improvements,
providing measurable insights
to enhance developer experience
within and beyond the IFT ecosystem.
Also, ideally these tools can be shared across projects, 
reinforcing cross project collaboration.


## Task list

### Log parser

* fully qualified name: `vac:dst:waku:2025q1-waku-tooling:log-parser`
* owner: Alberto
* status: 100%
* start-date: 2025/01/01
* end-date: 2025/01/31

#### Description
Code that is able to explore and analyze
Waku logging, and deliver requested insights.
Ideally, logging format should be abstract and pluggable,
so this is easy to use in other projects.

#### Deliverables
- [ ] Repository:
- [ ] PRs:
  - [Deployment yamls](https://github.com/vacp2p/10ksim/pull/54)
  - [Documentation and cleaning](https://github.com/vacp2p/10ksim/pull/52)

### Bandwidth monitor

* fully qualified name: `vac:dst:waku:2025q1-waku-tooling:bandwidth-monitor`
* owner: Wings
* status: 100%
* start-date: 2025/01/06
* end-date: 2025/01/24

#### Description
Tool that is able to work as a sidecar
in a Kubernetes environment.
This tool will be able to retrieve
the entire bandwidth of a binary,
filtering by origin/destination ports.
It will export this information as a metric,
so it can be scrapped by a monitoring stack.
It will be easily extendable if necessary, 
either with ports, and possibly different filters.

#### Deliverables
- [ ] Repository:
- [ ] PRs:
  - Github PR: [PR](https://github.com/vacp2p/10ksim/pull/53)
- [ ] Report with real example:
  - [Notion](https://www.notion.so/Raw-bandwidth-monitor-sidecar-18b8f96fb65c8062a2a8e176b0ac49be)

### Bandwidth monitor improvements

* fully qualified name: `vac:dst:waku:2025q1-waku-tooling:bandwidth-monitor-improvements`
* owner: Wings
* status: 0%
* start-date: 2025/02/10
* end-date: 2025/02/14

#### Description
Address feedback of bandwidth monitor tool.
This includes usability, race condition considerations,
prometheus optimizations and testing.
Add unit testing for functions, and a small
real test scenario to make sure it works properly.
Document the test scenario.

#### Deliverables
- [ ] Repository:
- [ ] PRs:
- [ ] Report with real example:

### Log parser extended

* fully qualified name: `vac:dst:waku:2025q1-waku-tooling:log-parser-extended`
* owner: Alberto
* status: 0%
* start-date: TBA
* end-date: TBA

#### Description
Include [Waku FURPS](https://www.notion.so/Waku-FURPS-1498f96fb65c803faedef2a591c22c00#1508f96fb65c80a8abd6f5d37a273657) for a log parser debugging tool
in the DST analysis framework.
> *Note*: This needs more input from project

#### Deliverables
- [ ] Repository:
- [ ] PRs:

### General tooling (recurring)

* fully qualified name: `vac:dst:waku:2025q1-waku-tooling:general-tooling`
* owner: Alberto
* status: recurring
* start-date: 2025/01/01
* end-date: 2025/03/31

#### Description
Group of utilities that are created
for the analysis of Waku.
Should be made general when possible.

#### Deliverables
- [ ] PRs:
  - Message distribution plot improvement: [PR](https://github.com/vacp2p/10ksim/pull/47)
  - Violin plot: [PR](https://github.com/vacp2p/10ksim/pull/51)
  - Outliers parameter: [PR](https://github.com/vacp2p/10ksim/pull/57)

### Local metrics
