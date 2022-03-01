
from floodsystem.stationdata import build_station_list
from floodsystem.geo import *

def test_rivers_with_stations():
    """This checks that all the rivers are in the set"""
    
    stations = build_station_list()
    station_rivers = rivers_with_stations(stations)

    count = 0
    for station in stations:
        if station.river not in station_rivers:
            count += 1
    assert(count == 0)


def test_stations_by_distance():

    data = build_station_list()
    stationsDistSorted = stations_by_distance(data, (52.2053, 0.1218))

    #checks closest station
    
    assert stationsDistSorted[:10] == [('Cambridge Jesus Lock', 0.840237595667494), ('Bin Brook', 2.502277543239629), ("Cambridge Byron's Pool", 4.07204948005424), ('Cambridge Baits Bite', 5.115596582531859), ('Girton', 5.227077565748483), ('Haslingfield Burnt Mill', 7.0443978959918025), ('Oakington', 7.12825901765745), ('Stapleford', 7.265704342799649), ('Comberton', 7.735085060177142), ('Dernford', 7.993872393303291)]
    #checks furthest station
    assert stationsDistSorted[-10:] == [('Boscadjack', 440.00325604140033), ('Gwithian', 442.0555261735786), ('Helston County Bridge', 443.3788620846717), ('Loe Pool', 445.0724593420217), ('Relubbus', 448.6500629265487), ('St Erth', 449.0347773512542), ('St Ives Consols Farm', 450.07409071624505), ('Penzance Tesco', 456.38638836619003), ('Penzance Alverton', 458.57727568406375), ('Penberth', 467.53431870130544)]


def test_stations_within_radius():
    # Build list of stations
    data = build_station_list()
    stationDat = stations_within_radius(data,(52.2053, 0.1218),10)

    assert(stationDat == ['Cambridge Jesus Lock', 'Bin Brook', "Cambridge Byron's Pool", 'Cambridge Baits Bite', 'Girton', 'Haslingfield Burnt Mill', 'Oakington', 'Stapleford', 'Comberton', 'Dernford', 'Lode'])

"""
def test_rivers_by_station_number():

    data = build_station_list()
    rivStatDat = rivers_by_station_number(data, 9)
    assert rivStatDat == [('River Thames', 54), ('River Avon', 31), ('River Great Ouse', 30), ('River Derwent', 25), ('River Aire', 24), ('River Calder', 23), ('River Severn', 21), ('River Stour', 21), ('River Ouse', 18)], 'code doesnt quite work'
"""
