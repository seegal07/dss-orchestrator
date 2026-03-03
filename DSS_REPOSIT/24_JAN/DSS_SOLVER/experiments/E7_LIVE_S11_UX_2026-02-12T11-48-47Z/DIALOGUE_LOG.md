Q1 | STEP=S11 | clarification_required=yes | info_gain=yes
Recap: Ход 1 = право выхода после года при уведомлении 6 месяцев; collecting: Criterion statement.
WHY: фиксируем первый проверяемый критерий выбора.
FORMAT: Критерий 1: <одно проверяемое условие>
A1: В договоре должно быть явно зафиксировано право арендатора после 1 года уведомить за 6 месяцев о расторжении.

Q2 | STEP=S11 | clarification_required=no | info_gain=yes
Recap: Ход 1 = право выхода после года при уведомлении 6 месяцев; collecting: Derived_from for Criterion 1.
WHY: связать критерий с источником для traceability.
FORMAT: Критерий 1 / Derived_from: IKR|CONSTRAINT|RISK
A2: RISK

Q3 | STEP=S11 | clarification_required=yes | info_gain=yes
Recap: Ход 1 = право выхода после года при уведомлении 6 месяцев; collecting: Check_method for Criterion 1.
WHY: зафиксировать измеримый способ проверки критерия.
FORMAT: Критерий 1 / Check_method: <как проверяем в 1 строке>
A3: проверка по зафиксированным пунктам договора (право выхода/сроки).

Q4 | STEP=S11 | clarification_required=no | info_gain=yes
Recap: Ход 2 = арендодатель ремонтирует, но ставка выше и выход позже; collecting: Criterion 2 statement.
WHY: зафиксировать второй проверяемый критерий выбора.
FORMAT: Критерий 2: <одно проверяемое условие>
A4: приемлемость по ставке (4.5-5k EUR при ремонте/условиях выхода) и неприемлемость потери 40-50 студентов при переезде.

Q5 | STEP=S11 | clarification_required=yes | info_gain=no
Recap: Ход 2 = арендодатель ремонтирует, но ставка выше и выход позже; collecting: Derived_from for Criterion 2.
WHY: связать критерий с одним источником traceability.
FORMAT: Критерий 2 / Derived_from: IKR|CONSTRAINT|RISK
A5: Икер Андриск

Q6 | STEP=S11 | clarification_required=no | info_gain=yes
Recap: Ход 2 = арендодатель ремонтирует, но ставка выше и выход позже; collecting: Derived_from for Criterion 2.
WHY: задать валидный источник traceability.
FORMAT: Критерий 2 / Derived_from: IKR|CONSTRAINT|RISK
A6: Derived_from: CONSTRAINT

Q7 | STEP=S11 | clarification_required=no | info_gain=yes
Recap: Ход 2 = арендодатель ремонтирует, но ставка выше и выход позже; collecting: Check_method for Criterion 2.
WHY: зафиксировать измеримый способ проверки критерия 2.
FORMAT: Критерий 2 / Check_method: <как проверяем в 1 строке>
A7: сравнение суммы аренды: ниже текущей в старом помещении, допускается выше идеального значения.

Q8 | STEP=S11 | clarification_required=no | info_gain=yes
Recap: Ход 3 = отказ от текущего объекта и поиск нового помещения; collecting: Criterion 3 statement.
WHY: зафиксировать третий проверяемый критерий выбора.
FORMAT: Критерий 3: <одно проверяемое условие>
A8: если арендодатель не принимает ни один из рабочих условий (выход/ставка/ремонт), сделка не подписывается.

Q9 | STEP=S11 | clarification_required=no | info_gain=yes
Recap: Ход 3 = отказ от текущего объекта и поиск нового помещения; collecting: Derived_from for Criterion 3.
WHY: задать источник traceability для критерия 3.
FORMAT: Критерий 3 / Derived_from: IKR|CONSTRAINT|RISK
A9: Derived_from: CONSTRAINT

Q10 | STEP=S11 | clarification_required=yes | info_gain=yes
Recap: Ход 3 = отказ от текущего объекта и поиск нового помещения; collecting: check_method for Criterion 3.
WHY: зафиксировать проверяемый метод для критерия отказа.
FORMAT: Критерий 3 / Check_method: <как проверяем в 1 строке>
A10: Если арендодатель не соглашается на условия выхода через один год с уведомлением за шесть месяцев ни при каких обстоятельствах...

Q11 | STEP=S11 | clarification_required=no | info_gain=yes
Recap: Ход 3 = отказ от текущего объекта и поиск нового помещения; collecting: check_method for Criterion 3.
WHY: завершить правило проверки критерия 3.
FORMAT: Критерий 3 / Check_method: если <условие> -> тогда <действие>
A11: если арендодатель не дает условия выхода через 1 год с уведомлением за 6 месяцев -> ищем другое помещение.

Q12 | STEP=S11 | clarification_required=no | info_gain=yes
Recap: Ход 1/2/3 и Критерии 1/2/3 собраны; collecting: Criteria confirmation.
WHY: получить явное подтверждение релевантности набора критериев от Decision Owner.
FORMAT: Criteria confirmation: YES|NO
A12: YES

Q13 | STEP=S11 | clarification_required=no | info_gain=yes
Recap: критерии подтверждены; collecting: reject reason for non-chosen Ход 2.
WHY: подготовить явную причину отклонения без ранжирования.
FORMAT: Reject reason / Ход 2: <почему отклоняем, 8–20 слов>
A13: высокая неопределенность: затраты на ремонт до 20k EUR при риске недобора и убыточности филиала.

Q14 | STEP=S11 | clarification_required=no | info_gain=yes
Recap: reject reason for Ход 2 already logged; collecting: reject reason for Ход 3.
WHY: получить второй явный мотив отклонения для S11 прозрачности.
FORMAT: Reject reason / Ход 3: <почему отклоняем, 8–20 слов>
A14: Ход 3 не отклоняется, но есть ограничение выполнимости по наличию подходящих помещений в Братиславе.

Q15 | STEP=S11 | clarification_required=no | info_gain=yes
Recap: reject reason for Ход 2 logged, Ход 3 condition noted; collecting: reject reason for Ход 1.
WHY: закрыть S11-prep полным набором причин для невыбранных ходов.
FORMAT: Reject reason / Ход 1: <почему отклоняем, 8–20 слов>
A15: Ход 1 допустим, но не желателен: готовы тратить не более 6000 EUR из ~12000 EUR экономии.

