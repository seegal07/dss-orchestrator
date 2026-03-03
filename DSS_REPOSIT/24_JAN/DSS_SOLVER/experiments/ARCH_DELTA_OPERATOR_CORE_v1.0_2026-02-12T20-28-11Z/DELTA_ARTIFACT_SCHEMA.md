# DELTA_ARTIFACT_SCHEMA

## New artifact 1: S08_5_OPERATOR_FRAME
Suggested file: `S08_5_OPERATOR_FRAME.md`

Minimum fields:
- `detected_conflict_types`: [A|B|C|D]
- `dominant_conflict_type`: A|B|C|D
- `priority_rule_applied`: "B>A>C>D"
- `operator_used`: Separation|Mediator|Level Shift|Dependency Inversion
- `x_y_reference`: {x: string, y: string}
- `structure_change_note`: string
- `illusion_test_result`: PASS|FAIL

## New artifact 2: GATECR_RESULT
Suggested file: `GATECR_RESULT.md`

Minimum fields:
- `gatecr_status`: PASS|SOFT_FAIL|HARD_FAIL
- `validation_matrix_answers`: Q1..Q5
- `justification_1l`: string
- `transition_effect`: S09_ALLOWED|S09_ALLOWED_COMPROMISE|S09_NOT_RUN

## New flags (for downstream traceability)
- `COMPROMISE_MODE`: TRUE|FALSE
- `OPERATOR_USED`: Separation|Mediator|Level Shift|Dependency Inversion
- `STRUCTURE_CHANGE_NOTE`: string
