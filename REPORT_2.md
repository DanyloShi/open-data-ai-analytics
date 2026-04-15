# REPORT 2 - CI/CD (GitHub Actions)

## Що зроблено

1. Налаштовано workflow [`ci.yml`](.github/workflows/ci.yml):
- тригери `push` у `main`, `pull_request` у `main`, `workflow_dispatch`.
- ручний вибір модуля (`all`, `data_load`, `data_quality_analysis`, `data_research`, `visualization`).
- паралельний запуск модулів через `matrix` + `fail-fast: false`.

2. Для кожного запуску:
- створюється окремий робочий каталог;
- виконується `data_load`, далі цільовий модуль;
- результати збираються як artifacts (логи + звіти + графіки).

3. Налаштовано self-hosted workflow [`ci-selfhosted.yml`](.github/workflows/ci-selfhosted.yml):
- ручний запуск;
- виконання вибраного модуля на локальному runner;
- завантаження artifacts.

## Як це працює

- CI runner бере `data/dataset.csv`.
- `data_load` формує SQLite БД.
- інші модулі працюють з цією БД і пишуть результати у `reports/` та `plots/` (в межах job).
- artifacts можна завантажити зі сторінки GitHub Actions run.

## Навіщо така схема

- стабільна для DevOps-демонстрації (без складних ML-залежностей);
- кожен модуль ізольований у своїй матричній задачі;
- легко порівнювати GitHub-hosted і self-hosted запуски.
