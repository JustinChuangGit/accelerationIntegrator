from sys import displayhook
import endaq

endaq.plot.utilities.set_theme('endaq_light')

import plotly.express as px
import pandas as pd
import numpy as np
import scipy
from IPython.display import display



accel_time_labels = dict(
    xaxis_title_text='',
    yaxis_title_text='Acceleration (g)',
    legend_title_text=''
)

velocity_labels = dict(
    xaxis_title_text='Time(s)',
    yaxis_title_text='Velocity (km/h)',
    legend_title_text=''
)


def plotit(data,points):

    if len(data.columns) > 1:
        del data['timestamp']


    fig = endaq.plot.plots.rolling_min_max_envelope(
    data,
    desired_num_points=points,
    plot_as_bars=True,
    opacity=0.7
    )

    fig.update_layout(
        velocity_labels,
        title_text='Beach Axis Velocity Plot',
    )
    fig.show()
