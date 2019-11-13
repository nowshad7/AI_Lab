# Import the necessary libraries
import matplotlib.pyplot as plot
import pandas

# Import the dataset
dataset = pandas.read_csv('salaryData.csv')

#Explore the dataset
print(dataset.shape) # number of rows and columns
print(dataset.head(5)) # display first five rows of the dataset
# iterating the columns 
for col in dataset.columns: 
    print(col)

# Differentiate attribute and target columns
x = dataset['YearsExperience'].values
y = dataset['Salary'].values
print(x.shape) # shape of x
print(y.shape) # shape of y

X = x.reshape(len(x),1)
Y = y.reshape(len(y),1)
print(X.shape) # shape of X
print(Y.shape) # shape of Y

plot.scatter(X, Y,  color='RED')
plot.show()
