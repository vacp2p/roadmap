---
title: Waku-Go-Bindings Testing Framework
tags:
  - "2025q1"
  - "qa"
  - "waku"  
draft: false  
description: Build a test automation framework for Waku-Go-Bindings and expand protocol coverage
---

`vac:qa:waku:2025q1-waku-go-bindings`

## Description
Develop a robust test automation framework for the `waku-go-bindings` package 
and enhance protocol coverage for critical Waku functionality.

The framework should enable interaction with multiple nodes 
and scale testing efforts similarly to `waku-interop-tests`. 
The primary focus is to cover essential protocols like relay and store, 
ensuring compatibility, scalability, and reliability across diverse scenarios.

**Alignment with VAC Narratives:**

* The VAC QA team plays a key role in supporting internal collaboration
  and efficiency across projects by ensuring the quality of Nwaku Go Bindings
  and the sunsetting of go-waku.
* By finding issues in specs during testing,
  VAC strengthens the RFC culture,
  contributing to continuous improvement and community engagement.

**Alignment with FURPS:** 

* **Functionality**:
  * Testing relay and store protocols ensures the core functionality of the `waku-go-bindings` package works as intended.  
* **Reliability**:
  * Robust tests provide stability and reduce errors, ensuring predictable behavior.  
* **Supportability**:
  * A flexible framework makes it easier to adapt, extend, and maintain tests as protocols evolve.

## Task List

### Framework Development

* fully qualified name: `vac:qa:waku:2025q1-waku-go-bindings:framework-development`
* owner: aya
* status: not started
* start-date: 2025/01/06
* end-date: 2025/01/20


#### Description
Create a test automation framework for the `waku-go-bindings` package. 
The framework should support running and interacting with multiple nodes, 
with the capability to scale testing to match the approach used in `waku-interop-tests`. 
It should also be adaptable to future testing needs.

#### Deliverables
* A new test framework for `waku-go-bindings`
* Integration with CI pipelines
* Documentation for framework setup and usage


### Relay Protocol Testing

* fully qualified name: `vac:qa:waku:2025q1-waku-go-bindings:relay`
* owner: aya
* status: not started
* start-date: 2025/01/20
* end-date: 2025/02/25

#### Description
Add test coverage by implementing tests for the relay protocol.
These tests should mirror the approach used in `waku-interop-tests`
and ensure reliable message propagation across multiple nodes.

#### Deliverables
* PR with relay protocol tests
* CI integration for relay tests
* Documentation for relay test scenarios
