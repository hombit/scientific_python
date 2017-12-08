#!/usr/bin/env python3

from functools import reduce
import numpy as np
from numpy.testing import assert_allclose
import numba


if __package__:
    from .contfrac import contfrac as cython_contfrac
else:
    import pyximport
    pyximport.install(setup_args={'include_dirs': [np.get_include()]})
    from cy_contfrac import contfrac as cython_contfrac

def pure_contfrac(a):
    return reduce(lambda x, y: y + 1/x, a[::-1])

@numba.jit
def numba_contfrac(a):
    c = 1 / a[-1]
    for i in range(len(a)-2, -1, -1):
        c = a[i] + 1/c
    return c

n = 1000
a = np.ones(n)
assert (pure_contfrac(a)
        == numba_contfrac(a)
        == cython_contfrac(a))
assert_allclose(pure_contfrac(a), 0.5*(np.sqrt(5)+1))
