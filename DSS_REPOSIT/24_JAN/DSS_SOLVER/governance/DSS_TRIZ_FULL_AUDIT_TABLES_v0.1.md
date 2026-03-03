# DSS_TRIZ_FULL_AUDIT_TABLES_v0.1

## 1) Pipeline Truth Table (S01–S14)

| Step | Gate | Enforce level | Что проверяется фактически | Что блокирует дальше | Evidence |
|---|---|---|---|---|---|
| S01 | Gate1 | structural | owner_role, owner_scope, constraints | FAIL gate | `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/harness/gates_structural.py:42` |
| S02 | Gate2 | structural | actor/system/environment/boundary_note | FAIL gate | `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/harness/gates_structural.py:60` |
| S03 | Gate3 | structural | elements/flows/symptom_location | FAIL gate | `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/harness/gates_structural.py:77` |
| S04 | Gate4 | structural + assisted | structural fields + assisted criteria (если answers есть) | FAIL/BLOCKED | `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/harness/gates_structural.py:106`, `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/harness/harness.py:26`, `:121` |
| S05 | Gate5 | structural + assisted | ikr_1l + assisted | FAIL/BLOCKED | `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/harness/gates_structural.py:123` |
| S06 | Gate6 | structural + assisted | barrier_1l, equivalent_to_step4 + assisted | FAIL/BLOCKED | `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/harness/gates_structural.py:132` |
| S07 | Gate7 | structural | resources list + tied_to per resource | FAIL gate | `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/harness/gates_structural.py:143` |
| S08 | Gate8 | structural/formal | presence PRIMARY_FORM, BOUNDARY_CHECK, TRIZ_CORE, PRINCIPLES_TO_ACTION... | FAIL gate | `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/harness/gates_structural.py:166` |
| S08 | GateTRIZ | semantic (engine) | physical contradiction, separation, system operator, non-obviousness, transformation model | FAIL overall run | `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/harness/harness.py:431`, `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/TRIZ_CORE_ENGINE/validators.py:140` |
| S09 | Gate9 | structural/formal | concepts list exists and count >=3 | FAIL gate; later blocks Gate12 (with Gate11 fail logic) | `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/harness/gates_structural.py:187` |
| S10 | Gate10 | structural/formal | concept_specs exists and is list | FAIL gate | `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/harness/gates_structural.py:203` |
| S11 | Gate11 | structural + assisted | new_contradiction_exists + selection_criteria_refs contains contradiction/ikr/barrier + assisted | FAIL gate; blocks Gate12 | `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/harness/gates_structural.py:215` |
| S12 | Gate12 | structural + assisted | chosen_concept_index/name/reasons + assisted | FAIL gate or NOT_RUN | `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/harness/gates_structural.py:234` |
| S13 | Gate13 | structural | workstreams list exists | FAIL gate | `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/harness/gates_structural.py:244` |
| S14 | Gate14 | structural | required Rule Update fields | FAIL gate | `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/harness/gates_structural.py:256` |

Доп. блокировка:
- Gate12 недостижим при FAIL Gate9 или Gate11.  
Evidence: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/harness/gates_structural.py:301`

## 2) 9 forms vs pipeline usage

| Form | Canon definition present | Pipeline field mapping | Runtime enforcement | Actual usage status |
|---|---|---|---|---|
| №1 Дифференциация | Yes | `S08.PRIMARY_FORM` (string) | No mapping validation in code | Canon-only / declarative |
| №2 Динамизация | Yes | same | No | Canon-only / declarative |
| №3 Превенция | Yes | same | No | Canon-only / declarative |
| №4 Медиация | Yes | same | No | Canon-only / declarative |
| №5 Инверсия | Yes | `linked_form` appears in tests | Not validated semantically | Partially referenced in data |
| №6 Ресурсоэффективность | Yes | same | No | Canon-only / declarative |
| №7 Реформатирование | Yes | same | No | Canon-only / declarative |
| №8 Кибернетика | Yes | same | No | Canon-only / declarative |
| №9 Айкидо | Yes | same | No | Canon-only / declarative |

Primary evidence:
- Canon: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/canon/CANON_9FORMS_v1.1.docx`
- Gate8 structural only: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/harness/gates_structural.py:166-184`
- Example linked_form in data: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/tests/TC_DSS01.yaml:123`

## 3) principles_to_action vs enforcement depth

| Layer | Expected by docs | Enforced in code | Depth |
|---|---|---|---|
| `S08.PRINCIPLES_TO_ACTION.PRINCIPLES` | Principles tied to selected form PRIMARY | Non-empty presence only | Structural-only |
| `S08.PRINCIPLES_TO_ACTION.ACTIONS` | One action per selected principle | Non-empty presence only | Structural-only |
| Allowed-principles-by-form rule | Defined in CANON_9FORMS | Not checked | Not enforced |
| Principles as generator for S09/S10 | Policy R1 optional | Not enforced in runtime | Not enforced |

Evidence:
- Policy: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/governance/DSS_TRIZ_2_40_PRINCIPLES_ROLE_DECISION_v1.0.md`
- Runtime check: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/harness/gates_structural.py:172-177`

