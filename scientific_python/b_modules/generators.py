#!/usr/bin/env python3

from __future__ import division, print_function, unicode_literals

import itertools


# # Some of built-in generators

# We have met some of built-in generators before, e.g. enumerate. Generators
# are iterable but, instead of sequences, generators don't hold their values
# but produce next value each time you ask them. After the last value is
# produced a generator raises exception when for more values.

# `for` loop
s = 'abc'
for i, x in enumerate(s):
    assert x == s[i]


# # `next()`

a = [5, 3]
enum = enumerate(a)
assert (0, 5) == next(enum)
assert (1, 3) == next(enum)
# enum is empty now
try:
    next(enum)
    assert False
except StopIteration:
    pass


# ## Generator expression

a = (x**2 for x in range(10))  # generator
for i, x in enumerate(a):
    assert i**2 == x

# Also this syntax is named list comprehensive
a = [x**2 for x in range(10)]
assert isinstance(a, list)
b = list(x**2 for x in range(10))
assert a == b

a = {x**2 for x in range(10)}  # set
assert isinstance(a, set)

a = {x: x**2 for x in range(10)}  # dict
assert isinstance(a, dict)
b = dict((x, x**2) for x in range(10))  # same dict
assert a == b

n = 10
s = sum(range(10))  # built-in that calculate sum of iterable's elements
assert (n - 1) * n / 2 == s
s = sum(x**2 for x in range(10))
assert (n - 1) * n * (2*n - 1) / 6 == s


# # Generator

# ## Short example

# Infinite generator from PEP 255:


def fib():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a+b


assert (1, 1, 2, 3, 5) == tuple(itertools.islice(fib(), 5))

# ## `yield` statement

# When you call for the next value of a generator, it works until `yield`
# statement and yields some value. When you need next value the generator
# remembers its state and continues just from the places it previously yields.
# Generator yields its values until the end of the block or until `return`
# statement.


def enumerate_first_elements(seq, n=10):
    i = 0
    for x in seq:
        yield i, x
        i += 1
        if i == n:
            return


n = 5
a = list(range(2*n))
first_n_enumerated_pairs = list(enumerate_first_elements(a, n=n))
assert len(first_n_enumerated_pairs) == n
assert first_n_enumerated_pairs[2] == (2, 2)
