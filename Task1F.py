
from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list

def run():
    #builds list of stations
    stations = build_station_list()

    #builds list of stations with inconsistent data
    InconsistentStationData = inconsistent_typical_range_stations(stations)

    #builds list of the names of stations with inconsistent data
    InconsistentStations = []

    for station in InconsistentStationData:
        InconsistentStations.append(station.name)

    InconsistentStations.sort()
    print(InconsistentStations)


if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System *** \n")
    run()