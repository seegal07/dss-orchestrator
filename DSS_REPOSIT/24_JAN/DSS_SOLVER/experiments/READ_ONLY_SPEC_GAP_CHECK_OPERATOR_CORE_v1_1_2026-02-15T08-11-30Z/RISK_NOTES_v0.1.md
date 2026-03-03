# RISK_NOTES_v0.1

## R1 — Governance/runtime split
- Risk: stakeholders assume MODE governance is machine-enforced in harness.
- Impact: false confidence in protocol control.
- Current status: governance-defined, not parsed in `harness/*.py`.

## R2 — Input vs computed GateCR status ambiguity
- Risk: users may prefill `step_8_5.gatecr_status` and assume it drives routing.
- Impact: misunderstanding of authoritative source.
- Current status: harness computes GateCR from `step_8_5` evidence fields.

## R3 — Operator iteration expectation
- Risk: expectation of iteration counter/retry loop inside harness for S08.5/GateCR.
- Impact: process mismatch during live runs.
- Current status: no Operator Core iteration counter implemented in harness.

## R4 — Post-factum control quality
- Risk: solutions pass as SOFT_FAIL and continue downstream while control remains mostly retrospective.
- Impact: repeated PARTIAL outcomes and operational friction.
- Current status: by design allowed (SOFT_FAIL -> RUN + PARTIAL).
