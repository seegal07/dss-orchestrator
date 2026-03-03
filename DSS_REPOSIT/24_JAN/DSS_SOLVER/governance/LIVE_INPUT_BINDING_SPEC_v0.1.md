# LIVE_INPUT_BINDING_SPEC_v0.1
Status: ACTIVE
Class: Governance SoT Binding Spec
Scope: Binding contract only (LIVE_INPUT_PROTOCOL -> runtime objects -> Phase0 artifacts)

## 1) Purpose
- Define binding contract from `LIVE_INPUT_PROTOCOL_v0.1` field names into runtime object locations and exported artifacts.
- Define only wiring/contract; no semantic extraction rules are introduced here.

## 2) Runtime objects and truth-sources (names only)
- `tc` (runtime test case dict used by harness)
- `case.json` (export object)
- `S03_0_PHASE0_OUTPUT.md` (Phase0 artifact)
- `gate_log.json` / `gate_summary.json` (GatePFL truth-source)

## 3) Field mapping (normative)
| Protocol key | Runtime destination key in `tc` | Export location | Required/Optional |
|---|---|---|---|
| `SCOPE` | `full_vector.step_1.owner_scope` | `S03_0_PHASE0_OUTPUT.md` as `canonical_scope`; `case.json` as `instrumentation.canonical_object.system_scope` | Required |
| `TIMEFRAME_DEADLINE` | `NOT_SPECIFIED` | `NOT_SPECIFIED` | Optional |
| `CONSTRAINT_*` | `full_vector.step_1.constraints` (list) | `S03_0_PHASE0_OUTPUT.md` as `canonical_constraints`; `case.json` as `instrumentation.canonical_object.constraints` | Required |
| `X_METRIC` | `NOT_SPECIFIED` | `NOT_SPECIFIED` | Required |
| `X_OBJECT` | `NOT_SPECIFIED` | `NOT_SPECIFIED` | Required |
| `X_METRIC_POLARITY` | `NOT_SPECIFIED` | `NOT_SPECIFIED` | Optional |
| `Y_METRIC` | `NOT_SPECIFIED` | `NOT_SPECIFIED` | Required |
| `Y_OBJECT` | `NOT_SPECIFIED` | `NOT_SPECIFIED` | Required |
| `Y_METRIC_POLARITY` | `NOT_SPECIFIED` | `NOT_SPECIFIED` | Optional |
| `CONTEXT` | `full_vector.step_0.symptom_1l` | Indirect input to Phase0 trace/canonicalization path via runtime `tc` | Optional |

## 4) What Phase0 reads (normative)
Phase0 canonicalization inputs in runtime path:
- `tc['pfl_X']` OR `tc['full_vector']['step_4']['improve_x']` OR `tc['full_vector']['step_4']['statement_1l']`
- `tc['pfl_Y']` OR `tc['full_vector']['step_4']['worsen_y']`
- `tc['full_vector']['step_1']['owner_scope']` OR `tc['full_vector']['step_2']['boundary_note_1l']`
- `tc['full_vector']['step_1']['constraints']`

Normative binding statement:
- When protocol keys are provided, Phase0 MUST consume canonicalization inputs derived from those protocol-bound keys.
- Phase0 MUST NOT rely on free-form raw outside protocol-bound keys in that case.

## 5) Valid-before-Phase0 criteria (normative)
`valid_live_input` requires presence of these protocol fields before Phase0 execution:
- `SCOPE`
- at least one `CONSTRAINT_*` entry
- `X_METRIC`
- `X_OBJECT`
- `Y_METRIC`
- `Y_OBJECT`

Failure class:
- `MISSING_REQUIRED_FIELD_BEFORE_PHASE0`

## 6) Implementation gaps (non-prescriptive)
- Direct runtime destination keys for `X_METRIC`, `X_OBJECT`, `X_METRIC_POLARITY`, `Y_METRIC`, `Y_OBJECT`, `Y_METRIC_POLARITY`, `TIMEFRAME_DEADLINE` are `NOT_SPECIFIED` in current binding path.
- Runtime path currently also uses `full_vector.step_4.statement_1l` and `full_vector.step_0.symptom_1l` as fallback sources in canonicalization/delta extraction path.
