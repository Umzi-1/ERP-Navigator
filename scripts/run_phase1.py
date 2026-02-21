#!/usr/bin/env python3
"""Cross-platform Phase 1 runner for ERP Navigator."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

JSON_FILES = [
    ROOT / "data/vendors.json",
    ROOT / "data/feature-parity-phase1.json",
    ROOT / "data/readiness-assessment-template.json",
    ROOT / "data/calculator-input-template.json",
    ROOT / "data/partner-profile-schema.json",
    ROOT / "examples/sample_assessment.json",
]


def _run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True, cwd=ROOT, stdout=subprocess.DEVNULL)


def validate() -> None:
    for json_file in JSON_FILES:
        _run([sys.executable, "-m", "json.tool", str(json_file)])
    print("JSON validation passed")


def generate() -> None:
    _run(
        [
            sys.executable,
            "tools/generate_rfp.py",
            "--input",
            "examples/sample_assessment.json",
            "--output",
            "examples/generated_rfp.md",
        ]
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Run ERP Navigator Phase 1 local checks")
    parser.add_argument(
        "command",
        choices=["validate", "generate", "run"],
        default="run",
        nargs="?",
        help="validate JSON, generate sample RFP, or run both",
    )
    args = parser.parse_args()

    if args.command in {"validate", "run"}:
        validate()
    if args.command in {"generate", "run"}:
        generate()

    if args.command == "run":
        print("Local Phase 1 checks complete")


if __name__ == "__main__":
    main()
