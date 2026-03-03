from __future__ import annotations

from typing import Any, Dict, List

from .validators import validate_triz_core as _validate_triz_core


def validate_triz_core(tc: Dict[str, Any], semantic: Dict[str, Any] | None, gate_log: List[Dict[str, Any]] | None) -> Dict[str, Any]:
    """Public API: validate TRIZ core requirements.

    Args:
        tc: Test case dict.
        semantic: semantic answers dict (optional).
        gate_log: existing gate log list (optional).
    Returns:
        dict with status, fail_reasons, artifacts.
    """
    return _validate_triz_core(tc, semantic, gate_log)
