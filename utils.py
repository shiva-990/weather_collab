# utils.py

import os
from pathlib import Path

import pandas as pd


def load_data(filename="weather_data.csv"):
    if isinstance(filename, Path):
        file_path = filename
    else:
        base_dir = Path(__file__).resolve().parent
        file_path = Path(filename) if os.path.isabs(filename) else base_dir / filename

    if not file_path.exists():
        raise FileNotFoundError(f"Data file not found: {file_path}")

    df = pd.read_csv(file_path)

    # Preprocessing
    df["date"] = pd.to_datetime(df["date"])
    df = df.dropna()
    df = df.sort_values(by=["city", "date"]) 

    return df