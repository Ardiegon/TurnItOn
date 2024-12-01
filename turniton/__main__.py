import numpy as np
import pandas as pd
import geopandas as gpd

import turniton.data as tiod

def main():
    data = tiod.get_data("data/1.csv")
    tiod.explain_data(data)
    tiod.visualisation(data, ["location_latitude"], "Lat")
    tiod.visualisation(data, ["location_longitude"], "Long")
    tiod.visualisation(data, ["location_latitude","location_longitude"], "GPS", correlation=True)

def test():
    data = tiod.get_data("data/1.csv")
    print(data["location_altitude"])
    print(data["location_altitude"].ffill())


if __name__=="__main__":
    main()
    # test()

