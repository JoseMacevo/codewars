import unittest
from reversed_sequence import reverse_seq


class test_basic_cases(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(reverse_seq(5), [5, 4, 3, 2, 1])
