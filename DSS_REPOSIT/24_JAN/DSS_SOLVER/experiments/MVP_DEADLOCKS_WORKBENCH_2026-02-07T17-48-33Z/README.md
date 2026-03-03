# MVP_DEADLOCKS_WORKBENCH

## Как запускать harness
Пример:
python3 /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/harness/harness.py run --tc-path <path-to-tc.yaml> --answers <path-to-semantic.yaml>

## Где появляются outputs
- По умолчанию: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/evidence и /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/exports
- Для воспроизводимости: копии всегда лежат в sample_runs/<deadlock>/evidence и sample_runs/<deadlock>/exports

## Как воспроизвести прогон
1) Взять TC_*.yaml и semantic_answers.yaml из sample_runs/<deadlock>/tests
2) Запустить harness с --tc-path
3) Скопировать RUN/BUGLIST и DSS_Output_Package в sample_runs/<deadlock>/

## Как работает DATA_GAPS
Если после 3 циклов коррекции decision‑critical поля остаются MISSING,
формируется DATA_GAPS в USER_VIEW walkthrough и решение блокируется.
