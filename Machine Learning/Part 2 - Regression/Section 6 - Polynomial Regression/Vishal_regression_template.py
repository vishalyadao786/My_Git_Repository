# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 11:11:46 2017

@author: visha
"""

#Regression Template
#Polynomial Regression
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Importing Data Sets
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
Y = dataset.iloc[:, 2].values

#Splitting the dataset into Test Set and Training Set
'''from sklearn.cross_validation import train_test_split
X_train, X_test, Y_train, Y_test =train_test_split(X, Y, test_size = 0.2, random_state = 0)
dataset = pd.read_csv ("data.csv")'''

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""


#Fitting the Regression Model to the dataset
#Create your regressor here

#Predicting a new result with Regression
y_pred = regressor.predict(6.5)

#Visualizing the Regression Results
plt.scatter(X, Y, color = 'red')
plt.plot(X, regressor.predict(X), color = 'blue')
plt.title('Truth or Bluff (Regression Model)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()

#Visualizing the Regression Results (For higher resolution and smoother curve)
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, Y, color = 'red')
plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')
plt.title('Truth or Bluff (Regression Model)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()
