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
* status: done
* start-date: 2025/01/20
* end-date: 2025/02/25

#### Description
Add test coverage by implementing tests for the relay protocol.
These tests should mirror the approach used in `waku-interop-tests`
and ensure reliable message propagation across multiple nodes.

#### Deliverables
PRs:
* [Framework support](https://github.com/waku-org/waku-go-bindings/pull/29)
* [Relay tests](https://github.com/waku-org/waku-go-bindings/pull/33)
Issues:
* [Cannot Unmarshal Array into messageHash of Type common.MessageHash](https://github.com/waku-org/waku-go-bindings/issues/24)
* [Panic: sync: negative WaitGroup counter Occurs During Relay Peer Connection](https://github.com/waku-org/waku-go-bindings/issues/25)
* [Message Received Despite Relay = false in Test TestMessageNotReceivedWithoutRelay](https://github.com/waku-org/waku-go-bindings/issues/28)
* [Unhandled Exception When Sending Invalid Payload in Waku Relay Publish](https://github.com/waku-org/waku-go-bindings/issues/37)

### Store Protocol Testing

* fully qualified name: `vac:qa:waku:2025q1-waku-go-bindings-testing:store`
* owner: aya
* status: in progress (75%)
* start-date: 2025/02/10
* end-date: 2025/03/10

#### Description
Add test coverage by implementing tests for the store protocol.
These tests should mirror the approach used in `waku-interop-tests`
and ensure reliable message storing across multiple nodes.

#### Deliverables
* [PR: Store tests](https://github.com/waku-org/waku-go-bindings/pull/43)
* [Bug: Can't pause & resume nodes](https://github.com/waku-org/waku-go-bindings/issues/40)
* [Bug: Legacy store not working](https://github.com/waku-org/waku-go-bindings/issues/41)

### Maintenance

* fully qualified name: `vac:qa:waku:2025q1-waku-go-bindings-testing:maintenance`
* owner: aya
* status: in progress (20%)
* start-date: 2025/01/01
* end-date: 2025/03/31

#### Description
Ongoing maintenance of Waku go bindings tests. 
This includes updating tests for changes in the bindings or in `nwaku` or `gowaku`, addressing regressions, 
investigating and resolving issues, and implementing minor improvements to the testing framework as needed.

#### Deliverables
* [Bug: issue with Retrieving Stored Messages on Pubsub Topic for Shard 8](https://github.com/waku-org/waku-go-bindings/issues/44)

### Connection

* fully qualified name: `vac:qa:waku:2025q1-waku-go-bindings-testing:connection`
* owner: radek
* status: in progress (10%)
* start-date: 2025/03/03
* end-date: 2025/03/10

#### Description
Create tests focusing on Discv5 peer discovery and direct peer connections.
More info [here](https://www.notion.so/go-bindings-Task-1a68f96fb65c804d949ffc53ef77f86b)

#### Deliverables
* PR

### Endurance

* fully qualified name: `vac:qa:waku:2025q1-waku-go-bindings-testing:endurance`
* owner: aya
* status: not started
* start-date: 2025/03/10
* end-date: 2025/03/20

#### Description
Create an endurance tests suite where we invoke waku functions thousand times 
and then making sure the memory doesn't grow, while waku still performs as expected.

#### Deliverables
* PR

### CI

* fully qualified name: `vac:qa:waku:2025q1-waku-go-bindings-testing:ci`
* owner: aya
* status: not started
* start-date: 2025/03/20
* end-date: 2025/03/30

#### Description
Create a github actions workflow that runs the tests each night.

#### Deliverables
* PR
* Github Actions Run
