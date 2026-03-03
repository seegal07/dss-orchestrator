# TRIZ_CORE_ENGINE

Назначение: автономный валидатор TRIZ‑ядра для DSS_TRIZ. Обязателен для принятия решения.

## API contract
```
validate_triz_core(tc: dict, semantic: dict | None, gate_log: list | None) -> dict
```
Возвращает:
```
{
  "status": "VALID" | "INVALID",
  "fail_reasons": [ { "code": "...", "msg": "...", "path": "..." } ],
  "artifacts": {
     "physical_contradiction": {...} | None,
     "separation": {...} | None,
     "system_operator": {...} | None,
     "transformation_model": {...} | None,
     "non_obviousness_check": {...} | None
  }
}
```
