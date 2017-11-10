import unittest
import numpy as np

def is_even(n):
    if int(n) != n:
        raise ValueError('Argument should be integer')
    return n % 2 == 0

class MyTest(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

class IsEvenTest(unittest.TestCase):
    def test_even(self):
        self.assertTrue(is_even(10))
    def test_odd(self):
        self.assertFalse(is_even(7))
    def test_float(self):
        with self.assertRaises(ValueError):
            is_even(3.14)

class FactorialTest(unittest.TestCase):
    def test_dactorial(self):
        self.assertEqual(120, np.math.factorial(5))

if __name__ == '__main__':
    unittest.main()