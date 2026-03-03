# LIVE_INPUT_PROTOCOL_v0.1
Status: ACTIVE
Class: Governance SoT Protocol
Scope: Live input structuring before Stage A run

## 1) Purpose (normative)
- Convert live “dirty text” into StageA-ready inputs so Phase0 can fill `canonical_slots_v0` sufficiently for readiness DoD.
- This protocol is not an advice tool and not a solver; it is input structuring only.

## 2) Required fields before run (normative)
Owner MUST fill all fields explicitly:
- `scope` (one sentence)
- `timeframe_deadline` (date or month)
- `constraints` (3–6 bullets, include hard constraints)
- `X_metric` (one noun; closed-ish list preferred, free text allowed)
- `X_object` (1–3 words)
- `X_metric_polarity` (`HIGHER_IS_BETTER` | `LOWER_IS_BETTER` | `UNKNOWN`)
- `Y_metric` (one noun)
- `Y_object` (1–3 words)
- `Y_metric_polarity` (`HIGHER_IS_BETTER` | `LOWER_IS_BETTER` | `UNKNOWN`)

## 3) Forbidden patterns in X/Y (normative)
- No action verbs in X/Y (examples: `переехать`, `сделать`, `внедрить`, `запустить`).
- If action wording is present, move it to `CONTEXT`, not to X/Y.

## 4) LIVE_INPUT template for harness (normative)
Use this exact block shape in `LIVE_INPUT.txt`:

```text
SCOPE: <one sentence>
TIMEFRAME_DEADLINE: <date or month>
CONSTRAINT_1: <hard constraint>
CONSTRAINT_2: <hard constraint>
CONSTRAINT_3: <constraint>
X_METRIC: <one noun>
X_OBJECT: <1-3 words>
X_METRIC_POLARITY: <HIGHER_IS_BETTER|LOWER_IS_BETTER|UNKNOWN>
Y_METRIC: <one noun>
Y_OBJECT: <1-3 words>
Y_METRIC_POLARITY: <HIGHER_IS_BETTER|LOWER_IS_BETTER|UNKNOWN>
CONTEXT: <optional background; actions allowed here>
```

## 5) Readiness mapping for repeat live-run (normative)
DoD PASS conditions:
- Phase0 PASS; `canonical_hash_v0` is non-null.
- `canonical_slots_v0`: `scope` non-empty; `X_metric`+`X_object` non-null; `Y_metric`+`Y_object` non-null.
- No `MISSING_SLOT:X_object` and no `MISSING_SLOT:Y_object`.
- Truth-source for Stage A verdict is GatePFL from `gate_log.json`; `SUMMARY.json` must match via extractor if used.
- GatePFL may be `FAIL/NO_MUTUAL_DEGRADATION`; this is not a v0.1 protocol failure by itself.

## 6) References (normative links)
- Intent SoT: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/governance/DSS_PRODUCT_INTENT_SOT_v0.1.md`
- StageA SoT: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/governance/STAGEA_METRICS_SPEC_v0.1.1_v1.3.md`
- Phase0 SoT: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/governance/PHASE0_CONFLICT_FORMALIZATION_SPEC_v0.3.md`

## 7) Readiness Control (Live)
- Canonical readiness control pack for live slots completeness:
  - `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/LIVE_OWNER_CASE_STAGEA_PROTOCOL_V0_1_AFTER_MINPATCH2_2026-02-26T09-27-55Z`
- Control objective: `canonical_slots_v0` completeness for `X_metric`/`X_object`/`Y_metric`/`Y_object` (non-null) and no `MISSING_SLOT` for these fields.
- This control is NOT an admission-pass expectation in v0.1; GatePFL may remain `FAIL/NO_MUTUAL_DEGRADATION`.
- Truth-source for verdict remains GatePFL from `gate_log.json` (with `gate_summary.json` secondary if present).

## 8) S2a observability gate (direction markers)
- If submitter expects S2a/delta_direction observability, `X` and `Y` text MUST include at least one explicit allowed direction marker.
- Allowed markers (closed list for this protocol patch):
  - RU: `выше`, `ниже`, `больше`, `меньше`, `быстрее`, `медленнее`, `дольше`, `короче`
- No expansion beyond this list in this protocol version.
- If markers are absent in input text, diagnostics expectation MUST be set to:
  - `S2a = N/A (input not eligible)`
  - This is a doc-level rule only; no code behavior is changed by this section.
