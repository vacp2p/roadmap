---
title: Logos Circles
tags:
  - "2026q2"
  - "web"
  - "logos"
draft: false
description: "Standardized sites for Circle admins so communities can showcase use cases for Logos tech (blockchain, messaging, storage) and manage contacts, with deployment via GitHub or CMS/CRM aligned with Logos website work."
---

`ift-ts:web:logos:2026q2-logos-circles`

## Description

This commitment supports Logos’ strategic goal to help **communities (Circles)** develop **use cases for Logos technology** (blockchain, messaging, storage) and, more broadly, **manage contacts** (volunteers, partnerships, and related relationships).

Circle **admins** should be able to **maintain a standardized website** from the content they provide and **deploy** it through one of two paths:

1. **Permission-based pipeline** — e.g. deploy via **GitHub** (approved repos, CI, previews), suitable for teams that want version control and review.
2. **Permissionless (low-friction) path** — deploy via **our CMS and CRM** capabilities, building on the same direction as [[web/logos/2026q2-logos-website|2026q2-logos-website]] (content tooling, self-hosting, and relationship/contact workflows as they land there).

The Circles product should keep **one coherent visual and content standard** so many Circle sites feel part of the same ecosystem while each Circle keeps its own copy and structure within the template.

## Task List

### Standardized Circle sites & admin experience

* fully qualified name: `ift-ts:web:logos:2026q2-logos-circles:standardized-sites-admin`
* owner: unassigned
* status: not started
* start-date: 2026/04/15
* end-date: 2026/06/15

#### Description

Define the **standardized site** pattern (layout, content slots, branding guardrails) Circle admins use from their **supplied content**. Specify how contacts and use-case stories map into the template; document the **admin workflow** (draft → review → publish) and what “maintain” means for a non-engineer versus a GitHub-based team.

#### Deliverables

- Written spec or RFC for the standard Circle site template and content model
- Admin journey (wireframes or flow) covering updates to pages, contacts, and use-case blocks
- Alignment checkpoints with design / EcoDev on Circles positioning

### Deploy pipelines — GitHub & CMS/CRM

* fully qualified name: `ift-ts:web:logos:2026q2-logos-circles:deploy-pipelines`
* owner: unassigned
* status: not started
* start-date: 2026/05/01
* end-date: 2026/06/30

#### Description

Implement or integrate **deployment** so Circle sites can ship **either** through a **permission-based GitHub-oriented pipeline** (access-controlled, build + host) **or** through **CMS/CRM-backed publishing** with minimal repo friction, **following up** on [[web/logos/2026q2-logos-website|2026q2-logos-website]] tasks (e.g. CMS direction, self-hosting). Where both paths exist, document when to recommend which path.

#### Deliverables

- GitHub pipeline outline or implementation (permissions, envs, deploy target) for at least one pilot Circle
- CMS/CRM publishing path documented or prototyped, reusing Logos website stack decisions where applicable
- Short operator doc: how to onboard a Circle, publish, and roll back
