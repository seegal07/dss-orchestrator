# DSS_PRODUCT_INTENT_SOT_v0.1
Status: ACTIVE
Class: Governance SoT (intent compilation)
Scope: Product intent and canon alignment across active SoT

## 1) What DSS is / is not
- DSS is a structured contradiction-processing system with deterministic admission and operator-controlled downstream transformation.
  - Source: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/governance/PROBLEM_FRAMING_LAYER_SPEC_v0.2.md`
  - Source: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/governance/OPERATOR_CORE_SPEC_v1.1.md`
- DSS is not an idea generator or automatic mechanism proposer in admission/operator definitions.
  - Source: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/governance/PROBLEM_FRAMING_LAYER_SPEC_v0.2.md`
  - Source: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/governance/OPERATOR_CORE_SPEC_v1.1.md`

## 2) End-to-end pipeline and truth-source
- Pipeline map:
  - Phase0 -> Stage A (PFL / GatePFL) -> Stage B (GateCR + outcome classification).
  - Source: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/governance/PHASE0_CONFLICT_FORMALIZATION_SPEC_v0.3.md`
  - Source: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/governance/PROBLEM_FRAMING_LAYER_SPEC_v0.2.md`
  - Source: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/governance/STAGEB_OUTCOME_POLICY_v1.0.md`
- Stage A verdict/metrics truth-source:
  - GatePFL evidence from `gate_log.json` (primary) and `gate_summary.json` (secondary).
  - Snapshot artifacts are not verdict truth-source.
  - Source: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/governance/STAGEA_METRICS_SPEC_v0.1.1_v1.3.md`
  - Source: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/governance/PROBLEM_FRAMING_LAYER_SPEC_v0.2.md`

## 3) Canon summary
- Canonical truth for Stage A:
  - `canonical_slots_v0` is canonical truth.
  - `canonical_hash_v0 = hash(normalize(canonical_slots_v0))` is Step1 identity.
  - `canonical_X`/`canonical_Y` are display-only.
  - `canonical_hash_text` is legacy telemetry/replay only.
  - Source: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/governance/PHASE0_CONFLICT_FORMALIZATION_SPEC_v0.3.md`
  - Source: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/governance/STAGEA_METRICS_SPEC_v0.1.1_v1.3.md`

## 4) Outcome policy
- Stage B outcome domain is:
  - `JUMP`
  - `COMPROMISE`
  - `INCONCLUSIVE`
- One Stage B run must produce exactly one value from this domain.
- Source: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/governance/STAGEB_OUTCOME_POLICY_v1.0.md`

## 5) Version boundaries (v0.1 / v0.2)
- v0.1/v0.2 admission posture:
  - `NOT_PROVEN` default for strict mutual-degradation proof unless required proof signals are satisfied.
  - S2a is model-declared trade-off logic and does not assert causality proof.
  - Source: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/governance/PROBLEM_FRAMING_LAYER_SPEC_v0.2.md`
- Current pause/freeze status for S1/S2a identity alignment:
  - OWNER_DECISION pending on split-hash vs keep-all strategy.
  - Source: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/governance/PAUSE_RECORD_S2A_HASH_COLLISION_v0.2.md`

## ICP v0 (minimal)
- Who: SMB owner / CEO / C-level operator.
- Situation: decision deadlock where improving one metric/state predictably worsens another (trade-off), with competing proposals and no stable framing.
- Input expectation: metrics/states + scope/constraints; avoid action/solution framing.
- Output expectation: stabilized conflict object (`canonical_slots_v0`) + StageA status (`NOT_PROVEN` / `STRUCTURE_READY_FOR_PROOF` / `DECLARED_TRADEOFF` when applicable) and decision-ready next-step signal (`NOT SPECIFIED`).
- Non-goal: not an idea generator; does not guarantee “jump”; may return `COMPROMISE`/`INCONCLUSIVE`.

## 6) Out of scope
- No code-level scope expansion is defined by this intent compilation file.
- Product-facing UI scope in governance SoT: NOT SPECIFIED.
- LIVE_SET expansion policy in governance SoT: NOT SPECIFIED.
- This file introduces no new requirements; it compiles existing active SoT only.
