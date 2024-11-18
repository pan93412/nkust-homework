from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt

samples = [
  [14, 15], [22, 28], [15, 18], [20, 30],
  [30, 35], [18, 20], [32, 30]
]

methods = ['single', 'complete', 'average', 'weighted', 'centroid', 'median', 'ward']

for method in methods:
  res = linkage(samples, method=method)
  dendrogram(res)
  plt.title(f"Using {method} for linkage")
  plt.show()

