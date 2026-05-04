import pandas as pd
import numpy as np


def temperature_stats(df):
    return df.groupby('city')['temperature_c'].agg(
        avg_temp='mean',
        median_temp='median',
        std_temp='std'
    ).to_dict()


def hottest_coldest(df):
    result = {}

    for city in df['city'].unique():
        city_df = df[df['city'] == city]

        hottest = city_df.loc[city_df['temperature_c'].idxmax()]
        coldest = city_df.loc[city_df['temperature_c'].idxmin()]

        result[city] = {
            "hottest_day": str(hottest['date']),
            "coldest_day": str(coldest['date'])
        }

    return result


def rolling_avg(df, window=2):
    df['rolling_temp'] = df.groupby('city')['temperature_c'].transform(
        lambda x: x.rolling(window).mean()
    )
    return df


def anomaly_detection(df):
    result = {}

    for city in df['city'].unique():
        city_df = df[df['city'] == city]

        mean = city_df['temperature_c'].mean()
        std = city_df['temperature_c'].std()

        z_scores = (city_df['temperature_c'] - mean) / std

        anomalies = city_df[np.abs(z_scores) > 1.5]

        result[city] = anomalies[['date', 'temperature_c']].to_dict('records')

    return result


def rainfall_humidity_stats(df):
    return df.groupby('city').agg({
        'rainfall_mm': ['sum', 'mean'],
        'humidity': ['mean']
    }).to_dict()