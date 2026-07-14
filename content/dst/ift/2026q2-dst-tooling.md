---
title: DST Tooling
tags:
  - "2026q2"
  - "dst"
  - "ift"
draft: false
description: "Creating tools that allow
DST to easily work with other IFT projects.
This includes functionalities such as deployments,
monitoring, analysis, and control of aforementioned software's."
---

`ift-ts:dst:ift:2026q2-dst-tooling`

## Description

We will create tools to help DST efficiency.
These tools can be composed of utilities for Kubernetes,
or any other kind that fits the necessities of DST and other projects.
As projects might share common necessities, this tasks will be considered
as a scaffold for DST tools, adapting the tools for each project if it needs.
The primary focus will be on adapting the necessities of the Waku team for
the log parser tool. This will comprise retrieving information from a given
message id, history of discovered peers, subscriptions, while having good 
performance and supportability.
Additionally, the project will define workflows that facilitate the creation
and execution of specialized scenarios. These scenarios will assist in 
the analysis of libp2p and Gossipsub, supporting studies focused on 
adversarial conditions and control message behavior.


## Task list

### General tooling (recurring)

* fully qualified name: `ift-ts:dst:ift:2026q2-dst-tooling:general-tooling`
* owner: DST
* status: in progress (75%)
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description
Group of utilities that are added to the main repository.
Should be made general when possible.

