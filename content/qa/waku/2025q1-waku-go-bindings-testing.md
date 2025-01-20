---
title: waku-go-bindings-testing Testing Framework
tags:
  - "2025q1"
  - "qa"
  - "waku"  
draft: false  
description: Build a test automation framework for waku-go-bindings and expand protocol coverage
---

`vac:qa:waku:2025q1-waku-go-bindings-testing`

## Description
Develop a robust test automation framework for the `waku-go-bindings` package 
and enhance protocol coverage for critical Waku functionality.

The framework should enable interaction with multiple nodes 
and scale testing efforts similarly to `waku-interop-tests`. 
The primary focus is to cover relay protocol, 
ensuring reliability across diverse scenarios in accordance to Waku FURPS.

**Alignment with VAC Narratives:**

* The VAC QA team plays a key role in supporting internal collaboration
  and efficiency across projects by ensuring the quality of Nwaku Go Bindings
  and the sunsetting of go-waku.
* By finding issues in specs during testing,
  VAC strengthens the RFC culture,
  contributing to continuous improvement and community engagement.

## Task List

### Framework Development

* fully qualified name: `vac:qa:waku:2025q1-waku-go-bindings-testing:framework-development`
* owner: aya
* status: done
* start-date: 2025/01/06
* end-date: 2025/01/20


#### Description
Create a test automation framework for the `waku-go-bindings-testing` package. 
The framework should support running and interacting with multiple nodes, 
with the capability to scale testing to match the approach used in `waku-interop-tests`. 
It should also be adaptable to future testing needs.

#### Deliverables
* https://github.com/waku-org/waku-go-bindings-tests


### Relay Protocol Testing

* fully qualified name: `vac:qa:waku:2025q1-waku-go-bindings-testing:relay`
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
