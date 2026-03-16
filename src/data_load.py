from __future__ import annotations

from pathlib import Path
from typing import Iterable

import pandas as pd


DATA_DIR = Path(__file__).resolve().parents[1] / "data/raw"
DATA_PATH = DATA_DIR / "air_quality.csv"


def _generate_sample_rows() -> Iterable[dict]:
    base = pd.Timestamp("2023-01-01 00:00:00")
    sample_values = [
        {"city_id": "1", "aqi": 35, "pm25": 9.1},
        {"city_id": "1", "aqi": 42, "pm25": 11.5},
        {"city_id": "1", "aqi": 58, "pm25": 16.2},
        {"city_id": "2", "aqi": 21, "pm25": 4.3},
        {"city_id": "2", "aqi": 28, "pm25": 5.8},
        {"city_id": "3", "aqi": 74, "pm25": 22.2},
    ]
    # Repeat sequence across a couple of days to mimic time series.
    for day in range(10):
        for idx, row in enumerate(sample_values):
            yield {
                "city_id": row["city_id"],
                "aqi": row["aqi"],
                "pm25": row["pm25"],
                "logged_at": (base + pd.Timedelta(hours=day * len(sample_values) + idx)).strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),
            }


def _ensure_sample_dataset() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    df = pd.DataFrame(list(_generate_sample_rows()))
    df.to_csv(DATA_PATH, index=False)


def load_data() -> pd.DataFrame:
    """
    Load the air quality dataset. If the canonical CSV is missing (e.g. in CI),
    synthesize a lightweight sample so that quality checks and visualizations can still run.
    """

    if not DATA_PATH.exists():
        _ensure_sample_dataset()

    return pd.read_csv(DATA_PATH, low_memory=False)


if __name__ == "__main__":
    df = load_data()
    print(df.head())
