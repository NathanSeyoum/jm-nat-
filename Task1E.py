""""

from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number

data = build_station_list()

rivStatDat = rivers_by_station_number(data, 9)
print(rivStatDat)

# write assert tags to check 
assert rivStatDat == [('River Thames', 55), ('River Avon', 31), ('River Great Ouse', 30), ('River Derwent', 25), ('River Aire', 24), ('River Calder', 23), ('River Severn', 21), ('River Stour', 21), ('River Ouse', 18)]
"""
from haversine import haversine, Unit

lyon = (45.7597, 4.8422)
paris = (48.8567, 2.3508)

print(haversine(lyon, paris))
