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

from endaqStuff import toNormal, test, retrieveData
from plot import plotit as plot
from scipy.signal import savgol_filter

doc = endaq.ide.get_doc('TCB.IDE')

accel = retrieveData("TCB.IDE")



filter(accel, plotBool = True)
# accel['timestamp'] = accel.index


# filtered = savgol_filter(accel['X (100g)'], 501, 2)






# filteredData = pd.DataFrame(filtered, accel['timestamp'])
# filteredData.columns = ['X (100g)']
# data = accel.assign(Y = filteredData['X (100g)'])
# # data = filteredData.assign(Y  = accel['X (100g)'])

# data = data.rename(columns={'Y':'Y (100g)'})
