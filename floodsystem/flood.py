

def stations_level_over_threshold(stations, tol): # by james mcallister task 2B
    
    returnList = []

    # iterate through list to check against tolerances
    for station in stations:
        if station.latest_level == None:
            break
        elif station.latest_level > tol:
            createTuple = (station,station.latest_level)
            returnList.append(createTuple)

    def byLevel(level):#dictates how sorted
        x, lev = level
        return lev

    #sorts list
    sortedList = sorted(returnList, key = byLevel, reverse=True)

    return sortedList

