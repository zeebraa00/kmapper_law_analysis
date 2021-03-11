"""
Copyright ⓒ 2021 성균관대학교 수학과 정재헌(JaeHeon Jeong) All Rights Reserved
email : zeebraa00@gmail.com
"""

import numpy as np
from scipy.spatial.distance import pdist, squareform
from kepler_mapper import kmapper as km
import sklearn
from sklearn import datasets

custom_metric = np.load("law_data/custom_metric.npy")

# Initialize
mapper = km.KeplerMapper(verbose=1)

projected_data = mapper.project(
    projection=sklearn.manifold.TSNE(),
    distance_matrix="precomputed"
)

# Set hyperparameters for clustering
cubes=30
overlap=0.3
epsilon=5

# Create dictionary called 'graph' with nodes, edges and meta-information
graph = mapper.map(
                projected_data,
                X=custom_metric,
                cover=km.Cover(n_cubes=cubes, perc_overlap=overlap),
                precomputed=True,
                clusterer=sklearn.cluster.DBSCAN(eps=epsilon, metric='precomputed').fit(custom_metric)
                )

# Visualize it
mapper.visualize(graph, path_html="keplermapper_output_"+str(cubes)+"_"+str(overlap)+"_"+str(epsilon)+".html",
                 title="law analysis using tda ("+str(cubes)+"_"+str(overlap)+"_"+str(epsilon)+")")