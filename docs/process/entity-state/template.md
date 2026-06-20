---
title: Entity State Diagram (Template)
version: 1.0.0
created: 2026-06-20
updated: 2026-06-20
owner: architect
reviewers: [developer, qa]
status: draft
tags: [process, state, uml]
audience: [developers, qa]
tier: T1
related:
  - ../../data/entity-relationship/example.md
  - ../workflow-sequence/example.md
  - ../../DIAGRAMS.md
---

# Entity State Diagram — Template

Model lifecycle states for a domain entity. One diagram per stateful aggregate.

```mermaid
stateDiagram-v2
  [*] --> Initial
  Initial --> Active: trigger
  Active --> Terminal: complete
  Terminal --> [*]
```

Document transitions: event, guard condition, side effects.
