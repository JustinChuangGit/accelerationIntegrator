from sys import displayhook
import endaq
import plotly.express as px
import pandas as pd
import numpy as np
import scipy
from IPython.display import display
from plot import plotit as plot
endaq.plot.utilities.set_theme('endaq_light')
import plotly.graph_objs as go


doc = endaq.ide.get_doc('TCB.IDE')

accel = endaq.ide.to_pandas(doc.channels[8].subchannels[0], time_mode='seconds')

plot(accel, 100000)


psd = endaq.calc.psd.welch(accel, bin_width=1)
psd['Resultant'] = psd.sum(axis=1)

psd_labels = dict(
    xaxis_title_text='Frequency (Hz)',
    yaxis_title_text='Acceleration (g^2/Hz)',
    legend_title_text='',
    xaxis_type='log',
    yaxis_type='log',
)

fig = px.line(psd)
fig.update_layout(
    psd_labels,
    title_text='Power Spectral Density',
)

oct_psd = endaq.calc.psd.to_octave(psd, fstart=4, octave_bins=3)
oct_psd.head()

for c in oct_psd.columns:
  fig.add_trace(go.Scattergl(
      x=oct_psd.index,
      y=oct_psd[c],
      name=c+' Octave',
      line_width=6,
      line_dash='dash'
  ))

fig.show()

data_df, fig = endaq.plot.octave_spectrogram(accel, window=0.15, bins_per_octave=3)
fig.show()