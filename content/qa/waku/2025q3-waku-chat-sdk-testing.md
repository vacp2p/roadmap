---
title: Chat SDK Testing
tags:
  - "2025q3"
  - "qa"
  - "waku"  
draft: false  
description: Test and validate the reliability of the Waku Chat SDK
---

`vac:qa:waku:2025q3-waku-chat-sdk-testing`

## Description
Test and validate the reliability of the Waku Chat SDK 
in accordance to [Waku FURPS](https://github.com/waku-org/pm/blob/2025H2/2025H2-summary.md?plain=1#L76). 
Ensure the SDK performs consistently 
and meets the expected functional and reliability requirements.
Note! This could be pushed to Q4 if the feature is not QA ready as planned.

**Alignment with VAC Narratives:**
- By testing the Waku Chat SDK, 
  VAC QA ensures robust and predictable behavior across diverse environments and tools.
- This initiative supports VAC’s commitment to building reliable and scalable testing frameworks 
  that foster collaboration and confidence in the Waku ecosystem.
- Reliability-focused testing directly aligns with the strategic objective of ensuring resilience in communication protocols.

## Task List

### Integrate Functional Testing into Interop Framework

* fully qualified name: `vac:qa:waku:2025q3-waku-chat-sdk-testing:functional-interop`
* owner: fbarbu15
* status: not started
* start-date: 
* end-date: 

#### Description
Implement functional tests for the new Waku Chat SDK within the interop testing framework.

#### Deliverables
* PRs with functional tests integrated into the interop testing framework
* CI integration for these functional tests
* Documentation outlining tested scenarios

### Reliability Testing for nwaku

* fully qualified name: `vac:qa:waku:2025q3-waku-chat-sdk-testing:functional-nwaku`
* owner: fbarbu15
* status: not started
* start-date: 
* end-date: 

#### Description
Test the core functionality of the Waku Chat SDK implemented in `nwaku`. 
Validate message reliability under various conditions, including network instability.

#### Deliverables
* PRs with functional test cases for `nwaku`
* CI pipelines for automated tests

### Long-Run Testing

* fully qualified name: `vac:qa:waku:2025q3-waku-chat-sdk-testing:long-run`
* owner: fbarbu15
* status: not started
* start-date: 
* end-date: 

#### Description
Perform long-duration tests to validate the Waku Chat SDK’s reliability over extended periods. 
Focus on scenarios such as repeated reconnections, sustained message delivery, 
and node resilience under ongoing network challenges.

#### Deliverables
* PRs with long-run test scenarios
* Reliability metrics from extended tests
* Recommendations for enhancements based on long-run test results
