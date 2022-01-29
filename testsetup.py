from distutils.command.build import build
from floodsystem.geo import rivers_by_station_number, stations_by_river
from floodsystem.stationdata import build_station_list
stations = build_station_list()
rivers_station = stations_by_river(stations)
print(list(rivers_station.keys())[0])