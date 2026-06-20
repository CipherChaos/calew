#!/usr/bin/env python3
"""Generate documentation bundles for project-workflow blueprint."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

FM = """---
title: {title}
version: 1.0.0
created: 2026-06-20
updated: 2026-06-20
owner: {owner}
reviewers: {reviewers}
status: {status}
tags: {tags}
audience: {audience}
tier: {tier}
related:
{related}
---

"""


def w(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)


def bundle(cat, slug, meta, template_body, example_body, guide_body, ext="md"):
    base = DOCS / cat / slug
    rel = meta.get("related_paths", [])
    related_yaml = "\n".join(f"  - {r}" for r in rel) if rel else "  - ../../STANDARD.md"
    for kind, body, status in [
        ("template", template_body, "draft"),
        ("example", example_body, "approved"),
        ("guide", guide_body, "approved"),
    ]:
        title = f"{meta['title']} ({kind.title()})"
        fm = FM.format(
            title=title,
            owner=meta["owner"],
            reviewers=meta["reviewers"],
            status=status,
            tags=meta["tags"],
            audience=meta["audience"],
            tier=meta["tier"],
            related=related_yaml,
        )
        suffix = f".{ext}" if kind == "example" and ext != "md" else ".md"
        if kind == "example" and ext != "md":
            w(base / f"{kind}.{ext}", fm + body)
        else:
            w(base / f"{kind}.md", fm + body)


def category_readme(cat, title, rows, agent_link):
    body = f"# {title}\n\n| Document | Tier | Bundle |\n|----------|------|--------|\n"
    for name, tier, slug in rows:
        body += f"| {name} | {tier} | [{slug}/]({slug}/) |\n"
    body += f"\nAgent: [{agent_link}]({agent_link})\n"
    w(DOCS / cat / "README.md", body)


# --- Process bundles ---
process_bundles = [
    ("workflow-sequence", "Workflow Sequence Diagram", "architect", "[developer]", "[process, sequence]", "[developers]", "T1",
     "# Workflow Sequence — Template\n\nDocument request/response flows for key use cases.\n\n```mermaid\nsequenceDiagram\n  participant User\n  participant API\n  participant DB\n  User->>API: Request\n  API->>DB: Query\n  DB-->>API: Result\n  API-->>User: Response\n```\n",
     "# Workflow Sequence — Acme Platform\n\n## Create Order\n\n```mermaid\nsequenceDiagram\n  participant Buyer\n  participant Portal\n  participant API\n  participant DB\n  participant ERP\n  Buyer->>Portal: Submit order\n  Portal->>API: POST /orders\n  API->>DB: Insert order\n  API->>ERP: Webhook order.created\n  API-->>Portal: 201 Created\n  Portal-->>Buyer: Confirmation\n```\n",
     "# Guide — Workflow Sequence\n\nCreate for each P1 user story. Link to [api-contract](../../data/api-contract/example.yaml).\n"),
    ("project-timeline", "Project Timeline", "manager", "[architect, devops]", "[pm, timeline]", "[stakeholders]", "T1",
     "# Project Timeline — Template\n\n| Milestone | Target date | Owner | Dependencies |\n|-----------|-------------|-------|--------------|\n| | | | |\n",
     "# Project Timeline — Acme Platform\n\n| Milestone | Target | Owner |\n|-----------|--------|-------|\n| Charter approved | Week 1 | Manager |\n| Architecture baseline | Week 3 | Architect |\n| MVP feature complete | Week 8 | Developer |\n| QA sign-off | Week 9 | QA |\n| Production launch | Week 10 | DevOps |\n",
     "# Guide — Project Timeline\n\nUpdate weekly. Tie milestones to sprint goals in [sprint-planning](../../project-management/sprint-planning/example.md).\n"),
    ("release-process", "Release Process", "devops", "[manager, qa]", "[process, release]", "[devops, developers]", "T2",
     "# Release Process — Template\n\n## Release checklist\n1. RC tagged\n2. QA sign-off\n3. Change window approved\n4. Deploy staging → prod\n5. Smoke test\n6. Stakeholder comms\n",
     "# Release Process — Acme Platform\n\n- **Cadence:** Bi-weekly, Tuesday 02:00 UTC\n- **RC tag:** `v{major}.{minor}.{patch}-rc1`\n- **Approval:** Manager + QA for T2+\n- **Rollback:** Redeploy previous artifact within 15 minutes\n",
     "# Guide — Release Process\n\nT1: informal releases OK with QA email sign-off. T2+: follow checklist. Link [quality-gates.yaml](../../../.cursor/workflow/quality-gates.yaml) gate `qa_to_devops`.\n"),
    ("incident-response", "Incident Response", "devops", "[manager, qa]", "[process, incident]", "[devops, on-call]", "T2",
     "# Incident Response — Template\n\n## Severity\n| Level | Response time |\n|-------|---------------|\n| P0 | Immediate |\n| P1 | 1 hour |\n\n## Steps\n1. Detect → Triage → Mitigate → Communicate → Postmortem\n",
     "# Incident Response — Acme Platform\n\n- **P0:** Order API down — page on-call, status page update within 15m\n- **Runbook:** [deployment/example.md](../../architecture/deployment/example.md)\n- **Postmortem:** Within 5 business days for P0/P1\n",
     "# Guide — Incident Response\n\nAlign severity with [escalation-matrix.md](../../../.cursor/workflow/escalation-matrix.md).\n"),
    ("change-management", "Change Management", "manager", "[devops, architect]", "[process, change]", "[all agents]", "T2",
     "# Change Management — Template\n\n## Change types\n| Type | Approval |\n|------|----------|\n| Standard | Team lead |\n| Normal | Manager |\n| Emergency | Manager + DevOps post-facto |\n",
     "# Change Management — Acme Platform\n\n- **Standard:** Dependency patch, config tweak — peer review\n- **Normal:** Schema migration, new service — Architect review + QA regression\n- **Emergency:** Hotfix — deploy then document SCR within 24h\n",
     "# Guide — Change Management\n\nDocument scope changes via SCR template in [manager/RULE.md](../../../.cursor/agents/manager/RULE.md).\n"),
    ("code-review", "Code Review Process", "developer", "[architect, qa]", "[process, review]", "[developers]", "T1",
     "# Code Review — Template\n\n## Checklist\n- [ ] Matches API contract\n- [ ] Tests added/updated\n- [ ] No secrets\n- [ ] Lint clean\n- [ ] Security patterns followed\n",
     "# Code Review — Acme Platform\n\n- **PR size:** ≤400 lines preferred\n- **Required reviewers:** 1 dev; Architect for API/schema changes\n- **CI:** lint + unit + integration must pass\n- **Branch naming:** `feature/REQ-*`, `fix/BUG-*`\n",
     "# Guide — Code Review\n\nDeveloper gate before `developer_to_qa`. See [developer/RULE.md](../../../.cursor/agents/developer/RULE.md).\n"),
]

for slug, title, owner, reviewers, tags, audience, tier, tmpl, ex, guide in process_bundles:
    bundle("process", slug, dict(title=title, owner=owner, reviewers=reviewers, tags=tags, audience=audience, tier=tier), tmpl, ex, guide)

category_readme("process", "Process Documentation",
    [("Workflow Sequence", "T1+", "workflow-sequence"), ("Project Timeline", "T1+", "project-timeline"),
     ("Release Process", "T2+", "release-process"), ("Incident Response", "T2+", "incident-response"),
     ("Change Management", "T2+", "change-management"), ("Code Review", "T1+", "code-review")],
    "../../.cursor/agents/manager/RULE.md")

# --- Data bundles ---
data_bundles = [
    ("entity-relationship", "Entity Relationship Diagram", "architect", "[developer]", "[data, erd]", "[developers]", "T1",
     "# ERD — Template\n\n```mermaid\nerDiagram\n  ENTITY_A ||--o{ ENTITY_B : relates\n  ENTITY_A {\n    uuid id PK\n    string name\n  }\n```\n",
     "# ERD — Acme Platform\n\n```mermaid\nerDiagram\n  CUSTOMER ||--o{ ORDER : places\n  ORDER ||--|{ ORDER_LINE : contains\n  PRODUCT ||--o{ ORDER_LINE : referenced\n  CUSTOMER {\n    uuid id PK\n    string name\n    string email\n  }\n  ORDER {\n    uuid id PK\n    uuid customer_id FK\n    string status\n    timestamp created_at\n  }\n  ORDER_LINE {\n    uuid id PK\n    uuid order_id FK\n    uuid product_id FK\n    int quantity\n  }\n  PRODUCT {\n    uuid id PK\n    string sku\n    string name\n    decimal price\n  }\n```\n",
     "# Guide — Entity Relationship\n\nDerive entities from charter and glossary. Gate: `architect_to_developer`.\n"),
    ("data-flow", "Data Flow Diagram", "architect", "[developer]", "[data, dfd]", "[developers, architect]", "T2",
     "# Data Flow — Template\n\n```mermaid\nflowchart LR\n  Source[Source] --> Process[Process]\n  Process --> Store[(Store)]\n  Process --> Sink[Sink]\n```\n",
     "# Data Flow — Acme Platform\n\n```mermaid\nflowchart LR\n  Portal[Web Portal] --> API[Order API]\n  API --> PG[(PostgreSQL)]\n  API --> Q[Message Queue]\n  Worker[Integration Worker] --> Q\n  Worker --> ERP[Customer ERP]\n```\n",
     "# Guide — Data Flow\n\nT2+ required. Show PII boundaries for GDPR projects.\n"),
    ("data-lifecycle", "Data Lifecycle", "architect", "[devops, manager]", "[data, lifecycle]", "[architect, devops]", "T3",
     "# Data Lifecycle — Template\n\n| Data class | Retention | Archive | Delete |\n|------------|-----------|---------|--------|\n| | | | |\n",
     "# Data Lifecycle — Acme Platform\n\n| Data class | Retention | Archive | Delete |\n|------------|-----------|---------|--------|\n| Orders | 7 years | S3 Glacier after 2y | Secure wipe after retention |\n| Audit logs | 3 years | — | — |\n| Session tokens | 24 hours | — | Auto-expire |\n",
     "# Guide — Data Lifecycle\n\nT3 mandatory. Legal review for regulated industries.\n"),
    ("data-mapping", "Data Mapping", "developer", "[architect]", "[data, mapping]", "[developers]", "T3",
     "# Data Mapping — Template\n\n| Source field | Target field | Transform | Notes |\n|--------------|--------------|-----------|-------|\n| | | | |\n",
     "# Data Mapping — Acme Platform\n\n| Acme field | ERP field | Transform |\n|------------|-----------|----------|\n| order.id | external_ref | UUID string |\n| order.status | state | enum map: PENDING→open |\n| order_line.quantity | qty | integer |\n",
     "# Guide — Data Mapping\n\nRequired for ERP/integration features. Update when API contract changes.\n"),
]

for slug, title, owner, reviewers, tags, audience, tier, tmpl, ex, guide in data_bundles:
    bundle("data", slug, dict(title=title, owner=owner, reviewers=reviewers, tags=tags, audience=audience, tier=tier), tmpl, ex, guide)

# API contract as YAML example
bundle("data", "api-contract",
    dict(title="API Contract (OpenAPI)", owner="architect", reviewers="[developer, qa]",
         tags="[data, api, openapi]", audience="[developers, qa]", tier="T1",
         related_paths=["../entity-relationship/example.md", "../../architecture/container/example.md"]),
    """# API Contract — Template

