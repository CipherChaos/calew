---
title: Entity Relationship Diagram (Guide)
version: 1.1.0
created: 2026-06-20
updated: 2026-06-20
owner: architect
reviewers: [developer]
status: approved
tags: [data, erd]
audience: [developers]
tier: T1
related:
  - ../class-diagram/example.md
  - ../../process/entity-state/example.md
  - ../../DIAGRAMS.md
---

# Guide — Entity Relationship

Derive entities from charter and glossary. Gate: `architect_to_developer`.

## What ERD shows

- **Entities** (tables, aggregates) and **relationships** (cardinality)
- Persistence structure — columns including `status` fields

## Related diagrams (create next)

| Diagram | Answers | Bundle |
|---------|---------|--------|
| **Class** | Types, methods, interfaces | [class-diagram](../class-diagram/guide.md) |
| **Entity State** | Allowed `status` transitions | [entity-state](../../process/entity-state/guide.md) |
| **Sequence** | Runtime message order | [workflow-sequence](../../process/workflow-sequence/guide.md) |

**ERD shows cardinality; Class shows types and behavior; ESD shows lifecycle transitions.**

See priority matrix: [DIAGRAMS.md](../../DIAGRAMS.md)

## Pitfalls

- **Wrong:** Putting business process steps in ERD
- **Right:** Model nouns and how they relate; use Activity or Sequence for verbs
