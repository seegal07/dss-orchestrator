# TRIZ_CORE_ADDON_SPEC_v0.1

Назначение: отдельный addon‑контур TRIZ‑ядра поверх DSS_SOLVER, без изменения S00–S14.

## Структура addon
1) **TRIZ_9_SCREENS**
- past_subsystem
- past_system
- past_supersystem
- present_subsystem
- present_system
- present_supersystem
- future_subsystem
- future_system
- future_supersystem

2) **TRIZ_CONTRADICTION_SHARPENING**
- initial_contradiction (из S04)
- sharpened_contradiction
- justification

3) **TRIZ_PHYSICAL_CONTRADICTION**
- parameter
- state_A
- state_B
- separation_principle (time/space/condition/system)

4) **TRIZ_SUFIELD_MODEL**
- S1 (объект/сторона 1 в бизнес‑терминах)
- S2 (объект/сторона 2 в бизнес‑терминах)
- Field (тип взаимодействия: информация/деньги/энергия/организация)
- problematic_link
- proposed_transformations (2–4 пункта)

## Соответствие pipeline
Addon использует ссылки на S04/S05/S07/S09/S10/S12 как контекст, но хранится отдельно.

## Формат хранения
- Отдельный addon‑файл (markdown) на кейс.
- Отдельный addon‑answers YAML для gate15–18.
