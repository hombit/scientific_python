import math
import random
import unittest
# import pytest
from math import sin

from numpy.testing import assert_allclose, assert_array_equal


def is_snake(word):
    if not word.isalpha():
        raise ValueError('Parameter must be a word')
    if word.lower() == 'питон':
        return True
    elif word.lower() == 'python':
        return True
    return False


class IsSnakeTestCase(unittest.TestCase):
    def test_ru_python(self):
        assert is_snake('Питон'), 'Питон is a snake'
    
    def test_python(self):
        self.assertTrue(is_snake('python'))
    
    def test_not_word(self):
        with self.assertRaises(ValueError):
            is_snake('123')


class SineTestCase(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(0, sin(0))
        
    def test_bounds(self):
        random.seed(0)
        x = random.random()
        self.assertLessEqual(-1, sin(x))
    
    def test_60(self):
        x = math.radians(60.0001)
        assert_allclose(0.5 * math.sqrt(3), sin(x), rtol=1e-5)
        
        
if __name__ == '__main__':
    unittest.main()