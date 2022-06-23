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
    temp = getIndexes(data,maxVal)
    display(temp)

def getIndexes(dfObj, value):
    ''' Get index positions of value in dataframe i.e. dfObj.'''
    listOfPos = list()
    # Get bool dataframe with True at positions where the given value exists
    result = dfObj.isin([value])
    # Get list of columns that contains the value
    seriesObj = result.any()
    columnNames = list(seriesObj[seriesObj == True].index)
    # Iterate over list of columns and fetch the rows indexes where value exists
    for col in columnNames:
        rows = list(result[col][result[col] == True].index)
        for row in rows:
            listOfPos.append((row, col))
    # Return a list of tuples indicating the positions of value in the dataframe
    return listOfPos