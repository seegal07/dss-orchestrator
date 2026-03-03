# E22_SLOT_INVARIANCE_PROTOCOL_v1.0
Status: ACTIVE
Class: Governance SoT Protocol
Scope: E22 Stage A invariance validation

## 1) Canonical Invariance Definition
Invariance is evaluated on canonical slots only.
Reference identity is `canonical_hash` computed from normalized canonical slots.

## 2) Slot Set (normative)
- canonical_scope
- canonical_X
- canonical_Y
- canonical_constraints
- canonical_conflict_type_candidate
- canonical_hash

## 3) Verdict Truth-Source (normative)
Admission verdict for E22 is sourced from GatePFL gate evidence (gate_log/gate_summary),
not from textual snapshots.

## 4) E22 Protocol Rule
- If canonical_hash is invariant across V1/V2/V3, GatePFL verdict drift is not expected.
- If GatePFL verdict differs, analysis must provide slot-level or gate-level evidence anchors.

## 5) Metrics Binding
flip_baseline_relative and PFL_variance_baseline_relative must be computed from GatePFL verdicts.

## 6) Evidence Contract
Each E22 pack must include machine-readable artifacts for:
- canonical slots/hash,
- GatePFL verdict/reason,
- diff anchors for any divergence.

## 7) Non-goals
No engine/harness/PFL/Phase0 implementation changes are introduced by this protocol.

## E22 Step1 canonical hash source (slots-hash)
For E22 slot-invariance:
- Use canonical_hash_v0 (hash(slots_v0)) as the primary hash.
- canonical_hash_text is legacy only and MUST NOT be used for Step1 invariance.
- canonical_X/canonical_Y are display-only and MUST NOT be used for Step1 invariance.

## E22 Negative Test: NOT_WORDING_ONLY

### Negative set definition (normative)
NEGATIVE E22 set includes variants where `canonical_slots_v0` diverges between V1/V2/V3:
- metrics differ, and/or
- directions differ, and/or
- objects differ.

### Step1 behavior (normative)
For NEGATIVE E22 set, Step1 MUST:
- compute field-level slot diff,
- emit deterministic marker `NOT_WORDING_ONLY`,
- emit `SLOT_DIVERGENCE` with the exact list of divergent fields.

Expected Step1 verdict for NEGATIVE E22 set:
- `FAIL`.

### Step2 gating (normative)
If `NOT_WORDING_ONLY` is triggered:
- Step2 MUST be `NOT_APPLICABLE`,
- even if GatePFL result/reason appears matched across variants.

### Evidence requirements (normative)
The report MUST include:
- per-variant `canonical_slots_v0` snapshots,
- explicit list of divergent fields used by Step1.

## E22 Positive_A: INVARIANCE_ONLY (normative)

### Positive set definition (normative)
POSITIVE E22 set includes variants where `canonical_slots_v0` MUST be identical between V1/V2/V3.
Display wording may differ, but the structural meaning is preserved.

### Case (v0.1)
- CASE_ID: E22_POSITIVE_CASE_01
- Scope: "Запуск филиалов в Европе"
- Constraint: "Не увеличивать бюджет и не увеличивать срок исследования/подготовки" (keep identical)

### Variants (raw texts, wording-only)
V1:
"Нужно ускорить запуск филиалов в Европе и повысить точность прогноза, не увеличивая бюджет и срок исследования."
V2:
"Как быстрее запустить филиалы в Европе и сделать прогноз точнее, не раздувая бюджет и сроки исследования?"
V3:
"Как ускорить старт филиалов в Европе, улучшив точность прогноза, без роста бюджета и длительности исследования?"

### Expected protocol behavior
- Step1 (slot-invariance via canonical_hash_v0): EXPECTED PASS
- Step2 = invariance-only check and is evaluated only if Step1 PASS
- GatePFL may be FAIL in v0.1; GatePFL PASS is not expected in v0.1

## E22 Positive_B: FRAMING_CLEAN (normative)

- Step1 PASS required.
- GatePFL_reason MUST NOT be `SOLUTION_AS_XY`.
- GatePFL_reason MUST NOT be `SYMPTOM_FRAMING`.
- Enum mismatch forbidden: `pfl_reason invalid` is not allowed.
- GatePFL PASS is NOT expected in v0.1 and MUST NOT be used as DoD.

## v0.1 Reporting/DoD Guardrail (normative)

- Any report MUST explicitly separate:
  - (i) invariance outcome (PASS/FAIL)
  - (ii) substantive admission outcome (may be FAIL in v0.1)
- For Positive_A/Positive_B in v0.1, GatePFL FAIL MUST NOT be labeled as test failure when invariance objectives are satisfied.

## v0.2 Readiness Guardrail (normative)

- Admission-pass tests are valid only when PROVEN mutual-degradation signals are implemented.
- Until PROVEN signals are implemented, admission-pass expectations MUST be labeled as `NOT_PROVEN`.
- `conflict_type_candidate` is excluded from PROVEN signals (`PROOF_WEIGHT=0`) until a real source exists.
