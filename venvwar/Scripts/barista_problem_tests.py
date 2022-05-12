import unittest
from barista_problem import barista


class test_basic_cases(unittest.TestCase):
    def test_cases(self):
        #self.assertEqual(barista([], 0, 'Sorry, but the smallest waiting time possible is: 85'))
        self.assertEqual(barista([2, 10, 5, 3, 9]), 85, 'Sorry, but the smallest waiting time possible is: 85')
        self.assertEqual(barista([4, 3, 2]), 22, 'Sorry, but the smallest waiting time possible is: 22')
        self.assertEqual(barista([20, 5]), 32, 'Sorry, but the smallest waiting time possible is: 32')
        self.assertEqual(barista([20, 5, 4, 3, 1, 5, 7, 8]), 211, 'Sorry, but the smallest waiting time possible is: 211')
        self.assertEqual(barista([5, 4, 3, 2, 1]), 55, 'Sorry, but the smallest waiting time possible is: 55')

