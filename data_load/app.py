from __future__ import annotations

import csv
import json
import sqlite3
import sys
from datetime import datetime, timedelta
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from common.pipeline_config import CSV_PATH, DB_PATH, REPORTS_DIR, ensure_directories


def _generate_sample_csv(csv_path: Path) -> None:
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    base = datetime(2024, 1, 1, 0, 0, 0)
    rows = []
    for i in range(48):
        rows.append(
            {
                "city_id": str((i % 4) + 1),
                "aqi": round(25 + (i % 20) * 1.8, 2),
                "pm25": round(5 + (i % 18) * 1.3, 2),
                "logged_at": (base + timedelta(hours=i)).strftime("%Y-%m-%d %H:%M:%S"),
            }
        )

    with csv_path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=["city_id", "aqi", "pm25", "logged_at"])
        writer.writeheader()
        writer.writerows(rows)


def _safe_float(value: str) -> float | None:
    value = (value or "").strip()
    if value == "":
        return None
    try:
        return float(value)
    except ValueError:
        return None


def _safe_text(value: str) -> str | None:
    value = (value or "").strip()
    return value or None


def load_csv_to_sqlite() -> dict:
    ensure_directories()
    if not CSV_PATH.exists():
        _generate_sample_csv(CSV_PATH)

    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS air_quality (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                city_id TEXT,
                aqi REAL,
                pm25 REAL,
                logged_at TEXT
            )
            """
        )
        conn.execute("DELETE FROM air_quality")

        inserted = 0
        with CSV_PATH.open("r", encoding="utf-8") as fh:
            reader = csv.DictReader(fh)
            for row in reader:
                conn.execute(
                    "INSERT INTO air_quality (city_id, aqi, pm25, logged_at) VALUES (?, ?, ?, ?)",
                    (
                        _safe_text(row.get("city_id", "")),
                        _safe_float(row.get("aqi", "")),
                        _safe_float(row.get("pm25", "")),
                        _safe_text(row.get("logged_at", "")),
                    ),
                )
                inserted += 1

        conn.commit()

    summary = {
        "csv_path": str(CSV_PATH),
        "db_path": str(DB_PATH),
        "rows_inserted": inserted,
    }

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    (REPORTS_DIR / "load_summary.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    (REPORTS_DIR / "load_summary.txt").write_text(
        f"Rows inserted: {inserted}\nDB: {DB_PATH}\nCSV: {CSV_PATH}\n",
        encoding="utf-8",
    )

    return summary


if __name__ == "__main__":
    result = load_csv_to_sqlite()
    print(json.dumps(result, indent=2, ensure_ascii=False))
