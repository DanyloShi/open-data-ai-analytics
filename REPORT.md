# REPORT

## **1. Створення репозиторію та структури**
Було створено репозиторій **open-data-ai-analytics** та базову структуру проєкту.  
Додано каталоги: `data/`, `notebooks/`, `src/`, `reports/figures/`, а також файли `README.md` і `.gitignore`.  
Така структура забезпечує розділення сирих даних, коду та результатів аналізу.

---

## **2. Налаштування .gitignore**
У файл `.gitignore` додано правила для виключення службових та великих файлів:
- `__pycache__/`, `.ipynb_checkpoints/`
- `.venv/`, `.env`
- `data/raw/`

Це дозволяє не зберігати у репозиторії тимчасові файли та сирі дані.

---

## **3. Заповнення README.md**
У `README.md` було описано:
- **мету проєкту** — аналіз якості повітря за показниками PM2.5 та AQI;
- **джерело даних** — портал відкритих даних data.gov.ua;
- **3 дослідницькі питання** для подальшого аналізу.

---

## **4. Реалізація завантаження даних**
У гілці **feature/data_load** створено модуль `src/data_load.py`, який зчитує дані з папки `data/raw/`.  
Перевірено роботу скрипта та виконано merge у `main` через Pull Request.

---

## **5. Перевірка якості даних**
У гілці **feature/data_quality_analysis** реалізовано модуль перевірки якості даних, який визначає:
- розмір датасету;
- кількість пропусків;
- кількість дублікатів;
- типи колонок.

Результати виводяться у вигляді текстового звіту.

---

## **6. Базовий аналіз та модель**
У гілці **feature/data_research** виконано:
- базову описову статистику для `aqi` та `pm25`;
- підготовку даних (видалення пропусків);
- побудову **baseline-моделі** (Linear Regression) для прогнозу AQI за PM2.5;
- оцінку якості моделі за метрикою **MAE**.

---

## **7. Візуалізація даних**
У гілці **feature/visualization** побудовано графіки:
- гістограму розподілу AQI;
- часовий ряд середнього PM2.5.

Графіки автоматично зберігаються у папку `reports/figures/`.

---

## **8. Робота з merge-конфліктом**
Було штучно створено конфлікт у файлі `README.md` між двома гілками.  
Конфлікт коректно розв’язано шляхом ручного об’єднання змін та видалення службових маркерів Git.

---

## **9. Версіонування**
Додано файл **CHANGELOG.md** та створено тег **v0.1.0**, що фіксує першу стабільну версію проєкту.

---

## **10. Історія Git**
Нижче наведено граф історії комітів:

