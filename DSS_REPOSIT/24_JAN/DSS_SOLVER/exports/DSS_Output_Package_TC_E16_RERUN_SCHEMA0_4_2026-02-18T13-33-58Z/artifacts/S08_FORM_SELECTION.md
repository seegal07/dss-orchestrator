# FORM_SELECTION

{
  "PRIMARY_FORM": "Form 5",
  "BOUNDARY_CHECK": {
    "note": "ok"
  },
  "TRIZ_CORE": {
    "physical_contradiction": {
      "object": "найм директора",
      "parameter": "строгость требований",
      "state_a": "максимальная строгость",
      "state_not_a": "минимальная строгость"
    },
    "separation": {
      "separation_type": "condition",
      "what_changes": "оффер только после проверки пригодности",
      "expected_resolution": "снижение риска ошибочного найма"
    },
    "system_operator": {
      "subsystem_present": "интервью",
      "system_present": "процесс найма",
      "supersystem_present": "региональное управление"
    },
    "transformation_model": {
      "changed_object": "правило финального оффера",
      "new_state": "оффер зависит от верифицированной пригодности",
      "resolution_link": "снижает риск ложноположительного найма"
    },
    "non_obviousness_check": {
      "assumption_broken": "быстрое закрытие без проверки пригодности неустойчиво",
      "why_not_obvious": "без условного разделения проверки и оффера риск не снимается"
    }
  },
  "PRINCIPLES_TO_ACTION": {
    "PRINCIPLES": [
      1
    ],
    "ACTIONS": [
      "\"сначала верификация пригодности",
      "затем оффер\""
    ]
  },
  "IKR_TEST": {
    "Q1": "YES"
  },
  "CONFIDENCE": {
    "score": 1
  }
}