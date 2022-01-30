# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

#line commented out but is from original IA code

#from .utils import sorted_by_key  # noqa
import math

print("working")

def stations_by_distance(stations, p):      #task 1B james mcallister
    
    #the return list
    stationListByDistance = []
    
    def angleBetweenCoordinates(coords): # a function that uses the wikipida formula https://en.m.wikipedia.org/wiki/Great-circle_distance#Formulas
       
        #split tuples
        long_1,lat_1 = p
        long_2, lat_2 = coords

        #simp of math
        multOfSinLat = math.sin(lat_1) * math.sin(lat_2)
        multOfCosLatTimesLong = math.cos(lat_1) * math.cos(lat_2) * math.cos(long_1-long_2)
        diffrenceInAngle = math.acos(multOfSinLat + multOfCosLatTimesLong)

        return diffrenceInAngle

    # itterator for the stations
    for station in stations:
        #takes monetring station class and gets important bits 
        name = station.split('\n')[0].split(':')[1]
        coordinate = station.split('\n')[3].split(':')[1] # these are in WGS84 coordinate system

        #TODO: turn string to tuple coord system / sort names by angleBetweenCoordinates / return list?? maybe string







        
