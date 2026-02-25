from pathlib import Path
import pandas as pd


DATA_PATH = Path(__file__).resolve().parents[1] / "data/raw/air_quality.csv"


def load_data():
    return pd.read_csv(DATA_PATH)


if __name__ == "__main__":
    df = load_data()
    print(df.head())