import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

# Example data: transaction amount, dispute duration, complaint type
data = pd.read_csv("banking_dispute_dataset_zzu.csv")

# Convert 'Dispute Type' (categorical) to numeric using Label Encoding
label_encoder = LabelEncoder()
data['Dispute Type'] = label_encoder.fit_transform(data['Dispute Type'])

# Use K-Means clustering
kmeans = KMeans(n_clusters=3)
data['Cluster'] = kmeans.fit_predict(data[['Transaction ID', 'Dispute Resolution Time', 'Dispute Type']])

# Visualize clusters
plt.scatter(data['Transaction ID'], data['Dispute Resolution Time'], c=data['Cluster'])
plt.xlabel('Transaction ID')
plt.ylabel('Dispute Duration')
plt.title('Clustering Disputes Based on Characteristics')
plt.show()
