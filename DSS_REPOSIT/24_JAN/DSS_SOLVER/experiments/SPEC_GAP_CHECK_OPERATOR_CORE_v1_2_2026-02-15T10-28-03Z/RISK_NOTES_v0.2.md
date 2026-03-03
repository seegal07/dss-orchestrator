# RISK_NOTES_v0.2

1. Control-flow complexity risk
- Adding retry introduces multi-pass behavior into currently single-pass gates.
- Risk: accidental infinite/ambiguous loops without strict `retry_consumed` guard.

2. Semantics drift risk
- If retry is added without explicit policy mapping for second `SOFT_FAIL`, runtime behavior can diverge from governance intent.

3. Evidence consistency risk
- Without a dedicated iteration log artifact, audits cannot distinguish first vs subsequent GateCR outcomes.

4. Schema fragmentation risk
- Reusing v0.2 for retry fields may blur historical meaning; version bump is safer.

5. Backward compatibility risk
- Low if schema-gated correctly; medium if retry logic is enabled globally.
