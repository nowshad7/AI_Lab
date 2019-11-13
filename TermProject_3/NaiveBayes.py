# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 00:29:03 2019

@author: nowshad
"""
from sklearn.model_selection import train_test_split
import pandas as pd 
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
import numpy

dataset = pd.read_csv('HeartDisease.csv')
print("\nSize:- ", dataset.shape) 
print("\n", dataset.head(5))

X=dataset[['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach',
       'exang', 'oldpeak', 'slope', 'ca', 'thal']]
y=dataset['target'] 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)
model = GaussianNB()
model.fit(X_train, y_train)
model_predictions = model.predict(X_test)

df = pd.DataFrame({'Actual': y_test, 'Predicted': model_predictions})
print("\n", df.head())

# Displaying errors
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, model_predictions))  
print('Mean Squared Error:', metrics.mean_squared_error(y_test, model_predictions))  
print('Root Mean Squared Error:', numpy.sqrt(metrics.mean_squared_error(y_test, model_predictions)))
print("Accuracy:",metrics.accuracy_score(y_test, model_predictions))

