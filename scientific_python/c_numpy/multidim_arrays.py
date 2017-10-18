#!/usr/bin/env python3

from __future__ import division, print_function, unicode_literals

import numpy as np
from numpy.testing import assert_almost_equal, assert_array_equal

# We have talked about 1-D ndarrays in `arrays.py`. Read it before this file.

### Basics ###

## np.array ##

# Usually np.array understands that nested list/tuple represents
# multidimensional array:
a = np.array([
    [1,2,3],
    [4,5,6],
])
assert a.ndim == 2
assert a.shape == (2, 3)
# ndarray.shape attribute contains sizes of the array throw its axes.

a = np.array([1,2,3], ndmin=2)  # produces one additional dimension
assert a.ndim == 2
assert a.shape == (1, 3)
a = np.array([1,2,3], ndmin=10)
assert a.ndim == 10
assert a.shape == (1,)*9 + (3,)

## reshape ##


## Simple indexing ##


