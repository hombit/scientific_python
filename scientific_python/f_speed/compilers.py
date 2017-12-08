#!/usr/bin/env python3

import numpy as np
from numpy.testing import assert_allclose
from timeit import timeit
from copy import copy


timeit_kwargs= {
    'stmt' : 'contfrac(a)',
    'number': 10,
    'setup': """import numpy as np
from contfrac import {f}_contfrac as contfrac
a = np.ones({n})""",
}

n = 1000000
f_types = ['pure', 'numba', 'cython']
time = {}
for f in f_types:
    kwargs = copy(timeit_kwargs)
    kwargs['setup'] = kwargs['setup'].format(f=f, n=n)
    time[f] = timeit(**kwargs)
assert time['pure'] > time['numba']
assert time['pure'] > time['cython']
