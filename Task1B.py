print(-1)

from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

print(0)
data = build_station_list()
print(1)
stationsDistSorted = stations_by_distance(data, (52.2053, 0.1218))
print(2)

print(stationsDistSorted[:10])
print(stationsDistSorted[-10:])


