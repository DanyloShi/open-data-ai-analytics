from __future__ import annotations

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
WORK_DIR = Path(os.getenv("WORK_DIR", BASE_DIR / "artifacts"))
DB_PATH = Path(os.getenv("DB_PATH", WORK_DIR / "db" / "air_quality.db"))
REPORTS_DIR = Path(os.getenv("REPORTS_DIR", WORK_DIR / "reports"))
PLOTS_DIR = Path(os.getenv("PLOTS_DIR", WORK_DIR / "plots"))
CSV_PATH = Path(os.getenv("CSV_PATH", BASE_DIR / "data" / "dataset.csv"))


def ensure_directories() -> None:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)
