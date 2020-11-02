#!/usr/bin/env python3

from contextlib import contextmanager
from functools import reduce, wraps
from random import normalvariate
from time import perf_counter

import numpy as np

try:
    import pyximport; pyximport.install(setup_args={'include_dirs': [np.get_include()]})
    from cy_examples import cython_contfrac, cython_autoreg
except ImportError:
    print('No Cython')
    
    def cython_contfrac(*args, **kwargs):
        pass

    def cython_autoreg(*args, **kwargs):
        pass


def trivial_wrapper(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        return f(*args, **kwargs)

    return wrapper


try:
    from numba import njit as numba_njit
except ImportError:
    print("Numba isn't found")
    numba_njit = trivial_wrapper


# Check if we are inside Nuitka binary
if "__compiled__" in globals():
    numba_njit = trivial_wrapper


@contextmanager
def timeit(msg):
    t = perf_counter()
    try:
        yield
    finally:
        dt = perf_counter() - t
        print(f'{msg}{dt:.6f} seconds')


def for_loop_no_casting_contfrac(a):
    c = 1 / a[-1]
    for i in range(len(a)-2, 0, -1):
        c = a[i] + 1/c
    return c


def for_loop_contfrac(a):
    c = 1.0 / a[-1]
    for i in range(len(a)-2, 0, -1):
        c = a[i] + 1.0/c
    return c


def reduce_contfrac(a):
    return reduce(lambda x, y: y + 1.0/x, a[::-1], 1.0)


numba_contfrac = numba_njit(for_loop_contfrac)
numba_contfrac.__name__ = 'numba_contfrac'


def autoreg(a, n):
    x = np.random.normal(0, 1, size=n)
    for i in range(1, n):
        x[i] += a * x[i - 1]
    return x


def autoreg_list(a, n):
    x = [normalvariate(0, 1)]
    for i in range(1, n):
        x.append(a * x[-1] + normalvariate(0, 1))
    return x


numba_autoreg = numba_njit(autoreg)
numba_autoreg.__name__ = 'numba_autoreg'


def main_contfrac():
    n = 1000
    count = 10000
    functions = [for_loop_no_casting_contfrac, for_loop_contfrac,
                 reduce_contfrac, numba_contfrac, cython_contfrac]
    a = np.ones(n)
    for f in functions:
        f(np.array([1]))
        with timeit(f'{f.__name__} exec time for np.array: '):
            for _ in range(count):
                f(a)
    functions = [for_loop_no_casting_contfrac, for_loop_contfrac,
                 reduce_contfrac]
    a = [1] * n
    for f in functions:
        f(np.array([1]))
        with timeit(f'{f.__name__} exec time for list: '):
            for _ in range(count):
                f(a)


def main_autoreg():
    n = 1000
    a = 0.5
    count = 1000
    functions = [autoreg, autoreg_list, numba_autoreg, cython_autoreg]
    for f in functions:
        f(a, n)
        with timeit(f'{f.__name__} exec time: '):
            for _ in range(count):
                f(a, n)


if __name__ == '__main__':
    main_contfrac()
    main_autoreg()
