
#@ james mcalliste write check function
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius


def run():
    """Requirements for Task 1C"""

    # Build list of stations
    data = build_station_list()
    stationDat = stations_within_radius(data,(52.2053, 0.1218),10)


    # Display data :
    print(stationDat.sort())


if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()
