---
title: Class Diagram (Example)
version: 1.0.0
created: 2026-06-20
updated: 2026-06-20
owner: architect
reviewers: [developer]
status: approved
tags: [data, uml, class]
audience: [developers]
tier: T2
related:
  - ../entity-relationship/example.md
  - ../../architecture/component/example.md
  - ../../DIAGRAMS.md
---

# Class Diagram — Acme Platform

Complements [entity-relationship/example.md](../entity-relationship/example.md).

```mermaid
classDiagram
  class Order {
    +UUID id
    +OrderStatus status
    +UUID customerId
    +addLine(productId, qty)
    +confirm()
    +cancel(reason)
  }
  class OrderLine {
    +UUID id
    +UUID productId
    +int quantity
    +decimal lineTotal()
  }
  class Customer {
    +UUID id
    +String name
    +String email
  }
  class Product {
    +UUID id
    +String sku
    +decimal price
  }
  class OrderRepository {
    <<interface>>
    +save(order)
    +findById(id)
  }
  class OrderService {
    +createOrder(request)
    +getOrder(id)
  }
  Order "1" --> "*" OrderLine
  Order --> Customer
  OrderLine --> Product
  OrderService --> OrderRepository
  OrderService ..> Order
```

| Class | Responsibility |
|-------|----------------|
| OrderService | Business rules, transactions |
| OrderRepository | Persistence port |
| Order | Aggregate root with lifecycle |
