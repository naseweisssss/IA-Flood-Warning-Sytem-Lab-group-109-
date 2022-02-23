from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import MonitoringStation

from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level



def run():
    stations = build_station_list()
    update_water_levels(stations)
    list_of_highest_stations = stations_highest_rel_level(stations, 10)

    for item in list_of_highest_stations:
        print(item.name, item.relative_water_level())

if __name__ == "__main__":
  print("---Demonstration 1 --- for task 2C")
  run()
