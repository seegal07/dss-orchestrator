# RUN_TIMELINE_AND_ARTIFACT_INDEX

## Timeline (ordered)

### 0) Frozen anchor
- Workspace: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/DRYRUN_CLIENT_INTERACTION_2026-02-10T20-05-42Z`
- Key artifact: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/DRYRUN_CLIENT_INTERACTION_2026-02-10T20-05-42Z/CASE_FREEZE.md`
- Role: immutable source facts.

### 1) E5.1 (S09 rerun)
- Workspace: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/E5_1_LIVE_S09_RERUN_2026-02-11T19-09-58Z`
- Key artifacts:
  - `EXECUTION_HEADER.md`
  - `DIALOGUE_LOG.md`
  - `S09_CONCEPT_SET_LIVE.md`
  - `SDP_EVENT_LOG.md`
  - `E5_1_REPORT_v0.1.md`
- Result summary:
  - `M1_concepts_count: 3`
  - `SDP_triggered: NO`
  - `DCF_rounds_used: 0`

### 2) E6 (S10 mechanism specs)
- Workspace: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/E6_LIVE_S10_UX_RETRY_V1_1_2026-02-12T08-59-13Z`
- Key artifacts:
  - `EXECUTION_HEADER.md`
  - `DIALOGUE_LOG.md`
  - `S10_MECHANISM_SPECS.md`
  - `SDP_EVENT_LOG.md`
  - `E6_REPORT_v0.1.md`
- Result summary:
  - `specs_collected: 3/3`
  - `SDP_triggers: 0`
  - `DCF_rounds: 0`

### 3) E7 (S11 criteria)
- Workspace: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/E7_LIVE_S11_UX_2026-02-12T11-48-47Z`
- Key artifacts:
  - `EXECUTION_HEADER.md`
  - `DIALOGUE_LOG.md`
  - `S11_SELECTION_CRITERIA.md`
  - `SDP_EVENT_LOG.md`
  - `E7_REPORT_v0.1.md`
- Result summary:
  - `criteria: 3`
  - `criteria_confirmation: YES`
  - `SDP_triggers: 0`
  - `DCF_rounds: 0`

### 4) E8 (S12 commit)
- Workspace: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/E8_LIVE_S12_COMMIT_2026-02-12T13-31-20Z`
- Key artifacts:
  - `EXECUTION_HEADER.md`
  - `DIALOGUE_LOG.md`
  - `S12_DECISION_RECORD.md`
  - `SDP_EVENT_LOG.md`
  - `E8_REPORT_v0.1.md`
- Result summary:
  - `commit: YES`
  - `SDP_triggers: 0`
  - `DCF_rounds: 0`

### 5) E9 (postrun UX fixation)
- Workspace: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/E9_POSTRUN_UX_FIXATION_2026-02-12T13-56-38Z`
- Key artifact:
  - `UX_BREAKS_E6_E8_v0.1.md`
- Result summary:
  - Friction severity count: `HIGH=2, MED=6, LOW=16`.

## DCF/SDP per step (from logs)
- E5.1/S09: SDP `NONE`; DCF rounds `0`.
- E6/S10: SDP `NONE`; DCF rounds `0`.
- E7/S11: SDP `NONE`; DCF rounds `0`.
- E8/S12: SDP `NONE`; DCF rounds `0`.
