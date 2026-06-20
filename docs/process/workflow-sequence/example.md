---
title: Workflow Sequence Diagram (Example)
version: 1.0.0
created: 2026-06-20
updated: 2026-06-20
owner: architect
reviewers: [developer]
status: approved
tags: [process, sequence]
audience: [developers]
tier: T1
related:
  - ../../STANDARD.md
---

# Workflow Sequence — Acme Platform

## Create Order

```mermaid
sequenceDiagram
  participant Buyer
  participant Portal
  participant API
  participant DB
  participant ERP
  Buyer->>Portal: Submit order
  Portal->>API: POST /orders
  API->>DB: Insert order
  API->>ERP: Webhook order.created
  API-->>Portal: 201 Created
  Portal-->>Buyer: Confirmation
```
