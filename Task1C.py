
#@ james mcalliste write check function
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

data = build_station_list()
stationDat = stations_within_radius(data,(52.2053, 0.1218))
print(stationDat)

#write assert tag
assert(stationDat == ['Bin Brook', 'Cambridge Baits Bite', "Cambridge Byron's Pool",
 'Cambridge Jesus Lock', 'Comberton', 'Dernford', 'Girton',
 'Haslingfield Burnt Mill', 'Lode', 'Oakington', 'Stapleford'])