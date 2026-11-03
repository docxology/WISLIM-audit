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


def load_validator():
    spec = importlib.util.spec_from_file_location("wislim_validate", VALIDATOR_PATH)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


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


if __name__ == "__main__":
    unittest.main()
