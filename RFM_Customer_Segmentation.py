import pandas as pd
from pathlib import Path

# Paths
DATA_DIR = Path("data")
FILE_PATH = DATA_DIR / "Superstore.csv"

def load_data():
    print(f"Loading data from: {FILE_PATH}")
    df = pd.read_csv(FILE_PATH, encoding="latin-1")
    print("Data loaded successfully!")
    print(df.head())
    print("\nData Shape:", df.shape)
    return df

if __name__ == "__main__":
    load_data()

