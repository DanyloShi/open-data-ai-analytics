# CI/CD Lab Report

## Про що проєкт
- Дані: `data/raw/air_quality.csv` із порталу data.gov.ua (PM2.5 та AQI).
- Модулі: `src/data_load.py`, `src/data_quality_analysis.py`, `src/data_research.py`, `src/visualization.py`.
- Ціль лабораторної — зібрати CI/CD конвеєр для кожного модуля, публікувати результати та продемонструвати self-hosted runner.

## Частина A — CI на GitHub-hosted runners
- **Файл**: `.github/workflows/ci.yml`.
- **Тригери**: `push`/`pull_request` у `main` + ручний `workflow_dispatch` (можна обрати конкретний модуль).
- **Matrix**: модулі `[data_load, data_quality_analysis, data_research, visualization]` виконуються паралельно з `strategy.fail-fast=false`.
- **Path filter**: job `detect-changes` використовує `dorny/paths-filter@v3`, щоб запускати лише модулі, чиї файли/загальні залежності змінились (бонус-вимога «не запускати зайве»).
- **Залежності**: `actions/setup-python@v5` (Python 3.12) + кешування `pip` по `requirements.txt`.
- **Команди**: кожен модуль запускається як `python -m src.<module>`, логи пишуться в `artifacts/<module>/run.log`.

## Частина B — Публікація результатів (CD)
- **Артефакти**: `actions/upload-artifact@v4` завантажує `artifacts/<module>` із логами та додатковими файлами.
- **Візуалізації**: після `src.visualization` усі PNG із `reports/figures` копіюються в артефакт (`figures/*.png`), тож можна скачати графіки прямо з Actions.
- **Результат**: кожен запуск CI створює комплект логів/зображень, які замінюють публікацію на GitHub Pages (умовний CD-вихід).

## Частина C — Self-hosted runner
- **Файл**: `.github/workflows/ci-selfhosted.yml`.
- **Тригери**: лише ручний `workflow_dispatch` з вибором модуля (дефолт — `visualization`).
- **Runner**: `runs-on: [self-hosted, linux]` — необхідно зареєструвати агент (Labels → додайте `linux`/`local` під час `./config.sh`).
- **Кроки**:
  1. `actions/checkout@v4`.
  2. Перевірка локального Python (`python3 --version`).
  3. `python3 -m pip install -r requirements.txt` (можна замінити на локальний `venv`).
  4. Запуск обраного модуля + збір артефактів.
- **Порівняння GitHub vs self-hosted**

| Критерій | GitHub-hosted | Self-hosted |
| --- | --- | --- |
| Швидкість | ~2–3 хв через встановлення Python і залежностей без кешів; стабільний інтернет. | Може бути <1 хв, якщо у локальному `venv` вже є залежності; але залежить від ПК. |
| Доступ до ресурсів | Лише файли репозиторію, без локальних даних/GPU. | Повний доступ до локальних даних, GPU, приватних мереж. |
| Ризики | Нема потреби підтримувати runner, але неможливо використати приватні ресурси. | Runner потрібно тримати онлайн, конфіг безпеки критичний (секрети → локальна машина), можливі збої через власну інфраструктуру. |

## Як запускати конвеєри
1. **Автоматично**: кожен `push`/`pull_request` у `main` тригерить `.github/workflows/ci.yml`. Непотрібні модулі пропускаються автоматично за path filter.
2. **Ручний CI**: у вкладці Actions → “CI Modules” → Run workflow → виберіть модуль (`all` або конкретний).
3. **Self-hosted**: після додавання runner (Settings → Actions → Runners → New self-hosted runner) перейдіть до “CI Self-Hosted”, запустіть workflow та оберіть модуль.
4. **Завантаження звітів**: відкрийте виконання → вкладка “Artifacts” → скачайте потрібний модуль (логи, графіки).

## Замітки для супроводу
- У репозиторії є `venv/`; для локальної роботи активуйте його (`source venv/bin/activate`) і встановіть залежності (`pip install -r requirements.txt`).
- `MPLCONFIGDIR=.mplconfig` вже враховано у workflow і в `.gitignore`, щоб Matplotlib не вимагав GUI.
- `src/data_research.py` очищає дані (каст до `float`) перед тренуванням, тому CI не падає через рядки у `aqi/pm25`.
- Під час розширення CD (наприклад, GitHub Pages) можна використати ті самі артефакти/фігури як джерело.
