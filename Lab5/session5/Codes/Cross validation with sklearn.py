from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score
import warnings
warnings.simplefilter("ignore")

iris_data = load_iris()

x = iris_data.data
y = iris_data.target

kf = KFold(n_splits=5)

print("\nK nearest neighbor:")
for train_index, test_index in kf.split(x):
    x_train, x_test = x[train_index], x[test_index]
    y_train, y_test = y[train_index], y[test_index]
    knn = KNeighborsClassifier()
    knn.fit(x_train,y_train)
    prediction = knn.predict(x_test)
    print(accuracy_score(y_test, prediction))
