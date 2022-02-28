# task 2G analysing the most at risk places
from re import S
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import update_water_levels
import datetime


def risingTimeline(station):
    num = 4
    collection = []
    for dt in range(num): 
        dt = dt +1
        
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))  
        daylength = (len(levels) / dt)
    
        sum = 0
        for points in levels:
            sum += points
        length = len(levels)
        if length == 0: #unsure fix
            length = 1
        sum = sum / length
        collection.append(sum)
    return collection

def isRising(station): # an abritarty justification to see if river levels are on adverage rising
    score = 0 
    ar = risingTimeline(station)
    
    if ar[3] > ar[0]:
        return 0
    if ar[0] > ar[1]: 
        score += 1
    if ar[1] > ar[2] and ar[0] > ar[1]:
        score += 1
    if ar[1] > ar[2] and ar[0] > ar[1] and ar[2] > ar[3]:
        score += 1
    return score


def riskAnalysis(stations):
    update_water_levels(stations)
    at_risk_stations = stations_highest_rel_level(stations, len(stations))  
    stationDanger = []
    

    for stat in at_risk_stations:
        height = stat.relative_water_level()
        if height != None:
        
            name = stat.name
            if height < 1:
                thingy = (name,"low")
                stationDanger.append(thingy)
            elif height >= 1 and height < 2: #randomly chosen point to see if at risk of flooding
                if isRising(stat) == 0: # checks how many days the water has beeen rising
                    thingy = (name,"low")
                    stationDanger.append(thingy)
                elif isRising(stat) > 3:
                    thingy = (name,"servere")
                    stationDanger.append(thingy)
                elif isRising(stat) > 2:
                    thingy = (name,"High")
                    stationDanger.append(thingy)
                elif isRising(stat) > 1:
                    thingy = (name,"moderate")
                    stationDanger.append(thingy) 
            else: # everything else bad
                thingy = (name,"servere")
                stationDanger.append(thingy)
        
    return stationDanger



'''
how this works 
-station data goes in
-checked to see relativly how high the river is
-if its been rising consistantly the flood risk goes up
-if the flood height is above 2 its flooded
'''


def run():
    """Requirements for Task 2G"""

    stations = build_station_list()
    print(riskAnalysis(stations))


if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()

