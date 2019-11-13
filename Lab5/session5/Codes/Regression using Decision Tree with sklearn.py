# Import the necessary libraries
import numpy
import matplotlib.pyplot as plot
import pandas
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

# Import the dataset
dataset = pandas.read_csv('salaryData.csv')

# Differentiate attribute and target columns
x = dataset['YearsExperience'].values
y = dataset['Salary'].values
X = x.reshape(len(x),1)
Y = y.reshape(len(y),1)

# Split the dataset into the training set and test set
xTrain, xTest, yTrain, yTest = train_test_split(X, Y, test_size = 2/3)

# Creating a DecisionTreeRegressor on our trainging set.
regressor = DecisionTreeRegressor()
regressor.fit(xTrain, yTrain)

# Predicting the test set results
yPrediction = regressor.predict(xTest)


# Displaying errors
print('Mean Absolute Error:', metrics.mean_absolute_error(yTest, yPrediction))  
