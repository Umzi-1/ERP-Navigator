#!/usr/bin/env python3
"""Generate a simple ERP RFP markdown document from assessment JSON."""

from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path


def _currency(value: float) -> str:
    return f"₹{value:,.0f}"


def build_rfp_markdown(payload: dict) -> str:
    company = payload.get("company", {})
    goals = payload.get("goals", {})
    scope = payload.get("scope", {})

    required_modules = scope.get("required_modules", [])
    integrations = scope.get("integrations", [])
    shortlisted_vendors = scope.get("shortlisted_vendors", [])

    budget = goals.get("implementation_budget_inr", 0)
    target_months = goals.get("target_go_live_months", "TBD")

    lines = [
        f"# ERP Implementation RFP — {company.get('name', 'Unknown Company')}",
        "",
        f"- **Generated on:** {date.today().isoformat()}",
        f"- **Industry:** {company.get('industry', 'N/A')}",
        f"- **Employees:** {company.get('employees', 'N/A')}",
        "",
        "## 1. Business Context",
        company.get("context", "Business context not provided."),
        "",
        "## 2. Objectives",
        f"- Target go-live timeline: **{target_months} months**",
        f"- Budget range: **{_currency(float(budget))}**",
        f"- Primary objective: **{goals.get('primary_objective', 'N/A')}**",
        "",
        "## 3. Scope",
        "### Required Modules",
    ]

    if required_modules:
        lines.extend([f"- {module}" for module in required_modules])
    else:
        lines.append("- To be finalized")

    lines.extend(["", "### Required Integrations"])

    if integrations:
        lines.extend([f"- {integration}" for integration in integrations])
    else:
        lines.append("- To be finalized")

    lines.extend(["", "## 4. Preferred OEM/Vendor Shortlist"])
    if shortlisted_vendors:
        lines.extend([f"- {vendor}" for vendor in shortlisted_vendors])
    else:
        lines.append("- Open to recommendations")

    lines.extend(
        [
            "",
            "## 5. Vendor/Partner Response Requirements",
            "- Proposed implementation plan and milestones",
            "- Team composition and certifications",
            "- Estimated timeline with assumptions",
            "- Detailed commercial quote (license + implementation + support)",
            "- Relevant case studies and references",
            "",
            "## 6. Evaluation Criteria",
            "- Functional fit to process requirements",
            "- Implementation methodology and delivery confidence",
            "- Cost and expected ROI",
            "- Post-go-live support model",
        ]
    )

    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate ERP RFP markdown from assessment JSON")
    parser.add_argument("--input", required=True, help="Path to assessment JSON")
    parser.add_argument("--output", required=True, help="Path to output markdown file")
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)

    payload = json.loads(input_path.read_text(encoding="utf-8"))
    output_path.write_text(build_rfp_markdown(payload), encoding="utf-8")

    print(f"RFP generated: {output_path}")


if __name__ == "__main__":
    main()
