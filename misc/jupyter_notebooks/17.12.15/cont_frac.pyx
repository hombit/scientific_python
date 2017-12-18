from libc.math cimport erf
cimport numpy as np

cdef double cy_square_erf(double x):
    cdef double e = erf(x)
    return e*e

def square_erf(double x):
    return cy_square_erf(x)

def cy_cont_frac(np.ndarray[np.float64_t, ndim=1] a):
    cdef np.float64_t c = 1.0 / a[-1]
    for i in range(len(a)-2, -1, -1):
        c = a[i] + 1.0/c
    return c

def golden_ratio(int n):
    cdef double c = 1
    for _ in range(n-1):
        c = 1 + 1/c
    return c

#cdef extern from "hello.c":
#    void hello_world()

#def hello():
#    hello_world()