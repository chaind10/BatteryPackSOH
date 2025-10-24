import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import matplotlib.pyplot as plt
import preprocessing as pp

x_data = pp.dataset.drop(columns=['SOH'])
x_data = np.array(x_data)

y_data = pp.dataset['SOH']
y_data = np.array(y_data)

#x_train and y_train are arrays used to train the model
#x_test and y_test are arrays used to test the model
#20% of the data for testing and 8% for training
X_train, X_test, y_train, y_test = train_test_split(
    x_data, y_data, test_size=0.2, random_state=1
)

#Creating and training the linear regression model
regModel = LinearRegression()
regModel.fit(X_train, y_train)

#making predictions using the test data values
predictions = regModel.predict(X_test)

#testing the model by comparing predicted values to actual values
r2 = r2_score(y_test, predictions)
MSE = mean_squared_error(y_test, predictions)
MAE = mean_absolute_error(y_test, predictions)

#stating the results of the model
print(f"R^2 Score: {r2}")
print(f"Mean Squared Error: {MSE}")
print(f"Mean Absolute Error: {MAE}")

#0.6 threshold
threshold = input("What is the threshold:") or 0.6
if (predictions >= threshold):
    print("The battery is healthy.")


plt.scatter(x_data, y_data)

plt.xlabel("Data")
plt.ylabel("SOH")
plt.title("Linear Regression")
