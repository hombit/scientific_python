#!/usr/bin/env python3

from __future__ import division, print_function

from timeit import timeit  # we need it for performance tests

import numpy as np  # this is a common alias from numpy documentation
from numpy.testing import assert_allclose, assert_array_equal

# `numpy` is a linear algebra library written primarily on `C`:
# <http://numpy.org>. `numpy` is a part of [SciPy](https://SciPy.org) 
# ecosystem that includes other useful scientific packages such as `scipy`,
# `IPython`, `pandas` and `matplotlib`.

# The kernel of `numpy` is `ndarray` class that implements multidimensional
# array of the same type objects. These arrays have constant size and their
# elements cannot be converted into another type in-place.

# One more remark before we start. Do not be confounded by [`array` module of
# standard library](https://docs.python.org/3/library/array.html) that contains
# class `array.array` very similar to `list` except that all its elements
# should have one type.

# This section is a summary of `numpy` tutorial:
# <http://docs.scipy.org/doc/numpy/user/quickstart.html>
# If you are a fan of Matlab see also:
# <http://docs.scipy.org/doc/numpy/user/numpy-for-matlab-users.html>

# # Array construction

# ## np.array
# You don't need to construct ndarray manually, use instead one of construction
# functions. The main one is `array`:
a = np.array([0, 1, 2, 3, 4])
a = np.array(range(5))

a = np.array([0, 1, 2, 3, 4], dtype=np.uint8)
a[0] = -1
# numpy numerical types are close related to `C` types:
assert a[0] == 255
# Long types are implemented on some 64bit systems:
try:
    a = np.array([1, 2, 3, 4], dtype=np.float128)
    assert a.itemsize == 16
    b = np.array([1, 2, 3, 4], dtype=np.complex256)
    assert a.itemsize == 16
except AttributeError as e:
    assert str(e) == "module 'numpy' has no attribute 'float128'"

# ## Implicit type conversion
a = np.array([1, 2, 3, 4], dtype=np.int)
a[0] = 5.5  # implicit type conversion as in C
assert a[0] == 5
# Implicit conversion from complex to float and int is denied:
try:
    a[0] = 5 + 3j
    assert False
except TypeError as e:
    assert str(e).startswith("can't convert complex to")
    # "... to int" in Python 3, "... to long" in Python 2

# ## Creation functions

# `np.arange` is `numpy` analogue of built-in `range`:
a = np.arange(5)
assert_array_equal(a, np.array(range(5)))
sl = (3, 30, 2)
assert_array_equal(np.arange(*sl), np.array(range(*sl)))

# Instead of `range` `np.arange` accept float arguments:
assert_array_equal(np.arange(3.5), np.array(range(4)))
assert_allclose(np.arange(0, 1, 0.25), [0., 0.25, 0.5, 0.75])
# However you should avoid to use `np.arange` with float steps, because of
# floating point arithmetic accuracy problems. Use `np.linspace` instead:
assert_allclose(np.arange(0, 1.1, 0.5), np.linspace(0, 1, 3))
# `np.linspace(start, stop, num)` includes both `start` and `stop`, and always
# has `num` elements.
# `np.logspace(start, stop, num)` is a similar function that produces geometric
# progression between `10**start` and `10**stop` numbers:
sl = (0, 1, 10)
assert_allclose(np.logspace(*sl), 10**np.linspace(*sl))

# `np.empty` creates array with "random" elements of specified dtype:
a = np.empty(10, dtype=np.float)
a = np.empty(20, dtype=np.complex)

# `np.zeros` produces array filled by zeros of specified dtype:
a = np.zeros(10, dtype=np.complex)
assert_array_equal(a, 0)  # you can type `assert np.all(a == 0)` instead

# `np.ones` produces array filled by ones of specified dtype:
a = np.ones(10, dtype=np.uint16)
assert_array_equal(a, 1)

# `np.full` produces array filled by specified value:
x = 3 + 5j
a = np.full(10, x)
assert_array_equal(a, x)
assert np.issubdtype(a.dtype, np.complex)
x = set(range(10))
a = np.full(10, x)
assert_array_equal(a, x)
assert np.issubdtype(a.dtype, np.object)

# All of four last functions (`empty`, `zeros`, `ones`, `full`) have `*_like`
# companions that help produce array of the same size (better said shape, the
# `tuple` attribute described size of the multidimensional array along each axis,
# we will describe shapes soon) and dtype.
a = np.arange(10, dtype=np.uint32)
b = np.ones_like(a)
assert len(a) == len(b)
assert a.shape == b.shape
assert a.dtype == b.dtype
assert_array_equal(b, 1)
# dtype of new array can differ from original:
b = np.zeros_like(a, dtype=np.float)
assert a.shape == b.shape
assert a.dtype != b.dtype
assert_array_equal(b, 0)
x = np.pi
# pi will be rounded to 3, because dtype=np.uint32:
b = np.full_like(a, x)
assert a.shape == b.shape
assert a.dtype == b.dtype
assert np.all(b == np.floor(x))


# # Array view and slicing

# ## list-like indexing

# numpy arrays can be sliced just like built-in python sequenses: `list`, `str`
# or `tuple`:
a = np.arange(10)
x = 5
assert x == a[x]  # index and value of the `a` are the same
assert_array_equal(a[2:8], np.arange(2, 8))

