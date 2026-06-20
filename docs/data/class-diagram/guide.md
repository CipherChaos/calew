---
title: Class Diagram (Guide)
version: 1.0.0
created: 2026-06-20
updated: 2026-06-20
owner: architect
reviewers: [developer]
status: approved
tags: [data, uml, class]
audience: [developers]
tier: T2
related:
  - ../entity-relationship/example.md
  - ../../architecture/component/example.md
  - ../../DIAGRAMS.md
---

# Guide — Class Diagram

T1: Optional. T2+: Recommended. T3: Critical for complex domains.

## vs ERD
| ERD | Class |
|-----|-------|
| Tables and FK cardinality | Types, methods, interfaces |
| Persistence focus | Behavior and ports/adapters |
| `erDiagram` | `classDiagram` |

## vs Component (C4 L3)
- Class: domain model inside a container
- Component: deployable modules and their interfaces

Create after ERD; link to [component diagram](../../architecture/component/example.md) for mapping classes to modules.

T1 skip allowed per scaling-indicators.
