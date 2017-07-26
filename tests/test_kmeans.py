import unittest
from kmeans import KMeans


class TestKMeans(unittest.TestCase):

    def test_kmeans(self):

        locations = [[1, 1], [1, 2], [2, 1], [1, 3], [3, 1], [2, 2],
                     [10, 10], [10, 20], [20, 10], [10, 30], [30, 10], [20, 20]]

        clusterer = KMeans(2)
        clusterer.train(locations)
