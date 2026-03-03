# SDP Instrumentation Report v0.1

## A) Trigger Accuracy Per Case
- CASE_A (NORMAL_PROGRESS): correct? **yes**
  - Expected: `FALSE`
  - Actual: `FALSE`
- CASE_B (REPHRASE_LOOP): correct? **yes**
  - Expected: `TRUE`
  - Actual: `TRUE` (`T2`)
- CASE_C (LOW_COUNT): correct? **yes**
  - Expected: `TRUE`
  - Actual: `TRUE` (`T1`)

## B) False Positive Risk Analysis
- Main risk zone: early turns with low concept count before S09 completion.
- Mitigation in this profile: `T1` is evaluated at end-of-S09, not mid-turn.
- Residual risk: semantically new concept paraphrased in short form may look repetitive.

## C) False Negative Risk Analysis
- Main risk zone: three superficially different concepts with same mechanism but weak repetition signal.
- If repetition detector is too strict on exact phrasing, `T2` may not fire.
- Residual risk: low divergence hidden by lexical variation.

## D) Threshold Sensitivity Observation
- Repetition threshold `>=2` in 3-turn window is sensitive enough for obvious loops.
- Lowering to `>=1` likely increases false positives.
- Raising to `>=3` risks missing short-loop stagnation in S09.

## E) Recommendation
- SDP ready for live pilot? **yes**
  - Reason: all three synthetic target behaviors matched expected trigger outcomes without DCF activation.
