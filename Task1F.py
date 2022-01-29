from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

def run():
    """
    The function return the list of stations that have inconsistent range data
    """

    stations = build_station_list()
    list_of_stations = inconsistent_typical_range_stations(stations)
    list_of_station_names = sorted([station.name for station in list_of_stations])
    
    print(list_of_station_names)


if __name__ == "__main__":
    print("---Demonstration 1 --- for task 1F")
    print("The list of station with inconsistent data")
    run()
