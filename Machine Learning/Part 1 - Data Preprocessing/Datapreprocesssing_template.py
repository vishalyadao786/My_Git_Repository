# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 11:45:53 2017

@author: visha
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Importing Data Sets
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 3].values

#Splitting the dataset into Test Set and Training Set
from sklearn.cross_validation import train_test_split
X_train, X_test, Y_train, Y_test =train_test_split(X, Y, test_size = 0.2, random_state = 0)
dataset = pd.read_csv ("data.csv")

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)"""