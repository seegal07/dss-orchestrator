# INTERACTION_MAP

{
  "elements": [
    "Счёт",
    "Срок",
    "Просрочка",
    "Оплата"
  ],
  "flows": [
    {
      "from": "Счёт",
      "to": "Срок",
      "type": "info",
      "note": "Назначение срока"
    },
    {
      "from": "Срок",
      "to": "Просрочка",
      "type": "other",
      "note": "Просрочка"
    }
  ],
  "symptom_location": "Просрочка >30 дней"
}