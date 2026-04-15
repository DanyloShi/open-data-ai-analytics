from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))


from common.db_utils import connect, wait_for_table
from common.pipeline_config import DB_PATH, REPORTS_DIR, ensure_directories


def build_quality_report() -> dict:
    ensure_directories()
    wait_for_table(DB_PATH, "air_quality")

    with connect(DB_PATH) as conn:
        total_rows = conn.execute("SELECT COUNT(*) FROM air_quality").fetchone()[0]
        missing_aqi = conn.execute("SELECT COUNT(*) FROM air_quality WHERE aqi IS NULL").fetchone()[0]
        missing_pm25 = conn.execute("SELECT COUNT(*) FROM air_quality WHERE pm25 IS NULL").fetchone()[0]
        duplicate_rows = conn.execute(
            """
            SELECT COALESCE(SUM(cnt - 1), 0)
            FROM (
                SELECT city_id, logged_at, COUNT(*) AS cnt
                FROM air_quality
                GROUP BY city_id, logged_at
                HAVING cnt > 1
            )
            """
        ).fetchone()[0]
        invalid_negative = conn.execute(
            "SELECT COUNT(*) FROM air_quality WHERE (aqi < 0) OR (pm25 < 0)"
        ).fetchone()[0]

    report = {
        "db_path": str(DB_PATH),
        "total_rows": int(total_rows),
        "missing_aqi": int(missing_aqi),
        "missing_pm25": int(missing_pm25),
        "duplicate_rows": int(duplicate_rows),
        "invalid_negative_values": int(invalid_negative),
    }

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    (REPORTS_DIR / "quality_report.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    (REPORTS_DIR / "quality_report.txt").write_text(
        "\n".join([
            f"Rows total: {report['total_rows']}",
            f"Missing AQI: {report['missing_aqi']}",
            f"Missing PM2.5: {report['missing_pm25']}",
            f"Duplicate rows: {report['duplicate_rows']}",
            f"Negative values: {report['invalid_negative_values']}",
        ])
        + "\n",
        encoding="utf-8",
    )

    return report


if __name__ == "__main__":
    result = build_quality_report()
    print(json.dumps(result, indent=2, ensure_ascii=False))
