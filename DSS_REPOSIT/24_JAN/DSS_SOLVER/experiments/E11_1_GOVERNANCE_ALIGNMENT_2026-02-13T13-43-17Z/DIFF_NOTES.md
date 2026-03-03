# DIFF_NOTES

## Conceptual changes from v1.0 to v1.1
1) Propagation scope alignment:
- HARD_FAIL scope unified to S09–S14 (spec + routing + owner policy).

2) Canonical message lock:
- Exact canonical HARD_FAIL literal defined and synchronized:
  - `structural resolution not found`

3) Phase-bound qualifier:
- Explicitly added that no-code restriction belongs to fixation phase only.
- E12 integration patch path explicitly allowed when authorized.

## Unchanged
- Tri-state model remains PASS / SOFT_FAIL / HARD_FAIL.
- Gate9–Gate12 semantics unchanged.
- DCF/SDP unchanged.
- 40 principles and 9 forms not activated as mandatory generation.
