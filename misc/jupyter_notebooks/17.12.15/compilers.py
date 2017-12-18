import numpy as np
import numba
import pyximport
pyximport.install(
    setup_args={'include_dirs': [np.get_include()]}
)
from cont_frac import golden_ratio as cy_golden_ratio
from cont_frac import cy_cont_frac
from cont_frac import square_erf
# from cont_frac import hello

@numba.jit
def golden_ratio(n=1000):
    c = 1
    for _ in range(n-1):
        c = 1 + 1/c
    return c

phi = 0.5 * (np.sqrt(5) + 1)
assert abs(phi - golden_ratio()) < 1e-6
assert abs(phi - cy_golden_ratio(1000)) < 1e-6
print(square_erf(0), square_erf(1), square_erf(np.inf))
#hello()

a = np.ones(1000, dtype=np.float64)
print(cy_cont_frac(a))