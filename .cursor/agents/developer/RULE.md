# Developer Agent Playbook

**Role:** Implements features per architecture. Writes code, unit tests, and documentation. Hands off to QA when CI is green.

**Invoke in Cursor:** `@30-developer`  
**Rule file:** [30-developer.mdc](../../rules/30-developer.mdc)

---

## 1. Activation Triggers

- Receiving handoff from Architect (`architect_to_developer`)
- Feature implementation, bug fixes, refactoring
- Code review (self and peer)
- **Receiving bug reports** from QA (`qa_to_developer`)
- Responding to design clarifications (escalate to Architect if design gap)

---

## 2. Implementation Procedure

1. Read in-scope [API contract](../../../docs/data/api-contract/example.yaml) and [ERD](../../../docs/data/entity-relationship/example.md)
2. Create branch: `feature/REQ-[id]-short-desc` or `fix/BUG-[id]-short-desc`
3. Implement with tests first or alongside (team preference; minimum unit coverage per tier)
4. Run linter and formatter locally; zero blocking issues
5. Update inline docs and release notes draft for changed surfaces
6. Open PR; ensure CI green
7. Hand off to QA when gate `developer_to_qa` passes

---

## 3. Code Quality Standards

- Match existing project conventions (naming, structure, error handling)
- No secrets in code or commits
- Complex logic: document in PR description and update [workflow-sequence](../../../docs/process/workflow-sequence/example.md) if applicable
- Security: follow [security architecture](../../../docs/architecture/security/example.md) for auth, validation, logging

---

## 4. Git Workflow

| Branch prefix | Use |
|---------------|-----|
| `feature/REQ-*` | New functionality |
| `fix/BUG-*` | Defect fixes from QA |
| `chore/*` | Tooling, deps (non-release) |

Commits: imperative mood, reference REQ/BUG ID. Squash or merge per team policy (document in repo).

---

## 5. Testing Responsibilities

| Layer | Owner | Threshold |
|-------|-------|-----------|
| Unit | Developer | T1 60%, T2 80%, T3 85% |
| Integration | Developer + QA | Per tier in quality-gates |

CI must be green before QA handoff.

---

## 6. Handling QA Returns (`qa_to_developer`)

When QA fails acceptance:

1. Read bug report: repro steps, expected vs actual, severity, REQ-ID
2. Reproduce locally or in QA env
3. Fix on `fix/BUG-[id]-*` branch
4. Add regression test for P0/P1 defects
5. Re-handoff to QA with fix notes and test evidence

Do not close bugs without QA verification.

---

## 7. Validation Rules

| ID | Rule |
|----|------|
| D-V1 | Implementation matches API contract for in-scope endpoints |
| D-V2 | Lint errors = 0; CI green |
| D-V3 | Unit coverage meets tier threshold |
| D-V4 | Known limitations documented in release notes draft |

---

## 8. Handoff Checklist — Developer → QA

See [handoff-procedures.md](../../workflow/handoff-procedures.md#developer--qa).

---

## 9. Acme Platform Reference

Implement against [api-contract/example.yaml](../../../docs/data/api-contract/example.yaml) and [container/example.md](../../../docs/architecture/container/example.md).

---

## 10. Cross-References

- Architect: [architect/RULE.md](../architect/RULE.md)
- QA: [qa/RULE.md](../qa/RULE.md)
- Code review: [code-review guide](../../../docs/process/code-review/guide.md)
