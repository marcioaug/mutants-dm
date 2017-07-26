import random
from linear_algebra import vector_mean, squared_distance


class KMeans:

    def __init__(self, k):
        self.k = k
        self.means = None

    def classify(self, input):
        return min(range(self.k), key=lambda i: squared_distance(input, self.means[i]))

    def train(self, inputs):
        self.means = random.sample(inputs, self.k)
        assignments = None

        while True:
            new_assignments = [self.classify(i) for i in inputs]

            if assignments == new_assignments:
                return assignments

            assignments = new_assignments

            for i in range(self.k):
                i_points = [p for p, a in zip(inputs, assignments) if a == i]

                if i_points:
                    self.means[i] = vector_mean(i_points)

