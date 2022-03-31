import unittest
from new_member import open_or_senior


class test_basic_cases(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(open_or_senior([(45, 12), (55, 21), (19, -2), (104, 20)]), ['Open', 'Senior', 'Open', 'Senior'])
        self.assertEqual(open_or_senior([(16, 23), (73, 1), (56, 20), (1, -1)]), ['Open', 'Open', 'Senior', 'Open'])

