# DECISION_LAYER_DEPENDENCY_GRAPH

## S09 artifact origin
- Source field: `full_vector.step_9.concepts` (test case / intake-derived data).
- Runtime does not generate concepts in harness; it validates and exports them.
- Sources:
  - `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/harness/gates_structural.py` (`gate9_solution_set`)
  - `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/harness/harness.py` (`run_tc`, `_export_package`)

## Downstream dependencies on S09 outputs
- S10 depends on concept set indices/content (mechanism specs expected per concept by canon; runtime checks presence).
- S11 selection context references prior solution space.
- S12 requires `chosen_concept_index` and `chosen_concept_name` aligned to solution set intent.
- Export package always includes `artifacts/S09_SOLUTION_SET.md` and downstream artifacts.

## Gate dependencies requiring S09 artifacts
- **Gate9**: direct requirement (`concepts` exists, list, count >= 3).
- **Gate10**: indirect dependency (mechanism specs are for concepts from S09).
- **Gate12**: structural decision fields required; runtime additionally enforces unreachable state if Gate9 or Gate11 FAIL.
- Blocking rule:
  - `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/harness/gates_structural.py`: Gate12 set to `NOT_RUN` when Gate9 or Gate11 fail.

## Dependency chain (text graph)
`S09 (concepts)` -> `S10 (concept_specs)` -> `S11 (criteria refs / secondary check)` -> `S12 (decision commit)`

`Gate9 FAIL` or `Gate11 FAIL` -> `Gate12 NOT_RUN`
