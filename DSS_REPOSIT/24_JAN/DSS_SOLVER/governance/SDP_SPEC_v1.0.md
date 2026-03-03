# Stagnation Detection Protocol (SDP) v1.0

## 1. Purpose
- Detect formal stagnation before FAIL.
- Authorize up to 1 DCF round per trigger.

## 2. Formal Triggers (T1–T5)
- T1: `<3` distinguishable concepts after S09.
- T2: repeated concept rephrasing.
- T3: identical mechanism structures.
- T4: client explicitly states `"I don't see alternatives"`.
- T5: clarification loop exhausted without divergence.

## 3. Data Structure
- `STAGNATION_FLAG`: boolean
- `STAGNATION_REASON`: enum[T1..T5]
- `STAGNATION_STEP`: enum[S09|S10]

## 4. Explicit Rule
- `SDP != FAIL`
- `SDP = permission to activate ONE DCF round`

## 5. Hard Rule
- If DCF exhausted and criteria unmet, FAIL is applied by normal Gate logic.
