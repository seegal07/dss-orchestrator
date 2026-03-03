# DCF Data Model v1.0

## Source of Truth Fields
- `client_phrases[]`
- `contradiction_elements[]`
- `ikr_statement`
- `barrier_statement`
- `resources_list[]`
- `current_concepts[]`
- `failed_concepts[]`
- `stagnation_reason`
- `stagnation_step`
- `DCF_ROUND_COUNTER` (int, default `0`)
- `DCF_ACTIVE` (boolean)
- `ASSISTED_MODE_ACK` (boolean)

## Constraints
- `DCF_MAX_ROUNDS = 3` (hard stop)
- no recursive fallback
- no hidden rounds
- DCF cannot alter Core
