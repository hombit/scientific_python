#!/usr/bin/env python3

from __future__ import print_function, division, unicode_literals

import unittest


def is_even(n):
    if int(n) != n:
        raise ValueError('Argument should be integer')
    return n % 2 == 0


class IsEvenTestCase(unittest.TestCase):
    def test_even(self):
        self.assertTrue(is_even(10), '10 is even')

    def test_odd(self):
        self.assertFalse(is_even(7), '7 is odd')

    def test_float(self):
        with self.assertRaises(ValueError,
                               msg='float number should lead to exception'):
            is_even(3.14)

    def test_non_integer(self):
        with self.assertRaises((ValueError, TypeError),
                               msg='argument should be a number'):
            is_even([2, 3])


# This function can be used in `setup.py` as `test_suite` keyword argument
def test_suite():
    suite = unittest.defaultTestLoader.loadTestsFromModule(__name__)
    return suite


if __name__ == '__main__':  # checks if this file executed as script
    unittest.main()
        
