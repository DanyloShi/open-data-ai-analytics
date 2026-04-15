from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))


from common.db_utils import connect, wait_for_table
from common.pipeline_config import DB_PATH, REPORTS_DIR, ensure_directories


def build_research_report() -> dict:
    ensure_directories()
    wait_for_table(DB_PATH, "air_quality")

    with connect(DB_PATH) as conn:
        total_rows = conn.execute("SELECT COUNT(*) FROM air_quality").fetchone()[0]
        cities = conn.execute("SELECT COUNT(DISTINCT city_id) FROM air_quality").fetchone()[0]

        stats = conn.execute(
            """
            SELECT
                AVG(aqi), MIN(aqi), MAX(aqi),
                AVG(pm25), MIN(pm25), MAX(pm25)
            FROM air_quality
            """
        ).fetchone()

        top_cities = conn.execute(
            """
            SELECT city_id, ROUND(AVG(aqi), 2) AS avg_aqi
            FROM air_quality
            WHERE aqi IS NOT NULL
            GROUP BY city_id
            ORDER BY avg_aqi DESC
            LIMIT 5
            """
        ).fetchall()

    report = {
        "db_path": str(DB_PATH),
        "total_rows": int(total_rows),
        "distinct_cities": int(cities),
        "aqi_avg": None if stats[0] is None else round(float(stats[0]), 3),
        "aqi_min": stats[1],
        "aqi_max": stats[2],
        "pm25_avg": None if stats[3] is None else round(float(stats[3]), 3),
        "pm25_min": stats[4],
        "pm25_max": stats[5],
        "top_cities_by_avg_aqi": [
            {"city_id": row[0], "avg_aqi": row[1]} for row in top_cities
        ],
    }

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    (REPORTS_DIR / "research_report.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    (REPORTS_DIR / "research_report.txt").write_text(
        "\n".join([
            f"Rows total: {report['total_rows']}",
            f"Distinct cities: {report['distinct_cities']}",
            f"AQI avg/min/max: {report['aqi_avg']} / {report['aqi_min']} / {report['aqi_max']}",
            f"PM2.5 avg/min/max: {report['pm25_avg']} / {report['pm25_min']} / {report['pm25_max']}",
        ])
        + "\n",
        encoding="utf-8",
    )

    return report


if __name__ == "__main__":
    result = build_research_report()
    print(json.dumps(result, indent=2, ensure_ascii=False))
