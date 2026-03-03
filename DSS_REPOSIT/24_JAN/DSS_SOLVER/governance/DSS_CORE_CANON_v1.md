# DSS_CORE_CANON_v1
Status: ACTIVE
Class: Governance SoT Reference
Scope: Current canonical baseline mirror only

## 1) Canonical baseline (Stage A)
- Canonical truth = `canonical_slots_v0`.
- Step1 identity = `canonical_hash_v0 = hash(normalize(canonical_slots_v0))`.
- Step1 identity uses the currently documented Stage A identity subset derived from `canonical_slots_v0`.
- `canonical_X` / `canonical_Y` = display-only and excluded from Step1.
- `canonical_hash_text` = legacy / telemetry only and is not Step1 identity.
- `trace_markers` are excluded from identity hashes.

## 2) Truth-source rules
- Stage A metrics / verdict truth-source = GatePFL from:
  - `gate_log.json` (primary)
  - `gate_summary.json` (secondary)
- `SUMMARY.json` and snapshot artifacts are not truth-source for Stage A metrics / verdict.

## 3) PFL v0.1 stance
- PFL v0.1 follows a FAIL-only compute posture.
- Admission-pass remains `NOT_PROVEN` in v0.1.
- `NO_MUTUAL_DEGRADATION` is interpreted as `NOT_PROVEN`, not as “proven no trade-off”.

## 4) S2a observability
- `s2a_hash` is a REQUIRED export for observability.
- `s2a_hash` is not a regression gate.
- S2a eligibility depends on protocol-compliant direction markers per `LIVE_INPUT_PROTOCOL_v0.1.md`.

## 5) Freeze / non-goals
- This document introduces no new rules.
- This document mirrors ACTIVE SoT only.
- Changes to canon require OWNER-gated `GOV_ONLY` changes in source SoT, not in this mirror.
- Stage B startup rules are governed elsewhere and are not changed here.

## 6) Sources
- `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/governance/PHASE0_CONFLICT_FORMALIZATION_SPEC_v0.3.md`
- `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/governance/STAGEA_METRICS_SPEC_v0.1.1_v1.3.md`
- `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/governance/PROBLEM_FRAMING_LAYER_SPEC_v0.2.md`
- `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/governance/REGRESSION_POLICY_v0.1.md`
- `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/governance/LIVE_INPUT_PROTOCOL_v0.1.md`
- `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/governance/LIVE_INPUT_BINDING_SPEC_v0.1.md`

## 7) NOT SPECIFIED
- Exact S1 identity subset key list is not enumerated in this mirror beyond “currently documented Stage A identity subset derived from `canonical_slots_v0`”.
- Any further canonical consolidation decisions are NOT SPECIFIED here.
