# PHASE0_INSERTION_POINT_OPTIONS_v0.1

## Option A (primary): in harness before structural gates
- Hook point: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/harness/harness.py` in `run_tc()`
- Current flow reference: `run_tc()` -> `_build_step_map(tc)` -> `run_structural_gates(tc, step_map)`
- Phase0 insertion location: immediately after TC load + before `_build_step_map(tc)` / `run_structural_gates(...)`

Why this point:
- Single choke point for all run modes that use harness run path.
- Clean pre-PFL admission placement without touching GateCR/Operator logic.

## Option B (secondary): inside structural pipeline runner
- Hook point: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/harness/gates_structural.py` in `run_structural_gates()`
- Insertion location: before Gate1..Gate3 sequence (or right before current PFL check branch)

Risk vs Option A:
- Blends formalization and gate execution layers.
- Higher coupling to gate orchestration internals.

## How it gates PFL
- On `phase0_verdict=PASS`: pass canonical fields to current PFL input fields.
- On `phase0_verdict=FAIL`: stop before PFL and mark downstream as NOT_RUN by policy.

## What stops downstream on FAIL
- Expected propagation target (spec intent): stop before PFL; no S04+ execution.
- Existing stop propagation mechanics reference:
  - `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/harness/gates_structural.py` (`NOT_RUN` propagation patterns for Gate0/PFL/HARD_FAIL).
