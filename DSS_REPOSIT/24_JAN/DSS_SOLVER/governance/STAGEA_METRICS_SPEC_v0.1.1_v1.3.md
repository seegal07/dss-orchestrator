# STAGEA_METRICS_SPEC_v0.1.1_v1.3
Status: ACTIVE
Class: Governance SoT Protocol
Scope: Stage A invariance and metrics truth-source policy

## 1) Canonical identity and Step1 (normative)
- Step1 slot-invariance uses only `canonical_hash_v0`.
- `canonical_hash_v0` identity is derived from `canonical_slots_v0`.
- `canonical_X` and `canonical_Y` are display-only and MUST NOT be used in Step1 identity checks.
- `canonical_hash_text` is legacy telemetry only and MUST NOT be used for Step1 identity.

## 2) Step1 protocol (normative)
- For wording-only sets, Step1 expects equality of `canonical_hash_v0` across V1/V2/V3.
- For non-wording-only sets, Step1 must report field-level slot divergence with deterministic markers.

## 3) Truth-source for admission metrics (normative)
- Admission verdict/reason truth-source is GatePFL evidence only:
  - `gate_log.json` (primary)
  - `gate_summary.json` (secondary if present)
- Snapshot artifacts (including `S03_5_PFL_OUTPUT.md`) are not verdict truth-source for metrics.

## 4) Metrics binding (normative)
- `flip_baseline_relative` and `PFL_variance_baseline_relative` are computed from GatePFL verdicts.
- Any verdict divergence must be accompanied by slot-level or gate-level anchors.

## 5) E22 protocol controls (normative)
- Negative set (`NOT_WORDING_ONLY`):
  - Step1 must emit `NOT_WORDING_ONLY` and `SLOT_DIVERGENCE`.
  - Step2 is `NOT_APPLICABLE`.
- Positive_A (`INVARIANCE_ONLY`):
  - Step1 PASS required.
  - Stage A substantive admission may still be FAIL in v0.1/v0.2 readiness.
- Positive_B (`FRAMING_CLEAN`):
  - Step1 PASS required.
  - GatePFL reason must not be `SOLUTION_AS_XY` or `SYMPTOM_FRAMING`.

## 6) Reporting guardrail (normative)
- Reports must separate:
  - invariance outcome (Step1)
  - substantive admission outcome (GatePFL)
- GatePFL FAIL must not be mislabeled as protocol failure when invariance objective is satisfied.

## 7) S2a hash observability policy (normative)
- `s2a_hash` is a REQUIRED exported diagnostic field for observability.
- `s2a_hash` is NOT a Stage A regression PASS/FAIL gate in v0.2.
- Until OWNER defines a normative drift criterion for S2a, any `s2a_hash` drift is observe-only and must not fail Step1 when `canonical_hash_v0` invariance holds.
- `s2a_hash` observability requires input eligibility per `LIVE_INPUT_PROTOCOL_v0.1.md` (S2a observability gate).
