# INTEGRATION_PLAN_v0.1

## 1) Runtime semantics for S08.5 + GateCR
- New sequence:
  - S08 (existing)
  - S08.5 Operator Extraction Layer (new)
  - GateCR (new)
  - S09 -> S10 -> S11 -> S12 (unchanged semantics)

## 2) GateCR reachability rules (mandatory)
- GateCR=PASS:
  - S09, S10, S11, S12 reachable (normal flow).
- GateCR=SOFT_FAIL:
  - S09, S10, S11, S12 reachable.
  - Mandatory runtime flag: `COMPROMISE_MODE=TRUE`.
- GateCR=HARD_FAIL:
  - S09, S10, S11, S12 = NOT_RUN.
  - Mandatory output message: `structural resolution not found`.

## 3) NOT_RUN propagation contract
- Propagation source: GateCR HARD_FAIL.
- Propagation target: Gate9, Gate10, Gate11, Gate12.
- Existing rule Gate12 blocked by Gate9/Gate11 remains intact and additive.

## 4) Required evidence artifacts
### S08.5 artifact (required)
- `S08_5_OPERATOR_FRAME`:
  - `detected_conflict_types[]`
  - `dominant_conflict_type`
  - `priority_rule_applied=B>A>C>D`
  - `operator_used`
  - `x_y_reference`
  - `structure_change_note`
  - `illusion_test_result`

### GateCR artifact (required)
- `GATECR_EVIDENCE`:
  - answers for Q1..Q5 validation matrix
  - separation illusion test result
  - `gatecr_status` PASS|SOFT_FAIL|HARD_FAIL
  - `transition_effect`

### S09 trace artifact (required)
- `S09_MECHANISM_TRACE`:
  - `operator_used`
  - `x_y_reference`
  - `what_changed_structurally`
  - `compromise_mode`

## 5) Required new flags/fields
- `OPERATOR_USED`
- `STRUCTURE_CHANGE_NOTE`
- `COMPROMISE_MODE`
- `GATECR_STATUS`
- `TRANSITION_EFFECT`

## 6) Deterministic operator selection enforcement
- Conflict classification priority:
  1. B (causal dependency)
  2. A (time conflict)
  3. C (interaction/mediator)
  4. D (scale/level)
- If multiple types detected, selected operator follows strict order B>A>C>D.

## 7) Separation Illusion Test integration
- Illusion Test is mandatory part of GateCR evaluation.
- Fail in illusion test cannot yield PASS.
- Illusion test outcome contributes to SOFT_FAIL/HARD_FAIL split.
