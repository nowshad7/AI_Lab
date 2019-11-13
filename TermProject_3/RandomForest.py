# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 00:29:03 2019

@author: nowshad
"""
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
import pandas as pd
import numpy

dataset = pd.read_csv('HeartDisease.csv')
print("\nSize:- ", dataset.shape) 
print("\n", dataset.head(5))

X=dataset[['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach',
       'exang', 'oldpeak', 'slope', 'ca', 'thal']]
y=dataset['target'] 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)
clf=RandomForestClassifier(n_estimators=100)
clf.fit(X_train,y_train)
y_pred=clf.predict(X_test)
print()
df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(df.head())

# Displaying errors
print('\nMean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))  
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))  
print('Root Mean Squared Error:', numpy.sqrt(metrics.mean_squared_error(y_test, y_pred)))
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))