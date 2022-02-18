
import datetime
import matplotlib
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

#for task2F (incomplete)
def polyfit(dates, levels, p):

    # converts dates into floats, 
    # where the floats are the time in days since the year 0001
    x = matplotlib.dates.date2num(dates)
    y = levels

    # Using shifted x values, find coefficient of best-fit
    # polynomial f(x) of degree p
    p_coeff = np.polyfit(x - x[0], y, p)

    # Convert coefficient into a polynomial that can be evaluated
    poly = np.poly1d(p_coeff)

    return (poly, x[0])