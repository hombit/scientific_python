#!/usr/bin/env python3

# This file contains examples of usage of scipy.integrate module

from __future__ import division

import numpy as np
from numpy.testing import assert_allclose, assert_array_equal
from scipy import integrate


### quad ###

# `quad` integrates numerically 1-D functions

a, b = 0, np.pi
integral, error = integrate.quad(np.sin, a, b)
assert_allclose(-np.cos(b) + np.cos(a), integral, rtol=0, atol=error)

integral, error = integrate.quad(
    lambda x: np.exp(-x**2),
    -np.inf, np.inf
)
assert_allclose(np.sqrt(np.pi), integral, rtol=0, atol=error)


