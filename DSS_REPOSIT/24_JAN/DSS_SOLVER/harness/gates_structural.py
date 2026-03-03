from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List


@dataclass
class GateResult:
    gate: str
    status: str  # PASS | FAIL | BLOCKED | NOT_RUN | SOFT_FAIL | HARD_FAIL
    reasons: List[str]


CANONICAL_HARD_FAIL_MESSAGE = 'structural resolution not found'
CANONICAL_PFL_TERMINAL_MESSAGE = 'structural contradiction not formulated'
OPERATOR_SET = {'SEPARATION', 'MEDIATOR', 'LEVEL_SHIFT', 'DEPENDENCY_INVERSION'}
CONFLICT_TYPES = {'A', 'B', 'C', 'D'}
PFL_CONFLICT_TYPES = {'causal', 'temporal', 'interaction', 'scale'}
PFL_REASONS = {
    'NONE',
    'INVALID_DUAL_TENSION',
    'NO_MUTUAL_DEGRADATION',
    'OUT_OF_SCOPE',
    'SYMPTOM_FRAMING',
    'TRIVIAL_CONFLICT',
    'SOLUTION_AS_XY',
}
MAX_PFL_REFRAME_ATTEMPTS = 3


def _is_non_empty(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return value.strip() != ''
    if isinstance(value, list):
        return len(value) > 0
    if isinstance(value, dict):
        return len(value) > 0
    return True


def _is_operator_core_enabled(tc: Dict[str, Any]) -> bool:
    canon_versions = tc.get('canon_versions') or {}
    schema_value = str(canon_versions.get('schema') or '')
    if 'TEST_VECTOR_SCHEMA_v0.2' in schema_value:
        return True
    flag_value = tc.get('operator_core_enabled')
    if isinstance(flag_value, bool):
        return flag_value
    return False


def _schema_version_float(tc: Dict[str, Any]) -> float:
    raw = tc.get('schema_version')
    if raw is None:
        return 0.0
    try:
        return float(str(raw))
    except (ValueError, TypeError):
        return 0.0


def _is_pfl_enabled(tc: Dict[str, Any]) -> bool:
    flag_value = tc.get('pfl_enabled')
    if isinstance(flag_value, bool) and flag_value:
        return True
    if _schema_version_float(tc) >= 0.3:
        return True
    canon_versions = tc.get('canon_versions') or {}
    schema_value = str(canon_versions.get('schema') or '')
    if 'TEST_VECTOR_SCHEMA_v0.3' in schema_value:
        return True
    return False


def _contains_solution_action(text: str) -> bool:
    lowered = text.lower()
    action_markers = [
        'внедр',
        'запуст',
        'добав',
        'сдела',
        'ввести',
        'нанять',
        'подпис',
        'купить',
        'переехать',
        'принять решение',
    ]
    return any(marker in lowered for marker in action_markers)


def gate0_envelope(tc: Dict[str, Any]) -> GateResult:
    reasons = []
    if tc.get('status') != 'FILLED':
        reasons.append('status is not FILLED')
    if tc.get('mode') not in ('full_vector', 'artifact_pack'):
        reasons.append('mode is invalid')
    if not _is_non_empty(tc.get('canon_versions')):
        reasons.append('canon_versions missing')
    if tc.get('mode') == 'full_vector' and not _is_non_empty(tc.get('full_vector')):
        reasons.append('full_vector missing')
    if tc.get('mode') == 'artifact_pack' and not _is_non_empty(tc.get('artifact_pack')):
        reasons.append('artifact_pack missing')
    status = 'PASS' if not reasons else 'BLOCKED'
    return GateResult(gate='Gate0', status=status, reasons=reasons)


def gate1_case_owner(step_map: Dict[int, Dict[str, Any]]) -> GateResult:
    reasons = []
    s0 = step_map.get(0, {})
    s1 = step_map.get(1, {})

    if not _is_non_empty(s0.get('symptom_1l')):
        reasons.append('Step0.symptom_1l missing')
    if not _is_non_empty(s1.get('owner_role')):
        reasons.append('Step1.owner_role missing')
    if not _is_non_empty(s1.get('owner_scope')):
        reasons.append('Step1.owner_scope missing')
    if not _is_non_empty(s1.get('constraints')):
        reasons.append('Step1.constraints missing')

    status = 'PASS' if not reasons else 'FAIL'
    return GateResult(gate='Gate1', status=status, reasons=reasons)


def gate2_system_boundary(step_map: Dict[int, Dict[str, Any]]) -> GateResult:
    reasons = []
    s2 = step_map.get(2, {})

    if not _is_non_empty(s2.get('actor')):
        reasons.append('Step2.actor missing')
    if not _is_non_empty(s2.get('system')):
        reasons.append('Step2.system missing')
    if not _is_non_empty(s2.get('environment')):
        reasons.append('Step2.environment missing')
    if not _is_non_empty(s2.get('boundary_note_1l')):
        reasons.append('Step2.boundary_note_1l missing')

    status = 'PASS' if not reasons else 'FAIL'
    return GateResult(gate='Gate2', status=status, reasons=reasons)


def gate3_interaction(step_map: Dict[int, Dict[str, Any]]) -> GateResult:
    reasons = []
    s3 = step_map.get(3, {})

    if not _is_non_empty(s3.get('elements')):
        reasons.append('Step3.elements missing')
    if not _is_non_empty(s3.get('flows')):
        reasons.append('Step3.flows missing')
    if not _is_non_empty(s3.get('symptom_location')):
        reasons.append('Step3.symptom_location missing')

    flows = s3.get('flows') or []
    for idx, flow in enumerate(flows):
        if not isinstance(flow, dict):
            reasons.append(f'Step3.flows[{idx}] not a dict')
            continue
        if not _is_non_empty(flow.get('from')):
            reasons.append(f'Step3.flows[{idx}].from missing')
        if not _is_non_empty(flow.get('to')):
            reasons.append(f'Step3.flows[{idx}].to missing')
        if not _is_non_empty(flow.get('type')):
            reasons.append(f'Step3.flows[{idx}].type missing')
        if not _is_non_empty(flow.get('note')):
            reasons.append(f'Step3.flows[{idx}].note missing')

    status = 'PASS' if not reasons else 'FAIL'
    return GateResult(gate='Gate3', status=status, reasons=reasons)




def _slots_v0_to_display(slots: dict, axis: str):
    """Assemble conservative display string from slots_v0."""
    if not isinstance(slots, dict):
        return None
    d = slots.get(f"{axis}_direction")
    m = slots.get(f"{axis}_metric")
    o = slots.get(f"{axis}_object")
    parts = [p for p in [d, m, o] if p]
    return " ".join(parts) if parts else None

def gatepfl_problem_framing(tc: Dict[str, Any], step_map: Dict[int, Dict[str, Any]]) -> GateResult:
    _ = step_map  # Reserved for future deterministic checks against S01-S03 payload.
    reasons = []
    phase0_enabled = bool(tc.get('phase0_enabled'))
    if phase0_enabled:
        slots_v0 = tc.get('canonical_slots_v0')
        x_value = str(_slots_v0_to_display(slots_v0, 'X') or '').strip()
        y_value = str(_slots_v0_to_display(slots_v0, 'Y') or '').strip()
        conflict_type = str(tc.get('canonical_conflict_type_candidate') or '').lower()
        if not x_value or not y_value:
            return GateResult(gate='GatePFL', status='FAIL', reasons=['MISSING_SLOTS_V0'])
    else:
        x_value = str(tc.get('pfl_X') or '').strip()
        y_value = str(tc.get('pfl_Y') or '').strip()
        conflict_type = str(tc.get('pfl_conflict_type_candidate') or '').lower()
    verdict = str(tc.get('pfl_verdict') or '').upper()
    pfl_reason = str(tc.get('pfl_reason') or '').upper()
    structural_tension = tc.get('pfl_structural_tension')
    attempt_index = tc.get('pfl_attempt_index')

    if not _is_non_empty(x_value):
        reasons.append('pfl_X missing')
    if not _is_non_empty(y_value):
        reasons.append('pfl_Y missing')
    if verdict not in {'PASS', 'FAIL'}:
        reasons.append('pfl_verdict invalid')
    if pfl_reason not in PFL_REASONS:
        reasons.append('pfl_reason invalid')
    if conflict_type not in PFL_CONFLICT_TYPES:
        reasons.append('pfl_conflict_type_candidate invalid')
    if structural_tension is None:
        reasons.append('pfl_structural_tension missing')
    if attempt_index is None:
        reasons.append('pfl_attempt_index missing')
    else:
        try:
            attempt_index = int(attempt_index)
            if attempt_index < 1 or attempt_index > MAX_PFL_REFRAME_ATTEMPTS:
                reasons.append('pfl_attempt_index out of range')
        except (ValueError, TypeError):
            reasons.append('pfl_attempt_index invalid')
            attempt_index = None

    if reasons:
        return GateResult(gate='GatePFL', status='FAIL', reasons=reasons)

    # SOLUTION_AS_XY deterministic detection.
    if _contains_solution_action(x_value) or _contains_solution_action(y_value):
        return GateResult(gate='GatePFL', status='FAIL', reasons=['SOLUTION_AS_XY'])

    if verdict == 'PASS':
        if pfl_reason != 'NONE':
            return GateResult(gate='GatePFL', status='FAIL', reasons=['pfl_reason must be NONE when pfl_verdict=PASS'])
        if structural_tension is not True:
            return GateResult(gate='GatePFL', status='FAIL', reasons=['pfl_structural_tension must be true when pfl_verdict=PASS'])
        return GateResult(gate='GatePFL', status='PASS', reasons=[])

    # verdict == FAIL
    if attempt_index == MAX_PFL_REFRAME_ATTEMPTS:
        return GateResult(gate='GatePFL', status='FAIL', reasons=[CANONICAL_PFL_TERMINAL_MESSAGE])
    return GateResult(gate='GatePFL', status='FAIL', reasons=[pfl_reason])


def gate4_contradiction(step_map: Dict[int, Dict[str, Any]]) -> GateResult:
    reasons = []
    s4 = step_map.get(4, {})

    if not _is_non_empty(s4.get('improve_x')):
        reasons.append('Step4.improve_x missing')
    if not _is_non_empty(s4.get('worsen_y')):
        reasons.append('Step4.worsen_y missing')
    if not _is_non_empty(s4.get('statement_1l')):
        reasons.append('Step4.statement_1l missing')
    if not _is_non_empty(s4.get('measurement_hint')):
        reasons.append('Step4.measurement_hint missing')

    status = 'PASS' if not reasons else 'FAIL'
    return GateResult(gate='Gate4', status=status, reasons=reasons)


def gate5_ikr(step_map: Dict[int, Dict[str, Any]]) -> GateResult:
    reasons = []
    s5 = step_map.get(5, {})
    if not _is_non_empty(s5.get('ikr_1l')):
        reasons.append('Step5.ikr_1l missing')
    status = 'PASS' if not reasons else 'FAIL'
    return GateResult(gate='Gate5', status=status, reasons=reasons)


def gate6_hard_barrier(step_map: Dict[int, Dict[str, Any]]) -> GateResult:
    reasons = []
    s6 = step_map.get(6, {})
    if not _is_non_empty(s6.get('barrier_1l')):
        reasons.append('Step6.barrier_1l missing')
    if s6.get('equivalent_to_step4') is None:
        reasons.append('Step6.equivalent_to_step4 missing')
    status = 'PASS' if not reasons else 'FAIL'
    return GateResult(gate='Gate6', status=status, reasons=reasons)


def gate7_resource_map(step_map: Dict[int, Dict[str, Any]]) -> GateResult:
    reasons = []
    s7 = step_map.get(7, {})
    resources = s7.get('resources')
    if not _is_non_empty(resources):
        reasons.append('Step7.resources missing')
    elif not isinstance(resources, list):
        reasons.append('Step7.resources is not a list')
    else:
        for idx, res in enumerate(resources):
            if not isinstance(res, dict):
                reasons.append(f'Step7.resources[{idx}] not a dict')
                continue
            if not _is_non_empty(res.get('name')):
                reasons.append(f'Step7.resources[{idx}].name missing')
            if not _is_non_empty(res.get('category')):
                reasons.append(f'Step7.resources[{idx}].category missing')
            if not _is_non_empty(res.get('tied_to')):
                reasons.append(f'Step7.resources[{idx}].tied_to missing')
    status = 'PASS' if not reasons else 'FAIL'
    return GateResult(gate='Gate7', status=status, reasons=reasons)


def gate8_form_selection(step_map: Dict[int, Dict[str, Any]]) -> GateResult:
    reasons = []
    s8 = step_map.get(8, {})
    for key in ('PRIMARY_FORM', 'BOUNDARY_CHECK', 'TRIZ_CORE', 'PRINCIPLES_TO_ACTION', 'IKR_TEST', 'CONFIDENCE'):
        if not _is_non_empty(s8.get(key)):
            reasons.append(f'Step8.{key} missing')
    pta = s8.get('PRINCIPLES_TO_ACTION', {})
    if isinstance(pta, dict):
        if not _is_non_empty(pta.get('PRINCIPLES')):
            reasons.append('Step8.PRINCIPLES_TO_ACTION.PRINCIPLES missing')
        if not _is_non_empty(pta.get('ACTIONS')):
            reasons.append('Step8.PRINCIPLES_TO_ACTION.ACTIONS missing')
    triz = s8.get('TRIZ_CORE', {})
    if isinstance(triz, dict):
        for key in ('physical_contradiction', 'separation', 'system_operator', 'transformation_model', 'non_obviousness_check'):
            if not _is_non_empty(triz.get(key)):
                reasons.append(f'Step8.TRIZ_CORE.{key} missing')
    status = 'PASS' if not reasons else 'FAIL'
    return GateResult(gate='Gate8', status=status, reasons=reasons)


def gatecr_operator_core(tc: Dict[str, Any], step_map: Dict[int, Dict[str, Any]]) -> GateResult:
    s85 = step_map.get(85, {})
    hard_fail_reasons = []
    soft_fail_reasons = []
    risk_shift_detected = False

    operator_selected = s85.get('operator_selected')
    if operator_selected not in OPERATOR_SET:
        hard_fail_reasons.append('Step8_5.operator_selected invalid or missing')

    detected_types = s85.get('detected_conflict_types')
    if not isinstance(detected_types, list) or len(detected_types) == 0:
        hard_fail_reasons.append('Step8_5.detected_conflict_types missing')
        detected_set = set()
    else:
        detected_set = set(str(x) for x in detected_types)
        invalid_types = [x for x in detected_set if x not in CONFLICT_TYPES]
        if invalid_types:
            hard_fail_reasons.append(f'Step8_5.detected_conflict_types contains invalid values: {sorted(invalid_types)}')

    dominant_type = s85.get('dominant_conflict_type')
    if str(dominant_type) not in CONFLICT_TYPES:
        hard_fail_reasons.append('Step8_5.dominant_conflict_type invalid or missing')
    elif detected_set and str(dominant_type) not in detected_set:
        hard_fail_reasons.append('Step8_5.dominant_conflict_type is not in detected_conflict_types')

    if not _is_non_empty(s85.get('transformed_conflict_frame')):
        hard_fail_reasons.append('Step8_5.transformed_conflict_frame missing')
    if not _is_non_empty(s85.get('what_changed_structurally')):
        hard_fail_reasons.append('Step8_5.what_changed_structurally missing')

    separation_illusion_test = s85.get('separation_illusion_test')
    if separation_illusion_test is None:
        hard_fail_reasons.append('Step8_5.separation_illusion_test missing')
    elif bool(separation_illusion_test):
        # Deterministic owner lock: any YES => HARD_FAIL.
        return GateResult(gate='GateCR', status='HARD_FAIL', reasons=[CANONICAL_HARD_FAIL_MESSAGE])

    assisted_matrix = s85.get('assisted_matrix')
    if not isinstance(assisted_matrix, list) or len(assisted_matrix) == 0:
        soft_fail_reasons.append('Step8_5.assisted_matrix missing')
    elif len(assisted_matrix) < 5:
        soft_fail_reasons.append('Step8_5.assisted_matrix has fewer than 5 checks')
    else:
        matrix_invalid = False
        matrix_has_no = False
        for idx, item in enumerate(assisted_matrix):
            if not isinstance(item, dict):
                matrix_invalid = True
                soft_fail_reasons.append(f'Step8_5.assisted_matrix[{idx}] is not a dict')
                continue
            if not _is_non_empty(item.get('question_id')):
                matrix_invalid = True
                soft_fail_reasons.append(f'Step8_5.assisted_matrix[{idx}].question_id missing')
            answer = str(item.get('answer') or '').upper()
            if answer not in {'YES', 'NO'}:
                matrix_invalid = True
                soft_fail_reasons.append(f'Step8_5.assisted_matrix[{idx}].answer invalid')
            elif answer == 'NO':
                matrix_has_no = True
        if matrix_invalid:
            soft_fail_reasons.append('Step8_5.assisted_matrix malformed')
        elif matrix_has_no:
            soft_fail_reasons.append('Step8_5.assisted_matrix contains NO')

    structural_resolution_confirmed = s85.get('structural_resolution_confirmed')
    if structural_resolution_confirmed is None:
        soft_fail_reasons.append('Step8_5.structural_resolution_confirmed missing')
    elif structural_resolution_confirmed is False:
        soft_fail_reasons.append('Step8_5.structural_resolution_confirmed=false')

    # E17 integrity policy: deterministic search-loop enforcement for schema_version >= 0.4.
    schema_version = _schema_version_float(tc)
    if schema_version >= 0.4:
        search_loop = s85.get('search_loop')
        if not isinstance(search_loop, bool):
            soft_fail_reasons.append('Step8_5.search_loop missing or invalid for schema_version>=0.4')
        elif search_loop is True:
            risk_shift_detected = True
            soft_fail_reasons.append('risk_shift_detected=true (search_loop=true)')

    if hard_fail_reasons:
        return GateResult(gate='GateCR', status='HARD_FAIL', reasons=[CANONICAL_HARD_FAIL_MESSAGE])
    if soft_fail_reasons:
        return GateResult(gate='GateCR', status='SOFT_FAIL', reasons=soft_fail_reasons)
    return GateResult(gate='GateCR', status='PASS', reasons=[])


def gate9_solution_set(step_map: Dict[int, Dict[str, Any]]) -> GateResult:
    reasons = []
    s9 = step_map.get(9, {})
    if not _is_non_empty(s9.get('count_rule')):
        reasons.append('Step9.count_rule missing')
    concepts = s9.get('concepts')
    if not _is_non_empty(concepts):
        reasons.append('Step9.concepts missing')
    elif not isinstance(concepts, list):
        reasons.append('Step9.concepts is not a list')
    elif len(concepts) < 3:
        reasons.append('Step9.concepts count < 3')
    status = 'PASS' if not reasons else 'FAIL'
    return GateResult(gate='Gate9', status=status, reasons=reasons)


def gate10_mechanism_specs(step_map: Dict[int, Dict[str, Any]]) -> GateResult:
    reasons = []
    s10 = step_map.get(10, {})
    specs = s10.get('concept_specs')
    if not _is_non_empty(specs):
        reasons.append('Step10.concept_specs missing')
    elif not isinstance(specs, list):
        reasons.append('Step10.concept_specs is not a list')
    status = 'PASS' if not reasons else 'FAIL'
    return GateResult(gate='Gate10', status=status, reasons=reasons)


def gate11_secondary_contradiction(step_map: Dict[int, Dict[str, Any]]) -> GateResult:
    reasons = []
    s11 = step_map.get(11, {})
    if s11.get('new_contradiction_exists') is None:
        reasons.append('Step11.new_contradiction_exists missing')
    criteria_refs = s11.get('selection_criteria_refs')
    if not _is_non_empty(criteria_refs):
        reasons.append('Step11.selection_criteria_refs missing')
    elif not isinstance(criteria_refs, list):
        reasons.append('Step11.selection_criteria_refs is not a list')
    else:
        required = {'contradiction', 'ikr', 'barrier'}
        missing = required - {str(x).lower() for x in criteria_refs}
        if missing:
            reasons.append(f'Step11.selection_criteria_refs missing required refs: {sorted(missing)}')
    status = 'PASS' if not reasons else 'FAIL'
    return GateResult(gate='Gate11', status=status, reasons=reasons)


def gate12_decision_record(
    step_map: Dict[int, Dict[str, Any]],
    gatecr_status: str | None = None,
    operator_core_enabled: bool = False,
) -> GateResult:
    reasons = []
    s12 = step_map.get(12, {})
    for key in ('chosen_concept_index', 'chosen_concept_name', 'reasons'):
        if not _is_non_empty(s12.get(key)):
            reasons.append(f'Step12.{key} missing')
    if operator_core_enabled and gatecr_status == 'SOFT_FAIL':
        if s12.get('compromise_mode') is not True:
            reasons.append('Step12.compromise_mode must be true when GateCR=SOFT_FAIL')
    status = 'PASS' if not reasons else 'FAIL'
    return GateResult(gate='Gate12', status=status, reasons=reasons)


def gate13_implementation_map(step_map: Dict[int, Dict[str, Any]]) -> GateResult:
    reasons = []
    s13 = step_map.get(13, {})
    workstreams = s13.get('workstreams')
    if not _is_non_empty(workstreams):
        reasons.append('Step13.workstreams missing')
    elif not isinstance(workstreams, list):
        reasons.append('Step13.workstreams is not a list')
    status = 'PASS' if not reasons else 'FAIL'
    return GateResult(gate='Gate13', status=status, reasons=reasons)


def gate14_rule_update(step_map: Dict[int, Dict[str, Any]]) -> GateResult:
    reasons = []
    s14 = step_map.get(14, {})
    required = [
        'rule_id',
        'rule_statement_if_then',
        'criterion',
        'boundaries',
        'evidence_from_case',
        'test_case_action',
        'version_note',
        'rationale_1l',
    ]
    for key in required:
        if not _is_non_empty(s14.get(key)):
            reasons.append(f'Step14.{key} missing')
    status = 'PASS' if not reasons else 'FAIL'
    return GateResult(gate='Gate14', status=status, reasons=reasons)


def run_structural_gates(tc: Dict[str, Any], step_map: Dict[int, Dict[str, Any]]) -> List[GateResult]:
    results = [gate0_envelope(tc)]

    if results[0].status == 'BLOCKED':
        for g in range(1, 15):
            results.append(GateResult(gate=f'Gate{g}', status='NOT_RUN', reasons=['Gate0 blocked']))
        return results

    operator_core_enabled = _is_operator_core_enabled(tc)

    results.extend([
        gate1_case_owner(step_map),
        gate2_system_boundary(step_map),
        gate3_interaction(step_map),
    ])

    if tc.get('phase0_enabled') is True:
        phase0_verdict = str(tc.get('phase0_verdict') or '').upper()
        phase0_reason = str(tc.get('phase0_reason_code') or 'OTHER')
        if phase0_verdict == 'PASS':
            results.append(GateResult(gate='GatePhase0', status='PASS', reasons=[]))
        else:
            results.append(GateResult(gate='GatePhase0', status='FAIL', reasons=[phase0_reason]))
            results.append(GateResult(gate='GatePFL', status='NOT_RUN', reasons=[phase0_reason]))
            for g in range(4, 15):
                results.append(GateResult(gate=f'Gate{g}', status='NOT_RUN', reasons=[phase0_reason]))
            return results
    else:
        results.append(GateResult(gate='GatePhase0', status='NOT_RUN', reasons=['Phase0 disabled (historical compatibility)']))

    if _is_pfl_enabled(tc):
        gatepfl = gatepfl_problem_framing(tc, step_map)
        results.append(gatepfl)
        if gatepfl.status == 'FAIL':
            reason = gatepfl.reasons[0] if gatepfl.reasons else 'GatePFL failed'
            for g in range(4, 15):
                results.append(GateResult(gate=f'Gate{g}', status='NOT_RUN', reasons=[reason]))
            return results
    else:
        results.append(GateResult(gate='GatePFL', status='NOT_RUN', reasons=['PFL disabled (historical compatibility)']))

    results.extend([
        gate4_contradiction(step_map),
        gate5_ikr(step_map),
        gate6_hard_barrier(step_map),
        gate7_resource_map(step_map),
        gate8_form_selection(step_map),
    ])

    gatecr_status: str | None = None
    if operator_core_enabled:
        gatecr = gatecr_operator_core(tc, step_map)
        gatecr_status = gatecr.status
        results.append(gatecr)
        if gatecr.status == 'HARD_FAIL':
            for g in range(9, 15):
                results.append(GateResult(gate=f'Gate{g}', status='NOT_RUN', reasons=[CANONICAL_HARD_FAIL_MESSAGE]))
            return results

    results.extend([
        gate9_solution_set(step_map),
        gate10_mechanism_specs(step_map),
        gate11_secondary_contradiction(step_map),
        gate12_decision_record(step_map, gatecr_status=gatecr_status, operator_core_enabled=operator_core_enabled),
        gate13_implementation_map(step_map),
        gate14_rule_update(step_map),
    ])

    # Enforce: Gate12 unreachable if Gate9 or Gate11 fail
    gate9 = next((g for g in results if g.gate == 'Gate9'), None)
    gate11 = next((g for g in results if g.gate == 'Gate11'), None)
    if (gate9 and gate9.status == 'FAIL') or (gate11 and gate11.status == 'FAIL'):
        for g in results:
            if g.gate == 'Gate12':
                g.status = 'NOT_RUN'
                g.reasons = ['Gate12 blocked due to Gate9/Gate11 FAIL']
                break

    return results
