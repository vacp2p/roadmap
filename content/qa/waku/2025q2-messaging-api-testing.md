---
title: Messaging API Testing
tags:
  - "2025q2"
  - "qa"
  - "waku"  
draft: false  
description: Test and validate the reliability of the Messaging API for nwaku and js-waku.
---

`vac:qa:waku:2025q2-messaging-api-testing`

## Description
Test and validate the reliability of the Messaging API 
for nwaku and js-waku in accordance to Waku FURPS. 
Ensure the API performs consistently and meets the expected functional and reliability requirements, 
aligning with behaviors used by applications like the Status app and Waku Tester tool.
Note! Waku confirmed that this will be ready to test somewhere in Q2 or even Q3 2025

**Alignment with VAC Narratives:**
- By testing the Messaging API, 
  VAC QA ensures robust and predictable API behavior across diverse environments and tools.
- This initiative supports VAC’s commitment to building reliable and scalable testing frameworks 
  that foster collaboration and confidence in the Waku ecosystem.
- Reliability-focused testing directly aligns with the strategic objective of ensuring resilience in communication protocols.

## Task List

### Integrate Functional Testing into Interop Framework

* fully qualified name: `vac:qa:waku:2025q2-messaging-api-testing:functional-interop`
* owner: fbarbu15
* status: not started
* start-date: 
* end-date: 

#### Description
Implement functional tests for the new Messaging API within the interop testing framework.

#### Deliverables
* PRs with functional tests integrated into the interop testing framework
* CI integration for these functional tests
* Documentation outlining tested scenarios

### Reliability Testing for nwaku

* fully qualified name: `vac:qa:waku:2025q2-messaging-api-testing:functional-nwaku`
* owner: fbarbu15
* status: not started
* start-date: 
* end-date: 

#### Description
Test the core functionality of the Messaging API implemented in `nwaku`. 
Validate message reliability under various conditions, including network instability.

#### Deliverables
* PRs with functional test cases for `nwaku`
* CI pipelines for automated tests

### Reliability Testing for js-waku

* fully qualified name: `vac:qa:waku:2025q2-messaging-api-testing:functional-js-waku`
* owner: fbarbu15
* status: not started
* start-date: 
* end-date: 

#### Description
Test the core functionality of the Messaging API implemented in `js-waku`. 
Validate message reliability under various conditions, including network instability.

#### Deliverables
* PRs with functional test cases for `js-waku`
* CI pipelines for automated tests

### Long-Run Testing

* fully qualified name: `vac:qa:waku:2025q2-messaging-api-testing:long-run`
* owner: fbarbu15
* status: not started
* start-date: 
* end-date: 

#### Description
Perform long-duration tests to validate the Messaging API’s reliability over extended periods. 
Focus on scenarios such as repeated reconnections, sustained message delivery, 
and node resilience under ongoing network challenges.

#### Deliverables
* PRs with long-run test scenarios
* Reliability metrics from extended tests
* Recommendations for enhancements based on long-run test results
