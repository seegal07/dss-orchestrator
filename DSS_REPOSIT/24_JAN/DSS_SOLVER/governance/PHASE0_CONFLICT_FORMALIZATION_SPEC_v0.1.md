# PHASE0_CONFLICT_FORMALIZATION_SPEC_v0.1
Status: ACTIVE (architecture-only)
Owner: Alex
Class: Pre-admission canonical formalization

## A) Purpose + Non-goals
### Purpose
Phase 0 converts raw problem text into a canonical structured conflict object used as input to Admission (PFL).

### Non-goals
- Phase 0 does NOT solve the problem.
- Phase 0 does NOT propose mechanisms/actions.
- Phase 0 does NOT change intent.
- Phase 0 does NOT alter owner goal semantics.

## B) Placement
`Free text -> Phase 0 -> PFL -> S04 -> Operator -> GateCR`

## C) Canonical Object Contract (STRICT FIELDS)
Phase 0 output MUST include:
- `system_scope` (string)
- `X_param` (string; parameter/property, NOT action)
- `Y_param` (string; parameter/property, NOT action)
- `tension_direction` (string; `X↑ -> Y↓` / `Y↑ -> X↓` or both)
- `constraints` (list of strings; unchanged meaning)
- `conflict_type_candidate` (enum: `causal|temporal|interaction|scale`)
- `canonical_hash` (string; deterministic normalized hash)
- `raw_hash` (string; hash of raw input)
- `trace` (list of items):
  - `raw_fragment` (short)
  - `interpreted_parameter` (short)
  - `reasoning_trace` (short; rule used)
  - `confidence_level` (`LOW|MED|HIGH`)

## D) Rules
- Phase 0 MUST separate intent/requirements from mechanisms.
- Phase 0 MUST reject `solution-as-XY` in canonical fields by either:
  - converting action -> parameter (if implicit and deterministically reconstructable), OR
  - marking as ambiguous with trace + confidence.
- Phase 0 MUST NOT add new business hypotheses.
- Phase 0 MUST NOT change owner goal.
- Reconstruction boundary (Level C): implicit parameters may be revealed, but no new intent may be introduced.
- Trace transparency is mandatory for every interpreted mapping.

## E) Determinism Rules
- Determinism policy: STRONG.
- Same raw input MUST produce identical canonical object and `canonical_hash`.
- Normalization rules MUST be deterministic:
  - trim/normalize whitespace,
  - normalize punctuation handling,
  - stable ordering of lists,
  - stable ordering of trace entries,
  - stable casing policy for hash input.
- `canonical_hash` MUST be computed only from normalized canonical object.
- `raw_hash` MUST be computed from raw input payload independently.
- `input_fingerprint` for repeatability tests MUST equal `canonical_hash`.

## F) Failure Modes
If formalization is impossible without introducing new intent:
- `phase0_verdict = FAIL`
- `phase0_reason_code = AMBIGUOUS_INTENT | INSUFFICIENT_SCOPE | MECHANISM_ONLY_INPUT | OTHER`
- pipeline MUST STOP before PFL.

## G) Export Fields (machine-readable)
Phase 0 export MUST include:
- `phase0_verdict`
- `phase0_reason_code`
- `canonical_hash`
- `raw_hash`
- `trace_count`
- `confidence_summary`

## Constraints (No implementation in this spec)
- No changes to engine tri-state behavior.
- No changes to GateCR logic.
- No changes to Operator Core logic.
- No changes to PFL logic in this phase.
