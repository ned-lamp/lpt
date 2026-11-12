"""
11 - K-Means Clustering on Sales Data (Elbow Method)

Aim: Implement K-Means clustering / hierarchical clustering on sales_data_sample.csv
     dataset. Determine the number of clusters using the elbow method.

Dataset: sales_data_sample.csv -> https://www.kaggle.com/datasets/kyanyoga/sample-sales-data

Formula: WCSS = sum of (distance of each point from its cluster centroid)^2

Complexity:
  Time  : O(n x K x i x f) -> n points, K clusters, i iterations, f features
  Space : O(n x f + K x f) -> the data + K centroids

Key terms:
  Clustering        : grouping similar data points together.
  Unsupervised      : no labels given; the algorithm finds groups itself.
  Centroid          : centre (mean) of a cluster.
  K-Means steps     : pick K centroids -> assign each point to nearest centroid ->
                      move centroid to mean of its points -> repeat until no change.
  WCSS (inertia)    : within-cluster sum of squares; lower = tighter clusters.
  Elbow method      : plot WCSS vs K; the bend ("elbow") point is the best K.
  n_init            : runs K-Means several times with different starts, keeps best.
  Hierarchical      : alternative; no K needed upfront, builds a tree (dendrogram)
                      by merging closest clusters.
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# 1. Load data (file needs latin1 encoding)
df = pd.read_csv("sales_data_sample.csv", encoding="latin1")
X = df[["QUANTITYORDERED", "PRICEEACH", "SALES"]].dropna()

# 2. Scale
X = StandardScaler().fit_transform(X)

# 3. Elbow method: try K = 1 to 10
wcss = []
for k in range(1, 11):
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X)
    wcss.append(km.inertia_)

plt.plot(range(1, 11), wcss, marker="o")
plt.xlabel("Number of clusters (K)")
plt.ylabel("WCSS")
plt.title("Elbow Method")
plt.show()

# 4. Final model with K from the elbow (usually 3)
km = KMeans(n_clusters=3, random_state=42, n_init=10)
labels = km.fit_predict(X)

print("Cluster sizes:", pd.Series(labels).value_counts().to_dict())

plt.scatter(X[:, 0], X[:, 2], c=labels)
plt.xlabel("Quantity Ordered (scaled)")
plt.ylabel("Sales (scaled)")
plt.title("K-Means Clusters")
plt.show()
