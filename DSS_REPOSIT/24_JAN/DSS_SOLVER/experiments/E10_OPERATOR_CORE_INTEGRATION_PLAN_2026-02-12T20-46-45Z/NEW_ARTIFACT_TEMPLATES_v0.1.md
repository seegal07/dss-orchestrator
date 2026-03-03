# NEW_ARTIFACT_TEMPLATES_v0.1

## Template A — S08_5_OPERATOR_FRAME.md

```md
# S08_5_OPERATOR_FRAME

- detected_conflict_types: [A|B|C|D]
- dominant_conflict_type: A|B|C|D
- priority_rule_applied: B>A>C>D
- operator_used: Separation|Mediator|Level Shift|Dependency Inversion
- x_y_reference:
  - x: <from S04.improve_x>
  - y: <from S04.worsen_y>
- structure_change_note: <what changed structurally>
- illusion_test_result: PASS|FAIL
- conflict_locus_before: <time/place/level>
- conflict_locus_after: <time/place/level>
```

## Template B — GATECR_EVIDENCE.md

```md
# GATECR_EVIDENCE

## Validation Matrix
Q1. where_conflict_before: <answer>
Q2. where_conflict_now: <answer>
Q3. locus_changed_time_place_level: YES|NO + <note>
Q4. dependency_x_to_y_still_holds: YES|NO + <note>
Q5. risk_shifted_hidden_or_third_party: YES|NO + <note>

## Separation Illusion Test
- postponement_only: YES|NO
- displaced_to_third_party_only: YES|NO
- hidden_obligation_substitution: YES|NO
- contradiction_unchanged_under_same_boundary: YES|NO

## Result
- gatecr_status: PASS|SOFT_FAIL|HARD_FAIL
- transition_effect: S09_ALLOWED|S09_ALLOWED_COMPROMISE|S09_NOT_RUN
- compromise_mode: TRUE|FALSE
- justification_1l: <single line>
```

## Template C — S09_MECHANISM_TRACE.md

```md
# S09_MECHANISM_TRACE

For each concept:
- concept_index: <int>
- operator_used: Separation|Mediator|Level Shift|Dependency Inversion
- x_y_reference:
  - x: <S04.improve_x>
  - y: <S04.worsen_y>
- what_changed_structurally: <explicit structural delta>
- compromise_mode: TRUE|FALSE
- gatecr_status_at_entry: PASS|SOFT_FAIL
```
