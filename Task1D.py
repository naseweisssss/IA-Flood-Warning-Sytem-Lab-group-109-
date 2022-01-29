from floodsystem.geo import rivers_with_station, stations_by_river
from floodsystem.stationdata import build_station_list

def run():
    """
    Define the function to run the demonstration code
    """

    
    print("---Demonstration 1 --- for task 1D")

    
    stations = build_station_list()
    rivers_set = rivers_with_station(stations)
    rivers_list = list(rivers_set)
    
    
    
    print("The station number is" +" " + str(len(rivers_list)))
    
    print("The first 10 station is" + " " + str(rivers_list[0:10]))
    
    
    
    print("---Demostration 2 --- for task 1E")
    rivers_to_stations_dict = stations_by_river(stations)
    
    # For River Aire
    stations_list = []
    for station in rivers_to_stations_dict["River Aire"]:
        stations_list.append(station.name)
    stations_list.sort()
    print("The station that are located on RIVER AIRE : " + str(stations_list))

    # River Cam
    stations_list = []
    for station in rivers_to_stations_dict["River Cam"]:
        stations_list.append(station.name)
    stations_list.sort()
    print("The station that are located on RIVER CAM : " + str(stations_list))

    # River Thames
    stations_list = []
    for station in rivers_to_stations_dict["River Thames"]:
        stations_list.append(station.name)
    stations_list.sort()
    print("The station that are located on RIVER THAMES : " + str(stations_list))


if __name__ == "__main__":
    print("*****Task1D*****")
    run()