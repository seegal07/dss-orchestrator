# FORM_SELECTION

{
  "PRIMARY_FORM": "Форма потоков",
  "BOUNDARY_CHECK": {
    "NEAREST_FORMS": [
      "Форма регламента",
      "Форма контроля"
    ],
    "WHY_NOT_X": [
      "Нельзя убрать контроль качества"
    ],
    "WHY_NOT_Y": [
      "Нельзя игнорировать SLA"
    ]
  },
  "TRIZ_CORE": {
    "CONTRADICTION_1L": "нужно ускорять сборку, но нельзя увеличивать ошибки",
    "IKR_1L": "SLA выполняется без роста ошибок"
  },
  "PRINCIPLES_TO_ACTION": {
    "PRINCIPLES": [
      13
    ],
    "ACTIONS": [
      "Разделить потоки заказов"
    ]
  },
  "IKR_TEST": {
    "Q1": "YES",
    "Q2": "YES"
  },
  "CONFIDENCE": {
    "score": 2,
    "justification": "Противоречие и IKR подтверждены метриками"
  }
}