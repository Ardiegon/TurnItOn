import pickle
import matplotlib.pyplot as plt
import osmnx as ox
import contextily as ctx

from pathlib import Path

import turniton.utils as tiou



def map_it(data, x_y_names: list, title="Map", color_column:str=None, threshold:float=None, threshold_type:str = "above", map_id: int = 1):
    path = Path(f"visualisations/{title}_{tiou.get_unique_tag()}")

    fig, ax = plt.subplots(figsize=(10, 10))
    data.plot(x=x_y_names[0], y=x_y_names[1], ax=ax, c="black")

    if threshold is not None and color_column is not None:
        if threshold_type == "above":
            data = data[data[color_column] > threshold]
        elif threshold_type == "below":
            data = data[data[color_column] < -threshold]
        elif threshold_type == "abs":
            data = data[(data[color_column] > threshold) | (data[color_column] < -threshold)]
        else:
            raise "threshold type can be only 'above', 'below', or 'abs'"

    with open(f'data/jk_map_{map_id}.pickle', 'rb') as handle:
        map = pickle.load(handle)

    if color_column is None:
        data.plot.scatter(x=x_y_names[0], y=x_y_names[1], ax=ax)
    else:
        scatter = ax.scatter(
            data[x_y_names[0]], 
            data[x_y_names[1]], 
            c=data[color_column], 
            cmap='jet', 
            alpha=1.0
        )
        cbar = plt.colorbar(scatter, ax=ax)
        cbar.set_label(color_column, fontsize=12)

    map.plot(ax=ax, linewidth=0.8, edgecolor="gray")
    
    ctx.add_basemap(ax, source=ctx.providers.CartoDB.Positron, crs=map.crs)
    
    ax.set_title(title, fontsize=16)
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")

    plt.savefig(path)
    plt.close(fig)

        

