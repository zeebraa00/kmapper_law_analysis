import numpy as np
from scipy.spatial.distance import pdist, squareform
from kepler_mapper import kmapper as km
import sklearn
from sklearn import datasets

####

# data, labels = datasets.make_circles(n_samples=7543, noise=0.03, factor=0.3)
# print(data)

names=np.load("law_list.npy").tolist()
print(names)

# Initialize
mapper = km.KeplerMapper(verbose=1)

projected_data = mapper.project(
    projection=sklearn.manifold.TSNE(),
    distance_matrix="precomputed"
)

cubes=30
overlap=0.2

# Create dictionary called 'graph' with nodes, edges and meta-information
graph = mapper.map(projected_data,
                cover=km.Cover(n_cubes=cubes, perc_overlap=overlap),
                precomputed=True,
                clusterer=sklearn.cluster.DBSCAN(metric="precomputed"))

# Visualize it
mapper.visualize(graph, path_html="keplermapper_output_"+str(cubes)+"_"+str(overlap)+".html",
                 X_names=names,
                 title="law analysis using tda ("+str(cubes)+"/"+str(overlap)+")")