---
title: Direct Message Reliability Testing
tags:
  - "2025q1"
  - "qa"
  - "waku"  
draft: false  
description: Test and validate the reliability of direct messages across Status chat protocols.
---

`vac:qa:waku:2025q1-direct-message-reliability-testing`

## Description
Focus on testing and validating the reliability of direct messages in Status chat protocols, 
including 1:1 chats and private groups in accordance to Waku FURPS.
This includes testing flows under degraded network conditions, 
ensuring message retrieval after reconnections, 
and validating the application of MVDS for improved message delivery reliability.

**Alignment with VAC Narratives:**

* By ensuring the reliability of direct messaging, 
  VAC QA contributes to a more robust and user-friendly experience within Status applications.
* Testing efforts provide valuable insights into potential issues, 
  supporting VAC’s goal of improving communication protocols and collaboration.
* This initiative directly aligns with strategic objectives 
  to ensure resilience and consistent performance in communication tools.

## Task List

### Functional Testing for Direct Messages

* fully qualified name: `vac:qa:waku:2025q1-direct-message-reliability-testing:functional`
* owner: fbarbu15
* status: in progress (90%)
* start-date: 2025/01/06
* end-date: 2025/01/25

#### Description
Implement and execute functional tests for direct message flows, 
including 1:1 chats and private groups. 

#### Deliverables
* PRs with functional test cases
* CI pipelines for automated functional tests
* Documentation outlining tested scenarios


### Reliability Testing Under Degraded Network Conditions

* fully qualified name: `vac:qa:waku:2025q1-direct-message-reliability-testing:degraded-network`
* owner: fbarbu15
* status: in progress (80%)
* start-date: 2025/01/25
* end-date: 2025/02/15

#### Description
Perform tests to validate direct message reliability under degraded network conditions. 
Specifically, also ensure messages are automatically retrieved in the Status app 
after a network reconnection.

#### Deliverables
* PRs with reliability test cases
* Reports on test results under degraded conditions
* Recommendations for improving message flow resilience

### Rate Limit Testing

* fully qualified name: `vac:qa:waku:2025q1-direct-message-reliability-testing:rate-limit`
* owner: fbarbu15
* status: in progress (10%)
* start-date: 2025/02/25
* end-date: 2025/03/10

#### Description
Perform tests to validate rate limiting in status-backend. 
Tests should be done ideally for relay, lightpush and filter 
but TBD when status-backend will support all this.

#### Deliverables
* PRs with new test cases

### Wakuext One To One Messages

* fully qualified name: `vac:qa:waku:2025q1-direct-message-reliability-testing:wakuext-one-to-one-message`
* owner: radoslav
* status: not started
* start-date: 2025/02/17
* end-date: 2025/02/24

#### Description
Perform tests functional tests to validate [wakuext_sendOneToOneMessage](https://github.com/status-im/status-go/issues/6084) endpoint. 

#### Deliverables
* PR with new test cases

### Wakuext Chat Messages

* fully qualified name: `vac:qa:waku:2025q1-direct-message-reliability-testing:wakuext-chat-message`
* owner: radoslav
* status: not started
* start-date: 2025/02/25
* end-date: 2025/03/14

#### Description
Perform tests functional tests to validate all [wakuext chat messages](https://github.com/status-im/status-go/issues/6084) endpoints. 

#### Deliverables
* PR with new test cases

### Other Message Endpoints

* fully qualified name: `vac:qa:waku:2025q1-direct-message-reliability-testing:other-message-ep`
* owner: radoslav
* status: not started
* start-date: 2025/03/17
* end-date: 2025/03/31

#### Description
Perform functional tests to validate all [remaining message](https://github.com/status-im/status-go/issues/6084) endpoints. 

#### Deliverables
* PR with new test cases
