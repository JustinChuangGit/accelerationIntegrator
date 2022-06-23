from sys import displayhook
import endaq
import plotly.express as px
import pandas as pd
import numpy as np
import scipy
from IPython.display import display
endaq.plot.utilities.set_theme('endaq_light')
import plotly.graph_objs as go
from savgolFilter import filter
import statsmodels.api as sm

from endaqStuff import toNormal, endaqDf, retrieveData, createDf, nearPeak
from integration import integrateIt
from plot import plotit as plot
from scipy.signal import savgol_filter

doc = endaq.ide.get_doc('TCB.IDE')

accel = retrieveData("TCB.IDE")

nearPeak(accel, 1.0)

#filteredData = filter(accel, plotBool = True)

# velocity = integrateIt(filteredData)#




# plot(velocity,100000)
