# CURRENT_PIPELINE_MAP

## S04–S12 (as-is)

| Step | Artifact (expected) | Step definition source | Gate | Gate implementation source | Enforcement mode |
|---|---|---|---|---|---|
| S04 | `CONTRADICTION_STATEMENT` | `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/canon/CANON_PIPELINE_v1.2.docx` | Gate4 | `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/harness/gates_structural.py` (`gate4_contradiction`) | structural + assisted (`Gate4` in semantic answers) |
| S05 | `IKR_CARD` | same canon | Gate5 | `gates_structural.py` (`gate5_ikr`) | structural + assisted |
| S06 | `HARD_BARRIER` | same canon | Gate6 | `gates_structural.py` (`gate6_hard_barrier`) | structural + assisted |
| S07 | `RESOURCE_MAP` | same canon | Gate7 | `gates_structural.py` (`gate7_resource_map`) | structural |
| S08 | `FORM_SELECTION` (+ `TRIZ_CORE`, `PRINCIPLES_TO_ACTION`) | same canon + `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/canon/CANON_9FORMS_v1.1.docx` | Gate8 + GateTRIZ | `gates_structural.py` (`gate8_form_selection`) + `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/TRIZ_CORE_ENGINE/validators.py` via `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/harness/harness.py` (`triz_validate`) | Gate8 structural, GateTRIZ semantic validator |
| S09 | `SOLUTION_SET` | `CANON_PIPELINE_v1.2.docx` | Gate9 | `gates_structural.py` (`gate9_solution_set`) | structural (count/list) |
| S10 | `MECHANISM_SPECS` | `CANON_PIPELINE_v1.2.docx` | Gate10 | `gates_structural.py` (`gate10_mechanism_specs`) | structural (presence/list) |
| S11 | `SECONDARY_CONTRADICTION_CHECK` | `CANON_PIPELINE_v1.2.docx` | Gate11 | `gates_structural.py` (`gate11_secondary_contradiction`) | structural + assisted |
| S12 | `DECISION_RECORD` | `CANON_PIPELINE_v1.2.docx` | Gate12 | `gates_structural.py` (`gate12_decision_record`) | structural + assisted |

## Where mechanism is first formed
- First explicit mechanism artifact appears at **S10** (`concept_specs`).
- Current runtime checks only require `concept_specs` to exist and be a list.
- Sources:
  - `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/harness/gates_structural.py` (`gate10_mechanism_specs`)
  - `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/harness/harness.py` (`_export_package` writes `S10_MECHANISM_SPECS/*`)
