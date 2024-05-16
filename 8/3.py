from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering
import pandas as pd
import scipy.cluster.hierarchy as shc

url = 'https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv'
dataset = pd.read_csv(url)
print(dataset.head())

print(dataset.shape)
data = dataset.iloc[:, 2:4].values

plt.figure(figsize=(28, 12), dpi=180)
plt.figure(figsize=(10,7))
dend = shc.dendrogram(shc.linkage(data, method='ward'))
plt.show()

cluster = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage='ward')
print(cluster.fit_predict(data))

plt.figure(figsize=(10,7))
plt.scatter(data[:,0], data[:,1], c=cluster.labels_, cmap='rainbow')
