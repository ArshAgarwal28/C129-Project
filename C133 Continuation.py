import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.cluster import KMeans


df = pd.read_csv(r'Projects\C129\venv\C131 Data.csv')

masses = df.iloc[:, -3]
radius = df.iloc[:, -2]

wcss = []

X = np.array(list(zip(masses, radius))).reshape(len(masses), 2)

for cluster in range(1, 11):
    kmeans = KMeans(n_clusters=cluster, init='k-means++',
                    random_state=0).fit(X)

    wcss.append(kmeans.inertia_)

# Plot 1 Elbow
plt.figure(figsize=(10, 5))
sns.lineplot(range(1, 11), wcss, marker='o', color='red')

plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')

plt.show()


# Plot 2 Cluster
kmeans = KMeans(n_clusters=4, init='k-means++', random_state=0)
y_kmeans = kmeans.fit_predict(X)

cluster1_x = []
cluster1_y = []

cluster2_x = []
cluster2_y = []

cluster3_x = []
cluster3_y = []

cluster4_x = []
cluster4_y = []

for index, data in enumerate(X):
    if y_kmeans[index] == 0:
        cluster1_x.append(data[0])
        cluster1_y.append(data[1])

    elif y_kmeans[index] == 1:
        cluster2_x.append(data[0])
        cluster2_y.append(data[1])

    elif y_kmeans[index] == 2:
        cluster3_x.append(data[0])
        cluster3_y.append(data[1])

    elif y_kmeans[index] == 3:
        cluster4_x.append(data[0])
        cluster4_y.append(data[1])

plt.figure(figsize=(15, 7))
sns.scatterplot(cluster1_x, cluster1_y, color='yellow', label='Cluster 1')
sns.scatterplot(cluster2_x, cluster2_y, color='red', label='Cluster 2')
sns.scatterplot(cluster3_x, cluster3_y, color='green', label='Cluster 3')
sns.scatterplot(cluster4_x, cluster4_y, color='blue', label='Cluster 4')

plt.title('Cluster of Planets')
plt.xlabel('Planet Radius')
plt.ylabel('Planet Mass')
plt.legend()
plt.gca().invert_yaxis()
plt.show()