Create `example.yaml` with OpenAPI 3.1. Minimum: info, servers, paths, components.schemas.

```yaml
openapi: 3.1.0
info:
  title: Your API
  version: 1.0.0
paths: {}
```
""",
    """openapi: 3.1.0
info:
  title: Acme Order API
  version: 1.0.0
  description: B2B order management for Acme Platform
servers:
  - url: https://api.acme.example/v1
paths:
  /orders:
    post:
      summary: Create order
      operationId: createOrder
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateOrderRequest'
      responses:
        '201':
          description: Created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Order'
        '400':
          description: Validation error
  /orders/{orderId}:
    get:
      summary: Get order by ID
      parameters:
        - name: orderId
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Order'
components:
  schemas:
    CreateOrderRequest:
      type: object
      required: [customerId, lines]
      properties:
        customerId:
          type: string
          format: uuid
        lines:
          type: array
          items:
            $ref: '#/components/schemas/OrderLineInput'
    OrderLineInput:
      type: object
      required: [productId, quantity]
      properties:
        productId:
          type: string
          format: uuid
        quantity:
          type: integer
          minimum: 1
    Order:
      type: object
      properties:
        id:
          type: string
          format: uuid
        status:
          type: string
          enum: [PENDING, CONFIRMED, SHIPPED, CANCELLED]
        customerId:
          type: string
          format: uuid
        lines:
          type: array
          items:
            $ref: '#/components/schemas/OrderLineInput'
        createdAt:
          type: string
          format: date-time
