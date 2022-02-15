from re import S
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import update_water_levels

def run():
    """Requirements for Task 2C"""

    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)

    topStations = stations_highest_rel_level(stations,10)

    for items in topStations: #formats print
        
        print(items.name,items.relative_water_level())

        #Letcombe Bassett seems slightly problimatic as relative level is 600+

    


if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()