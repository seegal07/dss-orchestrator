# PHASE0_ENABLEMENT_RUNBOOK_v1.0
Status: ACTIVE
Type: Governance SoT Runbook

## Purpose
Define deterministic enablement rules for Phase0 execution and historical compatibility behavior.

## Enablement Rule
- Phase0 runs when `phase0_enabled = true`.
- Phase0 may also run when schema policy explicitly requires it.

## Historical Compatibility Rule
- Historical vectors remain valid under historical compatibility policy.
- Historical inputs must not be retroactively invalidated by Phase0 enablement.

## Evidence Expectations
Each run should provide traceable evidence for:
- whether Phase0 was enabled,
- how compatibility mode was applied,
- resulting admission verdict source.

## Non-goals
This runbook does not change engine, harness, PFL logic, or Phase0 logic.

DoD (enablement PASS):
  1) Gate evidence: in V1/V2/V3 gate_log no "Phase0 disabled (historical compatibility)"
  2) Phase0 evidence: phase0_enabled=true; canonical_X/Y/hash not null; trace_count>0
  3) Admission usage evidence: GatePFL uses canonical object (not fallback), evidenced by gate_log pointers or case.json instrumentation canonical_object not-null and referenced
