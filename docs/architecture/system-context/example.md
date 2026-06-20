---
title: System Context Diagram (Example)
version: 1.0.0
created: 2026-06-20
updated: 2026-06-20
owner: architect
reviewers: [devops, manager]
status: approved
tags: [architecture, c4, level-1]
audience: [developers, stakeholders]
tier: T1
related:
  - ../container/example.md
  - ../../data/api-contract/example.yaml
  - ../../../.cursor/agents/architect/RULE.md
---

# System Context — Acme Platform

Acme Platform is a B2B order management SaaS connecting buyers, Acme ops, and customer ERP systems.

## Diagram (Mermaid)

```mermaid
flowchart TB
  Buyer[Buyer User] --> Acme[Acme Platform]
  Ops[Acme Operations] --> Acme
  Acme --> ERP[Customer ERP Systems]
  Acme --> Email[Email Provider]
  Acme --> Pay[Payment Gateway]
```

## Actors
| Actor | Description |
|-------|-------------|
| Buyer User | Creates and tracks orders via web portal |
| Acme Operations | Manages catalog, fulfillment, support |

## External Systems
| System | Purpose | Protocol |
|--------|---------|----------|
| Customer ERP | Order sync | REST + webhooks |
| Email Provider | Notifications | SMTP/API |
| Payment Gateway | Billing | REST |
