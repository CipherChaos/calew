# Cursor Agent Workflow Index

Navigable map of agent rules, playbooks, CALEW skills, and workflow artifacts.

**Blueprint version:** 1.2.0

---

## CALEW Orchestration (v1)

| Resource | Path | Purpose |
|----------|------|---------|
| Command cheat sheet | [SKILLS.md](../SKILLS.md) | Human quick reference |
| Architecture | [CALEW_ARCHITECTURE.md](../CALEW_ARCHITECTURE.md) | System design and v1 boundaries |
| Router skill | [skills/calew-router/SKILL.md](skills/calew-router/SKILL.md) | Command alias resolution |
| Talk-to skill | [skills/calew-talk-to/SKILL.md](skills/calew-talk-to/SKILL.md) | Consultation without ownership change |
| Handoff skill | [skills/calew-handoff/SKILL.md](skills/calew-handoff/SKILL.md) | Formal gate-validated transfer |
| Status skill | [skills/calew-status/SKILL.md](skills/calew-status/SKILL.md) | `/calew-status`, `/gate-check`, reporting |
| Session state | [session/state.yaml](session/state.yaml) | Active agent, phase, gates |
| Project config | [config/project.yaml](config/project.yaml) | Team overrides |
| Gate checker | [../scripts/gate-check.py](../scripts/gate-check.py) | Artifact validation script |

---

## Rules (Executable)

| File | CALEW alias | Always apply | Invoke when |
|------|-------------|--------------|-------------|
| [rules/00-cross-agent.mdc](rules/00-cross-agent.mdc) | — | Yes | Every session |
| [rules/10-manager.mdc](rules/10-manager.mdc) | `/hey-manager` | No | Planning, sprints, stakeholders, risks |
| [rules/20-architect.mdc](rules/20-architect.mdc) | `/hey-architect` | No | Design, stack, architecture docs |
| [rules/30-developer.mdc](rules/30-developer.mdc) | `/hey-developer` | No | Coding, review, refactor |
| [rules/40-qa.mdc](rules/40-qa.mdc) | `/hey-qa`, `/hey-tester` | No | Testing, bugs, UAT |
| [rules/50-devops.mdc](rules/50-devops.mdc) | `/hey-devops` | No | CI/CD, infra, deploy |

---

## Playbooks (Comprehensive)

| Role | Playbook | Tags |
|------|----------|------|
| Manager | [agents/manager/RULE.md](agents/manager/RULE.md) | pm, sprint, risk, stakeholder |
| Architect | [agents/architect/RULE.md](agents/architect/RULE.md) | architecture, security, api, db |
| Developer | [agents/developer/RULE.md](agents/developer/RULE.md) | code, git, test, docs |
| QA | [agents/qa/RULE.md](agents/qa/RULE.md) | qa, regression, uat, security-test |
| DevOps | [agents/devops/RULE.md](agents/devops/RULE.md) | cicd, k8s, iac, monitoring |

Agent overview: [agents/README.md](agents/README.md)

---

## Workflow Artifacts

| File | Type | Purpose |
|------|------|---------|
| [workflow/consultation-protocol.md](workflow/consultation-protocol.md) | Process | `/talk-to` rules |
| [workflow/communication-protocol.md](workflow/communication-protocol.md) | Process | Message formats, async norms |
| [workflow/handoff-procedures.md](workflow/handoff-procedures.md) | Process | Agent transition checklists |
| [workflow/escalation-matrix.md](workflow/escalation-matrix.md) | Process | Severity and escalation paths |
| [workflow/knowledge-transfer.md](workflow/knowledge-transfer.md) | Process | KT sessions, onboarding |
| [workflow/quality-gates.yaml](workflow/quality-gates.yaml) | Config | Pass/fail thresholds per transition |
| [workflow/architect-decision-tree.md](workflow/architect-decision-tree.md) | Process | Architect dilemma escalation vs proceed |
| [workflow/scaling-indicators.yaml](workflow/scaling-indicators.yaml) | Config | Tier detection and doc requirements |

---

## Handoff Gates

| Transition | Gate key |
|------------|----------|
| Manager → Architect | `manager_to_architect` |
| Architect → Manager | `architect_to_manager` |
| Architect → Developer | `architect_to_developer` |
| Developer → QA | `developer_to_qa` |
| QA → Developer | `qa_to_developer` |
| QA → DevOps | `qa_to_devops` |
| DevOps → Manager | `devops_to_manager` |

Validate: `/gate-check [gate_key]` or `python scripts/gate-check.py [gate_key]`

---

## Phase → Agent Map

| Phase | Primary agent | Key docs |
|-------|---------------|----------|
| Discovery & charter | Manager | [project-charter](../../docs/project-management/project-charter/) |
| Architecture | Architect | [architecture/](../../docs/architecture/) |
| Implementation | Developer | [api-contract](../../docs/data/api-contract/), [design-system](../../docs/ux/design-system/) |
| Verification | QA | [test strategy in qa/RULE.md](agents/qa/RULE.md) |
| Release | DevOps | [deployment](../../docs/architecture/deployment/) |

---

## Related

- [HELP.md](../HELP.md) — Agent diagrams and onboarding
- [SKILLS.md](../SKILLS.md) — CALEW command reference
- [BOOTSTRAP.md](../BOOTSTRAP.md) — AI project setup
- [docs/INDEX.md](../docs/INDEX.md) — Documentation catalog
- [docs/RELATIONSHIPS.md](../docs/RELATIONSHIPS.md) — Doc dependency graph
- [README.md](../README.md) — Repository quick start
