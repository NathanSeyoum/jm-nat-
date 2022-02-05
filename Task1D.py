
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_stations, stations_by_river

def run():
    
    #builds list of stations
    stations = build_station_list()
    
    #first part of task 1D
    sortedSet = sorted(rivers_with_stations(stations))

    #prints number of rivers with at least one monitoring station and prints the first 10
    print("{} stations. First 10 - {} \n".format(len(sortedSet),sortedSet[:10]))

    #second part of task 1D

    dictionary = stations_by_river(stations)

    #prints stations located on the given rivers
    for river in ['River Aire', 'River Cam', 'River Thames']:
            StationsList = dictionary[river]
            StationsList.sort()
            print("For {}: {} \n".format(river, StationsList))


if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System *** \n")
    run()