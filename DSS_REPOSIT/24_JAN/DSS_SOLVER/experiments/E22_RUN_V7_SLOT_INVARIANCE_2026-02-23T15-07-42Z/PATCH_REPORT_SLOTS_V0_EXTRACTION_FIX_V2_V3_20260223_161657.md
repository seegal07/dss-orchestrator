# PATCH_REPORT

## Updated metric token list excerpt
12-
13-    metric = None
14:    metric_stems = [
15-        ("точност", "точность"),
16-        ("время", "время"),
--
19-        ("расход", "расход"),
20-        ("бюджет", "бюджет"),
21:        ("скорост", "скорость"),
22:        ("темп", "темп"),
23-        ("качеств", "качество"),
24:        ("прогноз", "прогноз"),
25:        ("предоцен", "предоцен"),
26-    ]
27:    for stem, label in metric_stems:
28-        if stem in t:
29-            metric = label

## Updated direction precedence logic excerpt
16-    y_dir = _direction_enum(canonical_Y_display)
17-
18:    # Direction precedence: if metric indicates speed/pace, force accelerate.
19:    if x_metric in {"темп", "скорость"}:
20:        x_dir = "accelerate"
21:    if y_metric in {"темп", "скорость"}:
22:        y_dir = "accelerate"
23-
24-    trace_markers = []

## Updated object chunk extraction excerpt
10-            break
11-
12:    obj = None
13:    tokens = re.findall(r"[\w-]+", t)
14:    stop_tokens = {"при", "по", "в", "до", "на", "для", "с", "из"}
15-
16:    filial_idx = None
17-    for i, tok in enumerate(tokens):
18-        if "филиал" in tok:
19:            filial_idx = i
20-            break
21-
22:    if filial_idx is not None:
23:        chunk = [tokens[filial_idx]]
24:        for j in range(filial_idx + 1, min(filial_idx + 3, len(tokens))):
25-            nxt = tokens[j]
26:            if nxt in stop_tokens:
27-                break
28:            chunk.append(nxt)
29:        obj = " ".join(chunk)
30-
31-    if obj is None:
--
33-            m = re.search(rf"(\b\w{{0,12}}{re.escape(stem)}\w{{0,12}}\b(?:\s+\b\w+\b){{0,2}})", t)
34-            if m:
35:                obj = m.group(1)
36-                break
37-
--
40-    return metric, (obj[:120] if obj else None)
41-def _build_slots_v0(canonical_X_display: str, canonical_Y_display: str, scope: str, constraints):
42:    x_metric, x_obj = _extract_metric_object(canonical_X_display)
43:    y_metric, y_obj = _extract_metric_object(canonical_Y_display)
44-
45-    x_dir = _direction_enum(canonical_X_display)

## Static confirmations
- No other repository files changed in this patch task (targeted edit: harness.py).
- NO_RUN: YES
- No large dictionaries introduced; only small closed lists (metric_stems + stop_tokens).
