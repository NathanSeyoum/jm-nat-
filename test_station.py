# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town


def test_typical_range_consistent():
    """tests the method for a station with inconsistent data"""
    
    # Create a station with inconsistent data for typical low/high ranges
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (0, 0)
    trange = (1, -1)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    
    assert(s.typical_range_consistent() == False)


def test_inconsistent_typical_range_stations():
    """tests the function output for stations with consistent and inconsistent data"""

    stations = []

    # Creates a station with inconsistent data for typical low/high ranges
    a = MonitoringStation("s_id", "m_id", "label", "coord", (1,-1), "river", "town")
    
    # Creates a station with consistent data for typical low/high ranges
    b = MonitoringStation("s_id", "m_id", "label", "coord", (0,1), "river", "town")
    
    stations.append(a)
    stations.append(b)
    assert(a in inconsistent_typical_range_stations(stations))
    assert(b not in inconsistent_typical_range_stations(stations))

