---
title: Status evaluation
tags:
  - "2025q2"
  - "dst"
  - "status"
draft: false
description: "Test Status-go on each new version or feature
and look for regressions,
learn scaling properties and run scaling studies."
---

`vac:dst:status:2025q2-status-go-evaluation`

## Description

Test Status-go on each new version or requested feature
and look for regressions,
learn scaling properties and run scaling studies,
understand the limits of Status-go and its behaviour.
Deliver reports and actionable insights.
Do this monthly, reliably, with documentation of findings.

The scope of this commitment is expected to be updated based on input from Status.
work and improvements, and it is subjected to change.

### Background

We want to learn specific, actionable information
about Status-go's behaviour
and how it is evolving over time
with each new release
and with each thing we are specifically asked to check and test.

We will use a combination of real world testing,
theoretical analysis and simulation
to determine and measure the success,
side effects and other factors of Status-go and its evolution.

### Narratives

We will support the Conduit of Expertise narrative directly
by analysing and evaluating new Status-go releases and their features,
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

### Status-backend private chats - Idle-relay

* fully qualified name: `vac:dst:status:2025q2-status-go-evaluation:idle-relay`
* owner: TBA
* status: 0%
* start-date: TBA
* end-date: TBA

#### Description

**Setup:**

- 1 relay node - Alice
- 100 relay nodes - friends
- all friends have an accepted contact request with Alice who accepted it

**Test:**

- Idle for 10 minutes, an hour, 12 hours?

#### Deliverables

### Status-backend private chats - Idle-light

* fully qualified name: `vac:dst:status:2025q2-status-go-evaluation:idle-light`
* owner: TBA
* status: 0%
* start-date: TBA
* end-date: TBA

#### Description

**Setup:**

- 1 light node - Alice
- 100 light nodes - friends
- all friends have an accepted contact request with Alice who accepted it

**Test:**

- Idle for 10 minutes, an hour, 12 hours?

#### Deliverables

### Status-backend private chats - contact request

* fully qualified name: `vac:dst:status:2025q2-status-go-evaluation:contact-request`
* owner: TBA
* status: 0%
* start-date: TBA
* end-date: TBA

#### Description

**Setup:**

- 50 requesters nodes
- 150 requested nodes
    - 50 accepting
    - 50 rejecting
    - 50 ignoring
- 50 idle nodes
- 50% of nodes are relay, 50% are light/edge

**Test:**

