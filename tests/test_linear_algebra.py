import unittest
from linear_algebra import vector_add
from linear_algebra import vector_subtract
from linear_algebra import vector_sum
from linear_algebra import scalar_multiply
from linear_algebra import vector_mean
from linear_algebra import dot
from linear_algebra import sum_of_squares
from linear_algebra import magnitude
from linear_algebra import squared_distance
from linear_algebra import distance


class TestLinearAlgebraMethods(unittest.TestCase):

    def test_vector_add(self):
        self.assertEqual([3, 3, 3], vector_add([1, 3, 2], [2, 0, 1]))

    def test_vector_subtract(self):
        self.assertEqual([1, 0, 3], vector_subtract([3, 2, 6], [2, 2, 3]))

    def test_vector_sum(self):
        self.assertEqual([6, 5, 4], vector_sum([[2, 3, 1], [1, 1, 2], [3, 1, 1]]))

    def test_scalar_multiply(self):
        self.assertEqual([2, 4, 6], scalar_multiply(2, [1, 2, 3]))

    def test_vector_mean(self):
        result = vector_mean([[2, 3, 1], [1, 1, 2], [3, 1, 1]])

        self.assertAlmostEqual(6/3, result[0])
        self.assertAlmostEqual(5/3, result[1])
        self.assertAlmostEqual(4/3, result[2])

    def test_dot(self):
        self.assertEqual(7, dot([1, 2, 1], [2, 1, 3]))

    def test_sum_of_squares(self):
        self.assertEqual(6, sum_of_squares([1 , 2, 1]))

    def test_magnitude(self):
        self.assertEqual(5, magnitude([4, 3]))

    def test_squared_distance(self):
        self.assertEqual(8, squared_distance([4, 3], [2, 1]))

    def test_distance(self):
        self.assertEqual(5, distance([5, 4], [1, 1]))