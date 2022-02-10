from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number



# write assert tags to check 
#assert rivStatDat == [('Thames', 55), ('River Great Ouse', 31), ('River Avon', 30), ('River Calder', 24), ('River Aire', 21), ('River Severn', 20), ('River Derwent', 18), ('River Stour', 16), ('River Wharfe', 14), ('River Trent', 14), ('Witham', 14)], 'code doesnt quite work'

def run():
    """Requirements for Task 1B"""

    data = build_station_list()

    rivStatDat = rivers_by_station_number(data, 9)
    print(rivStatDat)
    


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
    