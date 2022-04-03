import unittest
from highest_profit import min_max


class test_basic_cases(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(min_max([1, 2, 3, 4, 5]), [1, 5])
        self.assertEqual(min_max([2334454, 5]), [5, 2334454])
