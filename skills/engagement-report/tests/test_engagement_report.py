from __future__ import annotations

import importlib.util
import json
import re
import shutil
import sys
import tempfile
import unittest
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = SKILL_ROOT / "scripts" / "engagement_report.py"
SPEC = importlib.util.spec_from_file_location("engagement_report", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def report_object(html: str) -> dict[str, object]:
    match = re.search(r"const REPORT = (.*?);\n\nfunction escapeHtml", html, re.DOTALL)
    if not match:
        raise AssertionError("REPORT object not found")
    return json.loads(match.group(1))


class EngagementReportTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.repo = Path(self.temp_dir.name)

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_add_engagement_is_idempotent(self) -> None:
        first = MODULE.add_engagement(self.repo, "Payments Platform")
        second = MODULE.add_engagement(self.repo, "Payments Platform")
        self.assertEqual(first, second)
        self.assertEqual(first["engagement"], "payments-platform")
        self.assertTrue((Path(first["path"]) / "README.md").is_file())

    def test_generate_carries_dates_and_multiple_images(self) -> None:
        MODULE.add_engagement(self.repo, "Payments Platform")
        MODULE.generate_period(
            self.repo,
            "payments-platform",
            "2026-03-01",
            "2026-03-31",
        )
        period = self.repo / "payments-platform" / "2026-03-01_2026-03-31"
        notes = period / "notes"
        images = notes / "images"
        images.mkdir()
        fixtures = Path(__file__).parent / "fixtures"
        shutil.copyfile(fixtures / "status-note.txt", notes / "status-note.md")
        shutil.copyfile(fixtures / "release-burndown.svg", images / "release-burndown.svg")
        shutil.copyfile(fixtures / "dependency-burnup.svg", images / "dependency-burnup.svg")
        shutil.copyfile(fixtures / "dependency-burnup.svg", period / "client-logo.svg")
        report_path = next(period.glob("*-report.md"))
        report_path.write_text(
            report_path.read_text(encoding="utf-8").replace("client_logo:", "client_logo: client-logo.svg"),
            encoding="utf-8",
        )
        (self.repo / "outside.svg").write_text("<svg/>", encoding="utf-8")

        result = MODULE.update_period(period)
        report_before = Path(result["report"]).read_bytes()
        presentation_before = Path(result["presentation"]).read_bytes()
        MODULE.update_period(period)
        self.assertEqual(Path(result["report"]).read_bytes(), report_before)
        self.assertEqual(Path(result["presentation"]).read_bytes(), presentation_before)

        report = Path(result["report"]).read_text(encoding="utf-8")
        self.assertLess(report.index("2026-01-05"), report.index("2026-02-14"))
        self.assertLess(report.index("2026-02-14"), report.index("2026-03-20"))
        self.assertLess(report.index("2026-03-20"), report.index("2026-06-30"))
        self.assertIn("SOW starts", report)
        self.assertIn("Release burndown after sprint 8", report)
        self.assertIn("Dependency Burnup", report)
        self.assertIn("[Partner-hosted progress visual](https://example.com/progress.png)", report)
        self.assertNotIn("![Partner dashboard](https://", report)
        self.assertEqual(len(result["rejected_images"]), 1)

        presentation = Path(result["presentation"]).read_text(encoding="utf-8")
        data = report_object(presentation)
        self.assertEqual(
            [event["date"] for event in data["timeline"]],
            ["2026-01-05", "2026-02-14", "2026-03-20", "2026-06-30"],
        )
        self.assertIsNone(data["plan_visual"])
        self.assertTrue(data["client_logo"].startswith("data:image/svg+xml;base64,"))
        self.assertEqual(len(data["plan_visuals"]), 3)
        local_images = [image for image in data["plan_visuals"] if not image["remote"]]
        self.assertEqual(len(local_images), 2)
        self.assertTrue(all(image["src"].startswith("data:image/svg+xml;base64,") for image in local_images))
        self.assertIn("vertical card grid", (SKILL_ROOT / "references" / "step-4-presentation-workflow.md").read_text())

    def test_empty_period_keeps_legacy_empty_shapes(self) -> None:
        result = MODULE.generate_period(
            self.repo,
            "Quiet Engagement",
            "2026-04-01",
            "2026-04-07",
        )
        data = report_object(Path(result["presentation"]).read_text(encoding="utf-8"))
        self.assertEqual(data["timeline"], [])
        self.assertEqual(data["plan_visuals"], [])
        self.assertIsNone(data["plan_visual"])


if __name__ == "__main__":
    unittest.main()
