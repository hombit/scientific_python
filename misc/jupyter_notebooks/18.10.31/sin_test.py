"""Run it by
python3 -m unittest sin_test
"""

import unittest
import numpy as np
from numpy.testing import assert_allclose, assert_array_equal


def is_snake(word):
    if not word.isalpha():
        raise ValueError("String '{}' is not a word")
    if word.lower() == 'python':
        return True
    if word.lower() == 'питон':
        return True
    return False


def plus(a, b):
    return a + b


class PlusTestCase(unittest.TestCase):
    def test_type(self):
        with self.assertRaises(TypeError):
            plus(1, 'a')
        self.assertTrue(isinstance('a', str))


class SinTestCase(unittest.TestCase):
    """Tests np.sin"""
    
    def test_zero(self):
        """sin(0) == 0"""
        x = 0
        y = 0
        self.assertEqual(np.sin(x), y)
    
    def test_half_pi(self):
        """sin(pi/2) == 1"""
        x = np.pi / 2
        y = 1
        self.assertEqual(np.sin(x), y,
                         msg='sin pi/2 should be equal unity')

    def test_trig(self):
        x = np.linspace(0, 1, 11)
        sin = np.sin(x)
        cos = np.cos(x)
        assert_allclose(1-cos**2, sin**2, rtol=1e-7, atol=1e-5)
        

class IsSnake(unittest.TestCase):
    def test_python(self):
        self.assertTrue(is_snake('python'), msg='python is a snake')
    
    def test_dog(self):
        self.assertFalse(is_snake('cat'))
        
