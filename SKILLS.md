# CALEW Commands — Quick Reference

**CALEW** (Command And Language for Engineering Workflows) is the orchestration layer on top of this blueprint. Use these commands in Cursor chat. They are conventions — Cursor does not register slash commands natively. `/hey-manager` behaves the same as `@10-manager`.

**Blueprint version:** 1.2.0  
**Full architecture:** [CALEW_ARCHITECTURE.md](CALEW_ARCHITECTURE.md)  
**Lifecycle guide:** [HELP.md](HELP.md)

---

## Lost?

```
/hey-manager
```

Manager triages and recommends the next agent.

---

## Invoke an Agent

| Command | Same as | Role |
|---------|---------|------|
| `/hey-manager` | `@10-manager` | Planning, routing, risks |
| `/hey-architect` | `@20-architect` | Design, diagrams, ADRs |
| `/hey-developer` | `@30-developer` | Implementation, bug fixes |
| `/hey-qa` | `@40-qa` | Write + run tests |
| `/hey-tester` | `@40-qa` (execute only) | Run existing tests only |
| `/hey-devops` | `@50-devops` | Build, deploy, infra |

---

## Three Golden Rules

### 1. Invoke — take ownership

```
/hey-developer /implement REQ-20
```

Developer builds the feature.

### 2. Consult — ask for advice (no ownership change)

```
/hey-developer /talk-to /hey-architect
Should I use REST or GraphQL for this?
```

Architect gives an opinion; Developer stays in charge.

### 3. Transfer — pass ownership (gate required)

```
/hey-developer /handoff-to /hey-qa
```

Only after quality checks pass. No skipping gates.

---

## Common Scenarios

| What you want | What to type |
|---------------|--------------|
| Start a project | `/hey-manager` |
| Design database | `/hey-architect /create-architecture` |
| Write code | `/hey-developer /implement REQ-xxx` |
| Write + run tests | `/hey-qa /write-tests /run-tests` |
| Just run tests | `/hey-tester /run-tests` |
| Deploy staging | `/hey-devops /set-mode on /deploy staging` |
| Ask another agent | `/hey-A /talk-to /hey-B <question>` |
| Pass work officially | `/handoff-to /hey-next` |
| Generate report | `/make-report on` |
| Check progress | `/calew-status` |
| Validate gate | `/gate-check architect_to_developer` |
| Reset session | `/calew-reset` |

---

## Agent Skills

### Manager

| Skill | Purpose |
|-------|---------|
| `/plan-sprint` | Sprint goal, stories, capacity |
| `/scope-change` | Scope change impact |
| `/resolve-dilemma` | Escalated conflicts |
| `/status-report` | Stakeholder update |

### Architect

| Skill | Purpose |
|-------|---------|
| `/create-architecture` | New feature or greenfield design |
| `/refactor-architecture` | Change existing design |
| `/pick-diagram` | Choose diagram type |
| `/write-adr` | Record decision |
| `/escalate-to-manager` | Blocking trade-off |

### Developer

| Skill | Purpose |
|-------|---------|
| `/set-position backend\|frontend\|fullstack` | Focus area |
| `/implement REQ-xxx` | Build from architecture |
| `/fix-bug BUG-xxx` | Fix QA failure |
| `/prepare-pr` | Pre-QA checklist |

### QA / Tester

| Skill | Purpose |
|-------|---------|
| `/test-plan` | Test strategy |
| `/write-tests` | Write suites |
| `/run-tests` | Execute tests |
| `/regression` | Regression suite |
| `/return-to-developer` | Fail path |
| `/approve-release` | Gate to DevOps |

### DevOps

| Skill | Purpose |
|-------|---------|
| `/set-mode on\|off` | Deployment readiness |
| `/build-project` | CI/local build |
| `/deploy staging\|prod` | Deploy (prod needs approval) |
| `/smoke-test` | Post-deploy check |
| `/rollback` | Incident response |

---

## Pipeline

```
Manager → Architect → Developer → QA → DevOps → Manager
         ↗ dilemma    ↖ fail
```

---

## When CALEW Asks Questions

1. **Dilemma** — trade-off needs a stakeholder choice
2. **Unclear** — ambiguous requirement
3. **Risk** — deadline or scope slip
4. **First time** — unfamiliar technology
5. **Budget** — cost implications

---

## What CALEW Handles Automatically (v1)

- Task sequencing and gate checklists
- Code generation per architecture
- Test writing (with QA)
- Documentation from templates
- Deployment script scaffolding
- Progress tracking when `/make-report on`

---

## Safety Rules

- No auto-handoff — only `/handoff-to`
- No skipping gates — QA must approve before DevOps
- No production deploy without human approval
- No guessing on ambiguous requirements — ask first
- When unsure: `/hey-manager`

---

## Gate Check Script

```bash
python scripts/gate-check.py manager_to_architect
python scripts/gate-check.py --tier T2 architect_to_developer
```

---

## Not in v1 (Future)

- Learning from past projects (`learning-db.yaml`)
- Auto-pilot mode (fully autonomous)
- Risk prediction with ML
- Resource optimization
- Cross-project memory

See [CALEW_ARCHITECTURE.md](CALEW_ARCHITECTURE.md) for v1 boundaries.
