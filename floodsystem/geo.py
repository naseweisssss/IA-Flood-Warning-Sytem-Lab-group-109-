# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

 
from .station import MonitoringStation
from .stationdata import build_station_list
from .utils import sorted_by_key


def rivers_with_station(stations):
    """This function returns the river that has at least one monitoring station and print the first 10 of these river with sorted order  """
    rivers_with_station  = []
    for item in stations:
        if item.river in rivers_with_station:
            pass
        else:
            rivers_with_station.append(item.river)

    # print(len(rivers_with_station))
    rivers_with_station  = sorted(rivers_with_station)
    # print(rivers_with_station[0:10])

    return rivers_with_station 

# print(rivers_with_station(stations))

def stations_by_river(stations):
    """
    This map the rivers to their respective stations
    """
    rivers_to_stations_dict = dict()
    for station in stations:
        if station.river in rivers_to_stations_dict:
            rivers_to_stations_dict[station.river].append(station)
        else:
            rivers_to_stations_dict[station.river] = []
            rivers_to_stations_dict[station.river].append(station)
    return rivers_to_stations_dict
# rivers_station = stations_by_river(stations)
# print(list(rivers_station.keys())[0])


def rivers_by_station_number(stations, N):
    list_of_rivers = []
    
    rivers_dict = stations_by_river(stations)
    for i in range (len(rivers_dict)):
        list_of_rivers.append((list(rivers_dict.keys())[i], len(list(rivers_dict.keys())[i])) )
    list_of_rivers = sorted_by_key(list_of_rivers,1, reverse = True)
    return list_of_rivers[0:N]
   
    

# print(rivers_by_station_number(stations, 10))