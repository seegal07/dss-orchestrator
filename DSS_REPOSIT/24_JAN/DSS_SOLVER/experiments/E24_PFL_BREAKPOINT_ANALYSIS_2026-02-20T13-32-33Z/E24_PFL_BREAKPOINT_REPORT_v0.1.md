# E24_PFL_BREAKPOINT_REPORT_v0.1

## Evidence set (exact paths of artifacts analyzed)
- `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/E22_E23_VARIABILITY_PACK_2026-02-20T11-39-12Z/RUN_EXPORT_SNIPPETS/E22_V1_export.json`
- `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/E22_E23_VARIABILITY_PACK_2026-02-20T11-39-12Z/RUN_EXPORT_SNIPPETS/E22_V2_export.json`
- `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/E22_E23_VARIABILITY_PACK_2026-02-20T11-39-12Z/RUN_EXPORT_SNIPPETS/E22_V3_export.json`
- `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/E22_E23_VARIABILITY_PACK_2026-02-20T11-39-12Z/CASE_INPUT_VARIANTS/V1_input.txt`
- `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/E22_E23_VARIABILITY_PACK_2026-02-20T11-39-12Z/CASE_INPUT_VARIANTS/V2_input.txt`
- `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/E22_E23_VARIABILITY_PACK_2026-02-20T11-39-12Z/CASE_INPUT_VARIANTS/V3_input.txt`
- `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/exports/DSS_Output_Package_TC_E22_V1_2026-02-20T11-39-12Z/artifacts/S01_PROBLEM_OWNER_CARD.md`
- `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/exports/DSS_Output_Package_TC_E22_V2_2026-02-20T11-39-14Z/artifacts/S01_PROBLEM_OWNER_CARD.md`
- `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/exports/DSS_Output_Package_TC_E22_V3_2026-02-20T11-39-15Z/artifacts/S01_PROBLEM_OWNER_CARD.md`
- `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/exports/DSS_Output_Package_TC_E22_V2_2026-02-20T11-39-14Z/gate_log.json`

## DIFF_MAP (V1 vs V2 vs V3: what changed)
- Unchanged fields:
  - `system_scope` = `правило запуска новых филиалов в Европе`
  - `constraints` (S01) = `не раздувать исследовательский бюджет/срок`
  - `boundary` (S02) = same text across V1/V2/V3
  - `manual_override_used` = `false`
  - `search_loop` = `true`
  - `attempt_index` = `1`
- Linguistically changed only:
  - `X` text (V1/V2/V3 wording differs)
  - `Y` text (V1/V2/V3 wording differs)
- Structurally changed outputs:
  - `pfl_verdict`: V1=`PASS`, V2=`FAIL`, V3=`PASS`
  - `pfl_reason`: V1=`NONE`, V2=`SOLUTION_AS_XY`, V3=`NONE`

## Trigger Hypothesis (minimum differentiating trigger for SOLUTION_AS_XY)
- Minimum differentiating fragment in V2 X: `сделать`.
- Working hypothesis: V2 token `сделать` hits action-verb heuristic (`сдела*`) and is classified as `SOLUTION_AS_XY`.
- Evidence anchor: V2 fails with `pfl_reason=SOLUTION_AS_XY`, while V1/V3 (same scope/constraints, no action-verb token in X) pass.

## Strictness vs Softness findings
### False Reject Candidates
- Candidate FR-01:
  - Same semantic intent for X/Y and same scope/constraints across V1/V2/V3.
  - Only V2 rejected with `SOLUTION_AS_XY`.
  - Evidence: `E22_V1_export.json`, `E22_V2_export.json`, `E22_V3_export.json`, `V1_input.txt`, `V2_input.txt`, `V3_input.txt`.

### False Admit Candidates
- No evidence in scope.

## Breakpoint localization (answer 4 questions)
1. Breakpoint layer:
- Primary: `(b) XY classification`
- Secondary: `(a) extraction/parsing heuristic trigger`

2. Dependency type:
- `(a) linguistic patterns`
- `(c) action verbs`
- Evidence: single-token wording shift in V2 X correlates with verdict flip.

3. Scope estimate:
- `pattern class` (verb-sensitive classification), not single-case random noise.

4. Input protocol clarifications needed (no design):
- Clarify that X/Y must be state/constraint statements, not action phrases.
- Clarify that mechanism verbs (`сделать`, `внедрить`, `запустить`) are disallowed in X/Y wording.
- Clarify separate slots: `X/Y` vs `mechanism/action` to avoid mixed phrasing.

## Input protocol clarifications (1–3)
- X/Y: only system tension statement (state/constraint), no action verbs.
- Mechanism language must not appear in X/Y line.
- If unsure, rewrite X/Y as measurable state pair before PFL submission.
