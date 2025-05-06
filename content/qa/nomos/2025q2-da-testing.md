---

title: Nomos Data Availability Testing
tags:
  - "2025q2"
  - "qa"
  - "nomos"  
draft: true  
description: Implement data availability test plans for the Nomos project at the cluster level. 

---

`vac:qa:nomos:2025q2-da-testing`

## Description
Implement data availability test plans for the Nomos project at the cluster level, 
focusing on protocol compatibility, internal interactions, data confidentiality, and resilience against failures.

**Alignment with VAC Narratives:**
- By developing and constantly updating tests for data availability,
  VAC QA ensures that the feature's implementation aligns with high standards.
- This continuous testing helps identify any spec-related issues early,
  contributing to the RFC culture and improving spec quality.
- The effort also supports IFT's strategic objective of scaling the project’s capacity
  and ensuring a reliable system for future community involvement.

## Task List

### Protocol and API Compatibility Tests

* fully qualified name: `vac:qa:nomos:2025q2-da-testing:protocol-api-compatibility`
* owner: romanzac
* status: done
* start-date: 2025/04/1
* end-date: 2025/04/15

#### Description
Add integration tests to verify DA works well with other blockchain components.

#### Deliverables
- [Test/protocol API compatibility](https://github.com/logos-co/nomos-e2e-tests/pull/14)


### Internal Interaction and Data Flow Tests

* fully qualified name: `vac:qa:nomos:2025q2-da-testing:interaction-data-flow`
* owner: romanzac
* status: done
* start-date: 2025/04/16
* end-date: 2025/05/16

#### Description
Add integration tests to verify correct interaction of the internal DA components 
to ensure correct data flow and end-to-end processing.

#### Deliverables
- [Test/interaction data flow](https://github.com/logos-co/nomos-e2e-tests/pull/15)


### Data Confidentiality

* fully qualified name: `vac:qa:nomos:2025q2-da-testing:data-confidentiality`
* owner: romanzac
* status: not started
* start-date: 2025/05/19
* end-date: 2025/06/6

#### Description
Add integration tests to verify data confidentiality, 
ensuring secure communications, and controlling unauthorized access.

#### Deliverables
* PR link with added tests
* CI runs showing successful or failed executions with detailed reports


### Data Integrity and Dispersal Process Resilience

* fully qualified name: `vac:qa:nomos:2025q2-da-testing:dispersal-resilience`
* owner: romanzac
* status: not started
* start-date: 2025/06/9
* end-date: 2025/06/30

#### Description
Add integration tests to verify the robustness of internal processes against tampering or malformed inputs 
and maintaining the integrity of the data handling mechanisms.

#### Deliverables
* PR link with added tests
* CI runs showing successful or failed executions with detailed reports
