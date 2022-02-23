import numpy as np
import datetime

def polyfit (dates, levels, p):
    """
    The function should return a tuple of (i) the polynomial object and (ii) any shift of the time (date) axis
    """

    first_time = dates[0]
    float_date = list()
    for d in dates:
        float_date.append((d- first_time).total_seconds())
    return np.polyfit(float_date, levels, p)