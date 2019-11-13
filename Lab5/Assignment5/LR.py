# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 03:12:40 2019

@author: nowshad
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('headbrain.csv')
print(dataset.shape) 
print(dataset.head(5))  

X = dataset['Head Size(cm^3)'].values
Y = dataset['Brain Weight(grams)'].values
mean_x = np.mean(X)
mean_y= np.mean(Y)

n=len(X)

numer=0
denom=0
for i in range(n):
    numer += (X[i]-mean_x)*(Y[i]-mean_y)
    denom += (X[i]-mean_x)**2
    
m= numer/denom
c= mean_y - (m*mean_x)
print("m= ",m)
print("c= ",c)

max_x = np.max(X)+1
min_x= np.min(X)-1
x=np.linspace(min_x,max_x,5)
y=m*x+c

plt.plot(x,y,color='green',label='Regression Line')
plt.scatter(X,Y,color='red',label='Scatter Plot')
plt.xlabel('Head Size')
plt.ylabel('Brain Weight')
plt.legend()
plt.show()

err_nm=0
err_dn=0
for i in range(n):
    y_predict=m*X[i]+c
    err_nm += (Y[i]-y_predict) **2
    err_dn += (Y[i]-mean_y)**2
error= (1-(err_nm/err_dn))*100
print("\nAccuracy:",error,"%")












