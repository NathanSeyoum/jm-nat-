

assert False, 'elp'

from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number

data = build_station_list()

rivStatDat = rivers_by_station_number(data, 9)
print(rivStatDat)

# write assert tags to check 
assert rivStatDat == [('Thames', 55), ('River Great Ouse', 31), ('River Avon', 30), ('River Calder', 24), ('River Aire', 21), ('River Severn', 20), ('River Derwent', 18), ('River Stour', 16), ('River Wharfe', 14), ('River Trent', 14), ('Witham', 14)]
