from sys import displayhook
import endaq
import plotly.express as px
import pandas as pd
import numpy as np
import scipy
from IPython.display import display
endaq.plot.utilities.set_theme('endaq_light')
import plotly.graph_objs as go
from savgolFilter import filterX, filterZ
import statsmodels.api as sm

from endaqStuff import toNormal, endaqDf, retrieveData, createDf, nearPeak, extractSection
from integration import integrateX, integrateZ
from plot import plotit as plot
from scipy.signal import savgol_filter

filename = "test2.IDE"
plotPoints = 100000

accelX = retrieveData(filename,'x')
accelZ = retrieveData(filename,'z')

filteredDataX = filterX(accelX, plotBool = True, points = plotPoints)

velocityX = integrateX(filteredDataX)



startInput = input("Enter Start Time")
endInput = input("Enter End Time")

accel = extractSection(filename, startInput, endInput)
filteredData = filterX(accel, plotBool = True, points = plotPoints)
filteredDataColumn = filteredData.rename(columns= {'X (100g)': 'Y (100g)'})
velocity = integrateX(filteredData)
accelAndVel = toNormal(velocity.join(filteredDataColumn))
plot(accelAndVel,plotPoints)
