- step: S11 (Criterion 1)
  what_broke: смешение терминов и сомнение по 'risk'.
  why: terminology confusion
  resolution: check_method извлечен как договорная верификация по пунктам; продолжаем к следующему критерию.

- step: S11 (Criterion 2 / Derived_from)
  what_broke: недопустимый формат токена источника.
  why: format mismatch
  resolution: запросить один валидный токен из IKR|CONSTRAINT|RISK.

- step: S11 (Criterion 3 / Check_method)
  what_broke: ответ оборван, не завершен как проверяемое правило.
  why: format incomplete
  resolution: запросить завершенную 1-строчную проверку в формате if/then.

