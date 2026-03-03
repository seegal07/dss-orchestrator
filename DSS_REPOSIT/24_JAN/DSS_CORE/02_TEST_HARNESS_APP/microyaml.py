"""Minimal YAML subset loader.

Supports:
- dicts and lists
- strings (quoted or unquoted), ints, booleans
- inline lists: [a, b, "c"]
- indentation with 2 spaces

This is intentionally small to avoid external dependencies.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, List, Tuple


@dataclass
class Line:
    raw: str
    indent: int
    text: str


def _strip_comments(line: str) -> str:
    # Remove comments only if they start the line or are preceded by space
    if '#' not in line:
        return line
    out = []
    in_quotes = False
    quote_char = ''
    for i, ch in enumerate(line):
        if ch in ('"', "'"):
            if not in_quotes:
                in_quotes = True
                quote_char = ch
            elif quote_char == ch:
                in_quotes = False
        if ch == '#' and not in_quotes:
            return ''.join(out)
        out.append(ch)
    return ''.join(out)


def _preprocess(text: str) -> List[Line]:
    lines = []
    for raw in text.splitlines():
        raw = _strip_comments(raw)
        if not raw.strip():
            continue
        indent = len(raw) - len(raw.lstrip(' '))
        lines.append(Line(raw=raw, indent=indent, text=raw.strip()))
    return lines


def _parse_scalar(value: str) -> Any:
    value = value.strip()
    if value == '':
        return ''
    if value.startswith('"') and value.endswith('"'):
        return value[1:-1]
    if value.startswith("'") and value.endswith("'"):
        return value[1:-1]
    if value.lower() in ('true', 'false'):
        return value.lower() == 'true'
    if value.lower() in ('null', 'none'):
        return None
    # Inline list
    if value.startswith('[') and value.endswith(']'):
        inner = value[1:-1].strip()
        if not inner:
            return []
        parts = [p.strip() for p in inner.split(',')]
        return [_parse_scalar(p) for p in parts]
    # Integer
    if value.isdigit() or (value.startswith('-') and value[1:].isdigit()):
        try:
            return int(value)
        except ValueError:
            pass
    return value


def _split_key_value(text: str) -> Tuple[str, str]:
    if ':' not in text:
        return text, ''
    key, value = text.split(':', 1)
    return key.strip(), value.strip()


def _parse_block(lines: List[Line], start: int, indent: int) -> Tuple[Any, int]:
    obj = None
    i = start
    while i < len(lines):
        line = lines[i]
        if line.indent < indent:
            break
        if line.indent > indent:
            raise ValueError(f"Unexpected indent at line: {line.raw}")

        text = line.text
        if text.startswith('- '):
            if obj is None:
                obj = []
            if not isinstance(obj, list):
                raise ValueError("Mixed list/dict in YAML")
            item_text = text[2:].strip()
            if item_text == '':
                item, i = _parse_block(lines, i + 1, indent + 2)
                obj.append(item)
                continue
            if ':' in item_text:
                key, value = _split_key_value(item_text)
                if value == '':
                    child, i = _parse_block(lines, i + 1, indent + 2)
                    obj.append({key: child})
                else:
                    item = {key: _parse_scalar(value)}
                    # Allow additional keys for this list item
                    if i + 1 < len(lines) and lines[i + 1].indent > indent:
                        child, i = _parse_block(lines, i + 1, indent + 2)
                        if not isinstance(child, dict):
                            raise ValueError("List item mapping expects dict child")
                        item.update(child)
                    else:
                        i += 1
                    obj.append(item)
                continue
            obj.append(_parse_scalar(item_text))
            i += 1
            continue

        # dict entry
        if obj is None:
            obj = {}
        if not isinstance(obj, dict):
            raise ValueError("Mixed list/dict in YAML")

        key, value = _split_key_value(text)
        if value == '':
            child, i = _parse_block(lines, i + 1, indent + 2)
            obj[key] = child
        else:
            obj[key] = _parse_scalar(value)
            i += 1

    if obj is None:
        obj = {}
    return obj, i


def load(path: str) -> Any:
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    lines = _preprocess(text)
    data, _ = _parse_block(lines, 0, 0)
    return data
