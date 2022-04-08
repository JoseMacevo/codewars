import unittest
from scrooge import calculate_years


class test_basic_cases(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(calculate_years(1000, 0.05, 0.18, 1100), 3)
        self.assertEqual(calculate_years(1000, 0.01625, 0.18, 1200), 6)
        self.assertEqual(calculate_years(1000, 0.05, 0.18, 1000), 0)
