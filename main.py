import time

from utils import load_data
from src.engineering_1_processing import (
    rolling_avg,
    temperature_stats,
    hottest_coldest,
    anomaly_detection,
    rainfall_humidity_stats
)

def main():

    df = load_data()

    df = rolling_avg(df, window=2)

    temp_stats = temperature_stats(df)

    extremes = hottest_coldest(df)

    anomalies = anomaly_detection(df)

    rainfall_stats = rainfall_humidity_stats(df)


    print("\nENGINEERING 1 OUTPUT")
    print("Temperature Stats:", temp_stats)
    print("Extremes:", extremes)
    print("Anomalies:", anomalies)
    print("Rainfall & Humidity:", rainfall_stats)


if __name__ == "__main__":
    start = time.time()

    main()

    end = time.time()
    print("\nExecution Time:", end - start)