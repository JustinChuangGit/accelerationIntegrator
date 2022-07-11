import scipy.integrate as it
import numpy as np 
import matplotlib.pyplot as plt
from scipy import integrate
from IPython.display import display
from endaqStuff import toNormal,createDf
import pandas as pd # for data manipulation

def integrateX(data):
    data = toNormal(data)
    t = data['timestamp'].to_numpy()
    y = data['X (100g)'].to_numpy()

    y_int = (integrate.cumtrapz(y, t, initial=0))*3.6
    
    final = createDf(t,y_int,'endaq')
    return final

def integrateZ(data):
    data = toNormal(data)
    t = data['timestamp'].to_numpy()
    y = data['Z (100g)'].to_numpy()

    y_int = (integrate.cumtrapz(y, t, initial=0))*3.6
    
    final = createDf(t,y_int,'endaq')
    return final


