#!/usr/bin/env python3

# This file contains examples of usage of scipy.optimize module

from __future__ import division

import numpy as np
from numpy.testing import assert_allclose
from scipy import optimize


# -- root --

# `root` is a function that solves a vector equation f(x) = 0. It providing
# interface to various root-finding methods. All of them perfroms numerical
# iteration, so `root` needs an initial approach to a solution.

# - 1-D example -

def parabola(x):
    """Equation with a solution of +-sqrt(2)"""
    return x**2 - 2


result = optimize.root(parabola, 1)  # 1 is an initial guess
assert isinstance(result, optimize.OptimizeResult)
assert result.success
assert_allclose(np.sqrt(2), result.x[0])  # .x is an array even in 1-D case

# In some cases the optimization will not be success:
# Using the default method (at least for scipy v. 1.0):
result = optimize.root(parabola, 0, method='hybr')
assert not result.success

# The optimization can be speeded up by providing Jacobian of the function:


def parabola_jac(x):
    """Jacobian of parabola()"""
    return 2*x


result_w_jac = optimize.root(parabola, 1e-5, jac=parabola_jac, tol=1e-9)
assert result_w_jac.success
result_wo_jac = optimize.root(parabola, 1e-5, tol=1e-9)
assert result_wo_jac.success
assert_allclose(result_wo_jac.x[0], result_w_jac.x[0])
# Compare number of function calls:
assert result_w_jac.nfev < result_wo_jac.nfev
# But call of Jacobian also takes some time!
assert result_w_jac.nfev + result_w_jac.njev < result_wo_jac.nfev

# - 2-D example -

# Let's find a solution of an equation $x^2 + bx + c = 0$. Of course, the right
# way to do it is using of polynomial root finding algorithm, but think about
# it as an simple example.
# Vieta's formulas give $x_0 + x_1 = -b$ and $x_0 x_1 = c$:


def vieta(x, b, c):
    return [x[0] + x[1] + b,
            x[0] * x[1] - c]


def vieta_jac(x, b, c):
    return [
        [1,    1],
        [x[1], x[0]]
    ]


b, c = -1, -1
result = optimize.root(vieta, [0, 1], args=(b, c), jac=vieta_jac)
assert result.success
# `numpy.roots(p)` provides roots of polynomial
# `p[0] * x**(len(p)-1) + p[1] * x**(len(p) - 2) ... + p[-1]`:
roots = np.roots((1, b, c))
assert_allclose(np.sort(roots), np.sort(result.x))


# -- minimize --

# `minimize` provides a common interface to a collection of minimization
# methods. See `lmfit` package that provides prettier interface to augmented
# collection of methods: https://lmfit.github.io/lmfit-py/


# - Multivariate function -


def func(x, a, b):
    """Negative Gaussian function with argument a*x+b and sigma=10"""
    y = np.dot(a, x) + b
    return -np.exp(-np.sum(np.square(y))/200)


a = np.array([[1, 2, 3], [1, 1, 1], [0, 0, 1]])
b = np.array([3, 2, 1])
result = optimize.minimize(func, np.ones_like(b), args=(a, b))
assert result.success
x = np.linalg.solve(a, -b)
assert_allclose(x, result.x, rtol=1e-3)

# - Various optimization problems -

# A lot of optimization problems can be solved using machine learning methods.
# Our days there are a lot of machine learning libraries and frameworks, e.g.
# see `scikit-learn` and `TensorFlow`:
# http://scikit-learn.org
# https://www.tensorflow.org

# # Here we solve a simple problem of cluster analysis using the most simple
# # approach. Let's consider that we have two comparable sets of objects in
# # N-dimensional space and we search the best separating hyperplane between
# # them.
# from scipy.stats import multivariate_normal as m_normal
# mean1 = np.array([1,  2,3])
# mean2 = np.array([-3,-3,5])
# cov1 = np.diag([1.5, 2.0, 2.5])
# cov2 = np.array([
#     [ 1.0, -0.3, 0.3],
#     [-0.3,  2.5, 0.3],
#     [ 0.3, -0.3, 3.0],
# ])
# size = 100
# random_state = np.random.RandomState(13)  # Lucky number
# y1 = m_normal.rvs(mean=mean1, cov=cov1, random_state=random_state)
# y2 = m_normal.rvs(mean=mean2, cov=cov2, random_state=random_state)
