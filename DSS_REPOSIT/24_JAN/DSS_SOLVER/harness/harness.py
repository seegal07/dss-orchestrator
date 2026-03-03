from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
from pathlib import Path
from typing import Any, Dict, List
import sys
import importlib.util

from gates_structural import run_structural_gates, GateResult

ROOT = Path('/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN')
DSS_DIR = ROOT / 'DSS_SOLVER'
TESTS_DIR = DSS_DIR / 'tests'
EVIDENCE_DIR = DSS_DIR / 'evidence'
EXPORTS_DIR = DSS_DIR / 'exports'

# Load microyaml from local harness dir
spec = importlib.util.spec_from_file_location('microyaml', str(DSS_DIR / 'harness' / 'microyaml.py'))
my = importlib.util.module_from_spec(spec)
sys.modules['microyaml'] = my
spec.loader.exec_module(my)

ASSISTED_GATES = {'Gate4', 'Gate5', 'Gate6', 'Gate11', 'Gate12'}
MANUAL_GATES = set()
ADDON_GATES = {'Gate15', 'Gate16', 'Gate17', 'Gate18'}
CANONICAL_HARD_FAIL_MESSAGE = 'structural resolution not found'
PHASE0_REASON_CODES = {'AMBIGUOUS_INTENT', 'INSUFFICIENT_SCOPE', 'MECHANISM_ONLY_INPUT', 'OTHER'}
PFL_REASON_ENUM = {
    'NONE',
    'INVALID_DUAL_TENSION',
    'NO_MUTUAL_DEGRADATION',
    'OUT_OF_SCOPE',
    'SYMPTOM_FRAMING',
    'TRIVIAL_CONFLICT',
    'SOLUTION_AS_XY',
}
PHASE0_ACTION_MARKERS = (
    'сдела',
    'внедр',
    'запуст',
    'нанят',
    'подпис',
    'перезапуст',
    'restart',
    'implement',
)

# --- Phase0 slots v0 helpers (added) ---
def _direction_enum(text: str):
    if not text:
        return None
    t = text.lower()
    if any(w in t for w in ["ускор", "быстр", "скор"]):
        return "accelerate"
    if any(w in t for w in ["замед", "медлен"]):
        return "decelerate"
    if any(w in t for w in ["увелич", "повыс", "рост", "улучш"]):
        return "increase"
    if any(w in t for w in ["сниз", "уменьш", "сократ", "удешев"]):
        return "decrease"
    if any(w in t for w in ["стабилиз", "сохран"]):
        return "stabilize"
    return "other"

def _extract_na_income_object(tokens):
    """
    Narrow exception for phrases with preposition 'на' in tax-load context:
    "... на мой доход", "... на наш доход", "... на доход".
    Returns normalized object token phrase or None.
    """
    if not tokens:
        return None
    for i, tok in enumerate(tokens):
        if tok != "на":
            continue
        if i + 2 < len(tokens) and tokens[i + 1] in {"мой", "наш"} and "доход" in tokens[i + 2]:
            return f"{tokens[i + 1]} {tokens[i + 2]}"
        if i + 1 < len(tokens) and "доход" in tokens[i + 1]:
            return tokens[i + 1]
    return None

def _extract_object_after_metric(tokens, metric_label, stop_tokens):
    """
    Narrow phrase extractor: returns up to 1-3 tokens after a metric token.
    Example: "комфорт проживания семьи" -> "проживания семьи".
    """
    if not tokens or not metric_label:
        return None
    for i, tok in enumerate(tokens):
        if metric_label not in tok:
            continue
        chunk = []
        for j in range(i + 1, min(i + 4, len(tokens))):
            nxt = tokens[j]
            if nxt in stop_tokens:
                break
            chunk.append(nxt)
        if chunk:
            return " ".join(chunk)[:120]
    return None

def _extract_metric_object(text: str):
    """
    Conservative extraction (no synonym dictionaries):
    - metric_token: from a closed metric stem list
    - object_token: short object chunk with stop-token boundary rules
    Returns (metric_token, object_token) or (None, None) when uncertain.
    """
    if not text:
        return None, None
    t = re.sub(r"\s+", " ", text.strip().lower())

    metric = None
    metric_stems = [
        ("точност", "точность"),
        ("время", "время"),
        ("срок", "срок"),
        ("стоимост", "стоимость"),
        ("расход", "расход"),
        ("бюджет", "бюджет"),
        ("скорост", "скорость"),
        ("темп", "темп"),
        ("качеств", "качество"),
        ("комфорт", "комфорт"),
        ("налог", "налоги"),
        ("нагрузк", "налоги"),
        ("прогноз", "прогноз"),
        ("предоцен", "предоцен"),
    ]
    for stem, label in metric_stems:
        if stem in t:
            metric = label
            break

    obj = None
    tokens = re.findall(r"[\w-]+", t)
    stop_tokens = {"при", "по", "в", "до", "на", "для", "с", "из"}

    filial_idx = None
    for i, tok in enumerate(tokens):
        if "филиал" in tok:
            filial_idx = i
            break

    if filial_idx is not None:
        chunk = [tokens[filial_idx]]
        for j in range(filial_idx + 1, min(filial_idx + 3, len(tokens))):
            nxt = tokens[j]
            if nxt in stop_tokens:
                if nxt == "на":
                    na_obj = _extract_na_income_object(tokens[j:])
                    if na_obj:
                        obj = na_obj
                break
            chunk.append(nxt)
        if obj is None:
            obj = " ".join(chunk)

    if obj is None:
        na_obj = _extract_na_income_object(tokens)
        if na_obj:
            obj = na_obj

    if obj is None and metric == "комфорт":
        obj = _extract_object_after_metric(tokens, "комфорт", stop_tokens)

    if obj is None:
        for stem in ["запуск", "выход", "прогноз", "предоцен", "рынок", "инвест"]:
            m = re.search(rf"(\b\w{{0,12}}{re.escape(stem)}\w{{0,12}}\b(?:\s+\b\w+\b){{0,2}})", t)
            if m:
                obj = m.group(1)
                break

    if metric is None and obj is None:
        return None, None
    return metric, (obj[:120] if obj else None)


def _extract_object_window(text: str, metric: str | None = None):
    """
    Deterministic fallback extractor for object phrase.
    Anchors by stems, captures up to 2 following tokens, stops on prepositions.
    """
    if not text:
        return None
    t = re.sub(r"\s+", " ", text.strip().lower())
    tokens = re.findall(r"[\w-]+", t)
    if not tokens:
        return None

    stop_tokens = {"при", "по", "в", "до", "на", "для", "с", "из"}
    anchor_stems = ("запуск", "старт", "внедр", "филиал")

    if (metric or "").lower() == "комфорт":
        metric_obj = _extract_object_after_metric(tokens, "комфорт", stop_tokens)
        if metric_obj:
            return metric_obj

    anchor_idx = None
    for i, tok in enumerate(tokens):
        if any(stem in tok for stem in anchor_stems):
            anchor_idx = i
            break
    if anchor_idx is None:
        return None

    chunk = [tokens[anchor_idx]]
    for j in range(anchor_idx + 1, min(anchor_idx + 3, len(tokens))):
        nxt = tokens[j]
        if nxt in stop_tokens:
            if nxt == "на":
                na_obj = _extract_na_income_object(tokens[j:])
                if na_obj:
                    return na_obj[:120]
            break
        chunk.append(nxt)

    candidate = " ".join(chunk).strip()
    return candidate[:120] if candidate else None


