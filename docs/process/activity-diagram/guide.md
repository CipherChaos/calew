---
title: Activity Diagram (Guide)
version: 1.0.0
created: 2026-06-20
updated: 2026-06-20
owner: architect
reviewers: [developer, qa]
status: approved
tags: [process, activity, uml]
audience: [developers, qa]
tier: T2
related:
  - ../entity-state/example.md
  - ../workflow-sequence/example.md
  - ../../DIAGRAMS.md
---

# Guide — Activity Diagram

T1: Optional. T2+: Recommended for multi-step business processes. T3: Critical for regulated flows.

## When to use
- Internal process with branches (not cross-system message order)
- Fulfillment, approval, onboarding flows

## vs Sequence
Use Sequence for API/integration timing; Activity for business logic steps.

## vs Entity State
Activity shows *how* work proceeds; ESD shows *what states* result.

T1 skip allowed per [scaling-indicators.yaml](../../../.cursor/workflow/scaling-indicators.yaml).
