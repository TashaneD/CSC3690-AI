import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

data = pd.read_csv('Credit Card Customer Data.csv')

# Display data
print("First few rows of the data:")
print(data.head())

# Select features for clustering
features = data[['Avg_Credit_Limit', 'Total_Credit_Cards', 'Total_visits_bank',
                 'Total_visits_online', 'Total_calls_made']]

# Standardize the data
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# Elbow Method to find the optimal number of clusters
inertia = []
k_values = range(1, 11)

for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(scaled_features)
    inertia.append(kmeans.inertia_)

# Plot the Elbow Curve
plt.figure(figsize=(8, 5))
plt.plot(k_values, inertia, marker='o', linestyle='--')
plt.title('Elbow Method for Optimal k')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia')
plt.xticks(k_values)
plt.grid()
plt.show()

# Choose optimal number of clusters
optimal_k = 3
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
kmeans.fit(scaled_features)

# Display the cluster centers
cluster_centers = scaler.inverse_transform(kmeans.cluster_centers_)
print(f"Cluster centers (k={optimal_k}):")
print(cluster_centers)
