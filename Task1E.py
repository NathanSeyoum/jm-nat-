
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number


def run():
    """Requirements for Task 1B"""

    data = build_station_list()

    rivStatDat = rivers_by_station_number(data, 9)
    print(rivStatDat)
    


if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()