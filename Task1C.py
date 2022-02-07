
#@ james mcalliste write check function
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

data = build_station_list()
stationDat = stations_within_radius(data,(52.2053, 0.1218),10)
print(stationDat)

#write assert tag
assert(stationDat == ['Cambridge Jesus Lock', 'Bin Brook', "Cambridge Byron's Pool", 'Cambridge Baits Bite', 'Girton', 'Haslingfield Burnt Mill', 'Oakington', 'Stapleford', 'Comberton', 'Dernford', 'Lode'])