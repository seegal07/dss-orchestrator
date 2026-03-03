# PHASE0_CONFLICT_FORMALIZATION_SPEC_v0.3
Status: ACTIVE
Class: Governance SoT Spec
Scope: Phase0 canonical representation contract for Stage A

## 1) Normative model (single source)
- Canonical truth for Stage A is `canonical_slots_v0`.
- `canonical_hash_v0` is the Stage A canonical identity and MUST be computed as:
  - `canonical_hash_v0 = hash(normalize(canonical_slots_v0))`
- `canonical_X` and `canonical_Y` are display-only fields and are non-normative for Step1 invariance.
- `canonical_hash_text` is legacy telemetry/replay only and MUST NOT be used for Step1 invariance.

## 2) canonical_slots_v0 schema (normative)
Required slots:
- `scope`
- `X_direction`
- `X_metric`
- `X_object`
- `Y_direction`
- `Y_metric`
- `Y_object`
- `constraints`
- `trace_markers`

S2a-support slots (required for S2a evaluation):
- `X_delta_direction`
- `Y_delta_direction`
- `X_metric_polarity`
- `Y_metric_polarity`

## 3) Deterministic normalization and hashing (normative)
- String normalization: trim + collapse whitespace.
- Stable ordering for list fields.
- Stable key ordering in serialized payload before hashing.
- `raw_hash` is audit-only and MUST NOT be used as Stage A truth identity.

## 4) Trace requirements (normative)
- `trace_count > 0` is required.
- Missing required slot markers MUST be explicit in `trace_markers` (e.g., `MISSING_SLOT:*`).
- Unknown S2a polarity must be explicit via `UNKNOWN_POLARITY:*`.

## 5) Boundary and non-goals
- This spec does not change PFL compute logic, gates logic, or engine behavior.
- This spec defines only canonical representation and identity contract.

## Appendix A) LEGACY (non-normative)
- Legacy text payload hash (`canonical_hash_text`) is retained for replay/telemetry compatibility.
- Legacy text fields (`canonical_scope`, `canonical_X`, `canonical_Y`, `canonical_constraints`, `canonical_conflict_type_candidate`) are not Step1 identity inputs.
