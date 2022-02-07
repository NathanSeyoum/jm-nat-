from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number

data = build_station_list()

print(rivers_by_station_number(data, 9))

# write assert tags to check 
