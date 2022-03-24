import unittest
from enough_space import enough


class test_basic_cases(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(enough(10, 5, 5), 0)
        self.assertEqual(enough(100, 60, 50), 10)
        self.assertEqual(enough(20, 5, 5), 0)