* bf899f3 (HEAD -> main, tag: v0.1.0, origin/main, origin/HEAD) Доадно changelog v0.1.0
*   4250e5e Merge pull request #8 from DanyloShi/feature/visualization
|\  
| * 7a112b1 (origin/feature/visualization, feature/visualization) Додано візуалізацію
|/  
*   5c986f6 Merge pull request #7 from DanyloShi/feature/conflict-b
|\  
| *   ac9e82a Merge branch 'main' into feature/conflict-b
| |\  
| |/  
|/|   
:...skipping...
* bf899f3 (HEAD -> main, tag: v0.1.0, origin/main, origin/HEAD) Доадно changelog v0.1.0
*   4250e5e Merge pull request #8 from DanyloShi/feature/visualization
|\  
| * 7a112b1 (origin/feature/visualization, feature/visualization) Додано візуалізацію
|/  
*   5c986f6 Merge pull request #7 from DanyloShi/feature/conflict-b
|\  
| *   ac9e82a Merge branch 'main' into feature/conflict-b
| |\  
| |/  
|/|   
* |   6250646 Merge pull request #6 from DanyloShi/feature/conflict-a
:...skipping...
* bf899f3 (HEAD -> main, tag: v0.1.0, origin/main, origin/HEAD) Доадно changelog v0.1.0
*   4250e5e Merge pull request #8 from DanyloShi/feature/visualization
|\  
| * 7a112b1 (origin/feature/visualization, feature/visualization) Додано візуалізацію
|/  
*   5c986f6 Merge pull request #7 from DanyloShi/feature/conflict-b
|\  
| *   ac9e82a Merge branch 'main' into feature/conflict-b
| |\  
| |/  
|/|   
* |   6250646 Merge pull request #6 from DanyloShi/feature/conflict-a
|\ \  
:...skipping...
* bf899f3 (HEAD -> main, tag: v0.1.0, origin/main, origin/HEAD) Доадно changelog v0.1.0
*   4250e5e Merge pull request #8 from DanyloShi/feature/visualization
|\  
| * 7a112b1 (origin/feature/visualization, feature/visualization) Додано візуалізацію
|/  
*   5c986f6 Merge pull request #7 from DanyloShi/feature/conflict-b
|\  
| *   ac9e82a Merge branch 'main' into feature/conflict-b
| |\  
| |/  
|/|   
* |   6250646 Merge pull request #6 from DanyloShi/feature/conflict-a
|\ \  
| * | 9763d87 (origin/feature/conflict-a, feature/conflict-a) Оновлено .gitignore
:...skipping...
* bf899f3 (HEAD -> main, tag: v0.1.0, origin/main, origin/HEAD) Доадно changelog v0.1.0
*   4250e5e Merge pull request #8 from DanyloShi/feature/visualization
|\  
| * 7a112b1 (origin/feature/visualization, feature/visualization) Додано візуалізацію
|/  
*   5c986f6 Merge pull request #7 from DanyloShi/feature/conflict-b
|\  
| *   ac9e82a Merge branch 'main' into feature/conflict-b
| |\  
| |/  
|/|   
* |   6250646 Merge pull request #6 from DanyloShi/feature/conflict-a
|\ \  
| * | 9763d87 (origin/feature/conflict-a, feature/conflict-a) Оновлено .gitignore
* | | 377bb3d Merge pull request #5 from DanyloShi/feature/conflict-a
:...skipping...
* bf899f3 (HEAD -> main, tag: v0.1.0, origin/main, origin/HEAD) Доадно changelog v0.1.0
*   4250e5e Merge pull request #8 from DanyloShi/feature/visualization
|\  
| * 7a112b1 (origin/feature/visualization, feature/visualization) Додано візуалізацію
|/  
*   5c986f6 Merge pull request #7 from DanyloShi/feature/conflict-b
|\  
| *   ac9e82a Merge branch 'main' into feature/conflict-b
| |\  
| |/  
|/|   
* |   6250646 Merge pull request #6 from DanyloShi/feature/conflict-a
|\ \  
| * | 9763d87 (origin/feature/conflict-a, feature/conflict-a) Оновлено .gitignore
* | | 377bb3d Merge pull request #5 from DanyloShi/feature/conflict-a
|\| | 
:...skipping...
* bf899f3 (HEAD -> main, tag: v0.1.0, origin/main, origin/HEAD) Доадно changelog v0.1.0
*   4250e5e Merge pull request #8 from DanyloShi/feature/visualization
|\  
| * 7a112b1 (origin/feature/visualization, feature/visualization) Додано візуалізацію
|/  
*   5c986f6 Merge pull request #7 from DanyloShi/feature/conflict-b
|\  
| *   ac9e82a Merge branch 'main' into feature/conflict-b
| |\  
| |/  
|/|   
* |   6250646 Merge pull request #6 from DanyloShi/feature/conflict-a
|\ \  
| * | 9763d87 (origin/feature/conflict-a, feature/conflict-a) Оновлено .gitignore
* | | 377bb3d Merge pull request #5 from DanyloShi/feature/conflict-a
|\| | 
| * | 730f5f4 Оновлено README (3 питання)
:...skipping...
* bf899f3 (HEAD -> main, tag: v0.1.0, origin/main, origin/HEAD) Доадно changelog v0.1.0
*   4250e5e Merge pull request #8 from DanyloShi/feature/visualization
|\  
| * 7a112b1 (origin/feature/visualization, feature/visualization) Додано візуалізацію
|/  
*   5c986f6 Merge pull request #7 from DanyloShi/feature/conflict-b
|\  
| *   ac9e82a Merge branch 'main' into feature/conflict-b
| |\  
| |/  
|/|   
* |   6250646 Merge pull request #6 from DanyloShi/feature/conflict-a
|\ \  
| * | 9763d87 (origin/feature/conflict-a, feature/conflict-a) Оновлено .gitignore
* | | 377bb3d Merge pull request #5 from DanyloShi/feature/conflict-a
|\| | 
| * | 730f5f4 Оновлено README (3 питання)
|/ /  
:...skipping...
* bf899f3 (HEAD -> main, tag: v0.1.0, origin/main, origin/HEAD) Доадно changelog v0.1.0
*   4250e5e Merge pull request #8 from DanyloShi/feature/visualization
|\  
| * 7a112b1 (origin/feature/visualization, feature/visualization) Додано візуалізацію
|/  
*   5c986f6 Merge pull request #7 from DanyloShi/feature/conflict-b
|\  
| *   ac9e82a Merge branch 'main' into feature/conflict-b
| |\  
| |/  
|/|   
* |   6250646 Merge pull request #6 from DanyloShi/feature/conflict-a
|\ \  
| * | 9763d87 (origin/feature/conflict-a, feature/conflict-a) Оновлено .gitignore
* | | 377bb3d Merge pull request #5 from DanyloShi/feature/conflict-a
|\| | 
| * | 730f5f4 Оновлено README (3 питання)
|/ /  
* |   c160718 Merge pull request #4 from DanyloShi/feature/data_research
:...skipping...
* bf899f3 (HEAD -> main, tag: v0.1.0, origin/main, origin/HEAD) Доадно changelog v0.1.0
*   4250e5e Merge pull request #8 from DanyloShi/feature/visualization
|\  
| * 7a112b1 (origin/feature/visualization, feature/visualization) Додано візуалізацію
|/  
*   5c986f6 Merge pull request #7 from DanyloShi/feature/conflict-b
|\  
| *   ac9e82a Merge branch 'main' into feature/conflict-b
| |\  
| |/  
|/|   
* |   6250646 Merge pull request #6 from DanyloShi/feature/conflict-a
|\ \  
| * | 9763d87 (origin/feature/conflict-a, feature/conflict-a) Оновлено .gitignore
* | | 377bb3d Merge pull request #5 from DanyloShi/feature/conflict-a
|\| | 
| * | 730f5f4 Оновлено README (3 питання)
|/ /  
* |   c160718 Merge pull request #4 from DanyloShi/feature/data_research
|\ \  
:...skipping...
* bf899f3 (HEAD -> main, tag: v0.1.0, origin/main, origin/HEAD) Доадно changelog v0.1.0
*   4250e5e Merge pull request #8 from DanyloShi/feature/visualization
|\  
| * 7a112b1 (origin/feature/visualization, feature/visualization) Додано візуалізацію
|/  
*   5c986f6 Merge pull request #7 from DanyloShi/feature/conflict-b
|\  
| *   ac9e82a Merge branch 'main' into feature/conflict-b
| |\  
| |/  
|/|   
* |   6250646 Merge pull request #6 from DanyloShi/feature/conflict-a
|\ \  
| * | 9763d87 (origin/feature/conflict-a, feature/conflict-a) Оновлено .gitignore
* | | 377bb3d Merge pull request #5 from DanyloShi/feature/conflict-a
|\| | 
| * | 730f5f4 Оновлено README (3 питання)
|/ /  
* |   c160718 Merge pull request #4 from DanyloShi/feature/data_research
|\ \  
| * | 3030f9d (origin/feature/data_research, feature/data_research) Додано код для аналізу даних та побудови моделі
:...skipping...
* bf899f3 (HEAD -> main, tag: v0.1.0, origin/main, origin/HEAD) Доадно changelog v0.1.0
*   4250e5e Merge pull request #8 from DanyloShi/feature/visualization
|\  
| * 7a112b1 (origin/feature/visualization, feature/visualization) Додано візуалізацію
|/  
*   5c986f6 Merge pull request #7 from DanyloShi/feature/conflict-b
|\  
| *   ac9e82a Merge branch 'main' into feature/conflict-b
| |\  
| |/  
|/|   
* |   6250646 Merge pull request #6 from DanyloShi/feature/conflict-a
|\ \  
| * | 9763d87 (origin/feature/conflict-a, feature/conflict-a) Оновлено .gitignore
* | | 377bb3d Merge pull request #5 from DanyloShi/feature/conflict-a
|\| | 
| * | 730f5f4 Оновлено README (3 питання)
|/ /  
* |   c160718 Merge pull request #4 from DanyloShi/feature/data_research
|\ \  
| * | 3030f9d (origin/feature/data_research, feature/data_research) Додано код для аналізу даних та побудови моделі
* | |   91a9dc5 Merge pull request #3 from DanyloShi/feature/data_quality_analysis
:...skipping...
* bf899f3 (HEAD -> main, tag: v0.1.0, origin/main, origin/HEAD) Доадно changelog v0.1.0
*   4250e5e Merge pull request #8 from DanyloShi/feature/visualization
|\  
| * 7a112b1 (origin/feature/visualization, feature/visualization) Додано візуалізацію
|/  
*   5c986f6 Merge pull request #7 from DanyloShi/feature/conflict-b
|\  
| *   ac9e82a Merge branch 'main' into feature/conflict-b
| |\  
| |/  
|/|   
* |   6250646 Merge pull request #6 from DanyloShi/feature/conflict-a
|\ \  
| * | 9763d87 (origin/feature/conflict-a, feature/conflict-a) Оновлено .gitignore
* | | 377bb3d Merge pull request #5 from DanyloShi/feature/conflict-a
|\| | 
| * | 730f5f4 Оновлено README (3 питання)
|/ /  
* |   c160718 Merge pull request #4 from DanyloShi/feature/data_research
|\ \  
| * | 3030f9d (origin/feature/data_research, feature/data_research) Додано код для аналізу даних та побудови моделі
* | |   91a9dc5 Merge pull request #3 from DanyloShi/feature/data_quality_analysis
|\ \ \  
:...skipping...
* bf899f3 (HEAD -> main, tag: v0.1.0, origin/main, origin/HEAD) Доадно changelog v0.1.0
*   4250e5e Merge pull request #8 from DanyloShi/feature/visualization
|\  
| * 7a112b1 (origin/feature/visualization, feature/visualization) Додано візуалізацію
|/  
*   5c986f6 Merge pull request #7 from DanyloShi/feature/conflict-b
|\  
| *   ac9e82a Merge branch 'main' into feature/conflict-b
| |\  
| |/  
|/|   
* |   6250646 Merge pull request #6 from DanyloShi/feature/conflict-a
|\ \  
| * | 9763d87 (origin/feature/conflict-a, feature/conflict-a) Оновлено .gitignore
* | | 377bb3d Merge pull request #5 from DanyloShi/feature/conflict-a
|\| | 
| * | 730f5f4 Оновлено README (3 питання)
|/ /  
* |   c160718 Merge pull request #4 from DanyloShi/feature/data_research
|\ \  
| * | 3030f9d (origin/feature/data_research, feature/data_research) Додано код для аналізу даних та побудови моделі
* | |   91a9dc5 Merge pull request #3 from DanyloShi/feature/data_quality_analysis
|\ \ \  
| |/ /  
:...skipping...
* bf899f3 (HEAD -> main, tag: v0.1.0, origin/main, origin/HEAD) Доадно changelog v0.1.0
*   4250e5e Merge pull request #8 from DanyloShi/feature/visualization
|\  
| * 7a112b1 (origin/feature/visualization, feature/visualization) Додано візуалізацію
|/  
*   5c986f6 Merge pull request #7 from DanyloShi/feature/conflict-b
|\  
| *   ac9e82a Merge branch 'main' into feature/conflict-b
| |\  
| |/  
|/|   
* |   6250646 Merge pull request #6 from DanyloShi/feature/conflict-a
|\ \  
| * | 9763d87 (origin/feature/conflict-a, feature/conflict-a) Оновлено .gitignore
* | | 377bb3d Merge pull request #5 from DanyloShi/feature/conflict-a
|\| | 
| * | 730f5f4 Оновлено README (3 питання)
|/ /  
* |   c160718 Merge pull request #4 from DanyloShi/feature/data_research
|\ \  
| * | 3030f9d (origin/feature/data_research, feature/data_research) Додано код для аналізу даних та побудови моделі
* | |   91a9dc5 Merge pull request #3 from DanyloShi/feature/data_quality_analysis
|\ \ \  
| |/ /  
|/| |   
:...skipping...
* bf899f3 (HEAD -> main, tag: v0.1.0, origin/main, origin/HEAD) Доадно changelog v0.1.0
*   4250e5e Merge pull request #8 from DanyloShi/feature/visualization
|\  
| * 7a112b1 (origin/feature/visualization, feature/visualization) Додано візуалізацію
|/  
*   5c986f6 Merge pull request #7 from DanyloShi/feature/conflict-b
|\  
| *   ac9e82a Merge branch 'main' into feature/conflict-b
| |\  
| |/  
|/|   
* |   6250646 Merge pull request #6 from DanyloShi/feature/conflict-a
|\ \  
| * | 9763d87 (origin/feature/conflict-a, feature/conflict-a) Оновлено .gitignore
* | | 377bb3d Merge pull request #5 from DanyloShi/feature/conflict-a
|\| | 
| * | 730f5f4 Оновлено README (3 питання)
|/ /  
* |   c160718 Merge pull request #4 from DanyloShi/feature/data_research
|\ \  
| * | 3030f9d (origin/feature/data_research, feature/data_research) Додано код для аналізу даних та побудови моделі
* | |   91a9dc5 Merge pull request #3 from DanyloShi/feature/data_quality_analysis
|\ \ \  
| |/ /  
|/| |   
| * | 7c6c569 (origin/feature/data_quality_analysis, feature/data_quality_analysis) Додано аналіз якості даних
:...skipping...
* bf899f3 (HEAD -> main, tag: v0.1.0, origin/main, origin/HEAD) Доадно changelog v0.1.0
*   4250e5e Merge pull request #8 from DanyloShi/feature/visualization
|\  
| * 7a112b1 (origin/feature/visualization, feature/visualization) Додано візуалізацію
|/  
*   5c986f6 Merge pull request #7 from DanyloShi/feature/conflict-b
|\  
| *   ac9e82a Merge branch 'main' into feature/conflict-b
| |\  
| |/  
|/|   
* |   6250646 Merge pull request #6 from DanyloShi/feature/conflict-a
|\ \  
| * | 9763d87 (origin/feature/conflict-a, feature/conflict-a) Оновлено .gitignore
* | | 377bb3d Merge pull request #5 from DanyloShi/feature/conflict-a
|\| | 
| * | 730f5f4 Оновлено README (3 питання)
|/ /  
* |   c160718 Merge pull request #4 from DanyloShi/feature/data_research
|\ \  
| * | 3030f9d (origin/feature/data_research, feature/data_research) Додано код для аналізу даних та побудови моделі
* | |   91a9dc5 Merge pull request #3 from DanyloShi/feature/data_quality_analysis
|\ \ \  
| |/ /  
|/| |   
| * | 7c6c569 (origin/feature/data_quality_analysis, feature/data_quality_analysis) Додано аналіз якості даних
* | | 9ed2d5b Merge pull request #2 from DanyloShi/feature/data_load
:...skipping...
* bf899f3 (HEAD -> main, tag: v0.1.0, origin/main, origin/HEAD) Доадно changelog v0.1.0
*   4250e5e Merge pull request #8 from DanyloShi/feature/visualization
|\  
| * 7a112b1 (origin/feature/visualization, feature/visualization) Додано візуалізацію
|/  
*   5c986f6 Merge pull request #7 from DanyloShi/feature/conflict-b
|\  
| *   ac9e82a Merge branch 'main' into feature/conflict-b
| |\  
| |/  
|/|   
* |   6250646 Merge pull request #6 from DanyloShi/feature/conflict-a
|\ \  
| * | 9763d87 (origin/feature/conflict-a, feature/conflict-a) Оновлено .gitignore
* | | 377bb3d Merge pull request #5 from DanyloShi/feature/conflict-a
|\| | 
| * | 730f5f4 Оновлено README (3 питання)
|/ /  
* |   c160718 Merge pull request #4 from DanyloShi/feature/data_research
|\ \  
| * | 3030f9d (origin/feature/data_research, feature/data_research) Додано код для аналізу даних та побудови моделі
* | |   91a9dc5 Merge pull request #3 from DanyloShi/feature/data_quality_analysis
|\ \ \  
| |/ /  
|/| |   
| * | 7c6c569 (origin/feature/data_quality_analysis, feature/data_quality_analysis) Додано аналіз якості даних
* | | 9ed2d5b Merge pull request #2 from DanyloShi/feature/data_load
|\| | 
:...skipping...
* bf899f3 (HEAD -> main, tag: v0.1.0, origin/main, origin/HEAD) Доадно changelog v0.1.0
*   4250e5e Merge pull request #8 from DanyloShi/feature/visualization
|\  
| * 7a112b1 (origin/feature/visualization, feature/visualization) Додано візуалізацію
|/  
*   5c986f6 Merge pull request #7 from DanyloShi/feature/conflict-b
|\  
| *   ac9e82a Merge branch 'main' into feature/conflict-b
| |\  
| |/  
|/|   
* |   6250646 Merge pull request #6 from DanyloShi/feature/conflict-a
|\ \  
| * | 9763d87 (origin/feature/conflict-a, feature/conflict-a) Оновлено .gitignore
* | | 377bb3d Merge pull request #5 from DanyloShi/feature/conflict-a
|\| | 
| * | 730f5f4 Оновлено README (3 питання)
|/ /  
* |   c160718 Merge pull request #4 from DanyloShi/feature/data_research
|\ \  
| * | 3030f9d (origin/feature/data_research, feature/data_research) Додано код для аналізу даних та побудови моделі
* | |   91a9dc5 Merge pull request #3 from DanyloShi/feature/data_quality_analysis
|\ \ \  
| |/ /  
|/| |   
| * | 7c6c569 (origin/feature/data_quality_analysis, feature/data_quality_analysis) Додано аналіз якості даних
* | | 9ed2d5b Merge pull request #2 from DanyloShi/feature/data_load
|\| | 
| * | 387a439 (origin/feature/data_load, feature/data_load) Додано README.md в папку з даними
:...skipping...
* bf899f3 (HEAD -> main, tag: v0.1.0, origin/main, origin/HEAD) Доадно changelog v0.1.0
*   4250e5e Merge pull request #8 from DanyloShi/feature/visualization
|\  
| * 7a112b1 (origin/feature/visualization, feature/visualization) Додано візуалізацію
|/  
*   5c986f6 Merge pull request #7 from DanyloShi/feature/conflict-b
|\  
| *   ac9e82a Merge branch 'main' into feature/conflict-b
| |\  
| |/  
|/|   
* |   6250646 Merge pull request #6 from DanyloShi/feature/conflict-a
|\ \  
| * | 9763d87 (origin/feature/conflict-a, feature/conflict-a) Оновлено .gitignore
* | | 377bb3d Merge pull request #5 from DanyloShi/feature/conflict-a
|\| | 
| * | 730f5f4 Оновлено README (3 питання)
|/ /  
* |   c160718 Merge pull request #4 from DanyloShi/feature/data_research
|\ \  
| * | 3030f9d (origin/feature/data_research, feature/data_research) Додано код для аналізу даних та побудови моделі
* | |   91a9dc5 Merge pull request #3 from DanyloShi/feature/data_quality_analysis
|\ \ \  
| |/ /  
|/| |   
| * | 7c6c569 (oty_analysis, feature/data_quality_analysis) Додано аналіз якості даних
* | | 9ed2d5b Merge pull request #2 from DanyloShi/feature/data_load
|\| | 
| * | 387a439 (origin/feature/data_load, feature/data_load) Додано README.md в папку з даними
* | | d03b94c Merge pull request #1 from DanyloShi/feature/data_load
|\| | 
| * | 2db1979 Додано скрипт для завантаження даних
:...skipping...
* bf899f3 (HEAD -> main, tag: v0.1.0, origin/main, origin/HEAD) Доадно changelog v0.1.0
*   4250e5e Merge pull request #8 from DanyloShi/feature/visualization
|\  
| * 7a112b1 (origin/feature/visualization, feature/visualization) Додано візуалізацію
|/  
*   5c986f6 Merge pull request #7 from DanyloShi/feature/conflict-b
|\  
| *   ac9e82a Merge branch 'main' into feature/conflict-b
| |\  
| |/  
|/|   
* |   6250646 Merge pull request #6 from DanyloShi/feature/conflict-a
|\ \  
| * | 9763d87 (origin/feature/conflict-a, feature/conflict-a) Оновлено .gitignore
* | | 377bb3d Merge pull request #5 from DanyloShi/feature/conflict-a
|\| | 
| * | 730f5f4 Оновлено README (3 питання)
|/ /  
* |   c160718 Merge pull request #4 from DanyloShi/feature/data_research
|\ \  
| * | 3030f9d (origin/feature/data_research, feature/data_research) Додано код для аналізу даних та побудови моделі
* | |   91a9dc5 Merge pull request #3 from DanyloShi/feature/data_quality_analysis
|\ \ \  
| |/ /  
|/| |   
| * | 7c6c569 (origin/feature/data_quality_analysis, feature/data_quality_analysis) Додано аналіз якості даних
* | | 9ed2d5b Merge pull request #2 from DanyloShi/feature/data_load
|\| | 
| * | 387a439 (origin/feature/data_load, feature/data_load) Додано README.md в папку з даними
* | | d03b94c Merge pull request #1 from DanyloShi/feature/data_load
|\| | 
| * | 2db1979 Додано скрипт для завантаження даних
|/ /  
:...skipping...
* bf899f3 (HEAD -> main, tag: v0.1.0, origin/main, origin/HEAD) Доадно changelog v0.1.0
*   4250e5e Merge pull request #8 from DanyloShi/feature/visualization
|\  
| * 7a112b1 (origin/feature/visualization, feature/visualization) Додано візуалізацію
|/  
*   5c986f6 Merge pull request #7 from DanyloShi/feature/conflict-b
|\  
| *   ac9e82a Merge branch 'main' into feature/conflict-b
| |\  
| |/  
|/|   
* |   6250646 Merge pull request #6 from DanyloShi/feature/conflict-a
|\ \  
| * | 9763d87 (origin/feature/conflict-a, feature/conflict-a) Оновлено .gitignore
* | | 377bb3d Merge pull request #5 from DanyloShi/feature/conflict-a
|\| | 
| * | 730f5f4 Оновлено README (3 питання)
|/ /  
* |   c160718 Merge pull request #4 from DanyloShi/feature/data_research
|\ \  
| * | 3030f9d (origin/feature/data_research, feature/data_research) Додано код для аналізу даних та побудови моделі
* | |   91a9dc5 Merge pull request #3 from DanyloShi/feature/data_quality_analysis
|\ \ \  
| |/ /  
|/| |   
| * | 7c6c569 (origin/feature/data_quality_analysis, feature/data_quality_analysis) Додано аналіз якості даних
* | | 9ed2d5b Merge pull request #2 from DanyloShi/feature/data_load
|\| | 
| * | 387a439 (origin/feature/data_load, feature/data_load) Додано README.md в папку з даними
* | | d03b94c Merge pull request #1 from DanyloShi/feature/data_load
|\| | 
| * | 2db1979 Додано скрипт для завантаження даних
|/ /  
| * bd42d0a (origin/feature/conflict-b, feature/conflict-b) Оновлено README (3 питання) конлфікт В
|/  
:...skipping...
* bf899f3 (HEAD -> main, tag: v0.1.0, origin/main, origin/HEAD) Доадно changelog v0.1.0
*   4250e5e Merge pull request #8 from DanyloShi/feature/visualization
|\  
| * 7a112b1 (origin/feature/visualization, feature/visualization) Додано візуалізацію
|/  
*   5c986f6 Merge pull request #7 from DanyloShi/feature/conflict-b
|\  
| *   ac9e82a Merge branch 'main' into feature/conflict-b
| |\  
| |/  
|/|   
* |   6250646 Merge pull request #6 from DanyloShi/feature/conflict-a
|\ \  
| * | 9763d87 (origin/feature/conflict-a, feature/conflict-a) Оновлено .gitignore
* | | 377bb3d Merge pull request #5 from DanyloShi/feature/conflict-a
|\| | 
| * | 730f5f4 Оновлено README (3 питання)
|/ /  
* |   c160718 Merge pull request #4 from DanyloShi/feature/data_research
|\ \  
| * | 3030f9d (origin/feature/data_research, feature/data_research) Додано код для аналізу даних та побудови моделі
* | |   91a9dc5 Merge pull request #3 from DanyloShi/feature/data_quality_analysis
|\ \ \  
| |/ /  
|/| |   
| * | 7c6c569 (origin/feature/data_quality_analysis, feature/data_quality_analysis) Додано аналіз якості даних
* | | 9ed2d5b Merge pull request #2 from DanyloShi/feature/data_load
|\| | 
| * | 387a439 (origin/feature/data_load, feature/data_load) Додано README.md в папку з даними
* | | d03b94c Merge pull request #1 from DanyloShi/feature/data_load
|\| | 
| * | 2db1979 Додано скрипт для завантаження даних
|/ /  
| * bd42d0a (origin/feature/conflict-b, feature/conflict-b) Оновлено README (3 питання) конлфікт В
|/  
* 5fd8dcb Changed README.md
:...skipping...
* bf899f3 (HEAD -> main, tag: v0.1.0, origin/main, origin/HEAD) Доадно changelog v0.1.0
*   4250e5e Merge pull request #8 from DanyloShi/feature/visualization
|\  
| * 7a112b1 (origin/feature/visualization, feature/visualization) Додано візуалізацію
|/  
*   5c986f6 Merge pull request #7 from DanyloShi/feature/conflict-b
|\  
| *   ac9e82a Merge branch 'main' into feature/conflict-b
| |\  
| |/  
|/|   
* |   6250646 Merge pull request #6 from DanyloShi/feature/conflict-a
|\ \  
| * | 9763d87 (origin/feature/conflict-a, feature/conflict-a) Оновлено .gitignore
* | | 377bb3d Merge pull request #5 from DanyloShi/feature/conflict-a
|\| | 
| * | 730f5f4 Оновлено README (3 питання)
|/ /  
* |   c160718 Merge pull request #4 from DanyloShi/feature/data_research
|\ \  
| * | 3030f9d (origin/feature/data_research, feature/data_research) Додано код для аналізу даних та побудови моделі
* | |   91a9dc5 Merge pull request #3 from DanyloShi/feature/data_quality_analysis
|\ \ \  
| |/ /  
|/| |   
| * | 7c6c569 (origin/feature/data_quality_analysis, feature/data_quality_analysis) Додано аналіз якості даних
* | | 9ed2d5b Merge pull request #2 from DanyloShi/feature/data_load
|\| | 
| * | 387a439 (origin/feature/data_load, feature/data_load) Додано README.md в папку з даними
* | | d03b94c Merge pull request #1 from DanyloShi/feature/data_load
|\| | 
| * | 2db1979 Додано скрипт для завантаження даних
|/ /  
| * bd42d0a (origin/feature/conflict-b, feature/conflict-b) Оновлено README (3 питання) конлфікт В
|/  
* 5fd8dcb Changed README.md
* 81905e6 Initial commit
:...skipping...
* bf899f3 (HEAD -> main, tag: v0.1.0, origin/main, origin/HEAD) Доадно changelog v0.1.0
*   4250e5e Merge pull request #8 from DanyloShi/feature/visualization
|\  
| * 7a112b1 (origin/feature/visualization, feature/visualization) Додано візуалізацію
|/  
*   5c986f6 Merge pull request #7 from DanyloShi/feature/conflict-b
|\  
| *   ac9e82a Merge branch 'main' into feature/conflict-b
| |\  
| |/  
|/|   
* |   6250646 Merge pull request #6 from DanyloShi/feature/conflict-a
|\ \  
| * | 9763d87 (origin/feature/conflict-a, feature/conflict-a) Оновлено .gitignore
* | | 377bb3d Merge pull request #5 from DanyloShi/feature/conflict-a
|\| | 
| * | 730f5f4 Оновлено README (3 питання)
|/ /  
* |   c160718 Merge pull request #4 from DanyloShi/feature/data_research
|\ \  
| * | 3030f9d (origin/feature/data_research, feature/data_research) Додано код для аналізу даних та побудови моделі
* | |   91a9dc5 Merge pull request #3 from DanyloShi/feature/data_quality_analysis
|\ \ \  
| |/ /  
|/| |   
| * | 7c6c569 (origin/feature/data_quality_analysis, feature/data_quality_analysis) Додано аналіз якості даних
* | | 9ed2d5b Merge pull request #2 from DanyloShi/feature/data_load
|\| | 
| * | 387a439 (origin/feature/data_load, feature/data_load) Додано README.md в папку з даними
* | | d03b94c Merge pull request #1 from DanyloShi/feature/data_load
|\| | 
| * | 2db1979 Додано скрипт для завантаження даних
|/ /  
| * bd42d0a (origin/feature/conflict-b, feature/conflict-b) Оновлено README (3 питання) конлфікт В
|/  
* 5fd8dcb Changed README.md
* 81905e6 Initial commit
~
(END)...skipping...
* bf899f3 (HEAD -> main, tag: v0.1.0, origin/main, origin/HEAD) Доадно changelog v0.1.0
*   4250e5e Merge pull request #8 from DanyloShi/feature/visualization
|\  
| * 7a112b1 (origin/feature/visualization, feature/visualization) Додано візуалізацію
|/  
*   5c986f6 Merge pull request #7 from DanyloShi/feature/conflict-b
|\  
| *   ac9e82a Merge branch 'main' into feature/conflict-b
| |\  
| |/  
|/|   
* |   6250646 Merge pull request #6 from DanyloShi/feature/conflict-a
|\ \  
| * | 9763d87 (origin/feature/conflict-a, feature/conflict-a) Оновлено .gitignore
* | | 377bb3d Merge pull request #5 from DanyloShi/feature/conflict-a
|\| | 
| * | 730f5f4 Оновлено README (3 питання)
|/ /  
* |   c160718 Merge pull request #4 from DanyloShi/feature/data_research
|\ \  
| * | 3030f9d (origin/feature/data_research, feature/data_research) Додано код для аналізу даних та побудови моделі
* | |   91a9dc5 Merge pull request #3 from DanyloShi/feature/data_quality_analysis
|\ \ \  
| |/ /  
|/| |   
| * | 7c6c569 (origin/feature/data_quality_analysis, feature/data_quality_analysis) Додано аналіз якості даних
* | | 9ed2d5b Merge pull request #2 from DanyloShi/feature/data_load
|\| | 
| * | 387a439 (origin/feature/data_load, feature/data_load) Додано README.md в папку з даними
* | | d03b94c Merge pull request #1 from DanyloShi/feature/data_load
|\| | 
| * | 2db1979 Додано скрипт для завантаження даних
|/ /  
| * bd42d0a (origin/feature/conflict-b, feature/conflict-b) Оновлено README (3 питання) конлфікт В
|/  
* 5fd8dcb Changed README.md
* 81905e6 Initial commit
~
~
(END)...skipping...
* bf899f3 (HEAD -> main, tag: v0.1.0, origin/main, origin/HEAD) Доадно changelog v0.1.0
*   4250e5e Merge pull request #8 from DanyloShi/feature/visualization
|\  
| * 7a112b1 (origin/feature/visualization, feature/visualization) Додано візуалізацію
|/  
*   5c986f6 Merge pull request #7 from DanyloShi/feature/conflict-b
|\  
| *   ac9e82a Merge branch 'main' into feature/conflict-b
| |\  
| |/  
|/|   
* |   6250646 Merge pull request #6 from DanyloShi/feature/conflict-a
|\ \  
| * | 9763d87 (origin/feature/conflict-a, feature/conflict-a) Оновлено .gitignore
* | | 377bb3d Merge pull request #5 from DanyloShi/feature/conflict-a
|\| | 
| * | 730f5f4 Оновлено README (3 питання)
|/ /  
* |   c160718 Merge pull request #4 from DanyloShi/feature/data_research
|\ \  
| * | 3030f9d (origin/feature/data_research, feature/data_research) Додано код для аналізу даних та побудови моделі
* | |   91a9dc5 Merge pull request #3 from DanyloShi/feature/data_quality_analysis
|\ \ \  
| |/ /  
|/| |   
| * | 7c6c569 (origin/feature/data_quality_analysis, feature/data_quality_analysis) Додано аналіз якості даних
* | | 9ed2d5b Merge pull request #2 from DanyloShi/feature/data_load
|\| | 
| * | 387a439 (origin/feature/data_load, feature/data_load) Додано README.md в папку з даними
* | | d03b94c Merge pull request #1 from DanyloShi/feature/data_load
|\| | 
| * | 2db1979 Додано скрипт для завантаження даних
|/ /  
| * bd42d0a (origin/feature/conflict-b, feature/conflict-b) Оновлено README (3 питання) конлфікт В
|/  
* 5fd8dcb Changed README.md
* 81905e6 Initial commit