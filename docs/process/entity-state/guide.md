---
title: Entity State Diagram (Guide)
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

# Guide — Entity State Diagram

**Critical** when domain has lifecycle states (orders, tickets, payments). **Optional** otherwise at T1.

## vs ERD
- ERD: entities and relationships; `status` as a column
- ESD: allowed values and transitions for that column

## vs Sequence
- Sequence: message order between actors
- ESD: valid state changes regardless of caller

## vs Activity
- Activity: process steps with decisions
- ESD: entity lifecycle; pair when steps trigger state changes

Gate: recommended for `architect_to_developer` when stateful domain.
