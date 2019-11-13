from pandas import DataFrame
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

Data = {'x': [25,34,22,27,33,33,31,22,35,34,67,54,57,43,50,57,59,52,65,47,49,48,35,33,44,45,38,43,51,46],
        'y': [79,51,53,78,59,74,73,57,69,75,51,32,40,47,53,36,35,58,59,50,25,20,14,12,20,5,29,27,8,7]
       }
  
df = DataFrame(Data,columns=['x','y'])

plt.title("Data before clustering")
plt.scatter(df['x'], df['y'])
plt.show()

cn = int(input("How many clusters? :"))

  
kmeans = KMeans(n_clusters=cn).fit(df)
centroids = kmeans.cluster_centers_
print(centroids)

plt.title("Data after clustering")
plt.scatter(df['x'], df['y'], c= kmeans.labels_)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red')
plt.show()

