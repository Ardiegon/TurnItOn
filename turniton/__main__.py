import numpy as np
import pandas as pd
import geopandas as gpd

import turniton.data as tiod

def main():
    data = tiod.get_data("data/1.csv")
    tiod.print_data(data)



