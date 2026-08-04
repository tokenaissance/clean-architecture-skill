#!/usr/bin/env python3
"""Run a lightweight rubric output eval for a fastagent skill package.

Two checks:
(a) contract coverage: does SKILL.md instruct the five output-contract behaviors?
(b) scenario scoring: do the authored reference answers satisfy their rubric dimensions?

Writes reports/output-eval.json with evidence_kind "behavior_specification".
This is a behavioral spec: it pins down what a compliant answer must contain,
not a provider-run measurement. Release tooling will truthfully label it as
non-provider/human evidence.
"""

from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path
from typing import Any

DEFAULT_CONTRACT = "evals/output-eval.json"


def load_json(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"{path}: expected JSON object")
    return payload


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def check_terms(text: str, terms: list[str]) -> tuple[list[str], list[str]]:
    found = [term for term in terms if term in text]
    missing = [term for term in terms if term not in text]
    return found, missing


def contract_coverage(skill_md: str, spec: dict[str, Any]) -> dict[str, Any]:
    contract = spec.get("contract", {})
    dimensions = []
    for dim, rule in contract.items():
        terms = list(rule.get("coverage_terms") or rule.get("required_terms", []))
        found, missing = check_terms(skill_md, terms)
        dimensions.append(
            {
                "dimension": dim,
                "label": rule.get("label", dim),
                "pass": not missing,
                "matched_terms": found,
                "missing_terms": missing,
            }
        )
    return {"pass": all(d["pass"] for d in dimensions), "dimensions": dimensions}


def score_scenario(scenario: dict[str, Any], contract: dict[str, Any]) -> dict[str, Any]:
    dims = list(scenario.get("dimensions", []))
    answer = str(scenario.get("reference_answer", ""))
    results = []
    for dim in dims:
        rule = contract.get(dim, {})
        terms = list(rule.get("required_terms", []))
        found, missing = check_terms(answer, terms)
        results.append(
            {
                "dimension": dim,
                "label": rule.get("label", dim),
                "pass": not missing,
                "matched_terms": found,
                "missing_terms": missing,
            }
        )
    return {
        "id": scenario.get("id", ""),
        "title": scenario.get("title", ""),
        "pass": all(r["pass"] for r in results),
        "dimensions": results,
    }


def evaluate(root: Path, spec_path: Path) -> dict[str, Any]:
    spec = load_json(spec_path)
    skill_md = read_text(root / "SKILL.md")
    coverage = contract_coverage(skill_md, spec)
    scenarios = [score_scenario(scenario, spec.get("contract", {})) for scenario in spec.get("scenarios", [])]
    ok = coverage["pass"] and all(scenario["pass"] for scenario in scenarios)
    return {
        "ok": ok,
        "evidence_kind": spec.get("evidence_kind", "behavior_specification"),
        "generated_at": date.today().isoformat(),
        "contract_coverage": coverage,
        "scenarios": scenarios,
        "summary": {
            "scenario_total": len(scenarios),
            "scenario_passed": sum(1 for scenario in scenarios if scenario["pass"]),
            "dimension_total": sum(len(scenario["dimensions"]) for scenario in scenarios),
            "dimension_passed": sum(1 for scenario in scenarios for dim in scenario["dimensions"] if dim["pass"]),
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Run a rubric output eval for a fastagent skill.")
    parser.add_argument("skill_dir", nargs="?", default=".", help="Skill directory.")
    parser.add_argument("--cases", default=DEFAULT_CONTRACT, help="Rubric scenario JSON path.")
    parser.add_argument("--output", "-o", help="Write JSON report to this path.")
    args = parser.parse_args()

    root = Path(args.skill_dir).resolve()
    cases_path = Path(args.cases)
    if not cases_path.is_absolute():
        cases_path = root / cases_path
    result = evaluate(root, cases_path)
    rendered = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        output = Path(args.output)
        if not output.is_absolute():
            output = root / output
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)
    if not result["ok"]:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
