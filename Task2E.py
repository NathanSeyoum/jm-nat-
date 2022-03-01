
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_levels
import datetime


def run():

    #builds list of stations
    stations = build_station_list()

    #builds list of the 5 stations at which the water level is highest
    at_risk_stations = stations_highest_rel_level(stations, 5)

    #plots the level data at each of those stationa over the past 10 days 
    for station in at_risk_stations:
        dt = 10
        dates, levels = fetch_measure_levels(station.measure_id,
                                        dt=datetime.timedelta(days=dt))  
        plot_water_levels(station, dates, levels)



if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()