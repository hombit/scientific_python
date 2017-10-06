#!/usr/bin/env python3

from __future__ import division, print_function, unicode_literals

import numpy as np  # this is a common alias from numpy documentation

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

# You don't need to construct ndarray manually, use instead one of construction
# functions. The main one is `array`:
a = np.array([0,1,2,3,4])
a = np.array(range(5))

a = np.array([0,1,2,3,4], dtype=np.uint8)
a[0] = -1
assert a[0] == 255
