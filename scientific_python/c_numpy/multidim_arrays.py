#!/usr/bin/env python3

from __future__ import division

import numpy as np
from numpy.testing import assert_allclose, assert_array_equal

# This and another files in this subpackage are based on NumPy User Guide. The
# guide is really good and you can prefer it to my modules:
# https://docs.scipy.org/doc/numpy/user/basics.html

# We have talked about 1-D ndarrays in `arrays.py`. Read it before this file.


# # Creation

# ## `np.array`

# Usually np.array understands that nested list/tuple represents
# multidimensional array:
a = np.array([
    [1, 2, 3],
    [4, 5, 6],
])
assert a.ndim == 2
assert a.shape == (2, 3)
# ndarray.shape attribute contains sizes of the array throw its axes.

a = np.array([1, 2, 3], ndmin=2)
# Produced one additional dimension. Same as a = np.array([[1,2,3]])
assert a.ndim == 2
assert a.shape == (1, 3)
assert_array_equal(a, [[1, 2, 3]])
a = np.array([1, 2, 3], ndmin=10)
assert a.ndim == 10
assert a.shape == (1,)*9 + (3,)

# ## np.zeros, np.ones, etc

# All functions producing an `np.ndarray` object can accept a `tuple` with the
# shape of the array instead of integer:
shape = (2, 2, 2)
a = np.zeros(shape, dtype=np.complex)
assert a.shape == shape
assert a.ndim == len(shape)
assert a.size == np.product(shape)  # multiplies all elements


# # Reshaping

# ## `ndarray.reshape` and `np.reshape`

# You can produce a new view of the original array with the different shape:
a = np.arange(16)
square = a.reshape(4, 4)
assert square.shape == (4, 4)
assert not square.flags.owndata

# ## `ndarray.resize` and `ndarray.shape = ...`

# Also you can change the shape of current `ndarray` object, this will not
# affect data nor create new `ndarray` object.
a = np.arange(16)
assert a.ndim == 1
a.resize((4, 4))  # This returns None
assert a.ndim == 2
# The equivalent of ndarray.resize() is directly changing of `ndarray.shape`
# attribute:
a.shape = (2, 2, 2, 2)
assert a.ndim == 4

# Sometimes resizing of current ndarray object is impossible. This is an
# example from `np.reshape()` documentation:
a = np.zeros((10, 2))
# A transpose make the array non-contiguous
b = a.T
# Taking a view makes it possible to modify the shape without modifying
# the initial object.
c = b.view()
try:
    c.shape = (20)
    assert False
except AttributeError as e:
    assert str(e) == 'incompatible shape for a non-contiguous array'

# ## Smart reshaping

# You can use special value "-1" for a dimension size which you wouldn't like
# to calculate manually:
a = np.arange(16)
assert a.shape == (16,)
b = a.reshape(4, -1)
assert b.shape == (4, 4)
c = b.reshape(2, -1, 2)
assert c.shape == (2, 4, 2)
d = c.reshape(-1)
assert d.shape == (16,)

# Of course, this special value can be used only once:
try:
    d.reshape(-1, -1)
    assert False
except ValueError as e:
    assert str(e) == 'can only specify one unknown dimension'


# # Indexing

# ## Simple indexing

# Remember that simple indexing always returns a view on original array and
# does not copy data.

a = np.array([
    [1, 2, 3],
    [4, 5, 6],
])
a_0 = a[0]    # For n-D array one index returns a view
assert not a_0.flags.owndata
assert a_0.ndim == 1
assert_array_equal(a[0], [1, 2, 3])
a_02 = a[0][2]  # a_0 is 1-D array, so we can get its elements by index

# A more numpyish way to take several indexes is using comma-separated index:
assert a[0, 2] == a[0][2]
# It is more flexible, and provides possibility to use slices not only for the
# last axis:
assert_array_equal(a[0][0:2], a[0, 0:2])
# but:
assert a[0:2, 1].shape != a[0:2][1].shape

# Example: getting the first column of 2-D array `a`:
assert_array_equal(a[:, 0], [1, 4])


# ## `np.newaxis`

# You can produce new unity sized axis using special index `np.newaxis`:
a = np.array([1, 2, 3])
b = a[1, np.newaxis]  # [2]
assert b.shape == (1,)
assert b[0] == a[1]


# ## Ellipsis

# `...` expression can be used as replacement of several `:` expressions:
a = np.arange(32).reshape((2,)*5)
assert a.ndim == 5
assert_array_equal(a.shape, np.full(5, 2))
assert_array_equal(a[1, :, :, :, 0], a[1, ..., 0])


# ## `tuple` object as an index

# If you would like to form index before usage then you can do it with `tuple`
a = np.arange(16).reshape(4, 4)
index = (2, 2)
assert a[index] == a[2, 2] == a[(2, 2)]

# Be careful and remember that a `list` index is an indexing array and operates
# in the different way then `tuple` index:
assert a[[2, 2]].size > 1
assert a[(2, 2)].ndim != a[[2, 2]].ndim

# Index `tuple` can contain not only integers but some special built-in objects
# such as a `slice` or an `Ellipsis`:
a.shape = (2,)*4
index = (1, Ellipsis)
assert_array_equal(a[index], a[1, ...])

a.shape = 2, 8
index = (0, slice(1, None, 2))
assert_array_equal(a[index], a[0, 1::2])

