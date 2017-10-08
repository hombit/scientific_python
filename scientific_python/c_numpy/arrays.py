#!/usr/bin/env python3

from __future__ import division, print_function, unicode_literals

import numpy as np  # this is a common alias from numpy documentation
from numpy.testing import assert_almost_equal, assert_array_equal

# `numpy` is a linear algebra library for python written primarily on C
# https://numpy.org `numpy` is a part of SciPy ecosystem that includes other
# useful packages for science programming such as `scipy`, `IPython`, `pandas` 
# and `matplotlib`.

# The kernel of `numpy` is `ndarray` class that implements multidimensional
# array of one-type objects. These arrays have constant size and their elements
# cannot be converted into another type in-place.

# One more remark before we start. Do not be confounded by `array` module of
# standard library https://docs.python.org/3/library/array.html that contains
# class `array.array` is very similar to list except that all its elements
# should have one type.

# This part will be a summary of `numpy` tutorial:
# https://docs.scipy.org/doc/numpy/user/quickstart.html
# If you are a fan of Matlab see also:
# https://docs.scipy.org/doc/numpy/user/numpy-for-matlab-users.html

### Array construction ###

## np.array ##
# You don't need to construct ndarray manually, use instead one of construction
# functions. The main one is `array`:
a = np.array([0,1,2,3,4])
a = np.array(range(5))

a = np.array([0,1,2,3,4], dtype=np.uint8)
a[0] = -1
# numpy numerical types are close related to C's types:
assert a[0] == 255
# Long types are available only on 64bit systems and float implementation is
# system specific (just like in C):
from sys import maxsize
if maxsize > 2**32:  # 64 (or more) bits system
    a = np.array([1,2,3,4], dtype=np.float128)
    assert a.itemsize == 16
    b = np.array([1,2,3,4], dtype=np.complex256)
    assert a.itemsize == 16
else:
    try:
        dtype = np.float128
        assert False
    except AttributionError as e:
        assert str(e) == "'module 'numpy' has no attribute 'float128''"

## Implicit type conversion ##
a = np.array([1,2,3,4], dtype=np.int)
a[0] = 5.5  # implicit type conversion as in C
assert a[0] == 5
# Implicit conversion from complex to float and int is denied:
try:
    a[0] = 5 + 3j
    assert False
except TypeError as e:
    assert str(e) == "can't convert complex to int"

## Creation functions ##

# `np.arange` is `numpy` analogue of built-in `range` function:
a = np.arange(5)
assert_array_equal(a, np.array(range(5)))
sl = (3, 30, 2)
assert_array_equal(np.arange(*sl), np.array(range(*sl)))

# Instead of `range` `np.arange` accept float arguments:
assert_array_equal(np.arange(3.5), np.array(range(4)))
assert_almost_equal(np.arange(0, 1, 0.25), [0., 0.25, 0.5, 0.75])
# However you should avoid to use `np.arange` with float steps, because of
# floating point arithmetic accuracy problems. Use `np.linspace` instead:
assert_almost_equal(np.arange(0, 1.1, 0.5), np.linspace(0, 1, 3))
# `np.linspace(start, stop, num)` includes both `start` and `stop`, and always
# has `num` elements.
# `np.logspace(start, stop, num)` is a similar function that produces geometric
# progression between `10**start` and `10**stop` numbers:
sl = (0, 1, 10)
assert_almost_equal(np.logspace(*sl), 10**np.linspace(*sl))


