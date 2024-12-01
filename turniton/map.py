import pickle
import matplotlib.pyplot as plt
import osmnx as ox
import contextily as ctx

from pathlib import Path

import turniton.utils as tiou

def map_it(data, x_y_names:list, color_column:None, title = "Map"):
    path = Path(f"visualisations/{title}_{tiou.get_unique_tag()}")

    with open('data/jk_map.pickle', 'rb') as handle:
        map = pickle.load(handle)

    fig, ax = plt.subplots(figsize=(10, 10))
    data[x_y_names].plot.scatter(x = x_y_names[0], y=x_y_names[1], ax=ax)
    map.plot(ax=ax, linewidth=0.8, edgecolor="gray")  # Plot the roads
    ctx.add_basemap(ax, source=ctx.providers.CartoDB.Positron, crs=map.crs)  # Add basemap
    ax.set_title(title, fontsize=16)
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.savefig(path)

        

