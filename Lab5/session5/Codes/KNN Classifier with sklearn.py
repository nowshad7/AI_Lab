'''
scikit-learn is a Python module for machine learning built on
top of SciPy and distributed under the 3-Clause BSD license.

installation command: pip install scikit-learn
'''

# importing necessary libraries
from sklearn import datasets
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from pandas import DataFrame
import pandas


'''
sklearn.datasets has a dataset called iris dataset

The data set contains 3 classes of 50 instances each,
where each class refers to a type of iris plant.

Attribute Information:
1. sepal length in cm
2. sepal width in cm
3. petal length in cm
4. petal width in cm
5. class: Iris Setosa , Iris Versicolour , Iris Virginica

'''

# print the top five rows of the dataset
# print(DataFrame(datasets.load_iris().data).head())

# loading the iris dataset
iris = datasets.load_iris()


# X -> features, Y -> label
X = iris.data
Y = iris.target

# print(X)
# print(Y)

# dividing X, y into train and test data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.67)

# training a KNN classifier
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=7).fit(X_train, Y_train)

# testing
knn_predictions = knn.predict(X_test)

df = pandas.DataFrame({'Actual': Y_test.flatten(), 'Predicted': knn_predictions.flatten()})
print(df)

# accuracy of prediction
accuracy = knn.score(X_test, Y_test)
print("\nAccuracy: ", accuracy)


