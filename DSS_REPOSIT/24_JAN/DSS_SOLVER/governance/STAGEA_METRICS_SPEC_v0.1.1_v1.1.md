# STAGEA_CANONICAL_SLOTS_POLICY_v1.0
Status: ACTIVE
Class: Governance SoT Policy
Scope: Stage A truth-source and invariance policy

## 1) Canonical Truth Model
Stage A truth is represented as canonical slots (structured fields), not free text snapshots.

## 2) Slot Set (minimum)
- canonical_scope
- canonical_X
- canonical_Y
- canonical_constraints
- canonical_hash
- trace_count
- GatePFL verdict (truth-source for admission outcome)

## 3) Truth-Source Rule
For Stage A metrics, admission verdict is taken from GatePFL gate evidence (gate_log/gate_summary), not from text snapshots.

## 4) E22 Invariance Rule
E22 is interpreted as slot-invariance -> verdict-invariance:
- If canonical slots are invariant across V1/V2/V3, verdict drift is not expected.
- If verdict differs, analysis must identify slot-level or gate-level evidence explaining divergence.

## 5) Evidence Contract
Every Stage A validation pack must expose machine-readable anchors for canonical slots and GatePFL verdict/reason.

## 6) Non-goals
This policy does not change engine, harness, PFL logic, or Phase0 rules.
