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
    # Interpolate in NaN columns
    nan_columns = ["location_altitude","location_speedAccuracy",
                   "location_bearingAccuracy","location_latitude",
                   "location_altitudeAboveMeanSeaLevel","location_bearing",
                   "location_horizontalAccuracy","location_verticalAccuracy",
                   "location_longitude","location_speed"]
    new_names = [f"{name}_filled" for name in nan_columns]
    csv[new_names] = csv[nan_columns].interpolate(method="linear", axis=0)

    # Make first derivatives and median filters
    interesting_cols = [x for x in csv.columns if x not in nan_columns]
    carefull_columns = ["accelerometer_z","accelerometer_y","accelerometer_x"]
    for d in interesting_cols:
        csv[f"{d}_diff"] = csv[d].diff()
        csv[f"{d}_filtered"] = csv[d].rolling(70).median() if d not in carefull_columns else csv[d].rolling(40).mean()

    data = csv[["accelerometer_z_filtered","accelerometer_y_filtered","accelerometer_x_filtered"]]
    csv["summed_acc"] = -data.sum(axis=1, skipna=True)
    csv["stop_only"] = -csv["accelerometer_y_filtered"].where(csv["accelerometer_y_filtered"] > 0, other=0)
    # csv["acc"] = -data["accelerometer_y_filtered"]
    # csv["acc.combined"] = csv["acc"] * np.abs(csv["accelerometer_x_filtered"])


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

