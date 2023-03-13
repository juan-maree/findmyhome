from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


"""KMean Clustering
References:
- https://becominghuman.ai/clustering-real-estate-data-594894e24484
- https://towardsdatascience.com/kmeans-clustering-for-classification-74b992405d0a
"""
  
def kmean(data):
  max_cluster = 5
  sil_graph = {}
  for cluster in range(2, max_cluster + 1):
    kmeans = KMeans(n_clusters=cluster, random_state=0).fit(data)
    sil_graph[cluster] = silhouette_score(data, kmeans.labels_)
  return data