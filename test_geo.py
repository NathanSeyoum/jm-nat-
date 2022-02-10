
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_stations


def test_rivers_with_stations():
    """This checks that all the rivers are in the set"""
    
    stations = build_station_list()
    station_rivers = rivers_with_stations(stations)

    count = 0
    for station in stations:
        if station.river not in station_rivers:
            count += 1
    assert(count == 0)