""",
    """# Guide — API Contract

OpenAPI is source of truth. Gate: `architect_to_developer`.

- Version breaking changes with `/v2` prefix
- Include standard error envelope with correlationId
- Idempotency-Key header on POST /orders
""",
    ext="yaml")

category_readme("data", "Data Documentation",
    [("Entity Relationship", "T1+", "entity-relationship"), ("Data Flow", "T2+", "data-flow"),
     ("Data Lifecycle", "T3", "data-lifecycle"), ("Data Mapping", "T3", "data-mapping"),
     ("API Contract", "T1+", "api-contract")],
    "../../.cursor/agents/architect/RULE.md")

# --- UX bundles ---
ux_bundles = [
    ("user-journey", "User Journey Map", "manager", "[qa, developer]", "[ux, journey]", "[pm, qa]", "T2",
     "# User Journey — Template\n\n| Stage | User action | Touchpoint | Pain points | Opportunities |\n|-------|-------------|------------|-------------|---------------|\n| | | | | |\n",
     "# User Journey — Acme Platform\n\n## Buyer: Place first order\n\n| Stage | Action | Touchpoint | Notes |\n|-------|--------|------------|-------|\n| Discover | Log in via SSO | Portal | OIDC |\n| Browse | Search catalog | Portal | Filter by SKU |\n| Order | Add lines, submit | Portal → API | Idempotent POST |\n| Track | View status | Portal | Webhook updates from ERP |\n",
     "# Guide — User Journey\n\nT2+ for major features. QA derives test scenarios from journeys.\n"),
    ("wireframes", "Wireframes", "developer", "[manager]", "[ux, wireframe]", "[developers, pm]", "T1",
     "# Wireframes — Template\n\nDescribe screens in ASCII or link to Figma export.\n\n```\n+----------------------------+\n| Logo          [User menu]  |\n+----------------------------+\n| [Search...............]    |\n| +--------+ +--------+      |\n| | Item 1 | | Item 2 |      |\n| +--------+ +--------+      |\n+----------------------------+\n```\n",
     "# Wireframes — Acme Platform\n\n## Order list screen\n\n```\n+----------------------------------+\n| Acme Portal     buyer@corp.com v |\n+----------------------------------+\n| Orders          [+ New Order]    |\n| +------+--------+--------+       |\n| | ID   | Status | Total  |       |\n| | a1b2 | PENDING| $420   |       |\n| +------+--------+--------+       |\n+----------------------------------+\n```\n",
     "# Guide — Wireframes\n\nT1: ASCII sufficient. T2+: link design tool exports in repo.\n"),
    ("design-system", "Design System", "developer", "[qa]", "[ux, design]", "[developers]", "T2",
     "# Design System — Template\n\n## Tokens\n| Token | Value | Usage |\n|-------|-------|-------|\n| color-primary | | |\n\n## Components\n| Component | Variants | Accessibility |\n|-----------|----------|---------------|\n| | | |\n",
     "# Design System — Acme Platform\n\n| Token | Value |\n|-------|-------|\n| color-primary | #2563eb |\n| color-error | #dc2626 |\n| spacing-unit | 4px |\n\n| Component | Notes |\n|-----------|-------|\n| Button | primary, secondary, danger |\n| DataTable | sortable, paginated |\n| FormField | label + error slot |\n",
     "# Guide — Design System\n\nT2+ for multi-developer UI work. Link [accessibility](accessibility/example.md).\n"),
    ("accessibility", "Accessibility Checklist", "qa", "[developer]", "[ux, a11y]", "[qa, developers]", "T2",
     "# Accessibility — Template\n\n- [ ] Keyboard navigation\n- [ ] Screen reader labels\n- [ ] Color contrast WCAG AA\n- [ ] Focus indicators\n- [ ] Form error association\n",
     "# Accessibility — Acme Platform\n\n- WCAG 2.1 AA target\n- All interactive elements tabbable\n- aria-label on icon-only buttons\n- Status badges include text, not color alone\n- Automated axe scan in CI for portal PRs\n",
     "# Guide — Accessibility\n\nQA gate T2+. Reference [security architecture](../architecture/security/example.md) for auth flows.\n"),
    ("usability-testing", "Usability Testing", "qa", "[manager]", "[ux, testing]", "[qa, pm]", "T2",
     "# Usability Testing — Template\n\n## Session plan\n| Task | Success criteria | Observer notes |\n|------|------------------|----------------|\n| | | |\n",
     "# Usability Testing — Acme Platform\n\n| Task | Success criteria |\n|------|------------------|\n| Create order with 3 line items | Completes in <3 min without help |\n| Find shipped order status | Locates within 2 clicks |\n\n**Participants:** 5 buyer users (T2 UAT minimum 3)\n",
     "# Guide — Usability Testing\n\nT2+ formal UAT supplement. Document in test report for `qa_to_devops`.\n"),
]

for slug, title, owner, reviewers, tags, audience, tier, tmpl, ex, guide in ux_bundles:
    bundle("ux", slug, dict(title=title, owner=owner, reviewers=reviewers, tags=tags, audience=audience, tier=tier), tmpl, ex, guide)

category_readme("ux", "User Experience Documentation",
    [("User Journey", "T2+", "user-journey"), ("Wireframes", "T1+", "wireframes"),
     ("Design System", "T2+", "design-system"), ("Accessibility", "T2+", "accessibility"),
     ("Usability Testing", "T2+", "usability-testing")],
    "../../.cursor/agents/qa/RULE.md")

# --- Project management bundles ---
pm_bundles = [
    ("project-charter", "Project Charter", "manager", "[architect]", "[pm, charter]", "[stakeholders]", "T1",
     "# Project Charter — Template\n\n## Purpose\n\n## Scope\n### In scope\n### Out of scope\n\n## Success metrics\n\n## Tier classification\n\n## Stakeholders\n",
     "# Project Charter — Acme Platform\n\n## Purpose\nDeliver B2B order management SaaS for mid-market manufacturers.\n\n## Scope\n**In:** Web portal, Order API, ERP integration, SSO\n**Out:** Native mobile apps, custom ERP adapters per customer\n\n## Success metrics\n- 50 pilot customers in 6 months\n- p95 order create < 300ms\n- 99.5% monthly API availability\n\n## Tier\nT2 — 6 devs, 2 deployable services, formal UAT\n",
     "# Guide — Project Charter\n\nFirst Manager deliverable. Gate: `manager_to_architect`.\n"),
    ("glossary", "Glossary", "manager", "[architect, developer]", "[pm, glossary]", "[all]", "T1",
     "# Glossary — Template\n\n| Term | Definition |\n|------|------------|\n| | |\n",
     "# Glossary — Acme Platform\n\n| Term | Definition |\n|------|------------|\n| Buyer | Customer org user who places orders |\n| Order | Header + line items representing a purchase request |\n| ERP | Customer enterprise resource planning system |\n| RC | Release candidate build for QA |\n",
     "# Guide — Glossary\n\nUpdate when new domain terms appear in stories or API.\n"),
    ("risk-assessment", "Risk Assessment", "manager", "[architect, devops]", "[pm, risk]", "[stakeholders]", "T1",
     "# Risk Assessment — Template\n\n| ID | Risk | P(1-5) | I(1-5) | Score | Mitigation | Owner |\n|----|------|--------|--------|-------|------------|-------|\n| | | | | | | |\n",
     "# Risk Assessment — Acme Platform\n\n| ID | Risk | P | I | Score | Mitigation |\n|----|------|---|---|-------|------------|\n| R1 | ERP webhook delays | 3 | 4 | 12 | Retry queue + DLQ |\n| R2 | SSO IdP outage | 2 | 5 | 10 | Cached session grace period |\n| R3 | Scope creep on integrations | 4 | 3 | 12 | SCR process, MoSCoW |\n",
     "# Guide — Risk Assessment\n\nScore ≥13 → escalate. Review each sprint (T1) or weekly (T2+).\n"),
    ("stakeholder-map", "Stakeholder Map", "manager", "[architect]", "[pm, stakeholder]", "[manager]", "T2",
     "# Stakeholder Map — Template\n\n| Stakeholder | Interest | Influence | Communication |\n|-------------|----------|-----------|---------------|\n| | | | |\n",
     "# Stakeholder Map — Acme Platform\n\n| Stakeholder | Interest | Influence | Communication |\n|-------------|----------|-----------|---------------|\n| Product sponsor | ROI, timeline | High | Weekly status |\n| Buyer IT | SSO, security | High | Architecture review |\n| Operations | Uptime, support | Medium | Release notes |\n",
     "# Guide — Stakeholder Map\n\nT2+ required. Drives [communication-protocol](../../../.cursor/workflow/communication-protocol.md).\n"),
    ("sprint-planning", "Sprint Planning", "manager", "[developer, architect]", "[pm, agile]", "[team]", "T1",
     "# Sprint Planning — Template\n\n## Sprint goal\n\n## Capacity (hours × 0.7)\n\n## Stories\n| ID | Story | Points | Owner | Acceptance criteria |\n|----|-------|--------|-------|---------------------|\n| | | | | |\n",
     "# Sprint Planning — Acme Platform\n\n## Sprint 2 goal\nDeliver order creation API and portal form.\n\n## Stories\n| ID | Story | Owner | Acceptance criteria |\n|----|-------|-------|---------------------|\n| REQ-12 | POST /orders | Developer | OpenAPI compliant, tests 80%+ |\n| REQ-13 | Order form UI | Developer | Wireframe match, a11y pass |\n| REQ-14 | ERP webhook | Developer | HMAC verified, idempotent |\n",
     "# Guide — Sprint Planning\n\nManager owns ceremony. Architect stories must complete before dependent dev stories.\n"),
]

for slug, title, owner, reviewers, tags, audience, tier, tmpl, ex, guide in pm_bundles:
    bundle("process" if False else "project-management", slug,
            dict(title=title, owner=owner, reviewers=reviewers, tags=tags, audience=audience, tier=tier), tmpl, ex, guide)

category_readme("project-management", "Project Management Documentation",
    [("Project Charter", "T1+", "project-charter"), ("Glossary", "T1+", "glossary"),
     ("Risk Assessment", "T1+", "risk-assessment"), ("Stakeholder Map", "T2+", "stakeholder-map"),
     ("Sprint Planning", "T1+", "sprint-planning"), ("Work Breakdown Structure", "T1+", "work-breakdown")],
    "../../.cursor/agents/manager/RULE.md")

# --- v1.1 Diagram expansion bundles ---

bundle(
    "project-management", "work-breakdown",
    dict(title="Work Breakdown Structure", owner="manager", reviewers="[architect, developer]",
         tags="[pm, wbs, planning]", audience="[team, stakeholders]", tier="T1",
         related_paths=["../project-charter/example.md", "../sprint-planning/example.md", "../../DIAGRAMS.md"]),
    """# Work Breakdown Structure — Template

