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
* status: not started
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
* status: not started
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

