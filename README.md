# RRES — Reasonable Reliance Evidence Standard (v0.1)

RRES is a minimal, open, machine-readable evidence record format for post-incident review of high-risk identity decisions (onboarding and high-value authorization).

It enables deterministic PASS/FAIL validation via a formal JSON Schema and a reference validator.

RRES relies on honest logging and does not detect fraud at source.

RRES is not a trust score, fraud model, compliance guarantee, or safe harbor.

This repository contains:
- RRES v0.1 Technical Specification
- rres-v0.1.schema.json (JSON Schema Draft 2020-12)
- validator_v2.py (reference implementation with --explain mode)
- /examples (4 JSON records: 2 PASS, 2 FAIL)
- compatibility-matrix.md (mapping to NIST, ETSI, EU AI Act, eIDAS)

License: Apache 2.0
