import unittest
from hamming_distance import hamming_distance
from hamming_distance import hamming_distance_matrix


class TestHammingDistance(unittest.TestCase):

    def test_hamming_distance_1(self):

        v = [1, 1, 1, 1, 1, 1, 1]
        w = [1, 1, 1, 1, 1, 1, 1]

        self.assertEqual(0, hamming_distance(v, w))

    def test_hamming_distance_2(self):

        v = [1, 1, 1, 1, 1, 0, 1]
        w = [1, 0, 1, 1, 1, 1, 1]

        self.assertEqual(2, hamming_distance(v, w))
        
    def test_hamming_distance_3(self):

        v = [0, 1, 0, 1, 0, 0, 1]
        w = [1, 0, 1, 0, 1, 1, 0]

        self.assertEqual(7, hamming_distance(v, w))

    def test_hamming_distance_matrix_1(self):

        vectors = [
            [1, 0], [0, 1]
        ]

        self.assertEqual([[0, 2], [2, 0]], hamming_distance_matrix(vectors))

    def test_hamming_distance_matrix_2(self):

        vectors = [
            [1, 0, 1], [0, 1, 1], [0, 1, 0]
        ]

        self.assertEqual([[0, 2, 2], [2, 0, 1], [3, 2, 0]], hamming_distance_matrix(vectors))
