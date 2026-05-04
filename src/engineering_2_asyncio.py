import asyncio
from concurrent.futures import ThreadPoolExecutor

from src.engineering_1_processing import (
    anomaly_detection,
    hottest_coldest,
    rainfall_humidity_stats,
    temperature_stats,
)


async def _run_in_thread(fn, df):
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(None, fn, df)


async def run_concurrent_tasks(df):
    with ThreadPoolExecutor(max_workers=4) as executor:
        loop = asyncio.get_running_loop()
        tasks = [
            loop.run_in_executor(executor, temperature_stats, df),
            loop.run_in_executor(executor, hottest_coldest, df),
            loop.run_in_executor(executor, anomaly_detection, df),
            loop.run_in_executor(executor, rainfall_humidity_stats, df),
        ]

        temperature_result, extremes_result, anomalies_result, rainfall_result = await asyncio.gather(*tasks)

    return {
        "temperature_stats": temperature_result,
        "extremes": extremes_result,
        "anomalies": anomalies_result,
        "rainfall_stats": rainfall_result,
    }













































































































































































