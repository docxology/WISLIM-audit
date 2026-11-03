"""Tests for the WISLIM-audit repository.

The tests use only the Python standard library and run under either:

    python3 -m unittest discover -s tests -v
    python3 -m pytest -q
"""

from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = ROOT / "tools" / "validate.py"
REGISTER_PATH = ROOT / "scripts" / "build_issue_register.py"


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_validator():
    return load_module("wislim_validate", VALIDATOR_PATH)


class RepositoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_validator()

    def test_repository_validates(self):
        self.assertEqual(self.module.main(["--quiet"]), 0)

    def test_source_is_immutable(self):
        metadata = self.module.load_json(self.module.METADATA)
        self.assertEqual(
            self.module.sha256(self.module.SOURCE_PDF), metadata["pdf_sha256"]
        )
        self.assertEqual(
            self.module.sha256(self.module.SOURCE_TXT), metadata["text_sha256"]
        )

    def test_claim_ids_are_stable(self):
        data = self.module.load_json(self.module.CLAIMS)
        self.assertEqual(
            [claim["id"] for claim in data["claims"]], self.module.CLAIM_IDS
        )

    def test_stress_catalog_is_complete(self):
        data = self.module.load_json(self.module.STRESS)
        self.assertEqual(
            [test["id"] for test in data["tests"]], self.module.STRESS_IDS
        )
        self.assertEqual(len(data["tests"]), 210)


class IssueRegisterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.register = load_module("wislim_register", REGISTER_PATH)
        cls.issues = cls.register.load_issues()

    def test_issue_ids_are_stable(self):
        self.assertEqual(
            [issue["id"] for issue in self.issues],
            [f"WISLIM-{index:03d}" for index in range(1, 67)],
        )

    def test_issue_coverage_is_complete(self):
        source_ids = {issue["source_id"] for issue in self.issues}
        self.assertEqual(
            source_ids,
            {f"AS{index:02d}" for index in range(1, 21)}
            | {f"WS{index:02d}" for index in range(1, 12)}
            | {f"C{index:02d}" for index in range(1, 36)},
        )

    def test_manifest_has_no_errors(self):
        self.assertEqual(self.register.check_manifest(self.issues), [])

    def test_every_issue_has_a_record(self):
        for issue in self.issues:
            path = ROOT / issue["file"]
            with self.subTest(issue=issue["id"]):
                self.assertTrue(path.is_file(), f"missing {issue['file']}")

    def test_records_have_required_sections(self):
        for issue in self.issues:
            text = (ROOT / issue["file"]).read_text(encoding="utf-8")
            for heading in (
                "## Quoted passage",
                "## Summary",
                "## Evidence",
                "## Why it matters",
                "## Required repair",
                "## Acceptance criteria",
                "## Related issues",
                "## Tracking",
            ):
                with self.subTest(issue=issue["id"], heading=heading):
                    self.assertIn(heading, text)
            if issue["kind"] == "claim":
                with self.subTest(issue=issue["id"], heading="steelman"):
                    self.assertIn("## Steelman and reply", text)

    def test_issue_map_is_complete(self):
        mapping = self.register.load_map()
        self.assertEqual(len(mapping), 66)
        numbers = [entry["number"] for entry in mapping.values()]
        self.assertEqual(len(set(numbers)), 66)
        for issue in self.issues:
            entry = mapping[issue["id"]]
            self.assertTrue(entry["url"].endswith(f"/issues/{entry['number']}"))
            record = (ROOT / issue["file"]).read_text(encoding="utf-8")
            self.assertIn(f"github_issue: {entry['number']}", record)
            self.assertIn(f"issues/{entry['number']}", record)

    def test_titles_are_unique(self):
        titles = [issue["title"] for issue in self.issues]
        self.assertEqual(len(set(titles)), len(titles))

    def test_red_team_fields_are_specific(self):
        for issue in self.issues:
            if issue["kind"] != "red-team":
                continue
            with self.subTest(issue=issue["id"]):
                self.assertNotIn("The scenario tests whether", issue["summary"])
                self.assertGreater(len(issue["summary"]), 120)


if __name__ == "__main__":
    unittest.main()
