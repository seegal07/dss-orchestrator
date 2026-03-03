# S03.5 PFL Prompt Template

Purpose:
- Validate structural admissibility before S04.

Required one-line fields:
- X: <requirement 1 in same system boundary>
- Y: <requirement 2 in same system boundary>
- conflict_type_candidate: causal|temporal|interaction|scale
- attempt_index: 1|2|3

Fixed clarification format (only for mutual degradation direction):
- Q1: Когда усиливаем X в рамках текущего scope — каким эффектом ухудшается Y? (1 строка)
- Q2: И наоборот: когда усиливаем Y — каким эффектом ухудшается X? (1 строка)

Do not output ideas/mechanisms/actions.
