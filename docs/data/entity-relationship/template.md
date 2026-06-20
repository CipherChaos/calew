---
title: Entity Relationship Diagram (Template)
version: 1.0.0
created: 2026-06-20
updated: 2026-06-20
owner: architect
reviewers: [developer]
status: draft
tags: [data, erd]
audience: [developers]
tier: T1
related:
  - ../../STANDARD.md
---

# ERD — Template

```mermaid
erDiagram
  ENTITY_A ||--o{ ENTITY_B : relates
  ENTITY_A {
    uuid id PK
    string name
  }
```