Decompose project into deliverable work packages aligned with agent phases.

```mermaid
mindmap
  root((Project Name))
    Foundation
      Charter
      Glossary
    Architecture
      C4 diagrams
      API contract
    Implementation
    Verification
    Release
```

Or use numbered tree:

```
1.0 Project Name
├── 1.1 Work package
│   └── 1.1.1 Task
```
""",
    """# Work Breakdown Structure — Acme Platform

```mermaid
mindmap
  root((Acme Platform))
    1 Foundation
      1.1 Charter and glossary
      1.2 Risk and tier
    2 Architecture
      2.1 C4 L1/L2
      2.2 ERD API ESD
      2.3 ERP integration design
    3 Implementation
      3.1 Order API
      3.2 Portal UI
      3.3 Integration worker
    4 Verification
      4.1 Test automation
      4.2 UAT
    5 Release
      5.1 CI/CD
      5.2 Production deploy
```

## Text tree

```
Acme Platform
├── 1. Foundation (Manager)
│   ├── 1.1 Charter & glossary
│   └── 1.2 Risk & tier
├── 2. Architecture (Architect)
│   ├── 2.1 C4 + ERD + API
│   └── 2.2 Integration design
├── 3. Implementation (Developer)
│   ├── 3.1 Order API
│   └── 3.2 Portal UI
├── 4. Verification (QA)
└── 5. Release (DevOps)
```

