# Regression Policy v0.1
Status: ACTIVE
Class: Governance SoT Policy
Scope: Regression validation and override control

## 1) Rule
- Any change that can affect outputs (docs/spec excluded) MUST be validated on a defined regression pack before being accepted.
- Existing regression packs MUST PASS after the change.

## 2) If a regression fails
- The change is forbidden unless OWNER issues an explicit OVERRIDE with rationale.

## 3) Override protocol (minimal)
- Owner records:
  - date
  - what is overridden
  - which pack failed
  - why override is accepted
  - follow-up action
- Override record is appended to the override log section below.

## 4) Roles
- Codex executes runs and evidence packaging.
- CEO validates DoD and reports PASS/FAIL.
- Owner is the only role that can approve overrides.

## 5) Minimal regression set definition
- At least one StageA pack (`E22 Positive_A` invariance-only).
- At least one readiness pack (`POSITIVE_C`).
- Packs MUST be versioned by folder path.
- Truth-source for verdicts is GatePFL evidence (`gate_log.json` primary, `gate_summary.json` secondary).
- `s2a_hash` is observe-only in v0.2 and is not a standalone PASS/FAIL gate unless OWNER defines explicit drift norm.

## Override Log
- (empty)
