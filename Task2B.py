#test for task 2B

from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.flood import stations_level_over_threshold

def run():
    """Requirements for Task 2B"""

    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)
    
    ofendingStations = stations_level_over_threshold(stations, 0.8)

    for items in ofendingStations: #takes offending stations and orders them into the correct locations
        x,y = items
        print(x.name,y)
   


if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()


