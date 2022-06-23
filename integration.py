import scipy.integrate as it
import numpy as np 
import matplotlib.pyplot as plt
from scipy import integrate
from IPython.display import display
from endaqStuff import toNormal,createDf
import pandas as pd # for data manipulation

def integrateIt(data):
    data = toNormal(data)
    t = data['timestamp'].to_numpy()
    y = data['X (100g)'].to_numpy()

    y_int = integrate.cumtrapz(y, t, initial=0)
    
    final = createDf(t,y_int,'endaq')
    return final


