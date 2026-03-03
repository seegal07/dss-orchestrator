# TRIZ_CORE_INTEGRATION_CONTRACT_v0.1

## 1) PURPOSE
Зафиксировать интерфейсы и ответственность между TRIZ_CORE_ENGINE, TRIZ_GUIDED_ELICITATION и DSS_SOLVER/harness для обязательной TRIZ‑валидации.

## 2) COMPONENTS & RESPONSIBILITIES
- **TRIZ_CORE_ENGINE**: валидатор. Возвращает VALID/INVALID + fail_reasons + artifacts. Не изменяет tc.
- **TRIZ_GUIDED_ELICITATION**: сопоставляет fail_code → (1 вопрос + шаблоны + критерии приёма). Пользователь — автор TRIZ‑полей.
- **DSS_SOLVER/harness**: вызывает валидатор, логирует GateTRIZ, принудительно блокирует INVALID, экспортирует evidence.

## 3) DATA CONTRACTS (SCHEMAS)
### 3.1 TRIZ_CORE_ENGINE result schema
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

### 3.2 fail_reason schema
- `code` (string, stable)
- `msg` (1 строка, без советов)
- `path` (строка‑указатель на поля tc)

### 3.3 GateTRIZ logging schema inside harness
- GateTRIZ должен появляться в `gate_log.json` и `gate_summary.json`.
- `gate_id`: "GateTRIZ"
- `check_type`: "TRIZ"
- `criteria_scope`: "TRIZ_CORE_ENGINE"
- `reason`: список fail_reasons в текстовой форме

## 4) CONTROL FLOW (STATE MACHINE)
- **VALID** → продолжение обычного пайплайна.
- **INVALID** → фиксируется как FAIL/BLOCKED, экспорт продолжается с причинами, решение не считается валидным.

## 5) IMMUTABILITY RULES
- TRIZ_CORE_ENGINE не мутирует tc.
- TRIZ_GUIDED_ELICITATION не генерирует TRIZ‑контент, только вопросы и шаблоны.
- Пользователь — единственный автор TRIZ‑полей.

## 6) VERSIONING RULES
- При появлении новых fail_code обновляются валидатор и elicitation‑спека, затем повышается версия контракта.

## 7) ACCEPTANCE TEST (Definition of Done)
- GateTRIZ виден в gate_log/gate_summary.
- 4 синтетических TCs дают ожидаемые статусы.
- fail_reasons отслеживаемы по code.
