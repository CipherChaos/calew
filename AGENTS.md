# Agents

This project uses five Cursor agents for agentic/loop engineering. **CALEW** adds command aliases (`/hey-*`) equivalent to `@` rule invocation.

**Start here:** [HELP.md](HELP.md) — role diagrams, lifecycle, and how to invoke each agent.  
**Commands:** [SKILLS.md](SKILLS.md) — CALEW cheat sheet.

## Quick Reference

| Agent | Rule | CALEW | Playbook |
|-------|------|-------|----------|
| Manager | [`.cursor/rules/10-manager.mdc`](.cursor/rules/10-manager.mdc) | `/hey-manager` | [`.cursor/agents/manager/RULE.md`](.cursor/agents/manager/RULE.md) |
| Architect | [`.cursor/rules/20-architect.mdc`](.cursor/rules/20-architect.mdc) | `/hey-architect` | [`.cursor/agents/architect/RULE.md`](.cursor/agents/architect/RULE.md) |
| Developer | [`.cursor/rules/30-developer.mdc`](.cursor/rules/30-developer.mdc) | `/hey-developer` | [`.cursor/agents/developer/RULE.md`](.cursor/agents/developer/RULE.md) |
| QA | [`.cursor/rules/40-qa.mdc`](.cursor/rules/40-qa.mdc) | `/hey-qa` | [`.cursor/agents/qa/RULE.md`](.cursor/agents/qa/RULE.md) |
| Tester (alias) | [`.cursor/rules/40-qa.mdc`](.cursor/rules/40-qa.mdc) | `/hey-tester` | execute-only mode on QA rule |
| DevOps | [`.cursor/rules/50-devops.mdc`](.cursor/rules/50-devops.mdc) | `/hey-devops` | [`.cursor/agents/devops/RULE.md`](.cursor/agents/devops/RULE.md) |

Cross-agent rules: [`.cursor/rules/00-cross-agent.mdc`](.cursor/rules/00-cross-agent.mdc) (always applied)

## CALEW Interaction Types

| Type | Command | Meaning |
|------|---------|---------|
| Invoke | `/hey-{agent}` | Adopt persona, take ownership |
| Consult | `/talk-to` | Ask opinion; owner keeps work |
| Transfer | `/handoff-to` | Pass ownership after gate pass |

Session: [`.cursor/session/state.yaml`](.cursor/session/state.yaml) — check with `/calew-status`.

## Workflow

```
Manager → Architect → Developer → QA → DevOps → Manager
         ↗ dilemma    ↖ fail
```

Bootstrap a new project: [BOOTSTRAP.md](BOOTSTRAP.md)