# Instead of regular python behaviour, numpy such slices does not copy elements
# but produces new ndarray that is a view of the original one.
# First, let's remember list's behaviour:
li = list(range(10))
li_slice = li[:5]
li_slice[:] = [-1]*5  # replace all elements
assert_array_equal(li_slice, -1)
assert_array_equal(li[:5], list(range(5)))  # original list haven't changed
assert li[:5] != li_slice

# But, ndarray's behaviour is different:
a = np.arange(10)
a_slice = a[:5]
assert a_slice.shape == (5,)
a_slice[:] = -1  # we can broadcast single element to a whole array
assert_array_equal(a[:5], a_slice, -1)
# We can check that `a_slice` is just a view and doesn't own its elements:
assert not a_slice.flags.owndata
assert a.flags.owndata
# .base attribute for views provides access to original data for views and is
# None for ndarrays that owns their data:
assert a.base is None
assert_array_equal(a_slice.base, a)

# Index access of 1-D ndarray returns an element, not view
a = np.arange(10, dtype=np.int)
x = a[0]  # is a number, not view of `a`
x += 1
assert x != a[0]  # original array doesn't changed
assert x.flags.owndata
assert np.issubdtype(x.dtype, np.int)
assert x.shape == ()  # numpy's numbers have empty shape

# If you'd like to produce 1-element view then use slice:
b = a[0:1]  # is a view with one element
b[0] += 1
assert b[0] == a[0]  # original array changed
assert not b.flags.owndata
assert np.issubdtype(x.dtype, np.int)
assert b.shape == (1,)

# If you'd like to make view on all the array, than use empty slice ":":
a = np.arange(10, dtype=np.int)
b = np.zeros_like(a, dtype=np.float)
b[:] = a  # copies `a`'s elements into b and convert their type
assert_array_equal(a, b)
assert b.flags.owndata
assert np.issubdtype(b.dtype, np.float)
c = a[:]  # a view on all elements of `a`
assert_array_equal(b, c)
assert not c.flags.owndata
d = a  # another variable that holds the same object as a
assert a is d
assert_array_equal(c, d)
# all attributes of `d` is the same as for `a`, remember that they are the same
# object:
assert d.flags.owndata

# Elements of the array can be modified in-place using "+=", "*=", etc:
a = np.arange(10)
b = a
a += 1
assert a is b  # `a` still is the same object, compare with tuple/str behaviour
assert_array_equal(a, b)
assert_array_equal(b, np.arange(1, 11))

# But "+", "-", "*", etc create new objects:
a = np.arange(10)
b = a
a = a + 1  # `a` is replaced with the new object
assert a is not b
assert_array_equal(a, np.arange(1, 11))
assert_array_equal(b, np.arange(10))

# As was shown before, elements of an array can be changed via slices:
a = np.arange(10)
b = a
a[:] = 1
assert a is b
assert_array_equal(a, b)
assert_array_equal(b, 1)

a = np.ones(10)
a[::2] = 0
assert_array_equal(a, np.arange(10) % 2)

# You should avoid to iterate ndarray (e.g. in for-loop), because numpy
# benches operations over array's elements and make them much faster together
# than one by one.
for n in np.logspace(2, 6, 3, dtype=np.int):
    kwargs = {
        'number': 10,
        'setup': 'import numpy as np; a = np.zeros({}, dtype=np.int)'.format(n)
    }
    t_for = timeit(
        """for i in range(a.shape[0]):
            a[i] += 1
        """,
        **kwargs
    )
    t_bench = timeit(
        'a += 1',
        **kwargs
    )
    assert t_for > t_bench

# - Indexing array -

# ndarray can be indexed in some more ways than built-in python collections.
# One of these ways is indexing array: ndarray or list (but not tuple!) with
# integer elements that are used as indices of target array.
a = np.arange(10)
index = [5, 1, 3, 1, 2]
assert_array_equal(a[index], index)

# Indexing array copies data to new ndarray (see exception bellow):
a = np.arange(10)
a_copy = a.copy()
c = a[index]
c[:] = 0
assert_array_equal(a, a_copy)  # original array hasn't changed
# But indexing arrays can be used to change elements in-place:
a[index] += 1
assert not np.all(a == a_copy)  # a has been changed
# If indexing array has duplicate index then this index is changed only once
a = np.zeros(2)
a[[0, 0, 0, 0]] += 1
assert_array_equal(a, [1, 0])

# - Mask (boolean) index -

# One more type of index that doesn't work for built-in collections is mask (or
# boolean) index. This is a ndarray (or a list, not a tuple) of boolean
# elements: True means that element with the same index from target array will
# be included and vice versa:
a = np.arange(10)
index = (a % 2) == 0
b = a[index]
assert_array_equal(b, a[::2])

# Mask index works the same way as indexing array: it copies elements when it
# is in the "right" part of expression and allows in-place modification when it
# is in the "left":
a = np.arange(10) - 5
index = a < 0
assert np.any(index)  # some indices are False
b = a[index]
assert b.flags.owndata
a[index] = 0  # replace all negative elements by zero
assert np.all(a >= 0)
a[a > 0] = 0  # replace all positive elements by zero
assert_array_equal(a, 0)
