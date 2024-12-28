import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path
import pickle
import json
from umap.umap_ import UMAP
from sklearn.cluster import DBSCAN
import pandas as pd

# Suppress the gRPC warning
import os
os.environ['GRPC_ENABLE_FORK_SUPPORT'] = '0'

# Load the saved embeddings and document map
with open("document_embeddings.pkl", 'rb') as f:
    embeddings_array = pickle.load(f)

with open("document_map.json", 'r') as f:
    document_map = json.load(f)
file_paths = document_map['file_paths']

# Convert file paths to just the filename for cleaner visualization
filenames = [Path(fp).name for fp in file_paths]

# Reduce dimensionality with UMAP
reducer = UMAP(n_neighbors=15, min_dist=0.1, random_state=42)
embeddings_2d = reducer.fit_transform(embeddings_array)

# Perform clustering
clustering = DBSCAN(eps=0.15, min_samples=2, metric='cosine')
labels = clustering.fit_predict(embeddings_array)

# Create a DataFrame for plotting
df = pd.DataFrame({
    'x': embeddings_2d[:, 0],
    'y': embeddings_2d[:, 1],
    'filename': filenames,
    'cluster': labels,
    'full_path': file_paths
})

# Create an interactive scatter plot
fig = px.scatter(
    df,
    x='x',
    y='y',
    color='cluster',
    hover_data=['filename', 'full_path'],
    title='Document Embeddings Visualization',
    labels={'cluster': 'Cluster'},
    color_continuous_scale='viridis'
)

# Update the layout
fig.update_layout(
    plot_bgcolor='white',
    width=1200,
    height=800,
    title={
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    }
)

# Add grid lines
fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')

# Save the interactive plot
fig.write_html("embeddings_visualization.html")

# Print some statistics
n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
n_noise = list(labels).count(-1)
print(f"Number of clusters: {n_clusters}")
print(f"Number of noise points: {n_noise}")
print(f"Total documents: {len(labels)}")

# Save visualization data for later use
df.to_csv("embedding_visualization_data.csv", index=False)