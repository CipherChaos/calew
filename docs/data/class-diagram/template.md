---
title: Class Diagram (Template)
version: 1.0.0
created: 2026-06-20
updated: 2026-06-20
owner: architect
reviewers: [developer]
status: draft
tags: [data, uml, class]
audience: [developers]
tier: T2
related:
  - ../entity-relationship/example.md
  - ../../architecture/component/example.md
  - ../../DIAGRAMS.md
---

# Class Diagram — Template

Domain types with attributes, methods, and relationships. Complements ERD — not a duplicate.

```mermaid
classDiagram
  class EntityName {
    +UUID id
    +String name
    +validate()
  }
  EntityName --> OtherEntity : association
```
