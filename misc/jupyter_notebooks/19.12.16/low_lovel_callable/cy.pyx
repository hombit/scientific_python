# cython: language_level = 3
# distutils: language = c++


from libc.math cimport sin, isinf


cdef double cython_func(double x):
    if x == 0.0:
        return 1.0
    if isinf(x):
        return 0.0
    return sin(x) / x