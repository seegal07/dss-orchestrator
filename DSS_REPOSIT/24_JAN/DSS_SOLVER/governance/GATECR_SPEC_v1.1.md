# GATECR_SPEC_v1.1

Status: ACTIVE SoT (architecture lock)

## 1) Scope
GateCR is the mandatory control gate after S08.5 and before S09.

## 2) Allowed outcomes
GateCR outputs tri-state only:
- `PASS`
- `SOFT_FAIL`
- `HARD_FAIL`

## 3) Validation matrix (mandatory)
GateCR must evaluate:
1. Where conflict existed before transformation.
2. Where conflict exists after transformation.
3. Whether time/place/level of conflict changed.
4. Whether original X→Y dependency still holds in the same form.
5. Whether risk is shifted to time / third party / hidden obligation.

## 4) Separation Illusion Test
Deterministic rule:
- any single YES => `HARD_FAIL`.

## 5) Routing and propagation
- `PASS` -> S09–S14 RUN.
- `SOFT_FAIL` -> S09–S14 RUN and `COMPROMISE_MODE=TRUE` is mandatory in S12_DECISION_RECORD.
- `HARD_FAIL` -> S09–S14 NOT_RUN.

## 6) Run-level mapping
- `SOFT_FAIL` => overall `PARTIAL`.
- `PASS` => overall status determined by remaining gates.
- `HARD_FAIL` => failed/blocked run.

## 7) Canonical HARD_FAIL literal
Fixed exact string only:
- `structural resolution not found`

Localized variants are not allowed for machine audit.

## 8) Backward compatibility
- Historical runs are exempt from GateCR.
- GateCR applies only when Operator Core is enabled by schema/version flag.

## 9) Evidence requirements
GateCR evidence must include:
- `detected_conflict_types[]`
- `dominant_conflict_type`
- applied matrix answers
- separation illusion test result
