# STAGE A METRICS SPEC v0.1
Project: DSS_TRIZ_Business  
Scope: Stage A (Admission / PFL) metrics only  
Status: Governance SoT (ACTIVE after index link)

## 0) Purpose
Materialize formal definitions for Stage A variability metrics so E22-like experiments can be computed reproducibly from evidence artifacts.

## 1) Evidence sources (binding for v0.1)
E22 Master Report:
- DSS_SOLVER/experiments/E22_E23_VARIABILITY_PACK_2026-02-20T11-39-12Z/E22_E23_MASTER_REPORT_v0.1.md

E22 exports (snippet exports used as evidence of verdict domain and keys):
- .../RUN_EXPORT_SNIPPETS/E22_V1_export.json
- .../RUN_EXPORT_SNIPPETS/E22_V2_export.json
- .../RUN_EXPORT_SNIPPETS/E22_V3_export.json

## 2) Domain: pfl_verdict
Definition:
- pfl_verdict ∈ {PASS, FAIL}

Evidence anchors:
- E22_E23_MASTER_REPORT_v0.1.md contains column “PFL verdict” with values PASS/FAIL only.
- E22_V*_export.json contains key "pfl_verdict" with values PASS/FAIL only.

## 3) Variants model (E22-style)
Variants are an explicit, manually defined list:
- V1 = baseline (as-is wording)
- V2..VN = wording-only paraphrases of V1

Invariants (must hold for v0.1 applicability):
- Same case_id / same case provenance
- Same scope intent (no new variables, no scope widening)
- “Wording-only” changes; semantic target unchanged

## 4) Guardrail: search_loop is not a variants generator
If an execution artifact contains search_loop=True, it does NOT mean variants were generated.
Variants are defined externally as V1..VN (manual list) and are not derived from search_loop.

## 5) FLIP_DEFINITION (baseline-relative)
Flip occurs iff:
- ∃ i ∈ {2..N} such that pfl_verdict(Vi) ≠ pfl_verdict(V1),
under the invariants in §3.

## 6) PFL_variance (baseline-relative)
Let N = number of variants in the set (N ≥ 2).

PFL_variance = #( i ∈ {2..N} : pfl_verdict(Vi) ≠ pfl_verdict(V1) ) / (N − 1)

Interpretation:
- 0.0 = no flips relative to baseline V1
- 1.0 = every paraphrase flips relative to baseline V1

Consistency check (E22 example, N=3):
- If only one of {V2,V3} differs from V1 → PFL_variance = 1/2 = 0.5 (50%)

## 7) Applicability limitation
This spec is valid ONLY for sets constructed as:
- “V1 baseline + wording-only paraphrases V2..VN”
It is NOT valid for “equal-status alternatives” (where no baseline reference is defined).

## 8) Normative truth source for pfl_verdict (metrics)
For Stage A metrics, the normative verdict is taken from:
- GatePFL result in gate_log.json (or gate_summary.json if present).

Rationale:
- PFL output snapshot (e.g., artifacts/S03_5_PFL_OUTPUT.md) may show PASS while GatePFL fails with SOLUTION_AS_XY; metrics must reflect gate admission outcome.

Non-normative:
- artifacts/S03_5_PFL_OUTPUT.md is treated as a snapshot, not as the admission verdict source for metrics.
