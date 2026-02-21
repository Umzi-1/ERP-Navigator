# ERP Navigator — Phase 1 Foundation

ERP Navigator is a neutral, AI-powered ERP discovery and implementation marketplace.

This repository now contains a practical **Phase 1 bootstrap** focused on lead capture,
qualification, and partner handoff:

- Public vendor/OEM content and parity data
- ERP Readiness Assessment data model
- Basic TCO/ROI calculator input model
- Partner directory profile schema
- A working RFP generator utility

## Included OEMs/Vendors

- Oracle
- SAP
- Microsoft
- Infor
- Epicor
- Workday
- Acumatica
- Sage
- Odoo
- IFS

## Repository Structure

- `docs/phase1-mvp-plan.md` — MVP scope, funnel, and delivery slices
- `data/vendors.json` — canonical Phase 1 vendor directory data
- `data/feature-parity-phase1.json` — module-level parity starter matrix
- `data/readiness-assessment-template.json` — assessment form model + scoring hints
- `data/calculator-input-template.json` — TCO/ROI baseline input model
- `data/partner-profile-schema.json` — partner profile validation schema
- `tools/generate_rfp.py` — converts assessment JSON into a downloadable RFP markdown file
- `examples/sample_assessment.json` — sample assessment payload

## Quick Start

Generate an RFP markdown file from sample assessment data:

```bash
python3 tools/generate_rfp.py \
  --input examples/sample_assessment.json \
  --output examples/generated_rfp.md
```

