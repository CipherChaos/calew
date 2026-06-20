---
title: Entity State Diagram (Example)
version: 1.0.0
created: 2026-06-20
updated: 2026-06-20
owner: architect
reviewers: [developer, qa]
status: approved
tags: [process, state, uml]
audience: [developers, qa]
tier: T1
related:
  - ../../data/entity-relationship/example.md
  - ../workflow-sequence/example.md
  - ../../DIAGRAMS.md
---

# Entity State Diagram — Acme Platform

## Order lifecycle

Maps to `ORDER.status` in [entity-relationship/example.md](../../data/entity-relationship/example.md).

```mermaid
stateDiagram-v2
  [*] --> PENDING
  PENDING --> CONFIRMED: payment_ok
  PENDING --> CANCELLED: timeout_or_user_cancel
  CONFIRMED --> SHIPPED: fulfillment_complete
  CONFIRMED --> CANCELLED: ops_cancel
  SHIPPED --> [*]
  CANCELLED --> [*]
```

| Transition | Guard | Side effect |
|------------|-------|-------------|
| PENDING → CONFIRMED | Payment authorized | Emit order.confirmed |
| CONFIRMED → SHIPPED | All lines picked | ERP webhook |
| * → CANCELLED | Policy allows | Release inventory |