Leaf tasks map to [sprint-planning/example.md](../sprint-planning/example.md) stories.
""",
    """# Guide — Work Breakdown Structure

Create after charter draft, before Sprint 1. Align WBS level-1 with agent phases (Manager → DevOps).

## When to update
- Major scope change (SCR approved)
- New deployable unit added

## Priority
**Critical** at all tiers per [DIAGRAMS.md](../../DIAGRAMS.md).

## Pair with
[sprint-planning](../sprint-planning/guide.md) — WBS leaves become sprint stories.
""",
)

bundle(
    "process", "entity-state",
    dict(title="Entity State Diagram", owner="architect", reviewers="[developer, qa]",
         tags="[process, state, uml]", audience="[developers, qa]", tier="T1",
         related_paths=["../../data/entity-relationship/example.md", "../workflow-sequence/example.md", "../../DIAGRAMS.md"]),
    """# Entity State Diagram — Template

Model lifecycle states for a domain entity. One diagram per stateful aggregate.

```mermaid
stateDiagram-v2
  [*] --> Initial
  Initial --> Active: trigger
  Active --> Terminal: complete
  Terminal --> [*]
```

Document transitions: event, guard condition, side effects.
""",
    """# Entity State Diagram — Acme Platform

## Order lifecycle

Maps to `ORDER.status` in [entity-relationship/example.md](../../data/entity-relationship/example.md).

