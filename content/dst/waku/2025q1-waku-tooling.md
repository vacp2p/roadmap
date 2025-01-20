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
* status: 20%
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

### Bandwidth monitor

* fully qualified name: `vac:dst:waku:2025q1-waku-tooling:bandwidth-monitor`
* owner: Wings
* status: 60%
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
- [ ] Report with real example:

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

### Local metrics
