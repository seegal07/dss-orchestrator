# DIFF_NOTES

## Scope
- Published v1.1 governance alignment documents.
- v1.0 files remained untouched.

## Conceptual changes applied
- `OPERATOR_CORE_SPEC_v1.1.md`
  - Harmonized HARD_FAIL propagation scope to `S09–S14` (pipeline insertion and outcomes logic).
  - Kept tri-state semantics unchanged.
  - Added phase-bound qualifier clarifying that no-code restriction is fixation-only and E12 integration patch is allowed when authorized.

- `OPERATOR_CORE_ROUTING_RULES_v1.1.md`
  - Kept NOT_RUN propagation target at `S09–S14`.
  - Defined canonical HARD_FAIL literal explicitly in §5 as exact machine string.
  - Added phase-bound qualifier for fixation vs authorized E12 integration phase.

- `OWNER_POLICY_DECISIONS_v1.1.md`
  - Preserved Q1–Q9 semantics.
  - Fixed Q10 by setting exact canonical literal to match routing §5.
  - Retained/clarified phase-bound qualifier (fixation-only no-code, E12 patch allowed when authorized).

## No semantic drift
- GateCR states remain: PASS / SOFT_FAIL / HARD_FAIL.
- Decision layer semantics unchanged.
