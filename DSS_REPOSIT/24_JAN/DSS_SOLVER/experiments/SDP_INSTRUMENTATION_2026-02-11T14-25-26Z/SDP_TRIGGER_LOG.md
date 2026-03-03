# SDP Trigger Log

## Detection Parameters (instrumentation profile)
- `stagnation_counter` starts at `0`
- Repetition threshold: `>= 2` repeated reformulations
- Low-count condition: concepts `< 3`
- Divergence scale (synthetic): `0..1`
- Trigger condition (synthetic):
  - `T1` immediately if count `< 3`
  - `T2` if repetition threshold reached and divergence remains low

## CASE_A: NORMAL_PROGRESS
- Turn 1:
  - concepts_seen: 1
  - repetition_detected: no
  - divergence_score: 0.35
  - stagnation_counter: 0
- Turn 2:
  - concepts_seen: 2
  - repetition_detected: no
  - divergence_score: 0.58
  - stagnation_counter: 0
- Turn 3:
  - concepts_seen: 3
  - repetition_detected: no
  - divergence_score: 0.74
  - stagnation_counter: 0
- Trigger: none
- Result: `STAGNATION_FLAG = FALSE`

## CASE_B: REPHRASE_LOOP
- Turn 1:
  - concepts_seen: 1
  - repetition_detected: no
  - divergence_score: 0.22
  - stagnation_counter: 0
- Turn 2:
  - concepts_seen: 2 (same mechanism, rephrased)
  - repetition_detected: yes
  - divergence_score: 0.20
  - stagnation_counter: 1
- Turn 3:
  - concepts_seen: 3 (same mechanism, rephrased)
  - repetition_detected: yes
  - divergence_score: 0.19
  - stagnation_counter: 2
- Trigger: `T2` at turn 3
- Result: `STAGNATION_FLAG = TRUE`

## CASE_C: LOW_COUNT
- Turn 1:
  - concepts_seen: 1
  - repetition_detected: no
  - divergence_score: 0.30
  - stagnation_counter: 0
- Turn 2:
  - concepts_seen: 2
  - repetition_detected: minor
  - divergence_score: 0.27
  - stagnation_counter: 1
- End-of-S09 check:
  - concepts_seen_total: 2
  - low_count_condition: true (`< 3`)
- Trigger: `T1` at end of S09
- Result: `STAGNATION_FLAG = TRUE`
