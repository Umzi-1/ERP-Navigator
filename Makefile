.PHONY: help validate generate-rfp run

help:
	@echo "Targets:"
	@echo "  make validate      - validate all JSON files"
	@echo "  make generate-rfp  - generate sample RFP markdown"
	@echo "  make run           - validate + generate sample RFP"

validate:
	python3 -m json.tool data/vendors.json >/dev/null
	python3 -m json.tool data/feature-parity-phase1.json >/dev/null
	python3 -m json.tool data/readiness-assessment-template.json >/dev/null
	python3 -m json.tool data/calculator-input-template.json >/dev/null
	python3 -m json.tool data/partner-profile-schema.json >/dev/null
	python3 -m json.tool examples/sample_assessment.json >/dev/null
	@echo "JSON validation passed"

generate-rfp:
	python3 tools/generate_rfp.py --input examples/sample_assessment.json --output examples/generated_rfp.md

run: validate generate-rfp
	@echo "Local Phase 1 checks complete"
