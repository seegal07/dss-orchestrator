# FORM_SELECTION

{
  "PRIMARY_FORM": "Form 5",
  "BOUNDARY_CHECK": {
    "note": "ускорение без адаптации ломает экономику"
  },
  "TRIZ_CORE": {
    "physical_contradiction": {
      "object": "запуск филиала",
      "parameter": "скорость/точность",
      "state_a": "быстро",
      "state_not_a": "точно"
    },
    "separation": {
      "separation_type": "condition",
      "what_changes": "запуск только после порога готовности",
      "expected_resolution": "снижение неверных запусков"
    },
    "system_operator": {
      "subsystem_present": "локальная подготовка",
      "system_present": "pipeline запуска",
      "supersystem_present": "международная сеть"
    },
    "transformation_model": {
      "changed_object": "момент разрешения необратимых затрат",
      "new_state": "разрешение только после порога",
      "resolution_link": "контроль риска неверного запуска"
    },
    "non_obviousness_check": {
      "assumption_broken": "быстрый перенос шаблона всегда масштабируется",
      "why_not_obvious": "без порога готовности рост скорости повышает риск системного перерасхода"
    }
  },
  "PRINCIPLES_TO_ACTION": {
    "PRINCIPLES": [
      1
    ],
    "ACTIONS": [
      "gate запуска по порогу команды и спроса"
    ]
  },
  "IKR_TEST": {
    "Q1": "YES"
  },
  "CONFIDENCE": {
    "score": 1
  },
  "risk_1l": "Первично ломается команда: некомпетентность/несоответствие приводит к провалу спроса и перерасходу."
}