def _extract_delta_direction(text: str):
    """
    Deterministic direction extraction for S2a fields.
    Returns one of: increase|decrease|accelerate|decelerate|unknown
    """
    if not text:
        return "unknown"
    t = text.lower()
    direction_markers = (
        ("accelerate", ("быстр", "скор")),
        ("decelerate", ("медлен", "дольше")),
        ("increase", ("выше", "больше", "раст")),
        ("decrease", ("ниже", "меньше", "сниж")),
    )
    for direction, markers in direction_markers:
        if any(marker in t for marker in markers):
            return direction
    return "unknown"


def _infer_metric_polarity(metric: str, display_text: str):
    """
    S2a closed mapping from spec:
    - accuracy/точность -> HIGHER_IS_BETTER
    - time/время/срок   -> LOWER_IS_BETTER
    - cost/стоимость    -> LOWER_IS_BETTER
    - risk/риск         -> LOWER_IS_BETTER
    - else              -> UNKNOWN
    """
    metric_value = (metric or "").lower()
    text_value = (display_text or "").lower()
    combined = f"{metric_value} {text_value}".strip()

    if "accuracy" in combined or "точност" in combined:
        return "HIGHER_IS_BETTER"
    if "comfort" in combined or "комфорт" in combined:
        return "HIGHER_IS_BETTER"
    if "time" in combined or "время" in combined or "срок" in combined:
        return "LOWER_IS_BETTER"
    if "cost" in combined or "стоимост" in combined:
        return "LOWER_IS_BETTER"
    if "risk" in combined or "риск" in combined:
        return "LOWER_IS_BETTER"
    if "налог" in combined or "нагрузк" in combined:
        return "LOWER_IS_BETTER"
    return "UNKNOWN"


def _build_slots_v0(
    canonical_X_display: str,
    canonical_Y_display: str,
    scope: str,
    constraints,
    raw_x_text: str | None = None,
    raw_y_text: str | None = None,
):
    x_metric, x_obj = _extract_metric_object(canonical_X_display)
    y_metric, y_obj = _extract_metric_object(canonical_Y_display)

    x_dir = _direction_enum(canonical_X_display)
    y_dir = _direction_enum(canonical_Y_display)

    # Direction precedence: if metric indicates speed/pace, force accelerate.
    if x_metric in {"темп", "скорость"}:
        x_dir = "accelerate"
    if y_metric in {"темп", "скорость"}:
        y_dir = "accelerate"

    trace_markers = []
    if x_metric is None:
        trace_markers.append('MISSING_SLOT:X_metric')
    if y_metric is None:
        trace_markers.append('MISSING_SLOT:Y_metric')
    if x_obj is None:
        trace_markers.append('MISSING_SLOT:X_object')

    if x_obj is None and x_metric == "комфорт":
        x_obj = _extract_object_window(canonical_X_display, metric=x_metric)
        if x_obj:
            trace_markers = [m for m in trace_markers if m != 'MISSING_SLOT:X_object']
            trace_markers.append('OBJ_FROM_METRIC_PHRASE:X')

    x_obj_from_na = _extract_na_income_object(re.findall(r"[\w-]+", (canonical_X_display or "").lower()))
    y_obj_from_na = _extract_na_income_object(re.findall(r"[\w-]+", (canonical_Y_display or "").lower()))
    if x_obj_from_na and x_obj == x_obj_from_na:
        trace_markers.append('OBJ_FROM_NA_PATTERN:X')
    if y_obj_from_na and y_obj == y_obj_from_na:
        trace_markers.append('OBJ_FROM_NA_PATTERN:Y')

    # Y_object fallback for v0.2 readiness: deterministic extraction or explicit UNKNOWN marker.
    if y_obj is None:
        y_obj = _extract_object_window(canonical_Y_display, metric=y_metric)
    if y_obj is None:
        y_obj = 'UNKNOWN'
        trace_markers.append('MISSING_SLOT:Y_object')

    x_delta_direction = _extract_delta_direction(canonical_X_display)
    y_delta_direction = _extract_delta_direction(canonical_Y_display)

    # Deterministic fallback: if canonical side text has no delta marker, retry using raw variant text.
    if x_delta_direction == "unknown" and raw_x_text:
        x_delta_from_raw = _extract_delta_direction(raw_x_text)
        if x_delta_from_raw != "unknown":
            x_delta_direction = x_delta_from_raw
            trace_markers.append('DELTA_FROM_RAW:X')
    if y_delta_direction == "unknown" and raw_y_text:
        y_delta_from_raw = _extract_delta_direction(raw_y_text)
        if y_delta_from_raw != "unknown":
            y_delta_direction = y_delta_from_raw
            trace_markers.append('DELTA_FROM_RAW:Y')

    if x_delta_direction == "unknown":
        trace_markers.append('MISSING_SLOT:X_delta_direction')
    if y_delta_direction == "unknown":
        trace_markers.append('MISSING_SLOT:Y_delta_direction')

    x_metric_polarity = _infer_metric_polarity(x_metric, canonical_X_display)
    y_metric_polarity = _infer_metric_polarity(y_metric, canonical_Y_display)
    if x_metric_polarity == "UNKNOWN":
        trace_markers.append('UNKNOWN_POLARITY:X')
    if y_metric_polarity == "UNKNOWN":
        trace_markers.append('UNKNOWN_POLARITY:Y')

    return {
        "scope": scope,
        "X_direction": x_dir,
        "X_delta_direction": x_delta_direction,
        "X_metric_polarity": x_metric_polarity,
        "X_metric": x_metric,
        "X_object": x_obj,
        "Y_direction": y_dir,
        "Y_delta_direction": y_delta_direction,
        "Y_metric_polarity": y_metric_polarity,
        "Y_metric": y_metric,
        "Y_object": y_obj,
        "constraints": constraints,
        "trace_markers": trace_markers,
    }
def _normalize_slots(slots: dict):
    def norm(x):
        if x is None:
            return None
        if isinstance(x, str):
            return " ".join(x.strip().split()).lower()
        return x
    out = {}
    for k in sorted(slots.keys()):
        v = slots[k]
        if isinstance(v, list):
            out[k] = [norm(i) for i in v]
        else:
            out[k] = norm(v)
    return out

