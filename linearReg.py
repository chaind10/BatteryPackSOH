import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import preprocessing as pp

x_data = pp.dataset.drop(columns=['SOH'])
x_data = np.array(x_data)

y_data = pp.dataset['SOH']
y_data = np.array(y_data)

plt.scatter(x_data, y_data)

plt.xlabel("Data")
plt.ylabel("SOH")
plt.title("Linear Regression")