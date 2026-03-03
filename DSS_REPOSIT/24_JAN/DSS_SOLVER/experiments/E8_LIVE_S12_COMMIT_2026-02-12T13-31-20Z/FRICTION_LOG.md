- step: S12 (A: Primary ход)
  what_broke: неясно требование на текущем шаге.
  why: format unclear
  resolution: запросить только номер одного хода в одной строке.

- step: S12 (C: Rationale)
  what_broke: непонимание требуемой структуры rationale.
  why: format unclear
  resolution: запросить одну строку 'почему Ход 1' с упоминанием критериев 1/2/3.

- step: S12 (D: Commit step)
  what_broke: неясно, что считать 'первым необратимым шагом'.
  why: terminology
  resolution: запросить первый конкретный шаг исполнения, который делается сразу после решения.

- step: S12 (E: Revisit if)
  what_broke: непонимание смысла 'условия пересмотра'.
  why: terminology
  resolution: запросить один триггер, при котором решение пересматривается.

- step: S12 (E: Revisit if)
  what_broke: повторное непонимание необходимости условия пересмотра.
  why: terminology / intent unclear
  resolution: объяснить как 'аварийный триггер отката' и снова запросить 1 строку.

