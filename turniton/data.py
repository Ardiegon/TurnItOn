import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from pathlib import Path

import turniton.utils as tiou

def get_data(path:str)->pd.DataFrame:
    csv = pd.read_csv(path)
    data = preprocess_csv(csv)
    return data

def preprocess_csv(csv: pd.DataFrame)->pd.DataFrame:
    nan_columns = ["location_altitude","location_speedAccuracy",
                   "location_bearingAccuracy","location_latitude",
                   "location_altitudeAboveMeanSeaLevel","location_bearing",
                   "location_horizontalAccuracy","location_verticalAccuracy",
                   "location_longitude","location_speed"]

    new_names = [f"{name}_filled" for name in nan_columns]
    csv[new_names] = csv[nan_columns].interpolate(method="linear", axis=0)

    interesting_cols = [x for x in csv.columns if x not in nan_columns]
    for d in interesting_cols:
        csv[f"{d}_diff"] = csv[d].diff()
        csv[f"{d}_filtered"] = csv[d].rolling(70).median()

    return csv

def explain_data(data: pd.DataFrame)->None:
    data.info()
    data.describe()

def visualisation(data:pd.DataFrame, columns:list, title:str = "visualization", correlation = False)->None:
    path = Path(f"visualisations/{title}_{tiou.get_unique_tag()}")
    if correlation and len(columns) == 2:
        data[columns].plot(x = columns[0], y=columns[1])
    else:
        data[columns].plot()
    plt.title(title)
    plt.savefig(path)

def clear_visualisations()->None:   
    folder_path = Path(f"visualisations")
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".png"):
            file_path = os.path.join(folder_path, file_name)
            os.remove(file_path)

