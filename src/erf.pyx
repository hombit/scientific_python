from libc cimport math

def erf(float x):
    return math.erf(x)

def erfc(float x):
    return math.erfc(x)
