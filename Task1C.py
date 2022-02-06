from distutils.command.build import build
from floodsystem.geo import stations_by_distance, stations_within_radius
from floodsystem.stationdata import build_station_list
from floodsystem.utils import sorted_by_key


def run():
    """
    This function initiate the required demonstration program
    """
    stations = build_station_list()

    stations_in_radius = stations_within_radius(stations, (52.2053, 0.1218), 10)

    list_of_stations = []

    for item in stations_in_radius:
        list_of_stations.append(item.name)

    list_of_stations.sort()
    print(list_of_stations)

if __name__ == "__main__":
    """
    Define the function to run the demonstration code
    """

    
    print("---Demonstration 1 --- for task 1C")
    run()
