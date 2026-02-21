# ERP Navigator — Phase 1 MVP Plan

## Goal
Launch a monetizable baseline that captures and qualifies ERP buyers, then routes them to implementation partners.

## Phase 1 In-Scope Capabilities

1. **Public content**
   - ERP 101 and vendor explainers
   - High-intent SEO landing pages (compare, TCO, ROI)
2. **ERP Readiness Assessment** (email gated)
   - Captures company profile, process maturity, systems landscape, constraints
3. **Basic TCO + ROI calculators**
   - Template-driven estimates for first-pass business case
4. **Feature parity matrix**
   - Top 6–8 modules across initial OEM set
5. **Partner directory**
   - Searchable profiles and contact form lead routing
6. **RFP generator**
   - Auto-builds RFP draft from assessment responses
7. **Admin + analytics baseline**
   - Lead events, funnel conversion, partner handoff tracking

## Initial Vendor/OEM Coverage

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

## Buyer Funnel (Phase 1)

1. Learn: ERP content + compare pages
2. Assess: short readiness flow with email gate
3. Compare: initial shortlist + basic cost/ROI estimates
4. RFP: downloadable document from captured inputs
5. Match: routed to partner directory contact workflows

## Implementation Slices

### Slice A — Content + Data Layer
- Publish canonical vendor metadata (`data/vendors.json`)
- Publish parity starter matrix (`data/feature-parity-phase1.json`)

### Slice B — Qualification Layer
- Readiness schema and scoring hints (`data/readiness-assessment-template.json`)
- Calculator assumptions model (`data/calculator-input-template.json`)

### Slice C — Marketplace Layer
- Partner schema (`data/partner-profile-schema.json`)
- Lead packaging metadata to support later monetization modes

### Slice D — Conversion Tooling
- Generate RFP draft from assessment (`tools/generate_rfp.py`)

## Success Metrics (MVP)

- Assessment completion rate
- % of qualified leads (defined by readiness + budget + timeline)
- RFP generation rate
- Partner response rate
- Lead-to-opportunity conversion rate

