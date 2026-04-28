import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans

iris = load_iris()
X = iris.data

k = 3

kmeans = KMeans(n_clusters= k , random_state = 0)
labels = kmeans.fit_predict(X)
centroids = kmeans.cluster_centers_

print("k_means labels:" , labels)
print("k-means centroids:" , centroids)

plt.scatter(X[:,0], X[:,1], c=labels , cmap = 'viridis')
plt.scatter(centroids[:,0] , centroids[:,1] , marker = 'x' , color = 'red' , s=200)
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.title('K-means clustering of iris Dataset')
plt.show()