def _build_s1_identity_payload(canonical_slots_v0: dict):
    """
    Option A split-hash identity payload for Step1/canonical_hash_v0.
    Includes only S1 identity fields and excludes S2a-derived fields and trace markers.
    """
    payload = {
        "scope": canonical_slots_v0.get("scope"),
        "X_metric": canonical_slots_v0.get("X_metric"),
        "X_object": canonical_slots_v0.get("X_object"),
        "Y_metric": canonical_slots_v0.get("Y_metric"),
        "Y_object": canonical_slots_v0.get("Y_object"),
    }
    timeframe = canonical_slots_v0.get("timeframe")
    if timeframe is not None and str(timeframe).strip():
        payload["timeframe"] = timeframe
    return _normalize_slots(payload)

def _build_s2a_derived_payload(canonical_slots_v0: dict):
    """
    Option A split-hash derived payload for S2a fields only.
    """
    payload = {
        "X_delta_direction": canonical_slots_v0.get("X_delta_direction"),
        "Y_delta_direction": canonical_slots_v0.get("Y_delta_direction"),
        "X_metric_polarity": canonical_slots_v0.get("X_metric_polarity"),
        "Y_metric_polarity": canonical_slots_v0.get("Y_metric_polarity"),
    }
    return _normalize_slots(payload)
# --- end helpers ---



def _normalize_reason_code(reason: str) -> str:
    text = (reason or '').strip()
    if not text:
        return 'UNSPECIFIED'
    if text == CANONICAL_HARD_FAIL_MESSAGE:
        return 'STRUCTURAL_RESOLUTION_NOT_FOUND'
    head = text.split(':', 1)[0].strip().upper()
    if head and all(ch.isalnum() or ch in {'_', '-'} for ch in head):
        return head.replace('-', '_')
    simplified = ''.join(ch if ch.isalnum() else '_' for ch in text.upper())
    simplified = '_'.join(part for part in simplified.split('_') if part)
    return simplified[:64] if simplified else 'UNSPECIFIED'


def _canonical_input_payload(tc: Dict[str, Any], step_map: Dict[int, Dict[str, Any]]) -> Dict[str, Any]:
    s1 = step_map.get(1, {}) or {}
    s2 = step_map.get(2, {}) or {}
    s4 = step_map.get(4, {}) or {}
    x_value = tc.get('pfl_X') or s4.get('improve_x') or s4.get('statement_1l') or ''
    y_value = tc.get('pfl_Y') or s4.get('worsen_y') or ''
    scope = s1.get('owner_scope') or s2.get('boundary_note_1l') or ''
    constraints = s1.get('constraints') or []
    if not isinstance(constraints, list):
        constraints = [constraints]
    canonical_constraints = [str(c).strip() for c in constraints if str(c).strip()]
    return {
        'canonical_X': str(x_value).strip(),
        'canonical_Y': str(y_value).strip(),
        'scope': str(scope).strip(),
        'constraints': canonical_constraints,
    }


def _input_fingerprint(tc: Dict[str, Any], step_map: Dict[int, Dict[str, Any]]) -> str:
    payload = _canonical_input_payload(tc, step_map)
    serialized = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
    return hashlib.sha256(serialized.encode('utf-8')).hexdigest()


def _normalize_scalar(value: Any) -> str:
    text = str(value or '')
    text = re.sub(r'\s+', ' ', text, flags=re.UNICODE).strip()
    return text


def _normalize_constraints(values: Any) -> List[str]:
    if values is None:
        return []
    if not isinstance(values, list):
        values = [values]
    normalized = [_normalize_scalar(v) for v in values if _normalize_scalar(v)]
    # Deterministic ordering policy.
    return sorted(normalized, key=lambda x: x.lower())


def _phase0_enabled(tc: Dict[str, Any]) -> bool:
    flag = tc.get('phase0_enabled')
    if isinstance(flag, bool):
        return flag
    schema_raw = tc.get('schema_version')
    try:
        return float(str(schema_raw)) >= 0.6
    except (TypeError, ValueError):
        return False


def _materialize_pfl_fields(
    tc: Dict[str, Any],
    phase0: Dict[str, Any],
) -> Dict[str, Any]:
    """
    Truthful shim for PFL availability.
    This function must not synthesize PFL verdict/reason/tension/attempt.
    """
    verdict = str(tc.get('pfl_verdict') or '').upper()
    reason = str(tc.get('pfl_reason') or '').upper()
    structural_tension = tc.get('pfl_structural_tension')
    attempt_index = tc.get('pfl_attempt_index')

    is_valid = True
    if verdict not in {'PASS', 'FAIL'}:
        is_valid = False
    if reason not in PFL_REASON_ENUM:
        is_valid = False
    if structural_tension is None:
        is_valid = False
    try:
        if attempt_index is None:
            is_valid = False
        else:
            attempt_int = int(attempt_index)
            if attempt_int < 1 or attempt_int > 3:
                is_valid = False
    except (ValueError, TypeError):
        is_valid = False

    if is_valid:
        return {
            'pfl_status': 'PFL_READY',
            'pfl_status_reason': 'PFL fields available in tc',
        }

    phase0_verdict = str(phase0.get('phase0_verdict') or '').upper()
    if phase0_verdict == 'FAIL':
        return {
            'pfl_status': 'PFL_BLOCKED',
            'pfl_status_reason': f'Phase0 verdict={phase0_verdict}',
        }
    return {
        'pfl_status': 'PFL_NOT_AVAILABLE',
        'pfl_status_reason': 'PFL fields missing/invalid in tc',
    }


def compute_pfl_v0_1(tc: Dict[str, Any]) -> Dict[str, Any]:
    """
    Deterministic PFL compute v0.1.
    Inputs: canonical_* fields only.
    """
    canonical_x_raw = tc.get('canonical_X')
    canonical_y_raw = tc.get('canonical_Y')
    canonical_scope_raw = tc.get('canonical_scope')
    canonical_constraints_raw = tc.get('canonical_constraints')
    canonical_conflict_raw = tc.get('canonical_conflict_type_candidate')

    canonical_x = _normalize_scalar(canonical_x_raw)
    canonical_y = _normalize_scalar(canonical_y_raw)
    canonical_scope = _normalize_scalar(canonical_scope_raw)
    canonical_conflict = _normalize_scalar(canonical_conflict_raw).lower()

    action_markers = (
        'внедр', 'запуст', 'сдела', 'улучш', 'оптимиз', 'автоматиз',
        'наня', 'увелич', 'сниз', 'повыс', 'ускор',
    )
    symptom_markers = (
        'проблем', 'плохо', 'не работа', 'хаос', 'бардак', 'пожар', 'падает', 'кризис',
    )

    def _fail(reason: str) -> Dict[str, Any]:
        return {
            'pfl_verdict': 'FAIL',
            'pfl_reason': reason,
            'pfl_structural_tension': False,
            'pfl_attempt_index': 1,
        }

    # Phase A — structural checks (FAIL-only).
    if not canonical_scope:
        return _fail('OUT_OF_SCOPE')
    if not canonical_x or not canonical_y or canonical_x == canonical_y:
        return _fail('INVALID_DUAL_TENSION')
    if canonical_constraints_raw is None or not canonical_conflict:
        return _fail('NO_MUTUAL_DEGRADATION')

    x_lower = canonical_x.lower()
    y_lower = canonical_y.lower()

    # Phase B — marker filters (FAIL-only, closed lists).
    if any(marker in x_lower for marker in action_markers) or any(marker in y_lower for marker in action_markers):
        return _fail('SOLUTION_AS_XY')
    if any(marker in x_lower for marker in symptom_markers) or any(marker in y_lower for marker in symptom_markers):
        return _fail('SYMPTOM_FRAMING')

    # v0.1: PASS is not produced (mutual-degradation proof deferred).
    _ = canonical_conflict  # consumed canonical input in v0.1 binding.
    return {
        'pfl_verdict': 'FAIL',
        'pfl_reason': 'NO_MUTUAL_DEGRADATION',
        'pfl_structural_tension': False,
        'pfl_attempt_index': 1,
    }


