# QUESTIONS_FOR_OWNER

1. Should runtime mode controls from `DSS_EXECUTION_MODE_SPEC_v1.1.md` become machine-enforced in harness, or stay governance-only?
2. For test authoring, should `TEST_VECTOR_SCHEMA_v0.2.md` be promoted as default for all new cases now?
3. Should `operator_core_enabled=true` fallback remain supported, or should schema flag be the only activation path?
4. Should GateCR `SOFT_FAIL` reasons be normalized into structured codes (currently plain text reasons)?
5. Do you want template files in `templates/operator_core/` to become executable render sources, or remain reference-only?
