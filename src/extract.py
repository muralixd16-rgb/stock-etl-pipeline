import pandas as pd

def extract_data(file_path):
    df = pd.read_csv(file_path)

    df.columns = [
        "trade_date",
        "open_price",
        "high_price",
        "low_price",
        "close_price",
        "adj_close_price",
        "volume"
    ]

    print("✅ Data extracted from CSV")
    return df