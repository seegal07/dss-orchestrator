# PIPELINE_LINK_GRAPH

## Text graph (S04..S14 + S08.5/GateCR)
- S04 -> Gate4 (`harness/gates_structural.py::gate4_contradiction`)
- S05 -> Gate5 (`gate5_ikr`)
- S06 -> Gate6 (`gate6_hard_barrier`)
- S07 -> Gate7 (`gate7_resource_map`)
- S08 -> Gate8 (`gate8_form_selection`)
- S08.5 -> GateCR (`gatecr_operator_core`) [only if Operator Core enabled]
- GateCR=HARD_FAIL -> S09..S14 => NOT_RUN (canonical reason)
- GateCR=PASS or SOFT_FAIL -> S09 -> Gate9
- S10 -> Gate10
- S11 -> Gate11
- S12 -> Gate12 (plus `compromise_mode=true` requirement if GateCR=SOFT_FAIL)
- S13 -> Gate13
- S14 -> Gate14
- After structural chain -> GateTRIZ (TRIZ core engine validation in `TRIZ_CORE_ENGINE/api.py`)

## Step driver mapping (spec/template pointers)
- S04..S08: mostly legacy/full_vector schema fields in test vectors.
- S08.5: `governance/TEST_VECTOR_SCHEMA_v0.2.md` + templates in `templates/operator_core/`.
- S09..S14: full_vector fields + decision record conventions in `governance/DSS_DECISION_RECORD_SPEC_v0.2.md`.

## Gate implementation modules
- Gate0..Gate14, GateCR: `harness/gates_structural.py`
- GateTRIZ: `TRIZ_CORE_ENGINE/validators.py` via `TRIZ_CORE_ENGINE/api.py`
- Gate15..Gate18 (addon): assembled in `harness/harness.py` from semantic answers.
