# GATECR_PASS_INTEGRITY_POLICY_v0.1
Status: ACTIVE
Owner: Alex
Class: PASS Criteria Hardening

------------------------------------------------------------
1. Definition: False-Positive PASS

False-positive PASS occurs when GateCR returns PASS
while structural risk has been shifted rather than eliminated.

Example class:
- mechanism includes stop / restart / repeated search loop
- unresolved downtime transferred into time dimension
- structural dependency remains but is masked procedurally

------------------------------------------------------------
2. Rule: PASS Forbidden Under Risk Shift

If risk_shift_detected == TRUE
→ PASS is prohibited.

Verdict must be:
- SOFT_FAIL (default)
- or HARD_FAIL (if additional structural defects present)

------------------------------------------------------------
3. Deterministic Enforcement

For schema_version >= 0.4:

If step_8_5.search_loop == TRUE
→ risk_shift_detected = TRUE
→ PASS not allowed

GateCR must rely on explicit vector field,
not NLP interpretation of mechanism text.

------------------------------------------------------------
4. Principle

"No illusion validation."

Structural resolution must remove dependency,
not postpone or proceduralize it.

END OF POLICY
