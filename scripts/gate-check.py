#!/usr/bin/env python3
"""Validate quality gate readiness for CALEW handoffs.

Checks required artifact paths, frontmatter status, and forbidden placeholders
in approved documents per .cursor/workflow/quality-gates.yaml.

Usage:
  python scripts/gate-check.py manager_to_architect
  python scripts/gate-check.py --tier T2 architect_to_developer
  python scripts/gate-check.py --all
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required. Install with: pip install pyyaml", file=sys.stderr)
    sys.exit(2)

ROOT = Path(__file__).resolve().parent.parent
GATES_FILE = ROOT / ".cursor" / "workflow" / "quality-gates.yaml"
SCALING_FILE = ROOT / ".cursor" / "workflow" / "scaling-indicators.yaml"

FORBIDDEN = ("TODO", "TBD", "fill in later", "PLACEHOLDER")
FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---", re.DOTALL)


def load_yaml(path: Path) -> dict:
    with path.open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def parse_frontmatter(path: Path) -> dict | None:
    if not path.is_file():
        return None
    text = path.read_text(encoding="utf-8")
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None
    return yaml.safe_load(m.group(1)) or {}


def find_artifact_file(bundle_dir: Path) -> Path | None:
    """Prefer example.md/yaml in bundle; fall back to any md/yaml."""
    if not bundle_dir.is_dir():
        return None
    for name in ("example.md", "example.yaml", "example.yml", "template.md"):
        p = bundle_dir / name
        if p.is_file():
            return p
    for ext in ("*.md", "*.yaml", "*.yml"):
        matches = sorted(bundle_dir.glob(ext))
        if matches:
            return matches[0]
    return None


def tier_artifacts(transition: dict, tier: str) -> list[str]:
    paths: list[str] = []
    req = transition.get("required_artifacts") or {}
    if isinstance(req, dict):
        paths.extend(req.get("all_tiers") or [])
        if tier in ("T2", "T3"):
            paths.extend(req.get("T2_plus") or [])
        if tier == "T3":
            paths.extend(req.get("T3_only") or [])
    elif isinstance(req, list):
        paths.extend(req)
    return paths


def check_bundle(path_str: str, require_approved: bool) -> tuple[bool, str]:
    bundle = ROOT / path_str.rstrip("/")
    if not bundle.is_dir():
        return False, f"MISSING dir: {path_str}"

    artifact = find_artifact_file(bundle)
    if artifact is None:
        return False, f"MISSING artifact in: {path_str}"

    rel = artifact.relative_to(ROOT)
    if not require_approved:
        return True, f"OK: {rel}"

    fm = parse_frontmatter(artifact)
    if fm is None:
        return False, f"NO frontmatter: {rel}"

    status = str(fm.get("status", "")).lower()
    if status != "approved":
        return False, f"status={status!r} (need approved): {rel}"

    body = artifact.read_text(encoding="utf-8")
    if FRONTMATTER_RE.match(body):
        body = body[FRONTMATTER_RE.match(body).end() :]
    for pat in FORBIDDEN:
        if pat in body:
            return False, f"forbidden {pat!r} in approved doc: {rel}"

    return True, f"OK approved: {rel}"


def check_gate(gate_key: str, tier: str, gates: dict) -> tuple[bool, list[str]]:
    transitions = gates.get("transitions") or {}
    if gate_key not in transitions:
        return False, [f"Unknown gate: {gate_key}"]

    transition = transitions[gate_key]
    lines: list[str] = []
    all_ok = True

    desc = transition.get("description", gate_key)
    lines.append(f"Gate: {gate_key} — {desc}")
    lines.append(f"Tier: {tier}")
    lines.append("")

    paths = tier_artifacts(transition, tier)
    doc_status_required = (
        gates.get("defaults") or {}
    ).get("doc_status_required", "approved")
    require_approved = doc_status_required == "approved"

    if paths:
        lines.append("Required artifacts:")
        for p in paths:
            ok, msg = check_bundle(p, require_approved)
            symbol = "PASS" if ok else "FAIL"
            lines.append(f"  [{symbol}] {msg}")
            if not ok:
                all_ok = False
    else:
        lines.append("(No required_artifacts paths for this gate)")

    validations = transition.get("validations") or []
    if validations:
        lines.append("")
        lines.append("Manual validations (not auto-checked):")
        for v in validations:
            lines.append(f"  [MANUAL] {v}")

    success = transition.get("success_criteria") or []
    if success:
        lines.append("")
        lines.append("Success criteria (confirm at handoff):")
        for s in success:
            lines.append(f"  [MANUAL] {s}")

    lines.append("")
    lines.append("RESULT: PASS" if all_ok else "RESULT: FAIL")
    return all_ok, lines


def default_tier() -> str:
    gates = load_yaml(GATES_FILE)
    return (gates.get("defaults") or {}).get("tier", "T2")


def main() -> int:
    parser = argparse.ArgumentParser(description="CALEW quality gate checker")
    parser.add_argument("gate", nargs="?", help="Gate key e.g. manager_to_architect")
    parser.add_argument("--tier", default=None, choices=["T1", "T2", "T3"])
    parser.add_argument("--all", action="store_true", help="Check all defined gates")
    args = parser.parse_args()

    if not GATES_FILE.is_file():
        print(f"ERROR: {GATES_FILE} not found", file=sys.stderr)
        return 2

    gates = load_yaml(GATES_FILE)
    tier = args.tier or default_tier()

    if args.all:
        keys = list((gates.get("transitions") or {}).keys())
        overall = True
        for key in keys:
            ok, lines = check_gate(key, tier, gates)
            print("\n".join(lines))
            print("-" * 60)
            overall = overall and ok
        return 0 if overall else 1

    if not args.gate:
        parser.print_help()
        return 2

    ok, lines = check_gate(args.gate, tier, gates)
    print("\n".join(lines))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
