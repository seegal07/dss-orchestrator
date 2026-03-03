"""Minimal Harness CLI for DSS_TRIZ_Business.

Reads SoT test cases and runs Gate0–Gate3 checks.
Writes evidence files to SOT/evidence.
"""
from __future__ import annotations

import argparse
import datetime as dt
import os
from typing import Any, Dict, List

from microyaml import load as yaml_load
from gates import run_mvp_gates

ROOT = "/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN"
SOT_DIR = os.path.join(ROOT, "КВ_24_MAIN", "SOT")
TESTS_DIR = os.path.join(SOT_DIR, "tests")
SCHEMA_PATH = os.path.join(SOT_DIR, "schema", "test_vector_schema.yaml")
EVIDENCE_DIR = os.path.join(SOT_DIR, "evidence")


def _now_stamp() -> str:
    return dt.datetime.utcnow().strftime("%Y-%m-%dT%H-%M-%SZ")


def _load_tc(tc_id: str) -> Dict[str, Any]:
    path = os.path.join(TESTS_DIR, f"{tc_id}.yaml")
    if not os.path.exists(path):
        raise FileNotFoundError(f"Test case not found: {path}")
    return yaml_load(path)


def _build_step_map(artifact_pack: List[Dict[str, Any]]) -> Dict[int, Dict[str, Any]]:
    step_map = {}
    for item in artifact_pack or []:
        step = item.get('pipeline_step')
        if isinstance(step, int):
            step_map[step] = item
        else:
            # attempt to parse numeric step if it is string
            try:
                step_map[int(step)] = item
            except Exception:
                pass
    return step_map


def _overall_status(gate_results: List[Any]) -> str:
    statuses = [g.status for g in gate_results]
    if 'BLOCKED' in statuses:
        return 'BLOCKED'
    if 'FAIL' in statuses:
        return 'FAIL'
    if all(s == 'PASS' for s in statuses if s != 'NOT_RUN'):
        return 'PASS'
    return 'PARTIAL'


def _write_yaml(path: str, data: str) -> None:
    with open(path, 'w', encoding='utf-8') as f:
        f.write(data)


def _evidence_yaml(tc_id: str, run_id: str, gate_results: List[Any]) -> str:
    lines = []
    lines.append(f"run_id: {run_id}")
    lines.append(f"test_case_id: {tc_id}")
    lines.append("harness_version: v0.1.0")
    lines.append(f"timestamp_utc: {run_id}")
    lines.append(f"overall_status: {_overall_status(gate_results)}")
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


def _buglist_yaml(tc_id: str, run_id: str, gate_results: List[Any]) -> str:
    lines = []
    lines.append(f"run_id: {run_id}")
    lines.append(f"test_case_id: {tc_id}")
    lines.append("issues:")
    for g in gate_results:
        if g.status in ('FAIL', 'BLOCKED'):
            for r in g.reasons:
                lines.append(f"  - gate: {g.gate}")
                lines.append("    issue_code: STRUCTURAL")
                lines.append(f"    message: \"{r}\"")
    if len(lines) == 3:
        lines.append("  - gate: NONE")
        lines.append("    issue_code: NONE")
        lines.append("    message: \"No issues\"")
    return "\n".join(lines) + "\n"


def run_tc(tc_id: str) -> None:
    tc = _load_tc(tc_id)
    artifact_pack = tc.get('artifact_pack') or []
    step_map = _build_step_map(artifact_pack)

    gate_results = run_mvp_gates(tc, step_map)

    run_id = _now_stamp()
    os.makedirs(EVIDENCE_DIR, exist_ok=True)
    run_path = os.path.join(EVIDENCE_DIR, f"RUN_{tc_id}_{run_id}.yaml")
    bug_path = os.path.join(EVIDENCE_DIR, f"BUGLIST_{tc_id}_{run_id}.yaml")

    _write_yaml(run_path, _evidence_yaml(tc_id, run_id, gate_results))
    _write_yaml(bug_path, _buglist_yaml(tc_id, run_id, gate_results))

    print(f"Wrote: {run_path}")
    print(f"Wrote: {bug_path}")


def main() -> None:
    parser = argparse.ArgumentParser(description="DSS_TRIZ_Business Harness")
    sub = parser.add_subparsers(dest='command', required=True)

    run_cmd = sub.add_parser('run', help='Run gates on a test case')
    run_cmd.add_argument('--tc', required=True, help='Test case id, e.g., TC04')

    args = parser.parse_args()

    if args.command == 'run':
        run_tc(args.tc)


if __name__ == '__main__':
    main()
