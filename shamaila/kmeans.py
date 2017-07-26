import random

from linear_algebra import vector_mean
from hamming_distance import hamming_distance_float


class ShamailaKMeans:

    def __init__(self, k):
        self.k = k
        self.means = None

    def classify(self, v):
        return min(range(self.k), key=lambda i: hamming_distance_float(v, self.means[i]))

    def train(self, vectors):
        self.means = random.sample(vectors, self.k)
        assignments = None

        while True:
            new_assignments = [self.classify(v) for v in vectors]

            if assignments == new_assignments:
                return assignments

            assignments = new_assignments

            for i in range(self.k):
                i_points = [v for v, a in zip(vectors, assignments) if i == a]

                if i_points:
                    self.means[i] = vector_mean(i_points)

