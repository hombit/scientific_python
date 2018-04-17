#!/usr/bin/env python3

# This file contains examples of usage of scipy.integrate module

from __future__ import division

import numpy as np
from numpy.testing import assert_allclose
from scipy import integrate


# -- quad --

# `quad` integrates numerically 1-D functions

# - Integral of sinus arc -

a, b = 0, np.pi
integral, error = integrate.quad(np.sin, a, b)
assert_allclose(-np.cos(b) + np.cos(a), integral, rtol=0, atol=error)

# - Gaussian integral -

integral, error = integrate.quad(
    lambda x: np.exp(-x**2),
    -np.inf, np.inf
)
assert_allclose(np.sqrt(np.pi), integral, rtol=0, atol=error)


# -- odeint --

# `odeint` integrates 1-D linear ordinary differential equation systems. Its
# first argument is a function that gets current values of unknowns and
# independent variable. Other words odeint solves the problem
# `dy/dt = f(y, t, ...)` where `y` is a vector function and `t` is an
# independent variable. The second argument is a vector of initial conditions
# and the third is a grid where function values will be found.

# - Harmonic oscillator -

# The problem is $d/dt(dx/ddt) + omega^2 x = 0, x(t=0) = 0, dx/dt(t=0)=1$ with
# the solution x = sin(omega t) / omega, dx/dt = cos(omega t).
# Let's transform it too the ODE, than let `y[0]` is `x` and `y[1]` is $dx/dt$,
# than $dy[0]/dt = y[1]$ and $dy[1]/dt = -omega^2 y[0]$. In the vector form
# $dy/dt = [y[1], -k y[0]]$ with initial condition [0, 1].

t = np.linspace(0., 1., 10)
omega = 2*np.pi
rtol = 1e-6  # Estimate of relative error of `y`
atol = 1e-6  # Estimate of absolute error of `y`
# Total error is `rtol * abs(y) + atol`
y = integrate.odeint(
    lambda y, t: [y[1], -omega**2 * y[0]],  # dy/dt
    [0, 1],  # y(t=t[0]) - initial condition
    t,
    rtol=rtol,
    atol=atol
)
assert_allclose(
    np.stack((np.sin(omega * t) / omega, np.cos(omega * t)), axis=1),
    y,
    rtol=10 * rtol,  # estimate errors are not good enough
    atol=10 * atol
)
