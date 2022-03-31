import unittest
from coupon_code import check_coupon


class test_basic_cases(unittest.TestCase):
    def tet_cases(self):
        self.assertEqual(check_coupon('123', '123', 'September 5, 2014', 'October 1, 2014'), True)
        self.assertEqual(check_coupon('123a', '123', 'September 5, 2014', 'October 1, 2014'), False)

