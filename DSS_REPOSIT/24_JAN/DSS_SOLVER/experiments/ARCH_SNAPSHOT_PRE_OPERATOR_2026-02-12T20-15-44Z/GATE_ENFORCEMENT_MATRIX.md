# GATE_ENFORCEMENT_MATRIX

## Active gates (runtime)

| Gate | PASS/FAIL basis (runtime) | Mandatory artifact fields (runtime) | Cross-step dependency |
|---|---|---|---|
| Gate0 | Envelope validity; mode/status/full_vector presence | `status`, `mode`, `canon_versions`, `full_vector`/`artifact_pack` | Blocks all gates if BLOCKED |
| Gate1 | owner fields present | `step_1.owner_role`, `owner_scope`, `constraints`; plus `step_0.symptom_1l` | S0->S1 consistency |
| Gate2 | system boundary fields present | `step_2.actor/system/environment/boundary_note_1l` | From S1 to S2 |
| Gate3 | interaction map present | `step_3.elements/flows/symptom_location` | Uses boundary model |
| Gate4 | contradiction fields present + assisted criteria status | `step_4.improve_x/worsen_y/statement_1l/measurement_hint` | Inputs for S5/S6/S11 refs |
| Gate5 | IKR present + assisted criteria | `step_5.ikr_1l` | Referenced later in Gate11 refs |
| Gate6 | barrier present + equivalence flag + assisted criteria | `step_6.barrier_1l`, `equivalent_to_step4` | Referenced later in Gate11 refs |
| Gate7 | resource list structure | `step_7.resources[*].name/category/tied_to` | Inputs for S8/S9 traceability |
| Gate8 | S08 form/TRIZ fields structurally present | `PRIMARY_FORM`, `BOUNDARY_CHECK`, `TRIZ_CORE`, `PRINCIPLES_TO_ACTION`, `IKR_TEST`, `CONFIDENCE` | Feeds GateTRIZ + S09 |
| Gate9 | concepts list exists and count >= 3 | `step_9.count_rule`, `step_9.concepts` | Blocks Gate12 on FAIL |
| Gate10 | mechanism specs exist as list | `step_10.concept_specs` | Feeds S11/S12 rationale |
| Gate11 | secondary check + mandatory refs + assisted criteria | `step_11.new_contradiction_exists`, `selection_criteria_refs` incl. `contradiction/ikr/barrier` | Blocks Gate12 on FAIL |
| Gate12 | decision fields present + assisted criteria | `step_12.chosen_concept_index`, `chosen_concept_name`, `reasons` | Not run if Gate9/11 fail |
| Gate13 | implementation map list present | `step_13.workstreams` | post-decision |
| Gate14 | rule update fields present | `step_14.rule_id`, `rule_statement_if_then`, `criterion`, `boundaries`, `evidence_from_case`, `test_case_action`, `version_note`, `rationale_1l` | finalization |
| GateTRIZ | TRIZ core validator returns VALID | `step_8.TRIZ_CORE.physical_contradiction/separation/system_operator/transformation_model/non_obviousness_check` | Mandatory run-level validity |

## Sources
- Structural gates: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/harness/gates_structural.py`
- Orchestration and GateTRIZ insertion: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/harness/harness.py`
- TRIZ validator logic: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/TRIZ_CORE_ENGINE/validators.py`
