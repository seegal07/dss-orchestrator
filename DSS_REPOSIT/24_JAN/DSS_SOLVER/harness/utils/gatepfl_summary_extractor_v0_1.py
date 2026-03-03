#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, Iterable, Iterator, List, Optional, Tuple


def _iter_dict_nodes(obj: Any) -> Iterator[Dict[str, Any]]:
    stack: List[Any] = [obj]
    while stack:
        current = stack.pop()
        if isinstance(current, dict):
            yield current
            for value in current.values():
                stack.append(value)
        elif isinstance(current, list):
            for item in reversed(current):
                stack.append(item)


def _extract_gate_entry(gate_log: Any, gate_id: str) -> Tuple[bool, Optional[Dict[str, Any]]]:
    matched: List[Dict[str, Any]] = []
    for node in _iter_dict_nodes(gate_log):
        if node.get("gate_id") == gate_id:
            matched.append(node)
    if not matched:
        return False, None
    return True, matched[-1]


def _load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def _load_summary(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {"variants": {}}
    data = _load_json(path)
    if not isinstance(data, dict):
        raise RuntimeError(f"SUMMARY.json must be an object: {path}")
    if not isinstance(data.get("variants"), dict):
        data["variants"] = {}
    return data


def _variant_dirs(exports_dir: Path) -> List[Path]:
    if not exports_dir.exists():
        return []
    return sorted([p for p in exports_dir.iterdir() if p.is_dir()])


def patch_summary(pack_path: Path, gate_id: str) -> Path:
    summary_path = pack_path / "SUMMARY.json"
    summary = _load_summary(summary_path)

    exports_dir = pack_path / "EXPORTS"
    variants = _variant_dirs(exports_dir)
    if not variants:
        raise RuntimeError(f"No variant folders found in EXPORTS: {exports_dir}")

    for variant_dir in variants:
        variant_name = variant_dir.name
        gate_log_path = variant_dir / "gate_log.json"
        if not gate_log_path.exists():
            continue

        gate_log = _load_json(gate_log_path)
        has_gate, gate_entry = _extract_gate_entry(gate_log, gate_id)

        result: Optional[str] = None
        reason: Optional[str] = None
        if has_gate and gate_entry is not None:
            raw_result = gate_entry.get("result")
            raw_reason = gate_entry.get("reason")
            if raw_result is None or raw_reason is None:
                raise RuntimeError(
                    f"{gate_log_path}: {gate_id} exists but result/reason is null "
                    f"(result={raw_result!r}, reason={raw_reason!r})"
                )
            result = str(raw_result)
            reason = str(raw_reason)

        variant_summary = summary["variants"].get(variant_name)
        if not isinstance(variant_summary, dict):
            variant_summary = {}
        variant_summary["GatePFL_result"] = result
        variant_summary["GatePFL_reason"] = reason
        summary["variants"][variant_name] = variant_summary

    with summary_path.open("w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
        f.write("\n")
    return summary_path


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Patch SUMMARY.json with GatePFL result/reason from gate_log.json using JSON parsing only."
    )
    parser.add_argument("--pack-path", required=True, help="Path to experiment pack containing EXPORTS and SUMMARY.json")
    parser.add_argument("--gate-id", default="GatePFL", help="Gate id to extract from gate_log.json (default: GatePFL)")
    args = parser.parse_args()

    pack_path = Path(args.pack_path)
    if not pack_path.exists():
        raise SystemExit(f"Pack path does not exist: {pack_path}")

    summary_path = patch_summary(pack_path=pack_path, gate_id=args.gate_id)
    print(f"SUMMARY_PATCHED={summary_path}")


if __name__ == "__main__":
    main()
