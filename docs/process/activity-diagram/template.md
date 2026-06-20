---
title: Activity Diagram (Template)
version: 1.0.0
created: 2026-06-20
updated: 2026-06-20
owner: architect
reviewers: [developer, qa]
status: draft
tags: [process, activity, uml]
audience: [developers, qa]
tier: T2
related:
  - ../entity-state/example.md
  - ../workflow-sequence/example.md
  - ../../DIAGRAMS.md
---

# Activity Diagram — Template

Business process with actions, decisions, and forks.

```mermaid
flowchart TD
  Start([Start]) --> Step1[Action]
  Step1 --> Decision{Condition?}
  Decision -->|Yes| Step2[Next action]
  Decision -->|No| Fail([End fail])
  Step2 --> End([End success])
```
