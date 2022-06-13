from sys import displayhook
import endaq
import plotly.express as px
import pandas as pd
import numpy as np
import scipy
from IPython.display import display
from plot import plotit as plot
endaq.plot.utilities.set_theme('endaq_light')



doc = endaq.ide.get_doc('TCB.IDE')

accel = endaq.ide.to_pandas(doc.channels[8].subchannels[0])

plot(accel, 100000)