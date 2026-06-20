---
title: Container Diagram (Template)
version: 1.0.0
created: 2026-06-20
updated: 2026-06-20
owner: architect
reviewers: [developer, devops]
status: draft
tags: [architecture, c4, level-2]
audience: [developers, devops]
tier: T1
related:
  - ../system-context/example.md
  - ../deployment/example.md
---

# Container Diagram — Template (C4 Level 2)

## Containers
| Container | Technology | Responsibility |
|-----------|------------|----------------|
| Web App | | |
| API | | |
| Database | | |

## PlantUML

```plantuml
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml
Person(user, "User")
System_Boundary(sys, "System") {
  Container(web, "Web App", "Tech", "UI")
  Container(api, "API", "Tech", "Business logic")
  ContainerDb(db, "Database", "Tech", "Persistence")
}
Rel(user, web, "Uses")
Rel(web, api, "HTTPS")
Rel(api, db, "TCP")
@enduml
```
