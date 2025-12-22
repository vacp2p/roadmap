---
title: Community Curation
tags:
  - "2026q1"
  - "web"
  - "status"
draft: false
description: "Migration of the Community Curation DApp to the status-web monorepo, enabling SNT holders to vote on which communities should be included in the Status Communities directory."
---

`vac:web:status:2026q1-community-curation`

> *note*: The `<` `>` mark places where information has to be filled in. Please do not copy the `<` and `>` characters into the actual commitment documents.

## Description

This commitment involves migrating the Community Curation DApp to the [status-web monorepo](https://github.com/status-im/status-web), a centralized repository for building user interfaces, websites, web applications, dApps, browser extensions, and APIs in the Status ecosystem.

The Community Curation DApp allows SNT holders to determine which communities should be included in the Status Communities directory through a decentralized voting mechanism. The DApp provides governance functionality for community inclusion, removal, and featured status.

**Key Features:**
- **Community Addition Voting**: SNT holders can vote for or against adding communities to the directory
- **Community Removal Voting**: SNT holders can vote for or against removing communities from the directory
- **Weekly Featured Selection**: Ongoing voting for which communities from the directory should appear in the Weekly Featured section
- **Voting Periods**: Two-week voting periods followed by one-week verification periods
- **Cooldown Periods**: 30-day cooldown between votes for the same community addition/removal, and 3-week cooldown for Weekly Featured communities

**Voting Rules:**
- Each vote lasts for two weeks, followed by a one-week verification period
- If a vote to add ends in favor, the community is added; otherwise, a new vote can be started after 30 days
- If a vote to remove ends in favor, the community is removed; otherwise, a new vote can be submitted after 30 days
- Weekly Featured section displays five communities with the most votes, rotating weekly
- Communities that leave Weekly Featured cannot return for three weeks

The migration to the status-web monorepo will support Status' strategic objectives by:
- **Code Consolidation**: Centralizing web development efforts in a unified monorepo structure
- **Maintainability**: Improving code organization and maintenance through shared tooling and packages
- **Developer Experience**: Leveraging the monorepo's shared components, build tools, and development workflows
- **Ecosystem Integration**: Aligning with other Status web applications and tools in the same repository

## Task List

### Migration to status-web Monorepo

* fully qualified name: `vac:web:status:2026q1-community-curation:migration-to-status-web-monorepo`
* owner: JulesFiliot
* status: not started
* start-date: 2026/03/05
* end-date: 2026/03/26

#### Description

- Migrate Community Curation DApp to the status-web monorepo
- Integrate with existing monorepo structure, build tools, and shared packages
- Ensure compatibility with status-web development workflows and deployment processes

