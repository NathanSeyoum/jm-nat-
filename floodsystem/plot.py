
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from .analysis import polyfit

#for task 2E 
def plot_water_levels(station, dates, levels):
    """displays a plot of the water level data against time for a station"""

    # Plot
    plt.plot(dates, levels)

    #adds plot lines for typical low and high levels
    levelRange = station.typical_range
    plt.axhline(y=levelRange[0])
    plt.axhline(y=levelRange[1])


    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()


#for task 2F
def plot_water_level_with_fit(station, dates, levels, p):
    """plots water level data and best fit polynomial"""

    poly, d0 = polyfit(dates, levels, p)

    #format data
    dates = matplotlib.dates.date2num(dates) - d0    
    x1 = np.linspace(dates[0],dates[-1],30)

    #plot 
    plt.plot(dates, levels, '.')
    plt.plot(x1, poly(x1))
    
    #adds plot for typical high/low range
    plt.plot(x1, np.linspace(station.typical_range[0],station.typical_range[0],30),"-r")
    plt.plot(x1, np.linspace(station.typical_range[1],station.typical_range[1],30),"-r")

    #add titles and labels
    plt.xlabel("days ago")
    plt.ylabel("water level(m)")
    plt.title(station.name)

    plt.show()