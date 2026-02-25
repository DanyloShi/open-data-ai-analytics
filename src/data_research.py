import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.linear_model import LinearRegression


def prepare_df(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df = df.dropna(subset=["aqi", "pm25"])

    return df


def train_simple_model(df: pd.DataFrame) -> float:
    X = df[["pm25"]]
    y = df["aqi"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    mae = mean_absolute_error(y_test, preds)
    return float(mae)


if __name__ == "__main__":
    from src.data_load import load_data

    df = load_data()
    df = prepare_df(df)

    print("BASIC STATS")
    print(df[["aqi", "pm25"]].describe())

    mae = train_simple_model(df)
    print(f"\nSimple model MAE (predict AQI from PM2.5): {mae:.3f}")