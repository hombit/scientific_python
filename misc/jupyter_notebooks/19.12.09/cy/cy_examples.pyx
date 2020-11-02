# cython: language_level = 3
# distutils: language = c++

import numpy as np

cimport cython
cimport numpy as cnp


cdef extern from 'autoreg.hpp':
    int autoreg(double, size_t, double*)

    
@cython.boundscheck(False)
cdef double c_contfrac(cnp.ndarray[double, ndim=1] a):
    cdef double[:] a_view = a
    cdef double c = 1.0 / a_view[-1]
    cdef Py_ssize_t i
    cdef Py_ssize_t length = a.shape[0]
    for i in range(length - 1, 0, -1):
        c = a_view[i] + 1.0 / c
    return c


def cython_contfrac(a):
    return c_contfrac(np.asarray(a, dtype=np.float64))


cdef cnp.ndarray[double, ndim=1] c_autoreg(double a, size_t n):
    cdef cnp.ndarray[double, ndim=1] x = np.empty(n, dtype=np.float64)
    cdef double[:] x_view = x
    autoreg(a, n, &x_view[0])
    return x


def cython_autoreg(a, n):
    return c_autoreg(a, n)