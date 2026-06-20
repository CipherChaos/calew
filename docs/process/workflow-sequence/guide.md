---
title: Workflow Sequence Diagram (Guide)
version: 1.1.0
created: 2026-06-20
updated: 2026-06-20
owner: architect
reviewers: [developer]
status: approved
tags: [process, sequence]
audience: [developers]
tier: T1
related:
  - ../../data/api-contract/example.yaml
  - ../entity-state/example.md
  - ../activity-diagram/example.md
  - ../../DIAGRAMS.md
---

# Guide — Workflow Sequence

Create for each P1 user story. Link to [api-contract](../../data/api-contract/example.yaml).

## When to use Sequence

- **Message order** between actors/systems over time
- API calls, webhooks, request/response flows

## When to use other behavior diagrams

| Need | Use instead |
|------|-------------|
| Entity lifecycle states | [Entity State](../entity-state/guide.md) |
| Internal process steps and decisions | [Activity](../activity-diagram/guide.md) |
| Persistent structure | [ERD](../../data/entity-relationship/guide.md) |

**Sequence = who talks to whom and when. Activity = what steps happen. ESD = what states result.**

## Priority by tier

| Tier | Priority |
|------|----------|
| T1 | Recommended |
| T2+ | Critical for P1 flows |

Full matrix: [DIAGRAMS.md](../../DIAGRAMS.md)

## Pair with

[api-contract/example.yaml](../../data/api-contract/example.yaml) — sequence exercises the OpenAPI operations.
