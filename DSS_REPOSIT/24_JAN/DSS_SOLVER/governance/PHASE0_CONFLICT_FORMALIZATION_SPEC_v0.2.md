# PHASE0_CANONICAL_SLOTS_AND_HASH_SPEC_v1.0
Status: ACTIVE
Class: Governance SoT Spec
Scope: Phase0 canonical representation contract

## 1) Canonical Slots Schema (normative)
Required slots:
- canonical_scope (string)
- canonical_X (string)
- canonical_Y (string)
- canonical_constraints (array<string>)
- canonical_conflict_type_candidate (enum: causal|temporal|interaction|scale)
- phase0_trace (array<object>)
- trace_count (int)

## 2) Hash-from-Slots Rule (normative)
`canonical_hash` MUST be computed only from canonical slots, not from raw input text.
The canonical hash payload MUST include exactly:
- canonical_scope
- canonical_X
- canonical_Y
- canonical_constraints
- canonical_conflict_type_candidate

## 3) Deterministic Normalization (normative)
Before hashing, the canonical payload MUST be normalized deterministically:
- trim and collapse whitespace in strings;
- stable ordering for canonical_constraints;
- stable key ordering in hash payload serialization.

## 4) Raw Hash Separation
`raw_hash` is allowed for audit only and MUST NOT be used as Stage A truth-source hash.

## 5) Invariance Contract
If canonical slots are invariant across paraphrases, `canonical_hash` must be invariant.
Any divergence in `canonical_hash` requires slot-level diff evidence.

## 6) Non-goals
This spec does not change engine, harness, PFL logic, or Phase0 decision rules.

## Canonical slots v0 and dual-hash (v0.3 policy block)

### Canonical truth
- Canonical truth for Stage A = canonical_slots_v0 (structured slots).
- canonical_X / canonical_Y are display-only (derived), non-normative.

### Minimal slots schema v0
Required:
- X_direction (enum), X_metric (short label), X_object (short label)
- Y_direction (enum), Y_metric, Y_object

Optional (only if explicitly present/extractable):
- scope, timeframe, constraints (normalized list)

### Dual hash
- canonical_hash_v0 = hash(normalize(canonical_slots_v0))  [NEW primary Stage A canonical identity]
- canonical_hash_text = hash(normalize(legacy_text_payload)) [LEGACY for replay/comparability]
Legacy_text_payload = {canonical_scope, canonical_X_display, canonical_Y_display, canonical_constraints, canonical_conflict_type_candidate}

### Invariance for E22
- Step1 slot-invariance MUST use canonical_hash_v0 (not text).
- Text equality is not a criterion.

### Trace requirements
- Phase0 MUST emit trace_count > 0
- If required slot missing: trace contains MISSING_SLOT:<slot>
- If slots diverge across variants: trace contains SLOT_DIVERGENCE with slot-level diffs