```mermaid
stateDiagram-v2
  [*] --> PENDING
  PENDING --> CONFIRMED: payment_ok
  PENDING --> CANCELLED: timeout_or_user_cancel
  CONFIRMED --> SHIPPED: fulfillment_complete
  CONFIRMED --> CANCELLED: ops_cancel
  SHIPPED --> [*]
  CANCELLED --> [*]
```

| Transition | Guard | Side effect |
|------------|-------|-------------|
| PENDING → CONFIRMED | Payment authorized | Emit order.confirmed |
| CONFIRMED → SHIPPED | All lines picked | ERP webhook |
| * → CANCELLED | Policy allows | Release inventory |
""",
    """# Guide — Entity State Diagram

**Critical** when domain has lifecycle states (orders, tickets, payments). **Optional** otherwise at T1.

## vs ERD
- ERD: entities and relationships; `status` as a column
- ESD: allowed values and transitions for that column

## vs Sequence
- Sequence: message order between actors
- ESD: valid state changes regardless of caller

## vs Activity
- Activity: process steps with decisions
- ESD: entity lifecycle; pair when steps trigger state changes

Gate: recommended for `architect_to_developer` when stateful domain.
""",
)

bundle(
    "process", "activity-diagram",
    dict(title="Activity Diagram", owner="architect", reviewers="[developer, qa]",
         tags="[process, activity, uml]", audience="[developers, qa]", tier="T2",
         related_paths=["../entity-state/example.md", "../workflow-sequence/example.md", "../../DIAGRAMS.md"]),
    """# Activity Diagram — Template

