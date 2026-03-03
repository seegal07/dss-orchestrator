# Dynamic Contextual Fallback Generator Spec v1.0

## Strict Rules
1. One structural shift per round.
2. Max 2 sentences.
3. No TRIZ terminology.
4. No ABC comparisons.
5. No visible divergence axes.
6. Must reuse `client_phrases[]`.
7. Output must be rephrased client language.

## Logic (pseudo)
```text
IF STAGNATION_FLAG = TRUE AND DCF_ROUND_COUNTER < 3:
    select internal divergence axis
    generate structural shift using client_phrases[]
    DCF_ROUND_COUNTER += 1
ELSE IF DCF_ROUND_COUNTER == 3:
    ASSISTED_MODE_ACK = TRUE
```

## Constraint
- DCF does NOT generate solutions.
- If new mechanism appears, it is considered client-generated.
