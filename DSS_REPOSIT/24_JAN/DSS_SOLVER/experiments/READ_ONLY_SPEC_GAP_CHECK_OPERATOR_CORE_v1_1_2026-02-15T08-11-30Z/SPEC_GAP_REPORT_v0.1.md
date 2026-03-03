# SPEC_GAP_REPORT_v0.1

Scope: Operator Core v1.1 governance vs current repo implementation (read-only check, no runs).

## Mandatory answers

1. **Where is conflict_type stored?**
- Input/runtime storage: `full_vector.step_8_5.detected_conflict_types[]` and `full_vector.step_8_5.dominant_conflict_type`.
  - Ref: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/governance/TEST_VECTOR_SCHEMA_v0.2.md`
  - Ref: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/harness/gates_structural.py` (`gatecr_operator_core`)
- Export/evidence storage: `artifacts/GATECR_RECORD.md` includes both fields.
  - Ref: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/harness/harness.py`

2. **Can S08.5 be inserted between S08 and S09?**
- Yes. Implemented.
- Parsing supports `step_8_5` mapped to internal step key `85`.
- GateCR executes after Gate8 and before Gate9 when Operator Core is enabled.
  - Ref: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/harness/harness.py` (`_build_step_map`)
  - Ref: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/harness/gates_structural.py` (`run_structural_gates`)

3. **Where is GateCR invoked in harness?**
- Invocation point: `run_structural_gates()` in `harness/gates_structural.py`.
- Evaluator: `gatecr_operator_core(step_map)`.
- Trigger condition: `_is_operator_core_enabled(tc)`.

4. **Is iteration counter supported?**
- For Operator Core/GateCR: No iteration counter in harness runtime.
- DCF round counters exist only in governance specs (`DCF_DATA_MODEL_v1.0.md`), not in harness runtime logic.

5. **Can compromise_mode be supported in current schema?**
- Yes. Supported.
- Schema includes `step_12.compromise_mode`.
- Gate12 enforces `compromise_mode == true` when GateCR status is `SOFT_FAIL`.
  - Ref: `governance/TEST_VECTOR_SCHEMA_v0.2.md`
  - Ref: `harness/gates_structural.py` (`gate12_decision_record`)

6. **Which files must change?**
- For current v1.1 Operator Core baseline: no mandatory code changes detected.
- Optional alignment-only changes (if required by process strictness):
  - Add explicit runtime note in governance that mode rules are documentary unless implemented in harness.
  - Add explicit statement whether prefilled `step_8_5.gatecr_status` is ignored at runtime (currently computed by harness).

7. **Any conflicts with harness control flow?**
- No blocking control-flow conflict for GateCR routing:
  - HARD_FAIL correctly forces S09–S14 to `NOT_RUN`.
  - SOFT_FAIL allows downstream.
- Noted interaction: existing Gate12 block rule (`Gate9/Gate11 FAIL -> Gate12 NOT_RUN`) still applies and is compatible.

8. **Any schema conflicts with TEST_VECTOR_SCHEMA_v0.2?**
- No hard conflicts.
- Minor implementation nuance:
  - Schema allows/presents `step_8_5.gatecr_status` and `hard_fail_message` as fields.
  - Runtime treats GateCR result as computed source-of-truth; input values are not authoritative.

9. **Does canonical HARD_FAIL literal already match spec?**
- Yes.
- Runtime constant: `structural resolution not found`.
- Governance literals match same exact string.
  - Ref: `harness/gates_structural.py`, `harness/harness.py`, `governance/OPERATOR_CORE_ROUTING_RULES_v1.1.md`, `governance/OWNER_POLICY_DECISIONS_v1.1.md`, `governance/GATECR_SPEC_v1.1.md`.

## Conclusion
- Operator Core v1.1 is materially wired in runtime and aligned on key enforcement points.
- Main gap is documentation/runtime-boundary clarity (mode governance vs executable harness), not GateCR routing logic.
