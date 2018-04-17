#!/usr/bin/env python3

import numpy as np
from numpy.testing import assert_allclose
from timeit import timeit
from copy import copy


if __package__:
    from .erf import erf, erfc
else:
    import pyximport
    pyximport.install()
    from erf import erf, erfc


assert erf(0) == 0
assert erf(-float('inf')) == -1
assert erfc(0) == 1
assert_allclose(erf(1), 1 - erfc(1))


timeit_kwargs = {
    'stmt': 'contfrac(a)',
    'number': 10,
    'setup': """import numpy as np
from {pack}contfrac import {func}_contfrac as contfrac
a = np.ones({n})""",
}

n = 1000000
pack = __package__+'.' if __package__ else ''
f_types = ['pure', 'numba', 'cython']
time = {}
for f in f_types:
    kwargs = copy(timeit_kwargs)
    kwargs['setup'] = kwargs['setup'].format(func=f, pack=pack, n=n)
    time[f] = timeit(**kwargs)
assert time['pure'] > time['numba']
assert time['pure'] > time['cython']
