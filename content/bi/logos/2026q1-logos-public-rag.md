---
title: Logos Public RAG
tags:
  - "2026q1"
  - "bi"
  - "logos"
draft: false
description: Create a Public RAG for the Logos Stack
---

`vac:bi:logos:2026q1-logos-public-rag`

## Description

Create a Public RAG and tooling to help the development of application using the Logos Stack.

Principal github issue: https://github.com/status-im/data-docs/issues/122

## Task List

### Update existing RAG Pipeline for public repository

* fully qualified name: `vac:bi:logos:2026q1-logos-public-rag:update-rag-pipelines`
* owner: nickninov
* status: not started
* start-date: 2026/01/01
* end-date: 2026/03/31
* url: https://github.com/status-im/data-docs/issues/131

#### Description

Adapt the ETL Pipeline to make a public RAG according to the new repository organization

#### Deliverables

- new pipeline version
- new Vector database

### MCP tooling for Logos Stack

* fully qualified name: `vac:bi:logos:2026q1-logos-public-rag:mcp-tooling`
* owner: alexis and claire
* status: not started
* start-date: 2026/01/01
* end-date: 2026/03/31
* url: https://github.com/status-im/data-docs/issues/122

#### Description

Prepare MCP tools to make the RAG data accessible in dev enviroment (Claude desktop, open-hands, ...)

#### Deliverables

- MCP server publicly available

### Messaging bot for RAG interaction

* fully qualified name: `vac:bi:logos:2026q1-logos-public-rag:messaging-bot`
* owner: tdb
* status: not started
* start-date: 2026/01/01
* end-date: 2026/03/31
* url: https://github.com/status-im/data-docs/issues/134

#### Description

Make a discord bot to interract with the Logos RAG in Discord Server (and Status)

#### Deliverables

- Discord bot interracting with the LLM
- Status bot (optional)

### Response Evaluation

* fully qualified name: `vac:bi:logos:2026q1-logos-public-rag:response-evaluation`
* owner: tdb
* status: not started
* start-date: 2026/01/01
* end-date: 2026/03/31
* url: https://github.com/status-im/data-docs/issues/132

#### Description

Automate the eualuation of the RAG replies. It must ensure the RAG reply with the latest data.

#### Deliverables

- Pipeline for Evaluation
- Alerting mecanism
