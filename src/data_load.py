from pathlib import Path
import pandas as pd


DATA_PATH = Path("data/raw/air_quality.csv")


def load_data():
    return pd.read_csv(DATA_PATH)


if __name__ == "__main__":
    df = load_data()
    print("Перші 5 рядків даних:")
    print(df.head())