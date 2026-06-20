# Documentation Catalog

Master index of all blueprint documentation bundles. Each bundle contains `template.md`, `example.md`, and `guide.md` (API contract uses `example.yaml`).

**Blueprint version:** 1.1.0

**Diagram guide:** [DIAGRAMS.md](DIAGRAMS.md) — priority matrix (Critical / Recommended / Optional / Skip by tier)

---

## Legend

| Tier | Required when |
|------|---------------|
| T1 | Small projects (1–3 devs) |
| T2 | Medium projects (4–10 devs) |
| T3 | Enterprise / regulated |

Status in examples is `approved` for reference; new projects start from `template.md` as `draft`.

---

## Architecture

| Document | Path | Tier | Owner |
|----------|------|------|-------|
| System Context (C4 L1) | [architecture/system-context/](architecture/system-context/) | T1+ | Architect |
| Container (C4 L2) | [architecture/container/](architecture/container/) | T1+ | Architect |
| Component (C4 L3) | [architecture/component/](architecture/component/) | T2+ | Architect |
| Deployment | [architecture/deployment/](architecture/deployment/) | T1+ | DevOps |
| Network | [architecture/network/](architecture/network/) | T2+ | DevOps |
| Security | [architecture/security/](architecture/security/) | T2+ | Architect |

Category index: [architecture/README.md](architecture/README.md)

---

## Process

| Document | Path | Tier | Owner |
|----------|------|------|-------|
| Workflow Sequence | [process/workflow-sequence/](process/workflow-sequence/) | T1+ | Architect |
| Entity State Diagram | [process/entity-state/](process/entity-state/) | T1+ | Architect |
| Activity Diagram | [process/activity-diagram/](process/activity-diagram/) | T2+ | Architect |
| Project Timeline | [process/project-timeline/](process/project-timeline/) | T1+ | Manager |
| Release Process | [process/release-process/](process/release-process/) | T2+ | DevOps |
| Incident Response | [process/incident-response/](process/incident-response/) | T2+ | DevOps |
| Change Management | [process/change-management/](process/change-management/) | T2+ | Manager |
| Code Review | [process/code-review/](process/code-review/) | T1+ | Developer |

Category index: [process/README.md](process/README.md)

---

## Data

| Document | Path | Tier | Owner |
|----------|------|------|-------|
| Entity Relationship | [data/entity-relationship/](data/entity-relationship/) | T1+ | Architect |
| Class Diagram | [data/class-diagram/](data/class-diagram/) | T2+ | Architect |
| Data Flow (DFD) | [data/data-flow/](data/data-flow/) | T2+ | Architect |
| Data Lifecycle | [data/data-lifecycle/](data/data-lifecycle/) | T3 | Architect |
| Data Mapping | [data/data-mapping/](data/data-mapping/) | T3 | Developer |
| API Contract (OpenAPI) | [data/api-contract/](data/api-contract/) | T1+ | Architect |

Category index: [data/README.md](data/README.md)

---

## User Experience

| Document | Path | Tier | Owner |
|----------|------|------|-------|
| User Journey | [ux/user-journey/](ux/user-journey/) | T2+ | Manager |
| Wireframes | [ux/wireframes/](ux/wireframes/) | T1+ | Developer |
| Design System | [ux/design-system/](ux/design-system/) | T2+ | Developer |
| Accessibility | [ux/accessibility/](ux/accessibility/) | T2+ | QA |
| Usability Testing | [ux/usability-testing/](ux/usability-testing/) | T2+ | QA |

Category index: [ux/README.md](ux/README.md)

---

## Project Management

| Document | Path | Tier | Owner |
|----------|------|------|-------|
| Project Charter | [project-management/project-charter/](project-management/project-charter/) | T1+ | Manager |
| Work Breakdown Structure | [project-management/work-breakdown/](project-management/work-breakdown/) | T1+ | Manager |
| Glossary | [project-management/glossary/](project-management/glossary/) | T1+ | Manager |
| Risk Assessment | [project-management/risk-assessment/](project-management/risk-assessment/) | T1+ | Manager |
| Stakeholder Map | [project-management/stakeholder-map/](project-management/stakeholder-map/) | T2+ | Manager |
| Sprint Planning | [project-management/sprint-planning/](project-management/sprint-planning/) | T1+ | Manager |

Category index: [project-management/README.md](project-management/README.md)

---

## Standards and Relationships

| Document | Path |
|----------|------|
| Diagram catalog and priorities | [DIAGRAMS.md](DIAGRAMS.md) |
| Writing standard | [STANDARD.md](STANDARD.md) |
| Dependency graph | [RELATIONSHIPS.md](RELATIONSHIPS.md) |

---

## Agent Cross-References

| Agent | Primary doc categories |
|-------|------------------------|
| Manager | project-management, process/project-timeline, [DIAGRAMS.md](DIAGRAMS.md) |
| Architect | architecture, data, process (sequence, entity-state, activity) |
| Developer | data/api-contract, ux/design-system, process/code-review |
| QA | ux/accessibility, ux/usability-testing, data/api-contract |
| DevOps | architecture/deployment, process/release-process |

Agent rules: [../.cursor/INDEX.md](../.cursor/INDEX.md)
