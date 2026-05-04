import asyncio
import json
import time
from pathlib import Path

from utils import load_data
from src.engineering_1_processing import (
    anomaly_detection,
    hottest_coldest,
    rainfall_humidity_stats,
    rolling_avg,
    temperature_stats,
)
from src.engineering_2_asyncio import run_concurrent_tasks

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "weather_data.csv"
OUTPUT_FILE_1 = BASE_DIR / "output_engineering_1.json"
OUTPUT_FILE_2 = BASE_DIR / "output_engineering_2.json"


def main():
    df = load_data(DATA_FILE)
    df = rolling_avg(df, window=2)

    results = {
        "temperature_stats": temperature_stats(df),
        "extremes": hottest_coldest(df),
        "anomalies": anomaly_detection(df),
        "rainfall_stats": rainfall_humidity_stats(df),
    }

    print("\nENGINEERING 1 OUTPUT")
    print(json.dumps(results, indent=2, default=str))

    with OUTPUT_FILE_1.open("w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, default=str)

    print("Engineering 1 Output Saved:", OUTPUT_FILE_1)
    return df


async def run_engineering_2(df):
    global_results = await run_concurrent_tasks(df)

    with OUTPUT_FILE_2.open("w", encoding="utf-8") as f:
        json.dump(global_results, f, indent=2, default=str)

    print("\nEngineering 2 Output Saved:", OUTPUT_FILE_2)


if __name__ == "__main__":
    start = time.time()

    df = main()
    asyncio.run(run_engineering_2(df))

    end = time.time()
    print("\nExecution Time:", end - start)
