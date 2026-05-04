# utils.py

import pandas as pd
import os

def load_data(filename="weather_data.csv"):
   
    BASE_DIR = os.path.dirname(__file__)

    file_path = os.path.join(BASE_DIR, filename)

  
    df = pd.read_csv(file_path)

    # Preprocessing
    df['date'] = pd.to_datetime(df['date'])
    df = df.dropna()
    df = df.sort_values(by=['city', 'date'])

    return df