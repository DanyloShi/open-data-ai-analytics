import pandas as pd


def quality_report(df: pd.DataFrame) -> dict:
    report = {}

    report["shape"] = df.shape
    report["columns"] = list(df.columns)

    report["missing_by_column"] = df.isna().sum().to_dict()

    report["duplicate_rows"] = int(df.duplicated().sum())

    report["dtypes"] = df.dtypes.astype(str).to_dict()

    return report


if __name__ == "__main__":
    from src.data_load import load_data

    df = load_data()
    rep = quality_report(df)

    print("DATA QUALITY REPORT")
    print(f"Shape: {rep['shape']}")
    print(f"Duplicate rows: {rep['duplicate_rows']}")
    print("Missing by column:")
    
    for k, v in rep["missing_by_column"].items():
        print(f"{k}: {v}")
    
    print("Dtypes:")
    for k, v in rep["dtypes"].items():
        print(f"{k}: {v}")