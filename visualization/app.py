from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from collections import defaultdict
from datetime import datetime

import matplotlib

from common.db_utils import connect, wait_for_table
from common.pipeline_config import DB_PATH, PLOTS_DIR, REPORTS_DIR, ensure_directories

# Headless backend for CI/Docker.
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def _parse_datetime(value: str | None) -> datetime | None:
    if not value:
        return None
    for fmt in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%dT%H:%M:%S"):
        try:
            return datetime.strptime(value, fmt)
        except ValueError:
            continue
    return None


def create_plots() -> dict:
    ensure_directories()
    wait_for_table(DB_PATH, "air_quality")

    with connect(DB_PATH) as conn:
        rows = conn.execute("SELECT logged_at, aqi, pm25 FROM air_quality").fetchall()

    aqi_values = [float(r[1]) for r in rows if r[1] is not None]

    daily_pm25 = defaultdict(list)
    for logged_at, _aqi, pm25 in rows:
        if pm25 is None:
            continue
        dt = _parse_datetime(logged_at)
        if dt is None:
            continue
        daily_pm25[dt.date().isoformat()].append(float(pm25))

    PLOTS_DIR.mkdir(parents=True, exist_ok=True)

    hist_path = PLOTS_DIR / "aqi_hist.png"
    plt.figure(figsize=(8, 4))
    if aqi_values:
        plt.hist(aqi_values, bins=20)
    else:
        plt.text(0.5, 0.5, "No AQI data", ha="center", va="center")
    plt.title("AQI distribution")
    plt.xlabel("AQI")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(hist_path, dpi=150)
    plt.close()

    trend_path = PLOTS_DIR / "pm25_daily_mean.png"
    plt.figure(figsize=(8, 4))
    if daily_pm25:
        days = sorted(daily_pm25)
        means = [sum(daily_pm25[d]) / len(daily_pm25[d]) for d in days]
        plt.plot(days, means, marker="o")
        plt.xticks(rotation=45, ha="right")
    else:
        plt.text(0.5, 0.5, "No PM2.5 data", ha="center", va="center")
    plt.title("Daily mean PM2.5")
    plt.xlabel("Date")
    plt.ylabel("PM2.5")
    plt.tight_layout()
    plt.savefig(trend_path, dpi=150)
    plt.close()

    report = {
        "plots": [hist_path.name, trend_path.name],
        "rows_used": len(rows),
        "aqi_points": len(aqi_values),
    }

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    (REPORTS_DIR / "visualization_report.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    return report


if __name__ == "__main__":
    result = create_plots()
    print(json.dumps(result, indent=2, ensure_ascii=False))
