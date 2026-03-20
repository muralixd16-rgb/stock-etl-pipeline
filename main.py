from src.extract import extract_data
from src.transform import transform_data
from src.load import load_to_postgres, load_to_mongo

def run_pipeline():
    df = extract_data("google.csv")
    df = transform_data(df)

    load_to_postgres(df)
    load_to_mongo(df)

if __name__ == "__main__":
    run_pipeline()