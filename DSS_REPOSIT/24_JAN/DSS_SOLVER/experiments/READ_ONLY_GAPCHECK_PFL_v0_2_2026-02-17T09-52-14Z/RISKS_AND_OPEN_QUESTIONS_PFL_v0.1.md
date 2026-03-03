# RISKS_AND_OPEN_QUESTIONS_PFL_v0.1

## Top 5 risks
1. Boundary instability in live mode: S02/S03 prompts are operational (dialogue-driven), not centralized in template files; consistency depends on operator discipline.
2. SOLUTION_AS_XY gap: current Gate4 is structural-presence only and can accept mechanism-like X/Y.
3. Stop-propagation ambiguity: current control flow has no PFL branch; unclear whether to mark `Gate4..Gate14` or `S04+` artifact-level only as NOT_RUN.
4. Schema compatibility risk: making `pfl_*` mandatory without version gate will break historical test vectors.
5. Canonical reason mismatch risk: PFL spec uses new canonical stop literal not present in current harness constants.

## Top 5 owner questions (blocking only)
1. On PFL terminal FAIL, should NOT_RUN propagation be implemented as `Gate4..Gate14` exactly, or only `S04+` artifact-level with partial gate execution?
2. Should PFL data live as top-level `pfl_*` fields or inside a dedicated `step_3_5` object for step-map compatibility?
3. Should PFL be enabled only under a new schema/version flag (historical exemption like GateCR), or globally for all runs?
4. Which canonical fail reason should be machine-enforced in logs and gate reasons: exact PFL literal only, or both PFL + existing harness literals?
5. Should PFL be purely structural in harness, or require assisted confirmation for mutual degradation direction before PASS?
