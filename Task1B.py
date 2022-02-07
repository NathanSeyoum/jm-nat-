#@james mcallister test for the geo station_by_distance function
#test for task 1B 

#probable issues I am missing a few modules that are needed in datafetcher.py

#import dateutil.parser, import requests

from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

data = build_station_list()
stationsDistSorted = stations_by_distance(data, (52.2053, 0.1218))


print(stationsDistSorted[:10])
print(stationsDistSorted[-10:])

#write assert tag



