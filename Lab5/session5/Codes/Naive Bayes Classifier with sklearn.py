from sklearn import datasets
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from pandas import DataFrame
import pandas 
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

wine = datasets.load_wine()
X = wine.data
Y = wine.target
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=2/3)
model = GaussianNB()
model.fit(X_train, Y_train)
model_predictions = model.predict(X_test)
accuracyScore = accuracy_score(Y_test, model_predictions)
df = pandas.DataFrame({'Actual': Y_test.flatten(), 'Predicted': model_predictions.flatten()})
print(df)
print(accuracyScore)

