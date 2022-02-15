

def stations_level_over_threshold(stations, tol): # by james mcallister task 2B
    
    returnList = []

    # iterate through list to check against tolerances
    for station in stations:
        if station.relative_water_level() == None:
            break
        elif station.relative_water_level() > tol:
            createTuple = (station,station.relative_water_level())
            returnList.append(createTuple)

    def byLevel(level):#dictates how sorted
        x, lev = level
        return lev

    #sorts list
    sortedList = sorted(returnList, key = byLevel, reverse=True)

    return sortedList



def stations_highest_rel_level(stations, N):
        

    def byLevel(stat):#dictates how sorted
        if stat.relative_water_level() == None: #checks that latest value is real
            return 0
            #returns water value to sort with 
        return stat.relative_water_level()

    #sorts stations by water level
    sortedList = sorted(stations, key = byLevel, reverse=True) 

    #only returns correct number
    return sortedList[:N]    
    
    