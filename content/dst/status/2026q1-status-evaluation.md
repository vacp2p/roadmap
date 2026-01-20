---
title: Status chat protocol benchmarks
tags:
  - "2026q1"
  - "dst"
  - "status"
draft: false
description: "Realize chat protocol benchmarks
of Status."
---

`vac:dst:status:2026q1-status-evaluation`

## Description

Realizing chat protocol benchmarks on status-go
will allow the Status and Waku team to perform
non-regression performance tests for chat protocols.
Also, this will allow quantify improvements tackled
by Waku Chat team.
The benchmarks will be done for communities,
with emphasis on subscription and store performance, and
private chats, with emphasis on contact requests,
1-1 messages and group messages.

### Background

The following scenarios will help review what kind of improvements
and changes can be made to the chat protocols, and see if
more baseline benchmarks are needed to be measured in FURPS.

## Task list

### Benchmarks second iteration

* fully qualified name: `vac:dst:status:2026q1-status-evaluation:benchmarks-second-iteration`
* owner: Alberto
* status: 50%
* start-date: 2026/01/01
* end-date: 2026/01/31

#### Description

Using the fix in the discovery process for the 
[relay nodes](https://www.notion.so/Chat-Protocol-Benchmarks-1938f96fb65c80d8b22fdf641c5ff003?source=copy_link#1998f96fb65c8014bf0af42ce2645fa9)
to repeat the benchmarks adding light nodes in the same chat protocol benchmarks scenarios.
Also, perform nwaku-based vs go-waku-based status-backend comparisons.

This task is a mix of `vac:dst:waku:2025q4-waku-scaling:nwaku-in-status-desktop` and 
`vac:dst:status:2025q4-status-evaluation:chat-protocol-benchmarks-followup`.

#### Deliverables
- Github PRs:
  - [Github PR: Multiple consumers #35](https://github.com/vacp2p/status-benchmarks/pull/35)
  - [Github PR: Logger adjustments #37](https://github.com/vacp2p/status-benchmarks/pull/37)
- Documents:
  - [Notion: Status-light and nWaku filter](https://www.notion.so/Status-light-and-nWaku-filter-2858f96fb65c8019ac2af3a84c688d68)
  - [Notion: Status benchmark discovery issues](https://www.notion.so/Status-benchmark-discovery-issues-27a8f96fb65c80e9bc09e356371556a0)
  - [Notion: Status-nWaku issues](https://www.notion.so/Status-nWaku-issues-2ed8f96fb65c8090add1c7f764e5690c)
