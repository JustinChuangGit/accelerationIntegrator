from tkinter import TRUE
import pandas as pd # for data manipulation
import numpy as np # for data manipulation
from plot import plotit as plot
from scipy.signal import savgol_filter
from IPython.display import display

def filterX(data, plotBool=False, points = 100000):
    
    data['timestamp'] = data.index
    filtered = savgol_filter(data['X (100g)'], 1301, 3)
    filteredData = pd.DataFrame(filtered, data['timestamp'])
    filteredData.columns = ['X (100g)']
    display(filteredData)
    data = data.assign(Y = filteredData['X (100g)'])
    # data = filteredData.assign(Y  = accel['X (100g)'])
    data = data.rename(columns={'Y':'Y (100g)'})

    if plotBool == TRUE:
        plot(data,points)
    return filteredData


def filterZ(data, plotBool=False, points = 100000):
    
    data['timestamp'] = data.index
    filtered = savgol_filter(data['Z (100g)'], 1301, 3)
    filteredData = pd.DataFrame(filtered, data['timestamp'])
    filteredData.columns = ['Z (100g)']
    display(filteredData)
    data = data.assign(Y = filteredData['Z (100g)'])
    # data = filteredData.assign(Y  = accel['X (100g)'])
    data = data.rename(columns={'Y':'Y (100g)'})

    if plotBool == TRUE:
        plot(data,points)
    return filteredData
