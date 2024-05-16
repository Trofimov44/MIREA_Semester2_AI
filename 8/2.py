import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
dataframe = load_iris()

X = dataframe.data

kmeans = KMeans(n_clusters = 3)
kmeans.fit(dataframe.data)
y_kmeans = kmeans.predict(dataframe.data)

plt.scatter(X[:, 0], X[:, 1], c = y_kmeans, s = 20, cmap='summer')
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c = 'blue', s = 100, alpha=0.9)
plt.show()