- Each requester send a contact request to 3 nodes in the requested set (random selection)
- accepting nodes in the set accept the request
- rejecting nodes rejects the request
- ignoring nodes ignore the request
- In addition to [Metrics](https://www.notion.so/Metrics-1938f96fb65c8049915cf78b7a951a9d?pvs=21), measure
    - Success rate of contact requests received
    - Success rate of contact request accepted

#### Deliverables

### Status-backend private chats - send-one-to-one

* fully qualified name: `vac:dst:status:2025q2-status-go-evaluation:send-one-to-one`
* owner: TBA
* status: 0%
* start-date: TBA
* end-date: TBA

#### Description

**Setup:**

- 50 sending nodes
- 50 receiving nodes
- 50 idle nodes
- Each sending node has sent a contact request to a receiving node, that accepted it

**Test:**

- Sending nodes send one text message per 10 sec

#### Deliverables

### Status-backend private chats - create private group

* fully qualified name: `vac:dst:status:2025q2-status-go-evaluation:create-private-group`
* owner: TBA
* status: 0%
* start-date: TBA
* end-date: TBA

#### Description

**Setup:**

- 10 admin nodes
- 100 single-group members

**Test:**

- Each admin node create a group and invite 10 single-group members in it
- single-group members accept the invite

#### Deliverables

### Status-backend private chats - send group message

* fully qualified name: `vac:dst:status:2025q2-status-go-evaluation:send-group-message`
* owner: TBA
* status: 0%
* start-date: TBA
* end-date: TBA

#### Description

**Setup:**

- 10 admin nodes
- 100 single-group members
- Each admin node create a group and invite 10 single-group members in it, who accept the invite

**Test:**

- Every member send a message in their group every 10 seconds

#### Deliverables

### Status-backend private chats - send one-to-one outage

* fully qualified name: `vac:dst:status:2025q2-status-go-evaluation:one-to-one-outage`
* owner: TBA
* status: 0%
* start-date: TBA
* end-date: TBA

#### Description

Testing app behaviour when something goes wrong.
Best to start with what is easier within test framework: cut nodes from network, stop and start nodes, suspend processes, etc.

**Setup:**

- 50 sending nodes
- 50 receiving nodes
- 50 idle nodes
- Mix of relay and light nodes, results should be per node type.
- Each sending node has sent a contact request to a receiving node, that accepted it

**Test:**

- Sending nodes send one text message per 10 sec
- Test runs for 2 hours or so.
- Sending and receiving nodes lose access to network or get killed, restarted
    - Duration of “outage” (whatever is the chose form), should go from 1 seconds to 1 hour; Probably a global setting so that we can look at bandwidth usage in relation to outage. and see if specific duration lead to an explosion of messages; or if specific duration lead to very poor UX (e.g. outage 30min, messages then take 60min to eventually arrive due to poor backoff strategy)
- Metrics to ensure all messages are **eventually** received (100%) is important
    - and metrics as specified in this page.

#### Deliverables

### Status-backend private chats - send group outage

* fully qualified name: `vac:dst:status:2025q2-status-go-evaluation:group-outage`
* owner: TBA
* status: 0%
* start-date: TBA
* end-date: TBA

#### Description

Same as @Send one-to-one message - Network outage for private group

#### Deliverables

### Status-backend communities phase 2 - message sending

* fully qualified name: `vac:dst:status:2025q2-status-go-evaluation:community-message-sending-2`
* owner: TBA
* status: 0%
* start-date: TBA
* end-date: TBA

#### Description

**Setup:**

- 1 admin community node
- 500 user nodes
- all users join community

**Test:**

- 100 nodes send 1 message every 5s

#### Deliverables

### Status-backend communities phase 2 - request to join mix

* fully qualified name: `vac:dst:status:2025q2-status-go-evaluation:group-outage`
* owner: TBA
* status: 0%
* start-date: TBA
* end-date: TBA

#### Description

**Setup:**

- 1 admin community node
- 500 user nodes
    - 200 user nodes have already joined the community
    - 300 have not (non-members)

**Test:**

- 200 of the 300 non-members send a “request to join community” to owner node.
    - maybe 1 node request per 1/5/10 seconds.
    - Or all requests at the same time see how owner node survives
- Owner node accepts 100 requests and reject the 100 remaining

#### Deliverables

### Status-backend communities phase 2 - isolated chat messages

* fully qualified name: `vac:dst:status:2025q2-status-go-evaluation:isolated-chat-messages`
* owner: TBA
* status: 0%
* start-date: TBA
* end-date: TBA

#### Description

**Setup:**

- 1 admin community node
- 500 user nodes
- 250 users joined community

**Test:**

- Community members send 1 message every 10 seconds; parameterize injection volume
- Also have 0 messages sent. And showing that stopping “user members” does not impact non-members traffics (community idle traffic does not impact users that are not part of any communities)

**Measure:**

- Ensure that the 250 nodes that did **not** join the community have minimal traffic, not correlated to the community traffic

#### Deliverables

### Status-backend communities phase 2 - isolated requests

* fully qualified name: `vac:dst:status:2025q2-status-go-evaluation:isolated-requests`
* owner: TBA
* status: 0%
* start-date: TBA
* end-date: TBA

#### Description

Similar to @Isolated traffic - chat messages but only looking at request to join community traffic

#### Deliverables