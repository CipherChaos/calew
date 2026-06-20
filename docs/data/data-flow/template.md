---
title: Data Flow Diagram (Template)
version: 1.0.0
created: 2026-06-20
updated: 2026-06-20
owner: architect
reviewers: [developer]
status: draft
tags: [data, dfd]
audience: [developers, architect]
tier: T2
related:
  - ../../STANDARD.md
---

# Data Flow — Template

```mermaid
flowchart LR
  Source[Source] --> Process[Process]
  Process --> Store[(Store)]
  Process --> Sink[Sink]
```
