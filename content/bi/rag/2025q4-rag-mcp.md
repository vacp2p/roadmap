---
title: RAG MCP Integration
tags:
  - "2025q4"
  - "bi"
  - "rag"
draft: false
description: Build an MCP-based interface to expose RAG data and tooling.
---

`vac:bi:rag:2025q4-rag-mcp`

## Description

Prototype a Model Context Protocol workflow so BI’s RAG data sources and evaluation tools can be plugged into IDE copilots without bespoke APIs.

## Task List

### MCP Proof of Concept

* fully qualified name: `vac:bi:rag:2025q4-rag-mcp:poc`
* owner: nickninov
* status: in progress (20%)
* start-date: 2025/11/01
* end-date: 2025/12/31

#### Description

Design and implement an MCP server that exposes key RAG endpoints (search, chunk metadata, evaluation) so we can validate the integration story.

#### Deliverables
- PRs and Designs
- Scaffolded the MCP PoC with placeholder commands and began wiring it to the existing RAG services.
