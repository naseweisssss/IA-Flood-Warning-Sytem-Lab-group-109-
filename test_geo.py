from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station, stations_by_river, rivers_by_station_number, stations_by_distance
from floodsystem.station import MonitoringStation

def test_rivers_with_station():
    stations = build_station_list()
    rivers_set = rivers_with_station(stations)

    assert len(rivers_set) > 0
    assert isinstance(rivers_set, list)
    


def test_stations_by_river():
    stations = build_station_list()
    rivers_to_stations_dict = stations_by_river(stations)

    assert len(rivers_to_stations_dict) > 0
    assert isinstance(rivers_to_stations_dict, dict)
    


def test_rivers_by_station_number():
   
    N = 39
    stations = build_station_list()
    list_of_rivers = rivers_by_station_number(stations, N)

    assert isinstance(list_of_rivers, list)
    for item in list_of_rivers:
        assert isinstance(item, tuple)
        assert len(item)==2
        assert isinstance(item[0], str)
        assert isinstance(item[1], int)
    
def test_stations_by_distance():
    stations = build_station_list()
    station_testing = stations_by_distance(stations, (52.2053, 0.1218))
    assert isinstance(station_testing, list)
    for item in station_testing:
        assert isinstance(item, tuple)
        assert isinstance(item[0], MonitoringStation)
        assert isinstance(item[1], float)