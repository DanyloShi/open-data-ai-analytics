from pathlib import Path
import matplotlib

# Use a non-interactive backend so CI/self-hosted runs do not need a GUI.
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

FIG_DIR = Path("reports/figures")
FIG_DIR.mkdir(parents=True, exist_ok=True)


def plot_aqi_distribution(df: pd.DataFrame) -> Path:
    fig_path = FIG_DIR / "aqi_distribution.png"

    series = pd.to_numeric(df["aqi"], errors="coerce").dropna()

    plt.figure()
    plt.hist(series, bins=40)
    plt.title("AQI distribution")
    plt.xlabel("AQI")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(fig_path, dpi=200)
    plt.close()

    return fig_path


def plot_pm25_over_time(df: pd.DataFrame) -> Path:
    fig_path = FIG_DIR / "pm25_over_time.png"

    dft = df.copy()
    dft["logged_at"] = pd.to_datetime(dft["logged_at"], errors="coerce")
    dft["pm25"] = pd.to_numeric(dft["pm25"], errors="coerce")

    dft = dft.dropna(subset=["logged_at", "pm25"]).sort_values("logged_at")
    daily = dft.set_index("logged_at")["pm25"].resample("D").mean().dropna()

    plt.figure()
    plt.plot(daily.index, daily.values)
    plt.title("Daily mean PM2.5 over time")
    plt.xlabel("Date")
    plt.ylabel("PM2.5")
    plt.tight_layout()
    plt.savefig(fig_path, dpi=200)
    plt.close()

    return fig_path


if __name__ == "__main__":
    from src.data_load import load_data

    df = load_data()

    p1 = plot_aqi_distribution(df)
    p2 = plot_pm25_over_time(df)

    print(f"Saved: {p1}")
    print(f"Saved: {p2}")
