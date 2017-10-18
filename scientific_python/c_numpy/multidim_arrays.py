#!/usr/bin/env python3

from __future__ import division, print_function, unicode_literals

import numpy as np
from numpy.testing import assert_almost_equal, assert_array_equal

# This and another files in this subpackage are based on NumPy User Guide. The
# guide is really good and you can prefer it to my modules:
# https://docs.scipy.org/doc/numpy/user/basics.html

# We have talked about 1-D ndarrays in `arrays.py`. Read it before this file.



### Creation ###

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

a = np.array([1,2,3], ndmin=2)
# Produced one additional dimension. Same as a = np.array([[1,2,3]])
assert a.ndim == 2
assert a.shape == (1, 3)
assert_array_equal(a, [[1,2,3]])
a = np.array([1,2,3], ndmin=10)
assert a.ndim == 10
assert a.shape == (1,)*9 + (3,)

## np.zeros, np.ones, etc ##

# All functions producing ndarrays can accept tuple with the shape of the array
# instead of alone integer:

shape = (2, 2, 2)
a = np.zeros(shape, dtype=np.complex)
assert a.shape == shape
assert a.ndim == len(shape)
assert a.size == np.product(shape)  # same as np.prod, multiplies all elements



### Reshaping ###

## ndarray.reshape (np.reshape) ##

# You can produce a new view of the original array with the different shape:
a = np.arange(16)
square = a.reshape(4,4)
assert square.shape == (4,4)
assert not square.flags.owndata

## ndarray.resize (ndarray.shape = ...) ##

# Also you can change the shape of current ndarray object, this will not affect
# data nor create new ndarray object.
a = np.arange(16)
assert a.ndim == 1
a.resize((4,4))  # This returns None
assert a.ndim == 2
# The equivalent of ndarray.resize() is directly changing of `ndarray.shape`
# attribute:
a.shape = (2,2,2,2)
assert a.ndim == 4

# Sometimes resizing of current ndarray object is impossible. This is an 
# example from np.reshape() documentation:
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

## Smart reshaping ##

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

# Of course this special value can be used only once:
try:
    d.reshape(-1, -1)
    assert False
except ValueError as e:
    assert str(e) == 'can only specify one unknown dimension'



### Indexing ###

## Simple indexing ##

# Remember that simple indexing always returns a view on original array and
# does not copy data.

a = np.array([
    [1,2,3],
    [4,5,6],
])
a_0 = a[0]    # For n-D array one index returns view
assert not a_0.flags.owndata
assert a_0.ndim == 1
assert_array_equal(a[0], [1,2,3])
a_02 = a[0][2]  # a_0 is 1-D ndarray, so we can get its elements by index

# A more numpyish way to take several indexes is using comma-separated index:
assert a[0,2] == a[0][2]
# It is more flexible, and provides possibility to use slices not only for the
# last axis:
assert np.all(a[0][0:2] == a[0,0:2])
# but:
assert not np.all(a[0:2,1] == a[0:2][1])

# Example: getting the first column of 2-D array `a`:
assert_array_equal(a[:,0], [1,4])


## np.newaxis ##

# You can produce new length of one axis using special index np.newaxis:
a = np.array([1,2,3])
b = a[1,np.newaxis]  # [2]
assert b.shape == (1,)
assert b[0] == a[1]


## Ellipsis ##

# "..." expression can be used as replacement of numerical ":" expressions:
a = np.arange(32).reshape((2,)*5)
assert a.ndim == 5
assert_array_equal(a.shape, np.full(5, 2))
assert_array_equal(a[1,:,:,:,0], a[1,...,0])


## `tuple` object as an index ##

# If you would like to form index before usage then you can do it using tuple.
a = np.arange(16).reshape(4,4)
index = (2, 2)
assert a[index] == a[2,2] == a[(2, 2)]

# Be careful and remember that a list index is an indexing array and operates
# in the different way then tuple!
assert a[[2,2]].size > 1
assert not np.all(a[(2,2)] == a[[2,2]])

# Index tuple can contain not only integers but some special built-in objects 
# as slice or Ellipsis:
a.shape = (2,)*4
index = (1, Ellipsis)
assert_array_equal(a[index], a[1,...])

a.shape = 2, 8
index = (0, slice(2,6,2))
assert_array_equal(a[index], a[0,2:6:2])


## np.ndenumerate ##

# Built-in enumerate generator can be used for iterating over only the first
# axis:
a = np.array([[1,2,3],[4,5,6]])
ii = 0
for i, x in enumerate(a):
    assert i == ii  # i is an integer
    assert_array_equal(x, a[i])
    assert x.ndim == 1  # x is a 1-D array, not a number!
    assert x.shape == (3,)
    ii += 1
# np.ndenumerate provides iterating over all elements of multidimensional
# array:
for i, x in np.ndenumerate(a):
    assert isinstance(i, tuple)
    assert len(i) == a.ndim
    assert x.shape == ()  # x is a numpy number, not an array
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
        b.append([i,j])
assert_array_equal(a, b)
