# REGRESSION_MIN_SET_v0.1
Status: ACTIVE
Class: Governance SoT Regression Set
Scope: Owner-approved minimal regression packs

References:
- Policy: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/governance/REGRESSION_POLICY_v0.1.md`

## Truth-source (normative)
- Verdict/reason truth-source is GatePFL evidence:
  - `gate_log.json` (primary)
  - `gate_summary.json` (secondary)
- Extractor path (for summary patching): `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/harness/utils/gatepfl_summary_extractor_v0_1.py`
- Snapshot artifacts are not verdict truth-source.

## Pack list (owner-approved; fixed)

1) POSITIVE_A
- Path: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/E22_POSITIVE_CASE_01_RUN_V4_2026-02-24T15-27-32Z`
- Type: StageA invariance-only
- Expected:
  - checkpoints: PASS/PASS
  - Step1: PASS
  - Step2: PASS
  - GatePFL truth-source (observed): `result=fail`, `reason=SOLUTION_AS_XY` (V1/V2/V3)
- Note (non-compared): Step2 here is invariance-only and not an admission-pass expectation.
- Rationale: validates wording-only invariance under stable slots pipeline.

2) POSITIVE_B
- Path: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/E22_POSITIVE_B_CASE_01_RUN_V2_2026-02-24T11-18-23Z`
- Type: framing-clean control
- Expected:
  - checkpoints: PASS/PASS
  - Step1: PASS
  - Step2: PASS
- Note (non-compared): Step2 here is invariance-only and not an admission-pass expectation.
- Rationale: validates clean framing set under current StageA policy.

3) POSITIVE_C
- Path: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/E22_POSITIVE_C_CASE_01_RUN_V1_2026-02-24T15-41-33Z`
- Type: readiness/object-metric control
- Expected:
  - checkpoints: PASS/PASS
  - Step1: PASS
  - Step2: PASS
  - GatePFL truth-source (observed): `result=fail`, `reason=NO_MUTUAL_DEGRADATION` (V1/V2/V3)
- Note (non-compared): Step2 here is invariance-only and not an admission-pass expectation.
- Rationale: validates readiness framing where admission-pass is not required in v0.1/v0.2 readiness.

4) NEGATIVE
- Path: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/E22_RUN_V8_SLOT_INVARIANCE_2026-02-23T15-24-39Z`
- Type: NOT_WORDING_ONLY negative control
- Expected:
  - checkpoints: PASS/PASS
  - Step1: FAIL
  - Step2: NOT_APPLICABLE
- Rationale: enforces negative gating and slot divergence handling.

5) RESOLVED_HISTORY (former KNOWN_ISSUE / PAUSE)
- Path: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/E22_POSITIVE_C_CASE_01_RUN_V3_2026-02-25T11-50-52Z`
- Type: resolved history / non-blocking informational
- Expected:
  - checkpoints: PASS/PASS
  - Step1: PASS
  - Step2: PASS
- Note (non-compared): this entry is retained for historical traceability and does not act as an active blocker.
- Rationale: pause was closed after split-hash resolution; this pack is kept as resolved history.

6) LIVE_PROTOCOL_READINESS_CONTROL
- Path: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/LIVE_OWNER_CASE_STAGEA_PROTOCOL_V0_1_AFTER_MINPATCH2_2026-02-26T09-27-55Z`
- Type: LIVE_PROTOCOL_READINESS_CONTROL
- Expected:
  - checkpoints: PASS
  - Phase0: PASS
  - canonical_hash_v0: non-null
  - slots completeness: PASS (`X_metric`/`X_object`/`Y_metric`/`Y_object` non-null; no `MISSING_SLOT` for those)
  - GatePFL truth-source: `gate_log.json` (primary), `gate_summary.json` (secondary)
- Rationale: live owner-input readiness control for StageA slot completeness under protocol v0.1.

## S2A_CAPABLE baseline note (normative)
- For S2A_CAPABLE baseline packs, `V1`/`V2`/`V3` inputs MUST comply with LIVE_INPUT_PROTOCOL S2a observability gate (explicit direction markers).
- If this gate is not satisfied, treat the pack as:
  - `PRE_S2A_BASELINE` / `N/A` for S2a drift reports.
- Normative S2A_CAPABLE baseline pack:
  - `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/S2A_CAPABLE_BASELINE_FAMILY_CONSISTENT_2026-02-27T11-32-41Z`
- Expectation (additional):
  - family-consistent delta directions (e.g., time -> decelerate markers like `дольше/медленнее`); avoid `больше/меньше` for time metrics.
- Superseded intermediate pack (non-normative):
  - `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/S2A_CAPABLE_BASELINE_PROTOCOL_COMPLIANT_V1_2026-02-27T09-37-12Z` — SUPERSEDED (intermediate, non-family-consistent).
