import pandas as pd # for data manipulation
import numpy as np # for data manipulation
from sklearn.linear_model import LinearRegression # to build a LR model for comparison
import plotly.graph_objects as go # for data visualization
import plotly.express as px # for data visualization 
import statsmodels.api as sm # to build a LOWESS model
from scipy.interpolate import interp1d # for interpolation of new data points

def filter(df):
    fig = px.scatter(df, df[df.columns[0]], df[df.columns[1]], 
                 opacity=0.8, color_discrete_sequence=['black'])

    # Change chart background color
    fig.update_layout(dict(plot_bgcolor = 'white'))

    # Update axes lines
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey', 
                    zeroline=True, zerolinewidth=1, zerolinecolor='lightgrey', 
                    showline=True, linewidth=1, linecolor='black')

    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey', 
                    zeroline=True, zerolinewidth=1, zerolinecolor='lightgrey', 
                    showline=True, linewidth=1, linecolor='black')

    # Set figure title
    fig.update_layout(title=dict(text="House Price Based on Distance from the Nearest MRT", 
                                font=dict(color='black')))

    # Update marker size
    fig.update_traces(marker=dict(size=3))

    fig.show()
    # ------- Select variables -------
    # x values for Linear Regression
    X=df['X3 distance to the nearest MRT station'].values.reshape(-1,1) # Note, we need X to be a 2D array, hence reshape
    # x values for LOWESS
    x=df['X3 distance to the nearest MRT station'].values 
    # y values for both
    y=df['Y house price of unit area'].values


    # ------- Linear Regression -------
    # Define and fit the model
    model1 = LinearRegression()
    LR = model1.fit(X, y)

    # Predict a few points with Linear Regression model for the grpah
    # Create 20 evenly spaced points from smallest X to largest X
    x_range = np.linspace(X.min(), X.max(), 20) 
    # Predict y values for our set of X values
    y_range = model1.predict(x_range.reshape(-1, 1))


    # ------- LOWESS -------
    # Generate y_hat values using lowess, try a couple values for hyperparameters
    y_hat1 = lowess(y, x) # note, default frac=2/3
    y_hat2 = lowess(y, x, frac=1/5)

    # Create a scatter plot
    fig = px.scatter(df, x=df['X3 distance to the nearest MRT station'], y=df['Y house price of unit area'], 
                    opacity=0.8, color_discrete_sequence=['black'])

    # Add the prediction line
    fig.add_traces(go.Scatter(x=x_range, y=y_range, name='Linear Regression', line=dict(color='limegreen')))
    fig.add_traces(go.Scatter(x=y_hat1[:,0], y=y_hat1[:,1], name='LOWESS, frac=2/3', line=dict(color='red')))
    fig.add_traces(go.Scatter(x=y_hat2[:,0], y=y_hat2[:,1], name='LOWESS, frac=1/5', line=dict(color='orange')))

    # Change chart background color
    fig.update_layout(dict(plot_bgcolor = 'white'))

    # Update axes lines
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey', 
                    zeroline=True, zerolinewidth=1, zerolinecolor='lightgrey', 
                    showline=True, linewidth=1, linecolor='black')

    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey', 
                    zeroline=True, zerolinewidth=1, zerolinecolor='lightgrey', 
                    showline=True, linewidth=1, linecolor='black')

    # Set figure title
    fig.update_layout(title=dict(text="House Price Based on Distance from the Nearest MRT with Model Predictions", 
                                font=dict(color='black')))

    # Update marker size
    fig.update_traces(marker=dict(size=3))

    fig.show()