# DELTA_GATES_IMPACT

## Gate relationship map
- GateTRIZ: unchanged; remains validator of TRIZ core artifacts.
- GateCR: new pre-S09 gate; evaluates structural contradiction transformation quality.
- Gate9–Gate12: unchanged semantics.

## Reachability rule
- If GateCR = HARD_FAIL -> Gate9, Gate10, Gate11, Gate12 become NOT_RUN.
- If GateCR = SOFT_FAIL -> Gate9–Gate12 remain reachable with `COMPROMISE_MODE=TRUE`.
- If GateCR = PASS -> normal path to Gate9–Gate12.

## Explicit non-change clause
- Existing Gate9–Gate12 pass/fail criteria are not edited by this delta.
