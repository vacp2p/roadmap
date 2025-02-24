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
* status: done
* start-date: 2025/01/06
* end-date: 2025/01/25

#### Description
Implement and execute functional tests for direct message flows, 
including 1:1 chats and private groups. 

#### Deliverables
* [Test reliability workflow](https://github.com/status-im/status-go/pull/6236)
* [Test private chat messages](https://github.com/status-im/status-go/pull/6259)
* [reactivate reliability workflow](https://github.com/status-im/status-go/pull/6280)
* [community messages](https://github.com/status-im/status-go/pull/6294)
* [CI RUN](https://github.com/status-im/status-go/actions/runs/13232288117)


### Reliability Testing Under Degraded Network Conditions

* fully qualified name: `vac:qa:waku:2025q1-direct-message-reliability-testing:degraded-network`
* owner: fbarbu15
* status: done
* start-date: 2025/01/25
* end-date: 2025/02/15

#### Description
Perform tests to validate direct message reliability under degraded network conditions. 
Specifically, also ensure messages are automatically retrieved in the Status app 
after a network reconnection.

#### Deliverables
* [Test reliability workflow](https://github.com/status-im/status-go/pull/6236)
* [Test private chat messages](https://github.com/status-im/status-go/pull/6259)
* [reactivate reliability workflow](https://github.com/status-im/status-go/pull/6280)
* [community messages](https://github.com/status-im/status-go/pull/6294)
* [CI RUN](https://github.com/status-im/status-go/actions/runs/13232288117)

### Rate Limit Testing

* fully qualified name: `vac:qa:waku:2025q1-direct-message-reliability-testing:rate-limit`
* owner: fbarbu15
* status: done
* start-date: 2025/02/25
* end-date: 2025/03/10

#### Description
- [Rate limiting tests](https://github.com/status-im/status-go/pull/6332)
- [CI RUN](https://github.com/status-im/status-go/actions/runs/13344807227)

#### Deliverables
* PRs with new test cases

### IP Change Testing

* fully qualified name: `vac:qa:waku:2025q1-direct-message-reliability-testing:ip-change`
* owner: fbarbu15
* status: in progress (80%)
* start-date: 2025/02/10
* end-date: 2025/02/17

#### Description
Perform tests to validate how status-backend handes ip change
and if message flow resumes after such event.

#### Deliverables
* PRs with new test cases

### Wakuext One To One Messages

* fully qualified name: `vac:qa:waku:2025q1-direct-message-reliability-testing:wakuext-one-to-one-message`
* owner: radek
* status: done
* start-date: 2025/02/17
* end-date: 2025/02/24

#### Description
Perform functional tests to validate [wakuext_sendOneToOneMessage](https://github.com/status-im/status-go/issues/6084) endpoint. 

#### Deliverables
* [test_: refactor default messaging scenario](https://github.com/status-im/status-go/pull/6351)

### Wakuext Chat Messages

* fully qualified name: `vac:qa:waku:2025q1-direct-message-reliability-testing:wakuext-chat-message`
* owner: radek
* status: in progress (15%)
* start-date: 2025/02/25
* end-date: 2025/03/14

#### Description
Perform tests functional tests to validate all [wakuext chat messages](https://github.com/status-im/status-go/issues/6084) endpoints. 

#### Deliverables
* [test_: Tests for wakuext messages 1](https://github.com/status-im/status-go/pull/6356)

### Other Message Endpoints

* fully qualified name: `vac:qa:waku:2025q1-direct-message-reliability-testing:other-message-ep`
* owner: radek
* status: not started
* start-date: 2025/03/17
* end-date: 2025/03/31

#### Description
Perform functional tests to validate all [remaining message](https://github.com/status-im/status-go/issues/6084) endpoints. 

#### Deliverables
* PR with new test cases
