from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list

def run():
    """
    This function will run the imported rivers_by_station_number
    """
    stations = build_station_list()
    list_of_tuples = rivers_by_station_number(stations, 9)
    print(list_of_tuples)


if __name__ == "__main__":
    print("---Demonstration 1 --- for task 1E")
    run()