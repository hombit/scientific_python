#!/usr/bin/env python3

# This file contains examples of usage of scipy.interpolate module

from __future__ import division

from distutils.version import LooseVersion

import numpy as np
from numpy.testing import assert_allclose
import scipy
from scipy import interpolate

if __package__:
    from .utils import ssd
else:
    from utils import ssd


# -- interp1d --

# `interp1d` provides a common interface to spline interpolation and returns
# interpolation function.


def func(x):
    """target function"""
    return np.sin(2.*np.pi * x)


# Values to interpolate:
x_ = np.linspace(0, 1, 11)
y_ = func(x_)

linear_spline_func = interpolate.interp1d(x_, y_, kind='linear')
cubic_spline_func = interpolate.interp1d(x_, y_, kind='cubic')

grid = np.linspace(0, 1, 1001)  # interpolated points
true_y = func(grid)  # real values of function
# Interpolated values:
linear_y = linear_spline_func(grid)
cubic_y = cubic_spline_func(grid)

# Sums of square differences (SSD):
linear_ssd = ssd(true_y, linear_y)
cubic_ssd = ssd(true_y, cubic_y)

assert linear_ssd > cubic_ssd  # cubic spline is better!


# -- Spline classes --

# `scipy.interpolate` contains another interface to splines - special `*Spline`
# classes.
# Some of these classes appears only in last releases of `scipy` (2016-2017).
if LooseVersion(scipy.__version__) >= LooseVersion('0.19.0'):
    def func(x):
        """Target function"""
        return np.exp(-x**2)

    def dfunc(x):
        """Derivative of func"""
        return -2 * x * func(x)

    def d2func(x):
        """Second derivative of func"""
        return 2 * func(x) * (2*x**2 - 1)

    def ifunc(x):
        """Integral of func, ifunc(-inf) = 0"""
        from scipy.special import erf
        return np.sqrt(np.pi) / 2 * (erf(x) + 1)

    x_ = np.linspace(-2, 2, 11)
    y_ = func(x_)
    grid = np.linspace(x_[0], x_[-1], 1001)

# - CubicSpline -
    cubic_spline = interpolate.CubicSpline(x_, y_)  # returns a callable object
    cubic_interp1d = interpolate.interp1d(x_, y_, kind=3)  # kind='cubic'
    assert_allclose(cubic_spline(grid), cubic_interp1d(grid))

# Instead of `interp1d` return value CubicSpline instance has some useful
# methods.

# - Derivative spline -
    d_cubic_spline = cubic_spline.derivative()
    # Compare with actual derivative on the original interpolation points:
    assert_allclose(dfunc(x_), d_cubic_spline(x_), rtol=0.01, atol=0.01)

    # Second derivative, this should be more accurate than
    # `d_cubic_spline.derivative()`:
    d2_cubic_spline = cubic_spline.derivative(2)
    # Second derivative has worse quality:
    assert_allclose(d2func(x_), d2_cubic_spline(x_), rtol=0.1, atol=0.1)

    # Antiderivative is an integral that equals zero on the left border of
    # interpolated grid:
    i_cubic_spline = cubic_spline.derivative(-1)
    assert_allclose(0, i_cubic_spline(i_cubic_spline.x[0]))
    assert_allclose(
        ifunc(x_) - ifunc(i_cubic_spline.x[0]),
        i_cubic_spline(x_),
        rtol=1e-3, atol=1e-3
    )  # Numerical integration is always more accurate than differentiation

# - Definite integral -
    # Definite integral can be obtained directly from original spline:
    a, b = cubic_spline.x[[2, -2]]
    assert_allclose(
        ifunc(b) - ifunc(a),
        cubic_spline.integrate(a, b),
        rtol=1e-3,
        atol=1e-3
    )
    # Use it instead of `scipy.integrate.quad` of cubic_spline or instead of
    # creation and executing antiderivative spline to obtain only one definite
    # integral.

# - BSpline -
    # `BSpline` provides interface similar to `CubicSpline`, for details see
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.BSpline.html
    # https://en.wikipedia.org/wiki/B-spline
    # TODO: write examples

# - Akima spline -
    # `Akima1DInterpolator` provides interface similar to `CubicSpline`. Akima
    # spline is a special case of the cubic splines that works more accurate
    # when data has gaps.
    def step_func(x):
        return np.sign(x)

    x_step = np.r_[-1:0:0.01, 0.01:1.01:0.01]  # from -1 to 1 without zero
    y_step = step_func(x_step)  # minus ones and ones

    cubic_spl_step = interpolate.CubicSpline(x_step, y_step)
    akima_spl_step = interpolate.Akima1DInterpolator(x_step, y_step)

    grid_step = np.linspace(x_step[0], x_step[-1], 1001)
    cubic_step_ssd = ssd(step_func(grid_step), cubic_spl_step(grid_step))
    akima_step_ssd = ssd(step_func(grid_step), akima_spl_step(grid_step))
    # Akima is better:
    assert cubic_step_ssd > akima_step_ssd

# - Smooth spline -
    # `UnivariateSpline` provides smooth splines.
    # Let's generate some noisy data:
    random_state = np.random.RandomState(777)  # lucky number
    y_noisy = y_ + random_state.normal(scale=0.1, size=y_.shape)

    # Interpolate it with cubic spline and smooth cubic spline:
    cubic_spl_noisy = interpolate.CubicSpline(x_, y_noisy)
    # s is a smooth factor
    smooth_spl = interpolate.UnivariateSpline(x_, y_noisy, k=3, s=0.1)

    # Which spline is closer to original distribution without noise?
    cubic_noisy_ssd = ssd(func(grid), cubic_spl_noisy(grid))
    smooth_ssd = ssd(func(grid), smooth_spl(grid))
    assert cubic_noisy_ssd > smooth_ssd  # we are lucky!
    # Of course, any of these splines can be closer to original distribution,
    # it depends on noise and smooth factor.

    # Smooth spline is smoother!
    assert (
        np.max(np.abs(cubic_spl_noisy.derivative()(grid)))
        > np.max(np.abs(smooth_spl.derivative()(grid)))
    )
