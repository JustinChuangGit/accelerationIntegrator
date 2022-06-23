import pandas as pd # for data manipulation
import numpy as np # for data manipulation
import endaq

from IPython.display import display


def test(data):
    data = data.set_index('timestamp')
    return data

def toNormal(data):
    data['timestamp'] = data.index
    data = data.reset_index(drop=True)
    return data

def retrieveData(filename):
    doc = endaq.ide.get_doc('TCB.IDE')
    data = endaq.ide.to_pandas(doc.channels[8].subchannels[0], time_mode='seconds')

    normalData = toNormal(data)
    averageOffset = normalData.iloc[0:1000,"X (100g)"].mean()
    print(averageOffset)

    return data
