---
title: Waku Interop Testing (extended)
tags:
  - "2025q1"
  - "qa"
  - "waku"  
draft: false  
description: Maintain Waku interop tests and add network condition tests
---

`vac:qa:waku:2025q1-interop-testing`

## Description
Maintain Waku interop tests and add network condition tests

The interop testing framework already provides extensive coverage,
running hundreds of tests across both nwaku and gowaku.

For this commitment, we aim to ensure the framework remains highly reliable 
while adding support for running tests under simulated network conditions, 
such as high latency, packet loss, and low bandwidth.

**Alignment with VAC Narratives:**

* The VAC QA team plays a key role in supporting internal collaboration
  and efficiency across projects by ensuring the quality of Waku’s interop framework.
* By finding issues in specs during testing,
  VAC strengthens the RFC culture,
  contributing to continuous improvement and community engagement.
* By working with developers to address known issues and enhancing CI performance,
  VAC directly contributes to IFT's strategic objective of scaling capacity and efficiency
  through community-driven efforts.

**Alignment with FURPS:**  

* **Functionality**:
  * By maintaining and extending the interop tests,
    this effort ensures compatibility and interoperability between `nwaku` and `gowaku` under various conditions.  
* **Reliability**:
  * Simulating network conditions like high latency and packet loss
    enhances the framework's ability to identify edge cases and prevent regressions,
    ensuring stable performance even under suboptimal circumstances.  
* **Performance**:
  * Testing under constrained network conditions evaluates the framework's efficiency and scalability,
    supporting improvements in CI execution speed.  

## Task List


### Network Conditions

* fully qualified name: `vac:qa:waku:2025q1-interop-testing:network-conditions`
* owner: fbarbu15
* status: not started
* start-date: 
* end-date: 

#### Description
Develop tests to simulate unusual network conditions,
such as high latency, packet loss, and low bandwidth,
particularly affecting light nodes.
The framework should be flexible enough to allow for the application
of these conditions across a full test run on-demand.
Additionally, ensure that a subset of these tests runs nightly
to catch issues that may arise under suboptimal network conditions.

#### Deliverables
* PR with network condition simulation tests
* CI configuration for on-demand full test runs with network constraints
* Nightly CI runs for a subset of tests under network strain

### Maintenance

* fully qualified name: `vac:qa:waku:2025q1-interop-testing:maintenace`
* owner: fbarbu15
* status: not started
* start-date: 2025/01/01
* end-date: 2025/03/31

#### Description
Ongoing Maintenance for Waku Interop Tests
This task involves ensuring the continued reliability 
and functionality of the Waku interop tests. 
It includes adjusting tests whenever there are changes in nwaku or go-waku, 
addressing detected regressions through investigation, reporting, and retesting, 
and resolving infrastructure issues that disrupt the tests. 
Additionally, it covers unplanned but necessary minor improvements to the testing framework 
to enhance its effectiveness.

#### Deliverables

* PRs with maintenace tasks
