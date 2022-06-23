import pandas as pd # for data manipulation
import numpy as np # for data manipulation

def test(data):
    data = data.set_index('timestamp')
    return data

def toNormal(data):
    data['timestamp'] = data.index
    data = data.reset_index(drop=True)
    return data

