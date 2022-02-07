# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

 
from .station import MonitoringStation
from .stationdata import build_station_list
from .utils import sorted_by_key
from haversine import haversine


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
    """
    This function return the N rivers with greatest number of monitoring stations
    """
    rivers_to_stations_dict = stations_by_river(stations)
    rivers_tuples = []

    for key, listofstations in rivers_to_stations_dict.items():
        rivers_tuples.append((key, len(listofstations)))
    rivers_tuples.sort(key=lambda t : t[1], reverse=True)

    # Check if there are more rivers with the same number of stations as the N th entry
    k = N-1
    while True:
        if rivers_tuples[k][1] == rivers_tuples[k+1][1]:
            k+=1
        else:
            break
    return rivers_tuples[:k+1]
   
    
def stations_by_distance (stations, p):
    """
    This function returns a sorted list of (station, distance) tuple
    """

    stations_and_distance = []
    sorted_list = []
    for item in stations:
        distance_calc = haversine(item.coord, p)
        stations_and_distance.append((item, distance_calc))
    sorted_list  = sorted_by_key (stations_and_distance, 1)

    return sorted_list 
def stations_within_radius(stations, centre, r):
    """
    This function return the station within the required radius
    """
    stations_within_radius = []
    stations_and_distance = stations_by_distance(stations, centre)
    for station, distance in stations_and_distance:
        if distance < r:
            stations_within_radius.append(station)
    return stations_within_radius
   

