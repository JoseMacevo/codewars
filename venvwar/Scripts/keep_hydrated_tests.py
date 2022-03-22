import unittest
from keep_hydrated import litres


class test_basic_cases(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(litres(2), 1, 'Should return 1 litre')
        self.assertEqual(litres(1.4), 0, 'Should return 0 litres')
        self.assertEqual(litres(12.3), 6, 'Should return 6 litres')
        self.assertEqual(litres(0.82), 0, 'Should return 0 litres')
        self.assertEqual(litres(11.8), 5, 'Should return 5 litres')
        self.assertEqual(litres(1787), 893, 'Should return 893 litres')
        self.assertEqual(litres(0), 0, 'Should return 0 litres')
