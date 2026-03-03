# RULE_UPDATE

{
  "rule_id": "RULE_E3_SLA_001",
  "rule_statement_if_then": "Если SLA <95% через 3 месяца, то правила очередей пересматриваются",
  "criterion": "SLA‑отгрузка",
  "boundaries": "Текущий склад",
  "evidence_from_case": "Отчёты WMS",
  "test_case_action": "Изменение правил очередей",
  "version_note": "v1",
  "rationale_1l": "Сохраняем SLA без роста ошибок"
}