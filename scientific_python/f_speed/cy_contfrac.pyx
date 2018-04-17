cimport numpy as np
cimport cython


def contfrac(np.ndarray[np.float64_t, ndim=1] a):
    cdef np.float64_t c = 1.0 / a[-1]
    for i in range(len(a)-2, -1, -1):
        c = a[i] + 1.0/c
    return c
