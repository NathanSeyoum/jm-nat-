#test for task 2B

from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels

def run():
    """Requirements for Task 2B"""

    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)
    stationOne = stations[0]
    print(stationOne.relative_water_level())
   


if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()
