import random
from kmeans import KMeans


locations = [[1, 1], [11, 11], [1, 2], [11, 12], [2, 1],
             [12, 11], [1, 3], [11, 13], [3, 1], [13, 11],
             [2, 2], [12, 12]]

random.seed(0)
clusterer = KMeans(2)
assignments = clusterer.train(locations)

print(clusterer.means)
print(assignments)
