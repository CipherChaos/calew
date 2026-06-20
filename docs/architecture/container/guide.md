---
title: Container Diagram (Guide)
version: 1.0.0
created: 2026-06-20
updated: 2026-06-20
owner: architect
reviewers: [developer, devops]
status: approved
tags: [architecture, c4, level-2]
audience: [developers, devops]
tier: T1
related:
  - ../system-context/example.md
  - ../deployment/example.md
---

# Guide — Container Diagram

Create after system context approved. One box per independently deployable/runtime unit.

## Update Triggers
New service, tech change, new data store.

## Tools
PlantUML C4-Container, Mermaid subgraphs, draw.io (export to repo).

## Validation
Each container maps to a deployment unit in [deployment](../deployment/example.md).
