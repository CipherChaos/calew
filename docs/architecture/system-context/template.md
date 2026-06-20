---
title: System Context Diagram (Template)
version: 1.0.0
created: 2026-06-20
updated: 2026-06-20
owner: architect
reviewers: [devops, manager]
status: draft
tags: [architecture, c4, level-1]
audience: [developers, stakeholders]
tier: T1
related:
  - ../container/example.md
  - ../../data/api-contract/example.yaml
  - ../../../.cursor/agents/architect/RULE.md
---

# System Context — Template (C4 Level 1)

## System Name
[Your System Name]

## Purpose
[One paragraph]

## Diagram (PlantUML)

```plantuml
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Context.puml
Person(user, "Primary User", "Description")
System(system, "System Name", "Core capability")
System_Ext(ext, "External System", "Integration")
Rel(user, system, "Uses")
Rel(system, ext, "Integrates")
@enduml
```

## Diagram (Mermaid fallback)

```mermaid
flowchart TB
  User[Primary User] --> System[System Name]
  System --> External[External System]
```

## Actors
| Actor | Description |
|-------|-------------|
| | |

## External Systems
| System | Purpose | Protocol |
|--------|---------|----------|
| | | |
