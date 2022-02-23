from distutils.command.build import build
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list

def test_stations_level_over_threshold():
    stations = build_station_list()
    tol = 0.8
    tuple_list = stations_level_over_threshold(stations, tol)
    for item in tuple_list:
        assert isinstance(item[1], int)

def test_stations_highest_rel_level():
    stations = build_station_list()
    N = 10
    list1 = stations_highest_rel_level(stations, N)
    assert isinstance(list1, list)