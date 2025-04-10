---

title: QA & RFC Synchronization for Waku Project - Core Protocols
tags:
  - "2025q2"
  - "qa"
  - "ift"
draft: false
description: Expand and formalize the QA & RFC synchronization process for the core protocols across all Waku implementations.

---

`vac:qa:ift:2025q2-qa-rfc-sync-waku`

## Description
Expand and formalize the QA & RFC synchronization process across all Waku Implementations, 
ensuring that core protocol implementations match specifications and have adequate test coverage.

Building on the previous quarter's efforts, 
this commitment focuses on systematically reviewing each Waku implementation (nim, js, go).
to ensure core protocol implementations match the corresponding RFCs. 
Any discrepancies will be flagged for either:
1. RFC updates (in collaboration with the RFC team), or 
2. Bug fixes and/or implementing missing parts in the respective repositories.

As part of this process, we will also assess the level of test automation and coverage for each core protocol, 
identifying gaps and proposing or creating additional tests as necessary.

**Alignment with VAC Narratives:**
* Continues fostering collaboration between QA, RFC contributors, and engineering teams, ensuring changes in one area promptly reflect across the ecosystem.
* Helps maintain a high standard for both internal and external contributions by detecting discrepancies early and closing testing gaps.

## Task List

### nwaku

* fully qualified name: `vac:qa:ift:2025q2-qa-rfc-sync-waku:nwaku`
* owner: fbarbu15
* status: in progress (10%)
* start-date: 2025/04/01
* end-date: 2025/06/30

#### Description
- Compare each core protocol implemented in `nwaku` against the Waku RFCs.
- Document any discrepancies found, such as missing specifications or incomplete implementations,
  and clarify whether the RFC or the implementation requires an update.
- Verify test automation exists for each core protocol and note any coverage gaps.
- Coordinate with developers for bug fixes and/or additional tests.

#### Deliverables
* Notion page summarizing the current implementation-to-RFC mapping, discrepancies, and action items.
* GitHub issues for required fixes or RFC updates.
* Recommendations for improved or additional test coverage.

### js-waku

* fully qualified name: `vac:qa:ift:2025q2-qa-rfc-sync-waku:js-waku`
* owner: fbarbu15
* status: not started
* start-date: 2025/04/01
* end-date: 2025/06/30

#### Description
- Compare each core protocol implemented in `js-waku` against the Waku RFCs.
- Document any discrepancies found, such as missing specifications or incomplete implementations,
  and clarify whether the RFC or the implementation requires an update.
- Verify test automation exists for each core protocol and note any coverage gaps.
- Coordinate with developers for bug fixes and/or additional tests.

#### Deliverables
* Notion page summarizing the current implementation-to-RFC mapping, discrepancies, and action items.
* GitHub issues for required fixes or RFC updates.
* Recommendations for improved or additional test coverage.

### go-waku

* fully qualified name: `vac:qa:ift:2025q2-qa-rfc-sync-waku:go-waku`
* owner: fbarbu15
* status: not started
* start-date: 2025/04/01
* end-date: 2025/06/30

#### Description
- Compare each core protocol implemented in `go-waku` against the Waku RFCs.
- Document any discrepancies found, such as missing specifications or incomplete implementations,
  and clarify whether the RFC or the implementation requires an update.
- Verify test automation exists for each core protocol and note any coverage gaps.
- Coordinate with developers for bug fixes and/or additional tests.

#### Deliverables
* Notion page summarizing the current implementation-to-RFC mapping, discrepancies, and action items.
* GitHub issues for required fixes or RFC updates.
* Recommendations for improved or additional test coverage.
