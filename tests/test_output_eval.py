"""Unit tests for the clean-architecture rubric output eval."""

import importlib.util
import json
import unittest
from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = PACKAGE_ROOT / "scripts" / "output_eval.py"


def load_output_eval():
    spec = importlib.util.spec_from_file_location("output_eval", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


oe = load_output_eval()


def spec_json():
    return json.loads((PACKAGE_ROOT / "evals" / "output-eval.json").read_text(encoding="utf-8"))


class TestContractCoverage(unittest.TestCase):
    def test_skill_md_instructs_all_output_behaviors(self):
        spec = spec_json()
        coverage = oe.contract_coverage((PACKAGE_ROOT / "SKILL.md").read_text(encoding="utf-8"), spec)
        self.assertTrue(coverage["pass"], coverage)

    def test_missing_marker_fails_coverage(self):
        spec = spec_json()
        coverage = oe.contract_coverage("# no architecture markers present", spec)
        self.assertFalse(coverage["pass"])
        self.assertEqual(len(coverage["dimensions"]), 5)


class TestScenarioScoring(unittest.TestCase):
    def test_all_authored_scenarios_pass(self):
        spec = spec_json()
        self.assertGreaterEqual(len(spec["scenarios"]), 3)
        for scenario in spec["scenarios"]:
            result = oe.score_scenario(scenario, spec["contract"])
            self.assertTrue(result["pass"], f"{scenario['id']}: {result}")

    def test_answer_missing_terms_fails(self):
        spec = spec_json()
        bad = {
            "id": "empty",
            "title": "empty",
            "dimensions": ["four_layer_terms", "code_example"],
            "reference_answer": "这是无关回答，不含任何架构内容",
        }
        result = oe.score_scenario(bad, spec["contract"])
        self.assertFalse(result["pass"])
        self.assertTrue(all(not dim["pass"] for dim in result["dimensions"]))


class TestEvaluate(unittest.TestCase):
    def test_full_eval_ok_and_evidence_kind(self):
        result = oe.evaluate(PACKAGE_ROOT, PACKAGE_ROOT / "evals" / "output-eval.json")
        self.assertTrue(result["ok"], result)
        self.assertEqual(result["evidence_kind"], "behavior_specification")
        self.assertEqual(result["summary"]["scenario_total"], len(spec_json()["scenarios"]))
        self.assertEqual(result["summary"]["scenario_passed"], result["summary"]["scenario_total"])


if __name__ == "__main__":
    unittest.main()
