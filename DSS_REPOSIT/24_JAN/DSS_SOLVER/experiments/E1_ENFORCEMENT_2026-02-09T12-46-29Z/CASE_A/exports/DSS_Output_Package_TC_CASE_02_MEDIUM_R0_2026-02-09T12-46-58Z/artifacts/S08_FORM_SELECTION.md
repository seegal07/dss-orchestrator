# FORM_SELECTION

{
  "PRIMARY_FORM": "NONE",
  "BOUNDARY_CHECK": {
    "NEAREST_FORMS": [
      "NONE"
    ],
    "WHY_NOT_X": [
      "Ограничение инцидентов"
    ],
    "WHY_NOT_Y": [
      "Ограничение скорости решений"
    ]
  },
  "TRIZ_CORE": {
    "CONTRADICTION_1L": "Автономия решений филиала должна быть высокой и низкой одновременно.",
    "IKR_1L": "Рост +30% без превышения инцидентов и без роста загрузки CEO.",
    "physical_contradiction": {
      "object": "Полномочия филиала",
      "parameter": "уровень автономии",
      "state_a": "высокая автономия для скорости",
      "state_not_a": "низкая автономия для контроля риска"
    },
    "separation": {
      "separation_type": "condition",
      "what_changes": "уровень автономии зависит от порога риска/суммы",
      "expected_resolution": "высокая автономия для низкого риска и обязательный контроль для высокого риска"
    },
    "system_operator": {
      "system_present": "Филиал принимает решения по продажам",
      "subsystem_present": "Менеджер филиала",
      "supersystem_present": "CEO и сеть филиалов"
    },
    "transformation_model": {
      "changed_object": "правила принятия решений в филиале",
      "new_state": "двухконтурная автономия по условию риска",
      "resolution_link": "разделение по условию снижает риск без снижения скорости"
    },
    "non_obviousness_check": {
      "assumption_broken": "Без condition-разделения по порогу риска автономия не может оставаться высокой и контролируемой одновременно.",
      "why_not_obvious": "Порог риска связывает скорость и контроль без роста участия CEO."
    }
  },
  "PRINCIPLES_TO_ACTION": {
    "PRINCIPLES": [
      "CORE_OPERATOR: separation_condition",
      "CORE_OPERATOR: segmentation"
    ],
    "ACTIONS": [
      {
        "\"Ввести два уровня автономии": "низкий риск — решение на месте, высокий риск — обязательная эскалация\""
      },
      "Разделить сделки на классы по сумме/риску и применять разные правила"
    ]
  },
  "IKR_TEST": {
    "Q1": "Рост +30% достигнут",
    "Q2": "Инциденты ≤ 8/мес и CEO ≤ 25 ч/нед"
  },
  "CONFIDENCE": {
    "score": "0.55",
    "justification": "Пороговый режим снижает риск при сохранении скорости"
  }
}