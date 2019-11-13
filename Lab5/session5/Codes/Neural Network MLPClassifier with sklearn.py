import warnings 
warnings.simplefilter("ignore") 

import pandas as pd
wine = pd.read_csv('wine_data.csv', names = ["Cultivator", "Alchol", "Malic_Acid", "Ash", "Alcalinity_of_Ash", "Magnesium", "Total_phenols", "Falvanoids", "Nonflavanoid_phenols", "Proanthocyanins", "Color_intensity", "Hue", "OD280", "Proline"])
# original dataset link: https://archive.ics.uci.edu/ml/datasets/Wine

print(wine.head())

print(wine.shape)

X = wine.drop('Cultivator',axis=1)
Y = wine['Cultivator']

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=2/3)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

from sklearn.neural_network import MLPClassifier
mlp = MLPClassifier()
mlp.fit(X_train,Y_train)

predictions = mlp.predict(X_test)

from sklearn.metrics import accuracy_score
accuracyScore = accuracy_score(Y_test, predictions)
print(accuracyScore)
