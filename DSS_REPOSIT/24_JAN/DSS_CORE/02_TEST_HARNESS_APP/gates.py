"""Gate checks for DSS_TRIZ_Business (MVP: Gate0–Gate3).

Extend this file to implement Gate4–Gate14.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List


@dataclass
class GateResult:
    gate: str
    status: str  # PASS | FAIL | BLOCKED
    reasons: List[str]


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


def gate0_envelope(tc: Dict[str, Any]) -> GateResult:
    reasons = []
    if tc.get('status') != 'FILLED':
        reasons.append("status is not FILLED")
    if tc.get('mode') not in ('artifact_pack', 'full_vector'):
        reasons.append("mode is invalid")
    if not _is_non_empty(tc.get('canon_versions')):
        reasons.append("canon_versions missing")
    if not _is_non_empty(tc.get('artifact_pack')):
        reasons.append("artifact_pack missing")
    status = 'PASS' if not reasons else 'BLOCKED'
    return GateResult(gate='Gate0', status=status, reasons=reasons)


def gate1_case_owner(tc: Dict[str, Any], step_map: Dict[int, Dict[str, Any]]) -> GateResult:
    reasons = []
    step0 = step_map.get(0, {})
    step1 = step_map.get(1, {})

    s0 = step0.get('payload', {}) if step0 else {}
    s1 = step1.get('payload', {}) if step1 else {}

    if not _is_non_empty(s0.get('symptom_1l')):
        reasons.append("Step0.symptom_1l missing")
    if not _is_non_empty(s1.get('owner_role')):
        reasons.append("Step1.owner_role missing")
    if not _is_non_empty(s1.get('owner_scope')):
        reasons.append("Step1.owner_scope missing")
    if not _is_non_empty(s1.get('constraints')):
        reasons.append("Step1.constraints missing")

    status = 'PASS' if not reasons else 'FAIL'
    return GateResult(gate='Gate1', status=status, reasons=reasons)


def gate2_system_boundary(step_map: Dict[int, Dict[str, Any]]) -> GateResult:
    reasons = []
    step2 = step_map.get(2, {})
    s2 = step2.get('payload', {}) if step2 else {}

    if not _is_non_empty(s2.get('actor')):
        reasons.append("Step2.actor missing")
    if not _is_non_empty(s2.get('system')):
        reasons.append("Step2.system missing")
    if not _is_non_empty(s2.get('environment')):
        reasons.append("Step2.environment missing")
    if not _is_non_empty(s2.get('boundary_note_1l')):
        reasons.append("Step2.boundary_note_1l missing")

    status = 'PASS' if not reasons else 'FAIL'
    return GateResult(gate='Gate2', status=status, reasons=reasons)


def gate3_interaction(step_map: Dict[int, Dict[str, Any]]) -> GateResult:
    reasons = []
    step3 = step_map.get(3, {})
    s3 = step3.get('payload', {}) if step3 else {}

    if not _is_non_empty(s3.get('elements')):
        reasons.append("Step3.elements missing")
    if not _is_non_empty(s3.get('flows')):
        reasons.append("Step3.flows missing")
    if not _is_non_empty(s3.get('symptom_location')):
        reasons.append("Step3.symptom_location missing")

    # Basic flow shape check
    flows = s3.get('flows') or []
    for idx, flow in enumerate(flows):
        if not isinstance(flow, dict):
            reasons.append(f"Step3.flows[{idx}] not a dict")
            continue
        if not _is_non_empty(flow.get('from')):
            reasons.append(f"Step3.flows[{idx}].from missing")
        if not _is_non_empty(flow.get('to')):
            reasons.append(f"Step3.flows[{idx}].to missing")
        if not _is_non_empty(flow.get('type')):
            reasons.append(f"Step3.flows[{idx}].type missing")
        if not _is_non_empty(flow.get('note')):
            reasons.append(f"Step3.flows[{idx}].note missing")

    status = 'PASS' if not reasons else 'FAIL'
    return GateResult(gate='Gate3', status=status, reasons=reasons)


def gate4_contradiction(step_map: Dict[int, Dict[str, Any]]) -> GateResult:
    reasons = []
    step4 = step_map.get(4, {})
    s4 = step4.get('payload', {}) if step4 else {}

    if not _is_non_empty(s4.get('improve_x')):
        reasons.append("Step4.improve_x missing")
    if not _is_non_empty(s4.get('worsen_y')):
        reasons.append("Step4.worsen_y missing")
    if not _is_non_empty(s4.get('statement_1l')):
        reasons.append("Step4.statement_1l missing")
    if not _is_non_empty(s4.get('measurement_hint')):
        reasons.append("Step4.measurement_hint missing")

    status = 'PASS' if not reasons else 'FAIL'
    return GateResult(gate='Gate4', status=status, reasons=reasons)


def gate5_ikr(step_map: Dict[int, Dict[str, Any]]) -> GateResult:
    reasons = []
    step5 = step_map.get(5, {})
    s5 = step5.get('payload', {}) if step5 else {}

    if not _is_non_empty(s5.get('ikr_1l')):
        reasons.append("Step5.ikr_1l missing")

    status = 'PASS' if not reasons else 'FAIL'
    return GateResult(gate='Gate5', status=status, reasons=reasons)


def gate6_hard_barrier(step_map: Dict[int, Dict[str, Any]]) -> GateResult:
    reasons = []
    step6 = step_map.get(6, {})
    s6 = step6.get('payload', {}) if step6 else {}

    if not _is_non_empty(s6.get('barrier_1l')):
        reasons.append("Step6.barrier_1l missing")
    if s6.get('equivalent_to_step4') is None:
        reasons.append("Step6.equivalent_to_step4 missing")

    status = 'PASS' if not reasons else 'FAIL'
    return GateResult(gate='Gate6', status=status, reasons=reasons)

def gate7_resource_map(step_map: Dict[int, Dict[str, Any]]) -> GateResult:
    reasons = []
    step7 = step_map.get(7, {})
    s7 = step7.get('payload', {}) if step7 else {}

    resources = s7.get('resources')
    if not _is_non_empty(resources):
        reasons.append("Step7.resources missing")
    elif not isinstance(resources, list):
        reasons.append("Step7.resources is not a list")
    else:
        for idx, res in enumerate(resources):
            if not isinstance(res, dict):
                reasons.append(f"Step7.resources[{idx}] not a dict")
                continue
            if not _is_non_empty(res.get('name')):
                reasons.append(f"Step7.resources[{idx}].name missing")
            if not _is_non_empty(res.get('category')):
                reasons.append(f"Step7.resources[{idx}].category missing")
            if not _is_non_empty(res.get('tied_to')):
                reasons.append(f"Step7.resources[{idx}].tied_to missing")

    status = 'PASS' if not reasons else 'FAIL'
    return GateResult(gate='Gate7', status=status, reasons=reasons)

def gate8_form_selection(step_map: Dict[int, Dict[str, Any]]) -> GateResult:
    reasons = []
    step8 = step_map.get(8, {})
    s8 = step8.get('payload', {}) if step8 else {}

    if not _is_non_empty(s8.get('PRIMARY_FORM')):
        reasons.append("Step8.PRIMARY_FORM missing")
    if not _is_non_empty(s8.get('BOUNDARY_CHECK')):
        reasons.append("Step8.BOUNDARY_CHECK missing")
    if not _is_non_empty(s8.get('TRIZ_CORE')):
        reasons.append("Step8.TRIZ_CORE missing")
    if not _is_non_empty(s8.get('PRINCIPLES_TO_ACTION')):
        reasons.append("Step8.PRINCIPLES_TO_ACTION missing")
    if not _is_non_empty(s8.get('IKR_TEST')):
        reasons.append("Step8.IKR_TEST missing")
    if not _is_non_empty(s8.get('CONFIDENCE')):
        reasons.append("Step8.CONFIDENCE missing")

    # Minimal internal checks
    pta = s8.get('PRINCIPLES_TO_ACTION', {})
    if isinstance(pta, dict):
        if not _is_non_empty(pta.get('PRINCIPLES')):
            reasons.append("Step8.PRINCIPLES_TO_ACTION.PRINCIPLES missing")
        if not _is_non_empty(pta.get('ACTIONS')):
            reasons.append("Step8.PRINCIPLES_TO_ACTION.ACTIONS missing")

    status = 'PASS' if not reasons else 'FAIL'
    return GateResult(gate='Gate8', status=status, reasons=reasons)

def gate9_solution_set(step_map: Dict[int, Dict[str, Any]]) -> GateResult:
    reasons = []
    step9 = step_map.get(9, {})
    s9 = step9.get('payload', {}) if step9 else {}

    if not _is_non_empty(s9.get('count_rule')):
        reasons.append("Step9.count_rule missing")
    concepts = s9.get('concepts')
    if not _is_non_empty(concepts):
        reasons.append("Step9.concepts missing")
    elif not isinstance(concepts, list):
        reasons.append("Step9.concepts is not a list")
    else:
        for idx, c in enumerate(concepts):
            if not isinstance(c, dict):
                reasons.append(f"Step9.concepts[{idx}] not a dict")
                continue
            if not _is_non_empty(c.get('concept_index')):
                reasons.append(f"Step9.concepts[{idx}].concept_index missing")
            if not _is_non_empty(c.get('name')):
                reasons.append(f"Step9.concepts[{idx}].name missing")
            if not _is_non_empty(c.get('idea_1l')):
                reasons.append(f"Step9.concepts[{idx}].idea_1l missing")

    status = 'PASS' if not reasons else 'FAIL'
    return GateResult(gate='Gate9', status=status, reasons=reasons)

def gate10_mechanism_specs(step_map: Dict[int, Dict[str, Any]]) -> GateResult:
    reasons = []
    step10 = step_map.get(10, {})
    s10 = step10.get('payload', {}) if step10 else {}

    specs = s10.get('concept_specs')
    if not _is_non_empty(specs):
        reasons.append("Step10.concept_specs missing")
    elif not isinstance(specs, list):
        reasons.append("Step10.concept_specs is not a list")
    else:
        for idx, spec in enumerate(specs):
            if not isinstance(spec, dict):
                reasons.append(f"Step10.concept_specs[{idx}] not a dict")
                continue
            if not _is_non_empty(spec.get('concept_index')):
                reasons.append(f"Step10.concept_specs[{idx}].concept_index missing")
            if not _is_non_empty(spec.get('A_name_tagline')):
                reasons.append(f"Step10.concept_specs[{idx}].A_name_tagline missing")
            if not _is_non_empty(spec.get('C_mechanism_steps')):
                reasons.append(f"Step10.concept_specs[{idx}].C_mechanism_steps missing")

    status = 'PASS' if not reasons else 'FAIL'
    return GateResult(gate='Gate10', status=status, reasons=reasons)

def gate11_secondary_contradiction(step_map: Dict[int, Dict[str, Any]]) -> GateResult:
    reasons = []
    step11 = step_map.get(11, {})
    s11 = step11.get('payload', {}) if step11 else {}

    if s11.get('new_contradiction_exists') is None:
        reasons.append("Step11.new_contradiction_exists missing")

    status = 'PASS' if not reasons else 'FAIL'
    return GateResult(gate='Gate11', status=status, reasons=reasons)

def gate12_decision_record(step_map: Dict[int, Dict[str, Any]]) -> GateResult:
    reasons = []
    step12 = step_map.get(12, {})
    s12 = step12.get('payload', {}) if step12 else {}

    if not _is_non_empty(s12.get('chosen_concept_index')):
        reasons.append("Step12.chosen_concept_index missing")
    if not _is_non_empty(s12.get('chosen_concept_name')):
        reasons.append("Step12.chosen_concept_name missing")
    if not _is_non_empty(s12.get('reasons')):
        reasons.append("Step12.reasons missing")

    status = 'PASS' if not reasons else 'FAIL'
    return GateResult(gate='Gate12', status=status, reasons=reasons)

def gate13_implementation_map(step_map: Dict[int, Dict[str, Any]]) -> GateResult:
    reasons = []
    step13 = step_map.get(13, {})
    s13 = step13.get('payload', {}) if step13 else {}

    workstreams = s13.get('workstreams')
    if not _is_non_empty(workstreams):
        reasons.append("Step13.workstreams missing")
    elif not isinstance(workstreams, list):
        reasons.append("Step13.workstreams is not a list")
    else:
        for idx, ws in enumerate(workstreams):
            if not isinstance(ws, dict):
                reasons.append(f"Step13.workstreams[{idx}] not a dict")
                continue
            if not _is_non_empty(ws.get('name')):
                reasons.append(f"Step13.workstreams[{idx}].name missing")
            if not _is_non_empty(ws.get('owner')):
                reasons.append(f"Step13.workstreams[{idx}].owner missing")
            if not _is_non_empty(ws.get('tasks')):
                reasons.append(f"Step13.workstreams[{idx}].tasks missing")

    status = 'PASS' if not reasons else 'FAIL'
    return GateResult(gate='Gate13', status=status, reasons=reasons)

def gate14_rule_update(step_map: Dict[int, Dict[str, Any]]) -> GateResult:
    reasons = []
    step14 = step_map.get(14, {})
    s14 = step14.get('payload', {}) if step14 else {}

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
            reasons.append(f"Step14.{key} missing")

    status = 'PASS' if not reasons else 'FAIL'
    return GateResult(gate='Gate14', status=status, reasons=reasons)


def run_mvp_gates(tc: Dict[str, Any], step_map: Dict[int, Dict[str, Any]]) -> List[GateResult]:
    results = [
        gate0_envelope(tc),
    ]

    # If Gate0 BLOCKED, downstream is NOT_RUN
    if results[0].status == 'BLOCKED':
        results.extend([
            GateResult(gate='Gate1', status='NOT_RUN', reasons=["Gate0 blocked"]),
            GateResult(gate='Gate2', status='NOT_RUN', reasons=["Gate0 blocked"]),
            GateResult(gate='Gate3', status='NOT_RUN', reasons=["Gate0 blocked"]),
            GateResult(gate='Gate4', status='NOT_RUN', reasons=["Gate0 blocked"]),
            GateResult(gate='Gate5', status='NOT_RUN', reasons=["Gate0 blocked"]),
            GateResult(gate='Gate6', status='NOT_RUN', reasons=["Gate0 blocked"]),
            GateResult(gate='Gate7', status='NOT_RUN', reasons=["Gate0 blocked"]),
            GateResult(gate='Gate8', status='NOT_RUN', reasons=["Gate0 blocked"]),
            GateResult(gate='Gate9', status='NOT_RUN', reasons=["Gate0 blocked"]),
            GateResult(gate='Gate10', status='NOT_RUN', reasons=["Gate0 blocked"]),
            GateResult(gate='Gate11', status='NOT_RUN', reasons=["Gate0 blocked"]),
            GateResult(gate='Gate12', status='NOT_RUN', reasons=["Gate0 blocked"]),
            GateResult(gate='Gate13', status='NOT_RUN', reasons=["Gate0 blocked"]),
            GateResult(gate='Gate14', status='NOT_RUN', reasons=["Gate0 blocked"]),
        ])
        return results

    results.extend([
        gate1_case_owner(tc, step_map),
        gate2_system_boundary(step_map),
        gate3_interaction(step_map),
        gate4_contradiction(step_map),
        gate5_ikr(step_map),
        gate6_hard_barrier(step_map),
        gate7_resource_map(step_map),
        gate8_form_selection(step_map),
        gate9_solution_set(step_map),
        gate10_mechanism_specs(step_map),
        gate11_secondary_contradiction(step_map),
        gate12_decision_record(step_map),
        gate13_implementation_map(step_map),
        gate14_rule_update(step_map),
    ])

    return results
