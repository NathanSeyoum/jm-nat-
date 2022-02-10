# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

#line commented out but is from original IA code

from .utils import sorted_by_key  # noqa
import math
from numpy import True_
from haversine import haversine, Unit

def stations_by_distance(stations, p): #for task1B
    """returns a list of (station, distance) tuples where distance is the station's distance from p"""
    alist = []
    for station in stations:
        dist = haversine(station.coord, p, unit=Unit.KILOMETERS)
        alist.append((station.name, dist))
    return sorted_by_key(alist, 1)

#task 1C @ james mcallister
def stations_within_radius(stations, centre, r):
    """returns a list of all the stations within a radius r from the centre"""
    withinRadius = []

    alist = stations_by_distance(stations, centre)
    for station in alist:
        if station[1] <= r:
            withinRadius.append(station[0])

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

    def firstEl(el):# this func has been checked but works for the sorting function
        
        return el[1]

    stationListByCount = sorted(listOfStations, key = firstEl, reverse=True)

    stationTuple = []
    for item in stationListByCount:
        thing = (item[0],item[1]) 
        stationTuple.append(thing)

    return stationTuple[:N]



