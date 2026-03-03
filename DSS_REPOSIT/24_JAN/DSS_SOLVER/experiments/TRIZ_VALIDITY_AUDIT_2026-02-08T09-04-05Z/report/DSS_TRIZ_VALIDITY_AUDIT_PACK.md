# DSS_TRIZ_VALIDITY_AUDIT_PACK

## Ключевые фактические находки (10–15)
- В схеме test vector есть TRIZ‑ядро уровня форм: `PRIMARY_FORM`, `BOUNDARY_CHECK`, `TRIZ_CORE`, `PRINCIPLES_TO_ACTION`, `IKR_TEST`. (см. `TEST_VECTOR_SCHEMA_v0.1.md.docx`)
- В каноне 9‑Forms указаны те же структурные секции для `TRIZ_CORE` и принципов. (см. `CANON_9FORMS_v1.1.docx`)
- В каноне pipeline есть правила прохождения Gate8 и связи с 9‑Forms/формами. (см. `CANON_PIPELINE_v1.2.docx`)
- В `ASSISTED_GATE_CRITERIA_v0.1.md` семантически проверяются Gate4/5/6/11/12 (противоречие/IKR/барьер/secondary contradiction/decision).
- В `gates_structural.py` Gate8 требует наличие `PRIMARY_FORM`, `BOUNDARY_CHECK`, `TRIZ_CORE`, `PRINCIPLES_TO_ACTION`, `IKR_TEST` (структурно).
- TRIZ‑элементы “9 экранов”, “физическое противоречие”, “обострение противоречия”, “Su‑Field/VEPOL” **в каноне/схеме отсутствуют** как обязательные поля.
- Эти элементы присутствуют **только в addon‑контуре** (`TRIZ_CORE_ADDON_SPEC_v0.1.md` и `TRIZ_CORE_ADDON_GATE_CRITERIA_v0.1.md`).
- Gate15–18 (addon) фиксируются в `harness.py` и попадают в `gate_log.json`, но **не являются decision‑critical по умолчанию**.
- Реальная валидация TRIZ‑ядра в DSS сейчас ограничена структурой (Gate8) и семантикой противоречия/IKR/барьера (Gate4–6).
- Кейсы E3 (VALID) и E4 (DATA_GAPS) показывают применение текущих gate‑критериев без TRIZ‑расширений.

## Семантическая инвентаризация (кластеры → доказательства)
### TRIZ_CORE / 9‑Forms (структура)
- `TEST_VECTOR_SCHEMA_v0.1.md.docx` → Step8 содержит `PRIMARY_FORM`, `BOUNDARY_CHECK`, `TRIZ_CORE`, `PRINCIPLES_TO_ACTION`, `IKR_TEST`.
  Выдержка:
  - “PRIMARY_FORM … BOUNDARY_CHECK … TRIZ_CORE … IKR_1L … PRINCIPLES_TO_ACTION … IKR_TEST …”
- `CANON_9FORMS_v1.1.docx` → описывает те же секции формы.

### Противоречие и IKR
- `ASSISTED_GATE_CRITERIA_v0.1.md` → Gate4 (противоречие), Gate5 (IKR).
  Выдержка:
  - “Gate5 — IKR_CARD … ikr_1l описывает конечный эффект…”

### Ресурсы
- `TEST_VECTOR_SCHEMA_v0.1.md.docx` → Step7 RESOURCE_MAP.

### TRIZ‑элементы расширения
- 9 экранов / физическое противоречие / обострение / Su‑Field присутствуют **только** в addon‑контуре:
  - `TRIZ_CORE_ADDON_SPEC_v0.1.md`
  - `TRIZ_CORE_ADDON_GATE_CRITERIA_v0.1.md`

## Enforced vs Decorative (факт)
- TRIZ_CORE (формы, принципы, IKR) → PRESENT+ENFORCED (структурно Gate8; семантика Gate4/5).
- Противоречие/IKR/барьер → PRESENT+ENFORCED (Gate4/5/6 assisted criteria).
- 9 экранов / физическое противоречие / обострение / Su‑Field → PRESENT+NOT_ENFORCED в основном контуре (есть только в addon, не критично по умолчанию).
- ARIZ/тренды эволюции → ABSENT.

## Coverage Matrix
| TRIZ элемент | Canon/Schema | Pipeline step | Enforced gate | Тип enforcement | Gap summary |
|---|---|---|---|---|---|
| 9 screens | Нет (в каноне) / Есть (addon) | Нет / addon | Gate15 (addon) | assisted_addon | Не в базовом DSS |
| Contradiction sharpening | Нет (в каноне) / Есть (addon) | Нет / addon | Gate17 (addon) | assisted_addon | Не в базовом DSS |
| Physical contradiction | Нет (в каноне) / Есть (addon) | Нет / addon | Gate16 (addon) | assisted_addon | Не в базовом DSS |
| Su‑Field/VEPOL | Нет (в каноне) / Есть (addon) | Нет / addon | Gate18 (addon) | assisted_addon | Не в базовом DSS |
| Resources | Да | S07 | Gate7 | structural | Есть |
| IKR | Да | S05 | Gate5 | assisted | Есть |
| Contradiction | Да | S04 | Gate4 | assisted | Есть |
| 9‑Forms (not 9 screens) | Да | S08 | Gate8 | structural | Есть |
| ARIZ | Нет | Нет | Нет | none | Отсутствует |
| Trends/Laws | Нет | Нет | Нет | none | Отсутствует |

## Gates/validators (что реально проверяется)
- `gates_structural.py`: Gate0–14 структурно.
- `ASSISTED_GATE_CRITERIA_v0.1.md`: Gate4/5/6/11/12 семантика.
- `harness.py`: запускает Gate0–14; добавляет Gate15–18 только при наличии addon‑answers.

## TOP‑10 файлов для загрузки в GPT (первый пакет)
1) /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/canon/TEST_VECTOR_SCHEMA_v0.1.md.docx — базовая схема S00–S14 и TRIZ_CORE поля.
2) /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/canon/CANON_9FORMS_v1.1.docx — нормативные формы и TRIZ_CORE секции.
3) /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/canon/CANON_PIPELINE_v1.2.docx — правила gate‑логики (структурные требования).
4) /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/governance/ASSISTED_GATE_CRITERIA_v0.1.md — семантические критерии Gate4/5/6/11/12.
5) /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/harness/gates_structural.py — фактическая структурная проверка.
6) /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/harness/harness.py — запуск и логирование gate‑результатов.
7) /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/E3_REAL_CASE_002_2026-02-07T13-18-18Z/intake/INTAKE_TRANSCRIPT_E3.md — VALID кейс (вход).
8) /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/E3_REAL_CASE_002_2026-02-07T13-18-18Z/exports/DSS_Decision_Record_E3_REAL_CASE_002.md — VALID решение.
9) /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/E3_REAL_CASE_002_2026-02-07T13-18-18Z/exports/DSS_Output_Package_TC_E3_REAL_CASE_002_2026-02-07T13-19-40Z/gate_log.json — VALID gate‑лог.
10) /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/E4_REAL_CASE_003_2026-02-07T13-18-18Z/exports/DSS_Decision_Record_E4_REAL_CASE_003.md — DATA_GAPS (blocked) кейс.

## Что загрузить в GPT первым пакетом (≤10)
Файлы 1–10 из списка TOP‑10 выше.
