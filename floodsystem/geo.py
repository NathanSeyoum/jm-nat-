# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

#line commented out but is from original IA code

#from .utils import sorted_by_key  # noqa
import math



def stations_by_distance(stations, p):      #task 1B james mcallister
    # returns list of names by points 
    # needs testing


    #the return list
    stationsandDistances = []
    stationListByDistance = []
    
    def angleBetweenCoordinates(coords): # a function that uses the wikipida formula https://en.m.wikipedia.org/wiki/Great-circle_distance#Formulas
       
        #split tuples
        long_1,lat_1 = p
        long_2, lat_2 = coords

        #simplification of of math
        multOfSinLat = math.sin(lat_1) * math.sin(lat_2)
        multOfCosLatTimesLong = math.cos(lat_1) * math.cos(lat_2) * math.cos(long_1-long_2)
        diffrenceInAngle = math.acos(multOfSinLat + multOfCosLatTimesLong)

        #to get actual angle multiply by earth radius
        
        return diffrenceInAngle

    # itterator for the stations
    for station in stations:
        #takes monetring station class and gets important bits 
        name = station.split('\n')[0].split(':')[1]
        coordinateRaw = station.split('\n')[3].split(':')[1].split(",") # these are in WGS84 coordinate system
        coordinatesTrimmed = coordinateRaw[1:-1] # spliting up the steps to reduce complexity
        coordinates = tuple(map(float, coordinatesTrimmed.split(",")))
        stationsandDistances.append(name,angleBetweenCoordinates(coordinates)) 

    def firstEl(el):# this func has been checked but works for the sorting function
        return el[0]

    stationListByDistance = sorted(stationsandDistances, key = firstEl)
    
    listofNamesByDistance = [] # 
    for n in stationListByDistance:
        listofNamesByDistance.append(n[0])

    return stationListByDistance #TODO: @james mcallister put in distance away instead of angle and put in and town name 


#task 1C
def stations_within_radius(stations, centre, r):
    withingRadius = stations_by_distance(stations, centre)
    earthRadius = 6378.137
    withinRadius = []
        
    for monstat in withingRadius:
        name,ang = monstat
        dist = ang*earthRadius
        if dist <= r:
            withinRadius.append(name)

    return withinRadius


#for task 1D by Nathan
def rivers_with_stations(stations):
#returns a set of the names of rivers with a monintoring station, 
#given a list of station objects
  
   #creates an empty set
    station_rivers = set()
    
    #checks for rivers with a monitoring station and adds them to the set
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

