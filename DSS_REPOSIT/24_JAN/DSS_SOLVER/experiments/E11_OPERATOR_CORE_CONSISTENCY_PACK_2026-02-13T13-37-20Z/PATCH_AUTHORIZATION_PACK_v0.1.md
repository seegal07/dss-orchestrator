# PATCH_AUTHORIZATION_PACK_v0.1

## E12 ordered patch plan (authorization only)

### Step 1 — Governance alignment patch
- Target files:
  - `OPERATOR_CORE_SPEC_v1.0.md` (or v1.1)
  - `OPERATOR_CORE_ROUTING_RULES_v1.0.md` (or v1.1)
  - `OWNER_POLICY_DECISIONS_v1.0.md` (append canonical literal)
- Goal:
  - remove propagation conflict (S09–S14)
  - lock exact canonical HARD_FAIL literal
  - clarify phase-bound non-modification clause
- Acceptance check:
  - `CONSISTENCY_MATRIX`: no CONFLICT on propagation scope
  - no AMBIGUOUS on canonical message
- Rollback note:
  - keep previous versions (`v1.0`) untouched; publish changes as `v1.1` docs.

### Step 2 — Schema routing patch (new schema version)
- Target files:
  - new `TEST_VECTOR_SCHEMA_v0.2` (or equivalent versioned name)
  - routing note cross-reference update
- Goal:
  - encode Operator Core enable flag
  - preserve historical run exemption
- Acceptance check:
  - v0.1 vectors remain valid
  - v0.2 vectors require S08.5 + GateCR fields
- Rollback note:
  - disable v0.2 selection path and continue with v0.1 only.

### Step 3 — Harness structural/flow patch
- Target files:
  - `DSS_SOLVER/harness/gates_structural.py`
  - `DSS_SOLVER/harness/harness.py`
  - optional new validator module for GateCR matrix
- Goal:
  - add GateCR tri-state handling
  - enforce NOT_RUN propagation S09–S14 on HARD_FAIL
  - enforce PARTIAL run-level mapping on SOFT_FAIL
- Acceptance check:
  - deterministic transition table reproduced in gate_summary/log
  - Gate9–Gate12 semantics unchanged when GateCR=PASS
- Rollback note:
  - feature-flag GateCR route off and revert to previous run path.

### Step 4 — Export/evidence patch
- Target files:
  - `harness.py` export section
- Goal:
  - include S08.5 and GateCR evidence artifacts/flags in output package
- Acceptance check:
  - output package contains required new artifacts
  - historical package format readable (backward parsing not broken)
- Rollback note:
  - keep old exporter path as fallback serializer.

### Step 5 — Post-patch verification (no pilot UX)
- Scope:
  - synthetic consistency run set only
- Acceptance check:
  - PASS/SOFT_FAIL/HARD_FAIL transitions match policy lock
  - conflict-free governance matrix
- Rollback note:
  - rollback to previous harness commit and keep governance-only artifacts.
