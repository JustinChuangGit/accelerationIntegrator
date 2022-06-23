from tkinter import TRUE
import pandas as pd # for data manipulation
import numpy as np # for data manipulation
from plot import plotit as plot
from scipy.signal import savgol_filter
from IPython.display import display

def filter(data, plotBool=False, desiredPoints = 100000):
    
    data['timestamp'] = data.index
    filtered = savgol_filter(data['X (100g)'], 1001, 3)
    filteredData = pd.DataFrame(filtered, data['timestamp'])
    filteredData.columns = ['X (100g)']
    display(filteredData)
    data = data.assign(Y = filteredData['X (100g)'])
    # data = filteredData.assign(Y  = accel['X (100g)'])
    data = data.rename(columns={'Y':'Y (100g)'})
    display(data)

    if plotBool == TRUE:
        plot(data,desiredPoints)
    return filteredData
