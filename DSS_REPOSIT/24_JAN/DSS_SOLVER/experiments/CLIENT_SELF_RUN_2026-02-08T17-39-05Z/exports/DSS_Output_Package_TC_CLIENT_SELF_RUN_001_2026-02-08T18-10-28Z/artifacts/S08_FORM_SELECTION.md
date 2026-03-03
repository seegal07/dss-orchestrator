# FORM_SELECTION

{
  "PRIMARY_FORM": "NONE",
  "BOUNDARY_CHECK": {
    "NEAREST_FORMS": [
      "NONE"
    ],
    "WHY_NOT_X": [
      "Распад группы"
    ],
    "WHY_NOT_Y": [
      "Невозможность онлайн участия"
    ]
  },
  "TRIZ_CORE": {
    "CONTRADICTION_1L": "Группа должна быть одновременно офлайн-ориентированной и допускать онлайн, иначе распадается.",
    "IKR_1L": "Группа сохраняется до конца курса без распада при гибридном формате.",
    "physical_contradiction": {
      "object": "сама группа",
      "parameter": "доля офлайн‑участия",
      "state_a": "высокая (почти все офлайн)",
      "state_not_a": "низкая (многие онлайн)"
    },
    "separation": {
      "separation_type": "condition",
      "what_changes": "онлайн допускается как исключение по заявлению студента, офлайн — базовый режим",
      "expected_resolution": "офлайн остаётся основным режимом, онлайн — исключение без распада группы"
    },
    "system_operator": {
      "system_present": "группа Python (15 студентов) в гибридном формате с преподавателем",
      "subsystem_present": "подгруппа офлайн в аудитории + подгруппа онлайн",
      "system_future": "если офлайн удержан, через 3 месяца остаётся ≥10 студентов"
    },
    "transformation_model": {
      "changed_object": "правила допуска к онлайн-участию",
      "new_state": "онлайн как исключение по заявлению, офлайн — базовый режим",
      "resolution_link": "офлайн-ядро сохраняется, гибкость остаётся"
    },
    "non_obviousness_check": {
      "assumption_broken": "кажется, что если разрешить онлайн всем, офлайн не пострадает — но это ломает группу",
      "why_not_obvious": "всем онлайн кажется удобным, но в итоге падает вовлечённость и группа распадается"
    }
  },
  "PRINCIPLES_TO_ACTION": {
    "PRINCIPLES": [
      "MISSING"
    ],
    "ACTIONS": [
      "MISSING"
    ]
  },
  "IKR_TEST": {
    "Q1": "MISSING",
    "Q2": "MISSING"
  },
  "CONFIDENCE": {
    "score": "MISSING",
    "justification": "MISSING"
  }
}