def _run_phase0(tc: Dict[str, Any], step_map: Dict[int, Dict[str, Any]]) -> Dict[str, Any]:
    s0 = step_map.get(0, {}) or {}
    s1 = step_map.get(1, {}) or {}
    s2 = step_map.get(2, {}) or {}
    s4 = step_map.get(4, {}) or {}
    source_x = tc.get('pfl_X') or s4.get('improve_x') or s4.get('statement_1l') or ''
    source_y = tc.get('pfl_Y') or s4.get('worsen_y') or ''
    source_scope = s1.get('owner_scope') or s2.get('boundary_note_1l') or ''
    source_constraints = s1.get('constraints') or []
    conflict_type = _normalize_scalar(tc.get('pfl_conflict_type_candidate') or 'causal').lower()
    if conflict_type not in {'causal', 'temporal', 'interaction', 'scale'}:
        conflict_type = 'causal'

    canonical_x = _normalize_scalar(source_x)
    canonical_y = _normalize_scalar(source_y)
    canonical_scope = _normalize_scalar(source_scope)
    canonical_constraints = _normalize_constraints(source_constraints)

    trace = []
    for key, raw_value, interpreted, rule in [
        ('X', source_x, canonical_x, 'normalize_whitespace'),
        ('Y', source_y, canonical_y, 'normalize_whitespace'),
        ('scope', source_scope, canonical_scope, 'scope_projection'),
        ('constraints', source_constraints, canonical_constraints, 'stable_list_sort'),
    ]:
        trace.append({
            'raw_fragment': _normalize_scalar(raw_value),
            'interpreted_parameter': interpreted,
            'reasoning_trace': f'{key}:{rule}',
            'confidence_level': 'HIGH' if interpreted else 'LOW',
        })

    canonical_object = {
        'system_scope': canonical_scope,
        'X_param': canonical_x,
        'Y_param': canonical_y,
        'tension_direction': 'X↑ -> Y↓',
        'constraints': canonical_constraints,
        'conflict_type_candidate': conflict_type,
    }
    canonical_hash = hashlib.sha256(
        json.dumps(canonical_object, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode('utf-8')
    ).hexdigest()
    canonical_hash_text = canonical_hash  # legacy text-shaped hash (historical replay)

    canonical_X_display = canonical_object.get('X_param')
    canonical_Y_display = canonical_object.get('Y_param')
    raw_variant_text = s0.get('symptom_1l') or s4.get('statement_1l') or ''
    canonical_slots_v0 = _build_slots_v0(
        canonical_X_display,
        canonical_Y_display,
        canonical_object.get('system_scope'),
        canonical_object.get('constraints'),
        raw_x_text=raw_variant_text,
        raw_y_text=raw_variant_text,
    )
    s1_identity_payload = _build_s1_identity_payload(canonical_slots_v0)
    s2a_derived_payload = _build_s2a_derived_payload(canonical_slots_v0)

    canonical_hash_v0 = hashlib.sha256(
        json.dumps(s1_identity_payload, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode('utf-8')
    ).hexdigest()
    s2a_hash = hashlib.sha256(
        json.dumps(s2a_derived_payload, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode('utf-8')
    ).hexdigest()
    canonical_hash = canonical_hash_v0  # primary Stage A canonical identity (slots-hash)
    raw_payload = {
        'raw_X': source_x,
        'raw_Y': source_y,
        'raw_scope': source_scope,
        'raw_constraints': source_constraints,
    }
    raw_hash = hashlib.sha256(
        json.dumps(raw_payload, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode('utf-8')
    ).hexdigest()

    verdict = 'PASS'
    reason_code = 'NONE'
    if not canonical_scope:
        verdict = 'FAIL'
        reason_code = 'INSUFFICIENT_SCOPE'
    elif not canonical_x or not canonical_y:
        verdict = 'FAIL'
        reason_code = 'AMBIGUOUS_INTENT'
    elif any(marker in canonical_x.lower() for marker in PHASE0_ACTION_MARKERS) and any(
        marker in canonical_y.lower() for marker in PHASE0_ACTION_MARKERS
    ):
        verdict = 'FAIL'
        reason_code = 'MECHANISM_ONLY_INPUT'

    confidence_values = [t['confidence_level'] for t in trace]
    if all(v == 'HIGH' for v in confidence_values):
        confidence_summary = 'HIGH'
    elif any(v == 'LOW' for v in confidence_values):
        confidence_summary = 'MED'
    else:
        confidence_summary = 'MED'

    if reason_code not in PHASE0_REASON_CODES and reason_code != 'NONE':
        reason_code = 'OTHER'

    return {
        'phase0_verdict': verdict,
        'phase0_reason_code': reason_code,
        'canonical_hash': canonical_hash,
        'canonical_hash_v0': canonical_hash_v0,
        's2a_hash': s2a_hash,
        'canonical_hash_text': canonical_hash_text,
        'canonical_slots_v0': canonical_slots_v0,
        'raw_hash': raw_hash,
        'canonical_object': canonical_object,
        'canonical_scope': canonical_scope,
        'canonical_X': canonical_x,
        'canonical_Y': canonical_y,
        'canonical_constraints': canonical_constraints,
        'canonical_conflict_type_candidate': conflict_type,
        'phase0_trace': trace,
        'trace_count': len(trace),
        'confidence_summary': confidence_summary,
    }

# TRIZ core engine (root-level package)
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))
from TRIZ_CORE_ENGINE.api import validate_triz_core as triz_validate


def _now_stamp() -> str:
    return dt.datetime.utcnow().strftime('%Y-%m-%dT%H-%M-%SZ')


def _load_tc(tc_id: str) -> Dict[str, Any]:
    path = TESTS_DIR / f'{tc_id}.yaml'
    if not path.exists():
        raise FileNotFoundError(f'Test case not found: {path}')
    return my.load(str(path))


def _load_tc_path(path: Path) -> Dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(f'Test case not found: {path}')
    return my.load(str(path))


def _build_step_map(tc: Dict[str, Any]) -> Dict[int, Dict[str, Any]]:
    step_map: Dict[int, Dict[str, Any]] = {}
    full_vector = tc.get('full_vector') or {}
    for k, v in full_vector.items():
        if k.startswith('step_'):
            parts = k.split('_')[1:]
            if len(parts) == 1 and parts[0].isdigit():
                step = int(parts[0])
            elif len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
                # Step 8.5 is represented as step_8_5 and mapped to integer key 85.
                step = int(parts[0]) * 10 + int(parts[1])
            else:
                continue
            step_map[step] = v
    return step_map


def _write_yaml(path: Path, data: str) -> None:
    path.write_text(data, encoding='utf-8')


def _evidence_yaml(tc_id: str, run_id: str, gate_results: List[GateResult]) -> str:
    lines = []
    lines.append(f"run_id: {run_id}")
    lines.append(f"test_case_id: {tc_id}")
    lines.append("harness_version: dss-solver-0.1")
    lines.append(f"timestamp_utc: {run_id}")
    lines.append(f"overall_status: { _overall_status(gate_results) }")
    lines.append("gate_results:")
    for g in gate_results:
        lines.append(f"  - gate: {g.gate}")
        lines.append(f"    status: {g.status}")
        if g.reasons:
            lines.append("    reasons:")
            for r in g.reasons:
                lines.append(f"      - \"{r}\"")
        else:
            lines.append("    reasons: []")
    return "\n".join(lines) + "\n"


def _buglist_yaml(tc_id: str, run_id: str, gate_results: List[GateResult]) -> str:
    lines = []
    lines.append(f"run_id: {run_id}")
    lines.append(f"test_case_id: {tc_id}")
    lines.append("issues:")
    for g in gate_results:
        if g.status in ('FAIL', 'BLOCKED', 'HARD_FAIL'):
            for r in g.reasons:
                lines.append(f"  - gate: {g.gate}")
                lines.append("    issue_code: STRUCTURAL")
                lines.append(f"    message: \"{r}\"")
    if len(lines) == 3:
        lines.append("  - gate: NONE")
        lines.append("    issue_code: NONE")
        lines.append("    message: \"No issues\"")
    return "\n".join(lines) + "\n"


def _overall_status(gate_results: List[GateResult]) -> str:
    statuses = [g.status for g in gate_results]
    if 'HARD_FAIL' in statuses:
        return 'FAIL'
    if 'BLOCKED' in statuses:
        return 'BLOCKED'
    if 'FAIL' in statuses:
        return 'FAIL'
    if 'SOFT_FAIL' in statuses:
        return 'PARTIAL'
    if all(s == 'PASS' for s in statuses if s != 'NOT_RUN'):
        return 'PASS'
    return 'PARTIAL'


def _load_semantic_answers(path: Path) -> Dict[str, Any]:
    data = my.load(str(path))
    return data or {}


def _apply_semantic(results: List[GateResult], answers: Dict[str, Any]) -> List[GateResult]:
    answer_map = answers.get('results', {}) if isinstance(answers, dict) else {}
    updated: List[GateResult] = []
    for g in results:
        if g.gate in ASSISTED_GATES or g.gate in MANUAL_GATES:
            # If structural failed/blocked, keep it
            if g.status in ('FAIL', 'BLOCKED', 'NOT_RUN', 'HARD_FAIL', 'SOFT_FAIL'):
                updated.append(g)
                continue
            a = answer_map.get(g.gate)
            if not isinstance(a, dict):
                updated.append(GateResult(gate=g.gate, status='BLOCKED', reasons=['semantic answers missing']))
                continue
            criteria = a.get('criteria', [])
            if not isinstance(criteria, list) or len(criteria) == 0:
                updated.append(GateResult(gate=g.gate, status='BLOCKED', reasons=['criteria list missing']))
                continue
            # Gate status derived from criteria statuses
            statuses = [c.get('status', '').upper() for c in criteria if isinstance(c, dict)]
            if any(s == 'FAIL' for s in statuses):
                status = 'FAIL'
            elif any(s == 'BLOCKED' for s in statuses):
                status = 'BLOCKED'
            elif all(s == 'PASS' for s in statuses):
                status = 'PASS'
            else:
                status = 'BLOCKED'
            reasons = []
            for c in criteria:
                if isinstance(c, dict):
                    cid = c.get('criterion_id')
                    ev = c.get('evidence')
                    if cid and ev:
                        reasons.append(f"{cid}: {ev}")
            updated.append(GateResult(gate=g.gate, status=status, reasons=reasons))
        else:
            updated.append(g)
    return updated


def _apply_addon(answers: Dict[str, Any]) -> List[GateResult]:
    answer_map = answers.get('results', {}) if isinstance(answers, dict) else {}
    addon_results: List[GateResult] = []
    for gate in sorted(ADDON_GATES):
        a = answer_map.get(gate)
        if not isinstance(a, dict):
            addon_results.append(GateResult(gate=gate, status='BLOCKED', reasons=['addon answers missing']))
            continue
        criteria = a.get('criteria', [])
        if not isinstance(criteria, list) or len(criteria) == 0:
            addon_results.append(GateResult(gate=gate, status='BLOCKED', reasons=['criteria list missing']))
            continue
        statuses = [c.get('status', '').upper() for c in criteria if isinstance(c, dict)]
        if any(s == 'FAIL' for s in statuses):
            status = 'FAIL'
        elif any(s == 'BLOCKED' for s in statuses):
            status = 'BLOCKED'
        elif all(s == 'PASS' for s in statuses):
            status = 'PASS'
        else:
            status = 'BLOCKED'
        reasons = []
        for c in criteria:
            if isinstance(c, dict):
                cid = c.get('criterion_id')
                ev = c.get('evidence')
                if cid and ev:
                    reasons.append(f"{cid}: {ev}")
        addon_results.append(GateResult(gate=gate, status=status, reasons=reasons))
    return addon_results


def _write_gate_logs(
    export_dir: Path,
    run_id: str,
    gate_results: List[GateResult],
    answers: Dict[str, Any],
    addon_results: List[GateResult] | None = None,
    addon_answers: Dict[str, Any] | None = None,
) -> None:
    gate_log = []
    answer_map = answers.get('results', {}) if isinstance(answers, dict) else {}
    for g in gate_results:
        criteria_entries = []
        a = answer_map.get(g.gate, {}) if g.gate in ASSISTED_GATES or g.gate in MANUAL_GATES else {}
        criteria = a.get('criteria', []) if isinstance(a, dict) else []
        if isinstance(criteria, list):
            for c in criteria:
                if isinstance(c, dict):
                    criteria_entries.append({
                        'criterion_id': c.get('criterion_id'),
                        'status': (c.get('status') or '').lower(),
                        'evidence': c.get('evidence')
                    })

        try:
            pipeline_step = int(g.gate.replace('Gate', ''))
        except ValueError:
            if g.gate == 'GateCR':
                pipeline_step = 85
            elif g.gate == 'GatePhase0':
                pipeline_step = 30
            elif g.gate == 'GatePFL':
                pipeline_step = 35
            elif g.gate == 'GateTRIZ':
                pipeline_step = 8
            else:
                pipeline_step = -1

        if g.gate == 'GateTRIZ':
            check_type = 'TRIZ'
            criteria_scope = 'TRIZ_CORE_ENGINE'
        elif g.gate == 'GatePhase0':
            check_type = 'PHASE0'
            criteria_scope = 'PHASE0'
        elif g.gate == 'GatePFL':
            check_type = 'PFL'
            criteria_scope = 'PFL'
        elif g.gate == 'GateCR':
            check_type = 'OPERATOR_CORE'
            criteria_scope = 'OPERATOR_CORE'
        else:
            check_type = 'ASSISTED' if g.gate in ASSISTED_GATES else 'AUTOMATED'
            criteria_scope = 'CANON'

        gate_log.append({
            'gate_log_entry_id': f"{run_id}-{g.gate}",
            'case_id': export_dir.name,
            'gate_id': g.gate,
            'pipeline_step': pipeline_step,
            'result': g.status.lower(),
            'check_type': check_type,
            'criteria_scope': criteria_scope,
            'criteria_results': criteria_entries,
            'reason': ', '.join(g.reasons or []),
            'normalized_reason_codes': [_normalize_reason_code(r) for r in (g.reasons or [])],
            'canon_ref': 'CANON_PIPELINE_v1.2',
            'run_id': run_id,
            'timestamp': run_id,
            'actor_type': 'system',
            'actor_user_id': None,
        })
    if addon_results:
        addon_map = addon_answers.get('results', {}) if isinstance(addon_answers, dict) else {}
        for g in addon_results:
            criteria_entries = []
            a = addon_map.get(g.gate, {}) if g.gate in ADDON_GATES else {}
            criteria = a.get('criteria', []) if isinstance(a, dict) else []
            if isinstance(criteria, list):
                for c in criteria:
                    if isinstance(c, dict):
                        criteria_entries.append({
                            'criterion_id': c.get('criterion_id'),
                            'status': (c.get('status') or '').lower(),
                            'evidence': c.get('evidence')
                        })
            gate_log.append({
                'gate_log_entry_id': f"{run_id}-{g.gate}",
                'case_id': export_dir.name,
                'gate_id': g.gate,
                'pipeline_step': int(g.gate.replace('Gate', '')),
                'result': g.status.lower(),
                'check_type': 'ASSISTED_ADDON',
                'criteria_scope': 'ADDON',
                'criteria_results': criteria_entries,
                'reason': ', '.join(g.reasons or []),
                'normalized_reason_codes': [_normalize_reason_code(r) for r in (g.reasons or [])],
                'canon_ref': 'TRIZ_CORE_ADDON_SPEC_v0.1',
                'run_id': run_id,
                'timestamp': run_id,
                'actor_type': 'system',
                'actor_user_id': None,
            })
    (export_dir / 'gate_log.json').write_text(json.dumps(gate_log, ensure_ascii=False, indent=2), encoding='utf-8')

    gate_summary = {
        'case_id': export_dir.name,
        'run_id': run_id,
        'latest': {g.gate: g.status.lower() for g in gate_results},
        'normalized_reason_codes': {
            g.gate: [_normalize_reason_code(r) for r in (g.reasons or [])]
            for g in gate_results
        },
    }
    if addon_results:
        for g in addon_results:
            gate_summary['latest'][g.gate] = g.status.lower()
    (export_dir / 'gate_summary.json').write_text(json.dumps(gate_summary, ensure_ascii=False, indent=2), encoding='utf-8')


def _export_package(
    tc_id: str,
    tc: Dict[str, Any],
    run_id: str,
    gate_results: List[GateResult],
    answers: Dict[str, Any],
    addon_results: List[GateResult] | None = None,
    addon_answers: Dict[str, Any] | None = None,
) -> Path:
    export_dir = EXPORTS_DIR / f"DSS_Output_Package_{tc_id}_{run_id}"
    art_dir = export_dir / 'artifacts'
    mech_dir = art_dir / 'S10_MECHANISM_SPECS'
    os.makedirs(mech_dir, exist_ok=True)

    step_map = _build_step_map(tc)

    def write_md(path: Path, title: str, payload: Any) -> None:
        content = f"# {title}\n\n" + json.dumps(payload, ensure_ascii=False, indent=2)
        path.write_text(content, encoding='utf-8')

    write_md(art_dir/'S00_CASE_SYMPTOM.md', 'CASE_SYMPTOM', step_map.get(0, {}))
    write_md(art_dir/'S01_PROBLEM_OWNER_CARD.md', 'PROBLEM_OWNER_CARD', step_map.get(1, {}))
    write_md(art_dir/'S02_SYSTEM_BOUNDARY_MAP.md', 'SYSTEM_BOUNDARY_MAP', step_map.get(2, {}))
    write_md(art_dir/'S03_INTERACTION_MAP.md', 'INTERACTION_MAP', step_map.get(3, {}))
    phase0_payload = {
        'phase0_enabled': tc.get('phase0_enabled', False),
        'phase0_verdict': tc.get('phase0_verdict'),
        'phase0_reason_code': tc.get('phase0_reason_code'),
        'canonical_hash': tc.get('canonical_hash'),
        'canonical_hash_v0': tc.get('canonical_hash_v0'),
        's2a_hash': tc.get('s2a_hash'),
        'canonical_hash_text': tc.get('canonical_hash_text'),
        'canonical_slots_v0': tc.get('canonical_slots_v0'),
        'raw_hash': tc.get('raw_hash'),
        'trace_count': tc.get('trace_count'),
        'confidence_summary': tc.get('confidence_summary'),
        'canonical_scope': tc.get('canonical_scope'),
        'canonical_X': tc.get('canonical_X'),
        'canonical_Y': tc.get('canonical_Y'),
        'canonical_constraints': tc.get('canonical_constraints'),
        'canonical_conflict_type_candidate_trace': tc.get('canonical_conflict_type_candidate_trace'),
        'phase0_trace': tc.get('phase0_trace', []),
    }
    write_md(art_dir/'S03_0_PHASE0_OUTPUT.md', 'PHASE0_OUTPUT', phase0_payload)
    pfl_payload = {
        'pfl_enabled': tc.get('pfl_enabled'),
        'pfl_status': tc.get('pfl_status'),
        'pfl_status_reason': tc.get('pfl_status_reason'),
        'pfl_verdict': tc.get('pfl_verdict'),
        'pfl_reason': tc.get('pfl_reason'),
        'pfl_attempt_index': tc.get('pfl_attempt_index'),
        'pfl_structural_tension': tc.get('pfl_structural_tension'),
        'pfl_conflict_type_candidate': tc.get('pfl_conflict_type_candidate'),
        'pfl_X': tc.get('pfl_X'),
        'pfl_Y': tc.get('pfl_Y'),
    }
    write_md(art_dir/'S03_5_PFL_OUTPUT.md', 'PFL_OUTPUT', pfl_payload)
    write_md(art_dir/'S04_CONTRADICTION_STATEMENT.md', 'CONTRADICTION_STATEMENT', step_map.get(4, {}))
    write_md(art_dir/'S05_IKR_CARD.md', 'IKR_CARD', step_map.get(5, {}))
    write_md(art_dir/'S06_HARD_BARRIER.md', 'HARD_BARRIER', step_map.get(6, {}))
    write_md(art_dir/'S07_RESOURCE_MAP.md', 'RESOURCE_MAP', step_map.get(7, {}))
    write_md(art_dir/'S08_FORM_SELECTION.md', 'FORM_SELECTION', step_map.get(8, {}))
    write_md(art_dir/'S08_5_OPERATOR_PROMPT.md', 'OPERATOR_PROMPT', (step_map.get(85, {}) or {}).get('operator_prompt', {}))
    gatecr_result = next((g for g in gate_results if g.gate == 'GateCR'), None)
    s85_payload = dict(step_map.get(85, {}) or {})
    s85_payload['gatecr_status_mirror'] = gatecr_result.status if gatecr_result else 'NOT_APPLICABLE'
    write_md(art_dir/'S08_5_OPERATOR_OUTPUT.md', 'OPERATOR_OUTPUT', s85_payload)
    write_md(art_dir/'S09_SOLUTION_SET.md', 'SOLUTION_SET', step_map.get(9, {}))
    write_md(art_dir/'S11_SECONDARY_CONTRADICTION_CHECK.md', 'SECONDARY_CONTRADICTION_CHECK', step_map.get(11, {}))
    write_md(art_dir/'S12_DECISION_RECORD.md', 'DECISION_RECORD', step_map.get(12, {}))
    write_md(art_dir/'S13_IMPLEMENTATION_MAP.md', 'IMPLEMENTATION_MAP', step_map.get(13, {}))
    write_md(art_dir/'S14_RULE_UPDATE.md', 'RULE_UPDATE', step_map.get(14, {}))
    s85 = step_map.get(85, {}) or {}
    schema_version_raw = tc.get('schema_version', 0)
    try:
        schema_version = float(str(schema_version_raw))
    except (ValueError, TypeError):
        schema_version = 0.0

    gatecr_record = {
        'status': gatecr_result.status if gatecr_result else 'NOT_APPLICABLE',
        'reasons': gatecr_result.reasons if gatecr_result else [],
        'normalized_reason_codes': [_normalize_reason_code(r) for r in (gatecr_result.reasons if gatecr_result else [])],
        'canonical_hard_fail_message': CANONICAL_HARD_FAIL_MESSAGE,
        'operator_core_enabled': (
            any(v in str((tc.get('canon_versions') or {}).get('schema') or '') for v in (
                'TEST_VECTOR_SCHEMA_v0.2',
                'TEST_VECTOR_SCHEMA_v0.3',
                'TEST_VECTOR_SCHEMA_v0.4',
            ))
            or bool(tc.get('operator_core_enabled'))
        ),
        'schema_version': schema_version_raw,
        'detected_conflict_types': s85.get('detected_conflict_types', []),
        'dominant_conflict_type': s85.get('dominant_conflict_type'),
        'operator_selected': s85.get('operator_selected'),
        'separation_illusion_test': s85.get('separation_illusion_test'),
        'search_loop': s85.get('search_loop'),
        'risk_shift_detected': bool(schema_version >= 0.4 and s85.get('search_loop') is True),
    }
    write_md(art_dir/'GATECR_RECORD.md', 'GATECR_RECORD', gatecr_record)

    specs = (step_map.get(10, {}) or {}).get('concept_specs', [])
    for idx, spec in enumerate(specs, start=1):
        fname = mech_dir / f"C{idx:02d}_MECHANISM_SPEC.md"
        write_md(fname, f"MECHANISM_SPEC C{idx:02d}", spec)

    _write_gate_logs(export_dir, run_id, gate_results, answers, addon_results, addon_answers)

    input_fingerprint = tc.get('input_fingerprint') or _input_fingerprint(tc, step_map)
    manual_override_used = bool(tc.get('manual_override_used', False))
    override_type = tc.get('override_type') if manual_override_used else None
    normalized_reason_codes = sorted({
        _normalize_reason_code(reason)
        for g in gate_results
        for reason in (g.reasons or [])
    })

    case_json = {
        'case_id': tc_id,
        'title': tc_id,
        'created_at': run_id,
        'updated_at': run_id,
        'case_version': 1,
        'status': 'done',
        'canon_versions': {
            'canon_pipeline_version': 'v1.2',
            'canon_9forms_version': 'v1.1'
        },
        'shell_versions': {
            'gate_automation_matrix_version': 'v0.1.1',
            'prd_version': 'v0.1',
            'ux_flow_version': 'v0.1',
            'export_spec_version': 'v0.1',
            'data_model_version': 'v0.1'
        },
        'pfl_status': tc.get('pfl_status'),
        'pfl_status_reason': tc.get('pfl_status_reason'),
        'pfl_verdict': tc.get('pfl_verdict'),
        'pfl_reason': tc.get('pfl_reason'),
        'pfl_attempt_index': tc.get('pfl_attempt_index'),
        'pfl_structural_tension': tc.get('pfl_structural_tension'),
        'instrumentation': {
            'input_fingerprint': input_fingerprint,
            'manual_override_used': manual_override_used,
            'override_type': override_type,
            'normalized_reason_codes': normalized_reason_codes,
            'gatecr_status_mirror': gatecr_result.status if gatecr_result else 'NOT_APPLICABLE',
            'phase0_verdict': tc.get('phase0_verdict'),
            'phase0_reason_code': tc.get('phase0_reason_code'),
            'canonical_hash': tc.get('canonical_hash'),
            'raw_hash': tc.get('raw_hash'),
            'trace_count': tc.get('trace_count'),
            'confidence_summary': tc.get('confidence_summary'),
            'reconstruction_trace': tc.get('phase0_trace', []),
            'canonical_object': {
                'system_scope': tc.get('canonical_scope'),
                'X_param': tc.get('canonical_X'),
                'Y_param': tc.get('canonical_Y'),
                'constraints': tc.get('canonical_constraints'),
                'conflict_type_candidate': tc.get('canonical_conflict_type_candidate'),
                'conflict_type_candidate_trace': tc.get('canonical_conflict_type_candidate_trace'),
                's2a_hash': tc.get('s2a_hash'),
            },
            'pfl_status': tc.get('pfl_status'),
            'pfl_status_reason': tc.get('pfl_status_reason'),
            'pfl_verdict': tc.get('pfl_verdict'),
            'pfl_reason': tc.get('pfl_reason'),
            'pfl_attempt_index': tc.get('pfl_attempt_index'),
            'pfl_structural_tension': tc.get('pfl_structural_tension'),
        },
    }
    (export_dir / 'case.json').write_text(json.dumps(case_json, ensure_ascii=False, indent=2), encoding='utf-8')

    # manifest
    def sha256(path: Path) -> str:
        import hashlib
        h = hashlib.sha256()
        with path.open('rb') as f:
            for chunk in iter(lambda: f.read(8192), b''):
                h.update(chunk)
        return h.hexdigest()

    files = []
    for path in [export_dir / 'case.json', export_dir / 'gate_log.json', export_dir / 'gate_summary.json'] + list(art_dir.rglob('*.md')):
        rel = path.relative_to(export_dir)
        files.append({
            'path': str(rel),
            'sha256': sha256(path),
            'size_bytes': path.stat().st_size,
            'artifact_type': 'meta' if path.name.endswith('.json') else 'artifact',
            'artifact_version_id': None,
        })

    manifest = {
        'bundle_id': f"DSS_Output_Package_{run_id}",
        'bundle_name': 'DSS_Output_Package',
        'case_id': tc_id,
        'case_version': 1,
        'run_id': run_id,
        'exported_at': run_id,
        'canon_versions': {
            'canon_pipeline_version': 'v1.2',
            'canon_9forms_version': 'v1.1'
        },
        'shell_versions': {
            'gate_automation_matrix_version': 'v0.1.1',
            'prd_version': 'v0.1',
            'ux_flow_version': 'v0.1',
            'export_spec_version': 'v0.1',
            'data_model_version': 'v0.1'
        },
        'files': files,
        'required_artifacts_check': {
            'missing_files': []
        }
    }
    (export_dir / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')

    return export_dir


def run_tc(
    tc_id: str | None,
    answers_path: str | None,
    tc_path: str | None,
    addon_answers_path: str | None,
    addon_strict: bool,
) -> None:
    if tc_path:
        tc = _load_tc_path(Path(tc_path))
        tc_id = tc.get('test_case_id') or 'UNKNOWN_TC'
    else:
        if not tc_id:
            raise SystemExit('Missing --tc or --tc-path')
        tc = _load_tc(tc_id)
    step_map = _build_step_map(tc)

    if _phase0_enabled(tc):
        phase0 = _run_phase0(tc, step_map)
        # merge Phase0 outputs into tc for export payloads
        tc.update(phase0)

        # Trace-only mapping: preserve external instrumentation conflict type candidate
        # without affecting canonical compute/hash fields.
        instrumentation = tc.get('instrumentation') if isinstance(tc.get('instrumentation'), dict) else {}
        canonical_obj_trace = instrumentation.get('canonical_object') if isinstance(instrumentation.get('canonical_object'), dict) else {}
        trace_conflict = canonical_obj_trace.get('conflict_type_candidate')
        if trace_conflict is not None and str(trace_conflict).strip():
            tc['canonical_conflict_type_candidate_trace'] = _normalize_scalar(trace_conflict)

        tc.update({
            'phase0_enabled': True,
            'phase0_verdict': phase0['phase0_verdict'],
            'phase0_reason_code': phase0['phase0_reason_code'],
            'canonical_hash': phase0['canonical_hash'],
            's2a_hash': phase0['s2a_hash'],
            'raw_hash': phase0['raw_hash'],
            'phase0_trace': phase0['phase0_trace'],
            'trace_count': phase0['trace_count'],
            'confidence_summary': phase0['confidence_summary'],
            'canonical_scope': phase0['canonical_scope'],
            'canonical_X': phase0['canonical_X'],
            'canonical_Y': phase0['canonical_Y'],
            'canonical_constraints': phase0['canonical_constraints'],
            'canonical_conflict_type_candidate': phase0['canonical_conflict_type_candidate'],
            'input_fingerprint': phase0['canonical_hash'],
        })
        # Admission must consume canonical fields only.
        tc['pfl_X'] = phase0['canonical_X']
        tc['pfl_Y'] = phase0['canonical_Y']
        tc['pfl_conflict_type_candidate'] = phase0['canonical_conflict_type_candidate']
        tc.update(compute_pfl_v0_1(tc))
        tc['pfl_status'] = 'PFL_READY'
        tc['pfl_status_reason'] = 'PFL v0.1 compute executed from canonical fields'
        if 'full_vector' not in tc or not isinstance(tc['full_vector'], dict):
            tc['full_vector'] = {}
        step1 = tc['full_vector'].setdefault('step_1', {})
        if isinstance(step1, dict):
            step1['owner_scope'] = phase0['canonical_scope']
            step1['constraints'] = phase0['canonical_constraints']
        step_map = _build_step_map(tc)

    structural_results = run_structural_gates(tc, step_map)

    if answers_path is None:
        raise SystemExit('Missing --answers for assisted gates')

    answers = _load_semantic_answers(Path(answers_path))
    gate_results = _apply_semantic(structural_results, answers)

    addon_results: List[GateResult] = []
    addon_answers = {}
    if addon_answers_path:
        addon_answers = _load_semantic_answers(Path(addon_answers_path))
        addon_results = _apply_addon(addon_answers)
        if addon_strict:
            gate_results = gate_results + addon_results

    # TRIZ core validation (mandatory)
    triz_result = triz_validate(tc, answers, None)
    if triz_result.get('status') != 'VALID':
        reasons = []
        for r in triz_result.get('fail_reasons', []):
            code = r.get('code')
            msg = r.get('msg')
            path = r.get('path')
            if code or msg or path:
                reasons.append(f"{code}: {msg} ({path})")
        if not reasons:
            reasons = ['TRIZ_CORE_ENGINE invalid']
        gate_results.append(GateResult(gate='GateTRIZ', status='FAIL', reasons=reasons))
    else:
        gate_results.append(GateResult(gate='GateTRIZ', status='PASS', reasons=[]))

    run_id = _now_stamp()
    os.makedirs(EVIDENCE_DIR, exist_ok=True)

    run_path = EVIDENCE_DIR / f"RUN_{tc_id}_{run_id}.yaml"
    bug_path = EVIDENCE_DIR / f"BUGLIST_{tc_id}_{run_id}.yaml"

    _write_yaml(run_path, _evidence_yaml(tc_id, run_id, gate_results))
    _write_yaml(bug_path, _buglist_yaml(tc_id, run_id, gate_results))

    export_dir = _export_package(tc_id, tc, run_id, gate_results, answers, addon_results, addon_answers)

    print(f"Wrote: {run_path}")
    print(f"Wrote: {bug_path}")
    print(f"Export: {export_dir}")


def main() -> None:
    parser = argparse.ArgumentParser(description='DSS Solver Harness (structural + assisted)')
    sub = parser.add_subparsers(dest='command', required=True)

    run_cmd = sub.add_parser('run', help='Run DSS solver harness')
    run_cmd.add_argument('--tc', required=False, help='Test case id, e.g., TC_DSS01')
    run_cmd.add_argument('--tc-path', required=False, help='Path to test case YAML')
    run_cmd.add_argument('--answers', required=True, help='Path to semantic answers YAML')
    run_cmd.add_argument('--addon-answers', required=False, help='Path to addon answers YAML (Gate15–18)')
    run_cmd.add_argument('--addon-strict', action='store_true', help='Make addon gates decision‑critical')

    args = parser.parse_args()

    if args.command == 'run':
        run_tc(args.tc, args.answers, args.tc_path, args.addon_answers, args.addon_strict)


if __name__ == '__main__':
    main()
