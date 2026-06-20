---
name: calew-handoff
description: >-
  Execute formal CALEW handoffs (/handoff-to) with quality gate validation.
  Use when work is complete and ownership must pass to the next agent.
---

# CALEW Handoff

Formal ownership transfer between agents. **Never** auto-handoff — only explicit `/handoff-to`.

## Grammar

```
/hey-{from} /handoff-to /hey-{to} [optional gate key]
```

Example:

```
/hey-developer /handoff-to /hey-qa
```

## Gate Keys

| From → To | Gate key |
|-----------|----------|
| Manager → Architect | `manager_to_architect` |
| Architect → Manager | `architect_to_manager` |
| Architect → Developer | `architect_to_developer` |
| Developer → QA | `developer_to_qa` |
| QA → Developer | `qa_to_developer` |
| QA → DevOps | `qa_to_devops` |
| DevOps → Manager | `devops_to_manager` |

## Handoff Procedure

1. Identify gate key from agent pair (or use explicit key in command)
2. Walk checklist in [handoff-procedures.md](../../workflow/handoff-procedures.md)
3. Validate thresholds in [quality-gates.yaml](../../workflow/quality-gates.yaml)
4. Run `/gate-check [gate_key]` or [gate-check.py](../../../scripts/gate-check.py) if available
5. If gate fails: report blockers; do **not** transfer ownership
6. If gate passes: update [state.yaml](../../session/state.yaml):

```yaml
active_agent: <to agent key>
active_mode: default
current_gate: <gate key>
last_handoff:
  from: <from agent key>
  to: <to agent key>
  gate: <gate key>
  timestamp: <ISO-8601>
consultation_stack: []
updated: <ISO-8601>
```

7. Emit handoff message per [communication-protocol.md](../../workflow/communication-protocol.md)

## Handoff Message Template

```markdown
## Handoff {From} → {To}

**Gate:** `{gate_key}`
**Date:** YYYY-MM-DD
**Tier:** T1 | T2 | T3

### Deliverables
- [path/to/artifact](path/to/artifact)

### Gate status
Pass | Fail (list blockers)

### Next agent
{To role} — begin {phase} work
```

## Safety

- No `qa_to_devops` without zero open P0/P1
- No production deploy without human approval ([project.yaml](../../config/project.yaml))
- Reverse handoffs (`qa_to_developer`) require bug reports with repro steps

## Related

- Consultation (no ownership change): [calew-talk-to](../calew-talk-to/SKILL.md)
- Architect dilemma tree: [architect-decision-tree.md](../../workflow/architect-decision-tree.md)
