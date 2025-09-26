---
title: Status chat protocol benchmarks
tags:
  - "2025q4"
  - "dst"
  - "status"
draft: false
description: "Realize chat protocol benchmarks
of Status."
---

`vac:dst:status:2025q4-status-evaluation`

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

### Narratives

We will support the Conduit of Expertise narrative directly
by analysing and evaluating Status features,
both with regards to features they have today
and with regards to how that compares to past behaviour.

Additionally, these efforts will contribute
to the Premier Research destination narrative by
improving and strengthening our relationship with the Status-go team
and thus increasing the reach and influence of the IFT,
and improving the chances
that we successfully grow our ecosystem's products and collaborations
and especially those we want to work with externally.

## Task list

### Send one-to-one outage (private chats)

* fully qualified name: `vac:dst:status:2025q4-status-evaluation:one-to-one-outage`
* owner: Alberto
* status: 0%
* start-date: TBA
* end-date: TBA

#### Description
[Notion Link](https://www.notion.so/Chat-Protocol-Benchmarks-1938f96fb65c80d8b22fdf641c5ff003?source=copy_link#19d8f96fb65c809e8f11d4296821b24d)
Testing app behaviour when something goes wrong.
Best to start with what is easier within test framework: cut nodes from network, stop and start nodes, suspend processes, etc.

Setup:

- 50 sending nodes
- 50 receiving nodes
- 50 idle nodes
- Mix of relay and light nodes, results should be per node type.
- Each sending node has sent a contact request to a receiving node, that accepted it

Test:

- Sending nodes send one text message per 10 sec
- Test runs for 2 hours or so.
- Sending and receiving nodes lose access to network or get killed, restarted
    - Duration of “outage” (whatever is the chose form), should go from 1 seconds to 1 hour; Probably a global setting so that we can look at bandwidth usage in relation to outage. and see if specific duration lead to an explosion of messages; or if specific duration lead to very poor UX (e.g. outage 30min, messages then take 60min to eventually arrive due to poor backoff strategy)
- Metrics to ensure all messages are **eventually** received (100%) is important
    - and metrics as specified in this page.

#### Deliverables

### Status-backend private chats - send group outage

* fully qualified name: `vac:dst:status:2025q4-status-evaluation:group-outage`
* owner: Alberto
* status: 0%
* start-date: TBA
* end-date: TBA

#### Description
[Notion Link](https://www.notion.so/Chat-Protocol-Benchmarks-1938f96fb65c80d8b22fdf641c5ff003?source=copy_link#19d8f96fb65c80aa8459d54b975df8b0)
Same as @Send one-to-one message - Network outage for private group

#### Deliverables


### Light node benchmark 2

* fully qualified name: `vac:dst:status:2025q4-status-evaluation:light-node-benchmark-2`
* owner: Alberto
* status: 0%
* start-date: TBA
* end-date: TBA

#### Description

Using the fix in the discovery process for the 
[relay nodes](https://www.notion.so/Chat-Protocol-Benchmarks-1938f96fb65c80d8b22fdf641c5ff003?source=copy_link#1998f96fb65c8014bf0af42ce2645fa9)
to repeat the benchmarks for only scenarios that use light nodes.

#### Deliverables
