---
name: calew-status
description: >-
  Report CALEW session position (/calew-status), reset session (/calew-reset),
  validate gates (/gate-check), and toggle reporting (/make-report).
---

# CALEW Status and Reporting

Session awareness and gate validation commands.

## Commands

| Command | Behavior |
|---------|----------|
| `/calew-status` | Human-readable summary from state.yaml + tier from scaling-indicators |
| `/calew-reset` | Reset state.yaml to template defaults |
| `/gate-check [gate_key]` | Walk quality-gates.yaml checklist; report pass/fail per item |
| `/make-report on\|off` | Toggle `modes.reporting` in state.yaml |

## /calew-status Output

Read [state.yaml](../../session/state.yaml) and [scaling-indicators.yaml](../../workflow/scaling-indicators.yaml). Emit:

```markdown
## CALEW Status

**Active agent:** Manager (@10-manager)
**Mode:** default
**Phase:** discovery
**Current gate:** manager_to_architect (pending)
**Tier:** T2 — Acme Platform
**Reporting:** off
**Last handoff:** none

### Pipeline position
Manager → Architect → Developer → QA → DevOps → Manager

### Suggested next step
<one sentence based on active_agent and current_gate>
```

## /calew-reset

Reset [state.yaml](../../session/state.yaml) to:

```yaml
version: "1.0.0"
updated: <now>
active_agent: null
active_mode: default
workflow_phase: discovery
current_gate: null
modes:
  reporting: false
  brainstorming: false
last_handoff: null
consultation_stack: []
```

Confirm with user before reset if work is in progress.

## /gate-check

1. Resolve gate key from argument or infer from `current_gate` in state
2. Load [quality-gates.yaml](../../workflow/quality-gates.yaml) transition entry
3. Check each required artifact path exists
4. For markdown/yaml artifacts: verify frontmatter `status: approved` when required
5. Scan for forbidden placeholders (`TODO`, `TBD`, `fill in later`) in approved docs
6. Optionally run `python scripts/gate-check.py <gate_key>` for automated validation
7. Report pass/fail table with blockers

## /make-report

Toggle `modes.reporting` in state.yaml.

When `reporting: true`, append structured progress blocks to substantive outputs per [communication-protocol.md](../../workflow/communication-protocol.md):

```markdown
### Progress (reporting mode)
- Phase: build
- Completed: API endpoint POST /orders
- In progress: unit tests
- Blockers: none
- Gate readiness: developer_to_qa — 2 items pending
```

## State Read/Write Contract

| Event | Update |
|-------|--------|
| `/hey-*` invoke | `active_agent`, `active_mode`, `workflow_phase`, `updated` |
| `/handoff-to` | `active_agent`, `current_gate`, `last_handoff`, clear `consultation_stack` |
| `/talk-to` | push to `consultation_stack` only |
| `/make-report` | `modes.reporting` |
| `/calew-reset` | all fields to defaults |

## Related

- Router: [calew-router](../calew-router/SKILL.md)
- Gate script: [gate-check.py](../../../scripts/gate-check.py)
