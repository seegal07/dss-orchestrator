# SDP Test Matrix

## Scope
Synthetic S09 stagnation detection only. No DCF activation.

## Cases

### CASE_A: NORMAL_PROGRESS
- Concepts count: 3
- Distinguishability: high
- Repetition: none
- Divergence trend: increasing
- Expected result: `STAGNATION_FLAG = FALSE`

### CASE_B: REPHRASE_LOOP
- Concepts count: 3 (surface)
- Distinguishability: low (same mechanism reworded)
- Repetition: high (3 rephrases)
- Divergence trend: flat
- Expected result: `STAGNATION_FLAG = TRUE`
- Expected trigger: `T2` (repeated concept rephrasing)

### CASE_C: LOW_COUNT
- Concepts count: 2
- Distinguishability: low
- Repetition: medium
- Divergence trend: weak
- Expected result: `STAGNATION_FLAG = TRUE`
- Expected trigger: `T1` (`<3` concepts after S09)
