---

title: Status QA Documentation
tags:
  - "2025q3"
  - "qa"
  - "status"
draft: false
description: QA documentation for the Status ecosystem.

---

`vac:qa:status:2025q3-status-qa-documentation`

## Description
Establish QA documentation for the Status ecosystem, 
building on existing rfc and other documentation sources to cover app functionality. 
We should cover:
- overall QA strategy Documentation
- test plans for status features and components
- requirements documentation framework that has:
	- feature tracking
	- document lifecycle management
	- tooling and templates to support community involvement in QA processes


**Alignment with VAC Narratives:**
* Continues fostering collaboration between QA, RFC contributors, 
  and engineering teams, ensuring changes in one area promptly reflect across the ecosystem.
* Helps maintain a high standard for both internal and external contributions 
  by detecting discrepancies early and closing testing gaps.

## Task List

### QA Strategy

* fully qualified name: `vac:qa:status:2025q3-status-qa-documentation:strategy`
* owner: magnus
* status: in progress (5%)
* start-date: 2025/07/01
* end-date: 2025/07/30

#### Description
- Create a knowledge base containing the QA strategy 
  for the core components under Status ecosystem.
- For each components, we will document the existing tests, coverage, 
  how and when they are run, any identified gaps, and recommendations for improvement. 

#### Deliverables
- Notion page with QA strategy


### Test Plans

* fully qualified name: `vac:qa:status:2025q3-status-qa-documentation:test-plans`
* owner: magnus
* status: 
* start-date:
* end-date: 

#### Description
- Create test plans for new Status features, releases and [RFCs](https://rfc.vac.dev/status).
- Identify and flag gaps.

#### Deliverables
- Notion pages with test plans


### Requirements Documentation Framework
* fully qualified name: `vac:qa:status:2025q3-status-qa-documentation:requirements-framework`
* owner: magnus
* status:
* start-date:
* end-date:

#### Description
- Implement a framework covering Status Desktop core features, 
  with workflows and compatibility with other tooling.

#### Deliverables
- Adapt POC framework to Status with latest revisions (add Feature Context docs and lifecycle management)
- Migrate existing docs and create tooling (GitHub Actions, static site generation, TestRail integration)
- Expand coverage of core features (wallet, chat, communities, settings modules with full flow/screen documentation)
- Develop team adoption workflows for new features (training materials, review processes, maintenance procedures)
