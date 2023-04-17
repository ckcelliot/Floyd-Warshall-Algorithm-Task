import unittest
import sys

# Import the functions to be tested
from floyd_rec import floyd_recursive
from floyd import floyd

class TestFloydAlgorithm(unittest.TestCase):

    def setUp(self):
        # Initialize test data
        self.NO_PATH = sys.maxsize
        self.graph = [
            [0, 7, self.NO_PATH, 8],
            [self.NO_PATH, 0, 5, self.NO_PATH],
            [self.NO_PATH, self.NO_PATH, 0, 2],
            [self.NO_PATH, self.NO_PATH, self.NO_PATH, 0]
        ]
        self.MAX_LENGTH = len(self.graph[0])

    def test_floyd_rec(self):
        # Test case 1: Start and end nodes are the same
        distance = [[self.NO_PATH] * self.MAX_LENGTH for _ in range(self.MAX_LENGTH)]
        intermediate = 0
        start_node = 0
        end_node = 0
        floyd_recursive(distance, intermediate, start_node, end_node)
        self.assertEqual(distance[start_node][end_node], 0)

        # Test case 2: Start node is different from end node
        distance = [[self.NO_PATH] * self.MAX_LENGTH for _ in range(self.MAX_LENGTH)]
        intermediate = 1
        start_node = 0
        end_node = 1
        floyd_recursive(distance, intermediate, start_node, end_node)
        self.assertEqual(distance[start_node][end_node], 7)

    def test_floyd(self):
        # Test case 1: Check if floyd function updates distance matrix correctly
        distance = [row[:] for row in self.graph]
        floyd(distance)
        expected_distance = [
            [0, 7, 5, 8],
            [self.NO_PATH, 0, 5, 7],
            [self.NO_PATH, self.NO_PATH, 0, 2],
            [self.NO_PATH, self.NO_PATH, self.NO_PATH, 0]
        ]
        self.assertEqual(distance, expected_distance)

if __name__ == '__main__':
    unittest.main()
