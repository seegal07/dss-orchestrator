# E2_STABILITY_REPORT_v0.1

## Case list (sources)
- VALID (source): /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/E2_STABILITY_2026-02-09T12-49-56Z/CASE_VALID/tests/TC_VALID.yaml
- EDGE (source): /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/E2_STABILITY_2026-02-09T12-49-56Z/CASE_EDGE/tests/TC_EDGE.yaml

## Expected vs Actual (Gate9–Gate12)

### VALID
- Expected: Gate9 PASS, Gate10 PASS, Gate11 PASS, Gate12 PASS
- Actual: Gate9 FAIL, Gate10 PASS, Gate11 FAIL, Gate12 NOT_RUN

### EDGE
- Expected: Gate9 PASS, Gate10 PASS, Gate11 PASS, Gate12 PASS
- Actual: Gate9 PASS, Gate10 PASS, Gate11 FAIL, Gate12 NOT_RUN

## Unexpected FAIL/PASS
- VALID: Gate9 FAIL (concepts < 3) and Gate11 FAIL (selection_criteria_refs missing).
- EDGE: Gate11 FAIL (selection_criteria_refs missing).

## Verdict
UNSTABLE — валидные ожидания не выполняются из‑за отсутствия selection_criteria_refs и недостаточного числа концептов в источниках.
