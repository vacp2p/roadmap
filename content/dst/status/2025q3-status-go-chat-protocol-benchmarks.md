---
title: Status-go chat protocol benchmarks
tags:
  - "2025q3"
  - "dst"
  - "status"
draft: false
description: "Realize chat protocol benchmarks
of Status-go. Establish a baseline of results to 
easier compare nWaku integration in the future."
---

`vac:dst:status:2025q3-status-go-chat-protocol-benchmarks`

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
by analysing and evaluating Status-go features,
both with regards to features they have today
and with regards to how that compares to past behaviour.

Additionally, these efforts will contribute
to the Premier Research destination narrative by
improving and strengthening our relationship with the Status-go team
and thus increasing the reach and influence of the IFT,
and improving the chances
that we successfully grow our ecosystem's products and collaborations
and especially those we want to work with externally.

### Additional info
This commitment has been rescheduled from 2025Q2 to 2025Q3
due to unforeseen circumstances.

## Task list

### Status-backend subscription performance (communities)

* fully qualified name: `vac:dst:status:2025q3-status-go-chat-protocol-benchmarks:subscription-performance`
* owner: Alberto
* status: 100%
* start-date: 2025/07/01
* end-date: 2025/07/18

#### Description
[Notion Link](https://www.notion.so/Chat-Protocol-Benchmarks-1938f96fb65c80d8b22fdf641c5ff003?source=copy_link#1998f96fb65c80e89cfdcc028735fe1c)

Setup:

- 1 publisher node (relay or light, doesn’t matter)
- 1-2 service nodes
- 200 light nodes
- 200 relay nodes
- One community setup
- All relay and light nodes have joined the community

Test:

- Only publisher and service nodes are up
- publisher node publishes messages (they get stored in store), then stops
- light and relay nodes go online
- They automatically perform store queries
- Measure time from start to time they get first query
- Measure on wire store query performance

#### Deliverables
- [Draft PR](https://github.com/vacp2p/status-benchmarks/pull/12)
- [Notion Document](https://www.notion.so/Subscription-Performance-2348f96fb65c80c6b04dc2100f3e1fea)

### Status-backend store performance (communities)

* fully qualified name: `vac:dst:status:2025q3-status-go-chat-protocol-benchmarks:store-performance`
* owner: Alberto
* status: 100%
* start-date: 2025/07/01
* end-date: 2025/07/18

#### Description
[Notion Link](https://www.notion.so/Chat-Protocol-Benchmarks-1938f96fb65c80d8b22fdf641c5ff003#1998f96fb65c800092e8d1af720e2182)

Setup:

- 1 publisher node (relay or light, doesn’t matter)
- 1-2 service nodes
- 200 light nodes
- 200 relay nodes
- One community setup
- All relay and light nodes have joined the community

Test:

- Only publisher and service nodes are up
- publisher node publishes messages (they get stored in store), then stops
- light and relay nodes go online
- They automatically perform store queries
- Measure time from start to time they get first query
- Measure on wire store query performance

#### Deliverables
- [PR #13: Asyncio](https://github.com/vacp2p/status-benchmarks/pull/13)
- [To review PR #14: Buffered Queue](https://github.com/vacp2p/status-benchmarks/pull/14)
- [Draft PR #15: Store performance](https://github.com/vacp2p/status-benchmarks/pull/15)
- [Notion Document](https://www.notion.so/Store-Performance-2368f96fb65c80889a10cfe276e51623)


### Message sending (communities)

* fully qualified name: `vac:dst:status:2025q3-status-go-chat-protocol-benchmarks:message-sending`
* owner: Alberto
* status: 100%
* start-date: 2025/07/01
* end-date: 2025/07/18

#### Description
[Notion Link](https://www.notion.so/Chat-Protocol-Benchmarks-1938f96fb65c80d8b22fdf641c5ff003#19d8f96fb65c8092b713ef96270be40b)

Setup:

- 1 admin community node
- 500 user nodes
- all users join community

Test:

- 100 nodes send 1 message every 5s

#### Deliverables
- [Draft PR #16: Message sending](https://github.com/vacp2p/status-benchmarks/pull/16)
- [Notion Document](https://www.notion.so/Message-sending-2368f96fb65c803fae4ac428bd0b7227)


### Request to join mix (communities)

* fully qualified name: `vac:dst:status:2025q3-status-go-chat-protocol-benchmarks:join-community-mix`
* owner: Alberto
* status: 100%
* start-date: 2025/07/01
* end-date: 2025/07/18

#### Description
[Notion Link](https://www.notion.so/Chat-Protocol-Benchmarks-1938f96fb65c80d8b22fdf641c5ff003#19d8f96fb65c806a905bf643fb5a2cd7)

Setup:

- 1 admin community node
- 500 user nodes
    - 200 user nodes have already joined the community
    - 300 have not (non-members)

Test:

- 200 of the 300 non-members send a “request to join community” to owner node.
    - maybe 1 node request per 1/5/10 seconds.
    - Or all requests at the same time see how owner node survives
- Owner node accepts 100 requests and reject the 100 remaining

#### Deliverables
- [Draft PR #17: Request to join mix](https://github.com/vacp2p/status-benchmarks/pull/17)
- [Notion Document](https://www.notion.so/Request-to-join-community-Mix-2368f96fb65c80998456d81b39a2df93)


### Isolated chat messages (communities)

* fully qualified name: `vac:dst:status:2025q3-status-go-chat-protocol-benchmarks:isolated-traffic-chat-messages`
* owner: Alberto
* status: 100%
* start-date: 2025/07/01
* end-date: 2025/07/18

#### Description
[Notion Link](https://www.notion.so/Chat-Protocol-Benchmarks-1938f96fb65c80d8b22fdf641c5ff003#19d8f96fb65c80f18beff8f3286e2f88)
 
Setup:

- 1 admin community node
- 500 user nodes
- 250 users joined community

Test:

- Community members send 1 message every 10 seconds; parameterize injection volume
- Also have 0 messages sent. And showing that stopping “user members” does not impact non-members 
traffics (community idle traffic does not impact users that are not part of any communities)

#### Deliverables
- [Draft PR #18: Isolated traffic](https://github.com/vacp2p/status-benchmarks/pull/18/)
- [Notion document 1](https://www.notion.so/Isolated-traffic-Chat-messages-1-2368f96fb65c80f69a22f0d9e6c91fb3)
- [Notion document 2](https://www.notion.so/Isolated-traffic-Chat-messages-2-2398f96fb65c8088a8c2fc726dd3f3b1)

### Isolated request to join (communities)

* fully qualified name: `vac:dst:status:2025q3-status-go-chat-protocol-benchmarks:isolated-traffic-request-to-join`
* owner: Alberto
* status: 100%
* start-date: 2025/07/01
* end-date: 2025/07/18

#### Description
[Notion Link](https://www.notion.so/Chat-Protocol-Benchmarks-1938f96fb65c80d8b22fdf641c5ff003#19d8f96fb65c8063bd1ddac9cca961aa)
 
Setup:

- 1 admin community node
- 500 user nodes
- 250 users joined community

Test:

- Community members send 1 message every 10 seconds; parameterize injection volume
- Also have 0 messages sent. And showing that stopping “user members” does not impact non-members 
traffics (community idle traffic does not impact users that are not part of any communities)

#### Deliverables
- [Draft PR #19: Isolated traffic request to join](https://github.com/vacp2p/status-benchmarks/pull/19/)
- [Notion Document](https://www.notion.so/Isolated-traffic-Request-to-Join-2368f96fb65c80f295b1f9950852f94e)


### Idle-relay (private chats)

* fully qualified name: `vac:dst:status:2025q3-status-go-chat-protocol-benchmarks:idle-relay`
* owner: Alberto
* status: 100%
* start-date: 2025/07/01
* end-date: 2025/07/18

#### Description
[Notion Link](https://www.notion.so/Chat-Protocol-Benchmarks-1938f96fb65c80d8b22fdf641c5ff003#1938f96fb65c80f1a803c3af7b437f59)

Setup:

- 1 relay node - Alice
- 100 relay nodes - friends
- all friends have an accepted contact request with Alice who accepted it

Test:

- Idle for 10 minutes, an hour, 12 hours?

#### Deliverables
- [Draft PR #20: Improvements](https://github.com/vacp2p/status-benchmarks/pull/20)
- [Draft PR #21: Idle-relay](https://github.com/vacp2p/status-benchmarks/pull/21)
- [Notion Document](https://www.notion.so/Idle-Relay-2368f96fb65c8029b825eaedc8b56677)

### Idle-light (private chats)

* fully qualified name: `vac:dst:status:2025q3-status-go-chat-protocol-benchmarks:idle-light`
* owner: Alberto
* status: 100%
* start-date: 2025/07/01
* end-date: 2025/07/18

#### Description
[Notion Task](https://www.notion.so/Chat-Protocol-Benchmarks-1938f96fb65c80d8b22fdf641c5ff003?source=copy_link#1998f96fb65c8078a135cd49bf923a0d)

Setup:

- 1 light node - Alice
- 100 light nodes - friends
- all friends have an accepted contact request with Alice who accepted it

Test:

- Idle for 10 minutes, an hour, 12 hours?

#### Deliverables
- [Draft PR#23: Idle Light](https://github.com/vacp2p/status-benchmarks/pull/22)
- [Notion Document](https://www.notion.so/Idle-Light-2368f96fb65c8093a283c2afc4748a4d)


### Contact request (private chats)

* fully qualified name: `vac:dst:status:2025q3-status-go-chat-protocol-benchmarks:contact-request`
* owner: Alberto
* status: 100%
* start-date: 2025/07/01
* end-date: 2025/07/18

#### Description
[Notion Link](https://www.notion.so/Chat-Protocol-Benchmarks-1938f96fb65c80d8b22fdf641c5ff003#1938f96fb65c80c8b861fd97cb07fb03)

Setup:

- 50 requesters nodes
- 150 requested nodes
    - 50 accepting
    - 50 rejecting
    - 50 ignoring
- 50 idle nodes
- 50% of nodes are relay, 50% are light/edge

Test:

- Each requester send a contact request to 3 nodes in the requested set (random selection)
- accepting nodes in the set accept the request
- rejecting nodes rejects the request
- ignoring nodes ignore the request
- In addition to [Metrics](https://www.notion.so/Metrics-1938f96fb65c8049915cf78b7a951a9d?pvs=21), measure
    - Success rate of contact requests received
    - Success rate of contact request accepted

#### Deliverables
- [Draft PR #23: Contact Request](https://github.com/vacp2p/status-benchmarks/pull/23)
- [Notion Document](https://www.notion.so/Contact-request-2368f96fb65c8039a772f2a90c034eb0)

### Send-one-to-one (private chats)

* fully qualified name: `vac:dst:status:2025q3-status-go-chat-protocol-benchmarks:send-one-to-one`
* owner: Alberto
* status: 100%
* start-date: 2025/07/01
* end-date: 2025/07/18

#### Description
[Notion Link](https://www.notion.so/Chat-Protocol-Benchmarks-1938f96fb65c80d8b22fdf641c5ff003?source=copy_link#1938f96fb65c802fad73db2d95f5e56c)

Setup:

- 50 sending nodes
- 50 receiving nodes
- 50 idle nodes
- Each sending node has sent a contact request to a receiving node, that accepted it

Test:

- Sending nodes send one text message per 10 sec

#### Deliverables
- [Draft PR #24: Send one to one](https://github.com/vacp2p/status-benchmarks/pull/24)
- [Notion Document](https://www.notion.so/Send-one-to-one-message-2368f96fb65c8037a8b7eb0b8e9d9f69)

### Create private group (private chats)

* fully qualified name: `vac:dst:status:2025q3-status-go-chat-protocol-benchmarks:create-private-group`
* owner: Alberto
* status: 100%
* start-date: 2025/07/01
* end-date: 2025/07/18

#### Description
[Notion Link](https://www.notion.so/Chat-Protocol-Benchmarks-1938f96fb65c80d8b22fdf641c5ff003#1938f96fb65c800f85f4e8c9e0abc642)

Setup:

- 10 admin nodes
- 100 single-group members

Test:

- Each admin node create a group and invite 10 single-group members in it
- single-group members accept the invite

#### Deliverables
- [Draft PR #25: Create private group](https://github.com/vacp2p/status-benchmarks/pull/25)
- [Notion Document](https://www.notion.so/Create-private-group-2368f96fb65c80629a16d3bdf388ac9d)

### Send group message (private chats)

* fully qualified name: `vac:dst:status:2025q3-status-go-chat-protocol-benchmarks:send-group-message`
* owner: Alberto
* status: 100%
* start-date: 2025/07/01
* end-date: 2025/07/18

#### Description
[Notion Link](https://www.notion.so/Chat-Protocol-Benchmarks-1938f96fb65c80d8b22fdf641c5ff003?source=copy_link#1938f96fb65c80f5983ce854a00f3f9b)

Setup:

- 10 admin nodes
- 100 single-group members
- Each admin node create a group and invite 10 single-group members in it, who accept the invite

Test:

- Every member send a message in their group every 10 seconds

#### Deliverables
- [Draft PR #26: Send group message](https://github.com/vacp2p/status-benchmarks/pull/26)
- [Notion Document](https://www.notion.so/Send-group-message-2368f96fb65c80d79b66d8e01701f845)

### Send one-to-one outage (private chats)

* fully qualified name: `vac:dst:status:2025q3-status-go-chat-protocol-benchmarks:one-to-one-outage`
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

* fully qualified name: `vac:dst:status:2025q3-status-go-chat-protocol-benchmarks:group-outage`
* owner: Alberto
* status: 0%
* start-date: TBA
* end-date: TBA

#### Description
[Notion Link](https://www.notion.so/Chat-Protocol-Benchmarks-1938f96fb65c80d8b22fdf641c5ff003?source=copy_link#19d8f96fb65c80aa8459d54b975df8b0)
Same as @Send one-to-one message - Network outage for private group

#### Deliverables

### Cleanup resources

* fully qualified name: `vac:dst:status:2025q3-status-go-chat-protocol-benchmarks:cleanup-resources`
* owner: Alberto
* status: 10%
* start-date: 2025/09/15
* end-date: 2025/09/30

#### Description

Close up draft PRs from previous procol benchmarks. Extract utilities and/or add documentation when possible.

#### Deliverables


### Delay and store

* fully qualified name: `vac:dst:status:2025q3-status-go-chat-protocol-benchmarks:delay-and-store`
* owner: Alberto
* status: 100%
* start-date: 2025/08/18
* end-date: 2025/08/29

#### Description

In a relay-friend request scenario, try the following:
1. Add a delay between friend requests and check if this has an impact on store requests.
2. Try changing the bootstrap node ENR in the fleet config to discv5nodes.
Check how this behaves, and if it solves scalability.

#### Deliverables


### Relay node benchmark 2

* fully qualified name: `vac:dst:status:2025q3-status-go-chat-protocol-benchmarks:relay-node-benchmark-2`
* owner: Alberto
* status: 10%
* start-date: 2025/09/15
* end-date: 2025/09/30

#### Description

Using the fix in the discovery process for the 
[relay nodes](https://www.notion.so/Chat-Protocol-Benchmarks-1938f96fb65c80d8b22fdf641c5ff003?source=copy_link#1998f96fb65c8014bf0af42ce2645fa9)
to repeat the benchmarks for only scenarios that use relay nodes, as discovery in light nodes is not working at the moment.

#### Deliverables
