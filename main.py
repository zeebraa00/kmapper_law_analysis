import numpy as np
from scipy.spatial.distance import pdist, squareform
from kepler_mapper import kmapper as km
import sklearn
from sklearn import datasets

####

# data, labels = datasets.make_circles(n_samples=7543, noise=0.03, factor=0.3)
# print(data)

# Initialize
mapper = km.KeplerMapper(verbose=1)

projected_data = mapper.project(
    projection=sklearn.manifold.TSNE(),
    distance_matrix="euclidean"
)

# Create dictionary called 'graph' with nodes, edges and meta-information
graph = mapper.map(projected_data, cover=km.Cover(n_cubes=30, perc_overlap=0.4))

# Visualize it
mapper.visualize(graph, path_html="keplermapper_output_30_0.4.html",
                 title="law analysis using tda (30 / 0.4)")