#### Deliverables
- Code:
  - [vacp2p/10ksim/pull/239](https://github.com/vacp2p/10ksim/pull/239) - Scrape refactor
  - [vacp2p/dst-libp2p-test-node#22](https://github.com/vacp2p/dst-libp2p-test-node/pull/22) Add logging for reliability analysis
  - [vacp2p/dst-libp2p-test-node#20](https://github.com/vacp2p/dst-libp2p-test-node/pull/20) Move nim test node to its own folder
  - [vacp2p/dst-libp2p-test-node#21](https://github.com/vacp2p/dst-libp2p-test-node/pull/21) Update Docker files for amd and arm
  - [vacp2p/dst-libp2p-test-node#16](https://github.com/vacp2p/dst-libp2p-test-node/pull/16) update dockerfiles
  - [vacp2p/pod-api-requester#5](https://github.com/vacp2p/pod-api-requester/pull/5) Added lru cache to getting pods
  - [vacp2p/10ksim#243](https://github.com/vacp2p/10ksim/pull/243) Analysis: Fix dumping logs for missed messages
  - [vacp2p/10ksim#247](https://github.com/vacp2p/10ksim/pull/247) Formatting for traffic.py
  - [vacp2p/10ksim#248](https://github.com/vacp2p/10ksim/pull/248) data_puller improvements
  - [vacp2p/10ksim#249](https://github.com/vacp2p/10ksim/pull/249) Fixed missing messages for nimlibp2p_analyzer
  - [vacp2p/10ksim#250](https://github.com/vacp2p/10ksim/pull/250) Fix debug logging
  - [vacp2p/10ksim#256](https://github.com/vacp2p/10ksim/pull/256) Added WakuExperiment for regression tests
  - [vacp2p/10ksim#254](https://github.com/vacp2p/10ksim/pull/254) NimLibp2pExperiment improvements
  - [vacp2p/10ksim#255](https://github.com/vacp2p/10ksim/pull/255) Bump default pod-api-requester version
  - [vacp2p/10ksim#258](https://github.com/vacp2p/10ksim/pull/258) Added MultiExperiment base class MultiNimlibp2p
  - [vacp2p/10ksim#260](https://github.com/vacp2p/10ksim/pull/260) Allow custom condition in wait_for_rollout
  - [vacp2p/10ksim#257](https://github.com/vacp2p/10ksim/pull/257) Fix metadata bridge when namespace not used
  - [vacp2p/10ksim#259](https://github.com/vacp2p/10ksim/pull/259) add delay+jitter with initContainer logic
  - [vacp2p/10ksim#268](https://github.com/vacp2p/10ksim/pull/268) Make format
  - [vacp2p/10ksim#264](https://github.com/vacp2p/10ksim/pull/264) Fix missing messages again
  - [vacp2p/10ksim#273](https://github.com/vacp2p/10ksim/pull/273) Remove unused code
  - [vacp2p/10ksim#269](https://github.com/vacp2p/10ksim/pull/269) BaseExperiment: Moved run params into fields
  - [vacp2p/10ksim#253](https://github.com/vacp2p/10ksim/pull/253) Remove old init_logger in kube_utils
  - [vacp2p/10ksim#271](https://github.com/vacp2p/10ksim/pull/271) Add pull policy methods to builders
  - [vacp2p/10ksim#272](https://github.com/vacp2p/10ksim/pull/272) Allow to specify service + dns searchs
  - [vacp2p/10ksim#275](https://github.com/vacp2p/10ksim/pull/275) Add nimp2p-service to nimlibp2p nodes
  - [vacp2p/10ksim#278](https://github.com/vacp2p/10ksim/pull/278) Add dump to BaseExp and fix run defs
  - [vacp2p/10ksim#287](https://github.com/vacp2p/10ksim/pull/287) Fix `poll_rollout_status` return value
  - [vacp2p/pod-api-requester#9](https://github.com/vacp2p/pod-api-requester/pull/9) Set log level from env var
  - [vacp2p/10ksim#286](https://github.com/vacp2p/10ksim/pull/286) kube utils tests
  - [vacp2p/10ksim#288](https://github.com/vacp2p/10ksim/pull/288) Remove outdated test suite
  - [vacp2p/10ksim#289](https://github.com/vacp2p/10ksim/pull/289) Add security_context to ContainerConfig
  - [vacp2p/10ksim#290](https://github.com/vacp2p/10ksim/pull/290) Split kube_utils into focused modules
  - [vacp2p/10ksim#295](https://github.com/vacp2p/10ksim/pull/295) Add serialize/deserialize BaseExperiment
  - [vacp2p/10ksim#299](https://github.com/vacp2p/10ksim/pull/299) Add tests for src/deployments/core/builders.py
  - [vacp2p/10ksim#303](https://github.com/vacp2p/10ksim/pull/303) Update str with Paths
  - [vacp2p/10ksim#302](https://github.com/vacp2p/10ksim/pull/302) Remove old helm_deployment files
  - [vacp2p/10ksim#305](https://github.com/vacp2p/10ksim/pull/305) Add kaniko cluster-build tooling for native amd64 image builds
  - [vacp2p/dst-libp2p-test-node#39](https://github.com/vacp2p/dst-libp2p-test-node/pull/39) Speed up regression node build: drop unused ggplotnim, merge apt layers
- Reports:
- Other:
  - Fixed `zerotesting-store` so it runs on k8s
  - [vacp2p/10ksim#306](https://github.com/vacp2p/10ksim/pull/306) Split base bridge and tests
  - [vacp2p/10ksim#304](https://github.com/vacp2p/10ksim/pull/304) BaseExperiment deploy: allow multiple deployments at once
  - [vacp2p/10ksim#310](https://github.com/vacp2p/10ksim/pull/310) Improve experiment config CLI params
  - [vacp2p/10ksim#312](https://github.com/vacp2p/10ksim/pull/312) Fix libp2p memory and high-peers metric queries


### Dashboard

* fully qualified name: `ift-ts:dst:ift:2026q2-dst-tooling:dashboard`
* owner: Mamoutou
* status: done
* start-date: 2026/04/01
* end-date: 2026/07/14

#### Description
Present DST reports automatically in a dashboard for other CCs.

#### Deliverables
- Code:
- Reports:
  - [DST Dashboard - Proposal For a Dynamic Public Lab Dashboard](https://app.notion.com/p/DST-Dashboard-Proposal-For-a-Dynamic-Public-Lab-Dashboard-3388f96fb65c804787b7e55cf6beb027) updated architecture, experiment descriptor, and embedded DB approach.
  - [DST Dashboard V0.0](https://dev.dashboard.lab.vac.dev/) deployed as the current dev version in Vaclab
  - Completed backend processors, dataset and panel storage, ECharts conversions, React frontend, Dockerfiles, and end-to-end experiment loading from `config.yaml`
  - [DST Dashboard Backend](https://github.com/vacp2p/10ksim/pull/349)
  - [DST Dashboard Frontend](https://github.com/vacp2p/10ksim/pull/350)

### Shadow

* fully qualified name: `ift-ts:dst:ift:2026q2-dst-tooling:shadow`
* owner: Alan
* status: done
* start-date: 2026/05/18
* end-date: 2026/06/23

#### Description
Shadow simulator is hardcoded at the moment in dst-libp2p-test-node for the nim version.
We want to abstract builders from the main repository to take into account shadow.
We want to be able to launch experiments on K8s, deciding if we want to use a realistic environment, or
shadow.
This needs to take into account further data analysis of the main pipeline. Can probably be split into
subtasks.

#### Deliverables
- Code:
  - [vacp2p/10ksim#276](https://github.com/vacp2p/10ksim/pull/276) Run GossipSub experiments with Shadow
  - [vacp2p/10ksim#285](https://github.com/vacp2p/10ksim/pull/285) Add post-run Shadow analysis for metrics and message reliability
  - [vacp2p/dst-libp2p-test-node#28](https://github.com/vacp2p/dst-libp2p-test-node/pull/28) Add Shadow runner base image
  - [vacp2p/pod-api-requester#10](https://github.com/vacp2p/pod-api-requester/pull/10) Shadow Support
  - [vacp2p/dst-libp2p-test-node#36](https://github.com/vacp2p/dst-libp2p-test-node/pull/36) Shadow base requester
  - [vacp2p/10ksim#297](https://github.com/vacp2p/10ksim/pull/297) Use pod-api-requester as the publisher for Shadow
- Reports:
  - [Using Shadow at DST](https://www.notion.so/Using-Shadow-at-DST-3698f96fb65c8091b011db3f7d267d61) documents usage, design choices, and gotchas.
