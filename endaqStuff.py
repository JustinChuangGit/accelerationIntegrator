import pandas as pd # for data manipulation
import numpy as np # for data manipulation
import endaq

from IPython.display import display


def createDf(x, y, type = 'normal'):
    d = {'X (100g)': y, 'timestamp' :x}
    df = pd.DataFrame(data=d)
    if type == 'endaq':
        return(endaqDf(df))
    elif type == 'normal':
        return df

def endaqDf(data):
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
    averageOffset = normalData.iloc[0:5000,[0]].to_numpy()
    averageOffset = np.median(averageOffset.T)
    return data-averageOffset

def nearPeak(data, plusMinus):
    maxVal = abs(data['X (100g)']).max()
    temp = data.index[abs(data['X (100g)'])==maxVal].tolist()
    display(temp)

