from datetime import datetime, timedelta
import numpy as np

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.flood import stations_highest_rel_level


def run():
    stations = build_station_list()
    update_water_levels(stations)
    list_of_highest_rel_level = stations_highest_rel_level(stations, 5)
    
    for station in list_of_highest_rel_level:
        dates, levels = fetch_measure_levels(station.measure_id, dt=timedelta(days=2))
        plot_water_level_with_fit(station, dates, levels, 4)


if __name__ == "__main__":
    print("---Demonstration 1 --- for task 2F")
    run()