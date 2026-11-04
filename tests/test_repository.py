"""Tests for the WISLIM-audit repository.

The tests use only the Python standard library and run under either:

    python3 -m unittest discover -s tests -v
    python3 -m pytest -q
"""

from __future__ import annotations

import contextlib
import importlib.util
import io
import json
import os
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = ROOT / "tools" / "validate.py"
REGISTER_PATH = ROOT / "scripts" / "build_issue_register.py"
REVIEW_REGISTER_PATH = ROOT / "scripts" / "build_review_register.py"
REPLY_REGISTER_PATH = ROOT / "scripts" / "build_reply_register.py"
QUOTE_CHECK_PATH = ROOT / "scripts" / "verify_oph_quotes.py"


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
                "## Publication reference",
                "## Primary quotations",
                "## Summary",
                "## Evidence",
                "## Why it matters",
                "## Proposed remediation",
                "## Suggested checks for reviewers",
                "## Related issues",
                "## Tracking",
            ):
                with self.subTest(issue=issue["id"], heading=heading):
                    self.assertIn(heading, text)
            if issue["kind"] == "claim":
                with self.subTest(issue=issue["id"], heading="steelman"):
                    self.assertIn("## Steelman and reply", text)

    def test_every_issue_has_primary_quotations(self):
        metadata = self.register.load_metadata()
        for issue in self.issues:
            text = (ROOT / issue["file"]).read_text(encoding="utf-8")
            with self.subTest(issue=issue["id"]):
                self.assertGreaterEqual(len(issue["quotes"]), 1)
                self.assertIn(metadata["work"], text)
                self.assertIn(metadata["philpapers"]["doi"], text)
                for quote in issue["quotes"]:
                    self.assertIn(
                        f"source/WISLIM-v2.0.1.txt:{quote['line']}", text
                    )

    def test_issues_are_optional_observations(self):
        for issue in self.issues:
            text = (ROOT / issue["file"]).read_text(encoding="utf-8")
            with self.subTest(issue=issue["id"]):
                self.assertEqual(issue["status"], "observation")
                self.assertIn("**Status:** observation", text)
                self.assertIn("status: observation", text)
                self.assertIn("audit observation, not a required fix", text)
                self.assertIn("does not mean the overall work fails", text)
                self.assertNotIn("The manuscript resolves the defect", text)
        index = (ROOT / "docs" / "audit" / "README.md").read_text(encoding="utf-8")
        self.assertIn("not a fatality rating", index)
        self.assertIn("read them as suggestions, not instructions", index)

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


class ReviewRegisterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.review = load_module("wislim_review_register", REVIEW_REGISTER_PATH)
        cls.data = cls.review.load_model()
        cls.topics = cls.data["topics"]

    def test_review_ids_are_stable(self):
        self.assertEqual(
            [topic["id"] for topic in self.topics],
            [f"OPH-REV-{index:03d}" for index in range(1, 13)],
        )

    def test_review_source_is_immutable(self):
        metadata = self.review.load_metadata()
        self.assertEqual(
            self.review.sha256(self.review.REVIEW_PDF), metadata["pdf_sha256"]
        )
        self.assertEqual(
            self.review.sha256(self.review.REVIEW_OCR), metadata["text_sha256"]
        )

    def test_verified_transcription_derives_from_the_ocr_text(self):
        metadata = self.review.load_metadata()["verified_transcription"]
        derived = self.review.REVIEW_OCR.read_text(encoding="utf-8")
        for old, new in metadata["substitutions"]:
            self.assertIn(old, derived)
            derived = derived.replace(old, new)
        self.assertEqual(derived, self.review.REVIEW_TEXT.read_text(encoding="utf-8"))
        self.assertEqual(
            self.review.sha256(self.review.REVIEW_TEXT), metadata["sha256"]
        )

    def test_review_quotes_do_not_carry_ocr_artifacts(self):
        artifacts = [old for old, _ in self.review.load_metadata()["verified_transcription"]["substitutions"]]
        for topic in self.topics:
            with self.subTest(topic=topic["id"]):
                for artifact in artifacts:
                    self.assertNotIn(artifact, topic["review_quote"])

    def test_oph_evidence_cites_the_pinned_repository(self):
        review = self.data["review"]
        self.assertEqual(
            review["oph_repository"],
            "https://github.com/FloatingPragma/observer-patch-holography",
        )
        self.assertEqual(len(review["oph_commit"]), 40)
        for topic in self.topics:
            for item in topic["oph_evidence"]:
                url = self.review.external_evidence_url(review, item)
                self.assertTrue(url.startswith(review["oph_repository"] + "/blob/"))
                self.assertIn(item.get("commit", review["oph_commit"]), url)

    def test_evidence_with_its_own_commit_is_the_review_day_release_and_says_so(self):
        review = self.data["review"]
        self.assertNotEqual(review["oph_review_day"]["commit"], review["oph_commit"])
        dated = [(t, i) for t in self.topics for i in t["oph_evidence"] if "commit" in i]
        self.assertTrue(dated)
        for topic, item in dated:
            with self.subTest(topic=topic["id"], quote=item["quote"]):
                self.assertEqual(item["commit"], review["oph_review_day"]["commit"])
                self.assertIn(
                    f"release {review['oph_review_day']['release']}",
                    self.review.external_evidence_link(review, item),
                )

    def test_review_model_rejects_a_commit_it_does_not_record(self):
        data = json.loads(json.dumps(self.data))
        data["topics"][0]["oph_evidence"][0]["commit"] = "0" * 40
        self.assertTrue(any("review-day release" in error for error in self.review.check_model(data)))

    def test_review_register_has_no_errors(self):
        self.assertEqual(self.review.check_all(self.data), [])

    def test_review_dispositions_are_complete(self):
        addressed = [t for t in self.topics if t["oph_status"] == "addressed"]
        contradicted = [t for t in self.topics if t["oph_status"] == "contradicted"]
        not_addressed = [
            t for t in self.topics if t["oph_status"] == "not-addressed"
        ]
        self.assertEqual(len(addressed), 4)
        self.assertEqual(len(contradicted), 3)
        self.assertEqual(len(not_addressed), 5)

    def test_every_topic_has_records_in_reviews_and_docs(self):
        for topic in self.topics:
            for path in (
                self.review.topic_path(topic),
                self.review.docs_topic_path(topic),
            ):
                with self.subTest(topic=topic["id"], path=str(path)):
                    self.assertTrue(path.is_file(), f"missing {path}")
                    text = path.read_text(encoding="utf-8")
                    self.assertIn("status: observation", text)
                    self.assertIn("## Intrinsic assessment", text)
                    self.assertIn("## Extrinsic assessment", text)

    def test_audits_and_response_email_exist_and_cite_topics(self):
        extrinsic = (
            ROOT / "reviews" / "oph-lfdi-57" / "extrinsic-audit.md"
        ).read_text(encoding="utf-8")
        docs_reviews = (ROOT / "docs" / "reviews.md").read_text(encoding="utf-8")
        for topic in self.topics:
            with self.subTest(topic=topic["id"]):
                self.assertIn(topic["id"], extrinsic)
                self.assertIn(topic["id"], docs_reviews)
        email = (
            ROOT / "reviews" / "oph-lfdi-57" / "correspondence" / "02-friedman-response-as-sent.txt"
        ).read_text(encoding="utf-8")
        self.assertIn("https://github.com/docxology/WISLIM-audit", email)

    def test_verification_receipt_records_quote_check(self):
        text = (
            ROOT / "reviews" / "oph-lfdi-57" / "verification.md"
        ).read_text(encoding="utf-8")
        self.assertIn(self.data["review"]["oph_commit"], text)
        self.assertIn(self.data["review"]["oph_checked"], text)
        self.assertIn("git grep -I -c -w -i", text)


class QuoteCheckTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.check = load_module("wislim_quote_check", QUOTE_CHECK_PATH)
        cls.lines = ["first line", "", "a wrapped", "quotation here", "last line"]

    def test_anchor_allows_for_wrapped_prose_near_the_line(self):
        self.assertTrue(self.check.anchored(self.lines, 3, "a wrapped quotation here"))
        self.assertTrue(self.check.anchored(self.lines, 5, "a wrapped quotation here"))
        self.assertFalse(self.check.anchored(self.lines, 3, "not in the file"))

    def test_locate_finds_where_a_moved_quotation_starts(self):
        self.assertEqual(self.check.locate(self.lines, "a wrapped quotation here"), 3)
        self.assertEqual(self.check.locate(self.lines, "quotation here last"), 4)
        self.assertIsNone(self.check.locate(self.lines, "not in the file"))

    def two_commits(self):
        """A throwaway repository whose second commit moves one line and drops another."""
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        repo = Path(directory.name)
        env = dict(os.environ, GIT_AUTHOR_NAME="test", GIT_AUTHOR_EMAIL="test@example.invalid")
        env.update(GIT_COMMITTER_NAME="test", GIT_COMMITTER_EMAIL="test@example.invalid")

        def git(*args):
            return subprocess.run(
                ["git", "-C", str(repo), *args],
                stdin=subprocess.DEVNULL, capture_output=True, text=True, check=True, env=env,
            ).stdout.strip()

        git("init", "-q")
        (repo / "a.md").write_text("alpha line\nbeta line\n", encoding="utf-8")
        git("add", "a.md")
        git("commit", "-q", "-m", "one")
        first = git("rev-parse", "HEAD")
        (repo / "a.md").write_text("new\n" * 7 + "alpha line\n", encoding="utf-8")
        git("add", "a.md")
        git("commit", "-q", "-m", "two")
        return repo, first, git("rev-parse", "HEAD")

    def run_check(self, function, *args, items):
        output = io.StringIO()
        with mock.patch.object(self.check, "evidence", side_effect=lambda: iter(items)):
            with contextlib.redirect_stdout(output), contextlib.redirect_stderr(output):
                return function(*args), output.getvalue()

    def test_verify_reads_an_entry_at_its_own_commit(self):
        repo, first, second = self.two_commits()
        items = [
            ("T", {"path": "a.md", "line": 8, "quote": "alpha line"}),
            ("T", {"path": "a.md", "line": 2, "quote": "beta line", "commit": first}),
        ]
        self.assertEqual(self.run_check(self.check.verify, repo, "r", second, items=items)[0], 0)
        unlabeled = [("T", {"path": "a.md", "line": 2, "quote": "beta line"})]
        self.assertEqual(self.run_check(self.check.verify, repo, "r", second, items=unlabeled)[0], 1)

    def test_verify_fails_when_the_models_record_nothing(self):
        repo, _, second = self.two_commits()
        self.assertEqual(self.run_check(self.check.verify, repo, "r", second, items=[])[0], 1)

    def test_drift_reports_what_moved_and_what_is_gone(self):
        repo, first, second = self.two_commits()
        items = [
            ("T", {"path": "a.md", "line": 1, "quote": "alpha line"}),
            ("T", {"path": "a.md", "line": 2, "quote": "beta line"}),
            ("T", {"path": "a.md", "line": 2, "quote": "beta line", "commit": first}),
        ]
        code, report = self.run_check(self.check.drift, repo, second, first, items=items)
        self.assertEqual(code, 1)
        self.assertIn("0 held, 1 moved, 1 gone; 1 name their own release", report)
        self.assertIn("a.md:1 is now at line 8", report)
        self.assertIn("a.md:2 is gone", report)

    def test_drift_exits_zero_when_every_quotation_holds_and_two_on_a_bad_ref(self):
        repo, _, second = self.two_commits()
        items = [("T", {"path": "a.md", "line": 8, "quote": "alpha line"})]
        self.assertEqual(self.run_check(self.check.drift, repo, second, second, items=items)[0], 0)
        self.assertEqual(self.run_check(self.check.drift, repo, "no-such-ref", second, items=items)[0], 2)


class ReplyRegisterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.reply = load_module("wislim_reply_register", REPLY_REGISTER_PATH)
        cls.data = cls.reply.load_model()
        cls.topics = cls.data["topics"]

    def test_ids_are_stable(self):
        self.assertEqual(
            [topic["id"] for topic in self.topics],
            [f"OPH-REP-{index:03d}" for index in range(1, 17)],
        )
        self.assertEqual(
            [item["id"] for item in self.data["corrections"]],
            [f"OPH-AUD-{index:03d}" for index in range(1, self.reply.CORRECTION_COUNT + 1)],
        )

    def test_register_has_no_errors(self):
        self.assertEqual(self.reply.check_all(self.data), [])

    def test_quotations_are_verbatim_in_the_reply(self):
        lines = self.reply.REPLY_TEXT.read_text(encoding="utf-8").splitlines()
        for topic in self.topics:
            for item in topic["quotes"]:
                with self.subTest(topic=topic["id"], line=item["line"]):
                    self.assertIn(item["quote"], lines[item["line"] - 1])

    def test_the_word_incorrect_is_not_in_the_response_as_sent(self):
        text = self.reply.SENT_TEXT.read_text(encoding="utf-8").lower()
        self.assertNotIn("incorrect", text)

    def test_records_carry_the_observation_status(self):
        for topic in self.topics:
            text = self.reply.topic_path(topic).read_text(encoding="utf-8")
            with self.subTest(topic=topic["id"]):
                self.assertIn("status: observation", text)
                self.assertIn("audit observation, not a required fix", text)

    def test_privacy_guard_rejects_the_general_class(self):
        for sample in ("write to someone@example.org", "call 555-010-0199 today", "call (555) 010-0199"):
            with self.subTest(sample=sample):
                found = self.reply.EMAIL_RE.search(sample) or self.reply.PHONE_RE.search(sample)
                self.assertIsNotNone(found)
        doi = "DOI: 10.21428/4831231e.8c4c6c8f"
        self.assertIsNone(self.reply.EMAIL_RE.search(doi))
        self.assertIsNone(self.reply.PHONE_RE.search(doi))
        self.assertEqual(self.reply.check_privacy(self.reply.privacy_paths(self.data)), [])

    def test_issue_map_covers_the_register(self):
        mapping = self.reply.load_issue_map()
        known = {topic["id"] for topic in self.topics} | {
            item["id"] for item in self.data["corrections"]
        }
        self.assertEqual(set(mapping), known)
        for topic in self.topics:
            number = mapping[topic["id"]]["number"]
            text = self.reply.topic_path(topic).read_text(encoding="utf-8")
            self.assertIn(f"github_issue: {number}", text)


if __name__ == "__main__":
    unittest.main()
