import unittest
from two_fighters_preloaded import Fighter
from two_fighters import declare_winner


class test_basic_cases(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(declare_winner(Fighter("Lew", 10, 2), Fighter ("Harry", 5, 4), "Lew"), "Lew")
        self.assertEqual(declare_winner(Fighter("Lew", 10, 2), Fighter ("Harry", 5, 4), "Harry"), "Harry")
        self.assertEqual(declare_winner(Fighter("Harold", 20, 5), Fighter ("Harry", 5, 4), "Harry"), "Harold")
        self.assertEqual(declare_winner(Fighter("Harold", 20, 5), Fighter ("Harry", 5, 4), "Harold"), "Harold")
        self.assertEqual(declare_winner(Fighter("Jerry", 30, 3), Fighter ("Harold", 20, 5), "Jerry",), "Harold")
        self.assertEqual(declare_winner(Fighter("Jerry", 30, 3), Fighter ("Harold", 20, 5), "Harold"), "Harold")