Business process with actions, decisions, and forks.

```mermaid
flowchart TD
  Start([Start]) --> Step1[Action]
  Step1 --> Decision{Condition?}
  Decision -->|Yes| Step2[Next action]
  Decision -->|No| Fail([End fail])
  Step2 --> End([End success])
```
""",
    """# Activity Diagram — Acme Platform

## Order fulfillment process

```mermaid
flowchart TD
  Start([Order CONFIRMED]) --> CheckInv{Inventory available?}
  CheckInv -->|No| Backorder[Mark backordered]
  Backorder --> NotifyBuyer[Notify buyer]
  CheckInv -->|Yes| Pick[Pick and pack]
  Pick --> SyncERP{ERP sync OK?}
  SyncERP -->|No| Retry[Retry with backoff]
  Retry --> SyncERP
  SyncERP -->|Yes| Ship[Update status SHIPPED]
  Ship --> End([Complete])
  NotifyBuyer --> Wait([Wait for restock])
```

Triggers [entity-state/example.md](../entity-state/example.md) transition CONFIRMED → SHIPPED.
""",
    """# Guide — Activity Diagram

T1: Optional. T2+: Recommended for multi-step business processes. T3: Critical for regulated flows.

## When to use
- Internal process with branches (not cross-system message order)
- Fulfillment, approval, onboarding flows

