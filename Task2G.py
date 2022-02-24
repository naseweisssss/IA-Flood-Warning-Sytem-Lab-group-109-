import datetime
import numpy as np
import matplotlib.pyplot as plt
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.flood import stations_highest_rel_level
from statistics import mean


# A reasonable time to notice a flood would be around 5 days
day_to_detect = 5
stations = build_station_list()
stations_copy = list()
town_at_severe_risk = list()
town_at_high_risk = list()
town_at_moderate_risk = list()
town_at_low_risk = list()

# finding list of stations that has the highest risk
update_water_levels(stations)
station_at_severe_risk = stations_highest_rel_level(stations, len(stations)//4)
for item in station_at_severe_risk:
    town_at_severe_risk.append(item.town)

station_at_high_risk = stations_highest_rel_level(stations, len(stations)//2)
for item in station_at_high_risk:
    if item not in station_at_severe_risk:
        town_at_high_risk.append(item.town)

station_at_moderate_risk = stations_highest_rel_level(stations, round(len(stations)*0.75))
for item in station_at_moderate_risk:
    if item not in station_at_high_risk and station_at_severe_risk:
        town_at_moderate_risk.append(item.town)

if item not in station_at_high_risk and station_at_moderate_risk and station_at_severe_risk:
    town_at_low_risk.append(item.town)
# for item in station_at_severe_risk:
#     town_at_severe_risk.append(item.town)
print("The town at severe risk are")
print(town_at_severe_risk)
print("The town at high risk are")
print(town_at_high_risk)
print("The town at moderate risk are")
print(town_at_moderate_risk)
print("The town at low risk are")
print(town_at_low_risk)
# print(town_at_severe_risk)

    
    
    
    
    # for x1, x2 in zip(levels[:-1], levels[1:]):
    #  try:
    #     pct = (x2 - x1) * 100 / x1
    #  except ZeroDivisionError:
    #     pct = None
    #  changes.append(pct)
    
    # mean_of_changes = mean(changes)
    
    
    
    # for date, level in zip(dates, levels):
    #     print(date, level)
    
        
    
    # perc=[0.0]+list(np.round((level_with_value[1:]/level_with_value[:-1]-1)*100,decimals=1))

    # even_value = np.linspace(start =0 , stop = 100, num = len(perc))
    # mean_of_change = np.mean(perc)

    
        

