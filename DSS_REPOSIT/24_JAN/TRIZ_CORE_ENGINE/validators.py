from __future__ import annotations

from typing import Any, Dict, List, Optional

from .models import FailReason, TRIZArtifacts, TRIZValidationResult


def _get_step(tc: Dict[str, Any], step: int) -> Dict[str, Any]:
    full_vector = tc.get('full_vector') or {}
    return full_vector.get(f'step_{step}', {}) or {}


def _fail(code: str, msg: str, path: str) -> FailReason:
    return FailReason(code=code, msg=msg, path=path)


def _physical_contradiction(tc: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    s8 = _get_step(tc, 8)
    triz = s8.get('TRIZ_CORE', {}) or {}
    return triz.get('physical_contradiction')


def _separation(tc: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    s8 = _get_step(tc, 8)
    triz = s8.get('TRIZ_CORE', {}) or {}
    return triz.get('separation')


def _system_operator(tc: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    s8 = _get_step(tc, 8)
    triz = s8.get('TRIZ_CORE', {}) or {}
    return triz.get('system_operator')


def _transformation_model(tc: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    s8 = _get_step(tc, 8)
    triz = s8.get('TRIZ_CORE', {}) or {}
    return triz.get('transformation_model')


def _non_obviousness(tc: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    s8 = _get_step(tc, 8)
    triz = s8.get('TRIZ_CORE', {}) or {}
    return triz.get('non_obviousness_check')


def _check_physical_contradiction(pc: Optional[Dict[str, Any]]) -> List[FailReason]:
    if not isinstance(pc, dict):
        return [_fail('TRIZ_G1_MISSING', 'physical_contradiction missing', 'step_8.TRIZ_CORE.physical_contradiction')]
    obj = pc.get('object')
    param = pc.get('parameter')
    a_state = pc.get('state_a')
    not_a_state = pc.get('state_not_a')
    if not obj or not param or not a_state or not not_a_state:
        return [_fail('TRIZ_G1_INCOMPLETE', 'physical contradiction fields missing', 'step_8.TRIZ_CORE.physical_contradiction')]
    if a_state == not_a_state:
        return [_fail('TRIZ_G1_TAUTOLOGY', 'state_a equals state_not_a', 'step_8.TRIZ_CORE.physical_contradiction')]
    return []


def _check_separation(sep: Optional[Dict[str, Any]]) -> List[FailReason]:
    if not isinstance(sep, dict):
        return [_fail('TRIZ_G2_MISSING', 'separation missing', 'step_8.TRIZ_CORE.separation')]
    stype = sep.get('separation_type')
    change = sep.get('what_changes')
    resolution = sep.get('expected_resolution')
    if not stype or stype not in ('time', 'space', 'condition', 'part-whole'):
        return [_fail('TRIZ_G2_INVALID_TYPE', 'invalid or missing separation_type', 'step_8.TRIZ_CORE.separation.separation_type')]
    if not change or not resolution:
        return [_fail('TRIZ_G2_INCOMPLETE', 'separation mapping incomplete', 'step_8.TRIZ_CORE.separation')]
    return []


def _check_system_operator(so: Optional[Dict[str, Any]]) -> List[FailReason]:
    if not isinstance(so, dict):
        return [_fail('TRIZ_G3_MISSING', 'system_operator missing', 'step_8.TRIZ_CORE.system_operator')]
    required_present = so.get('system_present')
    if not required_present:
        return [_fail('TRIZ_G3_NO_PRESENT', 'system_present missing', 'step_8.TRIZ_CORE.system_operator.system_present')]
    filled = 0
    for key in (
        'subsystem_past','subsystem_present','subsystem_future',
        'system_past','system_present','system_future',
        'supersystem_past','supersystem_present','supersystem_future',
    ):
        if so.get(key):
            filled += 1
    if filled < 3:
        return [_fail('TRIZ_G3_MIN_CELLS', 'less than 3 cells filled', 'step_8.TRIZ_CORE.system_operator')]
    return []


def _check_non_obviousness(nob: Optional[Dict[str, Any]], tc: Dict[str, Any]) -> List[FailReason]:
    if not isinstance(nob, dict):
        return [_fail('TRIZ_G4_MISSING', 'non_obviousness_check missing', 'step_8.TRIZ_CORE.non_obviousness_check')]
    if not (nob.get('assumption_broken') or nob.get('why_not_obvious')):
        return [_fail('TRIZ_G4_INCOMPLETE', 'non_obviousness fields missing', 'step_8.TRIZ_CORE.non_obviousness_check')]

    text = f"{nob.get('assumption_broken','')} {nob.get('why_not_obvious','')}".lower()
    bad_phrases = ['очевидно', 'логично', 'надо лучше управлять', 'оптимизировать']
    if any(p in text for p in bad_phrases):
        return [_fail('TRIZ_G4_TAUTOLOGY', 'generic non-obviousness phrase', 'step_8.TRIZ_CORE.non_obviousness_check')]

    s8 = _get_step(tc, 8)
    triz = s8.get('TRIZ_CORE', {}) or {}
    sep = triz.get('separation', {}) if isinstance(triz.get('separation', {}), dict) else {}
    pc = triz.get('physical_contradiction', {}) if isinstance(triz.get('physical_contradiction', {}), dict) else {}

    sep_terms = []
    if sep:
        for key in ('separation_type', 'what_changes', 'expected_resolution'):
            val = sep.get(key)
            if isinstance(val, str) and val.strip():
                sep_terms.append(val.lower())
    pc_terms = []
    if pc:
        for key in ('object', 'parameter', 'state_a', 'state_not_a'):
            val = pc.get(key)
            if isinstance(val, str) and val.strip():
                pc_terms.append(val.lower())

    if sep_terms:
        if not any(t in text for t in sep_terms):
            return [_fail('TRIZ_G4_INVALID', 'non-obviousness has no reference to separation', 'step_8.TRIZ_CORE.non_obviousness_check')]
    else:
        if not any(t in text for t in pc_terms):
            return [_fail('TRIZ_G4_INVALID', 'non-obviousness has no reference to contradiction', 'step_8.TRIZ_CORE.non_obviousness_check')]

    return []


def _check_transformation_model(tm: Optional[Dict[str, Any]]) -> List[FailReason]:
    if not isinstance(tm, dict):
        return [_fail('TRIZ_GX_MISSING', 'transformation_model missing', 'step_8.TRIZ_CORE.transformation_model')]
    if not tm.get('changed_object') or not tm.get('new_state') or not tm.get('resolution_link'):
        return [_fail('TRIZ_GX_INCOMPLETE', 'transformation_model fields missing', 'step_8.TRIZ_CORE.transformation_model')]
    return []


def validate_triz_core(tc: Dict[str, Any], semantic: Dict[str, Any] | None, gate_log: List[Dict[str, Any]] | None) -> Dict[str, Any]:
    pc = _physical_contradiction(tc)
    sep = _separation(tc)
    so = _system_operator(tc)
    tm = _transformation_model(tc)
    nob = _non_obviousness(tc)

    failures: List[FailReason] = []
    failures += _check_physical_contradiction(pc)
    failures += _check_separation(sep)
    failures += _check_system_operator(so)
    failures += _check_non_obviousness(nob, tc)
    failures += _check_transformation_model(tm)

    status = 'VALID' if not failures else 'INVALID'
    result = TRIZValidationResult(
        status=status,
        fail_reasons=failures,
        artifacts=TRIZArtifacts(
            physical_contradiction=pc,
            separation=sep,
            system_operator=so,
            transformation_model=tm,
            non_obviousness_check=nob,
        )
    )
    return {
        'status': result.status,
        'fail_reasons': [r.__dict__ for r in result.fail_reasons],
        'artifacts': {
            'physical_contradiction': result.artifacts.physical_contradiction,
            'separation': result.artifacts.separation,
            'system_operator': result.artifacts.system_operator,
            'transformation_model': result.artifacts.transformation_model,
            'non_obviousness_check': result.artifacts.non_obviousness_check,
        }
    }