# `np.s_` and `np.index_exp` are so-called index tricks. `numpy` index tricks
# are used as indexed objects but don't hold any data and acts similar to
# functions. Examples from `np.s_` documentation:
assert np.s_[2::2] == slice(2, None, 2)
assert np.s_[2::2, :] == (slice(2, None, 2), slice(None))
assert_array_equal(np.array([0, 1, 2, 3, 4])[np.s_[2::2]], [2, 4])
# The only difference between them is that np.index_exp always returns a
# `tuple`:
ie = np.index_exp[2::2]
assert isinstance(ie, tuple)
assert ie == (np.s_[2::2],)
assert np.index_exp[2::2, :] == np.s_[2::2, :]

# ## `np.ndenumerate`

# Built-in enumerate generator can be used for iterating over only the first
# axis:
a = np.array([[1, 2, 3], [4, 5, 6]])
ii = 0
for i, x in enumerate(a):
    assert i == ii  # i is an integer
    assert_array_equal(x, a[i])
    assert x.ndim == 1  # x is a 1-D array, not a number!
    assert x.shape == (3,)
    ii += 1
# `np.ndenumerate` provides iterating over all elements of multidimensional
# array:
for i, x in np.ndenumerate(a):
    assert isinstance(i, tuple)
    assert len(i) == a.ndim
    assert x.shape == ()  # x is a `numpy` number, not an array
    assert x.ndim == 0

# `numpy` provides another useful generators, for example a multidimensional
# equivalent of `range` built-in np.ndindex:
shape = (3, 2)
a = []
for i in np.ndindex(shape):  # (0,0), (0,1), (1,0), (1,1), (2,0), (2,1)
    assert isinstance(i, tuple)
    assert len(i) == len(shape)
    a.append(i)
a = np.array(a)
b = []
for i in range(shape[0]):
    for j in range(shape[1]):
        b.append([i, j])
assert_array_equal(a, b)


# # Stacks and splits

# Remember that `ndarray` objects have constant size and every array join or
# split copies data to the new object.

a = np.arange(0, 4).reshape(2, 2)
b = np.arange(4, 8).reshape(2, 2)
c = np.arange(8, 12).reshape(2, 2)

# ## np.concatenate
# Stack over the first axis (vertical stack for 2-D array)
v = np.concatenate((a, b, c))  # equivalent to deprecated np.vstack
assert_array_equal(v, np.arange(12).reshape(6, 2))
# Stack over the second axis (horizontal stack for 2-D array)
h = np.concatenate((a.T, b.T, c.T), axis=1)  # same as deprecated np.hstack
assert_array_equal(
    h,
    np.concatenate((
        np.arange(0, 12, 2).reshape(1, -1),
        np.arange(1, 12, 2).reshape(1, -1)
    ))
)

# ## `np.r_`

# `np.r_` is a so-called index trick: it provides ndarray creation interface
# throw its index.
# Default `np.r_` behaviour is equal to `np.concatenate(tuple, axis=0)`:
assert_array_equal(
    np.r_[a, b, c],
    np.concatenate((a, b, c))
)
assert_array_equal(
    np.r_[
        0:10,           # range
        0:1:5j,         # NB "j", it used to produce linspace instead of range
        a.reshape(-1),  # ndarray
        [3]*4           # list
    ],
    np.concatenate((
        np.arange(0, 10),
        np.linspace(0, 1, 5),
        a.reshape(-1),
        np.full(4, 3)
    ))
)

# Axis to concatenate along can be specified as a string:
assert_array_equal(
    np.r_['1', a, b, c],
    np.concatenate((a, b, c), axis=1)
)

# ## `np.stack`

# np.stack joins arrays throw new axis
s = np.stack((a, b, c))
assert s.shape == (3, 2, 2)
assert_array_equal(
    s,
    np.r_[a, b, c].reshape(-1, 2, 2)
)

# ## `np.column_stack`

# This function always produces 2-D array
x = np.column_stack((np.zeros(5), np.arange(5)))
assert x.shape == (5, 2)
x = np.column_stack(([[1, 2, 3], [3, 2, 1]], np.arange(6).reshape(2, -1)))
assert x.shape == (2, 6)

# ## `np.mgrid`

# np.mgrid is used to produce  a stack of `ndarray` objects with specified
# shape filled by identical 1-D arrays stacked over different shapes. An
# example:
grid = np.mgrid[0:2, 0:3]
assert grid.shape == (2, 2, 3)
X, Y = grid
assert_array_equal(
    X,
    [[0, 0, 0], [1, 1, 1]]
)
assert_array_equal(
    Y,
    [[0, 1, 2], [0, 1, 2]]
)

# 1-D `mgrid` is the same as `np.r_`:
assert_array_equal(np.mgrid[0:10], np.r_[0:10])
assert_array_equal(np.mgrid[0:2:5j], np.r_[0:2:5j])

# `mgrid` is useful in work with n-D distributions or functions. For example,
# 2-D normal distribution in square [-1..1]x[-1..1] can be produced in this
# way:
n = 11
sl = np.s_[-1:1:n*1j]
X, Y = np.mgrid[sl, sl]
Z = np.exp(-(X**2+Y**2)/0.5)
# Check distribution throw Ox and Oy axes and their bisector
assert_allclose(Z[n//2, :], np.exp(-np.r_[sl]**2/0.5))
assert_allclose(Z[:, n//2], Z[n//2, :])
assert_allclose(
    Z.diagonal(),
    np.exp(-np.linspace(-np.sqrt(X[0, 0]**2+Y[0, 0]**2),
                        np.sqrt(X[-1, -1]**2+Y[-1, -1]**2),
                        n)**2 / 0.5)
)

# ## `np.split`

# `np.split` produces a `list` of an array pieces

v = np.concatenate((a, b, c))
a1, b1, c1 = np.split(v, 3)
assert_array_equal(a, a1)
assert_array_equal(b, b1)
assert_array_equal(c, c1)

# See also `np.array_split`
