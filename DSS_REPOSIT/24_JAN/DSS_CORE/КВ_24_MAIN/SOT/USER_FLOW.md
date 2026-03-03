# User Flow (CORE → CLIENT)

## Purpose
Turn a user’s messy business problem into a validated DSS case with decisions and execution artifacts.

## Roles
- User (client/operator)
- DSS Operator (internal or automated)
- Harness (validation)

## Flow
1. Intake
- User submits problem statement and context.
- Output: draft Step0–Step1 data (symptom + owner constraints).

2. Structuring
- Operator completes Steps 2–7 (boundary, interactions, contradiction, IKR, barrier, resources).
- Output: structured problem model.

3. Synthesis
- Operator completes Steps 8–10 (form selection, solutions, mechanisms).
- Output: solution set + mechanism specs.

4. Decision & Execution
- Operator completes Steps 11–14 (secondary check, decision record, implementation map, rule update).
- Output: decision package + execution plan.

5. Validation
- Harness runs Gate0–Gate14 on the case.
- Output: PASS/FAIL with evidence.

6. Delivery
- User receives final package:
  - Problem model
  - Decision record
  - Implementation map
  - Rule update
  - Evidence summary

## Inputs and Outputs (per case)
Input:
- User context + constraints
- Any existing artifacts

Output:
- Case package (Steps 0–14)
- Evidence (RUN + BUGLIST)

## Productization Path
- Phase 1: Manual operator + Harness (current)
- Phase 2: Form-based intake + auto-structuring + Harness
- Phase 3: Full product UI with guided steps + export
