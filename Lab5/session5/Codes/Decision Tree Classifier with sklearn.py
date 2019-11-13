# importing necessary libraries
from sklearn import datasets
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from pandas import DataFrame
from sklearn import tree
from sklearn.metrics import accuracy_score

# loading the iris dataset
iris = datasets.load_iris()

# X -> features, Y -> label
X = iris.data
Y = iris.target

#print(X)
#print(Y)

# dividing X, Y into train and test data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=2/3)

# training a decision tree classifier
model = tree.DecisionTreeClassifier()
model.fit(X_train, Y_train)

# testing
model_predictions = model.predict(X_test)

# accuracy of prediction
accuracyScore = accuracy_score(Y_test, model_predictions)
print(accuracyScore)
