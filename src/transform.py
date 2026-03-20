def transform_data(df):
    # Example transformations
    df.dropna(inplace=True)
    df["volume"] = df["volume"].astype(int)

    print("✅ Data transformed")
    return df