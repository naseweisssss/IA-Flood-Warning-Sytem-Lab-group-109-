from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

def run():
    station = build_station_list()
    stations_in_distance = stations_by_distance(station, (52.2053, 0.1218))
    ten_closest = []
    ten_furthest = []

    for station, distance in stations_in_distance[:10] :
        ten_closest.append((station.name, station.town, distance))

    for station, distance in stations_in_distance[-10:] :
        ten_furthest.append((station.name, station.town, distance))

    print("The closest 10 stations is" + " " +str(ten_closest))
    print("The furthest 10 station is " + " " + str(ten_furthest))
if __name__ == "__main__":
    """
    Define the function to run the demonstration code
    """

    
    print("---Demonstration 1 --- for task 1D")
    run()

