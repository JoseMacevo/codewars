import unittest
from sort_numbers import solution


class test_basic_cases(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(solution([1, 2, 3, 10, 5]), [1, 2, 3, 5, 10])
        self.assertEqual(solution(None), [])
        self.assertEqual(solution([]), [])
        self.assertEqual(solution([20, 2, 10]), [2, 10, 20])
        self.assertEqual(solution([2, 20, 10]), [2, 10, 20])
