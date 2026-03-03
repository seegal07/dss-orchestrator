# PHASE0_OUTPUT

{
  "phase0_enabled": true,
  "phase0_verdict": "PASS",
  "phase0_reason_code": "NONE",
  "canonical_hash": "587f37c0d32820a2549316af93440a452f68f34563bf0beeef03a83b67ca95af",
  "canonical_hash_v0": null,
  "canonical_hash_text": null,
  "canonical_slots_v0": null,
  "raw_hash": "cbbae6e80f35e1a7f02a411685d9236b3dd8e1547c26f8355be122a9a1bce70c",
  "trace_count": 4,
  "confidence_summary": "HIGH",
  "canonical_scope": "правило запуска новых филиалов в Европе",
  "canonical_X": "Ускорить запуск филиалов в Европе и повысить точность CAPEX/OPEX+PMF до запуска.",
  "canonical_Y": "Не увеличивать чрезмерно время и стоимость подготовки запуска.",
  "canonical_constraints": [
    "не раздувать исследовательский бюджет/срок"
  ],
  "phase0_trace": [
    {
      "raw_fragment": "Ускорить запуск филиалов в Европе и повысить точность CAPEX/OPEX+PMF до запуска.",
      "interpreted_parameter": "Ускорить запуск филиалов в Европе и повысить точность CAPEX/OPEX+PMF до запуска.",
      "reasoning_trace": "X:normalize_whitespace",
      "confidence_level": "HIGH"
    },
    {
      "raw_fragment": "Не увеличивать чрезмерно время и стоимость подготовки запуска.",
      "interpreted_parameter": "Не увеличивать чрезмерно время и стоимость подготовки запуска.",
      "reasoning_trace": "Y:normalize_whitespace",
      "confidence_level": "HIGH"
    },
    {
      "raw_fragment": "правило запуска новых филиалов в Европе",
      "interpreted_parameter": "правило запуска новых филиалов в Европе",
      "reasoning_trace": "scope:scope_projection",
      "confidence_level": "HIGH"
    },
    {
      "raw_fragment": "['не раздувать исследовательский бюджет/срок']",
      "interpreted_parameter": [
        "не раздувать исследовательский бюджет/срок"
      ],
      "reasoning_trace": "constraints:stable_list_sort",
      "confidence_level": "HIGH"
    }
  ]
}