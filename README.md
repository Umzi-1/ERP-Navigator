# ERP Navigator — Phase 1 Foundation

ERP Navigator is a neutral, AI-powered ERP discovery and implementation marketplace.

This repository currently contains a practical **Phase 1 bootstrap** focused on lead capture,
qualification, and partner handoff data + tooling.

## Included in this Phase 1 repo

- Public vendor/OEM content seed data
- ERP Readiness Assessment template model
- Basic TCO/ROI calculator input model
- Partner directory profile schema
- RFP generator utility (JSON ➜ markdown)

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
- `tools/generate_rfp.py` — converts assessment JSON into RFP markdown
- `scripts/run_phase1.py` — cross-platform local runner (no `make` required)
- `examples/sample_assessment.json` — sample assessment payload
- `examples/generated_rfp.md` — generated sample RFP output

## How to run locally

> Note: this repo does not yet include a web app server. “Run locally” means validating data artifacts and running the CLI conversion flow.

### Prerequisites

- Python 3.9+
- GNU Make (optional)

### Option A (cross-platform, recommended)

Works on macOS/Linux/Windows (PowerShell/CMD):

```bash
python scripts/run_phase1.py run
```

Other commands:

```bash
python scripts/run_phase1.py validate
python scripts/run_phase1.py generate
```

### Option B (macOS/Linux with `make`)

```bash
make run
```

### Option C (Windows PowerShell, no make)

```powershell
python -m json.tool data/vendors.json > $null
python -m json.tool data/feature-parity-phase1.json > $null
python -m json.tool data/readiness-assessment-template.json > $null
python -m json.tool data/calculator-input-template.json > $null
python -m json.tool data/partner-profile-schema.json > $null
python -m json.tool examples/sample_assessment.json > $null
python tools/generate_rfp.py --input examples/sample_assessment.json --output examples/generated_rfp.md
```

## Quick start (custom input)

```bash
python tools/generate_rfp.py --input <your-assessment.json> --output <your-rfp.md>
```

