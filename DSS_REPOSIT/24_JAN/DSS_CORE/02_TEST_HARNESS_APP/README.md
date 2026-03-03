# 02_TEST_HARNESS_APP

Minimal executable Harness for DSS_TRIZ_Business.

## Purpose
- Read SoT test cases from `КВ_24_MAIN/SOT/tests/*.yaml`.
- Validate against `КВ_24_MAIN/SOT/schema/test_vector_schema.yaml`.
- Run Gate0–Gate3 checks (structural MVP).
- Write evidence to `КВ_24_MAIN/SOT/evidence/`.

## Usage
```bash
python3 harness.py run --tc TC04
```

## Notes
- YAML parser is a minimal subset (no external deps).
- Extend gates in `gates.py` to reach Gate14.
