import argparse
import numpy as np
import pandas as pd
import geopandas as gpd

import turniton.data as tiod
import turniton.map as tiom

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--data-id", type=int, help="ID of data sample")
    parser.add_argument("-c", "--color-column", default=None, help="Which column should be used to colour points on map")
    parser.add_argument("-t", "--opaqe-threshold", type=float, default=None, help="Above this value points on scatter are opaque")
    return parser.parse_args()

def main(opts):
    data = tiod.get_data(f"data/{opts.data_id}.csv")
    tiod.clear_visualisations()

    # Some uncorellated stuff
    tiod.visualisation(data, ["location_latitude_filled"], "Lat")
    tiod.visualisation(data, ["summed_acc"], "SA")
    tiod.visualisation(data, ["accelerometer_y_filtered"], "Ay")
    tiod.visualisation(data, ["accelerometer_x_filtered"], "Ax")
    tiod.visualisation(data, ["accelerometer_z_filtered"], "Az")
    tiod.visualisation(data, ["accelerometer_x_filtered", "accelerometer_z_filtered"], "corr_acc", correlation=True)

    # Geo Stuff
    tiod.visualisation(data, ["location_longitude_filled"], "Long")
    tiod.visualisation(data, ["location_longitude_filled_filtered"], "Long_filtered")
    tiod.visualisation(data, ["location_longitude_filled", "location_latitude_filled"], "GPS", correlation=True)
    tiod.visualisation(data, ["location_longitude_filled_filtered", "location_latitude_filled_filtered"], "GPS_filtered", correlation=True)
    
    # Maps
    tiom.map_it(data, ["location_longitude_filled_filtered", "location_latitude_filled_filtered"], "Map", color_column=opts.color_column, threshold=opts.opaqe_threshold)

def test():
    data = tiod.get_data("data/1.csv")
    print(data["location_altitude"])
    print(data["location_altitude"].ffill())


if __name__=="__main__":
    opts = parse_args()
    main(opts)
    # test()

