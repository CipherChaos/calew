---
title: Component Diagram (Template)
version: 1.0.0
created: 2026-06-20
updated: 2026-06-20
owner: architect
reviewers: [developer]
status: draft
tags: [architecture, c4, level-3]
audience: [developers]
tier: T2
related:
  - ../container/example.md
---

# Component Diagram — Template (C4 Level 3)

Scope one container. List components (modules), interfaces, dependencies.

```plantuml
@startuml
package "API Container" {
  [OrderController] --> [OrderService]
  [OrderService] --> [OrderRepository]
  [OrderService] --> [EventPublisher]
}
@enduml
```