## vs Sequence
Use Sequence for API/integration timing; Activity for business logic steps.

## vs Entity State
Activity shows *how* work proceeds; ESD shows *what states* result.

T1 skip allowed per [scaling-indicators.yaml](../../../.cursor/workflow/scaling-indicators.yaml).
""",
)

bundle(
    "data", "class-diagram",
    dict(title="Class Diagram", owner="architect", reviewers="[developer]",
         tags="[data, uml, class]", audience="[developers]", tier="T2",
         related_paths=["../entity-relationship/example.md", "../../architecture/component/example.md", "../../DIAGRAMS.md"]),
    """# Class Diagram — Template

Domain types with attributes, methods, and relationships. Complements ERD — not a duplicate.

```mermaid
classDiagram
  class EntityName {
    +UUID id
    +String name
    +validate()
  }
  EntityName --> OtherEntity : association
```
""",
    """# Class Diagram — Acme Platform

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
""",
    """# Guide — Class Diagram

T1: Optional. T2+: Recommended. T3: Critical for complex domains.

## vs ERD
| ERD | Class |
|-----|-------|
| Tables and FK cardinality | Types, methods, interfaces |
| Persistence focus | Behavior and ports/adapters |
| `erDiagram` | `classDiagram` |

## vs Component (C4 L3)
- Class: domain model inside a container
- Component: deployable modules and their interfaces

Create after ERD; link to [component diagram](../../architecture/component/example.md) for mapping classes to modules.

T1 skip allowed per scaling-indicators.
""",
)

# Update process and data READMEs with new bundles
category_readme("process", "Process Documentation",
    [("Workflow Sequence", "T1+", "workflow-sequence"), ("Entity State", "T1+", "entity-state"),
     ("Activity Diagram", "T2+", "activity-diagram"), ("Project Timeline", "T1+", "project-timeline"),
     ("Release Process", "T2+", "release-process"), ("Incident Response", "T2+", "incident-response"),
     ("Change Management", "T2+", "change-management"), ("Code Review", "T1+", "code-review")],
    "../../.cursor/agents/architect/RULE.md")

category_readme("data", "Data Documentation",
    [("Entity Relationship", "T1+", "entity-relationship"), ("Class Diagram", "T2+", "class-diagram"),
     ("Data Flow", "T2+", "data-flow"), ("Data Lifecycle", "T3", "data-lifecycle"),
     ("Data Mapping", "T3", "data-mapping"), ("API Contract", "T1+", "api-contract")],
    "../../.cursor/agents/architect/RULE.md")

print("All documentation bundles generated.")
