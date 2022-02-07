# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

#line commented out but is from original IA code

#from .utils import sorted_by_key  # noqa
import math
from numpy import True_
from haversine import haversine, Unit



def stations_by_distance(stations, p):      #task 1B james mcallister
    # returns list of names by points 
    # needs testing


    #the return list
    stationsandDistances = []
    stationListByDistance = []
    
    def angleBetweenCoordinates(coords): # a function that uses the wikipida formula https://en.m.wikipedia.org/wiki/Great-circle_distance#Formulas
       
       '''
        #split tuples
        long_1,lat_1 = p
        long_2, lat_2 = coords

        #simplification of of math
        
        # haversine formula 
        dlon = long_2 - long_1 
        dlat = lat_2 - lat_1 
        a = math.sin(dlat/2)**2 + math.cos(lat_1) * math.cos(lat_2) * math.sin(dlon/2)**2
        c = 2 * math.asin(math.sqrt(a)) 
        r = 6371
        #to get actual angle multiply by earth radius
        '''
        distance = haversine(coords, p, unit=Unit.KILOMETERS)
        
        # returns a distance now
        return distance 

    # itterator for the stations
    for station in stations:
        #takes monetring station class and gets important bits 
        name = station.name 
        town = station.town
        coordinateRaw = station.coord   # these are in WGS84 coordinate system
        coordinates = station.coord
        output = (name,town,angleBetweenCoordinates(coordinates))
        stationsandDistances.append(output) 

    def firstEl(el):# this func has been checked but works for the sorting function
        return el[2]

    stationListByDistance = sorted(stationsandDistances, key = firstEl)
    
    listofNamesByDistance = [] # 
    for n in stationListByDistance:
        listofNamesByDistance.append(n[0])

    return stationListByDistance #TODO: @james mcallister put in distance away instead of angle and put in and town name 


#task 1C @ james mcallister
def stations_within_radius(stations, centre, r):
    # fetches data by distances
    withingRadius = stations_by_distance(stations, centre)
    withinRadius = []
        
    for monitor in withingRadius:
        name, town, dist = monitor
        if dist <= r:
            withinRadius.append(name)

    return withinRadius


#for task 1D by Nathan
def rivers_with_stations(stations):
#returns a set of the names of rivers with a monintoring station, 
#given a list of station objects
  
   #creates an empty set
    station_rivers = set()
    
    #checks for ring station and adds them to the set
    for station in stations:       
        if station.river != None:
            station_rivers.add(station.river)
    
    return station_rivers

#also for task 1D by Nathan
def stations_by_river(stations):
#returns a dictionary that maos river names to a list of stations monitoring them

    #gets set of river names
    stationrivers = rivers_with_stations(stations)
    
    dictionary = {}

    #for each river, creates an empty list
    for river in stationrivers: 
        stationslist = []

        #finds the stations monitoring the river and add them to the list
        for station in stations:
            if station.river == river:
                stationslist.append(station.name)

        #adds the river(key) and list(value) pair to the dictionary
        dictionary[river] = stationslist
    
    return dictionary

#task 1E @james mcallister
def rivers_by_station_number(stations, N):
    listOfStations = []
    
    def searchlist(stationName):
        # searches list
        variableAdded = False
        for items in listOfStations:
            if items[0] == stationName:
                items[1] += 1
                variableAdded = True
                break
        
        #adds new station
        if variableAdded == False:
            thing = [stationName,1]
            listOfStations.append(thing)

        
            
            
            
    for station in stations:
        # get river name 
        river = station.river
        # searches list for name
        searchlist(river)
        
    # sorting
    #listOfStations.sort()

    def firstEl(el):# this func has been checked but works for the sorting function
        
        return el[1]

    stationListByCount = sorted(listOfStations, key = firstEl, reverse=True)

    stationTuple = []
    for item in stationListByCount:
        thing = (item[0],item[1]) 
        stationTuple.append(thing)

    return stationTuple[:N]




