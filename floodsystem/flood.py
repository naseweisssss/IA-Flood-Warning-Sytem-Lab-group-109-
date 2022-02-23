from .utils import sorted_by_key

def stations_level_over_threshold(stations, tol):
    """
    This function returns the descending list of (MonitoringStation, relative level) tuples

    """
    list_of_tuples = list()
    for station in stations:
        if station.latest_level != None and station.relative_water_level() != None:
            if station.relative_water_level() > tol:
                list_of_tuples.append((station, station.relative_water_level()))
    return sorted_by_key(list_of_tuples, 1, True)

def stations_highest_rel_level(stations, N):
    """
    This function returns a list of stations which the current relative level is the highest

    """
    list_of_tuples = list()
    for station in stations:
        if station.relative_water_level() != None:
            list_of_tuples.append((station, station.relative_water_level()))
    sorted_list_of_tuples = sorted_by_key(list_of_tuples, 1, True)
    list_of_stations = [t[0] for t in sorted_list_of_tuples]

    return list_of_stations[:N]
