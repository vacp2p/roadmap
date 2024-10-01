---
title: Status Go Functional Testing
tags:
  - "2024q4"
  - "qa"
  - "waku"  
draft: false  
description: Collaborate with Status QA in creation a test framework that uses status-backend to do functional testing for status go
---

`vac:qa:waku:status-go-functional-testing-2024q4`

## Description

The Status Go devs have created a new tool for functional testing of Status Go features. Status QA and VAC QA will collaborate to build a testing framework around this tool and add new test coverage through this framework. The tests should validate Status features under normal and abnormal conditions and usage. We will track test coverage to measure progress.

**Alignment with VAC Narratives:**
By helping create a robust functional testing framework for Status Go, VAC QA contributes directly to the narrative of internal collaboration and efficiency. Additionally, it aligns with the goal of fostering a strong RFC culture by ensuring the tests provide valuable feedback for maintaining high standards in the specifications.

## Task List

### Migrate to Status Backend`

* fully qualified name: `vac:qa:waku:status-go-functional-testing-2024q4:migrate-to-status-backend`
* owner: fbarbu15
* status: not started
* start-date: 2024/10/07
* end-date: 2024/10/21

#### Description 
The existing Status Go tests created by VAC QA and Status QA have been using the status-cli or statusd tools, which are primarily CLI-based. Now, developers want to replace them with status-backend, a more advanced tool with a JSON-RPC based approach. We need to update the existing tests to use this new tool and ensure alignment with the Status Go testing framework.

#### Deliverables 
* PR with the updated tests
* CI runs showing similar execution results with the new tool compared to the old one

### Status tests inside status-go repo

* fully qualified name: `vac:qa:waku:status-go-functional-testing-2024q4:status-tests-in-repo`
* owner: fbarbu15
* status: not started
* start-date: 2024/10/21
* end-date: 2024/11/11

#### Description
We have been asked to move all the tests we developed into the status-go repo since they have started a similar effort using Python.

#### Deliverables
* PR with the migrated tests  
* CI runs within the new repo

### Status message tests

* fully qualified name: `vac:qa:waku:status-go-functional-testing-2024q4:status-message-tests`
* owner: fbarbu15
* status: not started
* start-date: 2024/11/11
* end-date: 2024/11/25

#### Description
It seems that the intention is for message-related tests to be handled by the Waku/VAC team, but this is still to be confirmed, so this task may change.

#### Deliverables
* PR with the new tests
