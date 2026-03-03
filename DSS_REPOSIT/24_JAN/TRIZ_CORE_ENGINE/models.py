from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class FailReason:
    code: str
    msg: str
    path: str


@dataclass
class TRIZArtifacts:
    physical_contradiction: Optional[Dict[str, Any]]
    separation: Optional[Dict[str, Any]]
    system_operator: Optional[Dict[str, Any]]
    transformation_model: Optional[Dict[str, Any]]
    non_obviousness_check: Optional[Dict[str, Any]]


@dataclass
class TRIZValidationResult:
    status: str  # VALID | INVALID
    fail_reasons: List[FailReason]
    artifacts: TRIZArtifacts
