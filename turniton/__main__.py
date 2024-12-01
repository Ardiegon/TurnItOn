import numpy as np
import pandas as pd
import geopandas as gpd

import turniton.data as tiod
import turniton.map as tiom

def main():
    data = tiod.get_data("data/1.csv")
    # tiod.explain_data(data)
    tiod.clear_visualisations()
    tiod.visualisation(data, ["location_latitude_filled"], "Lat")
    tiod.visualisation(data, ["location_longitude_filled"], "Long")
    tiod.visualisation(data, ["location_longitude_filled_filtered"], "Long_filtered")
    tiod.visualisation(data, ["location_longitude_filled", "location_latitude_filled"], "GPS", correlation=True)
    tiod.visualisation(data, ["location_longitude_filled_filtered", "location_latitude_filled_filtered"], "GPS_filtered", correlation=True)
    tiom.map_it(data, ["location_longitude_filled_filtered", "location_latitude_filled_filtered"], "On Map")

def test():
    data = tiod.get_data("data/1.csv")
    print(data["location_altitude"])
    print(data["location_altitude"].ffill())


if __name__=="__main__":
    main()
    # test()

