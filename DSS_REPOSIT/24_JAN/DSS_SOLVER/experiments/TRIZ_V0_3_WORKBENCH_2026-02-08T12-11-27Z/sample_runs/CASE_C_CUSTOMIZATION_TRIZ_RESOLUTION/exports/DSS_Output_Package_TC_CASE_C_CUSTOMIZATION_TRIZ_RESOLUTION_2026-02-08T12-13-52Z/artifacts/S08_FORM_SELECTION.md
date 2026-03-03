# FORM_SELECTION

{
  "PRIMARY_FORM": "Форма противоречия",
  "BOUNDARY_CHECK": {
    "NEAREST_FORMS": [
      "Форма политики",
      "Форма контракта"
    ],
    "WHY_NOT_X": [
      "Нельзя расширять команду"
    ],
    "WHY_NOT_Y": [
      "Нельзя портить сервис действующим клиентам"
    ]
  },
  "TRIZ_CORE": {
    "CONTRADICTION_1L": "Нужно принять кастомизацию ради сделки, но нельзя разрушать роадмап и поддержку",
    "IKR_1L": "Сделка закрыта без перегрузки поддержки и без срыва роадмапа",
    "separation_strategy": [
      {
        "type": "condition",
        "description": "Разделить по условиям: кастомизация только для ограниченного сегмента"
      },
      {
        "type": "part-whole",
        "description": "Разделить по частям: вынести кастомизацию в отдельный слой"
      }
    ]
  },
  "PRINCIPLES_TO_ACTION": {
    "PRINCIPLES": [
      "Разделение по условиям",
      "Дробление"
    ],
    "ACTIONS": [
      "Контур кастомизации с SLA",
      "Модульный слой расширений вне ядра"
    ]
  },
  "IKR_TEST": {
    "Q1": "YES",
    "Q2": "YES"
  },
  "CONFIDENCE": {
    "score": 2,
    "justification": "Separation + principles заданы"
  }
}